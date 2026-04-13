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
    """One existing database row that conflicts with an incoming business key."""

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
        """Insert multiple sections and resolve their synthetic parent links."""
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
                    doc_uid,
                    section_id,
                    source_parent_section_id,
                    parent_section_db_id,
                    level,
                    title,
                    section_lineage,
                    position
                ) VALUES (?, ?, ?, NULL, ?, ?, ?, ?)
                """,
                [
                    (
                        section.doc_uid,
                        section.section_id,
                        section.parent_section_id,
                        section.level,
                        section.title,
                        json.dumps(section.section_lineage, ensure_ascii=False),
                        section.position,
                    )
                    for section in sections
                ],
            )
        except sqlite3.IntegrityError:
            logger.exception(f"Failed to insert {len(sections)} sections due to a (doc_uid, section_id) integrity error")
            raise

        self._populate_parent_section_db_ids(doc_uids=sorted({section.doc_uid for section in sections}))
        self._conn.commit()
        logger.info(f"Inserted {len(sections)} sections into database")

    def insert_closure_rows(self, doc_uid: str, closure_rows: list[SectionClosureRow]) -> None:
        """Insert ancestor/descendant closure rows using synthetic section ids."""
        if not closure_rows:
            return

        section_ids = sorted({row.ancestor_section_id for row in closure_rows} | {row.descendant_section_id for row in closure_rows})
        section_db_id_by_source_id = self.map_source_ids_to_db_ids(doc_uid=doc_uid, section_ids=section_ids)

        translated_rows: list[tuple[str, int, int, int]] = []
        for row in closure_rows:
            ancestor_section_db_id = section_db_id_by_source_id.get(row.ancestor_section_id)
            descendant_section_db_id = section_db_id_by_source_id.get(row.descendant_section_id)
            if ancestor_section_db_id is None or descendant_section_db_id is None:
                msg = f"Could not resolve closure row for doc_uid={doc_uid}: ancestor_section_id={row.ancestor_section_id!r}, descendant_section_id={row.descendant_section_id!r}"
                raise ValueError(msg)
            translated_rows.append((doc_uid, ancestor_section_db_id, descendant_section_db_id, row.depth))

        self._conn.executemany(
            """
            INSERT INTO section_closure (
                doc_uid,
                ancestor_section_db_id,
                descendant_section_db_id,
                depth
            ) VALUES (?, ?, ?, ?)
            """,
            translated_rows,
        )
        self._conn.commit()
        logger.info(f"Inserted {len(closure_rows)} section closure rows into database for doc_uid={doc_uid}")

    def get_sections_by_doc(self, doc_uid: str) -> list[SectionRecord]:
        """Get all sections for a document in document order."""
        rows = self._conn.execute(
            """
            SELECT
                db_id,
                section_id,
                doc_uid,
                source_parent_section_id,
                parent_section_db_id,
                level,
                title,
                section_lineage,
                position
            FROM sections
            WHERE doc_uid = ?
            ORDER BY position, section_id
            """,
            (doc_uid,),
        ).fetchall()
        return [_row_to_section_record(row) for row in rows]

    def get_section_by_source_id(self, doc_uid: str, section_id: str) -> SectionRecord | None:
        """Resolve one document-local source section id to its stored row."""
        row = self._conn.execute(
            """
            SELECT
                db_id,
                section_id,
                doc_uid,
                source_parent_section_id,
                parent_section_db_id,
                level,
                title,
                section_lineage,
                position
            FROM sections
            WHERE doc_uid = ? AND section_id = ?
            """,
            (doc_uid, section_id),
        ).fetchone()
        if row is None:
            return None
        return _row_to_section_record(row)

    def get_descendant_section_db_ids(self, section_db_id: int) -> list[int]:
        """Return all descendant synthetic section ids including the matched section itself."""
        rows = self._conn.execute(
            """
            SELECT descendant_section_db_id
            FROM section_closure
            WHERE ancestor_section_db_id = ?
            ORDER BY depth, descendant_section_db_id
            """,
            (section_db_id,),
        ).fetchall()
        return [row["descendant_section_db_id"] for row in rows]

    def map_source_ids_to_db_ids(self, doc_uid: str, section_ids: list[str]) -> dict[str, int]:
        """Resolve one document's source section ids to synthetic db ids."""
        unique_section_ids = sorted(set(section_ids))
        if not unique_section_ids:
            return {}

        requested_section_ids = set(unique_section_ids)
        rows = self._conn.execute(
            """
            SELECT section_id, db_id
            FROM sections
            WHERE doc_uid = ?
            ORDER BY section_id
            """,
            (doc_uid,),
        ).fetchall()
        return {row["section_id"]: row["db_id"] for row in rows if row["section_id"] in requested_section_ids}

    def delete_sections_by_doc(self, doc_uid: str) -> int:
        """Delete sections for one document and rely on cascading foreign keys."""
        cursor = self._conn.execute("DELETE FROM sections WHERE doc_uid = ?", (doc_uid,))
        self._conn.commit()
        deleted = cursor.rowcount
        logger.info(f"Deleted {deleted} sections for document {doc_uid}")
        return deleted

    def _find_existing_section_conflicts(self, sections: list[SectionRecord]) -> list[ExistingSectionConflict]:
        """Find existing section rows whose business keys conflict with the incoming payload."""
        conflicts: list[ExistingSectionConflict] = []
        unique_keys = sorted({(section.doc_uid, section.section_id) for section in sections})
        if not unique_keys:
            return conflicts

        for doc_uid, section_id in unique_keys:
            rows = self._conn.execute(
                """
                SELECT doc_uid, section_id, title, position
                FROM sections
                WHERE doc_uid = ? AND section_id = ?
                ORDER BY position
                """,
                (doc_uid, section_id),
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

    def _populate_parent_section_db_ids(self, doc_uids: list[str]) -> None:
        """Backfill synthetic parent links after inserts."""
        updates: list[tuple[int, int]] = []
        for doc_uid in doc_uids:
            sections = self.get_sections_by_doc(doc_uid)
            section_db_id_by_source_id = {section.section_id: section.db_id for section in sections if section.db_id is not None}
            for section in sections:
                if section.db_id is None or section.parent_section_id is None:
                    continue
                parent_section_db_id = section_db_id_by_source_id.get(section.parent_section_id)
                if parent_section_db_id is None:
                    continue
                updates.append((parent_section_db_id, section.db_id))

        if updates:
            self._conn.executemany(
                "UPDATE sections SET parent_section_db_id = ? WHERE db_id = ?",
                updates,
            )


def _row_to_section_record(row: sqlite3.Row) -> SectionRecord:
    return SectionRecord(
        section_id=row["section_id"],
        doc_uid=row["doc_uid"],
        parent_section_id=row["source_parent_section_id"],
        level=row["level"],
        title=row["title"],
        section_lineage=_decode_lineage(row["section_lineage"]),
        position=row["position"],
        db_id=row["db_id"],
        parent_section_db_id=row["parent_section_db_id"],
    )


def _decode_lineage(raw_value: str) -> list[str]:
    parsed = json.loads(raw_value)
    if not isinstance(parsed, list) or not all(isinstance(item, str) for item in parsed):
        msg = f"Invalid section_lineage payload: {raw_value}"
        raise ValueError(msg)
    return parsed


def _find_duplicate_payload_sections(sections: list[SectionRecord]) -> dict[tuple[str, str], list[SectionRecord]]:
    grouped_sections: dict[tuple[str, str], list[SectionRecord]] = defaultdict(list)
    for section in sections:
        grouped_sections[(section.doc_uid, section.section_id)].append(section)
    return {key: matching_sections for key, matching_sections in grouped_sections.items() if len(matching_sections) > 1}


def _log_duplicate_payload_sections(duplicate_sections: dict[tuple[str, str], list[SectionRecord]]) -> None:
    duplicate_count = len(duplicate_sections)
    duplicate_row_count = sum(len(sections) for sections in duplicate_sections.values())
    details = [
        (f"doc_uid={doc_uid}, section_id={section_id}, occurrences=[{'; '.join(_format_section_record(section) for section in sections)}]")
        for (doc_uid, section_id), sections in sorted(duplicate_sections.items())[:MAX_LOGGED_SECTION_CONFLICTS]
    ]
    logger.error(f"Detected {duplicate_count} duplicate (doc_uid, section_id) value(s) in the incoming payload covering {duplicate_row_count} section row(s): {' | '.join(details)}")


def _log_existing_section_conflicts(
    sections: list[SectionRecord],
    conflicts: list[ExistingSectionConflict],
) -> None:
    incoming_sections_by_key = {(section.doc_uid, section.section_id): section for section in sections}
    details = [
        (
            f"doc_uid={conflict.doc_uid}, section_id={conflict.section_id}, "
            f"incoming=({_format_section_record(incoming_sections_by_key[(conflict.doc_uid, conflict.section_id)])}), "
            f"existing=(title={conflict.title!r}, position={conflict.position})"
        )
        for conflict in conflicts[:MAX_LOGGED_SECTION_CONFLICTS]
        if (conflict.doc_uid, conflict.section_id) in incoming_sections_by_key
    ]
    logger.error(f"Detected {len(conflicts)} existing (doc_uid, section_id) conflict(s) before insert: {' | '.join(details)}")


def _format_section_record(section: SectionRecord) -> str:
    return f"doc_uid={section.doc_uid!r}, section_id={section.section_id!r}, title={section.title!r}, position={section.position}, parent_section_id={section.parent_section_id!r}"
