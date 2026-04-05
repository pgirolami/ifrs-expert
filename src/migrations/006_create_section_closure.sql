CREATE TABLE IF NOT EXISTS section_closure (
    ancestor_section_id TEXT NOT NULL,
    descendant_section_id TEXT NOT NULL,
    depth INTEGER NOT NULL,
    PRIMARY KEY (ancestor_section_id, descendant_section_id)
);

CREATE INDEX IF NOT EXISTS idx_section_closure_descendant ON section_closure(descendant_section_id);
