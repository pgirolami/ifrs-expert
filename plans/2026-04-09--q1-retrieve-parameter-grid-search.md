# Plan — Q1 retrieve parameter grid search

Date: 2026-04-09
Experiment: `experiments/22_manual_experiment_on_document_routing`

## Goal

Find retrieve parameter combinations that make both `ifrs9` and `ifric16` appear with **at least one chunk** across the full Q1 family, while also ranking runs by:

```text
avg_overall_rank(ifrs9) + 2 * avg_overall_rank(ifric16)
```

Lower is better.

## Agreed scope

### Questions
- Evaluate only the 23 files under `experiments/00_QUESTIONS/Q1`.

### Retrieve mode and fixed options
Every retrieve call will explicitly pass:
- `--retrieval-mode=documents`
- `--json`
- `--k=1`
- `--d=100`
- `--content-min-score=0`
- `--expand=0`
- `--full-doc-threshold=0`

We will **not** use `--expand-to-section` for this search.

### Parameters to vary
Vary only:
- `--ifrs-d` in `2..8`
- `--ifrs-min-score` in `0.40, 0.45, 0.50, 0.55, 0.60`
- `--ifric-d` in `2..8`
- `--ifric-min-score` in `0.40, 0.45, 0.50, 0.55, 0.60`

### Parameters kept explicit at constant defaults
Use explicit values from `src/commands/constants.py` for the other document types:
- `--ias-d=5`
- `--sic-d=5`
- `--ps-d=5`
- `--ias-min-score=0.55`
- `--sic-min-score=0.51`
- `--ps-min-score=0.50`

## Search size

Parameter combinations:
- `7 * 5 * 7 * 5 = 1,225`

Retrieve calls across all 23 Q1 questions:
- `1,225 * 23 = 28,175`

## Success criterion

A parameter combination is **qualified** only if, for **every** Q1 question:
- `ifrs9` appears in `document_hits`
- `ifric16` appears in `document_hits`

`document_hits` is sufficient for this experiment; we do not need to inspect returned chunks.

## Per-question metrics to collect

For both `ifrs9` and `ifric16`, collect:
- whether the document appears in `document_hits`
- overall document rank and total number of returned documents
- rank within its document type group and total number of returned docs in that type group
- document score

## Per-run aggregates

For each parameter combination, aggregate over all 23 questions:
- document coverage count
- average overall rank
- average overall total
- average type rank
- average type total
- average score
- final ranking metric:
  - `avg_rank(ifrs9) + 2 * avg_rank(ifric16)`

Missing documents will receive a rank penalty of `total + 1` for sorting purposes.

## Output artifacts

### Per script invocation
Create a fresh temporary directory inside the experiment folder and print its full path to stdout.

### Per run
Store one JSON file per parameter combination in:
- `<temp_dir>/runs/`

Each filename will be based on a sanitized command line string, with a short hash suffix for uniqueness.

### Summary artifacts
Write:
- `<temp_dir>/q1_retrieve_parameter_grid_summary.md`
- `<temp_dir>/q1_retrieve_parameter_grid_summary.json`

## Markdown summary table

The summary markdown will show:
- best 5 runs
- worst 5 runs

Ordering:
- by `avg_overall_rank(ifrs9) + 2 * avg_overall_rank(ifric16)`
- lower is better

Primary ranking scope:
- qualified runs only
- if no runs qualify, fall back to all runs

Columns:
- section (`Best` / `Worst`)
- parameter values
- metric value
- qualified yes/no
- `IFRS 9 surfaced` (question count and average position)
- `IFRIC 16 surfaced` (question count and average position)
- `IFRS 9`
- `IFRIC 16`
- artifact filename

The two new surfaced columns will make examples like this directly visible in the row:
- `IFRS 9 surfaced`: `22 questions / avg pos 1.7`
- `IFRIC 16 surfaced`: `16 questions / avg pos 12.3`

Document cell format:

```text
document_coverage/23
avg_overall_rank/avg_total_hits
avg_type_rank/avg_type_total
avg_score
```

Use a newline as the separator between lines inside the cell, not a slash.
Keep slash only inside ratio-style values such as:
- `avg_overall_rank/avg_total_hits`
- `avg_type_rank/avg_type_total`

## Performance / UX requirements

### Progress bar
The script will display a terminal progress bar at the parameter-combination level.
`livebar` may be used for this instead of a custom renderer.

### Parallel execution
The script will execute combinations concurrently using multiple workers.
Current implementation target:
- default worker count = `min(8, cpu_count())`
- overridable via `--workers`

## Execution phases

### Phase 1 — quick validation run
Run only a small subset first so you can inspect the outputs quickly.
Planned command:

```bash
uv run python experiments/22_manual_experiment_on_document_routing/search_q1_retrieve_parameter_grid.py --limit 5
```

This will **not** append anything to `EXPERIMENTS.md` yet.

### Phase 2 — full run
After review of the quick validation output, run the full grid.
Planned command:

```bash
uv run python experiments/22_manual_experiment_on_document_routing/search_q1_retrieve_parameter_grid.py --append-experiments
```

This will append the generated markdown summary to:
- `experiments/22_manual_experiment_on_document_routing/EXPERIMENTS.md`

## Current status

### Already drafted
- A new grid-search script has been drafted:
  - `experiments/22_manual_experiment_on_document_routing/search_q1_retrieve_parameter_grid.py`

### Paused pending review
- I will not run the validation subset or full search until this plan is approved.
