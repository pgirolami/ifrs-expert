# Plan — support IFRS multi-document captures and standard annotations

## Goal

Update the IFRS HTML capture flow so one standard landing page can be ingested correctly as four distinct document variants:

- `IFRS-S` (Standard)
- `IFRS-BC` (Basis for Conclusions)
- `IFRS-IE` (Illustrative Examples)
- `IFRS-IG` (Implementation Guidance)

Also ingest the new standard-only annotation bodies (agenda decisions / education footnote tables) as chunks, while still ignoring `div.note.edu` cross-reference notes for now.

## Problems to solve

### 1. Variant identity is currently ambiguous

The current importer relies too heavily on the shared page shell metadata:

- the HTML `<link rel="canonical">` is the same across all four variants
- the current filename slug logic produces the same basename for all four variants
- the sidecar title can stay generic even when the selected variant is not the Standard
- `document_type` currently collapses all IFRS variants into `IFRS`

### 2. Standard annotations are not ingested as chunks

The Standard capture now includes additional annotation bodies rendered as expandable education footnote tables such as:

- `table.edu_fn_table`
- left column contains chunk number like `E13`, `E19`, etc.
- right column contains the annotation heading plus the hidden body text

These need to become chunks.

### 3. Reference-only educational notes should still be excluded

For now we should ignore:

- `div.note.edu`

Those are cross-references, not substantive content chunks.

## Fixed decisions

### Document type mapping

Use the checked IFRS variant radio (`input[name="documentType"][checked]`) plus the `DC.Identifier` to distinguish variants.

Expected mappings:

- `ifrs9` -> `IFRS-S`
- `ifrs9-bc` -> `IFRS-BC`
- `ifrs9-ie` -> `IFRS-IE`
- `ifrs9-ig` -> `IFRS-IG`

### Document type derivation source

Do **not** rely on `derive_document_type_from_doc_uid()` for these HTML variants.

Instead:

- derive the selected variant from the full HTML + sidecar context
- use the checked `documentType` radio as the primary source of truth
- use `DC.Identifier` as a consistency signal, not as the only classifier
- persist the resolved `document_type` on the `DocumentRecord`

Because you will re-extract everything, we do not need legacy IFRS compatibility here.

That means `derive_document_type_from_doc_uid()` should be replaced with a more accurate abstraction, for example:

- a generic `resolve_document_type(...)` API, or
- source-specific resolvers such as IFRS HTML metadata resolution and simple PDF/doc_uid fallback

The new name should reflect that document type is resolved from source metadata, not merely derived from `doc_uid`.

### Variant-specific canonical URL

For IFRS captures, derive the stored canonical URL from:

- the shared shell canonical URL from `link[rel="canonical"]`
- the checked radio `value` for `documentType`

The resulting canonical URL should uniquely identify the selected variant, eg conceptually:

```text
<shell canonical url><checked documentType value>
```

This preserves the shared shell URL but differentiates the selected document variant.

### Sidecar title normalization

The browser capture should normalize the sidecar title using the selected variant label:

- Standard -> keep the base title
- Implementation Guidance -> append / normalize with `Implementation Guidance`
- Illustrative Examples -> append / normalize with `Illustrative Examples`
- Basis for Conclusions -> append / normalize with `Basis for Conclusions`

### Filename differentiation

The capture basename must include enough information to differ across the four variants.

The simplest acceptable path is to base the slug on the selected variant-specific canonical URL, so the basename changes automatically for:

- `ifrs9`
- `ifrs9-bc`
- `ifrs9-ie`
- `ifrs9-ig`

### Chrome extension responsibility

The Chrome extension should also provide the resolved `document_type` in the sidecar.

For IFRS captures:

- extension derives `document_type` from the checked `documentType` radio
- extension writes that value into the sidecar
- extractor recomputes the same value from the HTML and validates it against the sidecar
- any mismatch should fail fast rather than silently picking one source

This gives us:

- better filenames and sidecars directly at capture time
- clearer metadata for ingest debugging
- defense against bad or stale capture metadata

## Implementation plan

### Precondition — fixtures are already available

Assume the partial fixtures under `examples/IFRS/` already exist before implementation starts.

They should cover:

- Standard
- Implementation Guidance
- Illustrative Examples
- Basis for Conclusions

Only three sections per file are required.

For the Standard fixture set, include at least one annotation chunk expectation.

### Phase 1 — extend extractor tests for the four IFRS variants

Add HTML extraction tests that use the new samples under `examples/IFRS/` and verify, per file:

- `doc_uid`
- `document_type`
- normalized `source_title`
- variant-specific `canonical_url`
- representative chunks and sections from partial fixtures

### Phase 2 — split `src/extraction/html.py` into one file per extractor class

Before changing behavior, split the current module into three files, one per class:

- `HtmlExtractor`
- `IfrsHtmlExtractor`
- `NavisHtmlExtractor`

The exact filenames can follow the project’s naming conventions, but the end state should be one class per file.

Any shared helpers can live in a small shared helper module if needed, but the extractor classes themselves should no longer share one giant file.

### Phase 3 — update IFRS metadata derivation

In the new IFRS extractor module:

- detect the checked `documentType` radio
- derive the selected variant label and variant path
- compute the variant-specific canonical URL
- normalize the stored source title from the selected variant
- require the sidecar `canonical_url` and `document_type` to match the selected variant resolved from the HTML

### Phase 4 — support IFRS variant document types

In `src/models/document.py` and affected tests:

- extend supported document types with `IFRS-S`, `IFRS-BC`, `IFRS-IE`, `IFRS-IG`
- replace `derive_document_type_from_doc_uid()` with a better-named document-type resolution API
- for HTML extraction, resolve the type from full source metadata rather than from `doc_uid` alone
- keep any simple `doc_uid`-based fallback only where it is still genuinely useful for non-HTML sources

Update query / CLI tests that assert the list of supported document types.

### Phase 5 — ingest standard annotation tables as chunks

In `src/extraction/html.py`:

- detect `table.edu_fn_table`
- extract `chunk_number` from `.edu_fn_col1`
- extract chunk text from the title + expanded body in `.edu_fn_col2`
- keep ordered-list content and paragraph flow
- use the table `id` as the stable chunk id when available
- attach the annotation chunk to the currently active section context

### Phase 6 — ignore `div.note.edu`

Update IFRS body extraction helpers so `div.note.edu` is skipped during chunk text reconstruction.

Do not treat those reference notes as standalone chunks yet.

### Phase 7 — update Chrome extension capture metadata

In `chrome_extension/ifrs-expert-import/service_worker.js`:

- detect the checked IFRS variant radio and its label during capture
- compute and persist `document_type`
- compute a variant-specific canonical URL
- normalize the sidecar title from the selected variant
- let filename generation use the variant-specific canonical URL so the final basenames differ across variants
- fail capture-time assumptions loudly in logs if the IFRS page shell does not expose the expected selectors

Update the extension README if needed.

## Validation checklist

Before finishing, verify:

- the four new IFRS samples extract as four distinct docs
- the Standard variant is stored as `IFRS-S`
- standard annotations produce `E…` chunks
- `div.note.edu` is not ingested into chunk text
- existing IFRS / IFRIC HTML tests still pass
- document type resolution works for `IFRS-S`, `IFRS-BC`, `IFRS-IE`, `IFRS-IG`
- extractor-side document type validation agrees with the sidecar-provided `document_type`

## Deliverables

- plan file in `plans/`
- extractor split into one file per extractor class
- extractor + metadata code changes
- extension capture metadata updates, including `document_type`
- partial fixtures in `examples/IFRS/`
- updated unit tests covering the new behavior
