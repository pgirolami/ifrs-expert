"""Tests for case-analysis workflow stages."""

from __future__ import annotations

from typing import cast

from src.case_analysis.models import RetrievedSourcePackage, SourceChunkResult, ValidationFailure, ValidatedQuestion
from src.case_analysis.stages import RetrieveSourceMaterialStage, ValidateQuestionStage
from src.interfaces import SearchResult
from src.models.chunk import Chunk
from src.retrieval.models import RetrievalRequest, RetrievalResult
from src.retrieval.pipeline import RetrievalPipelineConfig
from tests.fakes import InMemoryChunkStore
from tests.policy import make_retrieval_policy
from tests.unit.test_answer_command import MockIndexPath, MockVectorStore


def test_validate_question_stage_returns_trimmed_question() -> None:
    stage = ValidateQuestionStage()

    result = stage.execute(query="  What is the scope?  ", policy=make_retrieval_policy(mode="text"))

    assert isinstance(result, ValidatedQuestion)
    assert result.question == "What is the scope?"


def test_validate_question_stage_rejects_empty_question() -> None:
    stage = ValidateQuestionStage()

    result = stage.execute(query="   ", policy=make_retrieval_policy(mode="text"))

    assert isinstance(result, ValidationFailure)
    assert result.error_stage == "validation"
    assert result.reason == "empty_question"
    assert "Query cannot be empty" in result.message


def test_retrieve_source_material_stage_returns_typed_package() -> None:
    captured_query: list[str] = []
    chunk = Chunk(id=1, doc_uid="doc1", chunk_number="1.1", text="Relevant text")
    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks([chunk])

    def fake_execute_retrieval(request: RetrievalRequest, config: RetrievalPipelineConfig) -> tuple[str | None, RetrievalResult | None]:
        del config
        captured_query.append(request.query)
        result = RetrievalResult(
            policy_name="text",
            document_routing_source="all_documents",
            document_routing_post_processing="none",
            chunk_retrieval_mode="chunk_similarity",
            document_hits=[],
            chunk_results=cast(list[SearchResult], [{"doc_uid": "doc1", "chunk_id": 1, "score": 0.9}]),
            doc_chunks={"doc1": [chunk]},
        )
        return None, result

    pipeline_config = RetrievalPipelineConfig(
        vector_store=MockVectorStore([]),
        chunk_store=chunk_store,
        init_db_fn=lambda: None,
        index_path_fn=lambda: MockIndexPath(exists=True),
    )
    stage = RetrieveSourceMaterialStage(pipeline_config=pipeline_config, execute_retrieval_fn=fake_execute_retrieval)

    result = stage.execute(question="What is the scope?", policy=make_retrieval_policy(mode="text"))

    assert isinstance(result, RetrievedSourcePackage)
    assert captured_query == ["What is the scope?"]
    assert result.policy_name == "text"
    assert result.retrieved_doc_uids == ["doc1"]
    assert result.chunk_results == [SourceChunkResult(doc_uid="doc1", chunk_id=1, score=0.9)]
    assert result.to_search_results() == [{"doc_uid": "doc1", "chunk_id": 1, "score": 0.9}]


def test_retrieve_source_material_stage_returns_failure_on_retrieval_error() -> None:
    def fake_execute_retrieval(request: RetrievalRequest, config: RetrievalPipelineConfig) -> tuple[str | None, RetrievalResult | None]:
        del request, config
        return "Error: No chunks retrieved", None

    pipeline_config = RetrievalPipelineConfig(
        vector_store=MockVectorStore([]),
        chunk_store=InMemoryChunkStore(),
        init_db_fn=lambda: None,
        index_path_fn=lambda: MockIndexPath(exists=True),
    )
    stage = RetrieveSourceMaterialStage(pipeline_config=pipeline_config, execute_retrieval_fn=fake_execute_retrieval)

    result = stage.execute(question="What is the scope?", policy=make_retrieval_policy(mode="text"))

    assert isinstance(result, ValidationFailure)
    assert result.error_stage == "retrieval"
    assert result.message == "Error: No chunks retrieved"
