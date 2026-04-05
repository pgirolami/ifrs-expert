"""List command - list all documents or chunks in the database."""

import json
import sqlite3

from src.db import ChunkStore, init_db


class ListCommand:
    """List all documents or chunks in the database."""

    def __init__(self, doc_uid: str | None = None) -> None:
        """Initialize the list command."""
        self.doc_uid = doc_uid

    def execute(self) -> str:
        """Execute the list command and return results as JSON."""
        try:
            init_db()

            with ChunkStore() as store:
                if self.doc_uid:
                    chunks = store.get_chunks_by_doc(self.doc_uid)
                    return json.dumps(
                        [
                            {
                                "id": c.id,
                                "doc_uid": c.doc_uid,
                                "chunk_number": c.chunk_number,
                                "chunk_id": c.chunk_id,
                                "containing_section_id": c.containing_section_id,
                                "page_start": c.page_start,
                                "page_end": c.page_end,
                                "text": c.text,
                            }
                            for c in chunks
                        ],
                        indent=2,
                        ensure_ascii=False,
                    )
                docs = store.get_all_docs()
                return json.dumps(docs, indent=2)
        except (sqlite3.OperationalError, TypeError) as e:
            return f"Error: {e}"
