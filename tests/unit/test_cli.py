"""Tests for CLI commands."""

import pytest
import json
from unittest.mock import MagicMock, patch
from pathlib import Path


class TestChunkCommand:
    """Tests for chunk command."""

    def test_chunk_command_success(self, tmp_path):
        """Test chunk command extracts and outputs chunks."""
        from src.cli import chunk_command
        import argparse
        from unittest.mock import MagicMock

        # Create a mock PDF path
        pdf_path = tmp_path / "test.pdf"
        pdf_path.touch()  # Create the file

        # Mock the extract_chunks function
        with patch("src.cli.extract_chunks") as mock_extract:
            from src.models.chunk import Chunk

            mock_extract.return_value = [
                Chunk(section_path="1.1", page_start="A1", page_end="A1", text="test content")
            ]

            args = argparse.Namespace(pdf=str(pdf_path))
            result = chunk_command(args)

            assert result == 0
            mock_extract.assert_called_once_with(pdf_path)

    def test_chunk_command_file_not_found(self):
        """Test chunk command with non-existent file."""
        from src.cli import chunk_command
        import argparse

        args = argparse.Namespace(pdf="/nonexistent/file.pdf")
        result = chunk_command(args)

        assert result == 1


class TestStoreCommand:
    """Tests for store command."""

    def test_store_command_success(self, tmp_path):
        """Test store command stores chunks in DB and vector store."""
        from src.cli import store_command
        from src.models.chunk import Chunk
        import argparse

        pdf_path = tmp_path / "test.pdf"
        pdf_path.touch()

        with patch("src.cli.init_db"), patch("src.cli.extract_chunks") as mock_extract, patch(
            "src.cli.ChunkStore"
        ) as mock_cs_class, patch("src.cli.VectorStore") as mock_vs_class:

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

            args = argparse.Namespace(pdf=str(pdf_path), doc_uid=None)
            result = store_command(args)

            assert result == 0


class TestListCommand:
    """Tests for list command."""

    def test_list_command_show_docs(self):
        """Test list command shows all documents."""
        from src.cli import list_command
        import argparse

        with patch("src.cli.init_db"), patch("src.cli.ChunkStore") as mock_cs_class:
            mock_cs = MagicMock()
            mock_cs.get_all_docs.return_value = ["doc1", "doc2"]
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            args = argparse.Namespace(doc_uid=None)
            result = list_command(args)

            assert result == 0

    def test_list_command_show_chunks(self):
        """Test list command shows chunks for a doc."""
        from src.cli import list_command
        from src.db.chunks import Chunk
        import argparse

        with patch("src.cli.init_db"), patch("src.cli.ChunkStore") as mock_cs_class:
            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = [
                Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="test")
            ]
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            args = argparse.Namespace(doc_uid="doc1")
            result = list_command(args)

            assert result == 0


class TestQueryCommand:
    """Tests for query command."""

    def test_query_no_index(self):
        """Test query command when no index exists."""
        from src.cli import query_command
        import argparse

        with patch("src.cli.get_index_path") as mock_path:
            mock_path.return_value.exists.return_value = False

            args = argparse.Namespace(query="test", k=5, min_score=None)
            result = query_command(args)

            assert result == 1

    def test_query_with_results(self):
        """Test query returns matching chunks."""
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

        with patch("src.cli.VectorStore") as mock_vs_class, patch("src.cli.init_db"), patch(
            "src.cli.ChunkStore"
        ) as mock_cs_class, patch("src.cli.get_index_path") as mock_path:
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

            from src.cli import query_command
            import argparse

            args = argparse.Namespace(query="test query", k=5, min_score=None)
            result = query_command(args)

            # Verify search was called
            mock_vs.search.assert_called_once_with("test query", k=5)
            # Verify chunks were retrieved (called once per unique doc_uid)
            assert mock_cs.get_chunks_by_doc.call_count == 1

    def test_query_no_results(self):
        """Test query command with no matching results."""
        from src.cli import query_command
        import argparse

        with patch("src.cli.VectorStore") as mock_vs_class, patch("src.cli.get_index_path") as mock_path:
            mock_path.return_value.exists.return_value = True

            mock_vs = MagicMock()
            mock_vs.search.return_value = []
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            args = argparse.Namespace(query="test", k=5, min_score=None)
            result = query_command(args)

            assert result == 0

    def test_query_exception_handling(self):
        """Test query command exception handling."""
        from src.cli import query_command
        import argparse

        with patch("src.cli.get_index_path") as mock_path:
            # Make exists() raise an exception
            mock_path.return_value.exists.side_effect = RuntimeError("Test error")

            args = argparse.Namespace(query="test", k=5, min_score=None)
            result = query_command(args)

            assert result == 1
