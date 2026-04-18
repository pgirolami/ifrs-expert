# Plan — fix `Issues` section extraction and repair document representations

## Goal

Fix a document-profile extraction bug where documents with a top-level section titled **`Issues`** do not populate `issue_text`, then repair the persisted document metadata and document-level FAISS index entries that were built from the bad representation.

## Problem statement

The document profile builder maps section titles to structured document fields using exact normalized title matching.

Current mapping in `src/retrieval/document_profile_builder.py`:

```python
SECTION_FIELD_BY_NORMALIZED_TITLE: dict[str, str] = {
    "background": "background_text",
    "issue": "issue_text",
    "objective": "objective_text",
    "scope": "scope_text",
    "introduction": "intro_text",
}
```

This recognizes:

- `Issue`

but not:

- `Issues`

As a result, IFRIC documents that use the plural section title are handled incorrectly, including IFRIC 16 which has been problematic in retrieval.

## Evidence

### Database schema

The `documents` table has a column named:

- `issue_text`

There is **no** `issues_text` column.

### Current population

Exact `document_type` counts in the current DB:

- `IFRIC`: **16 total**, **5** with non-empty `issue_text`
- `SIC`: **5 total**, **5** with non-empty `issue_text`

So the current pattern is:

- all SICs populate `issue_text`
- only some IFRICs populate it

### Section-title split explains the pattern

Documents using **singular** `Issue`:

- `ifric1`
- `ifric10`
- `ifric2`
- `ifric22`
- `ifric6`
- `sic10`
- `sic25`
- `sic29`
- `sic32`
- `sic7`

Documents using **plural** `Issues`:

- `ifric12`
- `ifric14`
- `ifric16`
- `ifric17`
- `ifric19`
- `ifric20`
- `ifric21`
- `ifric23`
- `ifric5`
- `ifric7`

That is a perfect match for the extraction behavior we are seeing.

### Example affected documents

`ifric16` sections in DB:

1. `Background`
2. `Scope`
3. `Issues`
4. `Consensus`

`ifric17` sections in DB:

1. `Background`
2. `Scope`
3. `Issues`
4. `Consensus`

But both currently have empty `issue_text` in `documents`.

## Impact

This bug affects more than just one field.

### 1. Wrong persisted document metadata

For affected IFRIC documents:

- `issue_text` is missing when it should be populated

### 2. Wrong `toc_text`

`toc_text` excludes representation sections based on `SECTION_FIELD_BY_NORMALIZED_TITLE`.

Because `Issues` is not recognized today:

- the `Issues` heading is incorrectly left in `toc_text`
- any intended TOC filtering of that representation section does not happen

### 3. Wrong document embeddings

The document-level embedding text is built from the structured fields plus TOC.

So for affected documents, the embedding is wrong in two ways:

- it is missing the `issue_text` payload
- it includes an overly noisy TOC contribution that should have been partly excluded

### 4. Existing document index entries are stale

The persisted document FAISS index was built from the incorrect representations, so at least the affected IFRIC docs must be re-embedded.

## Fixed decisions

### 1. Support both `Issue` and `Issues`

Update the title-to-field mapping so both normalized titles map to `issue_text`:

- `issue`
- `issues`

### 2. Keep the target field name as `issue_text`

Do **not** rename the persisted field.

The schema, codebase, and tests all already use `issue_text`. The bug is in title matching, not field naming.

### 3. Repair only the affected document representations and document index entries

A full document-index rebuild is not required for correctness.

Only documents with top-level title `Issues` are affected by this specific bug.

Initial repair scope:

- `ifric12`
- `ifric14`
- `ifric16`
- `ifric17`
- `ifric19`
- `ifric20`
- `ifric21`
- `ifric23`
- `ifric5`
- `ifric7`

### 4. Title index does not need rebuilding for this bug

The title index stores section-title embeddings from the `sections` table.

This bug does **not** change:

- section rows
- section titles
- section lineage

So the title index is unaffected.

### 5. Chunk index does not need rebuilding

This bug does not change chunk text or chunk embeddings.

### 6. Document query embedding caches do not need invalidation

Query embedding caches are keyed by query text and model, not by document content.

## What must be updated

### Must update

- code in `DocumentProfileBuilder`
- persisted `documents.issue_text` for affected docs
- persisted `documents.toc_text` for affected docs
- persisted document FAISS vectors for affected docs
- experiment narrative that relied on the old `issue_text` sparsity claim

### Does not need update

- `sections` table
- section/title FAISS index
- chunk FAISS index
- query embedding cache files

## Implementation strategy

## Step 1 — fix the mapping

Update `SECTION_FIELD_BY_NORMALIZED_TITLE` to include plural `issues`.

Files:

- `src/retrieval/document_profile_builder.py`

Change:

```python
"issues": "issue_text"
```

### Validation

Add or update unit tests to verify that:

- `Issue` populates `issue_text`
- `Issues` also populates `issue_text`
- `Issues` is excluded from `toc_text` the same way as other representation sections

## Step 2 — add regression coverage for affected IFRIC shapes

We need test fixtures for the plural-title case, ideally using a minimal synthetic document with:

- `Background`
- `Scope`
- `Issues`
- `Consensus`

Assertions:

- `issue_text` is populated from the `Issues` section descendants
- `toc_text` excludes the `Issues` section title and descendants consistently

Files likely touched:

- `tests/unit/test_document_profile_builder.py`

## Step 3 — choose repair path for persisted document metadata

Because the bad values are already stored in `documents`, we need a repair path.

### Preferred repair approach: rerun `store` on the affected source files

Because the affected set is very small, the simplest repair path is to rerun ingestion for those specific documents from their original source files.

Preferred command shape:

```bash
uv run python -m src.cli store <source-file> --scope documents
```

No manual cleanup should be required before running these commands.

Why this is preferred:

- reuses the normal ingestion path end to end
- automatically rebuilds the document profile with the fixed title mapping
- automatically updates the `documents` row and replaces the document FAISS vector
- avoids introducing one-off repair code for a narrow bug
- is fast enough because only a handful of documents are affected

Why `--scope documents` is sufficient for this bug:

- chunk text is unchanged
- section rows are unchanged
- title index is unchanged
- only `documents.*` fields and document embeddings are stale

Why no manual deletion is needed:

- `documents` rows are updated via upsert on `doc_uid`
- document FAISS entries are deleted and re-added by the normal `store` path
- `store --scope documents` should therefore repair the stale document metadata and document vector in place

Important caveat:

- the rerun must resolve to the same `doc_uid` as the existing stored document
- if UID inference from the source path is ambiguous, pass `--doc-uid <expected-doc-uid>` explicitly

### Caveat

This approach assumes the original source files for the affected IFRIC documents are still available and can be mapped back to the corresponding `doc_uid`s. If that assumption fails for any document, we can fall back to a DB-backed repair helper for the leftovers.

## Step 4 — repair affected docs by rerunning `store --scope documents`

For each affected doc:

1. locate the original source file
2. rerun `store` with `--scope documents` (and `--doc-uid` if needed to force the expected UID)
3. verify the resulting `documents.issue_text` and `documents.toc_text`
4. confirm the document FAISS entry was replaced

Artifacts updated:

- `documents` table rows for affected docs
- `corpus/data/index/faiss_documents.index`
- `corpus/data/index/id_map_documents.json`

No other indices need to change.

## Step 5 — rerun the targeted analysis that was invalidated

After repair, rerun the document-routing analysis that relied on `issue_text` assumptions, especially:

- the retrieval alternatives writeup in `experiments/34_retrieval_alternatives/EXPERIMENTS.md`

Specifically revisit:

- population counts for `issue_text`
- claims about IFRIC-wide viability of `issue_text`
- any type-aware field-selection discussion

## Testing strategy

### Unit tests

Add tests for:

1. `Issue` → `issue_text`
2. `Issues` → `issue_text`
3. `Issues` exclusion from `toc_text`
4. repaired embedding text includes `Issue:` line for plural-title IFRIC docs

### Repair test

Add at least one focused test for the repair path:

- given a persisted doc with plural `Issues`
- rebuild profile from DB-backed inputs
- verify `documents.issue_text` changes from empty to populated
- verify `documents.toc_text` changes as expected

### Manual validation

After repair, validate these documents directly:

- `ifric16`
- `ifric17`
- at least one other plural-title IFRIC (for example `ifric12`)

Check:

- `issue_text` is now non-empty
- `toc_text` no longer includes `Issues`
- the command did not require any manual DB or FAISS cleanup beforehand
- document query/routing behavior changes in the expected direction

## Risks

### 1. Original source files may not be easy to map back to every affected `doc_uid`

If the source-file lookup is messy or incomplete, the operationally simple rerun strategy may stall on a subset of docs.

Mitigation:

- start with rerunning `store --scope documents` for the clearly mappable affected docs
- only add a DB-backed repair helper if any affected docs cannot be repaired that way

### 2. Some analyses will shift in ways that look like regressions

Once `issue_text` is populated for the plural-title IFRIC docs, field-level ranking results may change materially.

Mitigation:

- explicitly treat the experiment-34 rewrite as part of the fix
- do not compare old and new results without noting that the old corpus state was buggy

### 3. There may be more title variants beyond `Issue` / `Issues`

This plan fixes the known bug first. We should also do a small post-fix audit of other top-level representation-section titles.

## Success criteria

This slice is successful if:

1. documents with section title `Issues` now populate `issue_text`
2. affected IFRIC docs have repaired `toc_text`
3. affected docs’ document embeddings are refreshed in the document FAISS index
4. title and chunk indices remain untouched
5. experiment 34 is updated to reflect the repaired corpus state

## Follow-up after this slice

Once the repair is complete, re-evaluate whether a type-aware strategy like:

- IFRS / IAS → `scope_text`
- IFRIC / SIC → `issue_text`

has become more viable.

Do not decide that before the repaired corpus state is measured.
