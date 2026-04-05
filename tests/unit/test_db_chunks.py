"""Tests for database chunks."""

import tempfile
from pathlib import Path

import pytest

from src.db.connection import init_db
from src.models.chunk import Chunk


class TestDbChunk:
    """Tests for the database Chunk class."""

    def test_create_db_chunk(self) -> None:
        """Test creating a database chunk."""
        chunk = Chunk(
            id=1,
            doc_uid="test-doc",
            chunk_number="B43",
            page_start="A856",
            page_end="A856",
            chunk_id="IFRS16_B43",
            text="Test text",
        )
        assert chunk.id == 1
        assert chunk.doc_uid == "test-doc"
        assert chunk.chunk_number == "B43"
        assert chunk.page_start == "A856"
        assert chunk.page_end == "A856"
        assert chunk.chunk_id == "IFRS16_B43"
        assert chunk.text == "Test text"


class TestChunkStore:
    """Tests for ChunkStore with temporary database."""

    @pytest.fixture
    def temp_db(self) -> Path:
        """Create a temporary database."""
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test.db"

            import src.db.connection as conn_module

            original_path = conn_module.DB_PATH
            conn_module.DB_PATH = db_path
            init_db()
            yield db_path
            conn_module.DB_PATH = original_path

    def test_insert_and_retrieve_chunks(self, temp_db: Path) -> None:
        """Test inserting and retrieving chunks."""
        from src.db.chunks import ChunkStore

        chunk = Chunk(
            doc_uid="test-doc",
            chunk_number="B43",
            page_start="A856",
            page_end="A856",
            chunk_id="IFRS16_B43",
            text="Test content",
        )

        with ChunkStore() as store:
            row_id = store.insert_chunk(chunk)
            assert row_id == 1

            retrieved = store.get_chunks_by_doc("test-doc")
            assert len(retrieved) == 1
            assert retrieved[0].chunk_number == "B43"
            assert retrieved[0].chunk_id == "IFRS16_B43"
            assert retrieved[0].text == "Test content"

    def test_get_chunks_by_doc_empty(self, temp_db: Path) -> None:
        """Test retrieving chunks for non-existent document."""
        from src.db.chunks import ChunkStore

        with ChunkStore() as store:
            retrieved = store.get_chunks_by_doc("nonexistent")
            assert len(retrieved) == 0

    def test_delete_chunks_by_doc(self, temp_db: Path) -> None:
        """Test deleting chunks by doc_uid."""
        from src.db.chunks import ChunkStore

        chunk = Chunk(
            doc_uid="test-doc",
            chunk_number="B43",
            page_start="A856",
            page_end="A856",
            chunk_id="IFRS16_B43",
            text="Test content",
        )

        with ChunkStore() as store:
            store.insert_chunk(chunk)
            deleted = store.delete_chunks_by_doc("test-doc")
            assert deleted == 1

            retrieved = store.get_chunks_by_doc("test-doc")
            assert len(retrieved) == 0

    def test_get_all_docs(self, temp_db: Path) -> None:
        """Test getting all document UIDs."""
        from src.db.chunks import ChunkStore

        chunks = [
            Chunk(doc_uid="doc1", chunk_number="1", page_start="1", page_end="1", chunk_id="DOC1_1", text="a"),
            Chunk(doc_uid="doc2", chunk_number="2", page_start="1", page_end="1", chunk_id="DOC2_2", text="b"),
        ]

        with ChunkStore() as store:
            store.insert_chunks(chunks)
            docs = store.get_all_docs()
            assert set(docs) == {"doc1", "doc2"}
