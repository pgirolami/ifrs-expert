"""Tests for CLI commands."""

import pytest
import json
from unittest.mock import MagicMock, patch
from pathlib import Path


class TestChunkCommand:
    """Tests for chunk command."""

    def test_chunk_command_success(self, tmp_path):
        """Test chunk command extracts and outputs chunks."""
        from src.commands import ChunkCommand
        from src.models.chunk import Chunk

        # Create a mock PDF path
        pdf_path = tmp_path / "test.pdf"
        pdf_path.touch()  # Create the file

        # Mock the extract_chunks function
        with patch("src.commands.chunk.extract_chunks") as mock_extract:
            mock_extract.return_value = [
                Chunk(section_path="1.1", page_start="A1", page_end="A1", text="test content")
            ]

            command = ChunkCommand(pdf_path=pdf_path)
            result = command.execute()

            assert not result.startswith("Error:"), f"Expected success, got error: {result}"
            data = json.loads(result)
            assert len(data) == 1
            mock_extract.assert_called_once_with(pdf_path)

    def test_chunk_command_file_not_found(self):
        """Test chunk command with non-existent file."""
        from src.commands import ChunkCommand

        command = ChunkCommand(pdf_path=Path("/nonexistent/file.pdf"))
        result = command.execute()

        assert result.startswith("Error:")
        assert "not found" in result


class TestStoreCommand:
    """Tests for store command."""

    def test_store_command_success(self, tmp_path):
        """Test store command stores chunks in DB and vector store."""
        from src.commands import StoreCommand
        from src.models.chunk import Chunk

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


class TestListCommand:
    """Tests for list command."""

    def test_list_command_show_docs(self):
        """Test list command shows all documents."""
        from src.commands import ListCommand

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
        from src.commands import ListCommand
        from src.db.chunks import Chunk

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


class TestQueryCommand:
    """Tests for query command."""

    def test_query_no_index(self):
        """Test query command when no index exists."""
        from src.commands import QueryCommand

        with patch("src.commands.query.get_index_path") as mock_path:
            mock_path.return_value.exists.return_value = False

            command = QueryCommand(query="test", k=5, min_score=None)
            result = command.execute()

            assert result.startswith("Error:")
            assert "No index found" in result

    def test_query_with_results(self):
        """Test query returns matching chunks."""
        from src.commands import QueryCommand
        from src.db.chunks import Chunk

        # Mock VectorStore search results (using score instead of distance)
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.8},
        ]

        # Mock chunks returned from database
        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="test text 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="test text 2"),
        ]

        with patch("src.commands.query.VectorStore") as mock_vs_class, patch(
            "src.commands.query.init_db"
        ), patch("src.commands.query.ChunkStore") as mock_cs_class, patch(
            "src.commands.query.get_index_path"
        ) as mock_path:
            # Setup path mock
            mock_path.return_value.exists.return_value = True

            # Setup VectorStore mock
            mock_vs = MagicMock()
            mock_vs.search.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            # Setup ChunkStore mock
            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = QueryCommand(query="test query", k=5, min_score=None, verbose=False)
            result = command.execute()

            # Verify search was called
            mock_vs.search.assert_called_once_with("test query", k=5)
            # Verify chunks were retrieved (called once per unique doc_uid)
            assert mock_cs.get_chunks_by_doc.call_count == 1
            # Verify results
            data = json.loads(result)
            assert len(data) == 2

    def test_query_no_results(self):
        """Test query command with no matching results."""
        from src.commands import QueryCommand

        with patch("src.commands.query.VectorStore") as mock_vs_class, patch(
            "src.commands.query.get_index_path"
        ) as mock_path:
            mock_path.return_value.exists.return_value = True

            mock_vs = MagicMock()
            mock_vs.search.return_value = []
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = QueryCommand(query="test", k=5, min_score=None, verbose=False)
            result = command.execute()

            assert result == "[]"

    def test_query_exception_handling(self):
        """Test query command exception handling."""
        from src.commands import QueryCommand

        with patch("src.commands.query.get_index_path") as mock_path:
            # Make exists() raise an exception
            mock_path.return_value.exists.side_effect = RuntimeError("Test error")

            command = QueryCommand(query="test", k=5, min_score=None, verbose=False)
            result = command.execute()

            assert result.startswith("Error:")
            assert "Test error" in result

    def test_query_score_threshold(self):
        """Test query command with min_score filters results."""
        from src.commands import QueryCommand
        from src.db.chunks import Chunk

        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.3},
        ]

        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="test text 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="test text 2"),
        ]

        with patch("src.commands.query.VectorStore") as mock_vs_class, patch(
            "src.commands.query.init_db"
        ), patch("src.commands.query.ChunkStore") as mock_cs_class, patch(
            "src.commands.query.get_index_path"
        ) as mock_path:

            mock_path.return_value.exists.return_value = True

            mock_vs = MagicMock()
            mock_vs.search.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            # Query with min_score of 0.5 should filter out chunk 2
            # Note: when min_score is set, search is called with k*3
            command = QueryCommand(query="test", k=5, min_score=0.5, verbose=False)
            result = command.execute()

            # Verify search was called with k*3 when min_score is set
            mock_vs.search.assert_called_once_with("test", k=15)

            data = json.loads(result)
            assert len(data) == 1
            assert data[0]["id"] == 1

    def test_query_verbose_output(self):
        """Test query verbose output includes relevance."""
        from src.commands import QueryCommand
        from src.db.chunks import Chunk

        # Mock search results with different scores
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},  # High
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.2},  # Low
        ]

        # Mock chunks returned from database
        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="test text 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="test text 2"),
        ]

        with patch("src.commands.query.VectorStore") as mock_vs_class, patch(
            "src.commands.query.init_db"
        ), patch("src.commands.query.ChunkStore") as mock_cs_class, patch(
            "src.commands.query.get_index_path"
        ) as mock_path:

            mock_path.return_value.exists.return_value = True

            mock_vs = MagicMock()
            mock_vs.search.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            # Test verbose output
            command = QueryCommand(query="test", k=5, min_score=None, verbose=True)
            result = command.execute()

            # Check that High and Low relevance are shown
            assert "(High)" in result
            assert "(Low)" in result
