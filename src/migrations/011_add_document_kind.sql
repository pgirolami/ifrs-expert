ALTER TABLE documents ADD COLUMN document_kind TEXT;

UPDATE documents
SET document_kind = CASE
    WHEN document_type IN ('IFRS', 'IFRS-S', 'IAS', 'PS') THEN 'standard'
    WHEN document_type IN ('IFRIC', 'SIC', 'NAVIS') THEN 'interpretation'
    WHEN document_type = 'IFRS-IG' THEN 'implementation_guidance'
    WHEN document_type = 'IFRS-IE' THEN 'illustrative_examples'
    WHEN document_type = 'IFRS-BC' THEN 'basis_for_conclusions'
    ELSE document_kind
END
WHERE document_kind IS NULL;
