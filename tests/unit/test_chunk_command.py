"""Tests for chunk command."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

from src.commands.chunk import ChunkCommand
from src.models.chunk import Chunk
from src.models.document import DocumentRecord
from src.models.extraction import ExtractedDocument


class TestChunkCommand:
    """Tests for chunk command."""

    def test_chunk_command_success(self, tmp_path: Path) -> None:
        """Test chunk command extracts and outputs chunks from HTML."""
        html_path = tmp_path / "test.html"
        html_path.touch()

        extracted_document = ExtractedDocument(
            document=DocumentRecord(
                doc_uid="ifrs9",
                source_type="html",
                source_title="IFRS 9",
                source_url="https://www.ifrs.org/ifrs9.html",
                canonical_url="https://www.ifrs.org/ifrs9.html",
                captured_at="2026-04-04T14:23:10Z",
            ),
            chunks=[Chunk(chunk_number="2.4", page_start="", page_end="", text="test content")],
        )

        with patch("src.commands.chunk.HtmlExtractor") as mock_extractor_cls:
            mock_extractor = mock_extractor_cls.return_value
            mock_extractor.extract.return_value = extracted_document

            command = ChunkCommand(html_path=html_path)
            result = command.execute()

            assert not result.startswith("Error:"), f"Expected success, got error: {result}"
            data = json.loads(result)
            assert len(data) == 1
            mock_extractor.extract.assert_called_once_with(html_path, None)

    def test_chunk_command_file_not_found(self) -> None:
        """Test chunk command with non-existent file."""
        command = ChunkCommand(html_path=Path("/nonexistent/file.html"))
        result = command.execute()

        assert result.startswith("Error:")
        assert "not found" in result
