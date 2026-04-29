# Plan - same-family reference expansion in retrieval

## Goal

Update retrieval so it uses the structured `content_references` data produced at ingestion time and expands retrieved chunks through explicit same-family references before section expansion.

The effective retrieval stage order should become:

1. document routing
2. seed chunk retrieval
3. same-family reference expansion
4. section expansion

Do not add cross-document reference expansion in this slice.

## Current-State Findings

The current retrieval path is centered in `src/retrieval/pipeline.py`.

- `execute_retrieval()` branches by retrieval mode and then returns `RetrievalResult` with `document_hits`, `chunk_results`, and `doc_chunks`.
- Chunk expansion is currently handled by `_expand_chunks()`, which applies:
  - section expansion via `_expand_to_section_subtrees()`
  - full-document inclusion via `_include_full_documents()`
  - neighborhood expansion via `_expand_with_neighbour_chunks()`
- There is no reference-expansion stage yet.
- The retrieval configs passed from `src/commands/retrieve.py`, `src/commands/answer.py`, and `src/commands/query.py` do not yet include a reference-store dependency.
- The runtime result model in `src/retrieval/models.py` currently carries only `doc_uid`, `chunk_id`, and `score` for chunk results.
- The answer-side retrieval artifacts in `src/answer_artifacts.py` serialize document hits and chunk hits, but do not yet carry provenance/reason metadata.
- The retrieval diagnostics contract in `experiments/analysis/target_chunk_retrieval/target_chunk_retrieval_contract.py` renders chunk coverage and expected range presence, but not retrieval-stage provenance.
- Same-family identification already exists in `src/models/document.py`:
  - `document_type_to_family()`
  - `resolve_standard_doc_uid()`
  - `infer_document_family()`
- The new ingestion schema already stores structured references in `content_references`, including:
  - source doc uid
  - source chunk / section identifiers
  - target raw text
  - target kind
  - target hint
  - parsed target bounds
  - source DB ids when available

Important constraints from the current codebase:

- Retrieval must not reparse HTML or chunk text.
- Reference expansion must use the stored reference rows.
- Seed results and reference-expanded results can point to the same chunk, so deduplication has to preserve provenance.
- Section expansion should run after reference expansion so governing paragraphs are present before the local subtree fan-out.

## Fixed Decisions

### Same-family rule

Use the document metadata helpers already present in `src/models/document.py` as the family boundary.

Practical rule for this slice:

- treat source and target as same-family only when they resolve to the same standard document uid via `resolve_standard_doc_uid()`
- treat same-family references as eligible only when the target is already a same-standard paragraph target
- do not auto-follow `BC`, `IE`, or `IG` targets in v1
- do not auto-follow cross-document references such as `IAS 24 paragraph 9`

That keeps the first version conservative while still recovering governing standard paragraphs cited from explanatory / appendix material.

### Reference expansion depth and scope

Keep reference expansion shallow and bounded:

- depth = 1 but make it configurable in the policy
- only expand from seed chunks
- only use stored references attached to the seed chunk or seed section containing the chunk
- cap the number of added chunks per seed chunk and per document to avoid explosion, configurable in the policy

### Range handling

Do not rely on `chunks.id` ordering for ranges.

Use chunk numbers and semantic ordering instead:

- exact chunk number matches should resolve directly
- ranges should expand from `target_start_lookup` / `target_end_lookup` or equivalent cleaned lookup values
- the resolver should compare chunk-number segments, not row ids and not lexicographic string order

This matters for cases like `4.1.1-4.1.2`, where `4.1.10` must not be included.

### Provenance

The retrieval pipeline needs a small machine-readable provenance field so diagnostics can explain why each chunk is present.

Recommended minimal shape:

- `similarity`
- `ref_sf` (same family reference)
- `exp_section_from_seed`  for section expansions from seed chunks
- `exp_sect_from_reference` for section expansions from referenced chunks

If a chunk is added by more than one stage, keep the first one

## Implementation Plan

### 1. Thread the reference store into retrieval

Add the reference-store dependency to the retrieval config objects and real command builders:

- `src/retrieval/pipeline.py`
- `src/commands/retrieve.py`
- `src/commands/answer.py`
- `src/commands/query.py`

Also update the test helpers that construct retrieval configs.

The pipeline should be able to read `content_references` without touching ingestion code.

### 2. Add a reference-expansion helper in the retrieval layer

Create a small helper module or pipeline helper that:

- loads references for the seed doc uid
- filters them to same-family references only
- resolves same-family target paragraph/range references to concrete chunks
- deduplicates against the seed set
- records provenance for chunks introduced by reference expansion

The helper should use the stored reference rows, not raw HTML.

Likely inputs:

- seed chunk list
- chunk store
- section store if needed for document-local resolution
- reference store

Likely outputs:

- expanded chunk membership
- provenance tags by chunk
- unresolved / skipped reference counters for diagnostics

### 3. Reorder the retrieval expansion pipeline

Refactor `src/retrieval/pipeline.py` so chunk expansion happens in this order:

1. seed results are selected
2. reference expansion adds same-family governing chunks & deduplicates them
3. section expansion runs on the expanded set
4. existing neighborhood/full-document expansion remains compatible with the new ordering

This is the key behavioral change.

The implementation should keep the current retrieval modes intact and only change how the final chunk set is expanded.

### 4. Make provenance visible in runtime results

Extend the retrieval result model so each chunk result can carry provenance / reasons.

Likely touch points:

- `src/retrieval/models.py`
- `src/commands/retrieve.py`
- `src/commands/answer.py`
- `src/answer_artifacts.py`

The goal is for JSON artifacts to show whether a chunk came from:

- seed similarity
- same-family reference expansion
- section expansion

This should remain backward compatible for callers that only read the existing fields.

### 5. Extend diagnostics to surface the new stage

Update the retrieval diagnostics path rather than inventing a parallel format.

Likely touch points:

- `experiments/analysis/target_chunk_retrieval/target_chunk_retrieval_contract.py`
- `experiments/analysis/document_routing/*` only if required by shared artifact helpers
- any helper that renders run JSON / markdown from answer artifacts

The diagnostics should make it clear why a chunk is present, especially when a governing paragraph was recovered by reference expansion rather than seed similarity.

### 6. Update policy/configuration cleanly

If the current retrieval policy needs a switch for this stage, add it in the existing policy decomposition rather than as a one-off flag.

Good fit:

- add a small reference-expansion config under the chunk expansion policy or as a sibling expansion block
- default it to enabled at depth 1
- keep the policy readable alongside the existing querying, routing, and chunk-expansion settings

### 7. Update docs

Update the retrieval architecture section in `README.md` so it reflects the new order:

- Querying
- Document routing
- Seed chunk retrieval
- Same-family reference expansion
- Section expansion
- Policy composition

Add a short note that ingestion-time `Refer:` annotations are now used to backfill governing paragraphs from explanatory or application guidance.

Add a short entry to `docs/JOURNAL.md` describing the new stage order and why it was added.

## Tests

Add focused tests for:

- same-family governing paragraph recovery from a seed appendix / application chunk
- reference expansion before section expansion
- cross-document references ignored in v1
- BC / IE / IG targets not auto-followed unless trivially safe
- deduplication when the same chunk arrives from seed and reference expansion
- provenance showing seed vs reference vs section expansion

Best-fit test locations:

- `tests/unit/test_retrieve_command.py`
- `tests/unit/test_answer_command.py`
- `tests/unit/test_document_type_caps.py`
- `tests/unit/test_target_chunk_retrieval_contract.py`
- new focused unit tests for the resolver if the logic is split out

## Validation Checklist

- retrieval-focused unit tests pass
- `make lint` passes
- retrieval output still matches the existing JSON / markdown shapes for untouched fields
- diagnostics show the new provenance tags for reference-expanded chunks

## First-Version Limits

Keep the first version deliberately small:

- same-family only
- depth 1 only
- no speculative cross-document expansion
- no HTML reparsing
- no full citation resolver
- no expansion beyond the stored reference rows

The purpose of this slice is to recover governing paragraphs explicitly cited by retrieved explanatory/application guidance, then let the existing section expansion widen the context locally.
