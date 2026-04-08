"""Tests for answer command."""

from __future__ import annotations

import logging
import unittest.mock
from typing import cast

from src.commands.answer import AnswerCommand, AnswerConfig, AnswerOptions
from src.interfaces import DocumentSearchResult, SearchDocumentVectorStoreProtocol, SearchResult, SearchVectorStoreProtocol
from src.models.chunk import Chunk
from src.models.section import SectionRecord
from src.retrieval.models import RetrievalResult
from tests.fakes import InMemoryChunkStore, InMemorySectionStore

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

    def test_answer_no_index(self, caplog) -> None:
        """Test answer command logs and fails clearly when no index exists."""
        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=False),
            send_to_llm_fn=lambda prompt: "result",
        )
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(k=5))

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
        command = AnswerCommand(query="What is the scope?", config=config, options=AnswerOptions(k=5))

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
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(k=5, min_score=0.5, expand=0))

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
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(k=5, full_doc_threshold=10))

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
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(k=5))

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
            options=AnswerOptions(k=5, content_min_score=0.5, expand_to_section=True, expand=0),
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
            options=AnswerOptions(
                retrieval_mode="documents",
                k=5,
                d=1,
                doc_min_score=0.5,
                content_min_score=0.5,
                expand=0,
            ),
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
            options=AnswerOptions(
                retrieval_mode="documents",
                k=3,
                d=9,
                doc_min_score=0.2,
                ifrs_d=7,
                ias_d=6,
                ifric_d=4,
                sic_d=3,
                ps_d=2,
                ifrs_min_score=0.61,
                ias_min_score=0.54,
                ifric_min_score=0.50,
                sic_min_score=0.49,
                ps_min_score=0.48,
                content_min_score=0.1,
                expand_to_section=True,
                expand=1,
                full_doc_threshold=2000,
            ),
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
        assert getattr(request, "doc_min_score") == 0.2
        assert getattr(request, "document_d_by_type") == {
            "IFRS": 7,
            "IAS": 6,
            "IFRIC": 4,
            "SIC": 3,
            "PS": 2,
        }
        assert getattr(request, "document_min_score_by_type") == {
            "IFRS": 0.61,
            "IAS": 0.54,
            "IFRIC": 0.50,
            "SIC": 0.49,
            "PS": 0.48,
        }
        assert getattr(request, "content_min_score") == 0.1
        assert getattr(request, "expand_to_section") is True
        assert getattr(request, "expand") == 1
        assert getattr(request, "full_doc_threshold") == 2000

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
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(k=5))

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
                        embedding_text="Recognition and derecognition",
                        position=1,
                    ),
                    SectionRecord(
                        section_id="IFRS09_g3.1.1-3.1.2",
                        doc_uid="ifrs9",
                        parent_section_id="IFRS09_0054",
                        level=3,
                        title="Initial recognition",
                        section_lineage=["Recognition and derecognition", "Initial recognition"],
                        embedding_text="Initial recognition",
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
            options=AnswerOptions(k=5, retrieval_mode="titles"),
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
