# Experiments

This directory contains ad hoc evaluation harnesses, archived experiment runs, and Promptfoo regression archives.

## Promptfoo archived runs

Promptfoo regression runs should be archived under an explicit experiment directory, for example:

```text
experiments/<experiment_subdir>/runs/<timestamp>_<slug>/
```

When invoking the runner or Make target, you only need to pass the subfolder name such as `promptfoo_regression`. Relative values are resolved under `experiments/`.

Each experiment maintains a Promptfoo database under `.promptfoo/`, for example:

```text
experiments/<experiment_subdir>/.promptfoo/promptfoo.db
```

Each archived Promptfoo run contains:
- `run.json` — run metadata and forwarded Promptfoo arguments
- `artifacts/` — per-test prompt/response files written by `scripts/run_answer.py`

Artifact layout:

```text
artifacts/<family>/<variant>/<provider>/
  A-prompt.txt
  A-response.json
  B-prompt.txt
  B-response.json
  B-response.md
```

## Running archived Promptfoo evals

`EXPERIMENT_DIR` is mandatory so every run is explicitly attached to an experiment folder.

Run, browse, and inspect experiment-local Promptfoo history with:

```bash
make eval EXPERIMENT_DIR=promptfoo_regression
make eval-view EXPERIMENT_DIR=promptfoo_regression
make eval-list EXPERIMENT_DIR=promptfoo_regression
make eval-show EXPERIMENT_DIR=promptfoo_regression EVAL_ID=<eval-id>
```

Focused run examples:

```bash
make eval EXPERIMENT_DIR=promptfoo_regression FAMILY=Q1
make eval EXPERIMENT_DIR=promptfoo_regression VARIANT=Q1.0 PROVIDER="Mistral Large 3"
make eval EXPERIMENT_DIR=promptfoo_regression FAMILY=Q1 DESCRIPTION="Q1 mistral"
make eval EXPERIMENT_DIR=scratch_promptfoo FAMILY=Q1
```

Direct runner usage:

```bash
uv run python scripts/run_promptfoo_eval.py \
  --experiment-dir promptfoo_regression \
  --description "Q1 mistral" \
  -- --filter-metadata family=Q1 --filter-targets Mistral
```
