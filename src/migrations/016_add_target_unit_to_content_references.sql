ALTER TABLE content_references ADD COLUMN target_unit TEXT NOT NULL DEFAULT 'paragraph';

UPDATE content_references
SET target_unit = CASE
    WHEN lower(trim(target_raw_text)) LIKE 'section %' OR lower(trim(target_raw_text)) LIKE 'sections %' THEN 'section'
    WHEN target_doc_hint IS NOT NULL AND target_start IS NULL AND target_end IS NULL THEN 'document'
    ELSE 'paragraph'
END;
