"""Document metadata storage for IFRS Expert."""

from __future__ import annotations

import logging
import sqlite3
from typing import Self

from src.db.connection import get_connection
from src.models.document import DocumentRecord, infer_document_type

logger = logging.getLogger(__name__)


class DocumentStore:
    """Manages document metadata in the database."""

    _conn: sqlite3.Connection

    def __enter__(self) -> Self:
        """Open the SQLite connection for document operations."""
        self._conn = get_connection()
        self._conn.row_factory = sqlite3.Row
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Close the SQLite connection for document operations."""
        self._conn.close()

    def upsert_document(self, document: DocumentRecord) -> None:
        """Insert or update a document record keyed by doc_uid."""
        document_type = document.document_type or infer_document_type(document.doc_uid)
        self._conn.execute(
            """
            INSERT INTO documents (
                doc_uid,
                source_type,
                source_title,
                source_url,
                canonical_url,
                captured_at,
                document_type,
                background_text,
                issue_text,
                objective_text,
                scope_text,
                intro_text,
                toc_text
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(doc_uid) DO UPDATE SET
                source_type = excluded.source_type,
                source_title = excluded.source_title,
                source_url = excluded.source_url,
                canonical_url = excluded.canonical_url,
                captured_at = excluded.captured_at,
                document_type = excluded.document_type,
                background_text = excluded.background_text,
                issue_text = excluded.issue_text,
                objective_text = excluded.objective_text,
                scope_text = excluded.scope_text,
                intro_text = excluded.intro_text,
                toc_text = excluded.toc_text,
                updated_at = CURRENT_TIMESTAMP
            """,
            (
                document.doc_uid,
                document.source_type,
                document.source_title,
                document.source_url,
                document.canonical_url,
                document.captured_at,
                document_type,
                document.background_text,
                document.issue_text,
                document.objective_text,
                document.scope_text,
                document.intro_text,
                document.toc_text,
            ),
        )
        self._conn.commit()
        logger.info(f"Upserted document metadata for doc_uid={document.doc_uid}")

    def get_document(self, doc_uid: str) -> DocumentRecord | None:
        """Fetch one document by doc_uid."""
        row = self._conn.execute(
            """
            SELECT
                doc_uid,
                source_type,
                source_title,
                source_url,
                canonical_url,
                captured_at,
                document_type,
                background_text,
                issue_text,
                objective_text,
                scope_text,
                intro_text,
                toc_text,
                created_at,
                updated_at
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
            document_type=row["document_type"],
            background_text=row["background_text"],
            issue_text=row["issue_text"],
            objective_text=row["objective_text"],
            scope_text=row["scope_text"],
            intro_text=row["intro_text"],
            toc_text=row["toc_text"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )
