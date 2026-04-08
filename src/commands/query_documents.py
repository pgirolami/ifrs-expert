"""Query documents command - search for similar documents using text query."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.commands.constants import DEFAULT_MIN_SCORE, DEFAULT_VERBOSE
from src.db import DocumentStore, init_db
from src.vector.document_store import DocumentVectorStore, get_document_index_path

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from src.interfaces import DocumentSearchResult, DocumentStoreProtocol, SearchDocumentVectorStoreProtocol
    from src.models.document import DocumentRecord

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class QueryDocumentsConfig:
    """Configuration for QueryDocumentsCommand."""

    document_vector_store: SearchDocumentVectorStoreProtocol
    document_store: DocumentStoreProtocol
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[], Path]


@dataclass(frozen=True)
class QueryDocumentsOptions:
    """Options for the query-documents command."""

    d: int = 5
    min_score: float | None = DEFAULT_MIN_SCORE
    verbose: bool = DEFAULT_VERBOSE


class QueryDocumentsCommand:
    """Search for similar documents using document-level embeddings."""

    def __init__(
        self,
        query: str,
        config: QueryDocumentsConfig,
        options: QueryDocumentsOptions | None = None,
    ) -> None:
        """Initialize the query-documents command."""
        self.query = query
        self._config = config
        self._options = options or QueryDocumentsOptions()

    def execute(self) -> str:
        """Execute the document-search workflow and return formatted results."""
        validation_error = self._get_validation_error()
        if validation_error is not None:
            return validation_error

        prerequisite_error = self._get_prerequisite_error()
        if prerequisite_error is not None:
            return prerequisite_error

        min_score = self._options.min_score if self._options.min_score is not None else DEFAULT_MIN_SCORE
        with self._config.document_vector_store as document_vector_store:
            ranked_results = document_vector_store.search_all(self.query)

        selected_results = _select_top_documents(ranked_results=ranked_results, d=self._options.d, min_score=min_score)
        if not selected_results:
            return f"Error: No documents found with score >= {min_score}"

        self._config.init_db_fn()
        documents = self._fetch_documents(selected_results)
        if not self._options.verbose:
            return json.dumps(_build_json_output(selected_results, documents), indent=2, ensure_ascii=False)
        return _build_verbose_output(selected_results, documents)

    def _get_validation_error(self) -> str | None:
        if not self.query or not self.query.strip():
            return "Error: Query cannot be empty"
        if self._options.d <= 0:
            return "Error: d must be > 0"
        return None

    def _get_prerequisite_error(self) -> str | None:
        index_path = self._config.index_path_fn()
        if not index_path.exists():
            logger.error(f"Missing document vector index at {index_path}; corpus must be built before running queries")
            return "Error: No document index found. Please run 'store' command first."
        return None

    def _fetch_documents(self, selected_results: list[DocumentSearchResult]) -> dict[str, DocumentRecord]:
        documents_by_uid: dict[str, DocumentRecord] = {}
        with self._config.document_store as document_store:
            for result in selected_results:
                document = document_store.get_document(result["doc_uid"])
                if document is not None:
                    documents_by_uid[result["doc_uid"]] = document
        return documents_by_uid


def _select_top_documents(
    ranked_results: list[DocumentSearchResult],
    d: int,
    min_score: float,
) -> list[DocumentSearchResult]:
    selected_results: list[DocumentSearchResult] = []
    for result in ranked_results:
        if result["score"] < min_score:
            continue
        selected_results.append(result)
        if len(selected_results) >= d:
            break
    return selected_results


def _build_json_output(
    selected_results: list[DocumentSearchResult],
    documents_by_uid: dict[str, DocumentRecord],
) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for result in selected_results:
        document = documents_by_uid.get(result["doc_uid"])
        if document is None:
            continue
        output.append(
            {
                "doc_uid": document.doc_uid,
                "source_type": document.source_type,
                "source_title": document.source_title,
                "source_url": document.source_url,
                "canonical_url": document.canonical_url,
                "captured_at": document.captured_at,
                "background_text": document.background_text,
                "issue_text": document.issue_text,
                "objective_text": document.objective_text,
                "scope_text": document.scope_text,
                "intro_text": document.intro_text,
                "score": round(result["score"], 4),
            }
        )
    return output


def _build_verbose_output(
    selected_results: list[DocumentSearchResult],
    documents_by_uid: dict[str, DocumentRecord],
) -> str:
    output_lines: list[str] = []
    for result in selected_results:
        document = documents_by_uid.get(result["doc_uid"])
        if document is None:
            continue
        preview_text = next(
            (
                value
                for value in (
                    document.background_text,
                    document.issue_text,
                    document.objective_text,
                    document.scope_text,
                    document.intro_text,
                )
                if value
            ),
            "",
        )
        snippet = preview_text[:200].replace("\n", " ")
        output_lines.append(f"\n--- Score: {result['score']:.4f} ---")
        output_lines.append(f"Document: {document.doc_uid}")
        output_lines.append(f"Title: {document.source_title}")
        if snippet:
            output_lines.append(f"Snippet: {snippet}...")
    return "\n".join(output_lines)


def create_query_documents_command(
    query: str,
    options: QueryDocumentsOptions | None = None,
) -> QueryDocumentsCommand:
    """Create QueryDocumentsCommand with real dependencies."""
    config = QueryDocumentsConfig(
        document_vector_store=DocumentVectorStore(),
        document_store=DocumentStore(),
        init_db_fn=init_db,
        index_path_fn=get_document_index_path,
    )
    return QueryDocumentsCommand(query=query, config=config, options=options)
