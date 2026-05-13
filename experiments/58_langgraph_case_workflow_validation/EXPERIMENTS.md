# Experiment 58 — LangGraph case workflow validation

Date: 2026-05-13

## Purpose

Validate the LangGraph case-analysis migration against the existing IFRS Expert answer and retrieval eval harness without changing the corpus database or vector store.

## Runs

### Answer smoke — Q1.0 only

Command:

```bash
make eval-answer EXPERIMENT_DIR=58_langgraph_case_workflow_validation FAMILY=Q1 VARIANT=Q1.0 DESCRIPTION="LangGraph case workflow Q1.0 answer smoke"
```

Run directory:

```text
experiments/58_langgraph_case_workflow_validation/runs/2026-05-13_15-25-21_langgraph-case-workflow-q1-0-answer-smoke
```

Compliance note: this answer eval was filtered to `family=Q1` and `variant=Q1.0`; no other answer variants were run.

Result: PASS. Promptfoo completed the Q1.0 answer smoke with two attempts for stability diagnostics.

Key artifacts:

- `artifacts/Q1/Q1.0/.../A-prompt.txt`
- `artifacts/Q1/Q1.0/.../A-response.json`
- `artifacts/Q1/Q1.0/.../B-prompt.txt`
- `artifacts/Q1/Q1.0/.../B-response.md`
- `artifacts/Q1/Q1.0/.../B-response_faq.md`
- `diagnostics/approach_detection/approach_detection_diagnostics.md`

Diagnostics summary:

- Expected Prompt B approach labels were stable across both attempts: `cash_flow_hedge`, `fair_value_hedge`, and `hedge_of_a_net_investment` each appeared in 2/2 attempts.
- Q1.0 stability: strict 100.0%, loose 100.0%, missing expected labels 0, spurious labels 0.
- Authority categorization identified IFRS 9 hedge-accounting paragraphs as authoritative and IAS 21 / IFRIC 16 material as secondary context.

### Retrieval diagnostics — Q1 family

Command:

```bash
make eval-retrieve EXPERIMENT_DIR=58_langgraph_case_workflow_validation FAMILY=Q1 DESCRIPTION="LangGraph case workflow Q1 retrieval diagnostics"
```

Run directory:

```text
experiments/58_langgraph_case_workflow_validation/runs/2026-05-13_15-29-17_langgraph-case-workflow-q1-retrieval-diagnostics
```

Result: PASS. Promptfoo retrieval eval completed with 23/23 passing tests.

Diagnostics generated:

- `diagnostics/document_routing/document_routing_diagnostics.md`
- `diagnostics/target_chunk_retrieval/target_chunk_retrieval_diagnostics.md`

Diagnostics summary:

- Document routing retrieved all expected target documents for every Q1 variant: IFRS 9, IAS 39, IFRIC 16, and IAS 21 were present across 23/23 retrieval cases.
- Target chunk retrieval found all expected target ranges for every Q1 variant: IFRS 9 6.3.1-6.3.6, IFRS 9 B6.3.1-B6.3.6, and IFRIC 16 10-13 were each present in 23/23 cases.
- Q1.0 specifically retrieved 3/3 expected ranges.

## Assessment

PASS for this validation scope.

The LangGraph orchestration migration preserved the existing retrieval stack and answer-eval behavior for the constrained Q1.0 answer smoke. Retrieval diagnostics for the broader Q1 family show no target-document or target-range regression.

## Notable observations

- The first attempt to run retrieval diagnostics with `VARIANT=Q1.0` was insufficient for family-level diagnostic scripts because those scripts expect all Q1 cases. A family-level retrieval eval was run afterward; this does not violate the answer-eval restriction.
- Experiment directory was corrected from `34_langgraph_case_workflow_validation` to `58_langgraph_case_workflow_validation`; textual metadata references were updated accordingly.
