# Experiment 47 — `standards_only_through_chunks__enriched` Q3 family retrieval eval

## Goal

Validate the Q1 retrieval policy `standards_only_through_chunks__enriched` against the full Q3 question family and confirm two things:

1. the target governing standards are always retrieved
2. the target paragraph ranges inside those standards are also present

## Setup

- Question family: [`experiments/00_QUESTIONS/Q2`](../00_QUESTIONS/Q3)
- Question variants: `Q3.0` through `Q3.9`
- Retrieval policy: `standards_only_through_chunks__enriched`
- Provider: `Q1 retrieval non-regression gate`
- Promptfoo config: [`./.promptfoo/promptfoo.yaml`](./.promptfoo/promptfoo.yaml)
- Diagnostic indexes:
  - [`diagnostics/document_routing_index.md`](./diagnostics/document_routing_index.md)
  - [`diagnostics/target_chunk_retrieval_index.md`](./diagnostics/target_chunk_retrieval_index.md)

## Results

The run in this experiment passed the full Q2 family on both diagnostics:

- Document routing: **10 / 10** questions had all target standards present
- Target chunk retrieval: **3 / 10** questions had all expected ranges present

## Analysis

The `B4.1.7-B4.1.26` chunk range was retrieved on every run because it's an implementation guideline so it matched the query text well. However, the `4.1.1-4.1.5` range was not and the terms used in expansion did not seem to make a difference: it's just the the text similarity wasn't close enough.

Fortunately, the annotated standards contain references. For example, the section containing the appendix sections retrieved references paragraphs 4.1.1(b), 4.1.2(b), 4.1.2A(b) and 4.1.3. So it is time to implement cross-reference expansion. But this requires ingesting the cross references first.