"""Case-analysis answer engine and rendering helpers."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Protocol

from src.case_analysis.citation_validation import CitationValidationService
from src.case_analysis.context_builder import ContextBuilder
from src.case_analysis.graph import CaseAnalysisGraphRunner
from src.case_analysis.models import ApproachIdentificationOutput, RetrievedSourcePackage, ValidationFailure
from src.case_analysis.prompt_builder import PromptBuilder
from src.case_analysis.rendering import AnswerRenderingAdapter
from src.case_analysis.stages import AnswerGeneratorProtocol, ApplicabilityAnalysisStage, ApproachIdentificationStage, AuthoritySufficiencyStage, ExecuteRetrievalFn
from src.commands.document_output import build_output_document_sections
from src.models.answer_command_result import AnswerCommandResult, RetrievedChunkHit, RetrievedDocumentHit
from src.models.document import infer_document_kind, infer_exact_document_type
from src.models.provenance import Provenance
from src.retrieval.pipeline import RetrievalPipelineConfig, execute_retrieval

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.interfaces import (
        ReadChunkStoreProtocol,
        ReadSectionStoreProtocol,
        ReferenceStoreProtocol,
        SearchDocumentVectorStoreProtocol,
        SearchResult,
        SearchTitleVectorStoreProtocol,
        SearchVectorStoreProtocol,
    )
    from src.models.chunk import Chunk
    from src.policy import RetrievalPolicy

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).parent.parent.parent
APPROACH_IDENTIFICATION_PATH = PROJECT_ROOT / "prompts" / "answer_prompt_A.txt"
APPLICABILITY_ANALYSIS_PATH = PROJECT_ROOT / "prompts" / "answer_prompt_B.txt"


class AnswerEngineConfigProtocol(Protocol):
    """Runtime dependency shape consumed by AnswerEngine."""

    vector_store: SearchVectorStoreProtocol
    chunk_store: ReadChunkStoreProtocol
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[], Path]
    answer_generator: AnswerGeneratorProtocol
    section_store: ReadSectionStoreProtocol | None
    reference_store: ReferenceStoreProtocol | None
    title_vector_store: SearchTitleVectorStoreProtocol | None
    title_index_path_fn: Callable[[], Path] | None
    document_vector_store: SearchDocumentVectorStoreProtocol | None
    document_vector_store_factory: Callable[[str], SearchDocumentVectorStoreProtocol] | None
    document_index_path_fn: Callable[[str], Path] | None


def _read_prompt_template(path: Path) -> str:
    """Read the prompt template from file."""
    lines = path.read_text(encoding="utf-8").split("\n")
    return "\n".join(line for line in lines if not line.lstrip().startswith("#"))


def _prompt_file_exists(path: Path) -> bool:
    """Check if prompt template file exists."""
    return path.exists()


@dataclass(frozen=True)
class AnswerEngineHooks:
    """Patchable callables used by the answer engine."""

    execute_retrieval_fn: ExecuteRetrievalFn = execute_retrieval
    prompt_file_exists_fn: Callable[[Path], bool] = _prompt_file_exists
    read_prompt_template_fn: Callable[[Path], str] = _read_prompt_template


def _build_retrieved_chunk_hits(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
) -> list[RetrievedChunkHit]:
    """Build serializable chunk hits from the retrieval result."""
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


def _extract_prompt_content(full_output: str) -> str:
    """Extract only the prompt content, skipping the chunk summary at the top."""
    lines = full_output.split("\n")
    start_idx = 0
    for index, line in enumerate(lines):
        if line.startswith("You are an IFRS expert"):
            start_idx = index
            break
    return "\n".join(lines[start_idx:])


class AnswerEngine:
    """Own answer workflow orchestration, prompt execution, and artifacts."""

    def __init__(
        self,
        query: str,
        policy: RetrievalPolicy,
        config: AnswerEngineConfigProtocol,
        hooks: AnswerEngineHooks | None = None,
    ) -> None:
        """Initialize the engine with workflow dependencies."""
        self.query = query
        self._policy = policy
        self._config = config
        self._hooks = hooks or AnswerEngineHooks()
        self._context_builder = ContextBuilder()
        self._rendering_adapter = AnswerRenderingAdapter()
        self._prompt_builder = PromptBuilder()
        self._citation_validation_service = CitationValidationService()
        self._retrieved_doc_uids: list[str] = []

    def run(self) -> AnswerCommandResult:
        """Run prerequisite checks and the deterministic case-analysis graph."""
        prerequisite_error = self.get_prerequisite_error()
        if prerequisite_error is not None:
            return AnswerCommandResult.failure(query=self.query, error=prerequisite_error, error_stage="prerequisite")

        runner = CaseAnalysisGraphRunner(
            policy=self._policy,
            pipeline_config=self._build_retrieval_pipeline_config(),
            execute_retrieval_fn=self._hooks.execute_retrieval_fn,
            build_answer_result_fn=self._build_answer_result_from_source_package,
            process_prompts_fn=self._process_source_package_prompts,
        )
        return runner.run(self.query)

    def get_prerequisite_error(self) -> str | None:
        """Return a CLI/runtime prerequisite error, if any."""
        prompt_error = self._get_prompt_template_error()
        if prompt_error is not None:
            return prompt_error

        if self._policy.document_routing.source == "all_documents" and self._policy.chunk_retrieval.mode == "title_similarity":
            return self._get_title_prerequisite_error()
        if self._policy.document_routing.source == "document_representation":
            document_prerequisite_error = self._get_document_prerequisite_error()
            if document_prerequisite_error is not None:
                return document_prerequisite_error

        index_path = self._config.index_path_fn()
        if not index_path.exists():
            logger.error(f"Missing vector index at {index_path}; corpus must be built before running the answer pipeline")
            return "Error: No index found. Please run 'store' command first."
        return None

    def _get_prompt_template_error(self) -> str | None:
        if not self._hooks.prompt_file_exists_fn(APPROACH_IDENTIFICATION_PATH):
            logger.error(f"Missing approach identification template at {APPROACH_IDENTIFICATION_PATH}")
            return "Error: approach identification template not found."
        if not self._hooks.prompt_file_exists_fn(APPLICABILITY_ANALYSIS_PATH):
            logger.error(f"Missing applicability analysis template at {APPLICABILITY_ANALYSIS_PATH}")
            return "Error: applicability analysis template not found."
        return None

    def _get_title_prerequisite_error(self) -> str | None:
        if self._config.title_index_path_fn is None:
            return "Error: Title retrieval is not configured."
        title_index_path = self._config.title_index_path_fn()
        if not title_index_path.exists():
            logger.error(f"Missing title vector index at {title_index_path}; corpus must be built before running the answer pipeline")
            return "Error: No title index found. Please run 'store' command first."
        return None

    def _get_document_prerequisite_error(self) -> str | None:
        if self._config.document_index_path_fn is None:
            return "Error: Document retrieval is not configured."
        required_representations = sorted({document_policy.similarity_representation for document_policy in self._policy.documents.by_document_type.values()})
        for representation in required_representations:
            try:
                document_index_path = self._config.document_index_path_fn(representation)
            except TypeError:
                document_index_path = self._config.document_index_path_fn()  # type: ignore[call-arg]
            if document_index_path.exists():
                continue
            logger.error(f"Missing document vector index at {document_index_path} for representation={representation}; corpus must be built before running the answer pipeline")
            return "Error: No document index found. Please run 'store' command first."
        return None

    def _build_retrieval_pipeline_config(self) -> RetrievalPipelineConfig:
        return RetrievalPipelineConfig(
            vector_store=self._config.vector_store,
            chunk_store=self._config.chunk_store,
            init_db_fn=self._config.init_db_fn,
            index_path_fn=self._config.index_path_fn,
            section_store=self._config.section_store,
            reference_store=self._config.reference_store,
            title_vector_store=self._config.title_vector_store,
            title_index_path_fn=self._config.title_index_path_fn,
            document_vector_store=self._config.document_vector_store,
            document_vector_store_factory=self._config.document_vector_store_factory,
            document_index_path_fn=self._config.document_index_path_fn,
        )

    def _build_answer_result_from_source_package(self, source_package: RetrievedSourcePackage) -> AnswerCommandResult:
        self._retrieved_doc_uids = source_package.retrieved_doc_uids
        search_results = source_package.to_search_results()
        doc_chunks = source_package.to_doc_chunks()
        return AnswerCommandResult(
            query=self.query,
            retrieved_doc_uids=list(self._retrieved_doc_uids),
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

    def _process_source_package_prompts(
        self,
        result: AnswerCommandResult,
        source_package: RetrievedSourcePackage,
    ) -> AnswerCommandResult:
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
        approach_identification_full = self._build_prompt_from_template(APPROACH_IDENTIFICATION_PATH, formatted_chunks, chunk_summary)
        result.approach_identification_text = _extract_prompt_content(approach_identification_full)
        approach_identification_text = result.approach_identification_text

        approach_identification_output = ApproachIdentificationStage(answer_generator=self._config.answer_generator).execute(approach_identification_text)
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
        applicability_analysis_context = self._context_builder.build_applicability_analysis_context(formatted_chunks, approach_identification_output)
        applicability_analysis_prompt = self._build_applicability_analysis(applicability_analysis_context, approach_identification_output)
        result.applicability_analysis_text = _extract_prompt_content(applicability_analysis_prompt)
        applicability_analysis_text = result.applicability_analysis_text

        applicability_analysis_output = ApplicabilityAnalysisStage(answer_generator=self._config.answer_generator).execute(applicability_analysis_text)
        if isinstance(applicability_analysis_output, ValidationFailure):
            result.error = applicability_analysis_output.message
            result.error_stage = applicability_analysis_output.error_stage
            return result

        result.applicability_analysis_output = applicability_analysis_output
        logger.info("Step 2 complete: Received final answer from LLM")

        citation_verification_result = self._citation_validation_service.validate_applicability_analysis(applicability_analysis_output, applicability_analysis_context)
        result.citation_verification_result = citation_verification_result

        rendered_artifacts = self._rendering_adapter.render_applicability_analysis(
            query=self.query,
            retrieved_doc_uids=self._retrieved_doc_uids,
            approach_identification=approach_identification_output,
            applicability_analysis=applicability_analysis_output,
            applicability_analysis_context=applicability_analysis_context,
        )
        result.applicability_analysis_memo_markdown = rendered_artifacts.memo_markdown
        result.applicability_analysis_faq_markdown = rendered_artifacts.faq_markdown
        result.mark_success()
        return result

    def _build_prompt_from_template(self, template_path: Path, chunks: list[str], chunk_summary: str) -> str:
        template = self._hooks.read_prompt_template_fn(template_path)
        return self._prompt_builder.build_approach_identification(template, self.query, chunks, chunk_summary)

    def _build_applicability_analysis(self, context: str, approach_identification: ApproachIdentificationOutput) -> str:
        template = self._hooks.read_prompt_template_fn(APPLICABILITY_ANALYSIS_PATH)
        return self._prompt_builder.build_applicability_analysis(template, self.query, context, approach_identification)

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


def _build_applicability_analysis_context(formatted_chunks: list[str], approach_identification_output: ApproachIdentificationOutput) -> str:
    return ContextBuilder().build_applicability_analysis_context(formatted_chunks, approach_identification_output)


def _extract_authority_references(approach_identification_output: ApproachIdentificationOutput) -> set[tuple[str, str]] | None:
    return ContextBuilder().extract_authority_references(approach_identification_output)


def _filter_chunks_by_authority(formatted_chunks: list[str], authority_refs: set[tuple[str, str]]) -> str:
    return ContextBuilder().filter_chunks_by_authority(formatted_chunks, authority_refs)


def _escape_xml(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")


def _extract_doc_uids_from_context(context: str) -> list[str]:
    doc_uids: list[str] = []
    for match in re.finditer(r'<Document\s+[^>]*name="([^"]+)"[^>]*>', context):
        doc_uid = match.group(1)
        if doc_uid not in doc_uids:
            doc_uids.append(doc_uid)
    return doc_uids


def _build_chunk_summary(results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> str:
    if not results:
        return "Retrieved chunks:\n- none"
    summaries = build_output_document_sections(results=results, doc_chunks=doc_chunks, logger=logger)
    lines: list[str] = ["Retrieved chunks:"]
    for summary in summaries:
        sections_text = ", ".join(summary.section_labels) if summary.section_labels else "(no sections)"
        lines.append(f"- {summary.doc_uid}: {sections_text}")
    return "\n".join(lines)
