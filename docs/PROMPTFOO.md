# Promptfoo Evaluation

This project uses Promptfoo as the main regression harness for structured-answer quality.

It helps detect regressions across:
- question phrasing variants
- question families
- LLM providers and models
- retrieval and prompting changes

## Quick start

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

## Operator rules

These are the important workflow rules for both humans and agents:

- Always use an explicit `EXPERIMENT_DIR`.
- In the Makefile workflow, you only provide `EXPERIMENT_DIR`.
- The Promptfoo config directory is derived internally as `<experiment>/.promptfoo`.
- Relative experiment paths are resolved under `experiments/`.
- Historical Promptfoo browsing happens per experiment, not globally.

## Storage model

Each experiment gets its own Promptfoo database under:

```text
experiments/<experiment_subdir>/.promptfoo/promptfoo.db
```

Per-run provider artifacts are archived under:

```text
experiments/<experiment_subdir>/runs/<timestamp>_<slug>/
```

Typical layout:

```text
experiments/<experiment_subdir>/
├── .promptfoo/
│   ├── promptfoo.db
│   └── ...
└── runs/
    └── <timestamp>_<slug>/
        ├── run.json
        └── artifacts/
            └── <family>/<variant>/<provider>/
                ├── A-prompt.txt
                ├── A-response.json
                ├── B-prompt.txt
                ├── B-response.json
                └── B-response.md
```

Each archived run contains:
- `run.json` — run metadata and forwarded Promptfoo arguments
- `artifacts/` — per-test prompt/response files written by `scripts/run_answer.py`

## Config generation

The root `promptfooconfig.yaml` is generated from:
- `promptfoo_src/base.yaml`
- `experiments/00_QUESTIONS/*/family.yaml`

When you update Promptfoo families or assertions, rebuild it with:

```bash
npm run eval:build
```

## Direct runner usage

The direct runner remains available when raw Promptfoo arguments need to be forwarded:

```bash
uv run python scripts/run_promptfoo_eval.py \
  --experiment-dir promptfoo_regression \
  --description "Q1 mistral" \
  -- --filter-metadata family=Q1¤ --filter-targets Mistral
```

In normal project usage, prefer the `make` targets.

## What the suite checks

The Promptfoo suite currently checks:
- valid JSON schema
- presence of expected approaches
- consistency of recommendation
- basic reasoning quality via an LLM-graded rubric

## Related docs

- Main project overview: [`README.md`](../README.md)
- Methodology: [`docs/METHODOLOGY.md`](./METHODOLOGY.md)
- Experiment directory overview: [`experiments/EXPERIMENTS.md`](../experiments/EXPERIMENTS.md)

![Example PromptFoo run comparing 2 models](./PromptFoo-run.png)
