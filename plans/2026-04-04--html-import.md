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
  "source_domain": "example.com"
}
```

Optional fields:

```json
{
  "extension_version": "0.1.0",
  "content_type": "text/html"
}
```

Required for HTML ingestion decisions:

- `canonical_url`

`canonical_url` must always be present for HTML ingestion and should be treated as the authoritative URL for document identity.

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
Imported: https://example.com/ifrs/ifrs-9 -> doc_uid=ifrs-9-section-6-3 (12 chunks)
Skipped: https://example.com/ifrs/ifrs-9-section-6-3 (unchanged content)
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

HTML parsing should be as structure-aware as PDF parsing.

The parser should:

- use known stable selectors from the representative HTML page(s)
- isolate only the IFRS content area
- ignore navigation, headers, footers, and account chrome
- derive section paths from the page’s real structure
- preserve paragraph numbering, heading hierarchy, and anchors where present

No generic heuristics are needed for v1 because the target pages share the same structure.

### Representative examples

Store development examples under `examples/`, alongside the existing PDF examples.

Examples should include:

- one or more representative IFRS HTML pages
- notes or expected section outputs where useful for parser validation

## Chunking Strategy

Chunking must remain structure-aware.

For both HTML and PDF, extractors should produce `Chunk` records aligned to real document structure rather than arbitrary windows.

### Preferred HTML chunk boundaries

For v1, HTML chunking should use only:

1. numbered paragraph nodes and their text

This should be implemented directly from the stable page structure rather than with fallback chunk-boundary strategies.

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

- for HTML, `doc_uid` is derived from the canonical URL
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
- HTML chunks leave page fields empty and use `source_anchor` where relevant

## Deduplication and Skip Rules

For HTML captures, deduplicate by canonical document identity and extracted content.

Recommended behavior:

- require `canonical_url` for every HTML capture
- derive `doc_uid` from `canonical_url`
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
- canonical URL chosen for HTML
- `doc_uid` chosen
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
- `doc_uid` derivation from canonical URL
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
3. `doc_uid` should be normalized from `canonical_url` for HTML imports.
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