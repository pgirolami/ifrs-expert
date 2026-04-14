# Promptfoo Evaluation

This project uses Promptfoo as the main regression harness for the current Prompt A → Prompt B answer pipeline.

It helps detect regressions across:
- question phrasing variants within a family
- question families under `experiments/00_QUESTIONS/`
- retrieval defaults and prompt changes
- whichever provider configurations are currently enabled in `promptfoo_src/base.yaml`

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

The checked-in base config currently enables one MiniMax provider stanza. Uncomment or add provider blocks in `promptfoo_src/base.yaml` when you want cross-provider comparisons.

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
            └── <family>/<variant>/<config>/
                ├── A-prompt.txt
                ├── A-response.json
                ├── B-prompt.txt
                ├── B-response.json
                └── B-response.md
```

The `<config>` path component is derived from the effective Promptfoo provider
configuration. In practice this usually includes `llm_provider` and any
non-default answer-command settings that were overridden for that run.

Each archived run contains:
- `run.json` — run metadata and forwarded Promptfoo arguments
- `artifacts/` — per-test prompt/response files written by `scripts/run_answer.py`

## Config generation

The root `promptfooconfig.yaml` is generated from:
- `promptfoo_src/base.yaml`
- `experiments/00_QUESTIONS/*/family.yaml`

`promptfoo_src/base.yaml` is the shared home for Promptfoo provider defaults.
It now carries the fixed `answer` command settings that should be explicit and
stable across eval runs, such as:
- `k`
- `min-score`
- `d`
- `doc-min-score`
- per-document-type caps and min scores
- `content-min-score`
- `expand-to-section`
- `expand`
- `full-doc-threshold`
- `retrieval-mode`

The checked-in defaults currently run the answer command in document-first mode
with section expansion enabled:
- `retrieval-mode: documents`
- `expand-to-section: true`

Artifact-output settings such as `output-dir` and `save-all` are not stored in
`promptfoo_src/base.yaml`; they are managed by `scripts/run_promptfoo_eval.py`
through the run archive layout and `PROMPTFOO_ARTIFACTS_DIR`.

When you update Promptfoo families, assertions, or shared provider defaults,
rebuild it with:

```bash
npm run eval:build
```

## Direct runner usage

The direct runner remains available when you want to bypass the Makefile shortcuts:

```bash
uv run python scripts/run_promptfoo_eval.py \
  --experiment-dir promptfoo_regression \
  --family Q1 \
  --provider "MiniMax 2.7 High current answer defaults" \
  --description "Q1 minimax"
```

If you need raw Promptfoo flags, append them after `--`. In normal project usage,
prefer the `make` targets.

## What the suite checks

The Promptfoo suite currently checks:
- output matches `prompts/answer_prompt_B.json`
- core structured fields are present for the active French families
- family-specific expected approach coverage where applicable (for example Q1 hedge approaches)
- recommendation answers use the allowed enum and include a non-trivial justification
- each approach carries an applicability assessment and at least one reference

LLM-graded rubric assertions are currently commented out in the checked-in family files, so the active suite relies on deterministic JSON/Javascript assertions.

## Related docs

- Main project overview: [`README.md`](../README.md)
- Methodology: [`docs/METHODOLOGY.md`](./METHODOLOGY.md)
- Experiment directory overview: [`experiments/EXPERIMENTS.md`](../experiments/EXPERIMENTS.md)

![Example PromptFoo run comparing 2 models](./PromptFoo-run.png)
