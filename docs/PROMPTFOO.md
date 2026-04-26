# Promptfoo Evaluation

This project uses Promptfoo as the main regression harness for the current Prompt A → Prompt B answer pipeline.

It helps detect regressions across:
- question phrasing variants within a family
- question families under `experiments/00_QUESTIONS/`
- answer-pipeline defaults and prompt changes
- retrieval-only guardrails and prompt changes
- whichever provider configurations are currently enabled in `promptfoo_src/base.answer.yaml` or `promptfoo_src/base.retrieve.yaml`

The same harness now also powers a retrieval-only suite for Q1. That suite does
not call any LLM. It runs `scripts/run_retrieve.py`, checks that the right
documents and sections are retrieved, and saves the exact text used for the
similarity search as a debug artifact for each question.

## Quick start

Run and inspect an experiment history with:

```bash
make eval EXPERIMENT_DIR=promptfoo_regression
make eval-retrieve EXPERIMENT_DIR=promptfoo_retrieval
make q1-retrieve-non-regression
make eval-view EXPERIMENT_DIR=promptfoo_regression
make eval-list EXPERIMENT_DIR=promptfoo_regression
make eval-show EXPERIMENT_DIR=promptfoo_regression EVAL_ID=<eval-id>
```

Focused runs against the same experiment database:

```bash
make eval EXPERIMENT_DIR=promptfoo_regression FAMILY=Q1
make eval EXPERIMENT_DIR=promptfoo_regression VARIANT=Q1.0 PROVIDER="OpenAI GPT 5.4 through Codex current answer defaults"
make eval EXPERIMENT_DIR=promptfoo_regression FAMILY=Q1 DESCRIPTION="Q1 codex smoke"
make eval EXPERIMENT_DIR=scratch_promptfoo FAMILY=Q1
```

The checked-in answer base config currently enables one OpenAI Codex provider stanza (`OpenAI GPT 5.4 through Codex current answer defaults`). Uncomment or add provider blocks in `promptfoo_src/base.answer.yaml` when you want cross-provider comparisons.

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
                ├── B-response.md
                └── B-response_faq.md
```

For retrieval runs, the provider also writes one plain-text artifact per
question at:

```text
experiments/<experiment_subdir>/runs/<timestamp>_<slug>/artifacts/<family>/<variant>/query_embedding.txt
```

That file contains only the exact text that was embedded for similarity search.

The `<config>` path component is derived from the effective Promptfoo provider
configuration. In practice this includes the staged `policy-config` path and,
when explicitly overridden for the run, `llm_provider` and other answer-command
settings.

Each archived run contains:
- `run.json` — run metadata and forwarded Promptfoo arguments
- `artifacts/` — per-test Prompt A/B inputs plus structured JSON, memo markdown, and FAQ markdown written by `scripts/run_answer.py`

## Config generation

The root `promptfooconfig.yaml` is generated from:
- `promptfoo_src/base.answer.yaml`
- `promptfoo_src/base.retrieve.yaml`
- `experiments/00_QUESTIONS/*/family.yaml`

`promptfoo_src/base.answer.yaml` is the shared home for the answer-suite Promptfoo provider defaults.
It carries the fixed `answer` command settings that should be explicit and
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

The checked-in defaults currently run the answer command through a staged policy
file (`./effective/policy.default.yaml`, copied from `config/policy.default.yaml`)
in document-first mode with section expansion enabled:
- `retrieval-mode: documents`
- `expand-to-section: true`

Artifact-output settings such as `output-dir` and `save-all` are not stored in
`promptfoo_src/base.answer.yaml`; they are managed by `scripts/run_promptfoo_eval.py`
through the run archive layout and `PROMPTFOO_ARTIFACTS_DIR`.

`promptfoo_src/base.retrieve.yaml` is the retrieval-only suite base config. It
uses `scripts/run_retrieve.py` as the `exec:` provider and does not call any LLM.

For retrieval tests, the important family-level contract lives in
`experiments/00_QUESTIONS/<family>/family.yaml` under `assert_retrieve`. The
config builder turns that simple declarative shape into the Promptfoo JavaScript
assertions used by the retrieve suite.

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
  --provider "OpenAI GPT 5.4 through Codex current answer defaults" \
  --description "Q1 codex"

uv run python scripts/run_promptfoo_eval.py \
  --experiment-dir promptfoo_retrieval \
  --suite retrieve \
  --family Q1 \
  --description "Q1 retrieval"

uv run python experiments/analysis/run_q1_retrieval_non_regression.py
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
- for Q1 retrieval runs, the required governing documents are in the top 5 and
  the required section/chunk ranges are present
- for Q1 retrieval runs, the exact embedded search text is saved in the run
  artifacts for inspection

LLM-graded rubric assertions are currently commented out in the checked-in family files, so the active suite relies on deterministic JSON/Javascript assertions.

## Related docs

- Main project overview: [`README.md`](../README.md)
- Methodology: [`docs/METHODOLOGY.md`](./METHODOLOGY.md)
- Experiment directory overview: [`experiments/EXPERIMENTS.md`](../experiments/EXPERIMENTS.md)

![Example PromptFoo run comparing 2 models](./images/PromptFoo-run.png)
