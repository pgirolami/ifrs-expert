"""Shared retrieval request and result models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.interfaces import SearchResult
    from src.models.chunk import Chunk


@dataclass(frozen=True)
class RetrievalRequest:
    """One retrieval request passed into the shared pipeline."""

    query: str
    retrieval_mode: str
    text_search_mode: str
    k: int
    d: int
    document_d_by_type: dict[str, int]
    document_min_score_by_type: dict[str, float]
    document_expand_to_section_by_type: dict[str, bool]
    chunk_min_score: float
    expand_to_section: bool
    expand: int
    full_doc_threshold: int
    top_k_initial: int
    top_k_final: int
    dense_weight: float
    sparse_weight: float
    multivector_weight: float
    score_normalization: str
    document_types: list[str] | None = None


@dataclass(frozen=True)
class DocumentHit:
    """One selected document-stage hit."""

    doc_uid: str
    score: float
    document_type: str


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
