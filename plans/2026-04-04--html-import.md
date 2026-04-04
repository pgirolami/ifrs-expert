# Plan — add an ingest command for HTML captures and PDFs

## Goal

Add a new CLI ingestion flow that scans a fixed inbox directory, finds new source files, and ingests them into IFRS Expert.

The command should support both:

- authenticated HTML pages captured from Chrome as `.html` + `.json` sidecar pairs
- standalone PDF files dropped into the same inbox directory

The ingestion flow should delegate document storage to `StoreCommand`, so there is still a single command responsible for:

- extracting structured chunks
- replacing existing chunks for a document
- updating embeddings in the vector index

## Core Decisions

The following decisions are fixed for this slice:

- CLI command name: `ingest`
- Python command module: `src/commands/ingest.py`
- Python command class: `IngestCommand`
- `ingest` scans the inbox and delegates each discovered source file to `StoreCommand`
- `StoreCommand` is generalized so it can ingest either HTML or PDF through a shared extraction protocol
- extraction code is consolidated under one package:

```text
src/
  extraction/
    __init__.py
    pdf.py
    html.py
```

- representative HTML pages live in `examples/`, just like the current PDF examples
- HTML parsing will use known stable selectors from representative samples; no generic heuristics are needed
- a `documents` table is added now, with `doc_uid` as the primary key
- unchanged HTML captures move to `skipped/`
- raw HTML hashes are not persisted in the database in v1
- the Chrome extension is part of the plan and should be implemented last

## User Flow

### HTML flow

1. The user signs in to the IFRS site in Chrome.
2. The user opens a page to ingest.
3. The user clicks **Import to IFRS Expert** in the Chrome extension.
4. The extension saves the rendered DOM and JSON sidecar into the inbox.
5. The user runs:

```bash
uv run python -m src.cli ingest
```

6. The CLI finds the new HTML capture pair.
7. The CLI delegates ingestion to `StoreCommand`.
8. The raw files are moved to:
   - `processed/` on success
   - `failed/` on failure
   - `skipped/` if the imported content is unchanged

### PDF flow

1. The user drops a PDF into the same inbox.
2. The user runs:

```bash
uv run python -m src.cli ingest
```

3. The CLI finds the PDF.
4. The CLI delegates ingestion to `StoreCommand`.
5. The raw file is moved to `processed/` or `failed/`.

## Directory Layout

Use a fixed directory under Downloads:

```text
~/Downloads/ifrs-expert/
  inbox/
  processed/
  failed/
  skipped/
```

Rules:

- the Chrome extension writes only to `inbox/`
- PDFs can be dropped manually into `inbox/`
- `ingest` is responsible for moving files out of `inbox/`

## File Contract

### HTML capture pair

Each HTML capture consists of two files with the same basename:

```text
YYYYMMDDTHHMMSSZ--<slug>.html
YYYYMMDDTHHMMSSZ--<slug>.json
```

Example:

```text
20260404T142310Z--ifrs-9-hedge-accounting.html
20260404T142310Z--ifrs-9-hedge-accounting.json
```

### PDF capture

Each PDF capture is a single file:

```text
<name>.pdf
```

### Temporary file handling

`.part` must be the last suffix so globbing for `*.html`, `*.json`, and `*.pdf` never picks temporary files up.

Examples:

```text
20260404T142310Z--ifrs-9-hedge-accounting.html.part
20260404T142310Z--ifrs-9-hedge-accounting.json.part
ifrs-9-financial-instruments.pdf.part
```

The CLI should only scan final files:

- `*.html`
- `*.json`
- `*.pdf`

and should never look at `*.part` files.

## HTML Sidecar Schema

Required fields:

```json
{
  "url": "https://example.com/path",
  "title": "IFRS 9 — Hedge accounting",
  "captured_at": "2026-04-04T14:23:10Z",
  "source_domain": "example.com",
  "canonical_url": "https://example.com/canonical-path"
}
```

Optional fields:

```json
{
  "extension_version": "0.1.0",
  "content_type": "text/html"
}
```

`canonical_url` must always be present for HTML ingestion and is the authoritative source URL stored on the document record.

The extension should populate `canonical_url` from the page DOM using:

- `document.querySelector('link[rel="canonical"]')?.href`

The extension should save the rendered DOM using:

- `document.documentElement.outerHTML`

not raw response source.

## CLI Contract

Add a new subcommand:

```bash
uv run python -m src.cli ingest
```

### Responsibilities

`IngestCommand` should:

1. scan `inbox/`
2. discover:
   - complete HTML capture pairs
   - standalone PDFs
3. validate HTML sidecars
4. choose the correct extractor based on file type
5. call `StoreCommand` for each discovered input
6. classify each input as processed, failed, or skipped
7. move raw files into the correct archive directory
8. print a concise summary

### Suggested output

```text
Processed 4 item(s): 2 imported, 1 skipped, 1 failed
Imported: /Users/.../inbox/ifrs-9.pdf -> doc_uid=ifrs-9 (145 chunks)
Imported: https://www.ifrs.org/.../ifrs-9-financial-instruments.html -> doc_uid=ifrs9 (12 chunks)
Skipped: https://www.ifrs.org/.../ifrs-9-financial-instruments.html (unchanged content)
Failed:  /Users/.../inbox/broken.html (invalid sidecar JSON)
```

### Future flags

The first implementation can stay minimal, but the design should allow later addition of:

- `--capture-dir`
- `--limit`
- `--dry-run`
- `--verbose`

## Architecture

### 1. Shared extraction protocol

HTML and PDF extraction should implement the same protocol so `StoreCommand` can use either transparently.

Recommended shape:

- `PdfExtractor` in `src/extraction/pdf.py`
- `HtmlExtractor` in `src/extraction/html.py`
- a shared protocol in `src/interfaces.py` or a dedicated extraction interface module

The protocol should cover:

- extracting document metadata
- extracting structure-aware chunks
- deriving or confirming `doc_uid`
- returning enough structured document metadata for `documents` upsert and skip decisions

### 2. Store command refactor

`StoreCommand` should no longer be conceptually “PDF only”.

It should be refactored so it can accept:

- a source path
- an extractor implementation
- an optional explicit `doc_uid`

Responsibilities remain:

- initialize database
- load structured chunks from the extractor
- replace existing chunks for that `doc_uid`
- update vector embeddings

This preserves the current storage logic while making extraction pluggable.

### 3. Ingest command orchestration

`IngestCommand` should do file discovery and routing only.

Responsibilities:

- pair HTML files with sidecars
- validate sidecars
- choose `HtmlExtractor` or `PdfExtractor`
- create and execute `StoreCommand`
- move files after the result is known
- keep processing later items even if one fails

## Extraction Package Layout

The extraction code should be reorganized to mirror HTML and PDF equally:

```text
src/
  extraction/
    __init__.py
    pdf.py
    html.py
```

Planned changes:

- move current PDF extraction logic from `src/pdf/extraction.py` into `src/extraction/pdf.py`
- add HTML extraction logic in `src/extraction/html.py`
- update imports so callers use the new shared extraction package

## Parsing Strategy

### PDF

Keep the current PDF parsing behavior, but move it into `src/extraction/pdf.py`.

The logic remains structure-aware and section-based.

### HTML

HTML parsing should be as structure-aware as PDF parsing, but the implementation can now be concrete because we have representative IFRS examples in `examples/`.

The parser will use the IFRS HTML viewer structure visible in those examples.

#### Source metadata extraction

From the saved HTML, the parser should extract:

- canonical URL from `link[rel="canonical"]`
- short document identifier from `meta[name="DC.Identifier"]`
- document title from the page metadata or sidecar

Planned rules:

- `canonical_url` from the sidecar is required
- `link[rel="canonical"]` in the HTML is also required
- the sidecar `canonical_url` and HTML canonical URL must match
- `doc_uid` for HTML should come from `meta[name="DC.Identifier"]` because it is short and stable in the provided examples (for example `ifrs9` and `ifric16`)
- if `meta[name="DC.Identifier"]` is missing, the import should fail rather than guess

#### Content root selection

Based on the representative IFRS pages, the parser should treat this as the content root:

- `section.ifrs-cmp-htmlviewer__section`

This avoids page chrome outside the actual standard text.

#### Paragraph node selection

Within the content root, the parser should identify chunk candidates with:

- `div.topic.paragraph[id]`

The examples show that these paragraph nodes are stable even when the nesting level differs (`nested3`, `nested4`, `nested5`) or when additional classes such as `principles` and `noprinciples` are present.

#### Section path extraction

For each paragraph node, extract the section path from:

- `td.paragraph_col1 .paranum > p`

Examples from the provided files include:

- `1`
- `AG8`
- `2.4`
- `3.1.1`
- `4.2.1`

This extracted paragraph identifier becomes `section_path`.

#### Text extraction

For each paragraph node, extract text from:

- `td.paragraph_col2 > .body`

Rules for text extraction:

- flatten visible text across nested inline elements (`p`, `span`, `a`, `em`, etc.)
- preserve the logical reading order
- normalize whitespace aggressively because the expected text is often split across multiple DOM nodes
- include ordered-list content that appears inside the paragraph body, such as `table.ol` rows with `(a)`, `(b)`, etc.
- exclude hidden educational or annotation-only content such as nodes with `style="display: none;"`
- exclude UI-only controls and page chrome because parsing starts from the content root

The matching principle for validation is:

- overall text content must match after whitespace normalization
- `section_path` must match exactly

#### Parsing scope for v1

For v1 we will extract only paragraph nodes and their text, where the paragraph identifier comes from the IFRS paragraph marker in the left column.

These identifiers are not limited to simple numbers. They can include values such as:

- `1`
- `3.1.1`
- `AG8`

We will not implement additional heading-based chunking or generic fallback heuristics because the representative IFRS pages already provide a stable paragraph-level structure.

### Representative examples

Development and validation should use the provided HTML and partial expected-output files under `examples/`.

In particular:

- `...ifric16.html`
- `...ifric16__CHUNKS.json`
- `...ifrs9.html`
- `...ifrs9__CHUNKS.json`

The `__CHUNKS.json` files are partial expectations, not complete exports. They should be used to verify:

- selector correctness
- exact `section_path` extraction
- normalized text reconstruction from fragmented DOM content

## Chunking Strategy

Chunking must remain structure-aware.

For both HTML and PDF, extractors should produce `Chunk` records aligned to real document structure rather than arbitrary windows.

### Preferred HTML chunk boundaries

For v1, HTML chunking should use only:

1. paragraph nodes and their text

Each paragraph node becomes exactly one chunk.

This should be implemented directly from the stable page structure described above rather than with fallback chunk-boundary strategies.

Each HTML chunk should preserve enough metadata to support traceability and later citation.

## Data Model Changes

Implement a `documents` table now and use `doc_uid` as the key.

### Documents table

Add a new table with `doc_uid` as the primary key.

Recommended fields:

- `doc_uid`
- `source_type` (`pdf` or `html`)
- `source_title`
- `source_url`
- `canonical_url`
- `captured_at`
- `created_at`
- `updated_at`

Notes:

- for HTML, `canonical_url` is stored as the authoritative source URL on the document record
- for HTML, `doc_uid` is derived from `meta[name="DC.Identifier"]` in the saved HTML, not from `canonical_url`
- for PDFs, `doc_uid` remains the explicit CLI value or filename stem
- no raw HTML hash is stored in v1

### Chunks table

Keep chunks linked by `doc_uid`.

Chunk-level fields should continue to include:

- `doc_uid`
- `section_path`
- `text`

And should evolve to support both formats cleanly.

Recommended chunk-level locator fields:

- `page_start`
- `page_end`
- `source_anchor`

Notes:

- PDF chunks keep `page_start` and `page_end`
- HTML chunks leave page fields empty
- for HTML, `source_anchor` should be populated from the paragraph node id, for example `IFRS09_3.1.1` or `IFRIC16_AG8`

## Deduplication and Skip Rules

For HTML captures, deduplicate by canonical document identity and extracted content.

Recommended behavior:

- require `canonical_url` for every HTML capture
- extract and validate `link[rel="canonical"]` from the saved HTML
- require the sidecar `canonical_url` to match the HTML canonical URL
- derive `doc_uid` from `meta[name="DC.Identifier"]`
- if a document with that `doc_uid` already exists, compare the newly extracted chunk payload with the stored chunk payload
- if identical, do not replace the document and move the raw files to `skipped/`
- if changed, replace the document contents through `StoreCommand`

For PDFs:

- preserve current replace-by-`doc_uid` behavior

This achieves skip behavior without storing a raw HTML hash in the database.

## Validation Rules

### HTML validation

Validate before calling `StoreCommand`:

- `.html` file exists
- matching `.json` sidecar exists
- JSON parses successfully
- required fields are present and non-empty
- `captured_at` is parseable
- `url` is HTTP or HTTPS
- `canonical_url` is present and is an HTTP or HTTPS URL
- `source_domain` is non-empty
- the saved HTML contains `link[rel="canonical"]`
- the saved HTML contains `meta[name="DC.Identifier"]`
- the HTML canonical URL matches the sidecar `canonical_url`

If validation fails, move both files to `failed/`.

### PDF validation

Validate before calling `StoreCommand`:

- `.pdf` file exists
- file is readable

If storage fails, move the PDF to `failed/`.

## Logging

Use the existing project logging style and make the ingest path easy to follow.

Important events:

- inbox scan started
- HTML capture pairs found
- PDFs found
- sidecar validation failures
- extractor selected
- canonical URL extracted from HTML and matched to sidecar
- `doc_uid` extracted from `meta[name="DC.Identifier"]`
- skip decision
- replace decision
- chunk count produced
- embeddings updated
- archive move destination
- final summary counts

## Test Plan

### Unit tests

Cover:

- inbox discovery for `.html`, `.json`, and `.pdf`
- `.part` suffix handling
- HTML pair matching
- sidecar validation
- extractor selection
- `doc_uid` derivation for HTML
- skip decision for unchanged HTML
- archive destination selection
- HTML parsing using representative files from `examples/`
- text normalization against partial `__CHUNKS.json` expectations

### Integration tests

Cover:

- end-to-end ingestion of a PDF from `inbox/`
- end-to-end ingestion of an HTML capture pair from `inbox/`
- replacement of an existing HTML document with changed content
- unchanged HTML moved to `skipped/`
- failed HTML capture moved to `failed/`

## Implementation Phases

### Phase 1 — data model and extraction refactor

Deliver:

- `documents` table migration
- `Chunk` / DB updates for dual-format ingestion
- shared extraction protocol
- move PDF logic to `src/extraction/pdf.py`

Success criteria:

- PDF ingestion still works after the extraction refactor

### Phase 2 — generalized store command and ingest command

Deliver:

- refactored `StoreCommand` using the extraction protocol
- new `src/commands/ingest.py`
- inbox scan for HTML and PDF
- archive move behavior for processed and failed items

Success criteria:

- `uv run python -m src.cli ingest` can discover files and delegate them correctly

### Phase 3 — HTML parser and skip logic

Deliver:

- `src/extraction/html.py`
- selector-based HTML parsing from representative examples
- canonical URL extraction and validation from `link[rel="canonical"]`
- `doc_uid` derivation from `meta[name="DC.Identifier"]`
- unchanged-content detection
- `skipped/` archive behavior

Success criteria:

- representative HTML pages ingest into structure-aware chunks with stable section paths

### Phase 4 — hardening with representative examples

Deliver:

- more example HTML pages under `examples/`
- richer tests against those examples
- improved logging and failure messages

Success criteria:

- importer is reliable against the set of representative IFRS pages provided for development

### Phase 5 — Chrome extension

Deliver last:

- a Chrome-only extension with button text **Import to IFRS Expert**
- saves rendered DOM to `inbox/`
- writes `.html.part` and `.json.part` first
- atomically renames to final `.html` and `.json`
- uses the agreed sidecar schema

Success criteria:

- the extension can capture a logged-in IFRS page into the inbox in the exact format the CLI expects

## Resolved Questions

1. Exact IFRS URL patterns do not matter for planning because the user will capture pages via the extension.
2. Stable selectors exist on the target pages.
3. `canonical_url` is authoritative for HTML source identity, but `doc_uid` should come from `meta[name="DC.Identifier"]` in the saved HTML.
4. Unchanged HTML captures should move to `skipped/`.
5. Raw HTML hashes should not be stored in the database in v1.

## Recommendation

Proceed with a narrow but complete v1 built around:

- a single `ingest` CLI command
- inbox scanning for both HTML and PDF
- `StoreCommand` as the shared storage path
- a unified extraction package with `pdf.py` and `html.py`
- a `documents` table keyed by `doc_uid`
- selector-based HTML parsing using representative pages in `examples/`
- a Chrome extension implemented last, after the HTML parser is validated against sample pages

This keeps the ingestion model coherent, reuses the current storage pipeline, and adds HTML support without introducing browser automation or unnecessary parsing heuristics.