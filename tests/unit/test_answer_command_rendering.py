"""Rendering and authority-filtering tests for answer command."""

from __future__ import annotations

import logging

import pytest

from src.case_analysis.engine import _build_applicability_analysis_context, _build_chunk_summary
from src.case_analysis.models import ApproachIdentificationOutput
from src.interfaces import SearchResult
from tests.unit.test_answer_command import *  # noqa: F403


def _make_approach_identification_output(authority_classification: dict[str, object]) -> ApproachIdentificationOutput:
    return ApproachIdentificationOutput.model_validate(
        {
            "status": "pass",
            "primary_accounting_issue": "Revenue recognition under IFRS 15",
            "authority_resolution": {
                "candidate_governing_documents": ["ifrs15"],
                "selected_primary_document": "ifrs15",
                "selection_reason": "Reason",
                "discarded_due_to_overlap": [],
                "residual_uncertainty": "Low",
            },
            "authority_classification": authority_classification,
            "treatment_families": [],
            "approaches": [],
        }
    )


class TestBuildApplicabilityAnalysisContext:
    """Tests for the _build_applicability_analysis_context method."""

    def _make_command(self, chunk_store: InMemoryChunkStore) -> AnswerCommand:
        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            answer_generator=make_answer_generator(),
        )
        return AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text")))

    def _make_formatted_chunks(self, chunks: list[Chunk]) -> list[str]:
        formatted: list[str] = []
        for chunk in chunks:
            chunk_xml = f'<chunk id="{chunk.id}" doc_uid="{chunk.doc_uid}" paragraph="{chunk.chunk_number}" score="0.9000">\n{chunk.text}\n</chunk>'
            formatted.append(f'<Document name="{chunk.doc_uid}">\n{chunk_xml}\n</Document>')
        return formatted

    def test_filters_applicability_analysis_context_to_primary_authority(self) -> None:
        mock_chunks = [
            Chunk(id=1, doc_uid="ifrs15", chunk_number="5.1", page_start="A1", page_end="A1", text="primary content - should be included"),
            Chunk(id=2, doc_uid="ifrs15", chunk_number="5.2", page_start="A2", page_end="A2", text="peripheral content - should be excluded"),
        ]
        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)
        approach_identification_output = _make_approach_identification_output(
            {
                "primary_authority": [{"document": "ifrs15", "references": ["5.1"], "reason": "Primary"}],
                "supporting_authority": [],
                "peripheral_authority": [],
            }
        )

        context = _build_applicability_analysis_context(formatted_chunks, approach_identification_output)

        assert "primary content" in context
        assert "peripheral content" not in context

    def test_filters_applicability_analysis_context_to_supporting_authority(self) -> None:
        mock_chunks = [
            Chunk(id=1, doc_uid="ifrs9", chunk_number="6.1", page_start="A1", page_end="A1", text="main standard content - should be excluded"),
            Chunk(id=2, doc_uid="ias21", chunk_number="8.2", page_start="B1", page_end="B1", text="supporting clarification - should be included"),
        ]
        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)
        approach_identification_output = _make_approach_identification_output(
            {
                "primary_authority": [],
                "supporting_authority": [{"document": "ias21", "references": ["8.2"], "reason": "Supporting"}],
                "peripheral_authority": [],
            }
        )

        context = _build_applicability_analysis_context(formatted_chunks, approach_identification_output)

        assert "supporting clarification" in context
        assert "main standard content" not in context

    def test_uses_all_chunks_when_no_primary_or_supporting_authority(self) -> None:
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="peripheral chunk 1"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="peripheral chunk 2"),
        ]
        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)
        approach_identification_output = _make_approach_identification_output(
            {
                "primary_authority": [],
                "supporting_authority": [],
                "peripheral_authority": [{"document": "doc1", "references": ["1.1"], "reason": "Peripheral"}],
            }
        )

        context = _build_applicability_analysis_context(formatted_chunks, approach_identification_output)

        assert "peripheral chunk 1" in context
        assert "peripheral chunk 2" in context

    def test_handles_multiple_references_per_document(self) -> None:
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
        approach_identification_output = _make_approach_identification_output(
            {
                "primary_authority": [{"document": "ifrs15", "references": ["5.1", "5.2"], "reason": "Primary"}],
                "supporting_authority": [],
                "peripheral_authority": [],
            }
        )

        context = _build_applicability_analysis_context(formatted_chunks, approach_identification_output)

        assert "first primary section" in context
        assert "second primary section" in context
        assert "excluded section" not in context


class TestAnswerCommandAuthorityFiltering:
    """Integration tests for full answer pipeline with authority-based filtering."""

    def test_build_chunk_summary_logs_top_chunk_preview(self, caplog: pytest.LogCaptureFixture) -> None:
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
                answer_generator=make_answer_generator(),
            ),
            options=AnswerOptions(policy=make_retrieval_policy(mode="text")),
        )
        results: list[SearchResult] = [
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
            summary = _build_chunk_summary(results, doc_chunks)

        assert summary.startswith("Retrieved chunks:")
        assert "doc1" in caplog.text
        assert "section_number=5.1" in caplog.text
        assert "score=0.9000" in caplog.text
        assert "section_text_preview='This is the first section text'" in caplog.text
        assert "section_number=8.3" in caplog.text
        assert "score=0.8000" in caplog.text
        assert "section_text_preview='Secondary document section tex'" in caplog.text
