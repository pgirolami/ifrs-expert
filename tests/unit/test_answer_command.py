"""Tests for answer command."""

from __future__ import annotations

import json
import logging
import unittest.mock
from pathlib import Path
from typing import cast

from src.case_analysis.models import ApproachIdentificationPassOutput, ApplicabilityAnalysisPassOutput
from src.commands.answer import AnswerCommand, AnswerConfig, AnswerOptions
from src.interfaces import DocumentSearchResult, SearchDocumentVectorStoreProtocol, SearchResult, SearchVectorStoreProtocol
from src.models.chunk import Chunk
from src.models.section import SectionRecord
from tests.fakes import FakeAnswerGenerator, InMemoryChunkStore, InMemorySectionStore
from tests.policy import make_retrieval_policy

VALID_APPROACH_IDENTIFICATION_RESPONSE = """{
  "status": "pass",
  "primary_accounting_issue": "Test accounting issue",
  "authority_resolution": {
    "candidate_governing_documents": ["doc1"],
    "selected_primary_document": "doc1",
    "selection_reason": "Test selection reason",
    "discarded_due_to_overlap": [],
    "residual_uncertainty": "Low uncertainty for test"
  },
  "authority_classification": {
    "primary_authority": [],
    "supporting_authority": [],
    "peripheral_authority": []
  },
  "treatment_families": [],
  "approaches": [
    {
      "id": "approach_1",
      "label": "Fair value hedge",
      "normalized_label": "fair_value_hedge",
      "rationale_for_inclusion": "Test rationale"
    }
  ]
}"""

VALID_APPLICABILITY_ANALYSIS_RESPONSE = """{
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
          "document": "doc1",
          "section": "6.3.1",
          "excerpt": "A hedged item can be a recognised asset or liability"
        }
      ]
    }
  ]
}"""



VALID_APPROACH_IDENTIFICATION_OUTPUT = ApproachIdentificationPassOutput.model_validate_json(VALID_APPROACH_IDENTIFICATION_RESPONSE)
VALID_APPLICABILITY_ANALYSIS_OUTPUT = ApplicabilityAnalysisPassOutput.model_validate_json(VALID_APPLICABILITY_ANALYSIS_RESPONSE)


def make_answer_generator() -> FakeAnswerGenerator:
    return FakeAnswerGenerator(approach_identification_output=VALID_APPROACH_IDENTIFICATION_OUTPUT, applicability_analysis_output=VALID_APPLICABILITY_ANALYSIS_OUTPUT)

class MockVectorStore(SearchVectorStoreProtocol):
    """Minimal mock for VectorStore context manager."""

    def __init__(self, search_results: list[dict[str, str | int | float]]) -> None:
        self._search_results = cast("list[SearchResult]", search_results)

    def __enter__(self) -> MockVectorStore:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[SearchResult]:
        return self._search_results


class MockDocumentVectorStore(SearchDocumentVectorStoreProtocol):
    """Minimal mock for document vector store context manager."""

    def __init__(self, search_results: list[dict[str, str | float]]) -> None:
        self._search_results = cast("list[DocumentSearchResult]", search_results)

    def __enter__(self) -> MockDocumentVectorStore:
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
            answer_generator=make_answer_generator(),
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
            answer_generator=make_answer_generator(),
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

        config = AnswerConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            answer_generator=make_answer_generator(),
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
        assert result.approach_identification_text is not None
        assert json.loads(result.approach_identification_raw_response) == json.loads(VALID_APPROACH_IDENTIFICATION_RESPONSE)
        assert result.approach_identification_json is not None
        assert result.applicability_analysis_text is not None
        assert json.loads(result.applicability_analysis_raw_response) == json.loads(VALID_APPLICABILITY_ANALYSIS_RESPONSE)
        assert result.applicability_analysis_json is not None
        assert result.applicability_analysis_memo_markdown is not None
        assert result.retrieved_doc_uids == ["doc1"]

    def test_answer_no_results(self) -> None:
        """Test answer command with no matching results."""
        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=InMemoryChunkStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            answer_generator=make_answer_generator(),
        )
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text", expand=1)))

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

        assert result.success is False
        assert result.error == "Error: No chunks retrieved"

    def test_answer_min_score_filter(self) -> None:
        """Test answer command respects min_score filter."""
        search_results = [
            {"doc_uid": "doc1", "chunk_id": 1, "section_id": "1.1", "score": 0.9},
            {"doc_uid": "doc1", "chunk_id": 2, "section_id": "1.2", "score": 0.3},
        ]

        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="high relevance content"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="low relevance content"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)
        answer_generator = make_answer_generator()

        config = AnswerConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            answer_generator=answer_generator,
        )
        command = AnswerCommand(
            query="initial recognition",
            config=config,
            options=AnswerOptions(policy=make_retrieval_policy(mode="text")),
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
        assert answer_generator.approach_identification_prompts
        approach_identification = answer_generator.approach_identification_prompts[0]
        assert "high relevance content" in approach_identification
        assert "low relevance content" not in approach_identification


# =============================================================================
# Tests for Applicability analysis authority-based context filtering
# =============================================================================
