"""Shared retrieval request and result models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.commands.constants import DEFAULT_D, DEFAULT_EXPAND, DEFAULT_FULL_DOC_THRESHOLD, DEFAULT_MIN_SCORE, DEFAULT_MIN_SCORE_FOR_DOCUMENTS, DEFAULT_RETRIEVAL_K

if TYPE_CHECKING:
    from src.interfaces import SearchResult
    from src.models.chunk import Chunk


@dataclass(frozen=True)
class RetrievalRequest:
    """One retrieval request passed into the shared pipeline."""

    query: str
    retrieval_mode: str = "text"
    k: int = DEFAULT_RETRIEVAL_K
    d: int = DEFAULT_D
    doc_min_score: float = DEFAULT_MIN_SCORE_FOR_DOCUMENTS
    content_min_score: float = DEFAULT_MIN_SCORE
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
