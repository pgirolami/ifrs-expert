# Plan — `documents2-through-chunks` routing

## Goal

Add a new retrieval mode, `documents2-through-chunks`, that expands document-routing options by using chunk similarity as the scoring basis for document selection.

Core behavior:

- search chunks first
- keep only chunks with score `>= retrieval.text.min_score`
- assign each exact document the maximum score of its surviving chunks
- for `documents2`, collapse exact documents to their standard bundle so the selected score for a standard is the best score across all chunks from the standard + supporting documents
- honor `retrieval.documents.global_d` as the cap on the number of selected document groups
- do **not** remove existing retrieval code or existing modes

## Current state

Today the retrieval pipeline has these relevant behaviors:

- `retrieval.mode` supports `text`, `titles`, `documents`, and `documents2`
- `documents` / `documents2` search document-level FAISS indexes by a configured similarity representation
- `documents2` currently consolidates variant document UIDs to the standard doc UID after document-stage search
- chunk retrieval already exists, but it is a downstream step after document selection
- `retrieval.text.min_score` already controls chunk filtering in text retrieval, but not document-stage routing

So there is no mode yet that says:

- “use chunk similarity as an additional document-routing algorithm”
- “rank documents by the best chunk they contain”
- “treat the standard bundle as the scoring unit”

## Fixed decisions

### 1. Add a new retrieval mode instead of changing existing ones

Introduce:

- `retrieval.mode = documents2-through-chunks`

Keep the existing modes intact:

- `documents`
- `documents2`
- `text`
- `titles`

This avoids breaking current behavior and keeps the experiment reversible.

### 2. Chunk score threshold comes from `retrieval.text.min_score`

For this new mode, chunk candidates are filtered using the existing text-stage threshold:

- only chunks with `score >= retrieval.text.min_score` are eligible
- chunks below that threshold are not returned

No new threshold field is needed for v1.

### 3. Global document cap still applies

`retrieval.documents.global_d` remains the hard cap on selected document groups.

For `documents2-through-chunks`, the selected unit should be the standard bundle / document group, not raw chunks.

### 4. Score aggregation is max-over-chunks

Scoring should be derived bottom-up:

1. each chunk gets a similarity score
2. each exact document gets the max score of its qualifying chunks
3. for `documents2`, each standard bundle gets the max score across all exact documents associated with that standard

That means supporting documents contribute to the score of the owning standard, which matches the existing `documents2` intent.

### 5. Preserve all code paths

Do not delete or replace the current document-retrieval implementation.

Instead, add a parallel code path for the new mode so the system can choose between document-representation routing and chunk-first routing.

## Implementation plan

## Phase 1 — extend policy validation

Update `src/policy.py` so `retrieval.mode` accepts:

- `documents2-through-chunks`

Also update any policy tests that validate allowed modes.

### Validation to add

- policy loading accepts `documents2-through-chunks`
- policy loading still accepts existing modes
- invalid mode values still fail with a clear error

## Phase 2 — define the chunk-first document routing shape

Add a chunk-first aggregation path in the retrieval models / pipeline.

Recommended shape:

- keep chunk search results as the primitive input
- aggregate chunk results into per-document scores using `max(score)`
- for `documents2-through-chunks`, aggregate those document scores again into standard-bundle scores using the same `max(score)` rule

This should likely live in `src/retrieval/pipeline.py` with helper functions that are easy to unit test.

Important behavior to preserve:

- exact documents should still be resolved using the existing document UID/type helpers
- `documents2` semantics should still use the standard bundle as the user-visible unit

### Validation to add

- a document with multiple chunk hits keeps the highest qualifying chunk score
- a document with no chunk above `retrieval.text.min_score` is excluded
- a standard bundle score is the max across all docs in that bundle

## Phase 3 — route `documents2-through-chunks` through the new aggregation path

Update the shared retrieval pipeline so:

- `text` keeps its current behavior
- `titles` keeps its current behavior
- `documents` keeps its current document-index behavior
- `documents2` keeps its current document-index behavior
- `documents2-through-chunks` uses the new chunk-first path

The new path should:

1. search chunks
2. filter chunks by `retrieval.text.min_score`
3. compute per-document max scores from the remaining chunks
4. collapse documents to their standard bundle for `documents2-through-chunks`
5. apply `retrieval.documents.global_d`
6. return the selected chunk set for the chosen documents / standard bundles

### Validation to add

- the new mode does not call document-level similarity search
- the new mode does use chunk search
- the returned chunk list contains only chunks above `retrieval.text.min_score`
- the selected documents respect `retrieval.documents.global_d`

## Phase 4 — keep document grouping semantics explicit

Make sure the standard-bundle collapse remains consistent with the existing `documents2` meaning:

- variants and supporting documents belong to the same standard group
- the group score is the max of all qualifying chunk scores across that group

This should reuse the existing standard-doc resolution helpers rather than inventing a second grouping scheme.

### Validation to add

- variant docs collapse onto their owning standard group
- supporting docs influence the group score
- the group key remains stable across retrieval and tests

## Phase 5 — add tests for the new mode

Add focused tests around the retrieval pipeline and command layer.

Suggested coverage:

- policy parsing accepts the new mode
- `documents2-through-chunks` uses chunk scores rather than document-level FAISS scores
- `retrieval.text.min_score` filters out low-scoring chunks
- `retrieval.documents.global_d` caps selected standard groups
- `documents2-through-chunks` still consolidates variants to the standard bundle
- existing `documents` and `documents2` behavior remains unchanged

## Files likely touched

### Policy and routing

- `src/policy.py`
- `src/retrieval/pipeline.py`
- `src/retrieval/models.py` if request/result shape needs a small helper field

### Commands

- `src/commands/retrieve.py`
- `src/commands/query.py`
- `src/commands/answer.py`

### Tests

- `tests/policy.py`
- `tests/unit/test_retrieve_command.py`
- `tests/unit/test_answer_command.py`
- retrieval pipeline / unit tests for chunk aggregation

## What does not need to change

- existing document-level retrieval code for `documents`
- existing document-level retrieval code for `documents2`
- title retrieval
- SQL schema
- index formats

## Risks

### 1. Ambiguity around the selected unit

The new mode mixes chunk scoring with `documents2` bundle semantics, so we need to be explicit about what counts toward `global_d`.

Mitigation:

- define the selected unit as the standard bundle / document group
- keep exact-document scoring as an internal aggregation step

### 2. Chunk noise may increase false positives

Chunk-first retrieval can surface documents with one good fragment and weak overall relevance.

Mitigation:

- keep `retrieval.text.min_score` as the gate
- validate on a small benchmark set before broad rollout

### 3. Score calibration may differ from document-level search

Chunk scores may not match document representation scores numerically.

Mitigation:

- keep the new mode isolated
- compare against current `documents2` before deciding whether it should become the default

## Success criteria

This slice is successful if:

1. `retrieval.mode = documents2-through-chunks` is accepted
2. chunk search drives document selection for the new mode
3. only chunks above `retrieval.text.min_score` are returned
4. `retrieval.documents.global_d` caps selected standard bundles
5. existing retrieval modes continue to work unchanged
