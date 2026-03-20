"""Chunk storage and retrieval for IFRS Expert."""

import logging
import sqlite3
from pathlib import Path
from typing import Self

from src.db.connection import get_connection
from src.models.chunk import Chunk as PdfChunk
from src.pdf import extract_chunks

logger = logging.getLogger(__name__)


class Chunk:
    """Represents a document chunk in the database."""

    chunk_id: int | None
    doc_uid: str
    section_path: str
    page_start: str
    page_end: str
    text: str

    def __init__(
        self,
        chunk_id: int | None = None,
        *,
        doc_uid: str = "",
        section_path: str = "",
        page_start: str = "",
        page_end: str = "",
        text: str = "",
    ) -> None:
        self.chunk_id = chunk_id
        self.doc_uid = doc_uid
        self.section_path = section_path
        self.page_start = page_start
        self.page_end = page_end
        self.text = text

    @classmethod
    def from_pdf_chunk(cls, pdf_chunk: PdfChunk, doc_uid: str) -> Self:
        """Create a database Chunk from a PDF Chunk."""
        return cls(
            doc_uid=doc_uid,
            section_path=pdf_chunk.section_path,
            page_start=pdf_chunk.page_start,
            page_end=pdf_chunk.page_end,
            text=pdf_chunk.text,
        )


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
        """Insert a chunk into the database.

        Args:
            chunk: Chunk to insert.

        Returns:
            ID of the inserted chunk.
        """
        cursor = self._conn.execute(
            """INSERT INTO chunks (doc_uid, section_path, page_start, page_end, text)
               VALUES (?, ?, ?, ?, ?)""",
            (chunk.doc_uid, chunk.section_path, chunk.page_start, chunk.page_end, chunk.text),
        )
        self._conn.commit()
        return cursor.lastrowid  # type: ignore[return-value]

    def insert_chunks(self, chunks: list[Chunk]) -> list[int]:
        """Insert multiple chunks into the database.

        Args:
            chunks: List of chunks to insert.

        Returns:
            List of inserted chunk IDs. Also updates chunk objects with their IDs.
        """
        ids: list[int] = []
        for chunk in chunks:
            chunk_id = self.insert_chunk(chunk)
            chunk.chunk_id = chunk_id
            ids.append(chunk_id)
        logger.info(f"Inserted {len(ids)} chunks into database")
        return ids

    def get_chunks_by_doc(self, doc_uid: str) -> list[Chunk]:
        """Get all chunks for a document.

        Args:
            doc_uid: Document UID to filter by.

        Returns:
            List of chunks for the document.
        """
        rows = self._conn.execute(
            "SELECT id, doc_uid, section_path, page_start, page_end, text "
            "FROM chunks WHERE doc_uid = ? ORDER BY id",
            (doc_uid,),
        ).fetchall()

        return [
            Chunk(
                chunk_id=row["id"],
                doc_uid=row["doc_uid"],
                section_path=row["section_path"],
                page_start=row["page_start"],
                page_end=row["page_end"],
                text=row["text"],
            )
            for row in rows
        ]

    def get_all_docs(self) -> list[str]:
        """Get all document UIDs.

        Returns:
            List of document UIDs.
        """
        rows = self._conn.execute("SELECT DISTINCT doc_uid FROM chunks ORDER BY doc_uid").fetchall()
        return [row["doc_uid"] for row in rows]

    def delete_chunks_by_doc(self, doc_uid: str) -> int:
        """Delete all chunks for a document.

        Args:
            doc_uid: Document UID to delete chunks for.

        Returns:
            Number of deleted chunks.
        """
        cursor = self._conn.execute("DELETE FROM chunks WHERE doc_uid = ?", (doc_uid,))
        self._conn.commit()
        deleted = cursor.rowcount
        logger.info(f"Deleted {deleted} chunks for document {doc_uid}")
        return deleted


def insert_chunks_from_file(pdf_path: Path, doc_uid: str) -> list[int]:
    """Extract chunks from a PDF and insert into database.

    Args:
        pdf_path: Path to the PDF file.
        doc_uid: Document UID to use.

    Returns:
        List of inserted chunk IDs.
    """
    logger.info(f"Extracting chunks from {pdf_path}")
    raw_chunks = extract_chunks(pdf_path)

    chunks = [Chunk.from_pdf_chunk(c, doc_uid) for c in raw_chunks]

    with ChunkStore() as store:
        return store.insert_chunks(chunks)
