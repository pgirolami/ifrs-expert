# Plan — support `abonnes.efl.fr` DOM ingestion as `naxis`

## Goal

Extend the existing HTML ingestion pipeline so IFRS Expert can ingest rendered DOM captures from both:

- `https://ifrs.org` / `https://*.ifrs.org`
- `https://abonnes.efl.fr`

The new `abonnes.efl.fr` corpus will be stored as a new document type called `naxis`.

This plan is intended to be implemented on a dedicated worktree branch created from the current SME review branch state, with the plan artifact committed on that branch.

## Important framing

In the current codebase:

- `source_type` means **transport format** (`pdf` or `html`)
- `document_type` means **document family** and should be treated as persisted metadata from the `documents` table, not something inferred from a naming convention in `doc_uid`

Because `naxis` is a new kind of document but still arrives as HTML, it should **not** become a new `source_type`.

The correct representation is:

- keep `source_type="html"`
- add support for `document_type="NAXIS"`  consistently across storage and retrieval
- route extraction by **source domain / source-specific parser**, not by `source_type`

## Current-state assessment

The current implementation already supports:

- HTML capture ingestion from `ifrs.org`
- PDF ingestion
- skip-if-unchanged behavior for HTML
- section extraction, section-title embeddings, and document embeddings
- a Chrome extension that captures DOM + sidecar into `~/Downloads/ifrs-expert/`

However, the HTML pipeline is still strongly IFRS-specific:

1. `src/extraction/html.py` assumes IFRS DOM structure and selectors.
2. It requires IFRS-specific metadata such as `meta[name="DC.Identifier"]`.
3. `IngestCommand` always builds the same `HtmlExtractor`; there is no per-domain routing.
4. The Chrome extension is enabled only on `ifrs.org`.
5. `document_type` behavior still depends heavily on `infer_document_type(doc_uid)` and its naming-convention assumptions.

Those assumptions will break for `abonnes.efl.fr` unless the HTML pipeline is split into source-specific parsing strategies.

## Fixed decisions for this slice

1. Support both `ifrs.org` and `abonnes.efl.fr` in the same ingestion flow.
2. The new EFL-derived corpus is represented as document type `NAXIS`.
3. `source_type` remains `html` for naxis captures.
4. Existing IFRS HTML ingestion must continue to work unchanged.
5. Parser design should be sample-driven from the two provided DOM downloads plus expected `_CHUNKS.json` fixtures.
6. Section hierarchy is required for naxis.
7. Implementation work happens in a dedicated worktree branch from the current SME review state.

## Sample inputs now available on the branch

The branch now contains representative EFL fixtures under:

- `examples/Lefebvre-Naxis/20260412T190013Z--document.html`
- `examples/Lefebvre-Naxis/20260412T190013Z--document.json`
- `examples/Lefebvre-Naxis/20260412T190013Z--document__CHUNKS.json`
- `examples/Lefebvre-Naxis/20260412T190029Z--document.html`
- `examples/Lefebvre-Naxis/20260412T190029Z--document.json`
- `examples/Lefebvre-Naxis/20260412T190029Z--document__CHUNKS.json`

These samples are enough to replace several earlier assumptions with concrete parser decisions.

## Findings from the added EFL fixtures

### 1. There is no IFRS-style canonical metadata in the DOM

The added `abonnes.efl.fr` HTML samples do **not** contain:

- `link[rel="canonical"]`
- `meta[name="DC.Identifier"]`

So the IFRS HTML contract cannot be reused for naxis.

For naxis, the plan should therefore assume:

- trust the sidecar `canonical_url`
- validate it against the sidecar `url` shape and hostname
- do not require canonical metadata inside the saved HTML

### 2. The content root is concrete and stable in the samples

The actual document content sits under:

- `#documentContent`
- `#documentContent #ua.ua-content.oldHtml`
- `#documentContent .question.question-export`

The parser should start from `#documentContent .question.question-export`, not from the whole page.

This is important because the page contains a very large amount of unrelated chrome before the actual document body.

### 3. Chunk boundaries are explicit in the content DOM

The samples show a stable chunk pattern:

- each chunk body is a `div.qw-par.qw-par-p`
- the numeric chunk identifier is in `div.qw-p-no`
- the actual chunk text is in `div.qw-p-body`

This matches the expected `_CHUNKS.json` files well:

- sample 1 produces numbered chunks such as `49850`, `49860`, `49870`
- sample 2 produces numbered chunks such as `12501`, `12545`

So the chunking rule for naxis v1 should be:

- one `div.qw-par.qw-par-p` with a `div.qw-p-no` becomes one chunk
- `chunk_number == section_path == text from div.qw-p-no`
- `text == normalized text from div.qw-p-body`

### 4. Heading context is explicit in the page body

The samples show heading nodes such as:

- `div.qw-level.qw-level-1`
- `div.qw-level.qw-level-2`
- `div.qw-level.qw-level-3`
- `div.qw-level.qw-level-7`

These headings appear immediately before the associated chunks and can be used to maintain an active heading stack while scanning the content linearly.

#### Heading-level mapping for verification

| DOM class | Sample meaning | Suggested `SectionRecord.level` |
|---|---|---:|
| `qw-level-1` | `TITRE ...` | 1 |
| `qw-level-2` | `CHAPITRE ...` | 2 |
| `qw-level-3` | editorial grouping such as `L'ESSENTIEL ...` or `QUESTIONS/REPONSES PRATIQUES` | 3 |
| `qw-level-7` | leaf topical heading such as `Généralités` or `Modalités de transition ...` | 4 |

This gives us a dense internal hierarchy even though the DOM skips from `3` to `7`.

### 5. Ignore the left TOC hierarchy for parsing

Although the page contains a left-side TOC under `#sommaire` / `#tocTree`, that hierarchy should **not** drive parsing for this slice.

The parser should instead rely on the actual document body stream under `#documentContent .question.question-export`.

That means:

- no TOC-tree parsing is required for naxis ingestion
- no dependence on TOC node IDs or TOC ancestry
- section hierarchy should be reconstructed from the heading nodes that appear inline in the document body

### 6. Paragraph anchor IDs matter for chunk identity

The updated `_CHUNKS.json` fixtures show that the relevant `section_id` for a chunk is the `id` of the `<a id="..."></a>` anchor that immediately precedes the corresponding `div.qw-par.qw-par-p` block.

Concrete examples from the updated fixtures:

- chunk `49870` -> anchor id `P2D8D9D1995F171F-EFL`
- chunk `12501` -> anchor id `P8A8E6F292F99E-EFL`
- chunk `12545` -> anchor id `P7DA8E6F292F99E-EFL`

So for naxis v1 the plan should assume:

- `chunk_number == section_path == text from div.qw-p-no`
- the anchor immediately preceding the paragraph block is the stable paragraph locator
- that anchor id should populate the same fields and columns used today for IFRS paragraph anchors: the persisted `chunk_id` field and the surfaced `source_anchor` alias

The fixture key named `section_id` should therefore be treated as the paragraph anchor identifier, even though the name is slightly confusing relative to the internal `SectionRecord.section_id` concept.

### 7. The sidecar URL shape gives a good doc identity candidate

The two sidecars have URLs of the form:

```text
https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&uaId=...&refId=...-EFL
```

From the samples:

- `key=QRIFRS` identifies the product / corpus
- `uaId` looks session- or user-specific and should not be part of persistent identity
- `refId=...-EFL` identifies the selected document node/page and should be treated as the stable page identity

Therefore the naxis `doc_uid` should be derived from `key` + `refId`, not from title and not from `uaId`.

Recommended format:

```text
naxis-qrifrs-<refid-lowercased>
```

This form is preferable because it preserves the original `key` exactly.

### 8. The current samples support sections, not just chunks

The added fixtures strongly suggest naxis should support section extraction in v1 because we have visible heading levels in the content body that can be tracked as a hierarchy while scanning the page linearly.

So the plan should assume **Option A** by default:

- chunks
- sections
- closure rows
- title embeddings
- TOC text derived from the extracted section hierarchy if needed

A chunks-only fallback can remain as a contingency, but it is no longer the expected primary path.

## Proposed architecture

### 1. Split HTML extraction into source-specific strategies

Refactor the current one-size-fits-all `HtmlExtractor` into a router plus source-specific extractors.

Recommended shape:

```text
src/
  extraction/
    __init__.py
    html_common.py         # shared sidecar validation and helpers
    html_router.py         # dispatch by source_domain / hostname
    html_ifrs.py           # existing ifrs.org extraction logic
    html_naxis.py          # new abonnes.efl.fr extraction logic
    pdf.py
```

Alternative acceptable shape if fewer files are preferred:

```text
src/extraction/html.py
```

with:

- `HtmlCaptureMetadata`
- `IfrsHtmlExtractor`
- `NaxisHtmlExtractor`
- `HtmlExtractorRouter`

The important design point is not the exact file split, but that **IFRS-specific assumptions are isolated from naxis-specific assumptions**.

### 2. Route by sidecar/source domain, not by suffix

`IngestCommand` should continue to discover HTML captures by `.html` + `.json`, but the extractor selected for an HTML pair should depend on:

- `source_domain` from sidecar
- and/or canonical URL hostname in the HTML itself

Recommended routing rules:

- `ifrs.org` and `*.ifrs.org` -> IFRS extractor
- `abonnes.efl.fr` -> Naxis extractor
- anything else -> validation failure

This keeps `IngestCommand` simple and makes the source-specific logic explicit.

### 3. Keep one storage path

Do **not** fork storage logic.

Both IFRS HTML and Naxis HTML should continue to flow through the same `StoreCommand` path so that they all benefit from:

- chunk replacement
- skip-if-unchanged behavior
- chunk embeddings
- section/title embeddings where available
- document profile generation
- document embeddings

Only extraction should vary by source.

## Data model changes

## 1. Add `NAXIS` as a supported document type

Current code uses:

- `src/models/document.py::DOCUMENT_TYPES`
- `infer_document_type(doc_uid)`
- `query_documents`
- retrieval pipeline document-allocation logic
- response grouping utilities

Planned changes:

- add `NAXIS` to `DOCUMENT_TYPES`
- ensure `DocumentRecord.document_type` can carry `NAXIS`
- change `infer_document_type(doc_uid)` so it queries the database for the stored document record instead of relying on a `doc_uid` naming convention
- update callers and tests so document-family classification comes from persisted metadata, not prefixes in `doc_uid`
- update any tests that currently assume the only valid families are `IFRS`, `IAS`, `IFRIC`, `SIC`, `PS`

## 2. Standardize naxis `doc_uid`

Even after moving document-type inference to the database, naxis documents should still use a readable stable `doc_uid` namespace starting with `naxis`.

Recommended format:

```text
naxis-<key-lowercased>-<refid-lowercased>
```

Concrete examples from the added fixtures:

```text
naxis-qrifrs-n2d7d9d1995f171f-efl
naxis-qrifrs-c2a8e6f292f99e-efl
```

This preserves a stable namespace and keeps document identifiers readable, even though correctness should no longer depend on prefix-based logic.

The added EFL samples show that the stable suffix should come from the sidecar URL query parameters, with the following precedence:

1. `refId` from the sidecar `canonical_url`
2. `key` from the sidecar `canonical_url`
3. never use `uaId` because it appears user/session specific
4. use title slug only as a last resort if the query parameters are unavailable

## 3. Persist more source identity metadata if needed

Today the database stores:

- `source_type`
- `source_title`
- `source_url`
- `canonical_url`
- `captured_at`
- `document_type`

For multi-source HTML ingestion, it would be useful to also persist:

- `source_domain`

Recommended change:

- add `source_domain` to `DocumentRecord`
- add a migration to `documents` that defaults to IFRS
- populate it from the sidecar for both IFRS and naxis HTML

This is not strictly required for ingestion, but it improves:

- traceability
- debugging
- future source-specific UI or retrieval behavior
- easier audits of mixed-source corpora

## Extraction changes

### 1. Common HTML validation

Keep the shared sidecar contract, but make the validation rules source-aware where needed.

Shared validations should still include:

- `.html` exists
- matching `.json` exists
- sidecar JSON parses
- required fields are present and non-empty
- `captured_at` is ISO parseable
- `url` is HTTP/HTTPS
- `canonical_url` is HTTP/HTTPS if present/required
- `source_domain` is non-empty

Then apply source-specific validations.

### 2. IFRS extractor remains as-is conceptually

The existing IFRS parser already works against known IFRS viewer structure and should be preserved with minimal behavioral change.

Expected work:

- move current logic behind an `IfrsHtmlExtractor`
- preserve current tests and fixtures
- ensure routing still selects it for `ifrs.org`

### 3. Implement a new `NaxisHtmlExtractor`

The new extractor should be written from the supplied `abonnes.efl.fr` fixtures, not from guesswork.

It must define sample-backed rules for:

- document identity / `doc_uid`
- document title
- canonical URL handling
- content root selection
- chunk boundary selection
- section-path extraction
- section tree extraction
- paragraph-anchor extraction
- text normalization rules
- hidden / irrelevant DOM removal

The added EFL samples already resolve several of these decisions:

- content root: `#documentContent .question.question-export`
- chunk container: `div.qw-par.qw-par-p`
- chunk number: `div.qw-p-no`
- chunk text: `div.qw-p-body`
- heading nodes: `div.qw-level.qw-level-*`
- paragraph anchor id: the `<a id="..."></a>` immediately preceding each paragraph block
- stable page identity: `refId` from the sidecar URL
- section hierarchy source: the inline heading stream in the document body, not the left TOC

The remaining implementation work is to codify these rules cleanly and validate them against more examples.

#### 4. Naxis supports sections

Ingest:

- chunks
- sections
- closure rows
- title embeddings
- TOC text derived from extracted sections if useful downstream

This preserves parity with IFRS HTML retrieval.

## Store-command and profile-builder changes

### 1. Remove hidden IFRS assumptions from HTML extraction path

`StoreCommand` should remain generic, but review these points for hidden IFRS assumptions:

- `infer_document_type(doc_uid)` assignment
- document profile builder fields
- section filtering by title
- intro extraction / TOC generation

Planned changes:

- allow the extractor to set `document.document_type` explicitly to `NAXIS`
- use the explicit type from extraction when storing a document
- reserve `infer_document_type(doc_uid)` for looking up already-persisted documents from the database, not for deriving type from naming

### 2. Keep chunk and document skip logic unchanged

Skip-if-unchanged should apply to naxis exactly as it already does for IFRS HTML:

- same `doc_uid`
- same extracted chunk payload
- same extracted section payload, if sections are present
- same stored document payload

If all match, move the capture to `skipped/`.

## Retrieval and query behavior changes

Supporting a new document type affects more than ingestion.

### 1. Update document-type filtering

Current document-selection code uses prefix inference from `doc_uid`.

Planned change:

- add `NAXIS` to `DOCUMENT_TYPES`
- change `infer_document_type(doc_uid)` to resolve `document_type` from the `documents` table
- update `query_documents`, retrieval, and response-formatting paths so they rely on persisted `document_type` metadata rather than `doc_uid` prefixes

Affected components include:

- `src/commands/query_documents.py`
- `src/retrieval/pipeline.py`
- `src/b_response_utils.py`

### 2. Authority semantics

Naxis documents are authoritative alongside IFRS/IAS/IFRIC/SIC/PS.

This matters for:

- document-selection quotas by type
- response formatting
- “documentation retenue pour l'analyse” logic
- any future authority filtering

Consequence:

- treat `NAXIS` as another retrievable family
- but keep the distinction visible in output formatting

## Chrome extension changes

The extension must stop being IFRS-only.

### Required changes

#### `manifest.json`

Add host permissions for:

- `https://abonnes.efl.fr/*`

#### `service_worker.js`

Update supported-URL logic so the extension is enabled on both:

- `ifrs.org` / `*.ifrs.org`
- `abonnes.efl.fr`

Update text that currently says “available only on ifrs.org”.

Suggested wording:

- `Import to IFRS Expert (available only on supported sources)`

#### Capture behavior

Keep the current capture contract:

- rendered DOM via `document.documentElement.outerHTML`
- sidecar with `url`, `title`, `captured_at`, `source_domain`, `canonical_url`, etc.

The added EFL samples do not expose `link[rel="canonical"]` in the HTML, so the source-specific rule should be:

- for IFRS: keep the current DOM canonical validation
- for naxis: use the sidecar `canonical_url` / `url` directly, normalize the query string, and derive identity from `key` + `refId`

### Nice-to-have logging improvement

Log which source family is being captured:

- `ifrs`
- `naxis`

This will make extension debugging easier.

## Testing plan

### Unit tests

Add or update tests for:

1. HTML extractor routing by `source_domain`
2. IFRS extraction remains unchanged
3. Naxis extraction matches expected `_CHUNKS.json`
4. Naxis `doc_uid` derivation
5. Naxis `document_type == "NAXIS"`
6. Naxis chunk locator extraction from the preceding `<a id="..."></a>` anchor into the same persisted fields used by IFRS (`chunk_id` / `source_anchor`)
7. Naxis section hierarchy reconstruction from inline body headings
8. canonical URL fallback/validation behavior for EFL if needed
9. behavior when EFL DOM shape is invalid
10. `infer_document_type(doc_uid)` returns the stored `document_type` from the database
11. response grouping and query filtering include `NAXIS`
12. extension supported-domain predicate includes `abonnes.efl.fr`

### Integration tests

Add or update tests for:

1. end-to-end ingestion of one naxis HTML capture pair
2. skip behavior for unchanged naxis capture
3. replace behavior when naxis HTML changes
4. mixed ingestion run containing IFRS HTML + Naxis HTML + PDF
5. archive behavior to `processed/`, `skipped/`, and `failed/`

### Regression tests

Existing IFRS tests must continue to pass:

- `tests/unit/test_html_extraction.py`
- `tests/unit/test_ingest_command.py`
- `tests/integration/test_ingest_command.py`
- document query and retrieval tests impacted by `DOCUMENT_TYPES`

## Implementation phases

### Phase 1 — lock the sample contract from the fixtures already on the branch

Deliver:

- codified parsing notes from the 2 representative `abonnes.efl.fr` HTML examples already under `examples/Lefebvre-Naxis/`
- matching sidecar handling rules
- expected `_CHUNKS.json` assertions
- optional `__SECTIONS.json` fixtures if we decide to formalize the hierarchy expectations explicitly

Success criteria:

- the team agrees on the stable naxis parsing contract derived from the existing real samples

### Phase 2 — refactor HTML extraction into routed strategies

Deliver:

- source-aware HTML extractor router
- extracted IFRS logic moved into `IfrsHtmlExtractor`
- no functional regression for IFRS HTML

Success criteria:

- all existing IFRS HTML ingestion tests still pass

### Phase 3 — implement `NaxisHtmlExtractor`

Deliver:

- source-specific DOM parsing for `abonnes.efl.fr`
- stable `doc_uid` derivation
- `document_type="NAXIS"`
- chunk extraction matching expected fixtures
- section extraction if the samples support it

Success criteria:

- the provided naxis fixtures ingest into expected chunks

### Phase 4 — update storage/query semantics for `NAXIS`

Deliver:

- `DOCUMENT_TYPES` updated
- `infer_document_type` updated to query the database
- affected query/retrieval/response helpers updated to use persisted `document_type`
- optional `source_domain` persistence migration

Success criteria:

- `NAXIS` documents can be stored, grouped, and filtered without breaking existing types

### Phase 5 — extend the Chrome extension

Deliver:

- host permissions for `abonnes.efl.fr`
- supported-domain logic for both sources
- updated action text and logs

Success criteria:

- the extension can capture both IFRS and EFL pages into the existing inbox layout

## Open questions

1. If we later rename the fixture field currently called `section_id`, what should the clearer fixture name be, given that it actually carries the paragraph anchor id used for `chunk_id` / `source_anchor`?

## Recommendation

Proceed with a **source-routed HTML extraction refactor** before adding the naxis parser itself.

That is the cleanest path because:

- the current HTML extractor is already IFRS-specific
- `abonnes.efl.fr` will almost certainly need different metadata and selectors
- storage, skip logic, embeddings, and ingestion orchestration can stay shared

The smallest sound implementation sequence is:

1. lock the naxis parser contract from the fixtures already in `examples/Lefebvre-Naxis/`
2. refactor HTML extraction into IFRS + naxis strategies behind a router
3. implement `NaxisHtmlExtractor` using body headings for section hierarchy and preceding paragraph anchors for chunk identity
4. add `NAXIS` document-type support and switch document-family inference to the database-backed `infer_document_type(doc_uid)` lookup
5. extend the Chrome extension to capture from `abonnes.efl.fr`

This preserves the current architecture, avoids mixing two incompatible DOM contracts into one extractor, and keeps the feature grounded in real sample data.
