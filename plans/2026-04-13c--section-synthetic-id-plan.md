# Plan — introduce synthetic section PKs and enforce `(doc_uid, section_id)` uniqueness

## Goal

Fix section persistence so section identifiers are treated as **document-local** identifiers, not global ones.

Target state:

- `sections` has a synthetic primary key, e.g. `id INTEGER PRIMARY KEY`
- business uniqueness is enforced by `UNIQUE (doc_uid, section_id)`
- foreign-key-style references use the synthetic section row id, not raw `section_id`
- section closure rows and chunk-to-section references become robust even when two documents reuse the same `section_id`

## Problem statement

Today the schema assumes `section_id` is globally unique:

- `sections.section_id TEXT PRIMARY KEY`
- `section_closure PRIMARY KEY (ancestor_section_id, descendant_section_id)`
- code paths such as `get_descendant_section_ids(section_id)` are missing `doc_uid`

That assumption is false.

For Navis/EFL ingestion, `section_id` values are only unique **within a document**. Reusing the same anchor id in another document is valid.

Observed consequence:

- ingestion can fail with `sqlite3.IntegrityError: UNIQUE constraint failed: sections.section_id`
- even if inserts succeeded, descendant lookups and title retrieval would be ambiguous across documents

## Fixed design decisions

1. `section_id` remains persisted as the source/document-local identifier.
2. `sections` gets a synthetic row id used for relational references.
3. `(doc_uid, section_id)` is the true business key and must be enforced with a unique constraint.
4. `section_closure` should reference section rows by synthetic ids, not by raw section ids.
5. chunks should reference the containing section row by synthetic id for relational integrity.
6. raw `containing_section_id` may be retained temporarily for migration/debugging, but the durable relational link should be the synthetic id.
7. APIs that currently accept only `section_id` must be rewritten to work either with:
   - synthetic section ids, or
   - `(doc_uid, section_id)` when addressing source ids explicitly.

## Proposed schema

### `sections`

Add / migrate to:

- `id INTEGER PRIMARY KEY`
- `doc_uid TEXT NOT NULL`
- `section_id TEXT NOT NULL`
- `parent_section_db_id INTEGER NULL`
- existing metadata columns remain (`level`, `title`, `section_lineage`, `embedding_text`, `position`, etc.)
- `UNIQUE (doc_uid, section_id)`

Notes:

- `parent_section_id` should be replaced by `parent_section_db_id` for relational linkage.
- if keeping the original source parent id temporarily helps migration/debugging, store it under a clearly named legacy/source field, not as the main relational field.

### `section_closure`

Replace source-id-based closure keys with synthetic-id-based keys:

- `ancestor_section_db_id INTEGER NOT NULL`
- `descendant_section_db_id INTEGER NOT NULL`
- `depth INTEGER NOT NULL`
- `PRIMARY KEY (ancestor_section_db_id, descendant_section_db_id)`

Optional but useful denormalization:

- retain `doc_uid TEXT NOT NULL` for easier filtering and diagnostics

### `chunks`

Add a synthetic reference to sections:

- `containing_section_db_id INTEGER NULL`

Migration choice:

- keep `containing_section_id TEXT NULL` for a transition period if it is already used in debugging, fixtures, or output
- long-term retrieval logic should prefer `containing_section_db_id`

### title-vector id map

The title vector store already keys entries as `(doc_uid, section_id)` in memory. That is acceptable short-term because it is unambiguous.

Recommended future improvement:

- store title embeddings against synthetic section db ids in the FAISS id map payload
- or store `(doc_uid, section_id)` until section db ids are easy to resolve everywhere

Either is valid, but DB reads and closure expansion should ultimately use synthetic ids.

## Code changes required

### 1. Migrations

Add one or more new migrations that:

- create a new `sections_v2` table with synthetic PK + unique `(doc_uid, section_id)`
- create a new `section_closure_v2` table keyed by synthetic ids
- add `chunks.containing_section_db_id`
- backfill synthetic parent/closure/chunk links from existing rows
- swap tables / rename once data is migrated

Because SQLite has limited `ALTER TABLE` support, this likely means:

1. create replacement tables
2. copy/backfill data
3. recreate indexes
4. drop old tables
5. rename replacements

### 2. Models

Update section-related models so they distinguish:

- synthetic db id
- source `section_id`

Likely changes:

- `SectionRecord`
  - add `id: int | None`
  - add `parent_section_db_id: int | None`
  - keep `section_id: str`
- `SectionClosureRow`
  - replace source-id fields with db-id fields
  - optionally keep source-id fields only if needed for extraction-stage temporary mapping

### 3. Extraction flow

Extraction should continue producing source-local identifiers initially.

Recommended pattern:

- extractor returns sections with source `section_id` and source parent linkage info
- persistence layer resolves these into inserted section rows and synthetic ids
- closure rows are built or translated to synthetic ids during persistence

This avoids forcing extractors to know about database-generated ids.

### 4. `SectionStore`

Refactor `src/db/sections.py` to:

- insert sections and capture generated row ids
- resolve `(doc_uid, section_id) -> db id`
- persist parent linkage via `parent_section_db_id`
- persist closure rows via synthetic ids
- expose descendant lookups by synthetic section id
- optionally expose helper lookups by `(doc_uid, section_id)` for interoperability

Suggested interface additions:

- `get_section_by_source_id(doc_uid: str, section_id: str) -> SectionRecord | None`
- `get_descendant_section_db_ids(section_db_id: int) -> list[int]`
- `get_descendant_sections(section_db_id: int) -> list[SectionRecord]`
- `map_source_ids_to_db_ids(doc_uid: str, section_ids: list[str]) -> dict[str, int]`

Suggested interface removals or deprecations:

- `get_descendant_section_ids(section_id: str)`

### 5. Chunk storage / retrieval

Update chunk persistence and readers to use `containing_section_db_id`.

Impacted areas:

- `src/db/chunks.py`
- `src/models/chunk.py`
- `src/commands/store.py`
- retrieval pipeline logic that expands chunk hits to sections
- prompt/debug output that currently surfaces `containing_section_id`

Transition recommendation:

- keep both fields briefly
- read/write both where necessary
- gradually switch logic to `containing_section_db_id`

### 6. Title retrieval

Update title retrieval and section expansion logic so section matching is resolved unambiguously.

Impacted areas:

- `src/retrieval/title_retrieval.py`
- `src/retrieval/pipeline.py`
- `src/commands/query_titles.py`
- `src/commands/retrieve.py`
- `src/commands/answer.py`
- `src/vector/title_store.py` if we decide to move its map to synthetic ids

Minimum safe version:

- keep title search results as `(doc_uid, section_id)`
- resolve those to one synthetic section row before descendant expansion
- perform closure traversal with synthetic ids only

### 7. Interfaces and fakes

Update protocols and test fakes:

- `src/interfaces.py`
- `tests/fakes.py`

Anything assuming section identity is a single string key must be updated to use either:

- synthetic id, or
- `(doc_uid, section_id)`

## Migration strategy

## Phase 1 — schema introduction

Add new schema elements without removing old ones yet:

- synthetic section PK
- unique `(doc_uid, section_id)`
- synthetic closure references
- `chunks.containing_section_db_id`

Backfill all existing persisted rows.

## Phase 2 — dual-write / dual-read

Temporarily support both old and new section linkage while code is being migrated:

- writes populate synthetic references
- reads prefer synthetic references
- legacy source-id fields remain for compatibility/debugging

## Phase 3 — retrieval cutover

Switch retrieval, title search, and closure expansion to synthetic references only.

## Phase 4 — cleanup

Once all code paths are migrated:

- remove obsolete source-id-as-FK usage
- keep raw source `section_id` only as document metadata / external identifier

## Validation plan

### Unit tests

Add or update tests for:

1. two different docs can persist the same `section_id`
2. uniqueness still fails for duplicate `(doc_uid, section_id)` within the same doc
3. closure traversal returns descendants only for the correct synthetic section row
4. chunk-to-section linkage resolves to the correct section row when source ids overlap across docs
5. title retrieval resolves the correct section when `(doc_uid, section_id)` is returned

### Integration tests

Add or update tests covering:

1. ingest two docs sharing one or more section source ids
2. re-ingest same doc and verify replacement behavior still works
3. section expansion in retrieval remains document-local
4. answer pipeline still builds context correctly after migration

### Manual verification

Use representative Navis captures where anchor ids recur across documents.

Confirm:

- ingestion succeeds
- no false section collisions across documents
- descendant expansion stays within the matched document
- logs clearly identify both source ids and synthetic ids when useful

## Risks / watchpoints

1. **SQLite migration complexity**
   - table rebuilds must preserve existing data correctly
2. **Hidden assumptions in retrieval code**
   - many places currently compare plain string section ids
3. **Title-vector index compatibility**
   - old id-map data may need rebuild/migration
4. **Chunk compatibility**
   - if `containing_section_id` is used in JSON/debug output, changing it abruptly may break expectations
5. **Test fake drift**
   - in-memory fakes currently key sections by plain `section_id`

## Recommended execution order

1. add plan artifact
2. add failing tests for per-document section-id reuse
3. implement schema migration(s)
4. update section models and `SectionStore`
5. update chunk linkage to synthetic section ids
6. update retrieval/title expansion paths
7. update fakes and remaining tests
8. rebuild/revalidate title index if needed
9. run full ingest and retrieval validation

## Success criteria

The work is complete when:

- two documents can share the same source `section_id` without collision
- duplicate `(doc_uid, section_id)` within one document is rejected
- closure traversal and title retrieval are unambiguous
- chunk-to-section references use synthetic section row ids for relational integrity
- ingestion, query-titles, retrieve, and answer all still work end-to-end
