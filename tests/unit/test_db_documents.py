"""Tests for document storage and chunk schema updates."""

from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path

import pytest

from src.db.connection import init_db
from src.models.chunk import Chunk
from src.models.document import DocumentRecord


@pytest.fixture
def temp_db() -> Path:
    """Create a temporary database path and patch the global DB location."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        import src.db.connection as conn_module

        original_path = conn_module.DB_PATH
        conn_module.DB_PATH = db_path
        init_db()
        yield db_path
        conn_module.DB_PATH = original_path


def test_init_db_creates_documents_table_and_source_anchor_column(temp_db: Path) -> None:
    """The new schema should support document metadata and HTML anchors."""
    with sqlite3.connect(temp_db) as connection:
        document_columns = {
            row[1]
            for row in connection.execute("PRAGMA table_info(documents)").fetchall()
        }
        chunk_columns = {
            row[1]
            for row in connection.execute("PRAGMA table_info(chunks)").fetchall()
        }

    assert {"doc_uid", "source_type", "source_title", "source_url", "canonical_url", "captured_at"}.issubset(document_columns)
    assert "source_anchor" in chunk_columns


def test_document_store_upserts_and_reads_document_records(temp_db: Path) -> None:
    """Document metadata should round-trip through the database."""
    from src.db.documents import DocumentStore

    record = DocumentRecord(
        doc_uid="ifrs9",
        source_type="html",
        source_title="IFRS 9",
        source_url="https://www.ifrs.org/ifrs9.html",
        canonical_url="https://www.ifrs.org/ifrs9.html",
        captured_at="2026-04-04T14:23:10Z",
    )

    with DocumentStore() as store:
        store.upsert_document(record)
        fetched = store.get_document("ifrs9")

    assert fetched is not None, "Expected stored document metadata to be retrievable"
    assert fetched.doc_uid == "ifrs9"
    assert fetched.source_type == "html"
    assert fetched.canonical_url == "https://www.ifrs.org/ifrs9.html"


def test_chunk_store_round_trips_source_anchor(temp_db: Path) -> None:
    """Chunk rows should preserve the HTML source anchor."""
    from src.db.chunks import ChunkStore

    chunk = Chunk(
        doc_uid="ifrs9",
        section_path="3.1.1",
        page_start="",
        page_end="",
        source_anchor="IFRS09_3.1.1",
        text="Chunk text",
    )

    with ChunkStore() as store:
        store.insert_chunks([chunk])
        fetched = store.get_chunks_by_doc("ifrs9")

    assert fetched[0].source_anchor == "IFRS09_3.1.1"
