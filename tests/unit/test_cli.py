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

    def test_store_command_oversized_chunks_fail(self, tmp_path):
        """Test store command fails when chunks exceed max size."""
        from src.commands import StoreCommand
        from src.commands.store import MAX_CHUNK_CHARS
        from src.models.chunk import Chunk

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

            assert result.startswith("Error:")
            assert "exceeding" in result
            assert str(MAX_CHUNK_CHARS) in result


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

    def test_query_expand_includes_neighboring_chunks(self):
        """Test query expansion includes surrounding chunks in document order."""
        from src.commands import QueryCommand
        from src.db.chunks import Chunk

        search_results = [
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.9},
        ]

        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="chunk 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="chunk 2"),
            Chunk(chunk_id=3, doc_uid="doc1", section_path="1.3", page_start="A3", page_end="A3", text="chunk 3"),
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

            command = QueryCommand(query="test", k=5, min_score=None, verbose=False, expand=1)
            result = command.execute()

            data = json.loads(result)
            assert [item["id"] for item in data] == [1, 2, 3]
            assert data[1]["score"] == 0.9
            assert data[0]["score"] == 0.0
            assert data[2]["score"] == 0.0

    def test_query_full_doc_threshold_uses_total_text_size(self):
        """Test query includes the full document when total text size is below threshold."""
        from src.commands import QueryCommand
        from src.db.chunks import Chunk

        search_results = [
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.9},
        ]

        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="aa"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="bbb"),
            Chunk(chunk_id=3, doc_uid="doc1", section_path="1.3", page_start="A3", page_end="A3", text="cccc"),
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

            command = QueryCommand(
                query="test",
                k=5,
                min_score=None,
                verbose=False,
                expand=0,
                full_doc_threshold=10,
            )
            result = command.execute()

            data = json.loads(result)
            assert [item["id"] for item in data] == [1, 2, 3]
            assert data[1]["score"] == 0.9
            assert data[0]["score"] == 0.0
            assert data[2]["score"] == 0.0


class TestAnswerCommand:
    """Tests for answer command."""

    def test_answer_no_index(self):
        """Test answer command when no index exists."""
        from src.commands import AnswerCommand

        with patch("src.commands.answer.get_index_path") as mock_path:
            mock_path.return_value.exists.return_value = False

            command = AnswerCommand(query="test", k=5)
            result = command.execute()

            assert result.startswith("Error:")
            assert "No index found" in result

    def test_answer_no_prompt_file(self):
        """Test answer command when prompt file doesn't exist."""
        from src.commands import AnswerCommand

        with patch("src.commands.answer.get_index_path") as mock_path, patch(
            "src.commands.answer._prompt_file_exists"
        ) as mock_exists:
            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = False

            command = AnswerCommand(query="test", k=5)
            result = command.execute()

            assert result.startswith("Error:")
            assert "Prompt template not found" in result

    def test_answer_with_results(self):
        """Test answer returns prompt with embedded chunks."""
        from src.commands import AnswerCommand
        from src.db.chunks import Chunk

        # Mock VectorStore search results
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.8},
        ]

        # Mock chunks returned from database
        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1 Introduction", page_start="A1", page_end="A1", text="This is the introduction section."),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2 Scope", page_start="A2", page_end="A2", text="This standard applies to all entities."),
        ]

        # Mock prompt template
        prompt_template = "Answer the user's question based on the provided context.\n\n<context>\n{{CHUNKS}}\n</context>\n\nQuestion: {{QUERY}}\n\nAnswer:"

        with patch("src.commands.answer.VectorStore") as mock_vs_class, patch(
            "src.commands.answer.init_db"
        ), patch("src.commands.answer.ChunkStore") as mock_cs_class, patch(
            "src.commands.answer.get_index_path"
        ) as mock_path, patch(
            "src.commands.answer._prompt_file_exists"
        ) as mock_exists, patch(
            "src.commands.answer._read_prompt_template"
        ) as mock_read:

            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = True
            mock_read.return_value = prompt_template

            mock_vs = MagicMock()
            mock_vs.search.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = AnswerCommand(query="What is the scope?", k=5)
            result = command.execute()

            # Verify search was called
            mock_vs.search.assert_called_once_with("What is the scope?", k=5)

            # Verify the result contains the prompt template with chunks
            assert "Answer the user's question" in result
            assert "Question: What is the scope?" in result
            assert "Retrieved chunks:" in result
            assert "- doc1: 1.1 Introduction, 1.2 Scope" in result
            # Verify chunks are embedded with section_path metadata in XML format
            assert '<Document name="doc1">' in result
            assert "section_path=" in result
            assert "1.1 Introduction" in result
            assert "1.2 Scope" in result
            assert "</Document>" in result

    def test_answer_no_results(self):
        """Test answer command with no matching results."""
        from src.commands import AnswerCommand

        prompt_template = "Answer based on context.\n\n<context>\n{{CHUNKS}}\n</context>\n\nQuestion: {{QUERY}}\n\nAnswer:"

        with patch("src.commands.answer.VectorStore") as mock_vs_class, patch(
            "src.commands.answer.get_index_path"
        ) as mock_path, patch(
            "src.commands.answer._prompt_file_exists"
        ) as mock_exists, patch(
            "src.commands.answer._read_prompt_template"
        ) as mock_read:

            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = True
            mock_read.return_value = prompt_template

            mock_vs = MagicMock()
            mock_vs.search.return_value = []
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = AnswerCommand(query="test", k=5)
            result = command.execute()

            # Should still return a valid prompt but with empty chunks placeholder
            # When chunks list is empty, the template is returned with empty {{CHUNKS}}
            assert "Question: test" in result
            assert "Answer based on context" in result
            assert "Retrieved chunks:\n- none" in result

    def test_answer_min_score_filter(self):
        """Test answer command respects min_score filter."""
        from src.commands import AnswerCommand
        from src.db.chunks import Chunk

        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.3},
        ]

        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="high relevance content"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="low relevance content"),
        ]

        prompt_template = "Context:\n{{CHUNKS}}\n\nQ: {{QUERY}}\n\nA:"

        with patch("src.commands.answer.VectorStore") as mock_vs_class, patch(
            "src.commands.answer.init_db"
        ), patch("src.commands.answer.ChunkStore") as mock_cs_class, patch(
            "src.commands.answer.get_index_path"
        ) as mock_path, patch(
            "src.commands.answer._prompt_file_exists"
        ) as mock_exists, patch(
            "src.commands.answer._read_prompt_template"
        ) as mock_read:

            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = True
            mock_read.return_value = prompt_template

            mock_vs = MagicMock()
            mock_vs.search.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            # Query with min_score of 0.5 should filter out chunk 2
            command = AnswerCommand(query="test", k=5, min_score=0.5)
            result = command.execute()

            # Verify search was called with k*3 when min_score is set
            mock_vs.search.assert_called_once_with("test", k=15)

            # Only high score chunk should be in output
            assert "high relevance content" in result
            assert "low relevance content" not in result

    def test_answer_k_parameter(self):
        """Test answer command respects k parameter."""
        from src.commands import AnswerCommand

        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
        ]

        prompt_template = "Context:\n{{CHUNKS}}\n\nQ: {{QUERY}}\n\nA:"

        with patch("src.commands.answer.VectorStore") as mock_vs_class, patch(
            "src.commands.answer.get_index_path"
        ) as mock_path, patch(
            "src.commands.answer._prompt_file_exists"
        ) as mock_exists, patch(
            "src.commands.answer._read_prompt_template"
        ) as mock_read:

            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = True
            mock_read.return_value = prompt_template

            mock_vs = MagicMock()
            mock_vs.search.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = AnswerCommand(query="test", k=10)
            result = command.execute()

            # Verify search was called with the correct k value
            mock_vs.search.assert_called_once_with("test", k=10)

    def test_answer_expand_includes_neighboring_chunks(self):
        """Test answer expansion includes surrounding chunks in document order."""
        from src.commands import AnswerCommand
        from src.db.chunks import Chunk

        search_results = [
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.9},
        ]

        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="chunk 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="chunk 2"),
            Chunk(chunk_id=3, doc_uid="doc1", section_path="1.3", page_start="A3", page_end="A3", text="chunk 3"),
        ]

        prompt_template = "Context:\n{{CHUNKS}}\n\nQ: {{QUERY}}\n\nA:"

        with patch("src.commands.answer.VectorStore") as mock_vs_class, patch(
            "src.commands.answer.init_db"
        ), patch("src.commands.answer.ChunkStore") as mock_cs_class, patch(
            "src.commands.answer.get_index_path"
        ) as mock_path, patch(
            "src.commands.answer._prompt_file_exists"
        ) as mock_exists, patch(
            "src.commands.answer._read_prompt_template"
        ) as mock_read:
            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = True
            mock_read.return_value = prompt_template

            mock_vs = MagicMock()
            mock_vs.search.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = AnswerCommand(query="test", k=5, expand=1)
            result = command.execute()

            assert '<Document name="doc1">' in result
            assert result.index('id="1"') < result.index('id="2"') < result.index('id="3"')
            assert "Retrieved chunks:" in result
            assert "- doc1: 1.1, 1.2, 1.3" in result
            assert "chunk 1" in result
            assert "chunk 2" in result
            assert "chunk 3" in result

    def test_answer_full_doc_threshold_uses_total_text_size(self):
        """Test answer includes the full document when total text size is below threshold."""
        from src.commands import AnswerCommand
        from src.db.chunks import Chunk

        search_results = [
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.9},
        ]

        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="aa"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="bbb"),
            Chunk(chunk_id=3, doc_uid="doc1", section_path="1.3", page_start="A3", page_end="A3", text="cccc"),
        ]

        prompt_template = "Context:\n{{CHUNKS}}\n\nQ: {{QUERY}}\n\nA:"

        with patch("src.commands.answer.VectorStore") as mock_vs_class, patch(
            "src.commands.answer.init_db"
        ), patch("src.commands.answer.ChunkStore") as mock_cs_class, patch(
            "src.commands.answer.get_index_path"
        ) as mock_path, patch(
            "src.commands.answer._prompt_file_exists"
        ) as mock_exists, patch(
            "src.commands.answer._read_prompt_template"
        ) as mock_read:
            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = True
            mock_read.return_value = prompt_template

            mock_vs = MagicMock()
            mock_vs.search.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = AnswerCommand(query="test", k=5, full_doc_threshold=10)
            result = command.execute()

            assert '<Document name="doc1">' in result
            assert result.index('id="1"') < result.index('id="2"') < result.index('id="3"')
            assert "- doc1: 1.1, 1.2, 1.3" in result
            assert "aa" in result
            assert "bbb" in result
            assert "cccc" in result
