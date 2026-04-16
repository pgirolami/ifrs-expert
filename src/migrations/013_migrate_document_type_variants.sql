-- Migration 013: Migrate IAS/IFRIC/SIC/PS document types to include variants
-- Previously, documents with -bc, -ie, -ig suffixes were stored with their
-- base type (IAS, IFRIC, SIC, PS). This migration:
-- 1. Updates base IAS to IAS-S for consistency with IFRS-S
-- 2. Updates all variants to their explicit types (IAS-BC, IFRIC-BC, etc.)

-- First, update base IAS to IAS-S (for consistency with IFRS-S)
UPDATE documents SET document_type = 'IAS-S' WHERE document_type = 'IAS';

-- Update IAS variants
UPDATE documents SET document_type = 'IAS-BC' WHERE doc_uid LIKE 'ias%-bc' AND document_type = 'IAS-S';
UPDATE documents SET document_type = 'IAS-IE' WHERE doc_uid LIKE 'ias%-ie' AND document_type = 'IAS-S';
UPDATE documents SET document_type = 'IAS-IG' WHERE doc_uid LIKE 'ias%-ig' AND document_type = 'IAS-S';

-- Update IFRIC variants
UPDATE documents SET document_type = 'IFRIC-BC' WHERE doc_uid LIKE 'ifric%-bc' AND document_type = 'IFRIC';
UPDATE documents SET document_type = 'IFRIC-IE' WHERE doc_uid LIKE 'ifric%-ie' AND document_type = 'IFRIC';

-- Update SIC variants
UPDATE documents SET document_type = 'SIC-BC' WHERE doc_uid LIKE 'sic%-bc' AND document_type = 'SIC';
UPDATE documents SET document_type = 'SIC-IE' WHERE doc_uid LIKE 'sic%-ie' AND document_type = 'SIC';

-- Update PS variants
UPDATE documents SET document_type = 'PS-BC' WHERE doc_uid LIKE 'ps%-bc' AND document_type = 'PS';

-- Verify the changes: count documents by type after migration
SELECT 'Documents by type after migration' AS check_label;
SELECT document_type, COUNT(*) AS count FROM documents WHERE document_type IS NOT NULL GROUP BY document_type ORDER BY document_type;
