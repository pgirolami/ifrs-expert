"""Tests for store command."""

from unittest.mock import MagicMock, patch

from src.commands import StoreCommand
from src.commands.store import MAX_CHUNK_CHARS
from src.models.chunk import Chunk


class TestStoreCommand:
    """Tests for store command."""

    def test_store_command_success(self, tmp_path):
        """Test store command stores chunks in DB and vector store."""
        pdf_path = tmp_path / "test.pdf"
        pdf_path.touch()

        with patch("src.commands.store.init_db"), patch(
            "src.commands.store.extract_chunks"
        ) as mock_extract, patch("src.commands.store.ChunkStore") as mock_cs_class, patch(
            "src.commands.store.VectorStore"
        ) as mock_vs_class:

            # Mock extract_chunks
            mock_extract.return_value = [
                Chunk(section_path="1.1", page_start="A1", page_end="A1", text="test content")
            ]

            # Mock ChunkStore
            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = []
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            # Mock VectorStore
            mock_vs = MagicMock()
            mock_vs.delete_by_doc.return_value = 0
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = StoreCommand(pdf_path=pdf_path, doc_uid=None)
            result = command.execute()

            assert not result.startswith("Error:"), f"Expected success, got error: {result}"
            assert "1 chunks" in result

    def test_store_command_oversized_chunks_fail(self, tmp_path):
        """Test store command fails when chunks exceed max size."""
        pdf_path = tmp_path / "test.pdf"
        pdf_path.touch()

        with patch("src.commands.store.init_db"), patch(
            "src.commands.store.extract_chunks"
        ) as mock_extract:

            # Create a chunk that exceeds the max size
            oversized_text = "x" * (MAX_CHUNK_CHARS + 1)
            mock_extract.return_value = [
                Chunk(section_path="1.1", page_start="A1", page_end="A1", text=oversized_text)
            ]

            command = StoreCommand(pdf_path=pdf_path, doc_uid=None)
            result = command.execute()

            # Should succeed but truncate the chunk
            assert result.startswith("Stored")
            assert "1 chunks" in result