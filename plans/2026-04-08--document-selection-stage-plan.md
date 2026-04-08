# Document-selection retrieval plan

- Worktree: `.worktrees/document-selection-plan`
- Branch: `feature/document-selection-plan`
- Date: 2026-04-05

## Goal

Add a document-selection stage before chunk retrieval:

1. build a document-level representation from document title plus high-signal sections such as objective, scope, intro, and a TOC field containing top-level sections with their subsections
2. embed and index that representation in FAISS
3. query the document index first to get top-`d` documents
4. run chunk retrieval only inside those documents
5. expose this through the CLI and the answer pipeline
6. add section-aware expansion, then optional common-parent expansion

---

## What I found

### Current implementation already has some useful building blocks

- `src/commands/store.py`
  - stores chunk embeddings in `VectorStore`
  - stores section-title embeddings in `TitleVectorStore`
- `src/extraction/html.py`
  - already extracts a section tree
  - already stores `containing_section_id` on chunks
  - already builds `section_closure` rows
- `src/retrieval/title_retrieval.py`
  - already shows the pattern of: vector hit -> relational expansion -> chunk list
  - already contains a section-expansion concept, because a matched title expands to descendant chunks
- `src/commands/answer.py`
  - still contains duplicated chunk retrieval and expansion logic already duplicated in `src/commands/query.py`

### Gaps relative to the new requirement

- there is **no document-level retrieval representation** yet
- there is **no document FAISS index** yet
- there is **no `query-documents` CLI command** yet
- there is **no `retrieve` CLI command** yet
- `answer --retrieval-mode` only supports `text|titles`
- current general retrieval expansion only does:
  - neighbor expansion via `--expand`
  - full-document expansion via `--full-doc-threshold`
- section expansion exists in `query-titles`, but it is **not extracted into a shared retrieval/expansion layer**
- there is **no common-parent expansion**

---

## Recommended design

Use the existing three-level structure that is emerging in the codebase:

1. **document level**: pick the best candidate documents
2. **chunk level**: run similarity search only within those documents
3. **section level**: expand selected chunks to their containing section, then optionally to a common parent

Keep the answer pipeline thin by moving retrieval into shared services and making CLI commands format the same retrieval result.

---

## Step A — Expand `store` so it builds and indexes a document-level representation

### A1. Extend the existing document metadata model/table

Do **not** add a separate document-profile table.

Instead, extend the existing document model and `documents` table with the source-derived fields that make up the document-level representation.

Recommended shape in `src/models/document.py` / `documents`:

- `doc_uid: str`
- `source_type: str`
- `source_title: str`
- `source_url: str | None`
- `canonical_url: str | None`
- `captured_at: str | None`
- `background_text: str | None`
- `issue_text: str | None`
- `objective_text: str | None`
- `scope_text: str | None`
- `intro_text: str | None`
- `toc_text: str | None` for the document-representation component labeled `TOC`
- `created_at: str | None`
- `updated_at: str | None`

The important constraint is:

- keep the representation fields as persisted **source-derived data** on `documents`
- do **not** persist `embedding_text`
- do **not** persist an `algorithm_version`

The embedding input text should be built transiently from the stored document fields when `store` updates the document FAISS index.

### A2. Build a deterministic document-representation builder

Add a class such as:

- `src/retrieval/document_profile_builder.py`

Inputs:

- `DocumentRecord`
- extracted `sections`
- extracted `chunks`

Its job should be twofold:

1. populate the new persisted fields on `DocumentRecord`
2. build a transient embedding input string from those fields for the document vector store

For HTML documents, build the representation from:

1. `Title:` from `document.source_title`
2. `Background:` from chunks under a section whose normalized title is `background`
3. `Issue:` from chunks under a section whose normalized title is `issue`
4. `Objective:` from chunks under a section whose normalized title is `objective`
5. `Scope:` from chunks under a section whose normalized title is `scope`
6. `Introduction:` from the first high-level introductory content when available
7. `TOC:` containing the text for all top-level sections and their subsections

Recommended heuristics:

- normalize section titles to lower-case for matching
- preserve the additional IFRIC/SIC handling that has already been added
- exact preferred matches first:
  - `background`
  - `issue`
  - `objective`
  - `scope`
  - `introduction`
- if a section exists, pull descendant chunks via `section_closure`
- build `TOC` by iterating all top-level sections and concatenating each top-level section's title plus the text from that section and its subsection descendants
- cap each extracted part by character budget so the final embedding input stays compact
- build the transient embedding input as labeled text, for example:
  - `Title: ...`
  - `Background: ...`
  - `Issue: ...`
  - `Objective: ...`
  - `Scope: ...`
  - `Introduction: ...`
  - `TOC: ...`
- if one of the target parts is missing, just omit it
- if all targeted parts are missing, fail the ingestion

For PDF documents, start with a simple fallback:

- title
- first N chunks up to a small budget

That keeps the feature usable for PDFs without blocking on a richer PDF section extractor for now.

### A3. Add a document FAISS index

Add a new vector-store path for one vector per document.

Recommended implementation:

- add a small shared FAISS helper extracted from `src/vector/store.py` and `src/vector/title_store.py`
- add `src/vector/document_store.py` as a thin wrapper over that helper

Document id map payload should be:

- `(doc_uid, doc_uid)` or just `doc_uid`

### A4. Update `StoreCommand`

Extend `StoreDependencies` with a document vector store.

`store` should now:

1. extract chunks and sections
2. build the document representation and update the enriched `DocumentRecord`
3. persist chunks, sections, and the updated document row
4. build/update chunk embeddings
5. build/update title embeddings
6. build/update document embeddings from the transient embedding input built off the document row

### A5. Update skip-if-unchanged logic

Today `store` skips when chunk payloads and section payloads are unchanged.

Update that to also compare the document-representation payload persisted on the document row:

- title/background/issue/objective/scope/intro/TOC parts
- any additional IFRIC/SIC-oriented fields already added

That way changes to the document representation alone will still rebuild the document index.

### A6. Update store output

Keep the output concise but mention the new artifact.

Example:

- `Stored 428 chunks, 73 sections, updated document representation fields, 428 chunk embeddings, 73 title embeddings, and 1 document embedding for doc_uid=ifrs9`

---

## Step B — Implement `query-documents`

Add a new CLI command:

- `query-documents`

### B1. CLI shape

- reads query text from stdin
- add `-d/--d`
- add `--json`
- add `--min-score`

### B2. Behavior

- query the document FAISS index
- return the top `d` matching documents above threshold
- fetch the enriched `documents` rows for formatting

### B3. Output

Make the output similar to `query`.

Verbose output should include at least:

- score
- document UID
- source title
- short profile snippet

JSON output should include at least:

- `doc_uid`
- `source_title`
- `background_text`
- `issue_text`
- `objective_text`
- `scope_text`
- `intro_text`
- `TOC`
- the additional IFRIC/SIC-oriented document fields that are persisted
- `score`

If a preview of the document representation is useful in output, build it transiently from the document row instead of persisting `embedding_text`.

### B4. Shared service

Implement the actual search in a reusable service, e.g.:

- `src/retrieval/document_retrieval.py`

So `query-documents` is just a formatter, not a second retrieval implementation.

---

## Step C — Add `retrieve` and extract retrieval out of `answer`

This is the highest-leverage refactor in the requirement.

### C1. Introduce a shared retrieval pipeline

Add shared retrieval modules, for example:

- `src/retrieval/models.py`
- `src/retrieval/pipeline.py`
- `src/retrieval/expansion.py`

Recommended typed outputs:

- `DocumentHit`
- `ChunkHit`
- `RetrievalResult`
- `RetrievalRequest`

`RetrievalResult` should carry enough information for all three consumers:

- `query`
- `retrieve`
- `answer`

At minimum it should include:

- selected document hits
- selected chunk hits
- fetched chunk objects in final prompt order
- retrieved document UIDs
- expansion metadata for debugging

### C2. Add `retrieve` CLI

Add a new CLI command:

- `retrieve`

It should run the shared retrieval pipeline only and format the result as text or JSON.

Recommended options:

- `-k/--k`
- `--d`
- `--doc-min-score`
- `--content-min-score`
- `-e/--expand`
- `-f/--full-doc-threshold`
- `--retrieval-mode`
- `--json`
- `--expand-to-section`
- `--expand-common-parent`

Here `content-min-score` means:

- chunk score in text retrieval modes
- title score in title retrieval modes

### C3. Refactor existing commands onto the shared pipeline

- `AnswerCommand` should stop doing retrieval itself
- `AnswerCommand` should call the shared retrieval pipeline and only do:
  - validation
  - prompt building
  - LLM calls
  - artifact persistence
- `QueryCommand` should also be moved onto the shared pipeline so the text-retrieval logic is no longer duplicated in `query` and `answer`

That satisfies the “do not copy-paste code” requirement in a way that still leaves the CLI backwards-compatible.

---

## Step D — Add document-first retrieval mode (`retrieval-mode="documents"`)

### D1. Add the new mode

Extend retrieval mode support from:

- `text|titles`

to:

- `text|titles|documents`

### D2. Add `--d` and separate score thresholds where the retrieval pipeline is exposed

Add `--d` to at least:

- `retrieve`
- `answer`

Add separate score thresholds:

- `--doc-min-score`
- `--content-min-score`

`query-documents` can keep a single `--min-score` because it only executes the document stage.

I would keep `query` as the legacy text-only command rather than making it multi-mode.

### D3. Pipeline behavior for `documents`

Recommended flow:

1. query the document index
2. keep the top `d` documents above `doc-min-score`
3. run chunk similarity search
4. filter chunk hits to those `doc_uid`s
5. apply chunk selection using `content-min-score`
6. do the existing per-document top-`k` selection
7. fetch chunks
8. run expansion

### D4. Filtering strategy

In the first implementation, it is acceptable to:

- run chunk search across the full FAISS chunk index
- filter ranked hits by `allowed_doc_uids`
- then apply top-`k` per document

That is simple and correct with the current vector-store design.

If needed later, the vector store can be optimized to support allowed-document filtering earlier in the search path.

### D5. Output transparency

When using `retrieval-mode=documents`, include the document-stage information in debug/JSON output:

- which documents were selected
- their document scores
- which chunk hits survived the document filter

That will make evaluation much easier.

---

## Step E — Add expansion to section, without common-parent expansion

### E1. Add a new shared section-aware expansion stage

Current general retrieval expansion is adjacency-based, but `query-titles` already has a related concept: matched sections expand to descendant chunks.

Do not invent a separate tree-expansion implementation if it can be avoided. Instead, extract and generalize the section/subtree expansion logic into a shared retrieval or expansion module driven by `containing_section_id` and `section_closure`.

Recommended semantics for “expand to section”:

- for each selected chunk
- find its `containing_section_id`
- include all chunks belonging to that section subtree
  - the containing section itself
  - all descendant sections
- dedupe chunks by `(doc_uid, chunk_id)`
- preserve original document order

This is more useful than “same section id only”, because a logical section often contains nested subsections.

### E2. Add the CLI flag

Add a boolean flag such as:

- `--expand-to-section`

This should be available on:

- `retrieve`
- `answer`

### E3. Expansion order

I recommend this order inside the shared pipeline:

1. retrieval hit selection
2. section expansion
3. neighbor expansion (`--expand`)
4. full-document expansion (`--full-doc-threshold`)

That keeps the new structural expansion separate from the existing adjacency padding.

### E4. Missing section metadata

If a chunk has no `containing_section_id`, skip section expansion for that chunk and keep the already-selected chunk.

Do not fail the retrieval for missing section metadata.

---

## Step F — Add optional expansion to common parent

### F1. Add a flag

Add a boolean flag such as:

- `--expand-common-parent`

This should be supported by:

- `retrieve`
- `answer`

### F2. Semantics

Only apply this when section-aware expansion is enabled and there are multiple selected sections inside the same document.

Limit the breadth to **one level up maximum**.

Recommended behavior:

- collect the selected `containing_section_id`s per document
- look only at their **immediate parent section**
- if the selected sections share the same immediate parent, expand to that parent’s subtree
- if they do not share the same immediate parent, do nothing
- do not climb beyond one level up
- union with already-selected chunks
- preserve document order

### F3. Data access needed

The current `SectionStore` can return descendants, but immediate-common-parent expansion will also need parent access.

Extend the section-access layer with one of these approaches:

- `get_section(section_id)` plus parent traversal
- or `get_parent_section_id(section_id)`
- or `get_sections_by_ids(section_ids)`

A full arbitrary-depth lowest-common-ancestor helper is not needed because expansion is capped at one level up.

I would keep the tree logic in the retrieval layer, not inside the CLI command.

### F4. Guardrail

Validate that:

- `--expand-common-parent` requires section-aware expansion or a section-aware retrieval mode

Otherwise the flag becomes ambiguous.

---

## Step G — Update Promptfoo/eval plumbing so provider configs can pass the new retrieval parameters

This requirement should be reflected not just in the CLI, but also in the evaluation harness.

### G1. Update `scripts/run_answer.py`

Extend the Promptfoo provider-option extraction so `promptfoo_src/base.yaml` providers can pass the new retrieval settings.

At minimum support:

- `d`
- `doc-min-score`
- `content-min-score`
- `retrieval-mode=documents`
- `expand-to-section`
- `expand-common-parent`

Also keep backward compatibility with the current keys:

- `k`
- `min-score` where still relevant for legacy text-only paths
- `expand`
- `retrieval-mode=text|titles`

Recommended changes:

- extend `ExtractionOptions`
- extend mapping extraction helpers for ints, floats, bools, and retrieval mode
- pass the new values into `AnswerOptions`
- include the new provider config keys in Promptfoo artifact directory naming so runs remain distinguishable

### G2. Update `promptfoo_src/base.yaml`

Document and demonstrate the new provider-level parameters directly in the base Promptfoo config.

Recommended provider config examples should show keys such as:

- `retrieval-mode: documents`
- `d: 5`
- `doc-min-score: 0.35`
- `content-min-score: 0.55`
- `expand-to-section: true`
- `expand-common-parent: false`

This is important because the requirement is specifically about being able to pass these parameters from Promptfoo providers.

### G3. Update `scripts/run_promptfoo_eval.py` and `Makefile` as needed

Review both files and make any needed changes so the new provider-driven configuration works cleanly in eval workflows.

Likely expectations:

- no provider options should get stripped or shadowed accidentally
- experiment metadata and archived artifacts should remain reproducible when new retrieval parameters are used
- if convenient, add Make targets/examples or env-driven documentation for common document-retrieval eval runs

Even if most of the new parameter flow is handled by `scripts/run_answer.py`, the plan should explicitly verify the full chain:

- `promptfoo_src/base.yaml`
- `scripts/run_answer.py`
- `scripts/run_promptfoo_eval.py`
- `Makefile`

### G4. Eval coverage

Add at least one Promptfoo provider/example configuration using the new document-selection retrieval path so it is easy to compare against existing text/title modes.

---

## Suggested implementation order

1. **Document representation + storage**
   - extend `documents`, add migration, update store, add builder
2. **Document vector index**
   - add document embeddings during `store`
3. **`query-documents`**
   - prove the document index works in isolation
4. **Shared retrieval pipeline**
   - extract retrieval out of `answer`
   - add `retrieve`
   - move `query` onto the same pipeline where possible
5. **`retrieval-mode=documents`**
   - document preselection + chunk filtering
6. **Section expansion**
7. **Common-parent expansion flag**
8. **Promptfoo / eval harness updates**
   - `scripts/run_answer.py`
   - `promptfoo_src/base.yaml`
   - `scripts/run_promptfoo_eval.py`
   - `Makefile`
9. **Answer integration cleanup**
   - make `answer` consume only shared retrieval results

This order lets you validate each layer independently before combining them.

---

## Files likely to change

### CLI and commands

- `src/cli.py`
- `src/commands/query.py`
- `src/commands/answer.py`
- new `src/commands/query_documents.py`
- new `src/commands/retrieve.py`
- `src/commands/__init__.py`

### Eval / Promptfoo plumbing

- `scripts/run_answer.py`
- `scripts/run_promptfoo_eval.py`
- `promptfoo_src/base.yaml`
- `Makefile`

### Retrieval layer

- new `src/retrieval/document_profile_builder.py`
- new `src/retrieval/document_retrieval.py`
- new `src/retrieval/pipeline.py`
- new `src/retrieval/models.py`
- new `src/retrieval/expansion.py`
- possibly `src/retrieval/title_retrieval.py` to align with shared result types

### DB / models

- `src/models/document.py`
- `src/db/documents.py`
- `src/interfaces.py`
- `src/db/__init__.py`
- new migration under `src/migrations/` to extend `documents`

### Vector stores

- `src/vector/store.py`
- `src/vector/title_store.py`
- new `src/vector/document_store.py`
- possibly a new shared FAISS utility module

### Store command

- `src/commands/store.py`

### Tests

- `tests/unit/test_store_command.py`
- `tests/unit/test_query_command.py`
- `tests/unit/test_answer_command.py`
- new `tests/unit/test_query_documents_command.py`
- new `tests/unit/test_retrieve_command.py`
- new retrieval-layer tests
- integration tests covering end-to-end store/query/retrieve behavior

---

## Test plan

### Unit tests

#### Document representation builder

- builds the persisted document fields from title + background + issue + objective + scope + intro when those sections exist
- preserves the additional IFRIC/SIC-oriented fields already added
- falls back cleanly when one or more parts are missing
- truncates oversized representation parts deterministically
- generates stable transient embedding input text

#### Store command

- stores enriched document rows and one document embedding per document
- re-store deletes and replaces document embeddings
- skip-if-unchanged checks document-representation payload too

#### Query documents

- returns top `d` document hits
- respects document-stage `min_score`
- supports verbose and JSON output
- surfaces document representation fields in JSON

#### Shared retrieval pipeline

- `text` mode preserves current behavior
- `documents` mode filters chunk hits to top-`d` documents before top-`k` chunk selection
- `titles` mode still works after the refactor
- document stage and content stage use separate score thresholds

#### Expansion

- section expansion includes descendant-section chunks
- section expansion preserves document order and dedupes
- common-parent expansion only moves one level up at most
- common-parent expansion triggers only when selected sections share the same immediate parent
- common-parent flag validation behaves correctly

#### Answer command

- answer uses the shared retrieval pipeline instead of local retrieval logic
- `answer --retrieval-mode documents --d N` works
- prompt context reflects expanded chunk set

#### Promptfoo / eval plumbing

- provider config in `promptfoo_src/base.yaml` can pass `d`, `doc-min-score`, `content-min-score`, `expand-to-section`, and `expand-common-parent`
- `scripts/run_answer.py` maps those provider options into `AnswerOptions`
- Promptfoo artifact naming still captures the new retrieval parameters
- eval runner / Makefile workflow still works with provider configs using the new settings

### Integration tests

- `store` creates chunk, title, and document indexes
- `query-documents` returns expected IFRS, IFRIC, and SIC docs for representative queries
- `retrieve --retrieval-mode documents` only returns chunks from the top `d` docs
- section expansion and immediate-common-parent expansion produce stable output on sample HTML documents

Follow the project testing rules:

- prefer dependency injection and fakes
- avoid routine monkey-patching
- keep mocks at external boundaries only

---

## Risks / open questions

### 1. Exact document-representation heuristic

The biggest design choice is how aggressively to include section text in the document embedding.

Recommendation:

- start with a compact labeled representation
- use exact section-title matches for `background`, `issue`, `objective`, `scope`, and `introduction`
- preserve the extra IFRIC/SIC-oriented components that were already added
- use deterministic fallbacks
- keep the total text small enough that the document vector reflects document identity, not the whole standard

### 2. Score thresholds for document stage vs chunk/title stage

Use separate thresholds from the start:

- document-stage threshold
- content-stage threshold

Recommended CLI/API naming:

- `--doc-min-score`
- `--content-min-score`

where `content-min-score` applies to chunk retrieval in text modes and title retrieval in title modes.

### 3. Common-parent expansion breadth

Keep common-parent expansion deliberately narrow.

For the first version:

- allow at most one-level-up expansion
- only use a shared immediate parent
- do nothing if that condition is not met
- make the result transparent in verbose/JSON output

### 4. Query command compatibility

I recommend keeping:

- `query` = legacy text-only CLI
- `query-documents` = document-only CLI
- `retrieve` = canonical retrieval pipeline CLI

That adds the new capability without breaking existing command usage.

### 5. Promptfoo provider compatibility

The evaluation harness must stay aligned with CLI changes.

In practice that means the implementation should treat these as part of the delivery surface, not as follow-up cleanup:

- `promptfoo_src/base.yaml`
- `scripts/run_answer.py`
- `scripts/run_promptfoo_eval.py`
- `Makefile`

Otherwise the new retrieval parameters may exist in the CLI but remain unusable from Promptfoo experiments.

---

## Final recommendation

Implement this as a **document-first retrieval pipeline** layered on top of the existing chunk and section infrastructure:

1. build and persist the document representation by extending `documents` during `store`
2. embed one vector per document in a new document FAISS index
3. add `query-documents` to inspect that stage directly
4. extract retrieval into a shared pipeline and add `retrieve`
5. add `retrieval-mode=documents` with separate document/content score thresholds so `answer` and `retrieve` can do:
   - document preselection
   - restricted chunk retrieval
   - section-aware expansion
   - optional immediate-common-parent expansion capped at one level up

That gives you a clean, testable architecture and keeps the new document-selection stage observable instead of hiding it inside `answer`.