# Plan — Q2 target-range headers and provenance display

## Goal

Keep the current target-chunk retrieval HTML matrix structure, but make the section columns easier to read for Q2 by:

- showing the exact target ranges from `family.yaml`
- still showing additional retrieved ranges inferred from the retrieved chunks
- exposing provenance so it is clear why a column is present and what kind of retrieval produced it

The target example is Q2, where the current family file declares:

- `ifrs9 B4.1.7-B4.1.9`
- `ifrs9 B4.1.10-B4.1.19`

The table should not require corpus-specific section identifiers to be the visible header label.

## Why this is needed

The current renderer is useful but confusing when a retrieved corpus section is broader than the exact target range.

Example:

- the family target is `B4.1.10-B4.1.19`
- the retrieved corpus section may be `gB4.1.10-B4.1.19`
- the retrieved set may also include a broader section such as `B4.1.7-B4.1.26`

Right now, the matrix can make that look like the target range and the broader retrieved range are separate unrelated targets, when in fact:

- the exact target range is what the evaluation cares about
- the broader retrieved range is an expansion artifact

We should make that distinction visible without changing the overall HTML layout.

## Current state

The current diagnostics stack already has a few useful pieces:

- target-chunk diagnostics are rendered by `experiments/analysis/target_chunk_retrieval/target_chunk_retrieval_contract.py`
- the table already marks expected columns with `🎯`
- retrieved chunks already carry a `provenance` field in the saved JSON
- the approach-detection matrix already uses emojis as a compact signal for authority category

The confusing part is not the presence of provenance data. The problem is that the visible section headers are derived from corpus section IDs, not from the exact expected ranges or an inferred retrieved-range view.

## Fixed decisions

### 1. Keep the HTML structure

Do not redesign the matrix.

Keep:

- the run metadata columns
- the emitted labels columns
- the section matrix
- the current markdown and JSON artifacts

The change should be mostly about labeling and provenance decoration.

### 2. Show exact expected target ranges explicitly

For Q2, render the exact `family.yaml` target ranges as the primary target headers.

Those headers should stay visible even if:

- a corpus section is broader
- the retrieved chunks only partially cover a section
- section expansion is enabled

This is important because section expansion is a configuration choice, not a guarantee that all chunks in a section are intended as the target.

### 3. Infer retrieved ranges from retrieved chunks

Build the visible retrieved-range columns from the retrieved chunks rather than from corpus section IDs.

Requirements for the inference step:

- ignore `Enn` chunks
- use the retrieved chunk numbers to infer the displayed range
- keep broader retrieved ranges if they are genuinely present
- do not collapse a broader retrieved range into a narrower target range

This lets the table show both:

- the exact required target ranges
- the other chunk ranges that were actually retrieved

### 4. Preserve corpus IDs as metadata

The corpus-specific section IDs are still useful, but only as secondary metadata.

They should appear in:

- tooltips
- JSON output
- possibly a small subtitle or note if needed

They should not be the primary visible header label when the exact target range is known.

### 5. Use emojis as compact provenance markers, not the full explanation

The existing `🎯` marker is already a compact signal that a column is target-related.

Use that pattern for provenance, but do not rely on emoji alone.

The plan is:

- keep `🎯` for exact target-range columns
- add small provenance markers for how a retrieved column was produced, if useful
- include the full provenance text in the tooltip and JSON

The emoji layer should be a quick visual cue, not the authoritative source of truth.

## Implementation plan

### 1. Separate expected ranges from inferred retrieved ranges

Update the target-chunk diagnostics renderer so it builds two logical sets of headers:

- exact expected ranges from `family.yaml`
- inferred retrieved ranges from the chunk payload

The matrix can still render them in one table, but they should be different concepts in the code.

### 2. Add range inference from retrieved chunks

Implement a helper that groups retrieved chunks into displayed ranges.

Recommended behavior:

- ignore `Enn` chunks
- derive ranges from chunk numbers
- preserve broader retrieved ranges when present
- keep the logic deterministic so diagnostics are reproducible

The inferred range should be based on the retrieval output, not on corpus section IDs.

### 3. Render exact target labels first

For each expected range:

- render the exact `start-end` label from `family.yaml`
- keep the `🎯` marker
- show provenance in the tooltip, such as whether the column was matched directly, expanded, or inferred from retrieved chunks

### 4. Render additional retrieved ranges separately

If a broader or different retrieved range exists, render it as its own column.

That column should explain:

- where it came from
- whether it was seed similarity, section expansion, or some other retrieval path
- which chunks support it

### 5. Surface provenance in a readable way

Use the current `provenance` field and existing emoji cues to display provenance compactly.

The most likely shape is:

- target columns: `🎯`
- seed similarity: one marker
- section expansion: one marker
- reference expansion, if present: one marker

The precise marker set can be chosen to keep the table readable, but the tooltip must include the explicit provenance string so the emojis are optional shorthand.

### 6. Update the diagnostics JSON and markdown consistently

The HTML is the visible artifact, but the underlying JSON and markdown should follow the same model.

That means:

- exact target ranges are explicit in JSON
- inferred retrieved ranges are explicit in JSON
- provenance is explicit in JSON
- markdown summary uses the same labels so the HTML and text stay aligned

### 7. Add a Q2 regression test

Add a focused test that covers the confusing case:

- target ranges are `B4.1.7-B4.1.9` and `B4.1.10-B4.1.19`
- retrieved chunks also imply a broader `B4.1.7-B4.1.26`
- `Enn` chunks are ignored for the inferred display ranges

The test should assert that:

- the exact target ranges are still visible
- the broader retrieved range still appears
- provenance text is present
- the corpus ID can still be shown in tooltip/metadata without becoming the visible header label

## Tests

Add or update tests for:

- exact target-range rendering in the header
- inferred retrieved-range grouping from chunk payloads
- ignoring `Enn` chunks during range inference
- provenance shown in tooltips / serialized diagnostics
- preserving the current HTML matrix structure

Likely test location:

- `tests/unit/test_target_chunk_retrieval_contract.py`

## Validation

- `make lint`
- the updated Q2 diagnostics render correctly for experiment 50
- the table shows exact target ranges and inferred retrieved ranges distinctly
- provenance is visible without making the matrix harder to read

## Scope limits

Keep this slice focused on diagnostics only.

Do not change retrieval behavior, corpus ingestion, or experiment definitions.
