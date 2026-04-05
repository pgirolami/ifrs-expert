# Query titles experiment plan

- Worktree: `.worktrees/query-titles-plan`
- Branch: `feature/query-titles-plan`
- Date: 2026-04-05

## Goal

Experiment with a second retrieval path that embeds and searches **section titles** instead of paragraph body text.

This should be exposed as a new CLI command:

- `query` = current paragraph-text similarity
- `query-titles` = new section-title similarity

The answer pipeline should then be able to use either retrieval mode.

---

## What I found

### Current implementation

Relevant code today:

- `src/extraction/html.py`
  - only extracts `div.topic.paragraph[id]`
  - uses `td.paragraph_col1 .paranum > p` for `section_path`
  - uses `td.paragraph_col2 > .body` for paragraph text
  - does **not** retain enclosing section headings
- `src/models/chunk.py`
  - chunk only stores `section_path`, `source_anchor`, `text`, etc.
- `src/db/chunks.py`
  - DB only persists paragraph rows
- `src/vector/store.py`
  - single FAISS index + single id map
  - id map assumes `(doc_uid, chunk_id)`
- `src/commands/store.py`
  - stores chunk rows and chunk-text embeddings only
- `src/commands/query.py`
  - searches chunk-text embeddings only
- `src/commands/answer.py`
  - duplicates retrieval/selection logic from `query.py`
  - directly depends on chunk-text retrieval

### HTML selectors and structure

The two example files confirm the structure you described.

#### Paragraph rows

Selector already used today:

- `div.topic.paragraph[id]`

Inside each paragraph row:

- paragraph identifier: `td.paragraph_col1 .paranum > p`
- paragraph body: `td.paragraph_col2 > .body`

Examples:

- IFRS 9 paragraph `IFRS09_2.4`
- IFRS 9 paragraph `IFRS09_3.1.1`
- IFRIC 16 paragraph `IFRIC16_10`
- IFRIC 16 paragraph `IFRIC16_AG8`

#### Section title containers

Enclosing section headings are non-paragraph `div.topic` nodes with `nestedN` classes.

Examples:

- IFRS 9
  - `div.topic.nested2` -> `Chapter 2 Scope`
  - `div.topic.nested3` -> `Contracts to buy or sell non-financial items`
  - `div.topic.nested3` -> `3.1 Initial recognition`
  - `div.topic.nested2` -> `4.2 Classification of financial liabilities`
- IFRIC 16
  - `div.topic.nested2` -> `Background`
  - `div.topic.nested2` -> `Consensus`
  - `div.topic.nested3` -> `Nature of the hedged risk and amount of the hedged item for which a hedging relationship may be designated`
  - appendix area:
    - wrapper `div.nested2.appendices` -> not a real section node to keep
    - `div.topic.nested3` -> appendix heading container
    - `div.topic.nested4` -> `Amounts reclassified to profit or loss on disposal of a foreign operation (paragraphs 16 and 17)`

### Implied normalization rules from the expanded `__CHUNKS.json`

The desired `section_h` values appear to be normalized titles, not raw heading text.

Examples from the expanded fixtures:

- IFRS 9 `2.4`
  - raw heading path: `Chapter 2 Scope` -> `Contracts to buy or sell non-financial items`
  - desired `section_h`: `[
    "Scope"
  ]`
- IFRS 9 `3.1.1`
  - raw heading path: `Chapter 3 Recognition and derecognition` -> `3.1 Initial recognition`
  - desired `section_h`: `[
    "Recognition and derecognition",
    "Initial recognition"
  ]`
- IFRS 9 `4.2.1`
  - raw heading path: `Chapter 4 Classification` -> `4.2 Classification of financial liabilities`
  - desired `section_h`: `[
    "Classification",
    "Classification of financial liabilities"
  ]`
- IFRIC 16 `1`
  - desired `section_h`: `["Background"]`
- IFRIC 16 `10`
  - desired `section_h`: `[
    "Consensus",
    "Nature of the hedged risk and amount of the hedged item for which a hedging relationship may be designated"
  ]`
- IFRIC 16 `AG8`
  - desired `section_h`: `[
    "Appendix",
    "Amounts reclassified to profit or loss on disposal of a foreign operation (paragraphs 16 and 17)"
  ]`

So the parser likely needs to:

1. ignore the document title `h1`
2. remove chapter numbering prefixes like `Chapter 3 `
3. remove section numbering prefixes like `3.1 ` or `4.2 `
4. normalize appendix headings consistently with the example fixtures
5. keep unnumbered headings as-is

---

## Options considered

### Option A — store section lineage only on each chunk, build the title index by duplicating one title vector per chunk

### Shape

- add `section_lineage` to `Chunk`
- store `section_lineage` in `chunks`
- for title retrieval, embed the leaf title once per chunk

### Pros

- smallest schema change
- no separate `sections` table
- easy to bolt onto current `VectorStore`

### Cons

- duplicates the same section title many times for sections with many paragraphs
- biases retrieval toward long sections
- harder to inspect/debug section-level data
- hard to map one title hit back to a unique section node

### Verdict

Good for a spike, but weak as a real implementation.

---

### Option B — store chunk lineage plus a separate `sections` table + separate title index

### Shape

- add section lineage to `Chunk`
- persist paragraph rows with their enclosing hierarchy
- create unique section records for every non-document-title heading node in the document
- embed one vector per unique section node
- resolve title hits back to paragraph chunks through explicit section ancestry

### Pros

- title index contains one vector per actual section node
- no section-size weighting artifact
- easier to debug and inspect
- clean basis for both `query-titles` and `answer --retrieval-mode titles`
- keeps paragraph retrieval and title retrieval clearly separate

### Cons

- more schema and code changes
- requires a second FAISS index
- requires a mapping from section hits to descendant paragraph chunks

### Verdict

**Recommended.** This is the cleanest experiment that still fits the current architecture.

---

### Option C — skip DB changes for sections and build section nodes dynamically at query time from chunk rows

### Pros

- less persisted state
- avoids a new table

### Cons

- query-time grouping becomes more complex
- section anchors/metadata are harder to preserve
- re-computes the same structure repeatedly
- less observable/testable

### Verdict

Not recommended if we want to compare retrieval modes cleanly.

---

## Recommended implementation

## 1) Data model changes

### Chunk model

Rename the current chunk fields in code so they reflect the new semantics cleanly:

- current database row id field `chunk_id: int | None` -> `id: int | None`
- current `section_path` -> `chunk_number: str`
- new paragraph HTML id field `chunk_id: str`
- keep `containing_section_id: str | None`

This keeps the paragraph number (`chunk_number`) and the paragraph HTML id (`chunk_id`) separate, while avoiding a collision with the database primary key.

Example:

- `id=101`
- `chunk_number="3.1.1"`
- `chunk_id="IFRS09_3.1.1"`
- `containing_section_id="IFRS09_g3.1.1-3.1.2"`

### New section model

Add a new dataclass, e.g. `src/models/section_title.py`:

- `section_id: str`
- `doc_uid: str`
- `parent_section_id: str | None`
- `level: int`
- `title: str`
- `section_lineage: list[str]`
- `embedding_text: str`
- `position: int`

Recommended meaning:

- `section_id` = stable HTML id such as `IFRS09_g3.1.1-3.1.2`; never null
- `title` = leaf title only
- `section_lineage` = full normalized hierarchy from the top indexed section down to this section
- `embedding_text` = exactly the leaf title text sent to embeddings
- `position` = document order for deterministic traversal/output

This keeps the embeddings title-only while making hierarchy and descendant resolution explicit in the relational model.

### Database changes

#### Extend `chunks`

New migration:

- `004_rename_and_add_chunk_metadata.sql`

Rename columns:

- `section_path` -> `chunk_number`
- `source_anchor` -> `chunk_id`

Also rename the current code/model field for the row primary key from `chunk_id` to `id`.

Add column:

- `containing_section_id TEXT DEFAULT NULL`

#### New `sections` table

New migration:

- `005_create_sections.sql`

Suggested columns:

- `section_id TEXT PRIMARY KEY`
- `doc_uid TEXT NOT NULL`
- `parent_section_id TEXT`
- `level INTEGER NOT NULL`
- `title TEXT NOT NULL`
- `section_lineage TEXT NOT NULL`
- `embedding_text TEXT NOT NULL`
- `position INTEGER NOT NULL`
- `created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP`

Suggested indexes:

- `idx_sections_doc_uid`
- `idx_sections_parent_section_id`
- `idx_sections_title`

#### New `section_closure` table

New migration:

- `006_create_section_closure.sql`

Suggested columns:

- `ancestor_section_id TEXT NOT NULL`
- `descendant_section_id TEXT NOT NULL`
- `depth INTEGER NOT NULL`

Suggested indexes:

- unique index on `(ancestor_section_id, descendant_section_id)`
- `idx_section_closure_descendant`

Why keep both `section_lineage` and `embedding_text` on `sections`?

- `section_lineage` is the authoritative structured hierarchy, serialized as JSON text
- `embedding_text` is the exact leaf title sent to embeddings

---

## 2) HTML extraction changes

## Current problem

`HtmlExtractor._extract_chunks()` only looks at paragraph nodes, so it loses all section context.

## Proposed approach

Replace the current paragraph-only scan with a document-order traversal that maintains the active heading stack.

### Traversal rule

Walk the content root in document order and inspect `div` nodes with `nestedN` classes.

For each node:

- if it is a non-paragraph `div.topic.nestedN`, extract the normalized heading title, create a section record, and update the active stack at depth `N`
- if it is a paragraph `div.topic.paragraph.nestedN`, extract the paragraph number/body, assign its paragraph HTML id to `chunk_id`, and set `containing_section_id` from the current stack up to depth `N-1`

Important rule:

- extract **every** non-document-title heading node, regardless of nesting level, into the `sections` table and title index
- exclude only the top document title

### Heading extraction helpers

Add helpers roughly like:

- `_extract_heading_titles(node: Tag) -> list[str]`
- `_extract_nested_level(node: Tag) -> int | None`
- `_normalize_heading_title(title: str) -> str`
- `_strip_heading_prefix(title: str) -> str`

### Normalization behavior

- remove the trailing expand marker text
- normalize whitespace
- ignore the top-level document title
- strip prefixes like:
  - `Chapter 3`
  - `3.1`
  - `4.2`
  - `A1`
  - `D3.3 `
- preserve substantive text after the prefix
- normalize appendix headings so the stored hierarchy matches the example fixtures

### Output

`HtmlExtractor.extract()` should return:

- paragraph chunks with `chunk_id`, `chunk_number`, and `containing_section_id`
- section records for all indexed heading nodes
- closure rows describing ancestor/descendant relationships between sections

That likely means extending `ExtractedDocument` to include:

- `sections: list[SectionTitle]`
- `section_closure_rows: list[SectionClosureRow]`

PDF extraction can initially return:

- no section rows for indexed titles
- `sections=[]`
- `section_closure_rows=[]`

so the feature remains HTML-first.

---

## 3) Store command changes

## Current behavior

`StoreCommand` only persists paragraph chunks and stores chunk-text embeddings.

## Proposed behavior

For each document:

1. persist paragraph chunks
2. persist section rows
3. store paragraph-text embeddings in the existing chunk index
4. store section-title embeddings in a second title index

### Dependency changes

Extend `StoreDependencies` to include a `section_store` and `title_store`, or replace the current dependency set with more explicit stores.

Likely additions:

- `SectionStore`
- `TitleStore`

### Replace / skip logic

`skip_if_unchanged` should compare more than paragraph text.

At minimum include in the payload:

- `chunk_number`
- `chunk_id`
- `text`
- `containing_section_id`
- extracted section rows

If a heading changes but paragraph text does not, the document should be reprocessed.

### Delete / re-store behavior

When replacing an existing HTML doc:

- delete existing chunk rows for the doc
- delete existing section rows for the doc
- delete existing chunk embeddings for the doc
- delete existing title embeddings for the doc
- insert fresh rows/embeddings

### CLI output

I would keep the CLI output simple but include both counts.

Example:

- `Stored 428 chunks, 73 sections, 428 chunk embeddings, and 73 title embeddings for doc_uid=ifrs9`

---

## 4) Vector store changes

## Current problem

`VectorStore` is hard-wired to one index and one id map whose payload is `(doc_uid, chunk_id)`.

## Proposed change

Support separate indexes for different entity types.

### Simplest clean option

Keep the current chunk index behavior and add a second store for titles.

For example:

- chunk index:
  - `data/index/faiss.index`
  - `data/index/id_map.json`
- title index:
  - `data/index/faiss_titles.index`
  - `data/index/id_map_titles.json`

Title id map payload should be:

- `(doc_uid, section_id)` where `section_id` is the stable HTML section string id

### Better medium-term option

Introduce a parameterized vector store, e.g. by `index_name` or `entity_kind`, so we do not duplicate the FAISS plumbing.

But for this experiment, a dedicated `TitleVectorStore` is acceptable if it avoids risky refactoring.

### Query cache

The query embedding cache can remain shared because the embedding model + query string are the same.

---

## 5) New `query-titles` command

## CLI shape

Add a new subcommand in `src/cli.py`:

- `query-titles`

Recommended options:

- `-k/--k`
- `--json`
- `--min-score`

I would **not** reuse `--expand` and `--full-doc-threshold` initially, because title retrieval is section-based rather than neighbor-chunk-based.

## Retrieval behavior

1. search the title index
2. select top-k matching sections per document above `min_score`
3. resolve each section hit to paragraph chunks
4. return both the section hit metadata and the resolved paragraph chunks

### How to resolve a section hit to paragraph chunks

Use explicit section ancestry, not lineage-prefix matching.

For a matched section:

1. read all descendant section ids from `section_closure`
2. include paragraph chunks in the same `doc_uid` whose `containing_section_id` is one of those descendant section ids
3. preserve document order when formatting output

This makes parent section matches include paragraph chunks directly under that section and any paragraph chunks nested several levels below it.

Example:

- matched section: `IFRS09_0054` (`Recognition and derecognition`)
- included chunks:
  - paragraphs directly under `IFRS09_0054`
  - paragraphs under `IFRS09_g3.1.1-3.1.2`
  - paragraphs under descendants of `IFRS09_g3.1.1-3.1.2`
  - paragraphs under any other descendant sections of `IFRS09_0054`

### Overlap handling

If two matched sections in the same document overlap, dedupe paragraph chunks by `(doc_uid, chunk_id)` before output.

For the first version, that is sufficient.

## Output recommendation

### Verbose mode

Show the section hit first, then the resolved paragraph snippets.

### JSON mode

Return something like:

```json
[
  {
    "doc_uid": "ifrs9",
    "section_id": "IFRS09_g3.1.1-3.1.2",
    "section_lineage": ["Recognition and derecognition", "Initial recognition"],
    "title": "Initial recognition",
    "score": 0.8123,
    "chunks": [
      {
        "id": 101,
        "chunk_number": "3.1.1",
        "chunk_id": "IFRS09_3.1.1",
        "containing_section_id": "IFRS09_g3.1.1-3.1.2",
        "text": "..."
      }
    ]
  }
]
```

That keeps the experiment inspectable.

---

## 6) Answer command changes

## Current problem

`AnswerCommand` is tied directly to chunk-text retrieval logic and duplicates a lot of `QueryCommand` behavior.

## Recommended approach

Do **not** make `AnswerCommand` shell out to `query` or `query-titles`.

Instead, extract retrieval into shared services and let:

- `query` format text-retrieval results
- `query-titles` format title-retrieval results
- `answer` choose which retriever to use

## CLI/API option

Add an answer option like:

- `--retrieval-mode text`
- `--retrieval-mode titles`

Default:

- `text`

Possible future extension:

- `auto` = titles first, then fallback to text

But I would keep v1 to `text|titles` only.

## Titles mode behavior

When `--retrieval-mode titles` is chosen:

1. run title search
2. automatically expand each matched section to all descendant sections
3. collect all paragraph chunks within those sections
4. dedupe chunk ids across overlapping section matches
5. preserve paragraph order within each document
6. feed the resulting paragraph chunks into the existing prompt-building flow

### Prompt transparency

When using title retrieval, include the matched section path somewhere visible.

- chunk XML attributes, e.g. `matched_section="Recognition and derecognition > Initial recognition"`

That will make evaluation easier.

---

## 7) Suggested refactor boundary

Because `query.py` and `answer.py` already duplicate retrieval logic, this feature is a good moment to introduce a shared retrieval layer.

Suggested new module(s):

- `src/retrieval/chunk_retriever.py`
- `src/retrieval/title_retriever.py`
- `src/retrieval/models.py`

Shared concepts:

- retrieval options
- result selection (`top-k per doc`, `min_score`)
- chunk resolution through section ancestry
- formatting left to commands

This keeps the CLI commands thin and makes answer-mode switching straightforward.

---

## 8) Test plan

## Unit tests

### HTML extraction

Add assertions for exact hierarchy extraction from the example HTML files:

- IFRS 9
  - `2.4 -> ["Scope"]`
  - `3.1.1 -> ["Recognition and derecognition", "Initial recognition"]`
  - `4.2.1 -> ["Classification", "Classification of financial liabilities"]`
- IFRIC 16
  - `1 -> ["Background"]`
  - `10 -> ["Consensus", "Nature of the hedged risk and amount of the hedged item for which a hedging relationship may be designated"]`
  - `AG8 -> ["Appendix", "Amounts reclassified to profit or loss on disposal of a foreign operation (paragraphs 16 and 17)"]`

### DB round-trips

- chunk `chunk_id`, `chunk_number`, and `containing_section_id` survive insert/read
- section rows and closure rows survive insert/read

### Store command

- stores both paragraph chunks and section rows
- stores both chunk embeddings and title embeddings
- re-store detects hierarchy-only changes

### Query titles

- returns matched sections
- resolves descendant paragraph chunks correctly
- dedupes overlapping section matches

### Answer command

- `--retrieval-mode text` preserves current behavior
- `--retrieval-mode titles` uses title retrieval and passes resolved paragraph chunks into prompts

## Integration tests

- ingest HTML capture stores `chunk_id`, `chunk_number`, and `containing_section_id`
- title index exists after store
- `query-titles` over IFRS 9 returns `Scope` / `Initial recognition` sections as expected
- answer command works in both retrieval modes

---

## 9) Recommended implementation order

1. **Extraction + model**
   - rename chunk fields to `id`, `chunk_id`, and `chunk_number`, and add `containing_section_id`
   - extract every non-document-title heading from HTML
   - extend tests around the example chunk and section fixtures
2. **Schema**
   - rename chunk columns to `chunk_id` and `chunk_number`
   - add `sections` and `section_closure` tables + stores
3. **Store**
   - persist sections and closure rows
   - build title embeddings in a second index
4. **Retrieval service**
   - add title retriever and section-descendant chunk resolution
5. **CLI**
   - add `query-titles`
6. **Answer**
   - add `--retrieval-mode text|titles`
7. **Evaluation**
   - compare `query` vs `query-titles` on representative IFRS questions

---

## 10) Risks / open questions

### 1. Should title embeddings use only the leaf title or the full hierarchy path?

Recommendation: embed **only the leaf title**.

Reason:

- this keeps the experiment faithful to title-only similarity
- hierarchy and ambiguity resolution should come from the section tree and descendant chunk expansion, not from concatenated embedding text

### 2. Should parent section matches include descendant paragraphs?

Recommendation: yes.

Otherwise chapter-level matches would often return nothing useful.

### 3. Should PDFs participate?

Recommendation: not in v1.

Return `section_lineage=[]` and no title rows for PDF sources unless a PDF outline strategy already exists.

### 4. Should answer default to title retrieval?

Recommendation: no.

Keep `text` as default and make titles opt-in until we evaluate quality.

### 5. How much refactoring should happen now?

Recommendation: enough to share retrieval logic between `query`, `query-titles`, and `answer`, but not a full rewrite of the command layer.

---

## Final recommendation

Implement this as a **parallel title-retrieval path**, not as a replacement for the current chunk-text retrieval.

The cleanest path is:

- persist `chunk_id`, `chunk_number`, and `containing_section_id` on chunks
- add `sections` and `section_closure` tables for the heading tree
- build a second FAISS index for section-title embeddings using leaf titles only
- add `query-titles`
- make `answer` select `text` or `titles` retrieval through a shared retriever abstraction, with title mode automatically expanding to all chunks in matched sections

That gives you a real experiment with minimal ambiguity, preserves the current workflow, and makes the retrieval mode easy to compare head-to-head.
