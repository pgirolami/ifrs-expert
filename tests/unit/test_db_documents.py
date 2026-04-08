"""Tests for document, chunk, and section schema updates."""

from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path

import pytest

from src.db.connection import init_db
from src.models.chunk import Chunk
from src.models.document import DocumentRecord
from src.models.section import SectionClosureRow, SectionRecord


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


def test_init_db_creates_documents_sections_and_chunk_metadata_columns(temp_db: Path) -> None:
    """The schema should support document metadata, section trees, and chunk references."""
    with sqlite3.connect(temp_db) as connection:
        document_columns = {row[1] for row in connection.execute("PRAGMA table_info(documents)").fetchall()}
        chunk_columns = {row[1] for row in connection.execute("PRAGMA table_info(chunks)").fetchall()}
        section_columns = {row[1] for row in connection.execute("PRAGMA table_info(sections)").fetchall()}
        closure_columns = {row[1] for row in connection.execute("PRAGMA table_info(section_closure)").fetchall()}

    assert {
        "doc_uid",
        "source_type",
        "source_title",
        "source_url",
        "canonical_url",
        "captured_at",
        "background_text",
        "issue_text",
        "objective_text",
        "scope_text",
        "intro_text",
        "toc_text",
    }.issubset(document_columns)
    assert {"chunk_number", "chunk_id", "containing_section_id"}.issubset(chunk_columns)
    assert {"section_id", "doc_uid", "parent_section_id", "title", "section_lineage", "embedding_text", "position"}.issubset(section_columns)
    assert {"ancestor_section_id", "descendant_section_id", "depth"}.issubset(closure_columns)


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
        background_text="Background text",
        issue_text="Issue text",
        objective_text="Objective text",
        scope_text="Scope text",
        intro_text="Intro text",
        toc_text="TOC text",
    )

    with DocumentStore() as store:
        store.upsert_document(record)
        fetched = store.get_document("ifrs9")

    assert fetched is not None, "Expected stored document metadata to be retrievable"
    assert fetched.doc_uid == "ifrs9"
    assert fetched.source_type == "html"
    assert fetched.canonical_url == "https://www.ifrs.org/ifrs9.html"
    assert fetched.background_text == "Background text"
    assert fetched.issue_text == "Issue text"
    assert fetched.objective_text == "Objective text"
    assert fetched.scope_text == "Scope text"
    assert fetched.intro_text == "Intro text"
    assert fetched.toc_text == "TOC text"


def test_chunk_store_round_trips_chunk_metadata(temp_db: Path) -> None:
    """Chunk rows should preserve chunk ids, numbers, and containing sections."""
    from src.db.chunks import ChunkStore

    chunk = Chunk(
        doc_uid="ifrs9",
        chunk_number="3.1.1",
        page_start="",
        page_end="",
        chunk_id="IFRS09_3.1.1",
        containing_section_id="IFRS09_g3.1.1-3.1.2",
        text="Chunk text",
    )

    with ChunkStore() as store:
        row_id = store.insert_chunk(chunk)
        fetched = store.get_chunks_by_doc("ifrs9")

    assert row_id == 1
    assert fetched[0].chunk_id == "IFRS09_3.1.1"
    assert fetched[0].chunk_number == "3.1.1"
    assert fetched[0].containing_section_id == "IFRS09_g3.1.1-3.1.2"


def test_section_store_round_trips_sections_and_closure(temp_db: Path) -> None:
    """Section rows and closure rows should round-trip through the database."""
    from src.db.sections import SectionStore

    sections = [
        SectionRecord(
            section_id="IFRS09_0054",
            doc_uid="ifrs9",
            parent_section_id=None,
            level=2,
            title="Recognition and derecognition",
            section_lineage=["Recognition and derecognition"],
            embedding_text="Recognition and derecognition",
            position=10,
        ),
        SectionRecord(
            section_id="IFRS09_g3.1.1-3.1.2",
            doc_uid="ifrs9",
            parent_section_id="IFRS09_0054",
            level=3,
            title="Initial recognition",
            section_lineage=["Recognition and derecognition", "Initial recognition"],
            embedding_text="Initial recognition",
            position=11,
        ),
    ]
    closure_rows = [
        SectionClosureRow(ancestor_section_id="IFRS09_0054", descendant_section_id="IFRS09_0054", depth=0),
        SectionClosureRow(ancestor_section_id="IFRS09_0054", descendant_section_id="IFRS09_g3.1.1-3.1.2", depth=1),
        SectionClosureRow(
            ancestor_section_id="IFRS09_g3.1.1-3.1.2",
            descendant_section_id="IFRS09_g3.1.1-3.1.2",
            depth=0,
        ),
    ]

    with SectionStore() as store:
        store.insert_sections(sections)
        store.insert_closure_rows(closure_rows)
        fetched_sections = store.get_sections_by_doc("ifrs9")
        descendant_ids = store.get_descendant_section_ids("IFRS09_0054")

    assert [section.section_id for section in fetched_sections] == ["IFRS09_0054", "IFRS09_g3.1.1-3.1.2"]
    assert descendant_ids == ["IFRS09_0054", "IFRS09_g3.1.1-3.1.2"]
