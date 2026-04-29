"""Tests for reference storage."""

from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path

import pytest

from src.db.connection import init_db
from src.models.reference import ContentReference


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


def test_init_db_creates_reference_tables(temp_db: Path) -> None:
    """The schema should include the content references table."""
    with sqlite3.connect(temp_db) as connection:
        reference_columns = {row[1] for row in connection.execute("PRAGMA table_info(content_references)").fetchall()}

    assert {
        "id",
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


def test_reference_store_round_trips_and_deletes_references(temp_db: Path) -> None:
    """References should round-trip through the database and delete by doc_uid."""
    from src.db.references import ContentReferenceStore

    references = [
        ContentReference(
            source_doc_uid="ifrs9",
            source_location_type="chunk",
            reference_order=1,
            annotation_raw_text="Refer: paragraphs 4.1.1(a)",
            target_raw_text="paragraph 4.1.1(a)",
            target_kind="same_standard_paragraph",
            target_start="4.1.1",
            parsed_ok=True,
            source_chunk_id="IFRS09_4.1.1__IFRS09_P0001",
            source_section_id="IFRS09_0054",
        ),
        ContentReference(
            source_doc_uid="ifrs9",
            source_location_type="section",
            reference_order=2,
            annotation_raw_text="Refer: paragraphs BC4.1-BC4.45",
            target_raw_text="paragraphs BC4.1-BC4.45",
            target_kind="basis_for_conclusions",
            target_start="BC4.1",
            target_end="BC4.45",
            parsed_ok=True,
            source_section_id="IFRS09_0054",
        ),
    ]

    with ContentReferenceStore() as store:
        inserted_ids = store.insert_references(references)
        fetched = store.get_references_by_doc("ifrs9")
        deleted = store.delete_references_by_doc("ifrs9")
        fetched_after_delete = store.get_references_by_doc("ifrs9")

    assert inserted_ids == [1, 2]
    assert [reference.id for reference in references] == [1, 2]
    assert len(fetched) == 2
    assert fetched[0].source_location_type == "chunk"
    assert fetched[0].source_chunk_id == "IFRS09_4.1.1__IFRS09_P0001"
    assert fetched[0].parsed_ok
    assert fetched[1].source_location_type == "section"
    assert fetched[1].target_kind == "basis_for_conclusions"
    assert deleted == 2
    assert fetched_after_delete == []
