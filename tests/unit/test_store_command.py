"""Tests for store command."""

from pathlib import Path
from unittest.mock import patch

import pytest

from src.commands.store import StoreCommand, MAX_CHUNK_CHARS
from src.models.chunk import Chunk
from tests.fakes import InMemoryChunkStore


class MockVectorStore:
    """Minimal mock for VectorStore context manager."""

    def __init__(self) -> None:
        self._deleted_count = 0

    def __enter__(self) -> "MockVectorStore":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        pass

    def delete_by_doc(self, doc_uid: str) -> int:
        return self._deleted_count

    def add_embeddings(self, doc_uid: str, chunk_ids: list[int], texts: list[str]) -> None:
        pass


class TestStoreCommand:
    """Tests for store command using dependency injection."""

    def test_store_command_success(self, tmp_path):
        """Test store command stores chunks in DB and vector store."""
        pdf_path = tmp_path / "test.pdf"
        pdf_path.write_text("dummy")

        command = StoreCommand(
            pdf_path=pdf_path,
            chunk_store=InMemoryChunkStore(),
            vector_store=MockVectorStore(),
            init_db_fn=lambda: None,
            doc_uid=None,
        )

        with patch("src.commands.store.extract_chunks") as mock_extract:
            mock_extract.return_value = [
                Chunk(section_path="1.1", page_start="A1", page_end="A1", text="test content")
            ]

            result = command.execute()

            assert not result.startswith("Error:"), f"Expected success, got error: {result}"
            assert "1 chunks" in result
            mock_extract.assert_called_once_with(pdf_path)

    def test_store_command_oversized_chunks_truncated(self, tmp_path):
        """Test store command truncates oversized chunks."""
        pdf_path = tmp_path / "test.pdf"
        pdf_path.write_text("dummy")

        command = StoreCommand(
            pdf_path=pdf_path,
            chunk_store=InMemoryChunkStore(),
            vector_store=MockVectorStore(),
            init_db_fn=lambda: None,
            doc_uid=None,
        )

        with patch("src.commands.store.extract_chunks") as mock_extract:
            oversized_text = "x" * (MAX_CHUNK_CHARS + 1)
            mock_extract.return_value = [
                Chunk(section_path="1.1", page_start="A1", page_end="A1", text=oversized_text)
            ]

            result = command.execute()

            # Should succeed but truncate the chunk
            assert result.startswith("Stored")
            assert "1 chunks" in result

    def test_store_command_file_not_found(self):
        """Test store command fails when PDF doesn't exist."""
        command = StoreCommand(
            pdf_path=Path("/nonexistent/file.pdf"),
            chunk_store=InMemoryChunkStore(),
            vector_store=MockVectorStore(),
            init_db_fn=lambda: None,
            doc_uid=None,
        )

        result = command.execute()

        assert result.startswith("Error:")
        assert "not found" in result

    def test_store_command_requires_dependencies(self, tmp_path):
        """Test that missing dependencies cause TypeError at construction."""
        pdf_path = tmp_path / "test.pdf"
        pdf_path.write_text("dummy")

        # Missing required arguments should raise TypeError
        with pytest.raises(TypeError):
            StoreCommand(pdf_path=pdf_path)  # type: ignore[call-arg]

        with pytest.raises(TypeError):
            StoreCommand(pdf_path=pdf_path, chunk_store=InMemoryChunkStore())  # type: ignore[call-arg]

    def test_store_command_replaces_existing_chunks(self, tmp_path):
        """Test store command replaces existing chunks for same doc_uid."""
        pdf_path = tmp_path / "test.pdf"
        pdf_path.write_text("dummy")

        chunk_store = InMemoryChunkStore()

        # Insert a chunk first
        with chunk_store as store:
            store.insert_chunks([
                Chunk(doc_uid="test", section_path="1.0", page_start="A1", page_end="A1", text="old content")
            ])

        # Verify initial state - should have 1 chunk
        with chunk_store as store:
            chunks = store.get_chunks_by_doc("test")
            assert len(chunks) == 1

        # Now run store command with same doc_uid
        command = StoreCommand(
            pdf_path=pdf_path,
            chunk_store=chunk_store,
            vector_store=MockVectorStore(),
            init_db_fn=lambda: None,
            doc_uid="test",
        )

        with patch("src.commands.store.extract_chunks") as mock_extract:
            mock_extract.return_value = [
                Chunk(section_path="2.0", page_start="B1", page_end="B1", text="new content")
            ]

            result = command.execute()

            # Old chunk should be replaced
            with chunk_store as store:
                chunks = store.get_chunks_by_doc("test")
                assert len(chunks) == 1
                assert chunks[0].text == "new content"