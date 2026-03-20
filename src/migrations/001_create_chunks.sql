-- Migration 001: Create chunks table

CREATE TABLE IF NOT EXISTS chunks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_uid TEXT NOT NULL,
    section_path TEXT NOT NULL,
    page_start TEXT NOT NULL,
    page_end TEXT NOT NULL,
    text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_chunks_doc_uid ON chunks(doc_uid);
CREATE INDEX IF NOT EXISTS idx_chunks_section_path ON chunks(section_path);
