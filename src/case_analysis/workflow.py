"""Answer workflow processing helpers."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

from src.case_analysis.citation_validation import CitationValidationService
from src.case_analysis.context_builder import ContextBuilder
from src.case_analysis.models import ApproachIdentificationOutput, RetrievedSourcePackage, ValidationFailure
from src.case_analysis.prompt_builder import PromptBuilder
from src.case_analysis.rendering import AnswerRenderingAdapter
from src.case_analysis.stages import AnswerGeneratorProtocol, ApplicabilityAnalysisStage, ApproachIdentificationStage, AuthoritySufficiencyStage
from src.models.answer_command_result import AnswerCommandResult, RetrievedChunkHit, RetrievedDocumentHit
from src.models.document import infer_document_kind, infer_exact_document_type
from src.models.provenance import Provenance

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from src.interfaces import SearchResult
    from src.models.chunk import Chunk
    from src.policy import RetrievalPolicy

logger = logging.getLogger(__name__)
TOP_CHUNK_PREVIEW_CHARS = 30


@dataclass
class OutputDocumentSections:
    """Output summary for one document and its selected section labels."""

    doc_uid: str
    section_labels: list[str]


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
            chunk_hits=_build_retrieved_chunk_hits(search_results, doc_chunks),
        )

    def process_source_package_prompts(self, result: AnswerCommandResult, source_package: RetrievedSourcePackage) -> AnswerCommandResult:
        """Run prompt processing for one retrieved source package."""
        return self._process_prompts(result, source_package.to_search_results(), source_package.to_doc_chunks())

    def _process_prompts(
        self,
        result: AnswerCommandResult,
        results: list[SearchResult],
        doc_chunks: dict[str, list[Chunk]],
    ) -> AnswerCommandResult:
        chunk_summary = _build_chunk_summary(results, doc_chunks)
        formatted_chunks = self._format_chunks(results, doc_chunks)
        return self._run_approach_identification_stage(result, formatted_chunks, chunk_summary)

    def _run_approach_identification_stage(
        self,
        result: AnswerCommandResult,
        formatted_chunks: list[str],
        chunk_summary: str,
    ) -> AnswerCommandResult:
        approach_identification_full = self._build_prompt_from_template(self.approach_identification_path, formatted_chunks, chunk_summary)
        result.approach_identification_text = _extract_prompt_content(approach_identification_full)
        approach_identification_text = result.approach_identification_text

        approach_identification_output = ApproachIdentificationStage(answer_generator=self.answer_generator).execute(approach_identification_text)
        if isinstance(approach_identification_output, ValidationFailure):
            result.error = approach_identification_output.message
            result.error_stage = approach_identification_output.error_stage
            return result

        result.approach_identification_output = approach_identification_output

        authority_sufficiency_result = AuthoritySufficiencyStage().execute(approach_identification_output)
        if isinstance(authority_sufficiency_result, ValidationFailure):
            result.error = authority_sufficiency_result.message
            result.error_stage = authority_sufficiency_result.error_stage
            return result

        return self._run_applicability_analysis_stage(result, formatted_chunks, approach_identification_output)

    def _run_applicability_analysis_stage(
        self,
        result: AnswerCommandResult,
        formatted_chunks: list[str],
        approach_identification_output: ApproachIdentificationOutput,
    ) -> AnswerCommandResult:
        applicability_analysis_context = self.context_builder.build_applicability_analysis_context(formatted_chunks, approach_identification_output)
        applicability_analysis_prompt = self._build_applicability_analysis(applicability_analysis_context, approach_identification_output)
        result.applicability_analysis_text = _extract_prompt_content(applicability_analysis_prompt)
        applicability_analysis_text = result.applicability_analysis_text

        applicability_analysis_output = ApplicabilityAnalysisStage(answer_generator=self.answer_generator).execute(applicability_analysis_text)
        if isinstance(applicability_analysis_output, ValidationFailure):
            result.error = applicability_analysis_output.message
            result.error_stage = applicability_analysis_output.error_stage
            return result

        result.applicability_analysis_output = applicability_analysis_output
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
                chunk_xml = f'<chunk id="{chunk_id}" doc_uid="{_escape_xml(doc_uid)}" paragraph="{_escape_xml(chunk.chunk_number)}" score="{score:.4f}">\n{chunk.text}\n</chunk>'
                formatted_chunks.append(chunk_xml)

            joined_chunks = "\n\n".join(formatted_chunks)
            document_type = infer_exact_document_type(doc_uid)
            document_kind = infer_document_kind(doc_uid)
            document_type_attr = _escape_xml(document_type or "")
            document_kind_attr = _escape_xml(document_kind or "")
            document_xml = f'<Document name="{_escape_xml(doc_uid)}" document_type="{document_type_attr}" document_kind="{document_kind_attr}">\n{joined_chunks}\n</Document>'
            formatted_documents.append(document_xml)

        return formatted_documents


def _build_retrieved_chunk_hits(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
) -> list[RetrievedChunkHit]:
    chunk_hits: list[RetrievedChunkHit] = []
    for result in results:
        doc_uid = str(result["doc_uid"])
        chunk_db_id = int(result["chunk_id"])
        score = float(result["score"])
        document_type = infer_exact_document_type(doc_uid)
        document_kind = infer_document_kind(doc_uid)
        for chunk in doc_chunks.get(doc_uid, []):
            if chunk.id != chunk_db_id:
                continue
            provenance_value = result.get("provenance")
            provenance = Provenance(provenance_value) if provenance_value is not None else None
            chunk_hits.append(
                RetrievedChunkHit(
                    doc_uid=doc_uid,
                    chunk_number=chunk.chunk_number,
                    chunk_id=chunk.chunk_id,
                    score=round(score, 4),
                    document_type=document_type,
                    document_kind=document_kind,
                    containing_section_id=chunk.containing_section_id,
                    containing_section_db_id=chunk.containing_section_db_id,
                    page_start=chunk.page_start,
                    page_end=chunk.page_end,
                    text=chunk.text,
                    provenance=provenance,
                )
            )
            break
    return chunk_hits


def _build_chunk_summary(results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> str:
    if not results:
        return "Retrieved chunks:\n- none"
    summaries = _build_output_document_sections(results=results, doc_chunks=doc_chunks, logger=logger)
    lines: list[str] = ["Retrieved chunks:"]
    for summary in summaries:
        sections_text = ", ".join(summary.section_labels) if summary.section_labels else "(no sections)"
        lines.append(f"- {summary.doc_uid}: {sections_text}")
    return "\n".join(lines)


def _escape_xml(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")


def _extract_prompt_content(full_output: str) -> str:
    lines = full_output.split("\n")
    start_idx = 0
    for index, line in enumerate(lines):
        if line.startswith("You are an IFRS expert"):
            start_idx = index
            break
    return "\n".join(lines[start_idx:])


def _build_output_document_sections(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
    logger: logging.Logger,
) -> list[OutputDocumentSections]:
    doc_order, chunk_ids_by_doc = _index_selected_chunk_ids_by_doc(results)
    top_chunk_by_doc = _build_top_chunk_by_doc(results)

    summaries: list[OutputDocumentSections] = []
    for doc_uid in doc_order:
        section_labels = _build_section_labels_for_doc(
            doc_uid=doc_uid,
            doc_chunks=doc_chunks,
            chunk_ids_by_doc=chunk_ids_by_doc,
            top_chunk_by_doc=top_chunk_by_doc,
            logger=logger,
        )
        summaries.append(OutputDocumentSections(doc_uid=doc_uid, section_labels=section_labels))
    return summaries


def _index_selected_chunk_ids_by_doc(results: list[SearchResult]) -> tuple[list[str], dict[str, set[int]]]:
    doc_order: list[str] = []
    chunk_ids_by_doc: dict[str, set[int]] = {}
    for result in results:
        doc_uid = str(result["doc_uid"])
        chunk_id = int(result["chunk_id"])
        if doc_uid not in chunk_ids_by_doc:
            chunk_ids_by_doc[doc_uid] = set()
            doc_order.append(doc_uid)
        chunk_ids_by_doc[doc_uid].add(chunk_id)
    return doc_order, chunk_ids_by_doc


def _build_top_chunk_by_doc(results: list[SearchResult]) -> dict[str, tuple[int, float]]:
    top_chunk_by_doc: dict[str, tuple[int, float]] = {}
    for result in results:
        doc_uid = str(result["doc_uid"])
        chunk_id = int(result["chunk_id"])
        score = float(result["score"])
        existing_top_chunk = top_chunk_by_doc.get(doc_uid)
        if existing_top_chunk is None or score > existing_top_chunk[1]:
            top_chunk_by_doc[doc_uid] = (chunk_id, score)
    return top_chunk_by_doc


def _build_section_labels_for_doc(
    *,
    doc_uid: str,
    doc_chunks: dict[str, list[Chunk]],
    chunk_ids_by_doc: dict[str, set[int]],
    top_chunk_by_doc: dict[str, tuple[int, float]],
    logger: logging.Logger,
) -> list[str]:
    section_labels: list[str] = []
    seen_sections: set[str] = set()
    top_chunk_logged = False
    top_chunk_id, top_chunk_score = top_chunk_by_doc.get(doc_uid, (-1, 0.0))
    for chunk in doc_chunks.get(doc_uid, []):
        chunk_id = chunk.id
        if chunk_id is None:
            continue
        if chunk_id not in chunk_ids_by_doc.get(doc_uid, set()):
            continue
        section_label = chunk.chunk_number or f"chunk {chunk_id}"
        if not top_chunk_logged and chunk_id == top_chunk_id:
            section_preview = " ".join(chunk.text.split())[:TOP_CHUNK_PREVIEW_CHARS]
            logger.info(f"Output document top chunk doc_uid={doc_uid}; section_number={section_label}; score={top_chunk_score:.4f}; section_text_preview='{section_preview}'")
            top_chunk_logged = True
        if section_label in seen_sections:
            continue
        seen_sections.add(section_label)
        section_labels.append(section_label)
    return section_labels
