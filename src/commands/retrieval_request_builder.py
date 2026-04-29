"""Shared helpers for building retrieval requests from policy settings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.retrieval.models import RetrievalRequest

if TYPE_CHECKING:
    from src.policy import RetrievalPolicy


@dataclass(frozen=True)
class RetrievalRequestOverrides:
    """Optional explicit routing overrides for special callers."""

    policy_name: str | None = None
    document_routing_source: str | None = None
    document_routing_post_processing: str | None = None
    chunk_retrieval_mode: str | None = None


def build_retrieval_request(
    *,
    query: str,
    policy: RetrievalPolicy,
    chunk_min_score: float,
    expand_to_section: bool,
    overrides: RetrievalRequestOverrides | None = None,
) -> RetrievalRequest:
    """Build a retrieval request that honors the policy query embedding mode."""
    expansion = policy.chunk_retrieval.profile_config.expansion
    reference_expansion = None if expansion is None else expansion.reference_expansion
    request_overrides = overrides or RetrievalRequestOverrides()
    return RetrievalRequest(
        query=query,
        query_embedding_mode=policy.query_embedding_mode,
        policy_name=request_overrides.policy_name or policy.policy_name,
        document_routing_source=request_overrides.document_routing_source or policy.document_routing.source,
        document_routing_post_processing=request_overrides.document_routing_post_processing or policy.document_routing.post_processing,
        chunk_retrieval_mode=request_overrides.chunk_retrieval_mode or policy.chunk_retrieval.mode,
        k=policy.k,
        d=policy.documents.global_d,
        document_d_by_type={document_type: document_policy.d for document_type, document_policy in policy.documents.by_document_type.items()},
        document_min_score_by_type={document_type: document_policy.min_score for document_type, document_policy in policy.documents.by_document_type.items()},
        document_expand_to_section_by_type={document_type: document_policy.expand_to_section for document_type, document_policy in policy.documents.by_document_type.items()},
        document_similarity_representation_by_type={document_type: document_policy.similarity_representation for document_type, document_policy in policy.documents.by_document_type.items()},
        chunk_min_score=chunk_min_score,
        expand_to_section=expand_to_section,
        expand=policy.expand,
        full_doc_threshold=policy.full_doc_threshold,
        reference_expand_enabled=reference_expansion.enabled if reference_expansion is not None else False,
        reference_expand_depth=reference_expansion.depth if reference_expansion is not None else 0,
        reference_expand_max_chunks_per_seed=reference_expansion.max_chunks_per_seed if reference_expansion is not None else 0,
        reference_expand_max_chunks_per_doc=reference_expansion.max_chunks_per_doc if reference_expansion is not None else 0,
    )
