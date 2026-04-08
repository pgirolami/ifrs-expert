ALTER TABLE documents ADD COLUMN document_type TEXT;

UPDATE documents
SET document_type = CASE
    WHEN lower(doc_uid) LIKE 'ifrs%' THEN 'IFRS'
    WHEN lower(doc_uid) LIKE 'ias%' THEN 'IAS'
    WHEN lower(doc_uid) LIKE 'ifric%' THEN 'IFRIC'
    WHEN lower(doc_uid) LIKE 'sic%' THEN 'SIC'
    WHEN lower(doc_uid) LIKE 'ps%' THEN 'PS'
    ELSE NULL
END
WHERE document_type IS NULL;
