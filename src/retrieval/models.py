"""Shared retrieval request and result models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.interfaces import SearchResult
    from src.models.chunk import Chunk
    from src.policy import QueryEmbeddingMode


@dataclass(frozen=True)
class RetrievalRequest:
    """One retrieval request passed into the shared pipeline."""

    query: str
    query_embedding_mode: QueryEmbeddingMode
    policy_name: str
    document_routing_source: str
    document_routing_post_processing: str
    chunk_retrieval_mode: str
    k: int
    d: int
    document_d_by_type: dict[str, int]
    document_min_score_by_type: dict[str, float]
    document_expand_to_section_by_type: dict[str, bool]
    document_similarity_representation_by_type: dict[str, str]
    chunk_min_score: float
    expand_to_section: bool
    expand: int
    full_doc_threshold: int
    reference_expand_enabled: bool = False
    reference_expand_depth: int = 0
    reference_expand_max_chunks_per_seed: int = 0
    reference_expand_max_chunks_per_doc: int = 0


@dataclass(frozen=True)
class DocumentHit:
    """One selected document-stage hit."""

    doc_uid: str
    score: float
    document_type: str


@dataclass(frozen=True)
class RetrievalResult:
    """Shared retrieval result used by query, retrieve, and answer."""

    policy_name: str
    document_routing_source: str
    document_routing_post_processing: str
    chunk_retrieval_mode: str
    document_hits: list[DocumentHit]
    chunk_results: list[SearchResult]
    doc_chunks: dict[str, list[Chunk]]

    @property
    def retrieved_doc_uids(self) -> list[str]:
        """Return document UIDs in first-appearance order from final chunk results."""
        return list(dict.fromkeys(result["doc_uid"] for result in self.chunk_results))
