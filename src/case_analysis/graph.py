"""LangGraph orchestration for deterministic case-analysis workflows."""

from __future__ import annotations

import importlib
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, cast

from langgraph.graph import END, START, StateGraph

from src.case_analysis.agent_tools import CaseEvidenceGatheringAgentNode, ToolRequest
from src.case_analysis.models import ApplicabilityAnalysisOutput, ApproachIdentificationOutput, CaseEvidenceAgentInput, CaseEvidenceAgentResult, RetrievedSourcePackage, ToolCallRecord, ValidatedQuestion, ValidationFailure
from src.case_analysis.stages import ExecuteRetrievalFn, ValidateQuestionStage
from src.models.answer_command_result import AnswerCommandResult
from src.retrieval.request_builder import build_retrieval_request

retrieval_models = importlib.import_module("src.retrieval.models")

if TYPE_CHECKING:
    from langgraph.graph.state import CompiledStateGraph

    from src.case_analysis.workflow import AnswerWorkflowProcessor
    from src.policy import ResolvedRetrievalPolicy
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
    case_evidence_input: CaseEvidenceAgentInput | None = None
    case_evidence_result: CaseEvidenceAgentResult | None = None
    case_evidence_tool_calls: tuple[ToolCallRecord, ...] = ()
    formatted_chunks: tuple[str, ...] = ()
    chunk_summary: str = ""
    approach_identification_output: ApproachIdentificationOutput | None = None
    applicability_analysis_context: str = ""
    applicability_analysis_output: ApplicabilityAnalysisOutput | None = None
    clarification_stage: str | None = None
    clarification_questions: tuple[str, ...] = ()
    failure: ValidationFailure | None = None


@dataclass(frozen=True)
class CaseAnalysisGraphRunner:
    """Run the deterministic answer workflow through LangGraph."""

    policy: ResolvedRetrievalPolicy
    pipeline_config: RetrievalPipelineConfig
    execute_retrieval_fn: ExecuteRetrievalFn
    workflow_processor: AnswerWorkflowProcessor
    case_evidence_enabled: bool = True
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
            case_evidence_input=cast("CaseEvidenceAgentInput | None", final_state.get("case_evidence_input")),
            case_evidence_result=cast("CaseEvidenceAgentResult | None", final_state.get("case_evidence_result")),
            case_evidence_tool_calls=cast("tuple[ToolCallRecord, ...]", final_state.get("case_evidence_tool_calls", ())),
            formatted_chunks=cast("tuple[str, ...]", final_state.get("formatted_chunks", ())),
            chunk_summary=cast("str", final_state.get("chunk_summary", "")),
            approach_identification_output=cast("ApproachIdentificationOutput | None", final_state.get("approach_identification_output")),
            applicability_analysis_context=cast("str", final_state.get("applicability_analysis_context", "")),
            applicability_analysis_output=cast("ApplicabilityAnalysisOutput | None", final_state.get("applicability_analysis_output")),
            clarification_stage=cast("str | None", final_state.get("clarification_stage")),
            clarification_questions=cast("tuple[str, ...]", final_state.get("clarification_questions", ())),
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
        builder.add_node("prepare_retrieval_request", self._prepare_retrieval_request_node)
        builder.add_node("retrieve_source_material", self._retrieve_source_material_node)
        builder.add_node("run_case_evidence_agent", self._run_case_evidence_agent_node)
        builder.add_node("prepare_prompt_materials", self._prepare_prompt_materials_node)
        builder.add_node("run_approach_identification", self._run_approach_identification_node)
        builder.add_node("prepare_applicability_context", self._prepare_applicability_context_node)
        builder.add_node("run_applicability_analysis", self._run_applicability_analysis_node)
        builder.add_node("build_clarification_failure", self._build_clarification_failure_node)
        builder.add_node("build_failure", self._build_failure_node)
        builder.add_node("finalize_answer", self._finalize_answer_node)

        builder.add_edge(START, "validate_question")
        builder.add_conditional_edges(
            "validate_question",
            self._route_after_failure_capable_node,
            {"continue": "prepare_retrieval_request", "fail": "build_failure"},
        )
        builder.add_conditional_edges(
            "prepare_retrieval_request",
            self._route_after_failure_capable_node,
            {"continue": "retrieve_source_material", "fail": "build_failure"},
        )
        builder.add_conditional_edges(
            "retrieve_source_material",
            self._route_after_failure_capable_node,
            {"continue": "run_case_evidence_agent", "fail": "build_failure"},
        )
        builder.add_conditional_edges(
            "run_case_evidence_agent",
            self._route_after_failure_capable_node,
            {"continue": "prepare_prompt_materials", "fail": "build_failure"},
        )
        builder.add_conditional_edges(
            "prepare_prompt_materials",
            self._route_after_failure_capable_node,
            {"continue": "run_approach_identification", "fail": "build_failure"},
        )
        builder.add_conditional_edges(
            "run_approach_identification",
            self._route_after_approach_identification_node,
            {"continue": "prepare_applicability_context", "clarify": "build_clarification_failure", "fail": "build_failure"},
        )
        builder.add_conditional_edges(
            "prepare_applicability_context",
            self._route_after_failure_capable_node,
            {"continue": "run_applicability_analysis", "fail": "build_failure"},
        )
        builder.add_conditional_edges(
            "run_applicability_analysis",
            self._route_after_applicability_analysis_node,
            {"continue": "finalize_answer", "clarify": "build_clarification_failure", "fail": "build_failure"},
        )
        builder.add_edge("build_clarification_failure", END)
        builder.add_edge("build_failure", END)
        builder.add_edge("finalize_answer", END)
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

    def _route_after_approach_identification_node(self, state: CaseAnalysisState) -> str:
        """Route toward clarification when approach identification asks for it."""
        if state.failure is not None:
            return "fail"
        approach_identification_output = state.approach_identification_output
        if approach_identification_output is not None and approach_identification_output.status == "needs_clarification":
            return "clarify"
        return "continue"

    def _route_after_applicability_analysis_node(self, state: CaseAnalysisState) -> str:
        """Route toward clarification when applicability analysis asks for it."""
        if state.failure is not None:
            return "fail"
        applicability_analysis_output = state.applicability_analysis_output
        if applicability_analysis_output is not None and applicability_analysis_output.status == "needs_clarification":
            return "clarify"
        return "continue"

    def _prepare_retrieval_request_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Prepare the retrieval request as an explicit graph checkpoint."""
        if state.validated_question is None:
            return {
                **self._advance_stage(state, "prepare_retrieval_request"),
                "failure": ValidationFailure(error_stage="validation", reason="missing_validated_question", message="Error: Missing validated question"),
            }
        expansion = self.policy.chunk_retrieval.profile_config.expansion
        expand_to_section = (expansion.expand_to_section if expansion is not None else False) if self.policy.document_routing.source == "all_documents" else True
        retrieval_request = build_retrieval_request(
            query=state.validated_question.question,
            policy=self.policy,
            chunk_min_score=self.policy.chunk_retrieval.profile_config.filter.min_score,
            expand_to_section=expand_to_section,
        )

        return {
            **self._advance_stage(state, "prepare_retrieval_request"),
            "retrieval_request": retrieval_request,
        }

    def _retrieve_source_material_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Retrieve source material through the existing retrieval pipeline."""
        retrieval_request = state.retrieval_request
        if retrieval_request is None:
            return {
                **self._advance_stage(state, "retrieve_source_material"),
                "failure": ValidationFailure(error_stage="workflow", reason="missing_retrieval_request", message="Error: Missing retrieval request"),
            }
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

    def _run_case_evidence_agent_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Run bounded case-evidence gathering after retrieval."""
        source_package = state.retrieved_source_package
        if source_package is None:
            return {
                **self._advance_stage(state, "run_case_evidence_agent"),
                "failure": ValidationFailure(error_stage="workflow", reason="missing_retrieved_source_package", message="Error: Missing retrieved source package"),
            }
        case_evidence_input = CaseEvidenceAgentInput(
            case_id=state.question,
            issue_type=self.policy.policy_name,
            known_facts=list(source_package.retrieved_doc_uids),
            required_criteria=["retrieve_case_evidence"],
        )
        agent_node = self._build_case_evidence_agent_node(source_package)
        case_evidence_result = agent_node.execute(case_evidence_input)
        if isinstance(case_evidence_result, ValidationFailure):
            return {
                **self._advance_stage(state, "run_case_evidence_agent"),
                "failure": case_evidence_result,
            }
        return {
            **self._advance_stage(state, "run_case_evidence_agent"),
            "case_evidence_input": case_evidence_input,
            "case_evidence_result": case_evidence_result,
            "case_evidence_tool_calls": tuple(case_evidence_result.tool_calls),
        }

    def _build_case_evidence_agent_node(self, source_package: RetrievedSourcePackage) -> CaseEvidenceGatheringAgentNode:
        """Build the bounded evidence agent with a narrow tool allow-list."""
        doc_chunks = source_package.to_doc_chunks()
        doc_uids = list(source_package.retrieved_doc_uids)
        max_tool_calls = max(1, min(len(doc_uids), 2))

        def planner(agent_input: CaseEvidenceAgentInput) -> list[ToolRequest]:
            del agent_input
            return [ToolRequest(name="retrieve_case_evidence", arguments={"doc_uid": doc_uid}) for doc_uid in doc_uids[:max_tool_calls]]

        def retrieve_case_evidence(arguments: dict[str, object]) -> dict[str, object]:
            doc_uid = str(arguments["doc_uid"])
            chunks = doc_chunks.get(doc_uid, [])
            snippets = [chunk.text for chunk in chunks[:2] if chunk.text is not None]
            return {
                "doc_uid": doc_uid,
                "chunk_count": len(chunks),
                "snippets": snippets,
            }

        return CaseEvidenceGatheringAgentNode(
            enabled=self.case_evidence_enabled,
            planner_fn=planner,
            tools={"retrieve_case_evidence": retrieve_case_evidence},
            max_tool_calls=max_tool_calls,
        )

    def _prepare_prompt_materials_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Prepare reusable prompt artifacts for the graph."""
        source_package = state.retrieved_source_package
        if source_package is None:
            return {
                **self._advance_stage(state, "prepare_prompt_materials"),
                "failure": ValidationFailure(error_stage="workflow", reason="missing_retrieved_source_package", message="Error: Missing retrieved source package"),
            }
        formatted_chunks, chunk_summary = self.workflow_processor.prepare_prompt_materials(source_package.to_search_results(), source_package.to_doc_chunks())
        return {
            **self._advance_stage(state, "prepare_prompt_materials"),
            "answer_result": self.workflow_processor.build_answer_result_from_source_package(source_package),
            "formatted_chunks": formatted_chunks,
            "chunk_summary": chunk_summary,
        }

    def _run_approach_identification_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Run approach identification as a graph step."""
        answer_result = state.answer_result
        if answer_result is None:
            return {
                **self._advance_stage(state, "run_approach_identification"),
                "failure": ValidationFailure(error_stage="workflow", reason="missing_answer_result", message="Error: Missing answer result"),
            }
        formatted_chunks = list(state.formatted_chunks)
        processed_result, approach_identification_output = self.workflow_processor.run_approach_identification(answer_result, formatted_chunks, state.chunk_summary)
        node_result: dict[str, object] = {
            **self._advance_stage(state, "run_approach_identification"),
            "answer_result": processed_result,
        }
        if isinstance(approach_identification_output, ValidationFailure):
            node_result["failure"] = approach_identification_output
            return node_result
        node_result["approach_identification_output"] = approach_identification_output
        if approach_identification_output.status == "needs_clarification":
            node_result["clarification_stage"] = "approach_identification"
            node_result["clarification_questions"] = tuple(approach_identification_output.questions)
        return node_result

    def _prepare_applicability_context_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Build the applicability-analysis context as a graph checkpoint."""
        answer_result = state.answer_result
        approach_identification_output = state.approach_identification_output
        if answer_result is None or approach_identification_output is None:
            return {
                **self._advance_stage(state, "prepare_applicability_context"),
                "failure": ValidationFailure(error_stage="workflow", reason="missing_approach_identification_output", message="Error: Missing approach identification output"),
            }
        applicability_analysis_context = self.workflow_processor.prepare_applicability_analysis_context(list(state.formatted_chunks), approach_identification_output)
        return {
            **self._advance_stage(state, "prepare_applicability_context"),
            "answer_result": answer_result,
            "applicability_analysis_context": applicability_analysis_context,
        }

    def _run_applicability_analysis_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Run applicability analysis as a graph step."""
        answer_result = state.answer_result
        approach_identification_output = state.approach_identification_output
        if answer_result is None or approach_identification_output is None:
            return {
                **self._advance_stage(state, "run_applicability_analysis"),
                "failure": ValidationFailure(error_stage="workflow", reason="missing_approach_identification_output", message="Error: Missing approach identification output"),
            }
        processed_result, applicability_analysis_output, applicability_analysis_context = self.workflow_processor.run_applicability_analysis(
            answer_result,
            list(state.formatted_chunks),
            approach_identification_output,
        )
        node_result: dict[str, object] = {
            **self._advance_stage(state, "run_applicability_analysis"),
            "answer_result": processed_result,
            "applicability_analysis_context": applicability_analysis_context,
        }
        if isinstance(applicability_analysis_output, ValidationFailure):
            node_result["failure"] = applicability_analysis_output
            return node_result
        node_result["applicability_analysis_output"] = applicability_analysis_output
        if applicability_analysis_output.status == "needs_clarification":
            node_result["clarification_stage"] = "applicability_analysis"
            node_result["clarification_questions"] = tuple(applicability_analysis_output.questions_fr)
        return node_result

    def _build_clarification_failure_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Convert a clarification branch into a public failure result."""
        clarification_stage = state.clarification_stage or "workflow"
        clarification_questions = list(state.clarification_questions)
        answer_result = self.workflow_processor.build_clarification_failure(state.question, clarification_stage, clarification_questions)
        return {
            **self._advance_stage(state, "build_clarification_failure"),
            "answer_result": answer_result,
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

    def _finalize_answer_node(self, state: CaseAnalysisState) -> dict[str, object]:
        """Finalize the answer after all deterministic checks pass."""
        answer_result = state.answer_result
        approach_identification_output = state.approach_identification_output
        applicability_analysis_output = state.applicability_analysis_output
        applicability_analysis_context = state.applicability_analysis_context
        if answer_result is None or approach_identification_output is None or applicability_analysis_output is None:
            return {
                **self._advance_stage(state, "finalize_answer"),
                "failure": ValidationFailure(error_stage="workflow", reason="missing_final_outputs", message="Error: Missing final workflow outputs"),
            }
        finalized_result = self.workflow_processor.finalize_answer(
            answer_result,
            approach_identification_output,
            applicability_analysis_output,
            applicability_analysis_context,
        )
        return {
            **self._advance_stage(state, "finalize_answer"),
            "answer_result": finalized_result,
        }
