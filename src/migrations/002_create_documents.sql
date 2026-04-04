CREATE TABLE IF NOT EXISTS documents (
    doc_uid TEXT PRIMARY KEY,
    source_type TEXT NOT NULL,
    source_title TEXT NOT NULL,
    source_url TEXT,
    canonical_url TEXT,
    captured_at TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_documents_source_type ON documents(source_type);
CREATE INDEX IF NOT EXISTS idx_documents_canonical_url ON documents(canonical_url);
