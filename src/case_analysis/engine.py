"""Case-analysis answer engine and rendering helpers."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Protocol

from src.case_analysis.context_builder import ContextBuilder
from src.case_analysis.graph import CaseAnalysisGraphRunner
from src.case_analysis.workflow import AnswerWorkflowProcessor, _build_output_document_sections
from src.models.answer_command_result import AnswerCommandResult
from src.retrieval.pipeline import RetrievalPipelineConfig, execute_retrieval

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.case_analysis.models import ApproachIdentificationOutput
    from src.case_analysis.stages import AnswerGeneratorProtocol, ExecuteRetrievalFn
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
        self.policy = policy
        self.config = config
        self._hooks = hooks or AnswerEngineHooks()
        self._workflow_processor = AnswerWorkflowProcessor(
            query=self.query,
            policy=self.policy,
            read_prompt_template_fn=self._hooks.read_prompt_template_fn,
            approach_identification_path=APPROACH_IDENTIFICATION_PATH,
            applicability_analysis_path=APPLICABILITY_ANALYSIS_PATH,
            answer_generator=self.config.answer_generator,
        )

    def run(self) -> AnswerCommandResult:
        """Run prerequisite checks and the deterministic case-analysis graph."""
        prerequisite_error = self.get_prerequisite_error()
        if prerequisite_error is not None:
            return AnswerCommandResult.failure(query=self.query, error=prerequisite_error, error_stage="prerequisite")

        runner = CaseAnalysisGraphRunner(
            policy=self.policy,
            pipeline_config=self._build_retrieval_pipeline_config(),
            execute_retrieval_fn=self._hooks.execute_retrieval_fn,
            build_answer_result_fn=self._workflow_processor.build_answer_result_from_source_package,
            process_prompts_fn=self._workflow_processor.process_source_package_prompts,
        )
        return runner.run(self.query)

    def get_prerequisite_error(self) -> str | None:
        """Return a CLI/runtime prerequisite error, if any."""
        prompt_error = self._get_prompt_template_error()
        if prompt_error is not None:
            return prompt_error

        if self.policy.document_routing.source == "all_documents" and self.policy.chunk_retrieval.mode == "title_similarity":
            return self._get_title_prerequisite_error()
        if self.policy.document_routing.source == "document_representation":
            document_prerequisite_error = self._get_document_prerequisite_error()
            if document_prerequisite_error is not None:
                return document_prerequisite_error

        index_path = self.config.index_path_fn()
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
        if self.config.title_index_path_fn is None:
            return "Error: Title retrieval is not configured."
        title_index_path = self.config.title_index_path_fn()
        if not title_index_path.exists():
            logger.error(f"Missing title vector index at {title_index_path}; corpus must be built before running the answer pipeline")
            return "Error: No title index found. Please run 'store' command first."
        return None

    def _get_document_prerequisite_error(self) -> str | None:
        if self.config.document_index_path_fn is None:
            return "Error: Document retrieval is not configured."
        required_representations = sorted({document_policy.similarity_representation for document_policy in self.policy.documents.by_document_type.values()})
        for representation in required_representations:
            try:
                document_index_path = self.config.document_index_path_fn(representation)
            except TypeError:
                document_index_path = self.config.document_index_path_fn()  # type: ignore[call-arg]
            if document_index_path.exists():
                continue
            logger.error(f"Missing document vector index at {document_index_path} for representation={representation}; corpus must be built before running the answer pipeline")
            return "Error: No document index found. Please run 'store' command first."
        return None

    def _build_retrieval_pipeline_config(self) -> RetrievalPipelineConfig:
        return RetrievalPipelineConfig(
            vector_store=self.config.vector_store,
            chunk_store=self.config.chunk_store,
            init_db_fn=self.config.init_db_fn,
            index_path_fn=self.config.index_path_fn,
            section_store=self.config.section_store,
            reference_store=self.config.reference_store,
            title_vector_store=self.config.title_vector_store,
            title_index_path_fn=self.config.title_index_path_fn,
            document_vector_store=self.config.document_vector_store,
            document_vector_store_factory=self.config.document_vector_store_factory,
            document_index_path_fn=self.config.document_index_path_fn,
        )


def _build_applicability_analysis_context(formatted_chunks: list[str], approach_identification_output: ApproachIdentificationOutput) -> str:
    return ContextBuilder().build_applicability_analysis_context(formatted_chunks, approach_identification_output)


def _extract_authority_references(approach_identification_output: ApproachIdentificationOutput) -> set[tuple[str, str]] | None:
    return ContextBuilder().extract_authority_references(approach_identification_output)


def _filter_chunks_by_authority(formatted_chunks: list[str], authority_refs: set[tuple[str, str]]) -> str:
    return ContextBuilder().filter_chunks_by_authority(formatted_chunks, authority_refs)


def _escape_xml(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")


def _build_chunk_summary(results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> str:
    if not results:
        return "Retrieved chunks:\n- none"
    summaries = _build_output_document_sections(results=results, doc_chunks=doc_chunks, logger=logger)
    lines: list[str] = ["Retrieved chunks:"]
    for summary in summaries:
        sections_text = ", ".join(summary.section_labels) if summary.section_labels else "(no sections)"
        lines.append(f"- {summary.doc_uid}: {sections_text}")
    return "\n".join(lines)


def _extract_doc_uids_from_context(context: str) -> list[str]:
    doc_uids: list[str] = []
    for match in re.finditer(r'<Document\s+[^>]*name="([^"]+)"[^>]*>', context):
        doc_uid = match.group(1)
        if doc_uid not in doc_uids:
            doc_uids.append(doc_uid)
    return doc_uids
