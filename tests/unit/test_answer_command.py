"""Tests for answer command."""

from pathlib import Path

import pytest
import unittest.mock

from src.commands.answer import AnswerCommand, AnswerOptions
from src.models.chunk import Chunk
from tests.fakes import InMemoryChunkStore


class MockVectorStore:
    """Minimal mock for VectorStore context manager."""

    def __init__(self, search_results: list[dict]) -> None:
        self._search_results = search_results

    def __enter__(self) -> "MockVectorStore":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        pass

    def search_all(self, query: str) -> list[dict]:
        return self._search_results


class MockIndexPath:
    """Mock index path."""

    def __init__(self, exists: bool = True) -> None:
        self._exists = exists

    def exists(self) -> bool:
        return self._exists


class TestAnswerCommand:
    """Tests for answer command using dependency injection."""

    def test_answer_no_index(self):
        """Test answer command when no index exists."""
        command = AnswerCommand(
            query="test",
            vector_store=MockVectorStore([]),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=False),
            send_to_llm_fn=lambda p: "result",
            options=AnswerOptions(k=5),
        )

        result = command.execute()

        assert result.startswith("Error:")
        assert "No index found" in result

    def test_answer_with_results(self):
        """Test answer returns prompt with embedded chunks."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.8},
        ]

        mock_chunks = [
            Chunk(chunk_id=1, doc_uid="doc1", section_path="1.1", page_start="A1", page_end="A1", text="This is the introduction section."),
            Chunk(chunk_id=2, doc_uid="doc1", section_path="1.2", page_start="A2", page_end="A2", text="This standard applies to all entities."),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        # Track calls to mock_send_to_llm
        call_count = [0]

        def mock_send_to_llm(prompt: str) -> str:
            call_count[0] += 1
            # First call is Prompt A -> return JSON, second is Prompt B -> return final
            if call_count[0] == 1:
                return '{"approaches": []}'
            return "Final answer from LLM"

        command = AnswerCommand(
            query="What is the scope?",
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
            options=AnswerOptions(k=5),
        )

        # Mock prompt file existence and reading
        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True), \
             unittest.mock.patch("src.commands.answer._read_prompt_template") as mock_read_template:
            
            # Template returns the prompt with placeholders replaced
            def read_template(path):
                return "You are an IFRS expert.\n\nContext:\n{{CHUNKS}}\n\nQuestion: {{QUERY}}\n\nAnswer:"
            
            mock_read_template.side_effect = read_template

            result = command.execute()

            assert "Final answer from LLM" in result

    def test_answer_no_results(self):
        """Test answer command with no matching results."""
        def mock_send_to_llm(prompt: str) -> str:
            return "result"

        command = AnswerCommand(
            query="test",
            vector_store=MockVectorStore([]),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
            options=AnswerOptions(k=5),
        )

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
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

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        captured_prompts: list[str] = []

        def mock_send_to_llm(prompt: str) -> str:
            captured_prompts.append(prompt)
            if "You are an IFRS expert" in prompt:
                return '{"approaches": []}'
            return "Final answer"

        command = AnswerCommand(
            query="test",
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
            options=AnswerOptions(k=5, min_score=0.5),
        )

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

            # Verify that the low relevance content was filtered out
            assert "high relevance content" in captured_prompts[0]
            assert "low relevance content" not in captured_prompts[0]

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

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        captured_prompts: list[str] = []

        def mock_send_to_llm(prompt: str) -> str:
            captured_prompts.append(prompt)
            if "You are an IFRS expert" in prompt:
                return '{"approaches": []}'
            return "Final answer"

        command = AnswerCommand(
            query="test",
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
            options=AnswerOptions(k=5, expand=1),
        )

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

            prompt_a = captured_prompts[0]
            assert '<Document name="doc1">' in prompt_a
            assert 'id="1"' in prompt_a
            assert 'id="2"' in prompt_a
            assert 'id="3"' in prompt_a  # expand=1 includes surrounding chunks

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

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        captured_prompts: list[str] = []

        def mock_send_to_llm(prompt: str) -> str:
            captured_prompts.append(prompt)
            if 'status": "pass"' in prompt or 'status": "needs_clarification"' in prompt:
                return '{"status": "pass", "approaches": []}'
            return '{"approaches": []}'

        command = AnswerCommand(
            query="test",
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
            options=AnswerOptions(k=5, full_doc_threshold=10),
        )

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True), \
             unittest.mock.patch("src.commands.answer._read_prompt_template") as mock_read_template:
            
            def read_template(path):
                return "Context:\n{{CHUNKS}}\n\nQuestion: {{QUERY}}\n\nAnswer:"
            
            mock_read_template.side_effect = read_template

            result = command.execute()

            prompt_a = captured_prompts[0]
            # All 3 chunks should be included when full_doc_threshold is triggered
            assert 'id="1"' in prompt_a
            assert 'id="2"' in prompt_a
            assert 'id="3"' in prompt_a

    def test_answer_requires_dependencies(self):
        """Test that missing dependencies cause TypeError at construction."""
        with pytest.raises(TypeError):
            AnswerCommand(query="test", vector_store=MockVectorStore([]))  # type: ignore[call-arg]