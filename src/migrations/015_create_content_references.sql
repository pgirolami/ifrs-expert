CREATE TABLE IF NOT EXISTS content_references (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_doc_uid TEXT NOT NULL,
    source_location_type TEXT NOT NULL CHECK (source_location_type IN ('chunk', 'section')),
    source_chunk_id TEXT,
    source_chunk_db_id INTEGER,
    source_section_id TEXT,
    source_section_db_id INTEGER,
    reference_order INTEGER NOT NULL,
    annotation_raw_text TEXT NOT NULL,
    target_raw_text TEXT NOT NULL,
    target_kind TEXT NOT NULL,
    target_doc_hint TEXT,
    target_start TEXT,
    target_end TEXT,
    parsed_ok INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source_chunk_db_id) REFERENCES chunks(id) ON DELETE CASCADE,
    FOREIGN KEY (source_section_db_id) REFERENCES sections(db_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_content_references_source_doc_uid ON content_references(source_doc_uid);
CREATE INDEX IF NOT EXISTS idx_content_references_source_chunk_id ON content_references(source_chunk_id);
CREATE INDEX IF NOT EXISTS idx_content_references_source_chunk_db_id ON content_references(source_chunk_db_id);
CREATE INDEX IF NOT EXISTS idx_content_references_source_section_id ON content_references(source_section_id);
CREATE INDEX IF NOT EXISTS idx_content_references_source_section_db_id ON content_references(source_section_db_id);
CREATE INDEX IF NOT EXISTS idx_content_references_target_kind ON content_references(target_kind);
