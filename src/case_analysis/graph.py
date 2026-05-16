"""LangGraph orchestration for deterministic case-analysis workflows."""

from __future__ import annotations

import importlib
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, cast

from langgraph.graph import END, START, StateGraph

from src.case_analysis.models import RetrievedSourcePackage, ValidatedQuestion, ValidationFailure
from src.case_analysis.stages import ExecuteRetrievalFn, ValidateQuestionStage
from src.models.answer_command_result import AnswerCommandResult
from src.retrieval.request_builder import build_retrieval_request

retrieval_models = importlib.import_module("src.retrieval.models")

if TYPE_CHECKING:
    from collections.abc import Callable

    from langgraph.graph.state import CompiledStateGraph

    from src.policy import RetrievalPolicy
    from src.retrieval.pipeline import RetrievalPipelineConfig


@dataclass
class CaseAnalysisState:
    """State passed between deterministic case-analysis graph nodes."""

    question: str = ""
    current_stage: str | None = None
    stage_trace: tuple[str, ...] = ()
    validated_question: ValidatedQuestion | None = None
    retrieval_request: retrieval_models.RetrievalRequest | None = None
    retrieval_result: retrieval_models.RetrievalResult | None = None
    retrieved_source_package: RetrievedSourcePackage | None = None
    answer_result: AnswerCommandResult | None = None
    failure: ValidationFailure | None = None


@dataclass(frozen=True)
class CaseAnalysisGraphRunner:
    """Run the deterministic answer workflow through LangGraph."""

    policy: RetrievalPolicy
    pipeline_config: RetrievalPipelineConfig
    execute_retrieval_fn: ExecuteRetrievalFn
    build_answer_result_fn: Callable[[RetrievedSourcePackage], AnswerCommandResult]
    process_prompts_fn: Callable[[AnswerCommandResult, RetrievedSourcePackage], AnswerCommandResult]
    _graph: CompiledStateGraph = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        """Compile the workflow graph once for this runner instance."""
        object.__setattr__(self, "_graph", self._build_graph())

    def run(self, question: str) -> AnswerCommandResult:
        """Run the graph and return an answer command result."""
        final_state = self.run_with_state(question)
        if final_state.answer_result is not None:
            return final_state.answer_result

        if final_state.failure is not None:
            return AnswerCommandResult.failure(query=question, error=final_state.failure.message, error_stage=final_state.failure.error_stage)

        return AnswerCommandResult.failure(
            query=question,
            error="Error: Case analysis graph ended without a result",
            error_stage="workflow",
        )

    def run_with_state(self, question: str) -> CaseAnalysisState:
        """Run the graph and return the final graph state snapshot."""
        final_state = cast("dict[str, object]", self._graph.invoke({"question": question}))
        return CaseAnalysisState(
            question=question,
            current_stage=cast("str | None", final_state.get("current_stage")),
            stage_trace=cast("tuple[str, ...]", final_state.get("stage_trace", ())),
            validated_question=cast("ValidatedQuestion | None", final_state.get("validated_question")),
            retrieval_request=cast("retrieval_models.RetrievalRequest | None", final_state.get("retrieval_request")),
            retrieval_result=cast("retrieval_models.RetrievalResult | None", final_state.get("retrieval_result")),
            retrieved_source_package=cast("RetrievedSourcePackage | None", final_state.get("retrieved_source_package")),
            answer_result=cast("AnswerCommandResult | None", final_state.get("answer_result")),
            failure=cast("ValidationFailure | None", final_state.get("failure")),
        )

    def _advance_stage(self, state: CaseAnalysisState, stage_name: str) -> dict[str, object]:
        """Record stage progression in the graph snapshot."""
        return {
            "current_stage": stage_name,
            "stage_trace": (*state.stage_trace, stage_name),
        }

    def _build_graph(self) -> CompiledStateGraph:
        """Build and compile the deterministic LangGraph workflow."""
        builder = StateGraph(CaseAnalysisState)
        builder.add_node("validate_question", self._validate_question_node)
        builder.add_node("retrieve_source_material", self._retrieve_source_material_node)
        builder.add_node("process_prompts", self._process_prompts_node)
        builder.add_node("build_failure", self._build_failure_node)

        builder.add_edge(START, "validate_question")
        builder.add_conditional_edges(
            "validate_question",
            self._route_after_failure_capable_node,
            {"continue": "retrieve_source_material", "fail": "build_failure"},
        )
        builder.add_conditional_edges(
            "retrieve_source_material",
            self._route_after_failure_capable_node,
            {"continue": "process_prompts", "fail": "build_failure"},
        )
        builder.add_edge("process_prompts", END)
        builder.add_edge("build_failure", END)
        return builder.compile()

    def _validate_question_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Validate the incoming question."""
        validation_result = ValidateQuestionStage().execute(query=state.question, policy=self.policy)
        if isinstance(validation_result, ValidationFailure):
            return {
                **self._advance_stage(state, "validate_question"),
                "failure": validation_result,
            }
        return {
            **self._advance_stage(state, "validate_question"),
            "validated_question": validation_result,
        }

    def _route_after_failure_capable_node(self, state: CaseAnalysisState) -> str:
        """Continue unless the previous node recorded a failure."""
        if state.failure is not None:
            return "fail"
        return "continue"

    def _retrieve_source_material_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Retrieve source material through the existing retrieval pipeline."""
        if state.validated_question is None:
            return {
                **self._advance_stage(state, "retrieve_source_material"),
                "failure": ValidationFailure(error_stage="validation", reason="missing_validated_question", message="Error: Missing validated question"),
            }
        retrieval_request = build_retrieval_request(
            query=state.validated_question.question,
            policy=self.policy,
            chunk_min_score=self.policy.titles.min_score if self.policy.chunk_retrieval.mode == "title_similarity" else self.policy.text.min_score,
            expand_to_section=self.policy.expand_to_section if self.policy.document_routing.source == "all_documents" else True,
        )
        error, retrieval_result = self.execute_retrieval_fn(request=retrieval_request, config=self.pipeline_config)
        if error is not None:
            return {
                **self._advance_stage(state, "retrieve_source_material"),
                "retrieval_request": retrieval_request,
                "failure": ValidationFailure(error_stage="retrieval", reason="retrieval_error", message=error),
            }
        if retrieval_result is None:
            return {
                **self._advance_stage(state, "retrieve_source_material"),
                "retrieval_request": retrieval_request,
                "failure": ValidationFailure(error_stage="retrieval", reason="missing_retrieval_result", message="Error: Retrieval did not return a result"),
            }
        source_package = RetrievedSourcePackage.from_retrieval_result(retrieval_result)
        return {
            **self._advance_stage(state, "retrieve_source_material"),
            "retrieval_request": retrieval_request,
            "retrieval_result": retrieval_result,
            "retrieved_source_package": source_package,
        }

    def _process_prompts_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Build the initial answer result and run prompt processing."""
        source_package = state.retrieved_source_package
        if source_package is None:
            return {
                **self._advance_stage(state, "process_prompts"),
                "failure": ValidationFailure(error_stage="workflow", reason="missing_retrieved_source_package", message="Error: Missing retrieved source package"),
            }
        answer_result = self.build_answer_result_fn(source_package)
        processed_result = self.process_prompts_fn(answer_result, source_package)
        return {
            **self._advance_stage(state, "process_prompts"),
            "answer_result": processed_result,
        }

    def _build_failure_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Convert a workflow failure to the public answer result shape."""
        failure = state.failure
        if failure is None:
            return {
                **self._advance_stage(state, "build_failure"),
                "answer_result": AnswerCommandResult.failure(query=state.question, error="Error: Missing workflow failure", error_stage="workflow"),
            }
        return {
            **self._advance_stage(state, "build_failure"),
            "answer_result": AnswerCommandResult.failure(query=state.question, error=failure.message, error_stage=failure.error_stage),
        }
