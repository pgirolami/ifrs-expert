ALTER TABLE chunks RENAME COLUMN section_path TO chunk_number;
ALTER TABLE chunks RENAME COLUMN source_anchor TO chunk_id;
ALTER TABLE chunks ADD COLUMN containing_section_id TEXT DEFAULT NULL;

CREATE INDEX IF NOT EXISTS idx_chunks_chunk_number ON chunks(chunk_number);
CREATE INDEX IF NOT EXISTS idx_chunks_chunk_id ON chunks(chunk_id);
CREATE INDEX IF NOT EXISTS idx_chunks_containing_section_id ON chunks(containing_section_id);
