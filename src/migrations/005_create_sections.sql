CREATE TABLE IF NOT EXISTS sections (
    section_id TEXT PRIMARY KEY,
    doc_uid TEXT NOT NULL,
    parent_section_id TEXT,
    level INTEGER NOT NULL,
    title TEXT NOT NULL,
    section_lineage TEXT NOT NULL,
    embedding_text TEXT NOT NULL,
    position INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_sections_doc_uid ON sections(doc_uid);
CREATE INDEX IF NOT EXISTS idx_sections_parent_section_id ON sections(parent_section_id);
CREATE INDEX IF NOT EXISTS idx_sections_title ON sections(title);
