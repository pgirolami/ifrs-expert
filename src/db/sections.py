"""Section storage and retrieval for IFRS Expert."""

from __future__ import annotations

import json
import logging
import sqlite3
from typing import Self

from src.db.connection import get_connection
from src.models.section import SectionClosureRow, SectionRecord

logger = logging.getLogger(__name__)


class SectionStore:
    """Manages section storage and retrieval in the database."""

    _conn: sqlite3.Connection

    def __enter__(self) -> Self:
        """Context manager entry."""
        self._conn = get_connection()
        self._conn.row_factory = sqlite3.Row
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Context manager exit."""
        self._conn.close()

    def insert_sections(self, sections: list[SectionRecord]) -> None:
        """Insert multiple sections."""
        if not sections:
            return

        self._conn.executemany(
            """
            INSERT INTO sections (
                section_id,
                doc_uid,
                parent_section_id,
                level,
                title,
                section_lineage,
                embedding_text,
                position
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    section.section_id,
                    section.doc_uid,
                    section.parent_section_id,
                    section.level,
                    section.title,
                    json.dumps(section.section_lineage, ensure_ascii=False),
                    section.embedding_text,
                    section.position,
                )
                for section in sections
            ],
        )
        self._conn.commit()
        logger.info(f"Inserted {len(sections)} sections into database")

    def insert_closure_rows(self, closure_rows: list[SectionClosureRow]) -> None:
        """Insert ancestor/descendant closure rows."""
        if not closure_rows:
            return

        self._conn.executemany(
            """
            INSERT INTO section_closure (
                ancestor_section_id,
                descendant_section_id,
                depth
            ) VALUES (?, ?, ?)
            """,
            [(row.ancestor_section_id, row.descendant_section_id, row.depth) for row in closure_rows],
        )
        self._conn.commit()
        logger.info(f"Inserted {len(closure_rows)} section closure rows into database")

    def get_sections_by_doc(self, doc_uid: str) -> list[SectionRecord]:
        """Get all sections for a document in document order."""
        rows = self._conn.execute(
            """
            SELECT section_id, doc_uid, parent_section_id, level, title, section_lineage, embedding_text, position
            FROM sections
            WHERE doc_uid = ?
            ORDER BY position, section_id
            """,
            (doc_uid,),
        ).fetchall()

        return [
            SectionRecord(
                section_id=row["section_id"],
                doc_uid=row["doc_uid"],
                parent_section_id=row["parent_section_id"],
                level=row["level"],
                title=row["title"],
                section_lineage=_decode_lineage(row["section_lineage"]),
                embedding_text=row["embedding_text"],
                position=row["position"],
            )
            for row in rows
        ]

    def get_descendant_section_ids(self, section_id: str) -> list[str]:
        """Return all descendant section ids including the matched section itself."""
        rows = self._conn.execute(
            """
            SELECT descendant_section_id
            FROM section_closure
            WHERE ancestor_section_id = ?
            ORDER BY depth, descendant_section_id
            """,
            (section_id,),
        ).fetchall()
        return [row["descendant_section_id"] for row in rows]

    def delete_sections_by_doc(self, doc_uid: str) -> int:
        """Delete sections and closure rows for one document."""
        section_rows = self._conn.execute(
            "SELECT section_id FROM sections WHERE doc_uid = ?",
            (doc_uid,),
        ).fetchall()
        section_ids = [row["section_id"] for row in section_rows]

        for section_id in section_ids:
            self._conn.execute(
                "DELETE FROM section_closure WHERE ancestor_section_id = ? OR descendant_section_id = ?",
                (section_id, section_id),
            )

        cursor = self._conn.execute("DELETE FROM sections WHERE doc_uid = ?", (doc_uid,))
        self._conn.commit()
        deleted = cursor.rowcount
        logger.info(f"Deleted {deleted} sections for document {doc_uid}")
        return deleted


def _decode_lineage(raw_value: str) -> list[str]:
    parsed = json.loads(raw_value)
    if not isinstance(parsed, list) or not all(isinstance(item, str) for item in parsed):
        msg = f"Invalid section_lineage payload: {raw_value}"
        raise ValueError(msg)
    return parsed
