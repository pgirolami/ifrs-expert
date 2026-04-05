"""Tests for chunk command."""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

from src.commands import ChunkCommand
from src.models.chunk import Chunk


class TestChunkCommand:
    """Tests for chunk command."""

    def test_chunk_command_success(self, tmp_path):
        """Test chunk command extracts and outputs chunks."""
        # Create a mock PDF path
        pdf_path = tmp_path / "test.pdf"
        pdf_path.touch()  # Create the file

        # Mock the extract_chunks function
        with patch("src.commands.chunk.extract_chunks") as mock_extract:
            mock_extract.return_value = [
                Chunk(chunk_number="1.1", page_start="A1", page_end="A1", text="test content")
            ]

            command = ChunkCommand(pdf_path=pdf_path)
            result = command.execute()

            assert not result.startswith("Error:"), f"Expected success, got error: {result}"
            data = json.loads(result)
            assert len(data) == 1
            mock_extract.assert_called_once_with(pdf_path)

    def test_chunk_command_file_not_found(self):
        """Test chunk command with non-existent file."""
        command = ChunkCommand(pdf_path=Path("/nonexistent/file.pdf"))
        result = command.execute()

        assert result.startswith("Error:")
        assert "not found" in result