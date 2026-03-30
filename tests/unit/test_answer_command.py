"""Tests for answer command."""

from __future__ import annotations

import unittest.mock
from typing import cast

from src.commands.answer import AnswerCommand, AnswerConfig, AnswerOptions
from src.interfaces import SearchResult, SearchVectorStoreProtocol
from src.models.chunk import Chunk
from tests.fakes import InMemoryChunkStore

VALID_PROMPT_B_RESPONSE = """{
  "assumptions_fr": ["Hypothèse de test"],
  "recommendation": {
    "answer": "oui",
    "justification": "Justification de test"
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Le traitement s'applique dans cette situation de test.",
      "conditions_fr": ["Condition de test"],
      "practical_implication_fr": "Implication de test",
      "references": [
        {
          "section": "6.3.1",
          "excerpt": "A hedged item can be a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": ["Point opérationnel de test"]
}"""


class MockVectorStore(SearchVectorStoreProtocol):
    """Minimal mock for VectorStore context manager."""

    def __init__(self, search_results: list[dict[str, str | int | float]]) -> None:
        self._search_results = cast(list[SearchResult], search_results)

    def __enter__(self) -> "MockVectorStore":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[SearchResult]:
        return self._search_results


class MockIndexPath:
    """Mock index path."""

    def __init__(self, exists: bool = True) -> None:
        self._exists = exists

    def exists(self) -> bool:
        return self._exists


class TestAnswerCommand:
    """Tests for answer command using dependency injection."""

    def test_answer_no_index(self) -> None:
        """Test answer command when no index exists."""
        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=False),
            send_to_llm_fn=lambda prompt: "result",
        )
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(k=5))

        result = command.execute()

        assert result.success is False
        assert result.error is not None
        assert "No index found" in result.error

    def test_answer_with_results_returns_result_artifacts(self) -> None:
        """Test answer command returns a structured result with artifacts."""
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

        call_count = [0]

        def mock_send_to_llm(prompt: str) -> str:
            call_count[0] += 1
            if call_count[0] == 1:
                return '{"status": "pass", "approaches": []}'
            return VALID_PROMPT_B_RESPONSE

        config = AnswerConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
        )
        command = AnswerCommand(query="What is the scope?", config=config, options=AnswerOptions(k=5))

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True), unittest.mock.patch(
            "src.commands.answer._read_prompt_template",
        ) as mock_read_template:
            mock_read_template.side_effect = lambda path: "You are an IFRS expert.\n\nContext:\n{{CHUNKS}}\n\nQuestion: {{QUERY}}\n\nAnswer:"

            result = command.execute()

        assert result.success is True
        assert result.error is None
        assert result.prompt_a_text is not None
        assert result.prompt_a_raw_response == '{"status": "pass", "approaches": []}'
        assert result.prompt_a_json is not None
        assert result.prompt_b_text is not None
        assert result.prompt_b_raw_response == VALID_PROMPT_B_RESPONSE
        assert result.prompt_b_json is not None
        assert result.prompt_b_markdown is not None
        assert result.retrieved_doc_uids == ["doc1"]

    def test_answer_no_results(self) -> None:
        """Test answer command with no matching results."""
        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=lambda prompt: "result",
        )
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(k=5))

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

        assert result.success is False
        assert result.error == "Error: No chunks retrieved"

    def test_answer_min_score_filter(self) -> None:
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
            if len(captured_prompts) == 1:
                return '{"status": "pass", "approaches": []}'
            return VALID_PROMPT_B_RESPONSE

        config = AnswerConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
        )
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(k=5, min_score=0.5))

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

        assert result.success is True
        assert captured_prompts
        assert "high relevance content" in captured_prompts[0]
        assert "low relevance content" not in captured_prompts[0]

    def test_answer_expand_includes_neighboring_chunks(self) -> None:
        """Test answer expansion includes surrounding chunks in document order."""
        search_results = [{"doc_uid": "doc1", "chunk_id": 2, "score": 0.9}]

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
            if len(captured_prompts) == 1:
                return '{"status": "pass", "approaches": []}'
            return VALID_PROMPT_B_RESPONSE

        config = AnswerConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
        )
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(k=5, expand=1))

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

        assert result.success is True
        prompt_a = captured_prompts[0]
        assert '<Document name="doc1">' in prompt_a
        assert 'id="1"' in prompt_a
        assert 'id="2"' in prompt_a
        assert 'id="3"' in prompt_a

    def test_answer_full_doc_threshold_uses_total_text_size(self) -> None:
        """Test answer includes the full document when total text size is below threshold."""
        search_results = [{"doc_uid": "doc1", "chunk_id": 2, "score": 0.9}]

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
            if len(captured_prompts) == 1:
                return '{"status": "pass", "approaches": []}'
            return VALID_PROMPT_B_RESPONSE

        config = AnswerConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
        )
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(k=5, full_doc_threshold=10))

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True), unittest.mock.patch(
            "src.commands.answer._read_prompt_template",
        ) as mock_read_template:
            mock_read_template.side_effect = lambda path: "Context:\n{{CHUNKS}}\n\nQuestion: {{QUERY}}\n\nAnswer:"

            result = command.execute()

        assert result.success is True
        prompt_a = captured_prompts[0]
        assert 'id="1"' in prompt_a
        assert 'id="2"' in prompt_a
        assert 'id="3"' in prompt_a
