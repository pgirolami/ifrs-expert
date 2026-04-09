"""Shared retrieval request and result models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from src.commands.constants import DEFAULT_EXPAND, DEFAULT_FULL_DOC_THRESHOLD, DEFAULT_RETRIEVAL_K, DEFAULT_RETRIEVE_CONTENT_MIN_SCORE, DEFAULT_RETRIEVE_DOCUMENT_D, get_default_document_d_by_type, get_default_document_min_score_by_type

if TYPE_CHECKING:
    from src.interfaces import SearchResult
    from src.models.chunk import Chunk


@dataclass(frozen=True)
class RetrievalRequest:
    """One retrieval request passed into the shared pipeline."""

    query: str
    retrieval_mode: str = "text"
    k: int = DEFAULT_RETRIEVAL_K
    d: int = DEFAULT_RETRIEVE_DOCUMENT_D
    doc_min_score: float | None = None
    document_d_by_type: dict[str, int] = field(default_factory=get_default_document_d_by_type)
    document_min_score_by_type: dict[str, float] = field(default_factory=get_default_document_min_score_by_type)
    content_min_score: float = DEFAULT_RETRIEVE_CONTENT_MIN_SCORE
    expand_to_section: bool = False
    expand: int = DEFAULT_EXPAND
    full_doc_threshold: int = DEFAULT_FULL_DOC_THRESHOLD


@dataclass(frozen=True)
class DocumentHit:
    """One selected document-stage hit."""

    doc_uid: str
    score: float


@dataclass(frozen=True)
class RetrievalResult:
    """Shared retrieval result used by query, retrieve, and answer."""

    retrieval_mode: str
    document_hits: list[DocumentHit]
    chunk_results: list[SearchResult]
    doc_chunks: dict[str, list[Chunk]]

    @property
    def retrieved_doc_uids(self) -> list[str]:
        """Return document UIDs in first-appearance order from final chunk results."""
        return list(dict.fromkeys(result["doc_uid"] for result in self.chunk_results))
