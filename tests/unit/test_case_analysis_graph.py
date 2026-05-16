"""Tests for the deterministic case-analysis LangGraph runner."""

from __future__ import annotations

from typing import cast

from src.case_analysis.graph import CaseAnalysisGraphRunner
from src.case_analysis.models import RetrievedSourcePackage, ValidationFailure
from src.interfaces import SearchResult
from src.models.answer_command_result import AnswerCommandResult
from src.models.chunk import Chunk
from src.retrieval.models import RetrievalRequest, RetrievalResult
from src.retrieval.pipeline import RetrievalPipelineConfig
from tests.fakes import InMemoryChunkStore
from tests.policy import make_retrieval_policy
from tests.unit.test_answer_command import MockIndexPath, MockVectorStore


def _make_pipeline_config(chunk_store: InMemoryChunkStore) -> RetrievalPipelineConfig:
    """Build a minimal retrieval pipeline config for graph tests."""
    return RetrievalPipelineConfig(
        vector_store=MockVectorStore([]),
        chunk_store=chunk_store,
        init_db_fn=lambda: None,
        index_path_fn=lambda: MockIndexPath(exists=True),
    )


def test_graph_runner_stops_before_retrieval_when_validation_fails() -> None:
    """The graph should route validation failures directly to an AnswerCommandResult failure."""
    retrieval_calls = 0

    def fake_execute_retrieval(*, request: RetrievalRequest, config: RetrievalPipelineConfig) -> tuple[str | None, RetrievalResult | None]:
        nonlocal retrieval_calls
        del request, config
        retrieval_calls += 1
        return "should not be called", None

    runner = CaseAnalysisGraphRunner(
        policy=make_retrieval_policy(mode="text"),
        pipeline_config=_make_pipeline_config(InMemoryChunkStore()),
        execute_retrieval_fn=fake_execute_retrieval,
        build_answer_result_fn=lambda package: AnswerCommandResult(query="unused"),
        process_prompts_fn=lambda result, package: result,
    )

    result = runner.run("   ")

    assert result.success is False
    assert result.error_stage == "validation"
    assert result.error == "Error: Query cannot be empty"
    assert retrieval_calls == 0


def test_graph_runner_retrieves_sources_then_processes_prompts() -> None:
    """The graph should run validation, retrieval, and prompt processing on the happy path."""
    chunk = Chunk(id=1, doc_uid="doc1", chunk_number="1.1", text="Relevant source text")
    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks([chunk])

    processed_packages: list[RetrievedSourcePackage] = []

    def fake_execute_retrieval(*, request: RetrievalRequest, config: RetrievalPipelineConfig) -> tuple[str | None, RetrievalResult | None]:
        del config
        retrieval_result = RetrievalResult(
            policy_name=request.policy_name,
            document_routing_source=request.document_routing_source,
            document_routing_post_processing=request.document_routing_post_processing,
            chunk_retrieval_mode=request.chunk_retrieval_mode,
            document_hits=[],
            chunk_results=cast(list[SearchResult], [{"doc_uid": "doc1", "chunk_id": 1, "score": 0.9}]),
            doc_chunks={"doc1": [chunk]},
        )
        return None, retrieval_result

    def build_answer_result(package: RetrievedSourcePackage) -> AnswerCommandResult:
        return AnswerCommandResult(query="What is scope?", retrieved_doc_uids=package.retrieved_doc_uids)

    def process_prompts(result: AnswerCommandResult, package: RetrievedSourcePackage) -> AnswerCommandResult:
        processed_packages.append(package)
        result.mark_success()
        return result

    runner = CaseAnalysisGraphRunner(
        policy=make_retrieval_policy(mode="text"),
        pipeline_config=_make_pipeline_config(chunk_store),
        execute_retrieval_fn=fake_execute_retrieval,
        build_answer_result_fn=build_answer_result,
        process_prompts_fn=process_prompts,
    )

    state = runner.run_with_state(" What is scope? ")
    result = state.answer_result

    assert state.current_stage == "process_prompts"
    assert state.stage_trace == ("validate_question", "prepare_retrieval_request", "retrieve_source_material", "process_prompts")
    assert state.retrieval_request is not None
    assert state.retrieval_result is not None
    assert result is not None
    assert result.success is True
    assert result.error is None
    assert result.retrieved_doc_uids == ["doc1"]
    assert len(processed_packages) == 1
    assert processed_packages[0].retrieved_doc_uids == ["doc1"]


def test_graph_runner_returns_retrieval_failure() -> None:
    """Retrieval failures should become AnswerCommandResult retrieval failures."""

    def fake_execute_retrieval(*, request: RetrievalRequest, config: RetrievalPipelineConfig) -> tuple[str | None, RetrievalResult | None]:
        del request, config
        return "Error: No chunks retrieved", None

    runner = CaseAnalysisGraphRunner(
        policy=make_retrieval_policy(mode="text"),
        pipeline_config=_make_pipeline_config(InMemoryChunkStore()),
        execute_retrieval_fn=fake_execute_retrieval,
        build_answer_result_fn=lambda package: AnswerCommandResult(query="unused"),
        process_prompts_fn=lambda result, package: result,
    )

    result = runner.run("What is scope?")

    assert result.success is False
    assert result.error_stage == "retrieval"
    assert result.error == "Error: No chunks retrieved"
