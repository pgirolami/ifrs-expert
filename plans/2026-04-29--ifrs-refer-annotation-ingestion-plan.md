# Plan - ingest IFRS `Refer:` annotations as structured references

## Goal

Extend IFRS HTML ingestion so educational `Refer:` annotations are parsed, normalized into reference records, resolved to stored target chunks where possible, and persisted for later retrieval-time reference expansion.

This slice is ingestion/storage only. Do not change retrieval behavior, but do resolve stored reference targets during ingestion so retrieval-time expansion can read precomputed links.

## Current-State Findings

The current ingestion path is:

- `src/extraction/html.py` routes HTML by `source_domain`.
- IFRS captures are parsed by `src/extraction/ifrs_html_extractor.py`.
- `IfrsHtmlExtractor._extract_structure()` walks `section.ifrs-cmp-htmlviewer__section` and emits `Chunk` plus `SectionRecord` objects.
- `div.note.edu` is currently treated as reference-only educational content and stripped by `_is_reference_only_educational_note()`.
- `ExtractedDocument` currently carries `document`, `chunks`, `sections`, and `section_closure_rows` only.
- `StoreCommand` persists chunks first, then sections, then syncs chunk `containing_section_db_id`.
- Skip-if-unchanged currently compares only chunk, section, and document payloads. New reference persistence must be included in the change/skip decision, or a force-store/backfill path must be documented.
- The schema uses versioned migrations under `src/migrations/`; the consolidated baseline is `000_schema.sql`.
- There is no existing reference table or reference model.
- The current database stores paragraph-level chunk numbers such as `4.1.1`, not subparagraph targets such as `4.1.1(a)`. A check against `corpus/data/db/ifrs.db` found `ifrs9 | 4.1.1 | IFRS09_4.1.1` and no chunk numbers containing parentheses.

Important existing behavior to preserve:

- `Refer:` note text must remain excluded from user-facing chunk text.
- `table.edu_fn_table` educational annotation bodies are substantive chunks and are separate from `div.note.edu` reference-only notes.
- IFRS section/chunk attachment should reuse existing stable ids: `Chunk.chunk_id`, `Chunk.containing_section_id`, `SectionRecord.section_id`, and stored section `db_id` after section persistence.

## Fixed Decisions

### Reference Storage Shape

Add a dedicated `content_references` table. Use one row per extracted target reference, plus a child table for the stored target chunks resolved from that reference.

Recommended schema:

```sql
CREATE TABLE IF NOT EXISTS content_references (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_doc_uid TEXT NOT NULL,
    source_location_type TEXT NOT NULL CHECK (source_location_type IN ('chunk', 'section')),
    source_chunk_id TEXT,
    source_chunk_db_id INTEGER,
    source_section_id TEXT,
    source_section_db_id INTEGER,
    reference_order INTEGER NOT NULL,
    annotation_raw_text TEXT NOT NULL,
    target_raw_text TEXT NOT NULL,
    target_kind TEXT NOT NULL,
    target_doc_hint TEXT,
    resolved_target_doc_uid TEXT,
    target_start TEXT,
    target_end TEXT,
    target_start_lookup TEXT,
    target_end_lookup TEXT,
    resolution_status TEXT NOT NULL,
    parsed_ok INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source_chunk_db_id) REFERENCES chunks(id) ON DELETE CASCADE,
    FOREIGN KEY (source_section_db_id) REFERENCES sections(db_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS content_reference_targets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reference_id INTEGER NOT NULL,
    target_doc_uid TEXT NOT NULL,
    target_chunk_id TEXT NOT NULL,
    target_chunk_db_id INTEGER NOT NULL,
    target_chunk_number TEXT NOT NULL,
    target_order INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (reference_id) REFERENCES content_references(id) ON DELETE CASCADE,
    FOREIGN KEY (target_chunk_db_id) REFERENCES chunks(id) ON DELETE CASCADE
);
```

Add indexes:

- `idx_content_references_source_doc_uid`
- `idx_content_references_source_chunk_id`
- `idx_content_references_source_chunk_db_id`
- `idx_content_references_source_section_id`
- `idx_content_references_source_section_db_id`
- optionally `idx_content_references_target_kind`
- `idx_content_references_resolved_target_doc_uid`
- `idx_content_reference_targets_reference_id`
- `idx_content_reference_targets_target_doc_uid`
- `idx_content_reference_targets_target_chunk_db_id`

The duplicate source id/db id fields are intentional:

- source ids are stable extraction identifiers useful before DB row ids exist
- DB ids support fast joins and cascade cleanup after persistence

### Reference Model

Add a typed dataclass, for example `src/models/reference.py`:

```python
@dataclass
class ContentReference:
    source_doc_uid: str
    source_location_type: Literal["chunk", "section"]
    reference_order: int
    annotation_raw_text: str
    target_raw_text: str
    target_kind: str
    target_doc_hint: str | None = None
    resolved_target_doc_uid: str | None = None
    target_start: str | None = None
    target_end: str | None = None
    target_start_lookup: str | None = None
    target_end_lookup: str | None = None
    resolution_status: str = "unresolved"
    parsed_ok: bool = False
    source_chunk_id: str | None = None
    source_chunk_db_id: int | None = None
    source_section_id: str | None = None
    source_section_db_id: int | None = None
    id: int | None = None
    resolved_targets: list[ContentReferenceTarget] = field(default_factory=list)


@dataclass
class ContentReferenceTarget:
    target_doc_uid: str
    target_chunk_id: str
    target_chunk_db_id: int
    target_chunk_number: str
    target_order: int
    id: int | None = None
    reference_id: int | None = None
```

Keep `target_kind` as a string enum-like value unless the repo already has a preferred enum pattern. Initial values:

- `same_standard_paragraph`
- `basis_for_conclusions`
- `implementation_guidance`
- `illustrative_examples`
- `cross_document`
- `unknown`

### Extraction Result

Extend `ExtractedDocument` with:

```python
references: list[ContentReference] = field(default_factory=list)
```

References are produced during extraction with stable source ids. DB ids are filled in during storage after chunks/sections have been inserted.

Resolved target chunk rows are filled after the relevant target document chunks are present in the local database. If a target document has not been ingested yet, the reference row must remain stored with `resolution_status="missing_target_document"` or another explicit unresolved status so a later reingest/backfill can resolve it.

### Attachment Rules

Use the cleanest current abstraction:

- Inline `div.note.edu` inside a paragraph body attaches to that paragraph chunk.
- End-of-chunk `div.note.edu` attached to or immediately following a paragraph attaches to that paragraph chunk.
- Top-of-section `div.note.edu` before paragraph content attaches to the active/nearest section.

Implementation detail:

- Prefer collecting note references while walking the same DOM stream in `_extract_structure()`.
- For notes nested under a paragraph node, attach during `_extract_chunk()` because the chunk id is available.
- For standalone notes encountered after a paragraph node, keep `last_chunk_by_section` or `last_emitted_chunk` traversal state and attach to that chunk when the note is a sibling immediately after paragraph content.
- For notes directly under a section/topic before child paragraphs, attach to the `SectionRecord` once that section has been registered.

If a note cannot be confidently attached, do not drop it silently. Emit a warning log with doc uid and note id, and skip persistence for that note in v1.

## Parsing Design

### Detect `Refer:` Annotations

Add a small IFRS-specific parser module, for example:

- `src/extraction/ifrs_references.py`

Responsibilities:

- detect whether a `Tag` is a `note edu` annotation with an `.edu_prefix` whose normalized text is `Refer:`
- extract the annotation raw text
- iterate each `a.xref` inside the annotation as one target reference
- preserve per-target raw anchor text
- infer context from surrounding prose in the same annotation, especially text before the anchor such as `Basis for Conclusions paragraphs`

Do not depend on the exact three supplied DOM shapes. The detector should work against:

- `span.note.edu`
- `div.note.edu`
- note with nested `p`
- linebreak spans
- prose separators like `and` and commas

### Raw Text Capture

Store both:

- `annotation_raw_text`: normalized full note text after bracket cleanup, for debugging and future resolver improvements
- `target_raw_text`: normalized anchor text, preserving prefixes such as `paragraphs` if the anchor contains them

Keep the existing chunk text stripping behavior by continuing to exclude `note edu` nodes from `_extract_body_lines_internal()`.

### Normalize Reference Text

Add a small normalizer with conservative behavior:

- normalize unusual IFRS word joiners and dash variants to a plain hyphen for parsing
- strip enclosing brackets
- strip leading `paragraph`, `paragraphs`, and similar labels while preserving the original `target_raw_text`
- parse single target into `target_start`
- parse range into `target_start` and `target_end`
- derive lookup keys such as `target_start_lookup` and `target_end_lookup` by stripping subparagraph suffixes that are not represented as chunk numbers, while preserving the exact parsed target
- detect explicit document hints such as `IAS 24`, `IFRS 9`, `IFRIC 16`

Examples:

- `paragraphs B4.1.7-B4.1.26` -> start `B4.1.7`, end `B4.1.26`, kind `same_standard_paragraph`
- `BC4.124-BC4.208` -> start `BC4.124`, end `BC4.208`, kind `basis_for_conclusions`
- `paragraph 4.1.1(a)` -> start `4.1.1(a)`, lookup start `4.1.1`, no end, kind `same_standard_paragraph`
- `IAS 24 paragraph 9` -> doc hint `IAS 24`, start `9`, kind `cross_document`

### Resolve Target Documents and Chunks

This slice must resolve targets to stored chunk ids where possible. The resolver should be conservative and deterministic.

Add a small resolver module, for example:

- `src/ingestion/reference_resolver.py` or `src/references/resolver.py`

Responsibilities:

- map `target_kind` and `target_doc_hint` to a target `doc_uid`
- resolve single paragraph references to matching `chunks.chunk_number`
- expand ranges to all matching chunks in document order
- persist one `content_reference_targets` row per resolved target chunk
- return an explicit `resolution_status` when resolution is partial or impossible

Initial document resolution rules:

- `same_standard_paragraph`: target doc uid is the source standard document, for example `ifrs9`.
- `basis_for_conclusions`: target doc uid is the same family BC document, for example `ifrs9-bc`.
- `implementation_guidance`: target doc uid is the same family IG document, for example `ifrs9-ig`.
- `illustrative_examples`: target doc uid is the same family IE document, for example `ifrs9-ie`.
- `cross_document`: derive doc uid from hints such as `IAS 24`, `IFRS 9`, `IFRIC 16`, plus target kind if the wording points to BC/IG/IE.

Family derivation should reuse existing document uid conventions and document type helpers from `src/models/document.py` where possible. Do not hardcode only IFRS 9.

Range expansion rules:

- match `target_start_lookup` and `target_end_lookup` against `chunks.chunk_number` in the resolved target document
- when no cleanup is needed, the lookup values should equal `target_start` and `target_end`
- do not order ranges by `chunks.id`; row ids are not a reliable semantic paragraph ordering guarantee
- build a semantic paragraph sort key from the stored `chunk_number` and use that for range inclusion
- include only chunks whose semantic paragraph key falls between the start and end keys
- make range comparison segment-aware so `4.1.10` is not included in `4.1.1-4.1.2`
- for appendix-style references such as `B4.1.7-B4.1.26`, use the repo's existing chunk numbering conventions rather than numeric-only parsing
- for BC ranges such as `BC4.1-BC4.45`, resolve against the BC document's chunk numbers
- handle letter-suffixed paragraphs such as `4.1.2A` explicitly; define ordering relative to `4.1.2` and `4.1.3` in tests before relying on it
- if either endpoint is missing, store the reference with a partial/unresolved status and any endpoint that could be resolved

Semantic sort key requirements:

- split paragraph numbers into prefix letters plus numeric dot-separated segments plus optional suffix letters
- compare numeric segments as integers, not strings
- compare `4.1.2` before `4.1.2A`
- compare `4.1.2A` before `4.1.3`
- compare `4.1.9` before `4.1.10`
- keep BC/B/IFRIC/IAS-style prefixes in the key so incompatible series are not mixed
- reject or mark `ambiguous` when start and end keys are from incompatible series

Suggested statuses:

- `resolved`
- `partially_resolved`
- `missing_target_document`
- `missing_start`
- `missing_end`
- `ambiguous`
- `parse_failed`

Do not use the resolved targets in retrieval in this slice.

## Implementation Phases

### Phase 1 - Add Models and Parser Unit Tests

Create focused parser tests before storage changes:

- `tests/unit/test_ifrs_references.py`

Cover:

- single same-document paragraph range
- multiple references in one annotation
- BC range classification
- cross-document hint such as `IAS 24 paragraph 9`
- IG/IE wording classification when present
- parser tolerance for nested `p`, commas, `and`, and linebreak spans

Expected assertions:

- reference count
- `annotation_raw_text`
- `target_raw_text`
- `target_start`
- `target_end`
- `target_doc_hint`
- `target_kind`
- `parsed_ok`

### Phase 2 - Add Migration and Store

Add:

- `src/migrations/015_create_content_references.sql`
- update `src/migrations/000_schema.sql` so fresh databases include the table
- `src/db/references.py` with `ContentReferenceStore`

Store API:

- `insert_references(references: list[ContentReference]) -> list[int]`
- `get_references_by_doc(doc_uid: str) -> list[ContentReference]`
- `delete_references_by_doc(doc_uid: str) -> int`
- `insert_reference_targets(reference_id: int, targets: list[ContentReferenceTarget]) -> list[int]`
- `get_reference_targets(reference_id: int) -> list[ContentReferenceTarget]`

Add tests:

- `tests/unit/test_db_references.py`

Verify:

- insert/get round trip
- one chunk source with multiple references
- resolved target chunk rows round trip
- section source support
- delete by document
- indexes/migration existence via `init_db()` if there is an existing migration smoke-test pattern

### Phase 3 - Wire Extraction

Update:

- `src/models/extraction.py`
- `src/extraction/ifrs_html_extractor.py`
- new parser module from Phase 1

Implementation approach:

- extend `_extract_structure()` to return `tuple[list[Chunk], list[SectionRecord], list[ContentReference]]`
- append references to `ExtractedDocument.references`
- preserve `section_closure_rows` behavior unchanged
- use existing stable ids for source attachment

Suggested traversal state addition:

```python
last_chunk: Chunk | None
last_chunk_by_section_id: dict[str, Chunk]
```

Use this only for standalone notes after chunk nodes. Inline notes inside paragraph bodies can be discovered from the paragraph body before note stripping.

Add extraction tests in `tests/unit/test_html_extraction.py` or a new targeted file:

- chunk-level inline note from Pattern 1
- chunk-level end note from Pattern 2
- section-level top note from Pattern 3

Keep the existing test that verifies note text is stripped from chunk text, but extend it to assert references are now extracted instead of lost.

### Phase 4 - Add Target Resolution

Add a resolver that runs after source references have source DB ids and after the target corpus chunks are available.

Implementation details:

- Use existing stored chunks as the target index.
- Add chunk-store queries needed for resolution, such as:
  - `get_chunks_by_doc(doc_uid: str) -> list[Chunk]` already exists.
  - add helper lookup functions only if they simplify range resolution.
- Resolve target document uid before chunk lookup.
- Resolve ranges into a list of target chunks, not just endpoint ids.
- Preserve unresolved reference rows with a concrete `resolution_status`.

Add tests for:

- same-document range resolves to multiple chunk ids
- `4.1.1-4.1.2` does not include `4.1.10`
- letter-suffixed paragraph ordering, for example `4.1.2`, `4.1.2A`, `4.1.3`
- subparagraph lookup cleanup, for example `4.1.1(a)` resolves to chunk number `4.1.1` while preserving `target_start="4.1.1(a)"`
- BC range resolves against `ifrs9-bc`
- IG/IE hints resolve against `ifrs9-ig` / `ifrs9-ie` when classification is inferable
- `IAS 24 paragraph 9` resolves against `ias24` when chunks exist
- missing target document stores `missing_target_document`
- missing endpoint stores `missing_start`, `missing_end`, or `partially_resolved`

### Phase 5 - Wire Persistence Through `StoreCommand`

Update interfaces and dependencies:

- add a `ReferenceStoreProtocol` in `src/interfaces.py`
- add `reference_store: ReferenceStoreProtocol | None` to `StoreDependencies`
- instantiate `ContentReferenceStore()` in `build_store_dependencies()`

Update `StoreCommand`:

- include references in `StorePayloadSnapshot`
- include references in skip-if-unchanged comparison
- after chunks and sections are stored, resolve DB ids:
  - map source chunk ids to inserted `Chunk.id`
  - use `section_db_id_by_source_id` from `_store_sections()`
- resolve target document and target chunk rows
- delete existing references for `doc_uid` before inserting replacement references
- insert resolved reference target rows after inserting parent reference rows
- insert references only when scope stores the required backing objects

Recommended policy:

- `scope="all"` stores references.
- `scope="chunks"` may store chunk-level references only if source chunk DB ids can be resolved.
- `scope="sections"` may store section-level references only if source section DB ids can be resolved.
- `scope="documents"` does not store references.

Document this behavior in code comments and tests because current `STORE_SCOPES` predates references.

Important ordering:

1. insert chunks
2. insert sections
3. sync chunk-section links
4. resolve reference source DB ids
5. resolve target doc uid and target chunks
6. delete and insert references
7. insert reference target rows
8. store embeddings

This keeps reference rows tied to the final chunk/section rows and lets cascading deletes work.

### Phase 6 - Integration Tests

Add or extend store command tests with fakes where practical:

- extracted document with one chunk-level reference persists through store
- extracted document with section-level reference persists through store
- multiple references from one annotation preserve `reference_order`
- resolved ranges persist one target row per target chunk
- cross-document targets persist the resolved target doc uid and chunk row
- unchanged-source skip compares reference payloads

If current fake store protocols make this too heavy, add lower-level integration tests using a temp DB and direct stores.

Minimum end-to-end evidence:

- run parser unit tests
- run DB reference tests
- run HTML extraction tests
- run relevant store command tests

### Phase 7 - Documentation

Lightly update:

- `docs/ENGINEERING_NOTES.md` or the most relevant ingestion documentation section
- `docs/JOURNAL.md`

Docs should say:

- IFRS HTML ingestion now parses explicit `Refer:` educational annotations.
- References are stored structurally, attached to chunks or sections, and linked to resolved target chunks where possible.
- Raw forms are preserved when normalization or target resolution is partial.
- Retrieval-time behavior is intentionally not changed yet.

## Edge Cases and Limitations

Expected v1 limitations:

- Context-sensitive target kind inference is best-effort.
- Target resolution depends on the relevant target document variant already being ingested.
- Cross-document resolution is limited to document hints that can be mapped to existing repo document uid conventions.
- Range expansion is based on a tested semantic paragraph sort key, not SQLite row ids or plain string ordering. Ambiguous or missing endpoints remain explicitly unresolved or partially resolved.
- Ambiguous unattached notes are logged and skipped rather than guessed.
- `Refer:` annotations remain excluded from chunk text, and retrieval does not consume the reference tables until a later retrieval change.

## Validation Checklist

Before finishing implementation:

- `uv run pytest tests/unit/test_ifrs_references.py -q`
- `uv run pytest tests/unit/test_db_references.py -q`
- `uv run pytest tests/unit/test_reference_resolver.py -q`
- `uv run pytest tests/unit/test_html_extraction.py -q`
- `uv run pytest tests/unit/test_store_command.py -q`
- `uv run ruff check src tests`
- `uv run ruff format --check src tests`

If full tests are too slow, run the focused tests above and state exactly what was not run.

## Deliverables

1. `ContentReference` model and parser for IFRS `Refer:` notes.
2. Database migration, baseline schema update, reference store, and resolved target table.
3. IFRS extraction changes that attach references to chunk or section sources.
4. Target resolver for same-variant, BC/IG/IE variant, cross-document, and range references.
5. Store command persistence wiring and skip comparison updates.
6. Focused parser, storage, resolver, extraction, and persistence tests.
7. Light docs and `docs/JOURNAL.md` entry.
8. Final summary covering stored fields, attachment rules, and v1 limitations.
