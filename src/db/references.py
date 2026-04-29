"""Reference storage for IFRS annotation ingestion."""

from __future__ import annotations

import logging
import sqlite3
from typing import Self

from src.db.connection import get_connection
from src.models.reference import ContentReference

logger = logging.getLogger(__name__)


class ContentReferenceStore:
    """Manage parsed IFRS references in the database."""

    _conn: sqlite3.Connection

    def __enter__(self) -> Self:
        """Open a database connection for reference persistence."""
        self._conn = get_connection()
        self._conn.row_factory = sqlite3.Row
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Close the database connection."""
        self._conn.close()

    def insert_references(self, references: list[ContentReference]) -> list[int]:
        """Insert parsed references and return row ids."""
        ids: list[int] = []
        for reference in references:
            cursor = self._conn.execute(
                """
                INSERT INTO content_references (
                    source_doc_uid,
                    source_location_type,
                    source_chunk_id,
                    source_chunk_db_id,
                    source_section_id,
                    source_section_db_id,
                    reference_order,
                    annotation_raw_text,
                    target_raw_text,
                    target_kind,
                    target_doc_hint,
                    target_start,
                    target_end,
                    parsed_ok
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    reference.source_doc_uid,
                    reference.source_location_type,
                    reference.source_chunk_id,
                    reference.source_chunk_db_id,
                    reference.source_section_id,
                    reference.source_section_db_id,
                    reference.reference_order,
                    reference.annotation_raw_text,
                    reference.target_raw_text,
                    reference.target_kind,
                    reference.target_doc_hint,
                    reference.target_start,
                    reference.target_end,
                    1 if reference.parsed_ok else 0,
                ),
            )
            row_id = cursor.lastrowid
            if row_id is None:
                message = "SQLite did not return a lastrowid for inserted reference"
                raise sqlite3.OperationalError(message)
            reference.id = row_id
            ids.append(row_id)
        self._conn.commit()
        logger.info(f"Inserted {len(ids)} references into database")
        return ids

    def get_references_by_doc(self, doc_uid: str) -> list[ContentReference]:
        """Fetch all references for one document."""
        rows = self._conn.execute(
            """
            SELECT
                id,
                source_doc_uid,
                source_location_type,
                source_chunk_id,
                source_chunk_db_id,
                source_section_id,
                source_section_db_id,
                reference_order,
                annotation_raw_text,
                target_raw_text,
                target_kind,
                target_doc_hint,
                target_start,
                target_end,
                parsed_ok
            FROM content_references
            WHERE source_doc_uid = ?
            ORDER BY reference_order, id
            """,
            (doc_uid,),
        ).fetchall()
        return [_row_to_reference(row) for row in rows]

    def delete_references_by_doc(self, doc_uid: str) -> int:
        """Delete all references for one document."""
        cursor = self._conn.execute("DELETE FROM content_references WHERE source_doc_uid = ?", (doc_uid,))
        self._conn.commit()
        deleted = cursor.rowcount
        logger.info(f"Deleted {deleted} references for document {doc_uid}")
        return deleted


def _row_to_reference(row: sqlite3.Row) -> ContentReference:
    return ContentReference(
        id=row["id"],
        source_doc_uid=row["source_doc_uid"],
        source_location_type=row["source_location_type"],
        source_chunk_id=row["source_chunk_id"],
        source_chunk_db_id=row["source_chunk_db_id"],
        source_section_id=row["source_section_id"],
        source_section_db_id=row["source_section_db_id"],
        reference_order=row["reference_order"],
        annotation_raw_text=row["annotation_raw_text"],
        target_raw_text=row["target_raw_text"],
        target_kind=row["target_kind"],
        target_doc_hint=row["target_doc_hint"],
        target_start=row["target_start"],
        target_end=row["target_end"],
        parsed_ok=bool(row["parsed_ok"]),
    )
