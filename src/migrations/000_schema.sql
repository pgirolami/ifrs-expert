CREATE TABLE IF NOT EXISTS chunks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_uid TEXT NOT NULL,
    chunk_number TEXT NOT NULL,
    page_start TEXT NOT NULL,
    page_end TEXT NOT NULL,
    chunk_id TEXT NOT NULL DEFAULT '',
    text TEXT NOT NULL,
    containing_section_id TEXT DEFAULT NULL,
    containing_section_db_id INTEGER DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (containing_section_db_id) REFERENCES sections(db_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_chunks_doc_uid ON chunks(doc_uid);
CREATE INDEX IF NOT EXISTS idx_chunks_chunk_number ON chunks(chunk_number);
CREATE INDEX IF NOT EXISTS idx_chunks_chunk_id ON chunks(chunk_id);
CREATE INDEX IF NOT EXISTS idx_chunks_containing_section_id ON chunks(containing_section_id);
CREATE INDEX IF NOT EXISTS idx_chunks_containing_section_db_id ON chunks(containing_section_db_id);

CREATE TABLE IF NOT EXISTS documents (
    doc_uid TEXT PRIMARY KEY,
    source_type TEXT NOT NULL,
    source_title TEXT NOT NULL,
    source_url TEXT,
    canonical_url TEXT,
    captured_at TEXT,
    source_domain TEXT,
    document_type TEXT,
    document_kind TEXT,
    background_text TEXT,
    issue_text TEXT,
    objective_text TEXT,
    scope_text TEXT,
    intro_text TEXT,
    toc_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_documents_source_type ON documents(source_type);
CREATE INDEX IF NOT EXISTS idx_documents_canonical_url ON documents(canonical_url);

CREATE TABLE IF NOT EXISTS sections (
    db_id INTEGER PRIMARY KEY,
    doc_uid TEXT NOT NULL,
    section_id TEXT NOT NULL,
    source_parent_section_id TEXT,
    parent_section_db_id INTEGER,
    level INTEGER NOT NULL,
    title TEXT NOT NULL,
    section_lineage TEXT NOT NULL,
    position INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (doc_uid, section_id),
    FOREIGN KEY (parent_section_db_id) REFERENCES sections(db_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_sections_doc_uid ON sections(doc_uid);
CREATE INDEX IF NOT EXISTS idx_sections_parent_section_db_id ON sections(parent_section_db_id);
CREATE INDEX IF NOT EXISTS idx_sections_title ON sections(title);

CREATE TABLE IF NOT EXISTS section_closure (
    doc_uid TEXT NOT NULL,
    ancestor_section_db_id INTEGER NOT NULL,
    descendant_section_db_id INTEGER NOT NULL,
    depth INTEGER NOT NULL,
    PRIMARY KEY (ancestor_section_db_id, descendant_section_db_id),
    FOREIGN KEY (ancestor_section_db_id) REFERENCES sections(db_id) ON DELETE CASCADE,
    FOREIGN KEY (descendant_section_db_id) REFERENCES sections(db_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_section_closure_doc_uid ON section_closure(doc_uid);
CREATE INDEX IF NOT EXISTS idx_section_closure_descendant_db_id ON section_closure(descendant_section_db_id);
