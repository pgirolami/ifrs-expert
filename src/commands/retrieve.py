"""Retrieve command - run the shared retrieval pipeline without invoking the LLM."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.commands.constants import DEFAULT_D, DEFAULT_EXPAND, DEFAULT_FULL_DOC_THRESHOLD, DEFAULT_MIN_SCORE, DEFAULT_MIN_SCORE_FOR_DOCUMENTS, DEFAULT_RETRIEVAL_K, DEFAULT_VERBOSE
from src.db import ChunkStore, SectionStore, init_db
from src.retrieval.models import RetrievalRequest, RetrievalResult
from src.retrieval.pipeline import RetrievalPipelineConfig, execute_retrieval
from src.vector.document_store import DocumentVectorStore, get_document_index_path
from src.vector.store import VectorStore, get_index_path
from src.vector.title_store import TitleVectorStore, get_title_index_path

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from src.interfaces import ReadChunkStoreProtocol, ReadSectionStoreProtocol, SearchDocumentVectorStoreProtocol, SearchResult, SearchTitleVectorStoreProtocol, SearchVectorStoreProtocol
    from src.models.chunk import Chunk

logger = logging.getLogger(__name__)

RELEVANCE_HIGH_THRESHOLD = 0.3


@dataclass(frozen=True)
class RetrieveConfig:
    """Configuration for RetrieveCommand."""

    vector_store: SearchVectorStoreProtocol
    chunk_store: ReadChunkStoreProtocol
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[], Path]
    section_store: ReadSectionStoreProtocol | None = None
    title_vector_store: SearchTitleVectorStoreProtocol | None = None
    title_index_path_fn: Callable[[], Path] | None = None
    document_vector_store: SearchDocumentVectorStoreProtocol | None = None
    document_index_path_fn: Callable[[], Path] | None = None


@dataclass(frozen=True)
class RetrieveOptions:
    """Options for the retrieve command."""

    k: int = DEFAULT_RETRIEVAL_K
    d: int = DEFAULT_D
    doc_min_score: float | None = DEFAULT_MIN_SCORE_FOR_DOCUMENTS
    content_min_score: float | None = DEFAULT_MIN_SCORE
    verbose: bool = DEFAULT_VERBOSE
    expand: int = DEFAULT_EXPAND
    full_doc_threshold: int = DEFAULT_FULL_DOC_THRESHOLD
    retrieval_mode: str = "text"


class RetrieveCommand:
    """Run the shared retrieval pipeline and format the retrieved chunks."""

    def __init__(
        self,
        query: str,
        config: RetrieveConfig,
        options: RetrieveOptions | None = None,
    ) -> None:
        """Initialize the retrieve command."""
        self.query = query
        self._config = config
        self._options = options or RetrieveOptions()

    def execute(self) -> str:
        """Execute retrieval and return formatted output."""
        validation_error = self._get_validation_error()
        if validation_error is not None:
            return validation_error

        retrieval_request = RetrievalRequest(
            query=self.query,
            retrieval_mode=self._options.retrieval_mode,
            k=self._options.k,
            d=self._options.d,
            doc_min_score=self._options.doc_min_score if self._options.doc_min_score is not None else DEFAULT_MIN_SCORE_FOR_DOCUMENTS,
            content_min_score=self._options.content_min_score if self._options.content_min_score is not None else DEFAULT_MIN_SCORE,
            expand=self._options.expand,
            full_doc_threshold=self._options.full_doc_threshold,
        )
        error, retrieval_result = execute_retrieval(
            request=retrieval_request,
            config=RetrievalPipelineConfig(
                vector_store=self._config.vector_store,
                chunk_store=self._config.chunk_store,
                init_db_fn=self._config.init_db_fn,
                index_path_fn=self._config.index_path_fn,
                section_store=self._config.section_store,
                title_vector_store=self._config.title_vector_store,
                title_index_path_fn=self._config.title_index_path_fn,
                document_vector_store=self._config.document_vector_store,
                document_index_path_fn=self._config.document_index_path_fn,
            ),
        )
        if error is not None:
            return error
        if retrieval_result is None:
            return "Error: Retrieval did not return a result"

        if self._options.verbose:
            return f"{self._options}\n{self._build_verbose_output(retrieval_result)}"
        return json.dumps(self._build_json_output(retrieval_result), indent=2, ensure_ascii=False)

    def _get_validation_error(self) -> str | None:
        error: str | None = None
        if not self.query or not self.query.strip():
            error = "Error: Query cannot be empty"
        elif self._options.k <= 0:
            error = "Error: k must be > 0"
        elif self._options.d <= 0:
            error = "Error: d must be > 0"
        elif self._options.expand < 0:
            error = "Error: expand must be >= 0"
        elif self._options.full_doc_threshold < 0:
            error = "Error: full_doc_threshold must be >= 0"
        elif self._options.retrieval_mode not in {"text", "titles", "documents"}:
            error = "Error: retrieval_mode must be 'text', 'titles', or 'documents'"
        return error

    def _build_json_output(self, retrieval_result: RetrievalResult) -> dict[str, object]:
        return {
            "retrieval_mode": retrieval_result.retrieval_mode,
            "document_hits": [{"doc_uid": document_hit.doc_uid, "score": round(document_hit.score, 4)} for document_hit in retrieval_result.document_hits],
            "chunks": _build_chunk_json_output(
                results=retrieval_result.chunk_results,
                doc_chunks=retrieval_result.doc_chunks,
            ),
        }

    def _build_verbose_output(self, retrieval_result: RetrievalResult) -> str:
        lines: list[str] = []
        if retrieval_result.document_hits:
            lines.append("Selected documents:")
            lines.extend(f"- {document_hit.doc_uid}: {document_hit.score:.4f}" for document_hit in retrieval_result.document_hits)
        chunk_lines = _build_chunk_verbose_output(
            results=retrieval_result.chunk_results,
            doc_chunks=retrieval_result.doc_chunks,
        )
        if chunk_lines:
            lines.append("Retrieved chunks:")
            lines.extend(chunk_lines)
        return "\n".join(lines)


def _build_chunk_json_output(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
) -> list[dict[str, object]]:
    chunks_output: list[dict[str, object]] = []
    for result in results:
        doc_uid = str(result["doc_uid"])
        chunk_id = int(result["chunk_id"])
        score = float(result["score"])
        for chunk in doc_chunks.get(doc_uid, []):
            if chunk.id != chunk_id:
                continue
            relevance = "High" if score >= RELEVANCE_HIGH_THRESHOLD else "Low"
            chunks_output.append(
                {
                    "id": chunk.id,
                    "doc_uid": chunk.doc_uid,
                    "chunk_number": chunk.chunk_number,
                    "chunk_id": chunk.chunk_id,
                    "containing_section_id": chunk.containing_section_id,
                    "page_start": chunk.page_start,
                    "page_end": chunk.page_end,
                    "text": chunk.text,
                    "score": round(score, 4),
                    "relevance": relevance,
                }
            )
            break
    return chunks_output


def _build_chunk_verbose_output(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
) -> list[str]:
    output_lines: list[str] = []
    for result in results:
        doc_uid = str(result["doc_uid"])
        chunk_id = int(result["chunk_id"])
        score = float(result["score"])
        for chunk in doc_chunks.get(doc_uid, []):
            if chunk.id != chunk_id:
                continue
            relevance = "High" if score >= RELEVANCE_HIGH_THRESHOLD else "Low"
            snippet = chunk.text[:200].replace("\n", " ")
            output_lines.append(f"\n--- Score: {score:.4f} ({relevance}) ---")
            output_lines.append(f"Document: {chunk.doc_uid}")
            output_lines.append(f"Chunk number: {chunk.chunk_number}")
            output_lines.append(f"Page: {chunk.page_start}-{chunk.page_end}")
            output_lines.append(f"Snippet: {snippet}...")
            break
    return output_lines


def create_retrieve_command(
    query: str,
    options: RetrieveOptions | None = None,
) -> RetrieveCommand:
    """Create RetrieveCommand with real dependencies."""
    config = RetrieveConfig(
        vector_store=VectorStore(),
        chunk_store=ChunkStore(),
        init_db_fn=init_db,
        index_path_fn=get_index_path,
        section_store=SectionStore(),
        title_vector_store=TitleVectorStore(),
        title_index_path_fn=get_title_index_path,
        document_vector_store=DocumentVectorStore(),
        document_index_path_fn=get_document_index_path,
    )
    return RetrieveCommand(query=query, config=config, options=options)
