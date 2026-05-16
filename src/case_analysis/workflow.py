"""Answer workflow processing helpers."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from src.case_analysis.citation_validation import CitationValidationService
from src.case_analysis.context_builder import ContextBuilder
from src.case_analysis.models import ApplicabilityAnalysisOutput, ApproachIdentificationOutput, RetrievedSourcePackage, ValidationFailure
from src.case_analysis.output_formatting import build_chunk_summary, build_retrieved_chunk_hits, escape_xml, extract_prompt_content
from src.case_analysis.prompt_builder import PromptBuilder
from src.case_analysis.rendering import AnswerRenderingAdapter
from src.case_analysis.stages import AnswerGeneratorProtocol, ApplicabilityAnalysisStage, ApproachIdentificationStage
from src.models.answer_command_result import AnswerCommandResult, RetrievedDocumentHit
from src.models.document import infer_document_kind, infer_exact_document_type

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from src.interfaces import SearchResult
    from src.models.chunk import Chunk
    from src.policy import RetrievalPolicy

logger = logging.getLogger(__name__)


@dataclass
class AnswerWorkflowProcessor:
    """Own prompt execution, validation, and artifact rendering for one answer run."""

    query: str
    policy: RetrievalPolicy
    read_prompt_template_fn: Callable[[Path], str]
    approach_identification_path: Path
    applicability_analysis_path: Path
    answer_generator: AnswerGeneratorProtocol
    context_builder: ContextBuilder = field(default_factory=ContextBuilder)
    rendering_adapter: AnswerRenderingAdapter = field(default_factory=AnswerRenderingAdapter)
    prompt_builder: PromptBuilder = field(default_factory=PromptBuilder)
    citation_validation_service: CitationValidationService = field(default_factory=CitationValidationService)
    retrieved_doc_uids: list[str] = field(default_factory=list)

    def build_answer_result_from_source_package(self, source_package: RetrievedSourcePackage) -> AnswerCommandResult:
        """Build the initial answer result from retrieved source material."""
        self.retrieved_doc_uids = list(source_package.retrieved_doc_uids)
        search_results = source_package.to_search_results()
        doc_chunks = source_package.to_doc_chunks()
        return AnswerCommandResult(
            query=self.query,
            retrieved_doc_uids=list(self.retrieved_doc_uids),
            document_hits=[
                RetrievedDocumentHit(
                    doc_uid=hit.doc_uid,
                    score=hit.score,
                    document_type=hit.document_type,
                    document_kind=infer_document_kind(hit.doc_uid),
                )
                for hit in source_package.document_hits
            ],
            chunk_hits=build_retrieved_chunk_hits(search_results, doc_chunks),
        )

    def prepare_prompt_materials(self, results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> tuple[tuple[str, ...], str]:
        """Build reusable prompt formatting artifacts for the graph."""
        chunk_summary = build_chunk_summary(results, doc_chunks, logger)
        formatted_chunks = tuple(self._format_chunks(results, doc_chunks))
        return formatted_chunks, chunk_summary

    def run_approach_identification(
        self,
        result: AnswerCommandResult,
        formatted_chunks: list[str],
        chunk_summary: str,
    ) -> tuple[AnswerCommandResult, ApproachIdentificationOutput | ValidationFailure]:
        """Run approach identification and keep the typed result on success."""
        approach_identification_full = self._build_prompt_from_template(self.approach_identification_path, formatted_chunks, chunk_summary)
        result.approach_identification_text = extract_prompt_content(approach_identification_full)
        approach_identification_text = result.approach_identification_text

        approach_identification_output = ApproachIdentificationStage(answer_generator=self.answer_generator).execute(approach_identification_text)
        if isinstance(approach_identification_output, ValidationFailure):
            result.error = approach_identification_output.message
            result.error_stage = approach_identification_output.error_stage
            return result, approach_identification_output

        result.approach_identification_output = approach_identification_output
        return result, approach_identification_output

    def prepare_applicability_analysis_context(
        self,
        formatted_chunks: list[str],
        approach_identification_output: ApproachIdentificationOutput,
    ) -> str:
        """Build the context used by applicability analysis."""
        return self.context_builder.build_applicability_analysis_context(formatted_chunks, approach_identification_output)

    def run_applicability_analysis(
        self,
        result: AnswerCommandResult,
        formatted_chunks: list[str],
        approach_identification_output: ApproachIdentificationOutput,
    ) -> tuple[AnswerCommandResult, ApplicabilityAnalysisOutput | ValidationFailure, str]:
        """Run applicability analysis and keep the typed result on success."""
        applicability_analysis_context = self.prepare_applicability_analysis_context(formatted_chunks, approach_identification_output)
        applicability_analysis_prompt = self._build_applicability_analysis(applicability_analysis_context, approach_identification_output)
        result.applicability_analysis_text = extract_prompt_content(applicability_analysis_prompt)
        applicability_analysis_text = result.applicability_analysis_text

        applicability_analysis_output = ApplicabilityAnalysisStage(answer_generator=self.answer_generator).execute(applicability_analysis_text)
        if isinstance(applicability_analysis_output, ValidationFailure):
            result.error = applicability_analysis_output.message
            result.error_stage = applicability_analysis_output.error_stage
            return result, applicability_analysis_output, applicability_analysis_context

        result.applicability_analysis_output = applicability_analysis_output
        return result, applicability_analysis_output, applicability_analysis_context

    def finalize_answer(
        self,
        result: AnswerCommandResult,
        approach_identification_output: ApproachIdentificationOutput,
        applicability_analysis_output: ApplicabilityAnalysisOutput,
        applicability_analysis_context: str,
    ) -> AnswerCommandResult:
        """Validate citations, render memo artifacts, and mark success."""
        logger.info("Step 2 complete: Received final answer from LLM")

        citation_verification_result = self.citation_validation_service.validate_applicability_analysis(applicability_analysis_output, applicability_analysis_context)
        result.citation_verification_result = citation_verification_result

        rendered_artifacts = self.rendering_adapter.render_applicability_analysis(
            query=self.query,
            retrieved_doc_uids=self.retrieved_doc_uids,
            approach_identification=approach_identification_output,
            applicability_analysis=applicability_analysis_output,
            applicability_analysis_context=applicability_analysis_context,
        )
        result.applicability_analysis_memo_markdown = rendered_artifacts.memo_markdown
        result.applicability_analysis_faq_markdown = rendered_artifacts.faq_markdown
        result.mark_success()
        return result

    def build_clarification_failure(self, query: str, stage: str, questions: list[str]) -> AnswerCommandResult:
        """Build a failure result for a clarification control point."""
        question_text = "; ".join(questions) if questions else "Clarification required"
        return AnswerCommandResult.failure(
            query=query,
            error=f"Error: Clarification required at {stage}: {question_text}",
            error_stage="clarification",
        )

    def process_source_package_prompts(self, result: AnswerCommandResult, source_package: RetrievedSourcePackage) -> AnswerCommandResult:
        """Run prompt processing for one retrieved source package."""
        results = source_package.to_search_results()
        doc_chunks = source_package.to_doc_chunks()
        formatted_chunks, chunk_summary = self.prepare_prompt_materials(results, doc_chunks)
        processed_result, approach_identification_output = self.run_approach_identification(result, list(formatted_chunks), chunk_summary)
        if isinstance(approach_identification_output, ValidationFailure):
            return processed_result
        if approach_identification_output.status == "needs_clarification":
            return self.build_clarification_failure(self.query, "approach_identification", approach_identification_output.questions)

        processed_result, applicability_analysis_output, applicability_analysis_context = self.run_applicability_analysis(
            processed_result,
            list(formatted_chunks),
            approach_identification_output,
        )
        if isinstance(applicability_analysis_output, ValidationFailure):
            return processed_result
        if applicability_analysis_output.status == "needs_clarification":
            return self.build_clarification_failure(self.query, "applicability_analysis", applicability_analysis_output.questions_fr)

        return self.finalize_answer(
            processed_result,
            approach_identification_output,
            applicability_analysis_output,
            applicability_analysis_context,
        )

    def _build_prompt_from_template(self, template_path: Path, chunks: list[str], chunk_summary: str) -> str:
        template = self.read_prompt_template_fn(template_path)
        return self.prompt_builder.build_approach_identification(template, self.query, chunks, chunk_summary)

    def _build_applicability_analysis(self, context: str, approach_identification: ApproachIdentificationOutput) -> str:
        template = self.read_prompt_template_fn(self.applicability_analysis_path)
        return self.prompt_builder.build_applicability_analysis(template, self.query, context, approach_identification)

    def _format_chunks(self, results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> list[str]:
        doc_order: list[str] = []
        chunk_ids_by_doc: dict[str, set[int]] = {}
        score_by_chunk: dict[tuple[str, int], float] = {}

        for result in results:
            doc_uid = result["doc_uid"]
            chunk_id = result["chunk_id"]
            score = result["score"]
            if doc_uid not in chunk_ids_by_doc:
                chunk_ids_by_doc[doc_uid] = set()
                doc_order.append(doc_uid)
            chunk_ids_by_doc[doc_uid].add(chunk_id)
            score_by_chunk[(doc_uid, chunk_id)] = score

        formatted_documents: list[str] = []
        for doc_uid in doc_order:
            formatted_chunks: list[str] = []
            for chunk in doc_chunks.get(doc_uid, []):
                chunk_id = chunk.id
                if chunk_id is None or chunk_id not in chunk_ids_by_doc.get(doc_uid, set()):
                    continue
                score = score_by_chunk.get((doc_uid, chunk_id), 0.0)
                chunk_xml = f'<chunk id="{chunk_id}" doc_uid="{escape_xml(doc_uid)}" paragraph="{escape_xml(chunk.chunk_number)}" score="{score:.4f}">\n{chunk.text}\n</chunk>'
                formatted_chunks.append(chunk_xml)

            joined_chunks = "\n\n".join(formatted_chunks)
            document_type = infer_exact_document_type(doc_uid)
            document_kind = infer_document_kind(doc_uid)
            document_type_attr = escape_xml(document_type or "")
            document_kind_attr = escape_xml(document_kind or "")
            document_xml = f'<Document name="{escape_xml(doc_uid)}" document_type="{document_type_attr}" document_kind="{document_kind_attr}">\n{joined_chunks}\n</Document>'
            formatted_documents.append(document_xml)

        return formatted_documents
