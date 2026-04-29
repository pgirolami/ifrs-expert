# Experiment 46 — `standards_only_through_chunks__enriched` Q2 family retrieval eval

## Goal

Validate the Q1 retrieval policy `standards_only_through_chunks__enriched` against the full Q2 question family and confirm two things:

1. the target governing standards are always retrieved
2. the target paragraph ranges inside those standards are also present

## Setup

- Question family: [`experiments/00_QUESTIONS/Q2`](../00_QUESTIONS/Q2)
- Question variants: `Q2.0` through `Q2.4`
- Retrieval policy: `standards_only_through_chunks__enriched`
- Provider: `Q1 retrieval non-regression gate`
- Promptfoo config: [`./.promptfoo/promptfoo.yaml`](./.promptfoo/promptfoo.yaml)
- Diagnostic indexes:
  - [`diagnostics/document_routing_index.md`](./diagnostics/document_routing_index.md)
  - [`diagnostics/target_chunk_retrieval_index.md`](./diagnostics/target_chunk_retrieval_index.md)

## Results

The run in this experiment passed the full Q2 family on both diagnostics:

- Document routing: **5 / 5** questions had all target standards present
- Target chunk retrieval: **5 / 5** questions had all expected ranges present
