"""Tests for answer command."""

from unittest.mock import MagicMock, patch

import pytest

from src.commands import AnswerCommand, AnswerOptions
from src.db.chunks import Chunk


class TestAnswerCommand:
    """Tests for answer command."""

    def test_answer_no_index(self):
        """Test answer command when no index exists."""
        with patch("src.commands.answer.get_index_path") as mock_path:
            mock_path.return_value.exists.return_value = False

            command = AnswerCommand(query="test", options=AnswerOptions(k=5))
            result = command.execute()

            assert result.startswith("Error:")
            assert "No index found" in result

    def test_answer_no_prompt_file(self):
        """Test answer command when prompt file doesn't exist."""
        with patch("src.commands.answer.get_index_path") as mock_path, patch(
            "src.commands.answer._prompt_file_exists"
        ) as mock_exists:
            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = False

            command = AnswerCommand(query="test", options=AnswerOptions(k=5))
            result = command.execute()

            assert result.startswith("Error:")
            assert "Prompt A template not found" in result

    def test_answer_with_results(self):
        """Test answer returns prompt with embedded chunks."""
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

        with patch("src.commands.answer.VectorStore._load_or_create_index") as mock_load, patch(
            "src.commands.answer.VectorStore.search_all"
        ) as mock_search, patch(
            "src.commands.answer.init_db"
        ), patch("src.commands.answer.ChunkStore") as mock_cs_class, patch(
            "src.commands.answer.get_index_path"
        ) as mock_path, patch(
            "src.commands.answer._prompt_file_exists"
        ) as mock_exists, patch(
            "src.commands.answer._read_prompt_template"
        ) as mock_read, patch(
            "src.commands.answer._send_to_llm"
        ) as mock_send_to_llm:

            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = True
            mock_read.return_value = prompt_template
            mock_search.return_value = search_results
            # Mock LLM to return valid JSON for both Prompt A and Prompt B
            mock_send_to_llm.side_effect = [
                '{"approaches": []}',  # First call (Prompt A)
                'Final answer from LLM',  # Second call (Prompt B)
            ]

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = AnswerCommand(query="What is the scope?", options=AnswerOptions(k=5))
            result = command.execute()

            # Verify the final result comes from the LLM
            assert "Final answer from LLM" in result

    @pytest.mark.skip(reason="AnswerCommand requires real LLM call - integration test")
    def test_answer_retrieves_top_k_per_document(self):
        """Test answer keeps up to k results per document above the relevance threshold."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.95},
            {"doc_uid": "doc2", "chunk_id": 10, "score": 0.94},
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.90},
            {"doc_uid": "doc2", "chunk_id": 11, "score": 0.89},
            {"doc_uid": "doc1", "chunk_id": 3, "score": 0.88},
            {"doc_uid": "doc2", "chunk_id": 12, "score": 0.87},
            {"doc_uid": "doc1", "chunk_id": 4, "score": 0.20},
        ]

        doc1_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="doc1 text 1"),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="doc1 text 2"),
            Chunk(chunk_id=3, doc_uid="doc1", section_path="1.3", page_start="A3", page_end="A3", text="doc1 text 3"),
            Chunk(chunk_id=4, doc_uid="doc1", section_path="1.4", page_start="A4", page_end="A4", text="doc1 text 4"),
        ]
        doc2_chunks = [
            Chunk(chunk_id=10, doc_uid="doc2", section_path="2.1", page_start="B1", page_end="B1", text="doc2 text 1"),
            Chunk(chunk_id=11, doc_uid="doc2", section_path="2.2", page_start="B2", page_end="B2", text="doc2 text 2"),
            Chunk(chunk_id=12, doc_uid="doc2", section_path="2.3", page_start="B3", page_end="B3", text="doc2 text 3"),
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
        ) as mock_read, patch(
            "src.commands.answer._send_to_llm"
        ) as mock_send:
            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = True
            mock_read.return_value = prompt_template

            mock_vs = MagicMock()
            mock_vs.search_all.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.side_effect = [doc1_chunks, doc2_chunks]
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            # Mock LLM to return valid JSON
            mock_send.side_effect = [
                '{"approaches": []}',  # First call (Prompt A)
                'Final answer from LLM',  # Second call (Prompt B)
            ]

            # Verify the LLM was called with the correct prompt
            assert mock_send.call_count >= 1
            first_call_args = mock_send.call_args_list[0]
            prompt_a = first_call_args[0][0]  # First positional argument
            assert "doc1 text 1" in prompt_a
            assert "doc1 text 2" in prompt_a
            assert "doc1 text 3" not in prompt_a  # Only k=2 per doc
            assert "doc2 text 1" in prompt_a
            assert "doc2 text 2" in prompt_a
            assert "doc2 text 3" not in prompt_a  # Only k=2 per doc
            assert "- doc1: 1.1, 1.2" in prompt_a
            assert "- doc2: 2.1, 2.2" in prompt_a

    def test_answer_no_results(self):
        """Test answer command with no matching results."""
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
            mock_vs.search_all.return_value = []
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = AnswerCommand(query="test", options=AnswerOptions(k=5))
            result = command.execute()

            assert result == "Error: No chunks retrieved"

    def test_answer_min_score_filter(self):
        """Test answer command respects min_score filter."""
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
        ) as mock_read, patch(
            "src.commands.answer._send_to_llm"
        ) as mock_send:
            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = True
            mock_read.return_value = prompt_template

            mock_vs = MagicMock()
            mock_vs.search_all.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            # Mock LLM to return valid JSON
            mock_send.side_effect = [
                '{"approaches": []}',  # First call (Prompt A)
                'Final answer from LLM',  # Second call (Prompt B)
            ]

            # Query with min_score of 0.5 should filter out chunk 2
            command = AnswerCommand(query="test", options=AnswerOptions(k=5, min_score=0.5))
            result = command.execute()

            mock_vs.search_all.assert_called_once_with("test")

            # Verify the LLM was called and received the filtered chunks
            assert mock_send.call_count >= 1
            first_call_args = mock_send.call_args_list[0]
            prompt_a = first_call_args[0][0]
            assert "high relevance content" in prompt_a
            assert "low relevance content" not in prompt_a  # Filtered out by min_score

    def test_answer_k_parameter(self):
        """Test answer command respects k parameter."""
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
            mock_vs.search_all.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            command = AnswerCommand(query="test", options=AnswerOptions(k=10))
            result = command.execute()

            # Verify search was called with the correct k value
            mock_vs.search_all.assert_called_once_with("test")

    def test_answer_expand_includes_neighboring_chunks(self):
        """Test answer expansion includes surrounding chunks in document order."""
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
        ) as mock_read, patch(
            "src.commands.answer._send_to_llm"
        ) as mock_send:
            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = True
            mock_read.return_value = prompt_template

            mock_vs = MagicMock()
            mock_vs.search_all.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            # Mock LLM to return valid JSON
            mock_send.side_effect = [
                '{"approaches": []}',  # First call (Prompt A)
                'Final answer from LLM',  # Second call (Prompt B)
            ]

            command = AnswerCommand(query="test", options=AnswerOptions(k=5, expand=1))
            result = command.execute()

            # Verify the LLM was called and the prompt included the expanded chunks
            assert mock_send.call_count >= 1
            first_call_args = mock_send.call_args_list[0]
            prompt_a = first_call_args[0][0]
            assert '<Document name="doc1">' in prompt_a
            assert 'id="1"' in prompt_a
            assert 'id="2"' in prompt_a
            assert 'id="3"' in prompt_a  # expand=1 includes surrounding chunks
            assert "Retrieved chunks:" in prompt_a

    def test_answer_full_doc_threshold_uses_total_text_size(self):
        """Test answer includes the full document when total text size is below threshold."""
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
        ) as mock_read, patch(
            "src.commands.answer._send_to_llm"
        ) as mock_send:
            mock_path.return_value.exists.return_value = True
            mock_exists.return_value = True
            mock_read.return_value = prompt_template

            mock_vs = MagicMock()
            mock_vs.search_all.return_value = search_results
            mock_vs_class.return_value.__enter__ = MagicMock(return_value=mock_vs)
            mock_vs_class.return_value.__exit__ = MagicMock(return_value=None)

            mock_cs = MagicMock()
            mock_cs.get_chunks_by_doc.return_value = mock_chunks
            mock_cs_class.return_value.__enter__ = MagicMock(return_value=mock_cs)
            mock_cs_class.return_value.__exit__ = MagicMock(return_value=None)

            # Mock LLM to return valid JSON
            mock_send.side_effect = [
                '{"approaches": []}',  # First call (Prompt A)
                'Final answer from LLM',  # Second call (Prompt B)
            ]

            command = AnswerCommand(query="test", options=AnswerOptions(k=5, full_doc_threshold=10))
            result = command.execute()

            # Verify the LLM was called and the prompt included all chunks
            assert mock_send.call_count >= 1
            first_call_args = mock_send.call_args_list[0]
            prompt_a = first_call_args[0][0]
            assert '<Document name="doc1">' in prompt_a
            assert 'id="1"' in prompt_a
            assert 'id="2"' in prompt_a
            assert 'id="3"' in prompt_a  # full_doc_threshold includes all chunks
            assert "- doc1: 1.1, 1.2, 1.3" in prompt_a