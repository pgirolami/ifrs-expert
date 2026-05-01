# Experiment 49
## Goal

Validate that recall is still 100% on Q1, Q2 and Q3 after re-ingesting the whole IFRS corpus because it massively increases the amount of cross-references

- Diagnostic indexes:
  - [`diagnostics/document_routing_index.md`](./diagnostics/document_routing_index.md)
  - [`diagnostics/target_chunk_retrieval_index.md`](./diagnostics/target_chunk_retrieval_index.md)

## Results

The runs in this experiment ran on Q1, Q2 and Q3.

Diagnostics show that target document & chunk recall is 100% for all variants across all families.