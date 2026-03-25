"""Tests for list command."""

import json
from unittest.mock import MagicMock, patch

from src.commands import ListCommand
from src.db.chunks import Chunk


class TestListCommand:
    """Tests for list command."""

    def test_list_command_show_docs(self):
        """Test list command shows all documents."""
        with patch("src.commands.list.init_db"), patch(
            "src.commands.list.ChunkStore"
        ) as mock_cs_class:
            mock_cs = MagicMock()
            mock_cs.get_all_docs.return_value = ["doc1", "doc2"]
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = ListCommand(doc_uid=None)
            result = command.execute()

            assert not result.startswith("Error:"), f"Expected success, got error: {result}"
            data = json.loads(result)
            assert data == ["doc1", "doc2"]

    def test_list_command_show_chunks(self):
        """Test list command shows chunks for a doc."""
        with patch("src.commands.list.init_db"), patch(
            "src.commands.list.ChunkStore"
        ) as mock_cs_class:
            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = [
                Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="test")
            ]
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = ListCommand(doc_uid="doc1")
            result = command.execute()

            assert not result.startswith("Error:"), f"Expected success, got error: {result}"
            data = json.loads(result)
            assert len(data) == 1