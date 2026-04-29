# Experiment 45 — `standards_only_through_chunks__enriched` Q1 family retrieval eval

## Goal

Validate the Q1 retrieval policy `standards_only_through_chunks__enriched` against the full Q1 question family and confirm two things:

1. the three target governing standards are always retrieved
2. the target paragraph ranges inside those standards are also present

The Q1 family is the intragroup FX hedge scenario set (`Q1.0` … `Q1.22`).

## Setup

- Question family: [`experiments/00_QUESTIONS/Q1`](../00_QUESTIONS/Q1)
- Question variants: `Q1.0` through `Q1.22`
- Retrieval policy: `standards_only_through_chunks__enriched`
- Provider: `Q1 retrieval non-regression gate`
- Promptfoo config: [`./.promptfoo/promptfoo.yaml`](./.promptfoo/promptfoo.yaml)
- Run artifacts: [`./runs/2026-04-29_09-16-57_promptfoo-eval-family-q1/`](./runs/2026-04-29_09-16-57_promptfoo-eval-family-q1/)
- Diagnostic indexes:
  - [`diagnostics/document_routing_index.md`](./diagnostics/document_routing_index.md)
  - [`diagnostics/target_chunk_retrieval_index.md`](./diagnostics/target_chunk_retrieval_index.md)

## Results

The later run in this experiment passed the full Q1 family on both diagnostics:

- Document routing: **23 / 23** questions had all target standards present
- Target chunk retrieval: **23 / 23** questions had all expected ranges present

### Target standards

The policy consistently retrieved all three target standards:

- `IFRS 9`
- `IAS 39`
- `IFRIC 16`

### Target chunk coverage

Expected ranges were present for all 23 questions:

- `IFRS 9` sections `6.3.1`–`6.3.6`: **23 / 23**
- `IFRS 9` appendix sections `B6.3.1`–`B6.3.6`: **23 / 23**
- `IFRIC 16` sections `10`–`13`: **23 / 23**

### Routing shape

The document-routing diagnostics show the retrieved set stayed compact and stable:

- `IFRS 9`: **23 / 23**
- `IAS 39`: **23 / 23**
- `IFRIC 16`: **23 / 23**
- `IAS 21`: **11 / 23**
- `IFRS 7`: **3 / 23**
- `IFRS 18`: **2 / 23**
- `IFRIC 17`: **2 / 23**
- `IFRS 1`: **2 / 23**
- `IFRS 17`: **2 / 23**
- `IFRS 19`: **2 / 23**
- `IFRS 10`: **1 / 23**

Every question retrieved **5 documents** total.

## Interpretation

- The Q1 family is now fully covered by the `standards_only_through_chunks__enriched` policy.
- The three governing standards are not only routed correctly, but the exact Q1 target ranges are also recovered every time.
- `IFRS 9` and `IAS 39` are extremely stable at the top of the result set.
- `IFRIC 16` is consistently retained, which is the key non-trivial part of the family.
- The extra retrieved standards are limited and mostly appear as lower-frequency support documents rather than competing targets.

## Diagnostics

- Document routing diagnostics markdown: [`runs/2026-04-29_09-16-57_promptfoo-eval-family-q1/diagnostics/document_routing/document_routing_diagnostics.md`](./runs/2026-04-29_09-16-57_promptfoo-eval-family-q1/diagnostics/document_routing/document_routing_diagnostics.md)
- Document routing diagnostics JSON: [`runs/2026-04-29_09-16-57_promptfoo-eval-family-q1/diagnostics/document_routing/document_routing_diagnostics.json`](./runs/2026-04-29_09-16-57_promptfoo-eval-family-q1/diagnostics/document_routing/document_routing_diagnostics.json)
- Target chunk retrieval diagnostics markdown: [`runs/2026-04-29_09-16-57_promptfoo-eval-family-q1/diagnostics/target_chunk_retrieval/target_chunk_retrieval_diagnostics.md`](./runs/2026-04-29_09-16-57_promptfoo-eval-family-q1/diagnostics/target_chunk_retrieval/target_chunk_retrieval_diagnostics.md)
- Target chunk retrieval diagnostics JSON: [`runs/2026-04-29_09-16-57_promptfoo-eval-family-q1/diagnostics/target_chunk_retrieval/target_chunk_retrieval_diagnostics.json`](./runs/2026-04-29_09-16-57_promptfoo-eval-family-q1/diagnostics/target_chunk_retrieval/target_chunk_retrieval_diagnostics.json)

## Artifacts

- Run metadata: [`runs/2026-04-29_09-16-57_promptfoo-eval-family-q1/run.json`](./runs/2026-04-29_09-16-57_promptfoo-eval-family-q1/run.json)
- Promptfoo config used by the experiment: [`./.promptfoo/promptfoo.yaml`](./.promptfoo/promptfoo.yaml)
- Promptfoo database: [`./.promptfoo/promptfoo.db`](./.promptfoo/promptfoo.db)
- Document-routing diagnostics index: [`diagnostics/document_routing_index.md`](./diagnostics/document_routing_index.md)
- Target-chunk diagnostics index: [`diagnostics/target_chunk_retrieval_index.md`](./diagnostics/target_chunk_retrieval_index.md)
- Earlier run captured in the experiment index: [`runs/2026-04-29_09-02-11_promptfoo-eval-family-q1/`](./runs/2026-04-29_09-02-11_promptfoo-eval-family-q1/)
