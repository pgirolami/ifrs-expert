-- Migration 014: Add explicit IFRIC implementation-guidance document type
-- IFRIC documents with an -ig suffix should be stored as IFRIC-IG rather than IFRIC.
-- Their document_kind should also be implementation_guidance.

UPDATE documents
SET
    document_type = 'IFRIC-IG',
    document_kind = 'implementation_guidance'
WHERE doc_uid LIKE 'ifric%-ig'
  AND document_type IN ('IFRIC', 'IFRIC-IG');
