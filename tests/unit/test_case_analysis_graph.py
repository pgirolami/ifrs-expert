"""Tests for the deterministic case-analysis LangGraph runner."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import cast

from src.case_analysis.graph import CaseAnalysisGraphRunner
from src.case_analysis.models import ApproachApplicability, ApplicabilityAnalysisOutput, ApproachIdentificationOutput, Recommendation, RetrievedSourcePackage, ValidationFailure
from src.case_analysis.workflow import AnswerWorkflowProcessor
from src.interfaces import SearchResult
from src.models.answer_command_result import AnswerCommandResult
from src.models.chunk import Chunk
from src.policy import RetrievalPolicy
from src.retrieval.models import RetrievalRequest, RetrievalResult
from src.retrieval.pipeline import RetrievalPipelineConfig
from tests.fakes import InMemoryChunkStore
from tests.policy import make_retrieval_policy
from tests.unit.test_answer_command import MockIndexPath, MockVectorStore


@dataclass
class FakeAnswerGenerator:
    """Typed answer generator stub for graph tests."""

    approach_output: ApproachIdentificationOutput | ValidationFailure
    applicability_output: ApplicabilityAnalysisOutput | ValidationFailure
    applicability_calls: int = 0

    def generate_approach_identification(self, prompt_text: str) -> ApproachIdentificationOutput:
        del prompt_text
        if isinstance(self.approach_output, ValidationFailure):
            raise RuntimeError("approach output configured as failure")
        return self.approach_output

    def generate_applicability_analysis(self, prompt_text: str) -> ApplicabilityAnalysisOutput:
        del prompt_text
        self.applicability_calls += 1
        if isinstance(self.applicability_output, ValidationFailure):
            raise RuntimeError("applicability output configured as failure")
        return self.applicability_output


def _make_pipeline_config(chunk_store: InMemoryChunkStore) -> RetrievalPipelineConfig:
    """Build a minimal retrieval pipeline config for graph tests."""
    return RetrievalPipelineConfig(
        vector_store=MockVectorStore([]),
        chunk_store=chunk_store,
        init_db_fn=lambda: None,
        index_path_fn=lambda: MockIndexPath(exists=True),
    )


def _make_workflow_processor(
    policy: RetrievalPolicy,
    approach_output: ApproachIdentificationOutput | ValidationFailure,
    applicability_output: ApplicabilityAnalysisOutput | ValidationFailure,
) -> tuple[AnswerWorkflowProcessor, FakeAnswerGenerator]:
    fake_generator = FakeAnswerGenerator(approach_output=approach_output, applicability_output=applicability_output)
    processor = AnswerWorkflowProcessor(
        query="What is scope?",
        policy=policy,
        read_prompt_template_fn=lambda path: f"You are an IFRS expert\n{path.name}",
        approach_identification_path=Path("prompt_A.txt"),
        applicability_analysis_path=Path("prompt_B.txt"),
        answer_generator=fake_generator,
    )
    return processor, fake_generator


def _make_applicability_output() -> ApplicabilityAnalysisOutput:
    return ApplicabilityAnalysisOutput(
        status="pass",
        recommendation=Recommendation(answer="oui", justification="ok"),
        approaches=[
            ApproachApplicability(
                id="A1",
                normalized_label="a1",
                label_fr="Approche 1",
                applicability="oui",
                reasoning_fr="raison",
                conditions_fr=[],
                practical_implication_fr="implication",
                references=[],
            ),
        ],
    )


def test_graph_runner_stops_before_retrieval_when_validation_fails() -> None:
    """The graph should route validation failures directly to an AnswerCommandResult failure."""
    retrieval_calls = 0

    def fake_execute_retrieval(*, request: RetrievalRequest, config: RetrievalPipelineConfig) -> tuple[str | None, RetrievalResult | None]:
        nonlocal retrieval_calls
        del request, config
        retrieval_calls += 1
        return "should not be called", None

    workflow_processor, _ = _make_workflow_processor(
        make_retrieval_policy(mode="text"),
        approach_output=ApproachIdentificationOutput(status="pass"),
        applicability_output=_make_applicability_output(),
    )
    runner = CaseAnalysisGraphRunner(
        policy=make_retrieval_policy(mode="text"),
        pipeline_config=_make_pipeline_config(InMemoryChunkStore()),
        execute_retrieval_fn=fake_execute_retrieval,
        workflow_processor=workflow_processor,
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

    workflow_processor, _ = _make_workflow_processor(
        make_retrieval_policy(mode="text"),
        approach_output=ApproachIdentificationOutput(status="pass"),
        applicability_output=_make_applicability_output(),
    )
    runner = CaseAnalysisGraphRunner(
        policy=make_retrieval_policy(mode="text"),
        pipeline_config=_make_pipeline_config(chunk_store),
        execute_retrieval_fn=fake_execute_retrieval,
        workflow_processor=workflow_processor,
    )

    state = runner.run_with_state(" What is scope? ")
    result = state.answer_result

    assert state.current_stage == "finalize_answer"
    assert state.stage_trace == (
        "validate_question",
        "prepare_retrieval_request",
        "retrieve_source_material",
        "run_case_evidence_agent",
        "prepare_prompt_materials",
        "run_approach_identification",
        "prepare_applicability_context",
        "run_applicability_analysis",
        "finalize_answer",
    )
    assert state.retrieval_request is not None
    assert state.retrieval_result is not None
    assert state.case_evidence_result is not None
    assert state.case_evidence_result.status == "complete"
    assert len(state.case_evidence_tool_calls) == 1
    assert state.approach_identification_output is not None
    assert state.applicability_analysis_output is not None
    assert "doc1" in state.applicability_analysis_context
    assert "Relevant source text" in state.applicability_analysis_context
    assert result is not None
    assert result.success is True
    assert result.error is None
    assert result.retrieved_doc_uids == ["doc1"]


def test_graph_runner_routes_clarification_before_applicability() -> None:
    """A clarification response should stop the graph before applicability analysis."""
    chunk = Chunk(id=1, doc_uid="doc1", chunk_number="1.1", text="Relevant source text")
    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks([chunk])

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

    workflow_processor, fake_generator = _make_workflow_processor(
        make_retrieval_policy(mode="text"),
        approach_output=ApproachIdentificationOutput(status="needs_clarification", questions=["Which standard applies?"]),
        applicability_output=_make_applicability_output(),
    )
    runner = CaseAnalysisGraphRunner(
        policy=make_retrieval_policy(mode="text"),
        pipeline_config=_make_pipeline_config(chunk_store),
        execute_retrieval_fn=fake_execute_retrieval,
        workflow_processor=workflow_processor,
    )

    state = runner.run_with_state(" What is scope? ")
    result = state.answer_result

    assert state.current_stage == "build_clarification_failure"
    assert state.stage_trace == (
        "validate_question",
        "prepare_retrieval_request",
        "retrieve_source_material",
        "run_case_evidence_agent",
        "prepare_prompt_materials",
        "run_approach_identification",
        "build_clarification_failure",
    )
    assert state.clarification_stage == "approach_identification"
    assert state.clarification_questions == ("Which standard applies?",)
    assert fake_generator.applicability_calls == 0
    assert result is not None
    assert result.success is False
    assert result.error_stage == "clarification"
    assert result.error == "Error: Clarification required at approach_identification: Which standard applies?"


def test_graph_runner_returns_retrieval_failure() -> None:
    """Retrieval failures should become AnswerCommandResult retrieval failures."""

    def fake_execute_retrieval(*, request: RetrievalRequest, config: RetrievalPipelineConfig) -> tuple[str | None, RetrievalResult | None]:
        del request, config
        return "Error: No chunks retrieved", None

    workflow_processor, _ = _make_workflow_processor(
        make_retrieval_policy(mode="text"),
        approach_output=ApproachIdentificationOutput(status="pass"),
        applicability_output=_make_applicability_output(),
    )
    runner = CaseAnalysisGraphRunner(
        policy=make_retrieval_policy(mode="text"),
        pipeline_config=_make_pipeline_config(InMemoryChunkStore()),
        execute_retrieval_fn=fake_execute_retrieval,
        workflow_processor=workflow_processor,
    )

    result = runner.run("What is scope?")

    assert result.success is False
    assert result.error_stage == "retrieval"
    assert result.error == "Error: No chunks retrieved"
