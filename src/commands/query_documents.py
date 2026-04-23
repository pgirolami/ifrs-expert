"""Query documents command - search for similar documents using text query."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.commands.constants import DEFAULT_VERBOSE
from src.db import DocumentStore, init_db
from src.models.document import DOCUMENT_TYPES, infer_persisted_document_type
from src.vector.document_store import DocumentVectorStore, get_document_id_map_path, get_document_index_path

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from src.interfaces import DocumentSearchResult, DocumentStoreProtocol, SearchDocumentVectorStoreProtocol
    from src.models.document import DocumentRecord
    from src.policy import RetrievalPolicy

logger = logging.getLogger(__name__)

VERBOSE_TEXT_PREVIEW_CHARS = 160
DOCUMENT_REPRESENTATION_FIELDS: tuple[tuple[str, str], ...] = (
    ("background_text", "Background"),
    ("issue_text", "Issue"),
    ("objective_text", "Objective"),
    ("scope_text", "Scope"),
    ("intro_text", "Introduction"),
    ("toc_text", "TOC"),
)


@dataclass(frozen=True)
class QueryDocumentsConfig:
    """Configuration for QueryDocumentsCommand."""

    document_store: DocumentStoreProtocol
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[str], Path]
    document_vector_store_factory: Callable[[str], SearchDocumentVectorStoreProtocol] | None = None
    document_vector_store: SearchDocumentVectorStoreProtocol | None = None


@dataclass(frozen=True)
class QueryDocumentsOptions:
    """Options for the query-documents command."""

    policy: RetrievalPolicy
    document_type: str
    verbose: bool = DEFAULT_VERBOSE


class QueryDocumentsCommand:
    """Search for similar documents using document-level embeddings."""

    def __init__(
        self,
        query: str,
        config: QueryDocumentsConfig,
        options: QueryDocumentsOptions,
    ) -> None:
        """Initialize the query-documents command."""
        self.query = query
        self._config = config
        self._options = options

    def execute(self) -> str:
        """Execute the document-search workflow and return formatted results."""
        validation_error = self._get_validation_error()
        if validation_error is not None:
            return validation_error

        prerequisite_error = self._get_prerequisite_error()
        if prerequisite_error is not None:
            return prerequisite_error

        document_policy = self._options.policy.documents.by_document_type[self._options.document_type]
        similarity_representation = document_policy.similarity_representation or "full"
        vector_store = self._get_document_vector_store(similarity_representation)
        with vector_store as document_vector_store:
            ranked_results = document_vector_store.search_all(self.query)

        selected_results = _select_top_documents(
            ranked_results=ranked_results,
            document_type=self._options.document_type,
            d=document_policy.d,
            min_score=document_policy.min_score,
        )
        if not selected_results:
            return f"Error: No {self._options.document_type} documents found with score >= {document_policy.min_score}"

        self._config.init_db_fn()
        documents = self._fetch_documents(selected_results)
        if not self._options.verbose:
            return json.dumps(_build_json_output(selected_results, documents), indent=2, ensure_ascii=False)
        return f"{self._options}\n{_build_verbose_output(selected_results, documents)}"

    def _get_validation_error(self) -> str | None:
        if not self.query or not self.query.strip():
            return "Error: Query cannot be empty"
        if self._options.document_type not in DOCUMENT_TYPES:
            supported_document_types = ", ".join(DOCUMENT_TYPES)
            return f"Error: document_type must be one of {supported_document_types}"
        document_policy = self._options.policy.documents.by_document_type.get(self._options.document_type)
        if document_policy is None:
            return f"Error: Missing policy entry for document_type={self._options.document_type}"
        if document_policy.d <= 0:
            return "Error: d must be > 0"
        return None

    def _get_prerequisite_error(self) -> str | None:
        document_policy = self._options.policy.documents.by_document_type[self._options.document_type]
        try:
            index_path = self._config.index_path_fn(document_policy.similarity_representation or "full")
        except TypeError:
            index_path = self._config.index_path_fn()  # type: ignore[call-arg]
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

    def _get_document_vector_store(self, representation: str) -> SearchDocumentVectorStoreProtocol:
        document_vector_store_factory = self._config.document_vector_store_factory
        if document_vector_store_factory is not None:
            return document_vector_store_factory(representation)
        document_vector_store = self._config.document_vector_store
        if document_vector_store is not None:
            return document_vector_store
        message = "Error: Document retrieval is not configured."
        raise RuntimeError(message)


def _select_top_documents(
    ranked_results: list[DocumentSearchResult],
    document_type: str,
    d: int,
    min_score: float,
) -> list[DocumentSearchResult]:
    selected_results: list[DocumentSearchResult] = []
    for result in ranked_results:
        if result["score"] < min_score:
            continue
        if infer_persisted_document_type(result["doc_uid"]) != document_type:
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
                "document_type": document.document_type,
                "document_kind": document.document_kind,
                "background_text": document.background_text,
                "issue_text": document.issue_text,
                "objective_text": document.objective_text,
                "scope_text": document.scope_text,
                "intro_text": document.intro_text,
                "TOC": document.toc_text,
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
            (getattr(document, field_name) for field_name, _ in DOCUMENT_REPRESENTATION_FIELDS if getattr(document, field_name)),
            "",
        )
        snippet = _truncate_verbose_text(preview_text)
        output_lines.append(f"\n--- Score: {result['score']:.4f} ---")
        output_lines.append(f"Document: {document.doc_uid}")
        if document.document_type is not None:
            output_lines.append(f"Type: {document.document_type}")
        if document.document_kind is not None:
            output_lines.append(f"Kind: {document.document_kind}")
        output_lines.append(f"Title: {document.source_title}")
        if snippet:
            output_lines.append(f"Snippet: {snippet}")
        representation_lines = _build_document_representation_lines(document)
        if representation_lines:
            output_lines.append("Document representation:")
            output_lines.extend(representation_lines)
    return "\n".join(output_lines)


def _build_document_representation_lines(document: DocumentRecord) -> list[str]:
    lines: list[str] = []
    for field_name, label in DOCUMENT_REPRESENTATION_FIELDS:
        field_value = getattr(document, field_name)
        if field_value is None or not field_value.strip():
            continue
        lines.append(f"- {label}: {_truncate_verbose_text(field_value)}")
    return lines


def _truncate_verbose_text(text: str) -> str:
    normalized_text = " ".join(text.split())
    if len(normalized_text) <= VERBOSE_TEXT_PREVIEW_CHARS:
        return normalized_text
    return f"{normalized_text[:VERBOSE_TEXT_PREVIEW_CHARS]}..."


def create_query_documents_command(
    query: str,
    options: QueryDocumentsOptions,
) -> QueryDocumentsCommand:
    """Create QueryDocumentsCommand with real dependencies."""
    config = QueryDocumentsConfig(
        document_vector_store_factory=lambda representation: DocumentVectorStore(
            index_path=get_document_index_path(representation),
            id_map_path=get_document_id_map_path(representation),
        ),
        document_store=DocumentStore(),
        init_db_fn=init_db,
        index_path_fn=get_document_index_path,
    )
    return QueryDocumentsCommand(query=query, config=config, options=options)
