"""Tests for document, chunk, and section schema updates."""

from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path

import pytest

from src.db.connection import get_connection, init_db
from src.models.chunk import Chunk
from src.models.document import DocumentRecord, infer_document_type
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
        reference_columns = {row[1] for row in connection.execute("PRAGMA table_info(content_references)").fetchall()}

    assert {
        "doc_uid",
        "source_type",
        "source_title",
        "source_url",
        "canonical_url",
        "captured_at",
        "source_domain",
        "document_type",
        "background_text",
        "issue_text",
        "objective_text",
        "scope_text",
        "intro_text",
        "toc_text",
    }.issubset(document_columns)
    assert {"chunk_number", "chunk_id", "containing_section_id", "containing_section_db_id"}.issubset(chunk_columns)
    assert {
        "db_id",
        "section_id",
        "doc_uid",
        "source_parent_section_id",
        "parent_section_db_id",
        "title",
        "section_lineage",
        "position",
    }.issubset(section_columns)
    assert {"doc_uid", "ancestor_section_db_id", "descendant_section_db_id", "depth"}.issubset(closure_columns)
    assert {
        "source_doc_uid",
        "source_location_type",
        "source_chunk_id",
        "source_chunk_db_id",
        "source_section_id",
        "source_section_db_id",
        "reference_order",
        "annotation_raw_text",
        "target_raw_text",
        "target_kind",
        "target_doc_hint",
        "target_start",
        "target_end",
        "parsed_ok",
    }.issubset(reference_columns)


def test_infer_document_type_returns_supported_prefixes() -> None:
    """Document types should fall back to supported doc_uid prefixes when no DB row exists."""
    assert infer_document_type("ifrs9") == "IFRS-S"
    assert infer_document_type("ifrs9-bc") == "IFRS-BC"
    assert infer_document_type("ifrs9-ie") == "IFRS-IE"
    assert infer_document_type("ifrs9-ig") == "IFRS-IG"
    assert infer_document_type("ias21") == "IAS-S"
    assert infer_document_type("ifric16") == "IFRIC"
    assert infer_document_type("ifric12-ig") == "IFRIC-IG"
    assert infer_document_type("sic25") == "SIC"
    assert infer_document_type("ps1") == "PS"
    assert infer_document_type("navis-QRIFRS-C2A8E6F292F99E-EFL") == "NAVIS"
    assert infer_document_type("custom-doc") is None


def test_infer_document_type_prefers_persisted_document_type(temp_db: Path) -> None:
    """Document-type inference should prefer persisted metadata over doc_uid prefixes."""
    from src.db.documents import DocumentStore

    with DocumentStore() as store:
        store.upsert_document(
            DocumentRecord(
                doc_uid="custom-doc",
                source_type="html",
                source_title="Custom Navis document",
                source_url="https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&refId=C2A8E6F292F99E-EFL",
                canonical_url="https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&refId=C2A8E6F292F99E-EFL",
                captured_at="2026-04-04T14:23:10Z",
                source_domain="abonnes.efl.fr",
                document_type="NAVIS",
            )
        )

    assert infer_document_type("custom-doc") == "NAVIS"


def test_infer_document_type_prefers_persisted_ifrs_variant_document_type(temp_db: Path) -> None:
    """Persisted IFRS variant metadata should override the doc_uid fallback family."""
    from src.db.documents import DocumentStore

    with DocumentStore() as store:
        store.upsert_document(
            DocumentRecord(
                doc_uid="ifrs9",
                source_type="html",
                source_title="IFRS 9 Financial Instruments",
                source_url="https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/",
                canonical_url="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html",
                captured_at="2026-04-14T09:45:54Z",
                source_domain="www.ifrs.org",
                document_type="IFRS-S",
            )
        )

    assert infer_document_type("ifrs9") == "IFRS-S"


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
        source_domain="www.ifrs.org",
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
    assert fetched.source_domain == "www.ifrs.org"
    assert fetched.document_type == "IFRS-S"
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
    assert fetched[0].containing_section_db_id is None


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
            position=10,
        ),
        SectionRecord(
            section_id="IFRS09_g3.1.1-3.1.2",
            doc_uid="ifrs9",
            parent_section_id="IFRS09_0054",
            level=3,
            title="Initial recognition",
            section_lineage=["Recognition and derecognition", "Initial recognition"],
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
        store.insert_closure_rows(doc_uid="ifrs9", closure_rows=closure_rows)
        fetched_sections = store.get_sections_by_doc("ifrs9")
        root_section = store.get_section_by_source_id(doc_uid="ifrs9", section_id="IFRS09_0054")
        child_section = store.get_section_by_source_id(doc_uid="ifrs9", section_id="IFRS09_g3.1.1-3.1.2")

        assert root_section is not None
        assert child_section is not None
        descendant_db_ids = store.get_descendant_section_db_ids(root_section.db_id or -1)

    assert [section.section_id for section in fetched_sections] == ["IFRS09_0054", "IFRS09_g3.1.1-3.1.2"]
    assert fetched_sections[0].db_id is not None
    assert fetched_sections[1].db_id is not None
    assert fetched_sections[0].parent_section_id is None
    assert fetched_sections[0].parent_section_db_id is None
    assert fetched_sections[1].parent_section_id == "IFRS09_0054"
    assert fetched_sections[1].parent_section_db_id == fetched_sections[0].db_id
    assert descendant_db_ids == [root_section.db_id, child_section.db_id]


def test_chunk_store_syncs_section_db_ids(temp_db: Path) -> None:
    """Chunk rows should be able to resolve document-local section ids to synthetic db ids."""
    from src.db.chunks import ChunkStore
    from src.db.sections import SectionStore

    with SectionStore() as section_store:
        section_store.insert_sections(
            [
                SectionRecord(
                    section_id="IFRS09_scope",
                    doc_uid="ifrs9",
                    parent_section_id=None,
                    level=2,
                    title="Scope",
                    section_lineage=["Scope"],
                    position=1,
                )
            ]
        )
        section_db_id_by_source_id = section_store.map_source_ids_to_db_ids(
            doc_uid="ifrs9",
            section_ids=["IFRS09_scope"],
        )

    with ChunkStore() as chunk_store:
        row_id = chunk_store.insert_chunk(
            Chunk(
                doc_uid="ifrs9",
                chunk_number="1",
                page_start="",
                page_end="",
                chunk_id="IFRS09_1",
                containing_section_id="IFRS09_scope",
                text="Chunk text",
            )
        )
        updated_count = chunk_store.sync_containing_section_db_ids(
            doc_uid="ifrs9",
            section_db_id_by_source_id=section_db_id_by_source_id,
        )
        fetched = chunk_store.get_chunks_by_doc("ifrs9")

    assert row_id == 1
    assert updated_count == 1
    assert fetched[0].containing_section_db_id == section_db_id_by_source_id["IFRS09_scope"]


def test_get_connection_enables_foreign_keys(temp_db: Path) -> None:
    """Application connections should enable SQLite foreign key enforcement."""
    del temp_db

    with get_connection(read_only=True) as connection:
        foreign_keys_enabled = connection.execute("PRAGMA foreign_keys").fetchone()[0]

    assert foreign_keys_enabled == 1


def test_chunk_store_rejects_invalid_section_foreign_key(temp_db: Path) -> None:
    """Chunk inserts should fail when containing_section_db_id points to a missing section row."""
    from src.db.chunks import ChunkStore

    with ChunkStore() as chunk_store:
        with pytest.raises(sqlite3.IntegrityError):
            chunk_store.insert_chunk(
                Chunk(
                    doc_uid="ifrs9",
                    chunk_number="1",
                    page_start="",
                    page_end="",
                    chunk_id="IFRS09_1",
                    text="Chunk text",
                    containing_section_db_id=999,
                )
            )


def test_deleting_parent_section_cascades_children_closure_and_chunks(temp_db: Path) -> None:
    """Deleting a parent section should cascade through all dependent section references."""
    from src.db.chunks import ChunkStore
    from src.db.sections import SectionStore

    sections = [
        SectionRecord(
            section_id="IFRS09_root",
            doc_uid="ifrs9",
            parent_section_id=None,
            level=2,
            title="Root",
            section_lineage=["Root"],
            position=1,
        ),
        SectionRecord(
            section_id="IFRS09_child",
            doc_uid="ifrs9",
            parent_section_id="IFRS09_root",
            level=3,
            title="Child",
            section_lineage=["Root", "Child"],
            position=2,
        ),
    ]
    closure_rows = [
        SectionClosureRow("IFRS09_root", "IFRS09_root", 0),
        SectionClosureRow("IFRS09_root", "IFRS09_child", 1),
        SectionClosureRow("IFRS09_child", "IFRS09_child", 0),
    ]

    with SectionStore() as section_store:
        section_store.insert_sections(sections)
        section_store.insert_closure_rows(doc_uid="ifrs9", closure_rows=closure_rows)
        section_db_id_by_source_id = section_store.map_source_ids_to_db_ids(
            doc_uid="ifrs9",
            section_ids=["IFRS09_root", "IFRS09_child"],
        )
        root_section = section_store.get_section_by_source_id(doc_uid="ifrs9", section_id="IFRS09_root")

    with ChunkStore() as chunk_store:
        chunk_store.insert_chunk(
            Chunk(
                doc_uid="ifrs9",
                chunk_number="1.1",
                page_start="",
                page_end="",
                chunk_id="IFRS09_1_1",
                containing_section_id="IFRS09_child",
                text="Child chunk",
            )
        )
        chunk_store.sync_containing_section_db_ids(
            doc_uid="ifrs9",
            section_db_id_by_source_id=section_db_id_by_source_id,
        )

    assert root_section is not None
    assert root_section.db_id is not None

    with get_connection() as connection:
        connection.execute("DELETE FROM sections WHERE db_id = ?", (root_section.db_id,))
        connection.commit()
        remaining_section_count = connection.execute("SELECT COUNT(*) FROM sections").fetchone()[0]
        remaining_closure_count = connection.execute("SELECT COUNT(*) FROM section_closure").fetchone()[0]
        remaining_chunk_count = connection.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]

    assert remaining_section_count == 0
    assert remaining_closure_count == 0
    assert remaining_chunk_count == 0
