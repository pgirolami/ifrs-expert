"""Shared helpers for building retrieval requests from policy settings."""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.retrieval.models import RetrievalRequest

if TYPE_CHECKING:
    from src.policy import RetrievalPolicy


def build_retrieval_request(
    *,
    query: str,
    policy: RetrievalPolicy,
    retrieval_mode: str,
    chunk_min_score: float,
    expand_to_section: bool,
) -> RetrievalRequest:
    """Build a retrieval request that honors the policy query embedding mode."""
    return RetrievalRequest(
        query=query,
        query_embedding_mode=policy.query_embedding_mode,
        retrieval_mode=retrieval_mode,
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
    )
