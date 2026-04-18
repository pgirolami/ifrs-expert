# Plan — configurable document-similarity representations per document type

## Goal

Extend `config/policy.default.yaml` so each exact `document_type` can choose which document-level representation is embedded for question similarity, then update retrieval, store, and migration flows so the correct FAISS document indices are used and kept in sync.

Target representations for v1:

- `background_and_issue` → concatenate `background_text` + `issue_text`
- `scope` → use `scope_text`
- `full` → current behavior

Initial policy mapping:

- `IFRS-S`, `IAS-S` → `background_and_issue`
- `IFRIC`, `SIC` → `scope`
- all other document types → `full`

## Current state

Today the document-retrieval stack assumes exactly one document-level FAISS index:

- persisted at `corpus/data/index/faiss_documents.index`
- id map at `corpus/data/index/id_map_documents.json`
- populated by `StoreCommand._store_document_embeddings()`
- queried by `RetrieveCommand` / `AnswerCommand` / `QueryDocumentsCommand`

The stored document text is also singular today:

- `DocumentProfileBuilder.build()` returns one `embedding_text`
- that text is the current `full` document representation
- retrieval mode `documents` searches that one index, then filters by per-type thresholds/caps from policy

So there is no place yet to say:

- “for IFRIC, compare the question against `scope_text`”
- “for IFRS-S, compare against `background_text + issue_text`”

## Fixed decisions

### 1. Add one explicit policy field per exact document type

Add a new field to each `retrieval.documents.by_document_type.<DOC_TYPE>` entry:

```yaml
similarity_representation: full | background_and_issue | scope
```

Recommended name: `similarity_representation`

Why this name:

- it is explicit about retrieval-stage use
- it does not overload the existing concept of the stored “document representation” fields
- it leaves room for future additions without changing the policy shape again

### 2. Keep one FAISS index per representation, not per document type

Add representation-specific document indices:

- `full` → keep using the current files
  - `corpus/data/index/faiss_documents.index`
  - `corpus/data/index/id_map_documents.json`
- `background_and_issue`
  - `corpus/data/index/faiss_documents_background_and_issue.index`
  - `corpus/data/index/id_map_documents_background_and_issue.json`
- `scope`
  - `corpus/data/index/faiss_documents_scope.index`
  - `corpus/data/index/id_map_documents_scope.json`

Why one index per representation:

- the policy values are representation choices, not type names
- multiple document types can share the same representation
- retrieval can search each needed representation once per query and then merge results
- changing policy mappings later does not require creating new index families

### 3. Store should update all document-representation indices, not only the one currently selected in policy

On every document store/update, delete and re-add the document across all document-level representation indices derived from the persisted document fields.

That means one `store` run keeps these synchronized:

- full
- background_and_issue
- scope

Why this is preferable:

- ingestion stays independent from the current policy file
- a policy-only change does not require re-ingesting the corpus
- the one-time migration only has to backfill the new indices once

### 4. Factor representation text building into a representation registry

The logic that turns a `DocumentRecord` into document-index text should be reusable from:

- `StoreCommand`
- the FAISS backfill script
- tests

Do **not** hardcode the three current representations throughout store/retrieval code.

Instead, introduce one registry/dictionary keyed by representation name, conceptually:

- `full`
- `background_and_issue`
- `scope`

where each key maps to the function that builds that representation text from the same populated `DocumentRecord`.

That gives us:

- one source of truth for supported representations
- a generic iteration model for store/backfill code
- easier extension when a fourth representation is added later

The current singular `embedding_text` flow should therefore evolve into something like:

- `texts_by_representation: dict[str, str]`

built from the registry after `DocumentProfileBuilder` has populated the structured fields.

### 5. No SQL schema migration is required

This slice changes:

- policy parsing
- document-index persistence
- retrieval routing
- a one-time FAISS backfill

It does **not** require new DB columns.

### 6. The FAISS backfill should be a dedicated one-off Python script

Do **not** trigger the backfill automatically from CLI startup or shared initialization.

Instead, add a dedicated script that is invoked manually once when we want to populate the new indices.

Recommended characteristics:

- lives under `scripts/`
- reads persisted rows from the `documents` table
- rebuilds the specialized document indices from those rows
- is idempotent by checking whether the target specialized index files already exist and are non-empty
- supports an explicit `--force` mode if we ever want to rebuild them deliberately

This keeps migrations operationally explicit and avoids surprising write work during ordinary read commands.

## Proposed policy shape

Example target shape in `config/policy.default.yaml`:

```yaml
retrieval:
  documents:
    global_d: 25
    by_document_type:
      IFRS-S:
        d: 4
        min_score: 0.53
        expand_to_section: true
        similarity_representation: background_and_issue
      IFRS-BC:
        d: 1
        min_score: 0.62
        expand_to_section: false
        similarity_representation: full
      IAS-S:
        d: 104
        min_score: 0.4
        expand_to_section: true
        similarity_representation: background_and_issue
      IFRIC:
        d: 6
        min_score: 0.48
        expand_to_section: true
        similarity_representation: scope
      SIC:
        d: 6
        min_score: 0.4
        expand_to_section: true
        similarity_representation: scope
      # all remaining exact types -> full
```

## Representation text definitions

### `full`

Keep the current behavior:

- the existing labeled multi-part document embedding text
- currently built from title + populated document fields + TOC

### `background_and_issue`

Build a deterministic text from:

- `background_text`
- `issue_text`

Recommended format:

```text
Background: ...
Issue: ...
```

This keeps debugging readable and consistent with the current labeled full representation.

### `scope`

Build a deterministic text from:

- `scope_text`

Recommended format:

```text
Scope: ...
```

### Missing-text behavior

This is the only material design edge case in the slice.

Recommended v1 behavior:

- build all three representations from the stored document fields
- if a representation has no usable text for a given document, skip inserting that document into that specific index and log it clearly
- do **not** silently synthesize `background_and_issue` or `scope` from `full`

Why:

- the index semantics stay clean and inspectable
- policy mistakes or sparse extraction become visible in logs/tests
- score behavior remains easier to reason about

Before rollout, validate that the chosen document types actually populate the needed fields often enough.

## Implementation plan

## Phase 1 — extend the typed policy model and validation

Update `src/policy.py`:

- add a typed alias or validated string for the representation choices
- extend `DocumentTypeRetrievalPolicy` with `similarity_representation: str`
- parse and validate the new field for every exact document type
- reject unknown values with a clear error

Also update:

- `tests/policy.py`
- any CLI/default-alignment tests that construct `DocumentTypeRetrievalPolicy`

### Validation to add

- config loads successfully when all types define a valid representation
- config fails on unknown representation values
- config fails if any exact document type omits the new field

## Phase 2 — make document-index paths representation-aware

Update `src/vector/document_store.py` so document index paths can be resolved by representation.

Recommended API shape:

- `get_document_index_path(representation: str = "full") -> Path`
- `get_document_id_map_path(representation: str = "full") -> Path`

And keep `DocumentVectorStore` constructible with explicit paths as it is today.

This keeps the core vector-store class generic while letting callers choose:

- full index
- background-and-issue index
- scope index

### Validation to add

- path helpers return the legacy filenames for `full`
- path helpers return deterministic suffixed filenames for the new representations
- existing `DocumentVectorStore` unit tests still pass for explicit paths

## Phase 3 — build reusable texts for all representations

Refactor the document-profile flow so the representation text generation is not hardcoded to one `embedding_text` string.

Recommended direction:

- keep `DocumentProfileBuilder.build()` responsible for populating structured fields on `DocumentRecord`
- add a reusable representation registry that converts a populated `DocumentRecord` into a dictionary such as:
  - `full` → text
  - `background_and_issue` → text
  - `scope` → text

Possible home:

- expand `src/retrieval/document_profile_builder.py`, or
- add a small sibling module such as `src/retrieval/document_similarity_representation.py`

The important outcome is not the filename, but that store/backfill/retrieval can work off dictionary keys from one shared registry rather than hardcoded branches scattered across the codebase.

### Validation to add

- `full` text remains unchanged for existing tests
- `background_and_issue` contains only the expected fields
- `scope` contains only `scope_text`
- empty specialized representations return empty text / `None` consistently

## Phase 4 — update store to fan out document embeddings across all representation indices

Update `src/commands/store.py`:

- replace the single document-embedding write with representation-aware writes
- on document persistence:
  - delete the current doc from all document-representation indices
  - rebuild the doc’s representation texts
  - add the doc to each index whose text is non-empty

This should happen for:

- normal `store --scope all`
- `store --scope documents`
- repair/rebuild scenarios where only document metadata changes

Recommended refactor:

- replace `_store_document_embeddings(doc_uid, embedding_text)`
- with something like `_store_document_embeddings(doc_uid, texts_by_representation)`

Also update the “missing document embedding repair” logic so it checks/repairs representation-specific indices rather than assuming exactly one document index exists.

### Validation to add

Add or extend unit tests in `tests/unit/test_store_command.py` to verify:

- one store operation updates all expected document indices
- a document with only `scope_text` is inserted into `full` and `scope`, but not `background_and_issue`
- rerunning `store --scope documents` replaces stale entries in the specialized indices
- unchanged-document repair can recreate missing specialized embeddings

## Phase 5 — route retrieval through the policy-selected representation index

Update the request-building layer:

- `src/retrieval/models.py`
- `src/commands/retrieve.py`
- `src/commands/answer.py` (indirectly via the shared retrieval request)

Add per-type mapping on the retrieval request, e.g.:

- `document_similarity_representation_by_type: dict[str, str]`

Then update `src/retrieval/pipeline.py` document-stage retrieval:

1. group exact document types by configured representation
2. for each required representation:
   - open the matching document FAISS index
   - search it once for the query
3. merge the ranked results
4. apply the existing per-type thresholds/caps/global `d`
5. continue with chunk retrieval exactly as today

Recommended merging rule for v1:

- merge by raw cosine score descending
- keep the current per-type threshold logic
- keep the current global `d` logic

This is the smallest behavioral delta from today.

### Important note

Because multiple indices may have somewhat different score distributions, retrieval thresholds may need light retuning after rollout. But the per-type `min_score` settings already exist and are the correct place to absorb that.

### Validation to add

Extend retrieval tests to verify:

- IFRS-S candidates are searched from the `background_and_issue` index
- IFRIC/SIC candidates are searched from the `scope` index
- other document types still use `full`
- merged results still respect per-type `d`, `min_score`, and global `d`

## Phase 6 — align `query-documents` with the same routing logic

`query-documents` is the manual inspection tool for document-level retrieval, so it must reflect the same per-type index selection.

Update `src/commands/query_documents.py` so:

- it reads the chosen exact `document_type`
- it resolves that type’s `similarity_representation` from policy
- it searches the matching representation-specific document index

This keeps manual experiments aligned with answer/retrieve behavior.

### Validation to add

Add/update tests so `query-documents --document-type IFRIC` uses the scope index while `--document-type IFRS-S` uses the background-and-issue index.

## Phase 7 — add the once-only FAISS backfill migration

Implement a dedicated one-off Python script that backfills the new document indices from already-persisted `documents` rows.

Recommended flow:

1. add a script under `scripts/`, for example `scripts/backfill_document_similarity_indices.py`
2. the script connects to the existing database and loads all persisted `documents`
3. it uses the shared representation registry to build texts by representation
4. it creates only the missing specialized index files by default
5. it writes the matching id maps
6. it exits without changing anything if the specialized indices already exist and are non-empty
7. optionally support `--force` to rebuild the specialized indices deliberately

### Why backfill from the database instead of re-extracting source files

- it is much faster
- it is deterministic from already persisted document fields
- it does not depend on source-file availability
- it avoids mixing ingestion concerns into migration code

### Files likely involved

- one new script under `scripts/`, for example `scripts/backfill_document_similarity_indices.py`
- shared representation helper code under `src/`
- possibly a small reusable DB/document-loading helper if needed

### Validation to add

- the script builds the new specialized indices when only the legacy full index exists
- re-running the script without `--force` is a no-op when the specialized indices already exist
- the script does not rewrite the legacy `full` index by default
- the script can rebuild the specialized indices when run with `--force`

## Files likely touched

### Config and policy

- `config/policy.default.yaml`
- `src/policy.py`
- `tests/policy.py`

### Retrieval and commands

- `src/retrieval/models.py`
- `src/retrieval/pipeline.py`
- `src/commands/retrieve.py`
- `src/commands/answer.py`
- `src/commands/query_documents.py`

### Store and document representations

- `src/commands/store.py`
- `src/retrieval/document_profile_builder.py` and/or a new representation helper module
- `src/vector/document_store.py`

### Migration script

- new script under `scripts/`
- shared representation helper under `src/`

### Tests

- `tests/unit/test_store_command.py`
- `tests/unit/test_retrieve_command.py`
- `tests/unit/test_query_documents_command.py`
- `tests/unit/test_document_and_title_vector_store.py`
- policy-loading tests

## What does not need to change

- chunk FAISS index format and storage
- title FAISS index format and storage
- SQL schema for `documents`
- query embedding cache keying

The query embedding cache is still keyed by query text and embedding model; representation-specific indices do not change the query embedding itself.

## Risks

### 1. Some chosen document types may not populate the requested specialized fields well enough

Example risk:

- if `background_text` / `issue_text` are sparse for some `IFRS-S` or `IAS-S` docs, those docs may disappear from the specialized index

Mitigation:

- add a one-off audit in the migration logs showing how many docs per exact type were inserted into each specialized index
- validate the selected mappings on a few known benchmark questions before final rollout

### 2. Scores from different representation indices may not be perfectly calibrated

Merging raw cosine scores across multiple indices is the simplest v1 choice, but it may slightly change cross-type competition.

Mitigation:

- rely on existing per-type `min_score` values
- retune only if needed after measuring retrieval behavior

### 3. A manual migration script can be forgotten during rollout

Because the backfill is no longer automatic, there is a deployment risk that someone updates the code and policy but forgets to run the one-off script.

Mitigation:

- document the script clearly in the rollout checklist
- make the script log the created/skipped indices loudly
- have retrieval fail clearly when a required specialized document index is missing

## Success criteria

This slice is successful if:

1. every exact document type in `config/policy.default.yaml` declares `similarity_representation`
2. document retrieval searches the FAISS index chosen by that field
3. `store` keeps all document-representation indices synchronized for changed docs
4. a dedicated one-off Python script backfills the missing specialized indices from persisted documents
5. `query-documents`, `retrieve`, and `answer` all use the same representation-routing behavior
6. the existing `full` document index remains backward-compatible
