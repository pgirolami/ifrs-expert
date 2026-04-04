"""Chunk storage and retrieval for IFRS Expert."""

from __future__ import annotations

import logging
import sqlite3
from typing import Self

from src.db.connection import get_connection
from src.models.chunk import Chunk

logger = logging.getLogger(__name__)


class ChunkStore:
    """Manages chunk storage and retrieval in the database."""

    _conn: sqlite3.Connection

    def __enter__(self) -> Self:
        """Context manager entry."""
        self._conn = get_connection()
        self._conn.row_factory = sqlite3.Row
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Context manager exit."""
        self._conn.close()

    def insert_chunk(self, chunk: Chunk) -> int:
        """Insert a chunk into the database and return its database ID."""
        cursor = self._conn.execute(
            """
            INSERT INTO chunks (doc_uid, section_path, page_start, page_end, source_anchor, text)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                chunk.doc_uid,
                chunk.section_path,
                chunk.page_start,
                chunk.page_end,
                chunk.source_anchor,
                chunk.text,
            ),
        )
        self._conn.commit()
        chunk_id = cursor.lastrowid
        if chunk_id is None:
            msg = "SQLite did not return a lastrowid for inserted chunk"
            raise sqlite3.OperationalError(msg)
        return chunk_id

    def insert_chunks(self, chunks: list[Chunk]) -> list[int]:
        """Insert multiple chunks and update their chunk_id values."""
        ids: list[int] = []
        for chunk in chunks:
            chunk_id = self.insert_chunk(chunk)
            chunk.chunk_id = chunk_id
            ids.append(chunk_id)
        logger.info(f"Inserted {len(ids)} chunks into database")
        return ids

    def get_chunks_by_doc(self, doc_uid: str) -> list[Chunk]:
        """Get all chunks for a document."""
        rows = self._conn.execute(
            """
            SELECT id, doc_uid, section_path, page_start, page_end, source_anchor, text
            FROM chunks
            WHERE doc_uid = ?
            ORDER BY id
            """,
            (doc_uid,),
        ).fetchall()

        return [
            Chunk(
                chunk_id=row["id"],
                doc_uid=row["doc_uid"],
                section_path=row["section_path"],
                page_start=row["page_start"],
                page_end=row["page_end"],
                source_anchor=row["source_anchor"],
                text=row["text"],
            )
            for row in rows
        ]

    def get_all_docs(self) -> list[str]:
        """Get all document UIDs present in chunks."""
        rows = self._conn.execute("SELECT DISTINCT doc_uid FROM chunks ORDER BY doc_uid").fetchall()
        return [row["doc_uid"] for row in rows]

    def delete_chunks_by_doc(self, doc_uid: str) -> int:
        """Delete all chunks for a document and return the deleted count."""
        cursor = self._conn.execute("DELETE FROM chunks WHERE doc_uid = ?", (doc_uid,))
        self._conn.commit()
        deleted = cursor.rowcount
        logger.info(f"Deleted {deleted} chunks for document {doc_uid}")
        return deleted
