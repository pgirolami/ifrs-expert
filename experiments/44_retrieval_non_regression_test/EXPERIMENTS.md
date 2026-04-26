# Experiment 44: Q1 retrieval non-regression test

## Goal

Build a cheap guardrail for Q1 retrieval that does not call any LLM.

The experiment now separates two things:

- document routing, meaning which governing standards are retrieved
- reference coverage, meaning which section ranges from those standards are present

## Setup

- Question family: [`experiments/00_QUESTIONS/Q1/family.yaml`](../00_QUESTIONS/Q1/family.yaml)
- Variants: `Q1.0` through `Q1.22`
- Harness: Promptfoo retrieval suite
- Provider wrapper: [`scripts/run_retrieve.py`](../../scripts/run_retrieve.py)
- Policy config: [`config/policy.default.yaml`](../../config/policy.default.yaml)
- Run directory: [`runs/2026-04-23_22-19-14_promptfoo-eval-family-q1/`](./runs/2026-04-23_22-19-14_promptfoo-eval-family-q1/)
- Document-level comparison artifact: [`q1-target-retrieval__documents2-through-chunks__exp43-vs-exp44.md`](./q1-target-retrieval__documents2-through-chunks__exp43-vs-exp44.md)

## What It Checks

For each Q1 variant, the suite checks:

- the expected governing documents are present in the top retrieval results
- the required section ranges are present in the retrieved chunks
- the exact text used for similarity search is saved as a plain-text artifact

The per-question artifact is stored at:

```text
runs/<timestamp>_<slug>/artifacts/Q1/<variant>/query_embedding.txt
```

That file contains only the embedded text. It is meant for quick inspection of
the enrichment step.

Example: the `Q1.0` artifact shows the original French question plus appended
English glossary terms such as `hedge accounting`, `dividend`, `receivable`,
`foreign exchange`, and `foreign currency`.

## Results

Document routing:

- The target-retrieval matrix comparison between experiments 43 and 44 shows
  no score or rank change for `IFRIC 16`, `IAS 39`, or `IFRS 9` on any Q1
  question.
- The document-routing layer still retrieves the same three governing standards
  for all 23 Q1 variants.

Reference coverage:

- Promptfoo eval ID: `eval-Syx-2026-04-23T22:19:17`
- Passed: **20 / 23**
- Failed: **3 / 23**
- Errors: **0**

The failing variants were:

- `Q1.5`: missing `IFRIC 16` sections `10` to `13`
- `Q1.15`: missing `IFRS 9` section `6.5.1` and `IFRIC 16` sections `10` to `13`
- `Q1.16`: missing `IFRS 9` section `6.5.1` and `IFRIC 16` sections `10` to `13`

So the current regression is not in the governing-document routing. It is in
the specific references that should be surfaced once those documents are
already retrieved. This is something we weren't checking before.

## Interpretation

- The retrieval harness is working without any LLM calls.
- The family-owned contract in `Q1/family.yaml` is now enforced directly by the
  retrieval eval.
- The new artifact output makes it much easier to inspect what text actually got
  embedded for a given question.
- The suite is catching missing reference coverage inside otherwise-correct
  document routing, which is the actual gap this experiment is meant to surface.

## Artifacts

- Promptfoo config used for the run: [`runs/2026-04-23_22-19-14_promptfoo-eval-family-q1/promptfooconfig.yaml`](./runs/2026-04-23_22-19-14_promptfoo-eval-family-q1/promptfooconfig.yaml)
- Run metadata: [`runs/2026-04-23_22-19-14_promptfoo-eval-family-q1/run.json`](./runs/2026-04-23_22-19-14_promptfoo-eval-family-q1/run.json)
- Staged effective config, including policy, glossary, and prompts: [`runs/2026-04-23_22-19-14_promptfoo-eval-family-q1/effective/`](./runs/2026-04-23_22-19-14_promptfoo-eval-family-q1/effective/)
- Provider artifacts: [`runs/2026-04-23_22-19-14_promptfoo-eval-family-q1/artifacts/`](./runs/2026-04-23_22-19-14_promptfoo-eval-family-q1/artifacts/)
- Document-routing comparison: [`q1-target-retrieval__documents2-through-chunks__exp43-vs-exp44.md`](./q1-target-retrieval__documents2-through-chunks__exp43-vs-exp44.md)
- Promptfoo logs: [`.promptfoo/logs/`](./.promptfoo/logs/)

## Document Routing Diagnostics

- Run `2026-04-23_22-19-14_promptfoo-eval-family-q1` covered 23 question(s).
- Provider: `Q1 retrieval non-regression gate`
- IFRS 9: 23/23 present
- IAS 39: 23/23 present
- IFRIC 16: 23/23 present
- IAS 21: 20/23 present
- IFRS 10: 13/23 present
- IFRS 7: 4/23 present
- IAS 32: 2/23 present
- IFRS 1: 2/23 present
- IFRS 18: 2/23 present
- IFRIC 2: 1/23 present
- IFRS 17: 1/23 present
- IFRS 19: 1/23 present
