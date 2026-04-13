"""Section storage and retrieval for IFRS Expert."""

from __future__ import annotations

import json
import logging
import sqlite3
from collections import defaultdict
from dataclasses import dataclass
from typing import Self

from src.db.connection import get_connection
from src.models.section import SectionClosureRow, SectionRecord

logger = logging.getLogger(__name__)

MAX_LOGGED_SECTION_CONFLICTS = 20


@dataclass(frozen=True)
class ExistingSectionConflict:
    """One existing database row that conflicts with an incoming section id."""

    section_id: str
    doc_uid: str
    title: str
    position: int


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

        duplicate_sections = _find_duplicate_payload_sections(sections)
        if duplicate_sections:
            _log_duplicate_payload_sections(duplicate_sections)

        existing_conflicts = self._find_existing_section_conflicts(sections)
        if existing_conflicts:
            _log_existing_section_conflicts(sections=sections, conflicts=existing_conflicts)

        try:
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
        except sqlite3.IntegrityError:
            logger.exception(f"Failed to insert {len(sections)} sections due to a section_id integrity error")
            raise

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

    def _find_existing_section_conflicts(self, sections: list[SectionRecord]) -> list[ExistingSectionConflict]:
        """Find existing section rows whose ids conflict with the incoming payload."""
        conflicts: list[ExistingSectionConflict] = []
        unique_section_ids = sorted({section.section_id for section in sections})
        if not unique_section_ids:
            return conflicts

        for section_id in unique_section_ids:
            rows = self._conn.execute(
                """
                SELECT section_id, doc_uid, title, position
                FROM sections
                WHERE section_id = ?
                ORDER BY section_id, doc_uid
                """,
                (section_id,),
            ).fetchall()
            conflicts.extend(
                ExistingSectionConflict(
                    section_id=row["section_id"],
                    doc_uid=row["doc_uid"],
                    title=row["title"],
                    position=row["position"],
                )
                for row in rows
            )
        return conflicts


def _decode_lineage(raw_value: str) -> list[str]:
    parsed = json.loads(raw_value)
    if not isinstance(parsed, list) or not all(isinstance(item, str) for item in parsed):
        msg = f"Invalid section_lineage payload: {raw_value}"
        raise ValueError(msg)
    return parsed


def _find_duplicate_payload_sections(sections: list[SectionRecord]) -> dict[str, list[SectionRecord]]:
    grouped_sections: dict[str, list[SectionRecord]] = defaultdict(list)
    for section in sections:
        grouped_sections[section.section_id].append(section)
    return {section_id: matching_sections for section_id, matching_sections in grouped_sections.items() if len(matching_sections) > 1}


def _log_duplicate_payload_sections(duplicate_sections: dict[str, list[SectionRecord]]) -> None:
    duplicate_count = len(duplicate_sections)
    duplicate_row_count = sum(len(sections) for sections in duplicate_sections.values())
    details = [f"section_id={section_id}, occurrences=[{'; '.join(_format_section_record(section) for section in sections)}]" for section_id, sections in sorted(duplicate_sections.items())[:MAX_LOGGED_SECTION_CONFLICTS]]
    logger.error(f"Detected {duplicate_count} duplicate section_id value(s) in the incoming payload covering {duplicate_row_count} section row(s): {' | '.join(details)}")


def _log_existing_section_conflicts(
    sections: list[SectionRecord],
    conflicts: list[ExistingSectionConflict],
) -> None:
    incoming_sections_by_id = {section.section_id: section for section in sections}
    details = [
        (f"section_id={conflict.section_id}, incoming=({_format_section_record(incoming_sections_by_id[conflict.section_id])}), existing=(doc_uid={conflict.doc_uid!r}, title={conflict.title!r}, position={conflict.position})")
        for conflict in conflicts[:MAX_LOGGED_SECTION_CONFLICTS]
        if conflict.section_id in incoming_sections_by_id
    ]
    logger.error(f"Detected {len(conflicts)} existing section_id conflict(s) before insert: {' | '.join(details)}")


def _format_section_record(section: SectionRecord) -> str:
    return f"doc_uid={section.doc_uid!r}, title={section.title!r}, position={section.position}, parent_section_id={section.parent_section_id!r}"
