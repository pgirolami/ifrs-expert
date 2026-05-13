"""LangGraph orchestration for deterministic case-analysis workflows."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from langgraph.graph import END, START, StateGraph

from src.case_analysis.models import RetrievedSourcePackage, ValidatedQuestion, ValidationFailure
from src.case_analysis.stages import ExecuteRetrievalFn, RetrieveSourceMaterialStage, ValidateQuestionStage
from src.models.answer_command_result import AnswerCommandResult

if TYPE_CHECKING:
    from collections.abc import Callable

    from langgraph.graph.state import CompiledStateGraph

    from src.policy import RetrievalPolicy
    from src.retrieval.pipeline import RetrievalPipelineConfig


@dataclass
class CaseAnalysisState:
    """State passed between deterministic case-analysis graph nodes."""

    question: str = ""
    validated_question: ValidatedQuestion | None = None
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

    def run(self, question: str) -> AnswerCommandResult:
        """Run the graph and return an answer command result."""
        graph = self._build_graph()
        final_state = graph.invoke({"question": question})
        answer_result = final_state.get("answer_result")
        if answer_result is not None:
            return answer_result

        failure = final_state.get("failure")
        if failure is not None:
            return AnswerCommandResult.failure(query=question, error=failure.message, error_stage=failure.error_stage)

        return AnswerCommandResult.failure(
            query=question,
            error="Error: Case analysis graph ended without a result",
            error_stage="workflow",
        )

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
            self._route_after_validation,
            {"continue": "retrieve_source_material", "fail": "build_failure"},
        )
        builder.add_conditional_edges(
            "retrieve_source_material",
            self._route_after_retrieval,
            {"continue": "process_prompts", "fail": "build_failure"},
        )
        builder.add_edge("process_prompts", END)
        builder.add_edge("build_failure", END)
        return builder.compile()

    def _validate_question_node(self, state: CaseAnalysisState) -> dict[str, ValidatedQuestion | ValidationFailure]:
        """Validate the incoming question."""
        validation_result = ValidateQuestionStage().execute(query=state.question, policy=self.policy)
        if isinstance(validation_result, ValidationFailure):
            return {"failure": validation_result}
        return {"validated_question": validation_result}

    def _route_after_validation(self, state: CaseAnalysisState) -> str:
        """Choose whether to continue after validation."""
        if state.failure is not None:
            return "fail"
        return "continue"

    def _retrieve_source_material_node(self, state: CaseAnalysisState) -> dict[str, RetrievedSourcePackage | ValidationFailure]:
        """Retrieve source material through the existing retrieval pipeline."""
        if state.validated_question is None:
            return {"failure": ValidationFailure(error_stage="validation", reason="missing_validated_question", message="Error: Missing validated question")}
        retrieval_result = RetrieveSourceMaterialStage(
            pipeline_config=self.pipeline_config,
            execute_retrieval_fn=self.execute_retrieval_fn,
        ).execute(question=state.validated_question.question, policy=self.policy)
        if isinstance(retrieval_result, ValidationFailure):
            return {"failure": retrieval_result}
        return {"retrieved_source_package": retrieval_result}

    def _route_after_retrieval(self, state: CaseAnalysisState) -> str:
        """Choose whether to continue after retrieval."""
        if state.failure is not None:
            return "fail"
        return "continue"

    def _process_prompts_node(self, state: CaseAnalysisState) -> dict[str, AnswerCommandResult]:
        """Build the initial answer result and run prompt processing."""
        source_package = state.retrieved_source_package
        if source_package is None:
            return {
                "answer_result": AnswerCommandResult.failure(
                    query=state.question,
                    error="Error: Missing retrieved source package",
                    error_stage="workflow",
                )
            }
        answer_result = self.build_answer_result_fn(source_package)
        processed_result = self.process_prompts_fn(answer_result, source_package)
        return {"answer_result": processed_result}

    def _build_failure_node(self, state: CaseAnalysisState) -> dict[str, AnswerCommandResult]:
        """Convert a workflow failure to the public answer result shape."""
        failure = state.failure
        if failure is None:
            return {"answer_result": AnswerCommandResult.failure(query=state.question, error="Error: Missing workflow failure", error_stage="workflow")}
        return {"answer_result": AnswerCommandResult.failure(query=state.question, error=failure.message, error_stage=failure.error_stage)}
