"""Retrieve command - run the shared retrieval pipeline without invoking the LLM."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.commands.constants import DEFAULT_VERBOSE
from src.commands.document_output import build_output_document_sections
from src.commands.retrieval_request_builder import build_retrieval_request
from src.db import ChunkStore, ContentReferenceStore, SectionStore, init_db
from src.models.document import infer_document_kind, infer_exact_document_type, resolve_document_kind_from_document_type
from src.policy import RetrievalPolicy
from src.retrieval.pipeline import RetrievalPipelineConfig, execute_retrieval
from src.vector.document_store import DocumentVectorStore, get_document_id_map_path, get_document_index_path
from src.vector.store import VectorStore, get_index_path
from src.vector.title_store import TitleVectorStore, get_title_index_path

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from src.interfaces import ReadChunkStoreProtocol, ReadSectionStoreProtocol, ReferenceStoreProtocol, SearchDocumentVectorStoreProtocol, SearchResult, SearchTitleVectorStoreProtocol, SearchVectorStoreProtocol
    from src.models.chunk import Chunk
    from src.policy import RetrievalPolicy
    from src.retrieval.models import RetrievalRequest, RetrievalResult

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
    reference_store: ReferenceStoreProtocol | None = None
    title_vector_store: SearchTitleVectorStoreProtocol | None = None
    title_index_path_fn: Callable[[], Path] | None = None
    document_vector_store: SearchDocumentVectorStoreProtocol | None = None
    document_vector_store_factory: Callable[[str], SearchDocumentVectorStoreProtocol] | None = None
    document_index_path_fn: Callable[[str], Path] | None = None


@dataclass(frozen=True)
class RetrieveOptions:
    """Options for the retrieve command."""

    policy: RetrievalPolicy
    verbose: bool = DEFAULT_VERBOSE


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
        if options is None:
            message = "RetrieveCommand requires options with a loaded policy"
            raise ValueError(message)
        self._options = options

    def execute(self) -> str:
        """Execute retrieval and return formatted output."""
        validation_error = self._get_validation_error()
        if validation_error is not None:
            return validation_error

        retrieval_request = self._build_retrieval_request()
        error, retrieval_result = execute_retrieval(
            request=retrieval_request,
            config=RetrievalPipelineConfig(
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
            ),
        )
        if error is not None:
            return error
        if retrieval_result is None:
            return "Error: Retrieval did not return a result"

        if self._options.verbose:
            return f"{self._options}\n{self._build_verbose_output(retrieval_result)}"
        return json.dumps(self._build_json_output(retrieval_result), indent=2, ensure_ascii=False)

    def _build_retrieval_request(self) -> RetrievalRequest:
        policy = self._options.policy
        chunk_min_score = policy.titles.min_score if policy.chunk_retrieval.mode == "title_similarity" else policy.text.min_score
        expand_to_section = policy.expand_to_section if policy.document_routing.source == "all_documents" else True
        return build_retrieval_request(
            query=self.query,
            policy=policy,
            chunk_min_score=chunk_min_score,
            expand_to_section=expand_to_section,
        )

    def _get_validation_error(self) -> str | None:
        validators = (
            self._get_query_validation_error,
            self._get_numeric_validation_error,
            self._get_policy_shape_validation_error,
        )
        for validator in validators:
            error = validator()
            if error is not None:
                return error
        return None

    def _get_query_validation_error(self) -> str | None:
        if self.query and self.query.strip():
            return None
        return "Error: Query cannot be empty"

    def _get_numeric_validation_error(self) -> str | None:
        policy = self._options.policy
        checks: tuple[tuple[str, int, int], ...] = (
            ("expand", policy.expand, 0),
            ("full_doc_threshold", policy.full_doc_threshold, 0),
        )
        for name, value, minimum in checks:
            if value >= minimum:
                continue
            operator = ">=" if minimum == 0 else ">"
            return f"Error: {name} must be {operator} {minimum}"
        return None

    def _get_policy_shape_validation_error(self) -> str | None:
        policy = self._options.policy
        if policy.document_routing.source not in {"all_documents", "top_chunk_results", "document_representation"}:
            return "Error: document_routing.source in policy must be 'all_documents', 'top_chunk_results', or 'document_representation'"
        if policy.chunk_retrieval.mode not in {"chunk_similarity", "title_similarity"}:
            return "Error: chunk_retrieval.mode in policy must be 'chunk_similarity' or 'title_similarity'"
        return None

    def _build_json_output(self, retrieval_result: RetrievalResult) -> dict[str, object]:
        build_output_document_sections(
            results=retrieval_result.chunk_results,
            doc_chunks=retrieval_result.doc_chunks,
            logger=logger,
        )
        return {
            "policy_name": retrieval_result.policy_name,
            "document_routing_source": retrieval_result.document_routing_source,
            "document_routing_post_processing": retrieval_result.document_routing_post_processing,
            "chunk_retrieval_mode": retrieval_result.chunk_retrieval_mode,
            "document_hits": [
                {
                    "doc_uid": document_hit.doc_uid,
                    "score": round(document_hit.score, 4),
                    "document_type": document_hit.document_type,
                    "document_kind": resolve_document_kind_from_document_type(document_hit.document_type),
                }
                for document_hit in retrieval_result.document_hits
            ],
            "chunks": _build_chunk_json_output(
                results=retrieval_result.chunk_results,
                doc_chunks=retrieval_result.doc_chunks,
            ),
        }

    def _build_verbose_output(self, retrieval_result: RetrievalResult) -> str:
        lines: list[str] = []
        if retrieval_result.document_hits:
            lines.append("Selected documents:")
            lines.extend(f"- {document_hit.doc_uid}: {document_hit.score:.4f} ({document_hit.document_type})" for document_hit in retrieval_result.document_hits)
        build_output_document_sections(
            results=retrieval_result.chunk_results,
            doc_chunks=retrieval_result.doc_chunks,
            logger=logger,
        )
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
        document_type = infer_exact_document_type(doc_uid)
        document_kind = infer_document_kind(doc_uid)
        for chunk in doc_chunks.get(doc_uid, []):
            if chunk.id != chunk_id:
                continue
            relevance = "High" if score >= RELEVANCE_HIGH_THRESHOLD else "Low"
            chunks_output.append(
                {
                    "id": chunk.id,
                    "doc_uid": chunk.doc_uid,
                    "document_type": document_type,
                    "document_kind": document_kind,
                    "chunk_number": chunk.chunk_number,
                    "chunk_id": chunk.chunk_id,
                    "containing_section_id": chunk.containing_section_id,
                    "containing_section_db_id": chunk.containing_section_db_id,
                    "page_start": chunk.page_start,
                    "page_end": chunk.page_end,
                    "text": chunk.text,
                    "score": round(score, 4),
                    "relevance": relevance,
                    "provenance": result.get("provenance", "similarity"),
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
        document_type = infer_exact_document_type(doc_uid)
        document_kind = infer_document_kind(doc_uid)
        for chunk in doc_chunks.get(doc_uid, []):
            if chunk.id != chunk_id:
                continue
            relevance = "High" if score >= RELEVANCE_HIGH_THRESHOLD else "Low"
            snippet = chunk.text[:200].replace("\n", " ")
            output_lines.append(f"\n--- Score: {score:.4f} ({relevance}) ---")
            output_lines.append(f"Provenance: {result.get('provenance', 'similarity')}")
            output_lines.append(f"Document: {chunk.doc_uid}")
            output_lines.append(f"Document type: {document_type}")
            output_lines.append(f"Document kind: {document_kind}")
            output_lines.append(f"Chunk number: {chunk.chunk_number}")
            output_lines.append(f"Page: {chunk.page_start}-{chunk.page_end}")
            output_lines.append(f"Snippet: {snippet}...")
            break
    return output_lines


def create_retrieve_command(
    query: str,
    options: RetrieveOptions,
) -> RetrieveCommand:
    """Create RetrieveCommand with real dependencies."""
    config = RetrieveConfig(
        vector_store=VectorStore(),
        chunk_store=ChunkStore(),
        init_db_fn=init_db,
        index_path_fn=get_index_path,
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
    return RetrieveCommand(query=query, config=config, options=options)
