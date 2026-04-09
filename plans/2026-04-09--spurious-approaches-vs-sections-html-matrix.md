# Plan — Spurious approaches vs retrieved sections HTML matrix

Date: 2026-04-09
Scope: visual inspection artifact for Q1 experiment runs

## Goal

Create a standalone HTML matrix that makes it easy to visually inspect whether **spurious emitted approaches** correlate with the **sections** from `ifrs9`, `ias21`, and `ifric16` that had at least one retrieved chunk in a run.

This artifact is for **run-level inspection**, not aggregate scoring.

## Agreed vocabulary

- A **chunk** in the project data model maps 1:1 to an IFRS **paragraph**.
- A **section** is a grouping of chunks/paragraphs.
- A chunk belongs to a section via `chunks.containing_section_id`.
- Section expansion does **not** retrieve parent sections.
- Section expansion means: when one chunk is retrieved by similarity, the sibling chunks from the same section are included too.

Because the artifact is section-oriented, it should represent:
- **which sections had at least one retrieved chunk** in a run,
- not which exact expanded sibling chunks were present.

## Output artifact

Write one standalone HTML file with embedded CSS and JS.

Suggested filename:
- `spurious_approaches_vs_sections_matrix.html`

The file should be easy to open locally in a browser with no external dependencies.

## Row granularity

One row per **run**.

Examples:
- `Q1.0/base`
- `Q1.0/repeat-1`
- `Q1.0/repeat-2`

## Column granularity

### Label columns
Use one binary column per emitted approach label.

Include:
- the 3 core labels,
- all spurious / alternative labels that appear in the analyzed runs.

This is important because we want to see both:
- which spurious label appeared,
- and which expected core labels disappeared.

### Section columns
Use one column per **section**, not per chunk.

A section column is identified by:
- `doc_uid`
- `section_id`

A section column is included **iff** at least one retrieved chunk from that section appears in at least one analyzed run.

So the matrix must **not** include all sections in a document.
It must include only the observed retrieved sections across the analyzed runs.

## Documents represented as section-column groups

Create separate grouped blocks for:
- `ifrs9`
- `ias21`
- `ifric16`

No other documents are in scope for this artifact.

## Section metadata source

Use the `sections` table for section metadata.

Relevant columns guaranteed/populated in current schema:
- `section_id`
- `title`
- `section_lineage`
- `position`

Use:
- `section_id` as the stable key,
- `title` / `section_lineage` for display,
- `position` for ordering within a document.

## Section-column inclusion rule

A `(doc_uid, section_id)` pair gets a column **only if**:
- there exists at least one run,
- with at least one retrieved chunk,
- whose `doc_uid` matches,
- and whose `containing_section_id` equals that `section_id`.

Exclude:
- sections never touched by retrieval,
- sections that exist in the DB but do not occur in the analyzed runs.

## Cell semantics for section columns

A section cell represents:

> the retrieved chunks in that run whose `containing_section_id` is that section.

Do **not** create a separate visual state for expansion-only chunks.
At section level, expansion is already absorbed by the section abstraction.

### Section cell text
Use a **score range** rounded to 2 decimals.

Rules:
- one retrieved chunk in that section → `0.58`
- multiple retrieved chunks in that section → `0.55–0.61`
- no retrieved chunks in that section → blank

The score range must be computed from the retrieved chunk scores only.

### Section cell tooltip
On hover, show:
- document uid,
- `section_id`,
- section `title`,
- full `section_lineage`,
- all retrieved chunks/paragraph numbers in that section,
- exact per-chunk scores,
- displayed score range.

## Header display for section columns

### Internal column key
Use:
- `doc_uid::section_id`

### Visible column label
Use a compact human-readable label derived from the section metadata.

Preferred display rule:
- start from `title`,
- disambiguate with `position` or lineage if needed.

The full lineage and section id should stay in the tooltip.

## Metadata columns

Keep a sticky metadata block on the left.

Recommended columns:
- `question`
- `run`
- `recommendation`
- `spurious_labels`
- `all_labels`

Optional:
- `valid`
- per-run score if useful for orientation

## Label cell rendering

Label cells are binary.

Recommended visual treatment:
- core labels: dark neutral fill when present,
- spurious labels: red fill when present,
- absent: blank.

## Section cell color encoding

Use the HTML cell background in addition to the score text.

### Hue by document
- `ifrs9` → blue
- `ias21` → orange
- `ifric16` → green

### Intensity by strength
Use the **maximum retrieved score** in the cell to drive intensity.

So a darker cell means the section had a stronger retrieved chunk in that run.

The visible text remains the range, e.g. `0.55–0.61`.

## Table structure

Use a 2-row header.

### Header row 1
Grouped blocks:
- metadata
- labels
- IFRS 9
- IAS 21
- IFRIC 16

### Header row 2
Actual column names:
- metadata field names,
- label names,
- section display labels.

## Ordering

### Row ordering modes
Support at least 2 views or sort modes.

#### 1. Question order
Sort by:
- question id,
- then base/repeat order.

This is best for debugging one question at a time.

#### 2. Spurious-first order
Sort by:
- rows with non-empty `spurious_labels` first,
- then `spurious_labels`,
- then question id,
- then run id.

This is best for visual pattern detection.

### Section column ordering
Within each document group, sort section columns by:
- `sections.position`,
- then `section_id` as tie-breaker.

## Controls / UX

Recommended HTML controls:
- toggle: show only rows with spurious labels,
- toggle: hide empty section columns,
- toggle per document block (`ifrs9`, `ias21`, `ifric16`),
- optional question text filter.

Sticky behavior:
- sticky top header,
- sticky left metadata columns.

## Interpretation goal

The matrix should make it possible to visually inspect patterns such as:
- runs where `foreign_currency_accounting` appears,
- whether those rows tend to light up in `ias21` sections,
- whether stable runs tend to include certain `ifric16` or `ifrs9` sections,
- whether missing core labels coincide with a different section mix.

## Final agreed design summary

The artifact is a **direct HTML table**, not Markdown and not a spreadsheet export.

It uses:
- one row per run,
- binary emitted-label columns,
- one column per observed retrieved section,
- only for `ifrs9`, `ias21`, and `ifric16`,
- score-range text inside section cells,
- background color for document identity and strength,
- section metadata from the `sections` table,
- and only sections that had at least one retrieved chunk in at least one run.
