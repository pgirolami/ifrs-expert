"""Tests for section storage diagnostics."""

from __future__ import annotations

import logging
import sqlite3
import tempfile
from pathlib import Path

import pytest

from src.db.connection import init_db
from src.models.section import SectionRecord


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


def _section(section_id: str, doc_uid: str, title: str, position: int) -> SectionRecord:
    return SectionRecord(
        section_id=section_id,
        doc_uid=doc_uid,
        parent_section_id=None,
        level=1,
        title=title,
        section_lineage=[title],
        position=position,
    )


def test_section_store_logs_duplicate_payload_section_ids(temp_db: Path, caplog: pytest.LogCaptureFixture) -> None:
    """SectionStore should log duplicate business keys before the insert fails."""
    del temp_db
    from src.db.sections import SectionStore

    duplicate_sections = [
        _section(section_id="shared-section", doc_uid="navis-doc", title="First heading", position=1),
        _section(section_id="shared-section", doc_uid="navis-doc", title="Repeated heading", position=2),
    ]

    with SectionStore() as store, caplog.at_level(logging.ERROR):
        with pytest.raises(sqlite3.IntegrityError, match=r"UNIQUE constraint failed: sections.doc_uid, sections.section_id"):
            store.insert_sections(duplicate_sections)

    assert "Detected 1 duplicate (doc_uid, section_id) value(s) in the incoming payload" in caplog.text
    assert "shared-section" in caplog.text
    assert "navis-doc" in caplog.text
    assert "First heading" in caplog.text
    assert "Repeated heading" in caplog.text


def test_section_store_allows_same_source_section_id_in_different_documents(temp_db: Path) -> None:
    """Section ids should be reusable across different documents."""
    del temp_db
    from src.db.sections import SectionStore

    with SectionStore() as store:
        store.insert_sections(
            [
                _section(section_id="shared-section", doc_uid="existing-doc", title="Existing heading", position=10),
                _section(section_id="shared-section", doc_uid="new-doc", title="Incoming heading", position=20),
            ]
        )
        existing_section = store.get_section_by_source_id(doc_uid="existing-doc", section_id="shared-section")
        new_section = store.get_section_by_source_id(doc_uid="new-doc", section_id="shared-section")

    assert existing_section is not None
    assert new_section is not None
    assert existing_section.doc_uid == "existing-doc"
    assert new_section.doc_uid == "new-doc"
    assert existing_section.db_id != new_section.db_id


def test_section_store_logs_existing_doc_local_key_conflicts(temp_db: Path, caplog: pytest.LogCaptureFixture) -> None:
    """SectionStore should log existing doc-local conflicts before the insert fails."""
    del temp_db
    from src.db.sections import SectionStore

    existing_section = _section(section_id="shared-section", doc_uid="existing-doc", title="Existing heading", position=10)
    incoming_section = _section(section_id="shared-section", doc_uid="existing-doc", title="Incoming heading", position=20)

    with SectionStore() as store:
        store.insert_sections([existing_section])

    with SectionStore() as store, caplog.at_level(logging.ERROR):
        with pytest.raises(sqlite3.IntegrityError, match=r"UNIQUE constraint failed: sections.doc_uid, sections.section_id"):
            store.insert_sections([incoming_section])

    assert "Detected 1 existing (doc_uid, section_id) conflict(s) before insert" in caplog.text
    assert "shared-section" in caplog.text
    assert "existing-doc" in caplog.text
    assert "Existing heading" in caplog.text
    assert "Incoming heading" in caplog.text
