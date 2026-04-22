"""Tests for answer command."""

from __future__ import annotations

import json
import logging
import unittest.mock

import pytest
from pathlib import Path
from typing import cast

from src.commands.answer import AnswerCommand, AnswerConfig, AnswerOptions
from src.interfaces import DocumentSearchResult, SearchDocumentVectorStoreProtocol, SearchResult, SearchVectorStoreProtocol
from src.models.chunk import Chunk
from src.models.section import SectionRecord
from src.retrieval.models import RetrievalResult
from tests.fakes import InMemoryChunkStore, InMemorySectionStore
from tests.policy import load_test_policy_config, load_test_retrieval_policy, make_retrieval_policy

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
  ]
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


class MockDocumentVectorStore(SearchDocumentVectorStoreProtocol):
    """Minimal mock for document vector store context manager."""

    def __init__(self, search_results: list[dict[str, str | float]]) -> None:
        self._search_results = cast(list[DocumentSearchResult], search_results)

    def __enter__(self) -> "MockDocumentVectorStore":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[DocumentSearchResult]:
        del query
        return self._search_results


class MockIndexPath:
    """Mock index path."""

    def __init__(self, exists: bool = True) -> None:
        self._exists = exists

    def exists(self) -> bool:
        return self._exists


class TestAnswerCommand:
    """Tests for answer command using dependency injection."""

    def test_answer_options_are_stored_on_command(self) -> None:
        """AnswerCommand should retain all option values passed by the caller."""
        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=lambda prompt: "result",
        )
        output_dir = Path("artifacts/test-output")
        command = AnswerCommand(
            query="test",
            config=config,
            options=AnswerOptions(policy=make_retrieval_policy(mode="text"), output_dir=output_dir),
        )

        assert command.output_dir == output_dir

    def test_answer_no_index(self, caplog) -> None:
        """Test answer command logs and fails clearly when no index exists."""
        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=False),
            send_to_llm_fn=lambda prompt: "result",
        )
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text", expand=1)))

        with caplog.at_level(logging.INFO):
            result = command.execute()

        assert result.success is False
        assert result.error is not None
        assert "No index found" in result.error
        assert "Missing vector index" in caplog.text

    def test_answer_with_results_returns_result_artifacts(self) -> None:
        """Test answer command returns a structured result with artifacts."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "doc1", "chunk_id": 2, "score": 0.8},
        ]

        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="This is the introduction section."),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="This standard applies to all entities."),
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
        command = AnswerCommand(query="What is the scope?", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text")))

        with (
            unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True),
            unittest.mock.patch(
                "src.commands.answer._read_prompt_template",
            ) as mock_read_template,
        ):
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
        assert result.prompt_b_memo_markdown is not None
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
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text", expand=1)))

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
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="high relevance content"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="low relevance content"),
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
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text", chunk_min_score=0.5)))

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
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="chunk 1"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="chunk 2"),
            Chunk(id=3, doc_uid="doc1", chunk_number="1.3", page_start="A3", page_end="A3", text="chunk 3"),
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
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text", expand=1)))

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

        assert result.success is True
        prompt_a = captured_prompts[0]
        assert '<Document name="doc1"' in prompt_a
        assert 'document_type="' in prompt_a
        assert 'document_kind="' in prompt_a
        assert 'id="1"' in prompt_a
        assert 'id="2"' in prompt_a
        assert 'id="3"' in prompt_a

    def test_answer_full_doc_threshold_uses_total_text_size(self) -> None:
        """Test answer includes the full document when total text size is below threshold."""
        search_results = [{"doc_uid": "doc1", "chunk_id": 2, "score": 0.9}]

        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="aa"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="bbb"),
            Chunk(id=3, doc_uid="doc1", chunk_number="1.3", page_start="A3", page_end="A3", text="cccc"),
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
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text", full_doc_threshold=2000)))

        with (
            unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True),
            unittest.mock.patch(
                "src.commands.answer._read_prompt_template",
            ) as mock_read_template,
        ):
            mock_read_template.side_effect = lambda path: "Context:\n{{CHUNKS}}\n\nQuestion: {{QUERY}}\n\nAnswer:"

            result = command.execute()

        assert result.success is True
        prompt_a = captured_prompts[0]
        assert 'id="1"' in prompt_a
        assert 'id="2"' in prompt_a
        assert 'id="3"' in prompt_a

    def test_answer_prompt_a_contains_context(self) -> None:
        """Test that prompt A contains the retrieved chunk content."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
        ]

        unique_chunk_text = "UNIQUE_MARKER_12345_CONTEXT_CONTENT"
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text=unique_chunk_text),
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
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text", expand=1)))

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

        assert result.success is True
        assert len(captured_prompts) == 2
        prompt_a = captured_prompts[0]
        assert unique_chunk_text in prompt_a, "Prompt A should contain the chunk context"

    def test_answer_expand_to_section_includes_descendant_section_chunks(self) -> None:
        """Section expansion should include all chunks in the matched section subtree."""
        search_results = [{"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.91}]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(
                [
                    Chunk(id=1, doc_uid="ifrs9", chunk_number="3.0", page_start="A1", page_end="A1", chunk_id="IFRS09_3.0", containing_section_id="IFRS09_0054", text="chapter text"),
                    Chunk(id=2, doc_uid="ifrs9", chunk_number="3.1.1", page_start="A2", page_end="A2", chunk_id="IFRS09_3.1.1", containing_section_id="IFRS09_g3.1.1-3.1.2", text="initial recognition text"),
                ]
            )

        section_store = InMemorySectionStore()
        with section_store as store:
            store.insert_sections(
                [
                    SectionRecord(
                        section_id="IFRS09_0054",
                        doc_uid="ifrs9",
                        parent_section_id=None,
                        level=2,
                        title="Recognition and derecognition",
                        section_lineage=["Recognition and derecognition"],
                        position=1,
                    ),
                    SectionRecord(
                        section_id="IFRS09_g3.1.1-3.1.2",
                        doc_uid="ifrs9",
                        parent_section_id="IFRS09_0054",
                        level=3,
                        title="Initial recognition",
                        section_lineage=["Recognition and derecognition", "Initial recognition"],
                        position=2,
                    ),
                ]
            )
            store.add_descendant_mapping("IFRS09_0054", ["IFRS09_0054", "IFRS09_g3.1.1-3.1.2"])

        captured_prompts: list[str] = []

        def mock_send_to_llm(prompt: str) -> str:
            captured_prompts.append(prompt)
            if len(captured_prompts) == 1:
                return '{"status": "pass", "approaches": []}'
            return VALID_PROMPT_B_RESPONSE

        config = AnswerConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            section_store=section_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
        )
        command = AnswerCommand(
            query="recognition",
            config=config,
            options=AnswerOptions(policy=make_retrieval_policy(mode="text")),
        )

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

        assert result.success is True
        assert captured_prompts
        assert "chapter text" in captured_prompts[0]
        assert "initial recognition text" in captured_prompts[0]

    def test_answer_documents_mode_filters_prompt_context_to_selected_documents(self) -> None:
        """Document-first retrieval should only keep chunks from preselected documents."""
        search_results = [
            {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.91},
            {"doc_uid": "ias21", "chunk_id": 2, "score": 0.89},
        ]
        document_search_results = [
            {"doc_uid": "ias21", "score": 0.95},
            {"doc_uid": "ifrs9", "score": 0.80},
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(
                [
                    Chunk(id=1, doc_uid="ifrs9", chunk_number="1.1", page_start="A1", page_end="A1", text="ifrs chunk text"),
                    Chunk(id=2, doc_uid="ias21", chunk_number="2.1", page_start="B1", page_end="B1", text="ias chunk text"),
                ]
            )

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
            document_vector_store=MockDocumentVectorStore(document_search_results),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
        )
        command = AnswerCommand(
            query="foreign operation",
            config=config,
            options=AnswerOptions(policy=make_retrieval_policy(d=1, chunk_min_score=0.5, expand=0, mode="documents")),
        )

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

        assert result.success is True
        assert result.retrieved_doc_uids == ["ias21"]
        assert captured_prompts
        assert "ias chunk text" in captured_prompts[0]
        assert "ifrs chunk text" not in captured_prompts[0]

    def test_answer_documents_mode_passes_per_type_thresholds_to_retrieval(self) -> None:
        """Answer command should pass per-type document controls into the shared retrieval request."""
        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(
                [
                    Chunk(id=1, doc_uid="ifrs9", chunk_number="1.1", page_start="A1", page_end="A1", text="ifrs chunk text"),
                ]
            )

        captured_prompts: list[str] = []
        captured_requests: list[object] = []

        def mock_send_to_llm(prompt: str) -> str:
            captured_prompts.append(prompt)
            if len(captured_prompts) == 1:
                return '{"status": "pass", "approaches": []}'
            return VALID_PROMPT_B_RESPONSE

        def mock_execute_retrieval(*, request: object, config: object) -> tuple[None, RetrievalResult]:
            del config
            captured_requests.append(request)
            return (
                None,
                RetrievalResult(
                    retrieval_mode="documents",
                    document_hits=[],
                    chunk_results=[{"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.9}],
                    doc_chunks={
                        "ifrs9": [
                            Chunk(
                                id=1,
                                doc_uid="ifrs9",
                                chunk_number="1.1",
                                page_start="A1",
                                page_end="A1",
                                text="ifrs chunk text",
                            )
                        ]
                    },
                ),
            )

        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            document_vector_store=MockDocumentVectorStore([]),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
        )
        command = AnswerCommand(
            query="foreign operation",
            config=config,
            options=AnswerOptions(policy=make_retrieval_policy(
                k=3,
                d=9,
                chunk_min_score=0.1,
                expand=1,
                full_doc_threshold=2000,
                expand_to_section=True,
                per_type_d={
                    "IFRS-S": 7,
                    "IAS-S": 6,
                    "IFRIC": 4,
                    "SIC": 3,
                    "PS": 2,
                    "NAVIS": 5,
                },
                per_type_min_score={
                    "IFRS-S": 0.61,
                    "IAS-S": 0.54,
                    "IFRIC": 0.50,
                    "SIC": 0.49,
                    "PS": 0.48,
                    "NAVIS": 0.47,
                },
                mode="documents",
            )),
        )

        with (
            unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True),
            unittest.mock.patch("src.commands.answer.execute_retrieval", side_effect=mock_execute_retrieval),
        ):
            result = command.execute()

        assert result.success is True
        assert len(captured_requests) == 1
        request = captured_requests[0]
        assert getattr(request, "retrieval_mode") == "documents"
        assert getattr(request, "k") == 3
        assert getattr(request, "d") == 9
        document_d_by_type = getattr(request, "document_d_by_type")
        document_min_score_by_type = getattr(request, "document_min_score_by_type")
        assert document_d_by_type["IFRS-S"] == 7
        assert document_d_by_type["IAS-S"] == 6
        assert document_d_by_type["IFRIC"] == 4
        assert document_d_by_type["SIC"] == 3
        assert document_d_by_type["PS"] == 2
        assert document_d_by_type["NAVIS"] == 5
        assert document_min_score_by_type["IFRS-S"] == 0.61
        assert document_min_score_by_type["IAS-S"] == 0.54
        assert document_min_score_by_type["IFRIC"] == 0.50
        assert document_min_score_by_type["SIC"] == 0.49
        assert document_min_score_by_type["PS"] == 0.48
        assert document_min_score_by_type["NAVIS"] == 0.47
        assert getattr(request, "chunk_min_score") == 0.1
        assert getattr(request, "expand_to_section") is True
        assert getattr(request, "expand") == 1
        assert getattr(request, "full_doc_threshold") == 2000

    def test_answer_documents2_mode_passes_through_retrieval_mode(self) -> None:
        """Answer command should allow documents2 mode and pass it to retrieval."""
        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(
                [
                    Chunk(id=1, doc_uid="ifrs9", chunk_number="1.1", page_start="A1", page_end="A1", text="ifrs chunk text"),
                ]
            )

        captured_requests: list[object] = []

        def mock_send_to_llm(prompt: str) -> str:
            del prompt
            return '{"status": "pass", "approaches": []}'

        def mock_execute_retrieval(*, request: object, config: object) -> tuple[None, RetrievalResult]:
            del config
            captured_requests.append(request)
            return (
                None,
                RetrievalResult(
                    retrieval_mode="documents2",
                    document_hits=[],
                    chunk_results=[{"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.9}],
                    doc_chunks={
                        "ifrs9": [
                            Chunk(
                                id=1,
                                doc_uid="ifrs9",
                                chunk_number="1.1",
                                page_start="A1",
                                page_end="A1",
                                text="ifrs chunk text",
                            )
                        ]
                    },
                ),
            )

        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            document_vector_store=MockDocumentVectorStore([]),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
        )
        command = AnswerCommand(
            query="foreign operation",
            config=config,
            options=AnswerOptions(policy=make_retrieval_policy(k=3, d=9, chunk_min_score=0.1, expand=1, full_doc_threshold=2000, expand_to_section=True, mode="documents2")),
        )

        with (
            unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True),
            unittest.mock.patch("src.commands.answer.execute_retrieval", side_effect=mock_execute_retrieval),
        ):
            result = command.execute()

        assert result.success is True
        assert len(captured_requests) == 1
        request = captured_requests[0]
        assert getattr(request, "retrieval_mode") == "documents2"
        assert getattr(request, "expand_to_section") is True

    def test_answer_documents2_through_chunks_mode_passes_through_retrieval_mode(self) -> None:
        """Answer command should allow documents2-through-chunks mode and pass it to retrieval."""
        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(
                [
                    Chunk(id=1, doc_uid="ifrs9", chunk_number="1.1", page_start="A1", page_end="A1", text="ifrs chunk text"),
                ]
            )

        captured_requests: list[object] = []

        def mock_send_to_llm(prompt: str) -> str:
            del prompt
            return '{"status": "pass", "approaches": []}'

        def mock_execute_retrieval(*, request: object, config: object) -> tuple[None, RetrievalResult]:
            del config
            captured_requests.append(request)
            return (
                None,
                RetrievalResult(
                    retrieval_mode="documents2-through-chunks",
                    document_hits=[],
                    chunk_results=[{"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.9}],
                    doc_chunks={
                        "ifrs9": [
                            Chunk(
                                id=1,
                                doc_uid="ifrs9",
                                chunk_number="1.1",
                                page_start="A1",
                                page_end="A1",
                                text="ifrs chunk text",
                            )
                        ]
                    },
                ),
            )

        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
        )
        command = AnswerCommand(
            query="foreign operation",
            config=config,
            options=AnswerOptions(policy=make_retrieval_policy(k=3, d=9, chunk_min_score=0.1, expand=1, full_doc_threshold=2000, expand_to_section=True, mode="documents2-through-chunks")),
        )

        with (
            unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True),
            unittest.mock.patch("src.commands.answer.execute_retrieval", side_effect=mock_execute_retrieval),
        ):
            result = command.execute()

        assert result.success is True
        assert len(captured_requests) == 1
        request = captured_requests[0]
        assert getattr(request, "retrieval_mode") == "documents2-through-chunks"
        assert getattr(request, "expand_to_section") is True

    def test_answer_prompt_b_contains_context(self) -> None:
        """Test that prompt B contains the retrieved chunk content (the bug fix verification)."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
        ]

        unique_chunk_text = "UNIQUE_MARKER_67890_CONTEXT_FOR_PROMPT_B"
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text=unique_chunk_text),
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
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text", expand=1)))

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

        assert result.success is True
        assert len(captured_prompts) == 2
        prompt_b = captured_prompts[1]
        assert unique_chunk_text in prompt_b, "Prompt B should contain the chunk context"

    def test_answer_titles_mode_expands_matched_section_to_descendant_chunks(self) -> None:
        """Title retrieval mode should include all descendant chunks of a matched section."""
        search_results = [{"doc_uid": "ifrs9", "section_id": "IFRS09_0054", "score": 0.92}]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(
                [
                    Chunk(id=1, doc_uid="ifrs9", chunk_number="3.0", chunk_id="IFRS09_3.0", containing_section_id="IFRS09_0054", text="chapter text"),
                    Chunk(id=2, doc_uid="ifrs9", chunk_number="3.1.1", chunk_id="IFRS09_3.1.1", containing_section_id="IFRS09_g3.1.1-3.1.2", text="initial recognition text"),
                ]
            )

        section_store = InMemorySectionStore()
        with section_store as store:
            store.insert_sections(
                [
                    SectionRecord(
                        section_id="IFRS09_0054",
                        doc_uid="ifrs9",
                        parent_section_id=None,
                        level=2,
                        title="Recognition and derecognition",
                        section_lineage=["Recognition and derecognition"],
                        position=1,
                    ),
                    SectionRecord(
                        section_id="IFRS09_g3.1.1-3.1.2",
                        doc_uid="ifrs9",
                        parent_section_id="IFRS09_0054",
                        level=3,
                        title="Initial recognition",
                        section_lineage=["Recognition and derecognition", "Initial recognition"],
                        position=2,
                    ),
                ]
            )
            store.add_descendant_mapping("IFRS09_0054", ["IFRS09_0054", "IFRS09_g3.1.1-3.1.2"])

        captured_prompts: list[str] = []

        def mock_send_to_llm(prompt: str) -> str:
            captured_prompts.append(prompt)
            if len(captured_prompts) == 1:
                return '{"status": "pass", "approaches": []}'
            return VALID_PROMPT_B_RESPONSE

        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=chunk_store,
            section_store=section_store,
            title_vector_store=MockVectorStore(search_results),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            title_index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
        )
        command = AnswerCommand(
            query="initial recognition",
            config=config,
            options=AnswerOptions(policy=make_retrieval_policy(mode="titles")),
        )

        with (
            unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True),
            unittest.mock.patch(
                "src.commands.answer._read_prompt_template",
            ) as mock_read_template,
        ):
            mock_read_template.side_effect = lambda path: "Context:\n{{CHUNKS}}\n\nQuestion: {{QUERY}}\n\nAnswer:"

            result = command.execute()

        assert result.success is True
        assert captured_prompts
        prompt_a = captured_prompts[0]
        assert "chapter text" in prompt_a
        assert "initial recognition text" in prompt_a


# =============================================================================
# Tests for Prompt B authority-based context filtering
# =============================================================================


class TestBuildPromptBContext:
    """Tests for the _build_prompt_b_context method that filters Prompt B context by authority."""

    def _make_command(self, chunk_store: InMemoryChunkStore) -> AnswerCommand:
        """Helper to create AnswerCommand with mock dependencies."""
        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=lambda prompt: "result",
        )
        return AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text")))

    def _make_formatted_chunks(self, chunks: list[Chunk]) -> list[str]:
        """Helper to format chunks as they would appear in the prompt."""
        formatted: list[str] = []
        for chunk in chunks:
            chunk_xml = f'<chunk id="{chunk.id}" doc_uid="{chunk.doc_uid}" paragraph="{chunk.chunk_number}" score="0.9000">\n{chunk.text}\n</chunk>'
            formatted.append(f'<Document name="{chunk.doc_uid}">\n{chunk_xml}\n</Document>')
        return formatted

    def test_filters_prompt_b_context_to_primary_authority(self) -> None:
        """Prompt B context should include only chunks listed in primary_authority."""
        mock_chunks = [
            Chunk(id=1, doc_uid="ifrs15", chunk_number="5.1", page_start="A1", page_end="A1", text="primary content - should be included"),
            Chunk(id=2, doc_uid="ifrs15", chunk_number="5.2", page_start="A2", page_end="A2", text="peripheral content - should be excluded"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {"status": "pass", "authority_classification": {"primary_authority": [{"document": "ifrs15", "references": ["5.1"], "reason": "Primary"}], "supporting_authority": [], "peripheral_authority": []}}

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "primary content" in context
        assert "peripheral content" not in context

    def test_filters_prompt_b_context_to_supporting_authority(self) -> None:
        """Prompt B context should include only chunks listed in supporting_authority."""
        mock_chunks = [
            Chunk(id=1, doc_uid="ifrs9", chunk_number="6.1", page_start="A1", page_end="A1", text="main standard content - should be excluded"),
            Chunk(id=2, doc_uid="ias21", chunk_number="8.2", page_start="B1", page_end="B1", text="supporting clarification - should be included"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {"status": "pass", "authority_classification": {"primary_authority": [], "supporting_authority": [{"document": "ias21", "references": ["8.2"], "reason": "Supporting"}], "peripheral_authority": []}}

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "supporting clarification" in context
        assert "main standard content" not in context

    def test_combines_primary_and_supporting_authority(self) -> None:
        """Prompt B context should include chunks from both primary and supporting authority."""
        mock_chunks = [
            Chunk(id=1, doc_uid="ifrs15", chunk_number="5.1", page_start="A1", page_end="A1", text="primary chunk"),
            Chunk(id=2, doc_uid="ias21", chunk_number="8.2", page_start="B1", page_end="B1", text="supporting chunk"),
            Chunk(id=3, doc_uid="ifrs9", chunk_number="3.4", page_start="C1", page_end="C1", text="peripheral chunk"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {
            "status": "pass",
            "authority_classification": {
                "primary_authority": [{"document": "ifrs15", "references": ["5.1"], "reason": "Primary"}],
                "supporting_authority": [{"document": "ias21", "references": ["8.2"], "reason": "Supporting"}],
                "peripheral_authority": [],
            },
        }

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "primary chunk" in context
        assert "supporting chunk" in context
        assert "peripheral chunk" not in context

    def test_uses_all_chunks_when_no_authority_classification(self) -> None:
        """Prompt B context should use all chunks when authority_classification is missing."""
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="first chunk"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="second chunk"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {"status": "pass"}  # No authority_classification

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "first chunk" in context
        assert "second chunk" in context

    def test_uses_all_chunks_when_no_primary_or_supporting_authority(self) -> None:
        """Prompt B context should use all chunks when primary and supporting authority are empty."""
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="peripheral chunk 1"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="peripheral chunk 2"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {"status": "pass", "authority_classification": {"primary_authority": [], "supporting_authority": [], "peripheral_authority": [{"document": "doc1", "references": ["1.1"], "reason": "Peripheral"}]}}

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "peripheral chunk 1" in context
        assert "peripheral chunk 2" in context

    def test_handles_multiple_references_per_document(self) -> None:
        """Prompt B context should handle multiple references for the same document."""
        mock_chunks = [
            Chunk(id=1, doc_uid="ifrs15", chunk_number="5.1", page_start="A1", page_end="A1", text="first primary section"),
            Chunk(id=2, doc_uid="ifrs15", chunk_number="5.2", page_start="A2", page_end="A2", text="second primary section"),
            Chunk(id=3, doc_uid="ifrs15", chunk_number="5.3", page_start="A3", page_end="A3", text="excluded section"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {"status": "pass", "authority_classification": {"primary_authority": [{"document": "ifrs15", "references": ["5.1", "5.2"], "reason": "Primary"}], "supporting_authority": [], "peripheral_authority": []}}

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "first primary section" in context
        assert "second primary section" in context
        assert "excluded section" not in context

    def test_handles_non_dict_prompt_a_json(self) -> None:
        """Prompt B context should use all chunks when Prompt A JSON is not a dict."""
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="first chunk"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="second chunk"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        # Array instead of dict
        prompt_a_json: object = []

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "first chunk" in context
        assert "second chunk" in context

    def test_handles_missing_document_in_references(self) -> None:
        """Prompt B context should skip authority items without a document field."""
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="included chunk"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {
            "status": "pass",
            "authority_classification": {
                "primary_authority": [
                    {"references": ["1.1"], "reason": "Missing document"}  # Missing document field
                ],
                "supporting_authority": [],
                "peripheral_authority": [],
            },
        }

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        # Falls back to all chunks
        assert "included chunk" in context

    def test_handles_missing_references_in_authority_item(self) -> None:
        """Prompt B context should skip authority items without references."""
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="fallback chunk"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {
            "status": "pass",
            "authority_classification": {
                "primary_authority": [
                    {"document": "doc1", "reason": "No references"}  # Missing references
                ],
                "supporting_authority": [],
                "peripheral_authority": [],
            },
        }

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        # Falls back to all chunks
        assert "fallback chunk" in context

    def test_excludes_entire_document_when_no_matching_chunks(self) -> None:
        """When no chunks from a document match authority, exclude the entire document."""
        mock_chunks = [
            Chunk(id=1, doc_uid="peripheral_doc", chunk_number="2.1", page_start="A1", page_end="A1", text="peripheral doc content"),
            Chunk(id=2, doc_uid="peripheral_doc", chunk_number="2.2", page_start="A2", page_end="A2", text="more peripheral content"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {"status": "pass", "authority_classification": {"primary_authority": [{"document": "some_other_doc", "references": ["1.1"], "reason": "Primary"}], "supporting_authority": [], "peripheral_authority": []}}

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        # Falls back to all chunks when no chunks match
        assert "peripheral doc content" in context


class TestAnswerCommandAuthorityFiltering:
    """Integration tests for full answer pipeline with authority-based Prompt B filtering."""

    def test_build_chunk_summary_logs_top_chunk_preview(self, caplog: pytest.LogCaptureFixture) -> None:
        """Chunk summary should log the top chunk section number and a short text preview per document."""
        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(
                [
                    Chunk(id=1, doc_uid="doc1", chunk_number="5.1", page_start="A1", page_end="A1", text="This is the first section text and it continues."),
                    Chunk(id=2, doc_uid="doc1", chunk_number="5.2", page_start="A2", page_end="A2", text="This is not the top chunk."),
                    Chunk(id=3, doc_uid="doc2", chunk_number="8.3", page_start="B1", page_end="B1", text="Secondary document section text for logging."),
                ]
            )

        command = AnswerCommand(
            query="test",
            config=AnswerConfig(
                vector_store=MockVectorStore([]),
                chunk_store=chunk_store,
                init_db_fn=lambda: None,
                index_path_fn=lambda: MockIndexPath(exists=True),
                send_to_llm_fn=lambda _prompt: "result",
            ),
            options=AnswerOptions(policy=make_retrieval_policy(mode="text")),
        )
        results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "doc2", "chunk_id": 3, "score": 0.8},
        ]
        doc_chunks = {
            "doc1": [
                Chunk(id=1, doc_uid="doc1", chunk_number="5.1", page_start="A1", page_end="A1", text="This is the first section text and it continues."),
                Chunk(id=2, doc_uid="doc1", chunk_number="5.2", page_start="A2", page_end="A2", text="This is not the top chunk."),
            ],
            "doc2": [
                Chunk(id=3, doc_uid="doc2", chunk_number="8.3", page_start="B1", page_end="B1", text="Secondary document section text for logging."),
            ],
        }

        with caplog.at_level(logging.INFO):
            summary = command._build_chunk_summary(results, doc_chunks)

        assert summary.startswith("Retrieved chunks:")
        assert "doc1" in caplog.text
        assert "section_number=5.1" in caplog.text
        assert "score=0.9000" in caplog.text
        assert "section_text_preview='This is the first section text'" in caplog.text
        assert "section_number=8.3" in caplog.text
        assert "score=0.8000" in caplog.text
        assert "section_text_preview='Secondary document section tex'" in caplog.text

    def test_answer_prompt_b_context_filtered_by_authority(self) -> None:
        """End-to-end test: Prompt B should contain only primary/supporting chunks."""
        search_results = [
            {"doc_uid": "ifrs15", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "ifrs15", "chunk_id": 2, "score": 0.85},
            {"doc_uid": "ias21", "chunk_id": 3, "score": 0.8},
        ]

        mock_chunks = [
            Chunk(id=1, doc_uid="ifrs15", chunk_number="5.1", page_start="A1", page_end="A1", text="PRIMARY_CONTENT_IFRS15"),
            Chunk(id=2, doc_uid="ifrs15", chunk_number="5.2", page_start="A2", page_end="A2", text="PERIPHERAL_CONTENT_IFRS15"),
            Chunk(id=3, doc_uid="ias21", chunk_number="8.2", page_start="B1", page_end="B1", text="SUPPORTING_CONTENT_IAS21"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        captured_prompts: list[str] = []

        def mock_send_to_llm(prompt: str) -> str:
            captured_prompts.append(prompt)
            if len(captured_prompts) == 1:
                # Prompt A response: ifrs15 5.1 is primary, ias21 8.2 is supporting
                return json.dumps(
                    {
                        "status": "pass",
                        "authority_classification": {
                            "primary_authority": [{"document": "ifrs15", "references": ["5.1"], "reason": "Governs the issue"}],
                            "supporting_authority": [{"document": "ias21", "references": ["8.2"], "reason": "Clarifies the treatment"}],
                            "peripheral_authority": [{"document": "ifrs15", "references": ["5.2"], "reason": "Not directly relevant"}],
                        },
                    }
                )
            return VALID_PROMPT_B_RESPONSE

        config = AnswerConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
        )
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text", expand=1)))

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

        assert result.success is True
        assert len(captured_prompts) == 2
        prompt_b = captured_prompts[1]

        # Prompt B should contain primary and supporting authority chunks
        assert "PRIMARY_CONTENT_IFRS15" in prompt_b
        assert "SUPPORTING_CONTENT_IAS21" in prompt_b

        # Prompt B should NOT contain peripheral authority chunk
        assert "PERIPHERAL_CONTENT_IFRS15" not in prompt_b
