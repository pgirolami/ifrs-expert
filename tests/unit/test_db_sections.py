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
        embedding_text=title,
        position=position,
    )


def test_section_store_logs_duplicate_payload_section_ids(temp_db: Path, caplog: pytest.LogCaptureFixture) -> None:
    """SectionStore should log the duplicate payload rows before the insert fails."""
    del temp_db
    from src.db.sections import SectionStore

    duplicate_sections = [
        _section(section_id="shared-section", doc_uid="navis-doc", title="First heading", position=1),
        _section(section_id="shared-section", doc_uid="navis-doc", title="Repeated heading", position=2),
    ]

    with SectionStore() as store, caplog.at_level(logging.ERROR):
        with pytest.raises(sqlite3.IntegrityError, match="UNIQUE constraint failed: sections.section_id"):
            store.insert_sections(duplicate_sections)

    assert "Detected 1 duplicate section_id value(s) in the incoming payload" in caplog.text
    assert "shared-section" in caplog.text
    assert "First heading" in caplog.text
    assert "Repeated heading" in caplog.text



def test_section_store_logs_existing_section_id_conflicts(temp_db: Path, caplog: pytest.LogCaptureFixture) -> None:
    """SectionStore should log the existing conflicting rows before the insert fails."""
    del temp_db
    from src.db.sections import SectionStore

    existing_section = _section(section_id="shared-section", doc_uid="existing-doc", title="Existing heading", position=10)
    incoming_section = _section(section_id="shared-section", doc_uid="new-doc", title="Incoming heading", position=20)

    with SectionStore() as store:
        store.insert_sections([existing_section])

    with SectionStore() as store, caplog.at_level(logging.ERROR):
        with pytest.raises(sqlite3.IntegrityError, match="UNIQUE constraint failed: sections.section_id"):
            store.insert_sections([incoming_section])

    assert "Detected 1 existing section_id conflict(s) before insert" in caplog.text
    assert "shared-section" in caplog.text
    assert "existing-doc" in caplog.text
    assert "Existing heading" in caplog.text
    assert "new-doc" in caplog.text
    assert "Incoming heading" in caplog.text
