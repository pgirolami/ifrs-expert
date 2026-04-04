"""Document metadata storage for IFRS Expert."""

from __future__ import annotations

import logging
import sqlite3
from typing import Self

from src.db.connection import get_connection
from src.models.document import DocumentRecord

logger = logging.getLogger(__name__)


class DocumentStore:
    """Manages document metadata in the database."""

    _conn: sqlite3.Connection

    def __enter__(self) -> Self:
        self._conn = get_connection()
        self._conn.row_factory = sqlite3.Row
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        self._conn.close()

    def upsert_document(self, document: DocumentRecord) -> None:
        """Insert or update a document record keyed by doc_uid."""
        self._conn.execute(
            """
            INSERT INTO documents (
                doc_uid,
                source_type,
                source_title,
                source_url,
                canonical_url,
                captured_at
            ) VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(doc_uid) DO UPDATE SET
                source_type = excluded.source_type,
                source_title = excluded.source_title,
                source_url = excluded.source_url,
                canonical_url = excluded.canonical_url,
                captured_at = excluded.captured_at,
                updated_at = CURRENT_TIMESTAMP
            """,
            (
                document.doc_uid,
                document.source_type,
                document.source_title,
                document.source_url,
                document.canonical_url,
                document.captured_at,
            ),
        )
        self._conn.commit()
        logger.info(f"Upserted document metadata for doc_uid={document.doc_uid}")

    def get_document(self, doc_uid: str) -> DocumentRecord | None:
        """Fetch one document by doc_uid."""
        row = self._conn.execute(
            """
            SELECT doc_uid, source_type, source_title, source_url, canonical_url, captured_at, created_at, updated_at
            FROM documents
            WHERE doc_uid = ?
            """,
            (doc_uid,),
        ).fetchone()
        if row is None:
            return None
        return DocumentRecord(
            doc_uid=row["doc_uid"],
            source_type=row["source_type"],
            source_title=row["source_title"],
            source_url=row["source_url"],
            canonical_url=row["canonical_url"],
            captured_at=row["captured_at"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )
