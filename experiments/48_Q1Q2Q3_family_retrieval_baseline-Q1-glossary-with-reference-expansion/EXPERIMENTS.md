# Experiment 48 — `standards_only_through_chunks__enriched` retrieval eval on Q1, Q2, Q3 families

## Goal

Validate that the new cross-reference expansion solves the recall problem on Q3

- Diagnostic indexes:
  - [`diagnostics/document_routing_index.md`](./diagnostics/document_routing_index.md)
  - [`diagnostics/target_chunk_retrieval_index.md`](./diagnostics/target_chunk_retrieval_index.md)

## Results

The runs in this experiment ran on Q1, Q2 and Q3.

Diagnostics show that target document & chunk recall is 100% for all variants across all families.