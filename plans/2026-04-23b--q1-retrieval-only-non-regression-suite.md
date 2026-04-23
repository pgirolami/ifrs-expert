# Plan — Q1 retrieval-only non-regression suite (Promptfoo harness)

## Goal

Create a cheap, deterministic retrieval guardrail for Q1 that runs with Promptfoo infrastructure but never calls an LLM.

Primary regressions to catch:
- routing regressions
- ranking regressions
- glossary-enrichment regressions
- ingestion-related retrieval regressions

## V1 scope (smallest useful version)

Use Promptfoo as the execution harness for retrieval-only runs:
- provider calls `src.cli retrieve --json`
- same family/variant filtering model as existing evals
- dedicated retrieval suite separated from answer suite

V1 validates:
- expected governing authorities for Q1 are always surfaced
- rank/fan-out stay within fixed thresholds
- required citation chunks are present for selected authorities
- enriched retrieval remains non-regressive vs raw on glossary-sensitive targets
- single-run deterministic behavior only (no repeat loop)

Out of scope for V1:
- any LLM-based assertions
- answer correctness metrics
- broad multi-family rollout

## Harness design (Promptfoo-first)

### Suite split (must-have)

Add explicit suite separation so answer and retrieval evals do not mix:
- `answer` suite: current behavior, unchanged
- `retrieve` suite: new provider + retrieval assertions

Proposed structure:
- `promptfoo_src/base.answer.yaml` (existing base behavior moved here)
- `promptfoo_src/base.retrieve.yaml` (new retrieval provider)
- `scripts/build_promptfoo_config.py --suite answer|retrieve`

### Retrieval provider wrapper (must-have)

Add a Promptfoo wrapper script dedicated to retrieval execution:
- input: question text from Promptfoo prompt var
- provider options: `policy-config`, `retrieval-policy`, optional retrieval debug flags
- command path: `uv run python -m src.cli retrieve --policy-config ... --retrieval-policy ... --json`
- output: retrieval JSON only

## Inputs and fixtures

### Inputs
- question family: `experiments/00_QUESTIONS/Q1/Q1.*.txt`
- policy config: `config/policy.default.yaml`
- retrieval policies:
  - `standards_only_through_chunks__enriched` (primary gate)
  - `documents2_through_chunks__raw` and `documents2_through_chunks__enriched` (glossary sentinel)
- family-level retrieval assertions should be declarative, not raw Promptfoo JavaScript

### Fixtures (new)
- `tests/fixtures/retrieval/q1_retrieval_non_regression.yaml`

### Fixture file shapes

`tests/fixtures/retrieval/q1_retrieval_non_regression.yaml`

```yaml
common:
  suite: retrieve
  family: Q1
  policy_config: config/policy.default.yaml

scenarios:
  authority_gate:
    mode: absolute
    retrieval_policy: standards_only_through_chunks__enriched
    hard_gates:
      recall_at_5:
        ias39: 1.0
        ifrs9: 1.0
        ifric16: 1.0
      all_targets_in_top_5_rate: 1.0

  glossary_sentinel:
    mode: compare
    baseline_policy: documents2_through_chunks__raw
    candidate_policy: documents2_through_chunks__enriched
    hard_gates:
      non_regression:
        recall_at_5_per_authority: true
        all_targets_in_top_5_rate: true
```

`experiments/00_QUESTIONS/Q1/family.yaml`

```yaml
assert_retrieve:
  required_documents:
    - ifrs9
    - ifric16
    - ias39
  required_section_ranges:
    - document: ifrs9
      start: "6.3.1"
      end: "6.3.6"
    - document: ifrs9
      start: "6.5.1"
      end: "6.5.1"
    - document: ifric16
      start: "10"
      end: "13"
```

## Assertions

### Primary authority gate (must-have)

Against `standards_only_through_chunks__enriched`:
- `ias39`, `ifrs9`, `ifric16` present in 23/23 Q1 variants
- metadata checks:
  - `ias39` -> `IAS-S`
  - `ifrs9` -> `IFRS-S`
  - `ifric16` -> `IFRIC`
- hard gate thresholds come from fixture:
  - recall@5 per required authority
  - all-targets-in-top-5 rate
- citation coverage checks are declared in `assert_retrieve.required_section_ranges`
- `chunk_number` is the stable citation label and ranges are expanded to atomic labels by the checker
- if a corpus cannot provide stable `chunk_number` values, the checker should fail fast

### Glossary sentinel gate (must-have)

Compare raw vs enriched on full Q1:
- hard-gate non-regression from `scenarios.glossary_sentinel`:
  - recall@5 per required authority must not degrade
  - all-targets-in-top-5 rate must not degrade

## Variants

### Variants
- primary gate: all Q1 variants (`Q1.0`..`Q1.22`)
- glossary sentinel: all Q1 variants (`Q1.0`..`Q1.22`)

## Metrics and pass/fail

### Hard gates (blocking, V1 uses K=5)

- recall@5 for each required authority
  - computed per authority as: `queries where authority rank <= 5 / total queries`
  - evaluated directly in Promptfoo assertions by checking target rank in retrieval JSON
  - threshold source:
    - absolute gate: `scenarios.authority_gate.hard_gates.recall_at_5`
    - compare gate: `scenarios.glossary_sentinel.hard_gates.non_regression.recall_at_5_per_authority`
- all-targets-in-top-5 rate
  - computed as: `queries where all required authorities rank <= 5 / total queries`
  - reported as a percentage in summary outputs
  - threshold source:
    - absolute gate: `scenarios.authority_gate.hard_gates.all_targets_in_top_5_rate`
    - compare gate: `scenarios.glossary_sentinel.hard_gates.non_regression.all_targets_in_top_5_rate`

### Diagnostics (non-blocking, always reported)

- mean rank of each authoritative document
- average number of returned documents
- max number of returned documents
- MRR (mean reciprocal rank), computed over authoritative documents
- citation presence matrix by `chunk_number`
- first-hit rank for each required citation range
- these diagnostics are always computed; the fixture does not toggle them on or off

### Gate decision

Pass/fail is computed by retrieval post-processing:
- `PASS`: all hard-gate thresholds pass
- `FAIL`: any hard-gate threshold fails, any required citation is missing, or any authority metadata contract fails (`document_type`)

## Fit with current workflow

Keep existing Promptfoo scaffolding and add one retrieval lane:
- `make eval ...` remains answer-oriented by default
- add retrieval-specific entrypoint (example: `make eval-retrieve EXPERIMENT_DIR=... FAMILY=Q1`)
- keep existing run archive layout (`runs/<timestamp>_*`, Promptfoo UI, filters)
- run retrieval summary/checker after Promptfoo run to compute deterministic gate verdict

This gives:
- existing UI and concurrency
- existing family/variant selection
- no duplication of run orchestration

## Failure artifacts

Write retrieval regression artifacts under the run directory:
- `runs/<run_id>/retrieval/summary.json`
- `runs/<run_id>/retrieval/summary.md`
- `runs/<run_id>/retrieval/target_matrix.md`
- `runs/<run_id>/retrieval/citation_matrix.md`
- `runs/<run_id>/retrieval/raw/Q1.x.retrieve.json`
- `runs/<run_id>/retrieval/effective_inputs.json`

Artifacts must identify failure category: routing, ranking, glossary, or ingestion.
When a citation gate fails, artifacts must also identify missing `chunk_number` labels.

## Implementation steps and deliverables

### Step 1 — Promptfoo suite split (must-have)
Deliverables:
- `promptfoo_src/base.answer.yaml`
- `promptfoo_src/base.retrieve.yaml`
- `scripts/build_promptfoo_config.py` updated with `--suite` and declarative retrieve-assertion translation
- docs note on suite selection

### Step 2 — Retrieval provider wrapper (must-have)
Deliverables:
- `scripts/run_retrieve.py` Promptfoo exec wrapper
- unit tests for option parsing, command wiring, and error payload shape

### Step 3 — Retrieval expectations and checker (must-have)
Deliverables:
- family-level `assert_retrieve.required_documents` and `assert_retrieve.required_section_ranges`
- retrieval checker script that reads Promptfoo retrieval outputs and computes gate metrics
- citation-range expansion from fixture ranges to atomic `chunk_number` labels
- `summary.json` + `summary.md` emission
- fixture for shared metric thresholds, scenario names, and output artifacts

### Step 4 — Workflow wiring (must-have)
Deliverables:
- Make targets for retrieval eval and retrieval gate
- concise README section with `answer` vs `retrieve` workflow

### Step 5 — Optional hardening (nice-to-have)
Deliverables:
- second policy gate (`documents2_through_chunks__enriched`)
- CI integration for retrieval gate

## What not to do yet

- no LLM calls in retrieval suite
- no attempt to force all aggregate metrics into Promptfoo native assertions
- no repeat runs for retrieval; keep single deterministic execution
- no full-rank snapshot testing for every non-target document
- no automatic threshold rewriting from latest run
- no expansion beyond Q1 until V1 is stable
