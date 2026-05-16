"""Answer command adapter for the case-analysis engine."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.ai.pydantic_client import PydanticAIAnswerGenerator, create_default_answer_generator
from src.case_analysis.engine import AnswerEngine, AnswerEngineHooks, _build_applicability_analysis_context, _build_chunk_summary, _prompt_file_exists, _read_prompt_template
from src.case_analysis.models import ApproachIdentificationOutput, ValidationFailure
from src.case_analysis.stages import AnswerGeneratorProtocol, ValidateQuestionStage
from src.commands.constants import DEFAULT_VERBOSE
from src.db import ChunkStore, ContentReferenceStore, SectionStore, init_db
from src.models.answer_command_result import AnswerCommandResult
from src.retrieval.pipeline import execute_retrieval
from src.vector.document_store import DocumentVectorStore, get_document_id_map_path, get_document_index_path
from src.vector.store import VectorStore, get_index_path
from src.vector.title_store import TitleVectorStore, get_title_index_path

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

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


@dataclass
class AnswerConfig:
    """Runtime dependencies for AnswerCommand."""

    vector_store: SearchVectorStoreProtocol
    chunk_store: ReadChunkStoreProtocol
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[], Path]
    answer_generator: AnswerGeneratorProtocol
    section_store: ReadSectionStoreProtocol | None = None
    reference_store: ReferenceStoreProtocol | None = None
    title_vector_store: SearchTitleVectorStoreProtocol | None = None
    title_index_path_fn: Callable[[], Path] | None = None
    document_vector_store: SearchDocumentVectorStoreProtocol | None = None
    document_vector_store_factory: Callable[[str], SearchDocumentVectorStoreProtocol] | None = None
    document_index_path_fn: Callable[[str], Path] | None = None


@dataclass
class AnswerOptions:
    """Options for answer command."""

    policy: RetrievalPolicy
    verbose: bool = DEFAULT_VERBOSE
    output_dir: Path | None = None


class AnswerCommand:
    """Thin adapter that validates command options and runs the answer engine."""

    def __init__(
        self,
        query: str,
        config: AnswerConfig,
        options: AnswerOptions | None = None,
    ) -> None:
        """Initialize the command with query, dependencies, and options."""
        if options is None:
            message = "AnswerCommand requires options with a loaded policy"
            raise ValueError(message)
        self.query = query
        self._config = config
        self._options = options
        self.output_dir = options.output_dir
        self.verbose = options.verbose

    def execute(self) -> AnswerCommandResult:
        """Execute the answer workflow and return public artifacts."""
        policy = self._options.policy
        logger.info(f"AnswerCommand(query='{self.query[:50]}', k={policy.k}, expand={policy.expand}, f={policy.full_doc_threshold}, min-score={policy.text.min_score})")
        validation_result = ValidateQuestionStage().execute(query=self.query, policy=policy)
        if isinstance(validation_result, ValidationFailure):
            return AnswerCommandResult.failure(query=self.query, error=validation_result.message, error_stage=validation_result.error_stage)
        self.query = validation_result.question
        return self._build_engine().run()

    def _build_engine(self) -> AnswerEngine:
        """Build the case-analysis engine directly."""
        hooks = AnswerEngineHooks(
            execute_retrieval_fn=execute_retrieval,
            prompt_file_exists_fn=_prompt_file_exists,
            read_prompt_template_fn=_read_prompt_template,
        )
        return AnswerEngine(query=self.query, policy=self._options.policy, config=self._config, hooks=hooks)

    def _build_applicability_analysis_context(self, formatted_chunks: list[str], approach_identification_output: ApproachIdentificationOutput | dict[str, object]) -> str:
        """Build applicability analysis context for tests and the rendering path."""
        return _build_applicability_analysis_context(formatted_chunks, approach_identification_output)

    def _build_chunk_summary(self, results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> str:
        """Build chunk summary for tests and internal rendering."""
        return _build_chunk_summary(results, doc_chunks)


def _default_answer_generator() -> PydanticAIAnswerGenerator:
    """Create the configured Pydantic AI answer generator."""
    try:
        return create_default_answer_generator()
    except ValueError as e:
        error_msg = f"Pydantic AI LLM not configured: {e}"
        raise RuntimeError(error_msg) from e


def create_answer_command(
    query: str,
    options: AnswerOptions,
) -> AnswerCommand:
    """Create AnswerCommand with real dependencies."""
    config = AnswerConfig(
        vector_store=VectorStore(),
        chunk_store=ChunkStore(),
        init_db_fn=init_db,
        index_path_fn=get_index_path,
        answer_generator=_default_answer_generator(),  # ty: ignore[invalid-argument-type]
        reference_store=ContentReferenceStore(),
        section_store=SectionStore(),
        title_vector_store=TitleVectorStore(),
        title_index_path_fn=get_title_index_path,
        document_vector_store=DocumentVectorStore(),
        document_vector_store_factory=lambda representation: DocumentVectorStore(
            index_path=get_document_index_path(representation),
            id_map_path=get_document_id_map_path(representation),
        ),
        document_index_path_fn=get_document_index_path,
    )
    return AnswerCommand(query=query, config=config, options=options)
