# Promptfoo Evaluation

This project uses Promptfoo as its regression suite for structured-answer quality.

Promptfoo helps ensure behavior remains stable across:
- question phrasing variants
- question families
- LLM providers and models
- changes in retrieval and prompting logic

## Promptfoo config

The root `promptfooconfig.yaml` is generated from:
- `promptfoo_src/base.yaml`
- `experiments/00_QUESTIONS/*/family.yaml`

When you update Promptfoo families or assertions, rebuild it with:

```bash
npm run eval:build
```

## Experiment-local Promptfoo databases

Promptfoo runs are always attached to an explicit experiment.

`EXPERIMENT_DIR` is required so each run is explicitly attached to an experiment folder.
For relative values, the runner automatically prefixes `experiments/`.

Each experiment gets its own Promptfoo database under:

```text
experiments/<experiment_subdir>/.promptfoo/promptfoo.db
```

Per-run provider artifacts are archived under:

```text
experiments/<experiment_subdir>/runs/<timestamp>_<slug>/
```

## Common commands

Run and inspect an experiment history with:

```bash
make eval EXPERIMENT_DIR=promptfoo_regression
make eval-view EXPERIMENT_DIR=promptfoo_regression
make eval-list EXPERIMENT_DIR=promptfoo_regression
make eval-show EXPERIMENT_DIR=promptfoo_regression EVAL_ID=<eval-id>
```

Focused runs against the same experiment database:

```bash
make eval EXPERIMENT_DIR=promptfoo_regression FAMILY=Q1
make eval EXPERIMENT_DIR=promptfoo_regression VARIANT=Q1.0 PROVIDER="Mistral Large 3"
make eval EXPERIMENT_DIR=promptfoo_regression FAMILY=Q1 DESCRIPTION="Q1 mistral smoke"
make eval EXPERIMENT_DIR=scratch_promptfoo FAMILY=Q1
```

Direct runner usage remains available when you need to forward raw Promptfoo arguments:

```bash
uv run python scripts/run_promptfoo_eval.py \
  --experiment-dir promptfoo_regression \
  --description "Q1 mistral" \
  -- --filter-metadata family=Q1
```

## Checks currently covered

The Promptfoo suite currently checks:
- valid JSON schema
- presence of expected approaches
- consistency of recommendation
- basic reasoning quality via an LLM-graded rubric

## Related docs

- Experiment archive conventions: [`experiments/EXPERIMENTS.md`](../experiments/EXPERIMENTS.md)
- Methodology: [`docs/METHODOLOGY.md`](./METHODOLOGY.md)

![Example PromptFoo run comparing 2 models](./PromptFoo-run.png)
