-- Migration 012: Migrate IFRS document type to IFRS-S
-- IFRS was an alias for IFRS-S in earlier versions; this migration
-- updates any persisted document_type value to the canonical name.

-- Update documents table
UPDATE documents SET document_type = 'IFRS-S' WHERE document_type = 'IFRS';

-- Verify the change
SELECT 'IFRS documents remaining' AS check_label, COUNT(*) AS count FROM documents WHERE document_type = 'IFRS';
SELECT 'IFRS-S documents after migration' AS check_label, COUNT(*) AS count FROM documents WHERE document_type = 'IFRS-S';
