"""Shared retrieval pipeline for text, title, and document-first retrieval."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.retrieval.chunk_expansion import ExpansionConfig, _expand_chunks
from src.retrieval.chunk_search import _collect_doc_uids_for_chunk_expansion, _fetch_chunks, _search_chunks, _select_top_k_per_document
from src.retrieval.document_routing import (
    _aggregate_standard_document_scores,
    _get_chunk_index_error,
    _get_document_retrieval_prerequisite_error,
    _search_documents_by_representation,
    _select_top_d_documents,
)
from src.retrieval.models import RetrievalRequest, RetrievalResult
from src.retrieval.query_embedding import build_query_embedding_text
from src.retrieval.title_pipeline import _execute_title_retrieval

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from src.interfaces import (
        ReadChunkStoreProtocol,
        ReadSectionStoreProtocol,
        ReferenceStoreProtocol,
        SearchDocumentVectorStoreProtocol,
        SearchTitleVectorStoreProtocol,
        SearchVectorStoreProtocol,
    )

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class RetrievalPipelineConfig:
    """Dependencies required by the shared retrieval pipeline."""

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


def execute_retrieval(
    request: RetrievalRequest,
    config: RetrievalPipelineConfig,
) -> tuple[str | None, RetrievalResult | None]:
    """Execute the shared retrieval pipeline for one request."""
    query_for_embedding = _build_query_for_embedding(request)
    if request.document_routing_source == "all_documents" and request.chunk_retrieval_mode == "title_similarity":
        return _execute_title_retrieval(request=request, query_for_embedding=query_for_embedding, config=config)
    if request.document_routing_source == "document_representation":
        return _execute_document_retrieval(request=request, query_for_embedding=query_for_embedding, config=config)
    if request.document_routing_source == "top_chunk_results":
        return _execute_document_routing_through_chunks(request=request, query_for_embedding=query_for_embedding, config=config)
    if request.document_routing_source == "all_documents":
        return _execute_text_retrieval(request=request, query_for_embedding=query_for_embedding, config=config)
    message = f"Error: Unsupported document routing source: {request.document_routing_source}"
    logger.error(message)
    return message, None


def _build_query_for_embedding(request: RetrievalRequest) -> str:
    """Build the retrieval-time query text used for embeddings only."""
    if request.query_embedding_mode == "raw":
        logger.info(f"Prepared raw retrieval query for embedding; chars={len(request.query)}")
        return request.query

    query_for_embedding = build_query_embedding_text(request.query).embedding_text
    logger.info(f"Prepared enriched retrieval query for embedding; original_chars={len(request.query)}, embedded_chars={len(query_for_embedding)}")
    logger.info(f"Enriched query text being embedded:\n{query_for_embedding}")
    return query_for_embedding


def _execute_text_retrieval(
    request: RetrievalRequest,
    query_for_embedding: str,
    config: RetrievalPipelineConfig,
) -> tuple[str | None, RetrievalResult | None]:
    index_error = _get_chunk_index_error(config=config)
    if index_error is not None:
        return index_error, None

    ranked_results = _search_chunks(query=query_for_embedding, config=config)
    if not ranked_results:
        return "Error: No chunks retrieved", None

    selected_results = _select_top_k_per_document(
        ranked_results=ranked_results,
        k=request.k,
        min_score=request.chunk_min_score,
    )
    if not selected_results:
        return f"Error: No chunks found with score >= {request.chunk_min_score}", None

    doc_uids_to_fetch = _collect_doc_uids_for_chunk_expansion(selected_results, request)
    doc_chunks = _fetch_chunks(doc_uids=doc_uids_to_fetch, config=config)
    expanded_results = _expand_chunks(
        ranked_results=ranked_results,
        results=selected_results,
        doc_chunks=doc_chunks,
        expansion_config=ExpansionConfig(
            section_store=config.section_store,
            reference_store=config.reference_store,
            expand_to_section=request.expand_to_section,
            expand_to_section_doc_uids=None,
            expand=request.expand,
            full_doc_threshold=request.full_doc_threshold,
            reference_expand_enabled=request.reference_expand_enabled,
            reference_expand_depth=request.reference_expand_depth,
            reference_expand_max_chunks_per_seed=request.reference_expand_max_chunks_per_seed,
            reference_expand_max_chunks_per_doc=request.reference_expand_max_chunks_per_doc,
            reference_expand_section_max_chunks_per_target=request.reference_expand_section_max_chunks_per_target,
        ),
    )
    return (
        None,
        RetrievalResult(
            policy_name=request.policy_name,
            document_routing_source=request.document_routing_source,
            document_routing_post_processing=request.document_routing_post_processing,
            chunk_retrieval_mode=request.chunk_retrieval_mode,
            document_hits=[],
            chunk_results=expanded_results,
            doc_chunks=doc_chunks,
        ),
    )


def _execute_document_retrieval(  # noqa: PLR0911
    request: RetrievalRequest,
    query_for_embedding: str,
    config: RetrievalPipelineConfig,
) -> tuple[str | None, RetrievalResult | None]:
    prerequisite_error = _get_document_retrieval_prerequisite_error(config=config, request=request)
    if prerequisite_error is not None:
        return prerequisite_error, None

    ranked_document_results = _search_documents_by_representation(
        query=query_for_embedding,
        config=config,
        document_similarity_representation_by_type=request.document_similarity_representation_by_type,
        consolidate_variants_to_standard=request.document_routing_post_processing == "aggregate_to_main_variant",
    )

    if not ranked_document_results:
        return "Error: No documents retrieved", None

    document_selection_error, document_hits = _select_top_d_documents(
        ranked_results=ranked_document_results,
        d=request.d,
        document_d_by_type=request.document_d_by_type,
        document_min_score_by_type=request.document_min_score_by_type,
    )
    if document_selection_error is not None:
        return document_selection_error, None
    if not document_hits:
        return "Error: No documents found with the configured per-type score thresholds", None

    allowed_doc_uids = {hit.doc_uid for hit in document_hits}
    ranked_chunk_results = _search_chunks(query=query_for_embedding, config=config)
    if not ranked_chunk_results:
        return "Error: No chunks retrieved", None

    filtered_ranked_chunk_results = [result for result in ranked_chunk_results if result["doc_uid"] in allowed_doc_uids]
    selected_results = _select_top_k_per_document(
        ranked_results=filtered_ranked_chunk_results,
        k=request.k,
        min_score=request.chunk_min_score,
    )
    if not selected_results:
        return (
            f"Error: No chunks found in selected documents with score >= {request.chunk_min_score}",
            None,
        )

    doc_uids_to_fetch = _collect_doc_uids_for_chunk_expansion(selected_results, request)
    doc_chunks = _fetch_chunks(doc_uids=doc_uids_to_fetch, config=config)
    docs_to_expand_to_section = {document_hit.doc_uid for document_hit in document_hits if request.document_expand_to_section_by_type.get(document_hit.document_type, False)}
    expanded_results = _expand_chunks(
        ranked_results=filtered_ranked_chunk_results,
        results=selected_results,
        doc_chunks=doc_chunks,
        expansion_config=ExpansionConfig(
            section_store=config.section_store,
            reference_store=config.reference_store,
            expand_to_section=request.expand_to_section,
            expand_to_section_doc_uids=docs_to_expand_to_section,
            expand=request.expand,
            full_doc_threshold=request.full_doc_threshold,
            reference_expand_enabled=request.reference_expand_enabled,
            reference_expand_depth=request.reference_expand_depth,
            reference_expand_max_chunks_per_seed=request.reference_expand_max_chunks_per_seed,
            reference_expand_max_chunks_per_doc=request.reference_expand_max_chunks_per_doc,
            reference_expand_section_max_chunks_per_target=request.reference_expand_section_max_chunks_per_target,
        ),
    )
    return (
        None,
        RetrievalResult(
            policy_name=request.policy_name,
            document_routing_source=request.document_routing_source,
            document_routing_post_processing=request.document_routing_post_processing,
            chunk_retrieval_mode=request.chunk_retrieval_mode,
            document_hits=document_hits,
            chunk_results=expanded_results,
            doc_chunks=doc_chunks,
        ),
    )


def _execute_document_routing_through_chunks(  # noqa: PLR0911
    request: RetrievalRequest,
    query_for_embedding: str,
    config: RetrievalPipelineConfig,
) -> tuple[str | None, RetrievalResult | None]:
    chunk_index_error = _get_chunk_index_error(config=config)
    if chunk_index_error is not None:
        return chunk_index_error, None

    ranked_chunk_results = _search_chunks(query=query_for_embedding, config=config)
    if not ranked_chunk_results:
        return "Error: No chunks retrieved", None

    selected_results = _select_top_k_per_document(
        ranked_results=ranked_chunk_results,
        k=request.k,
        min_score=request.chunk_min_score,
    )
    if not selected_results:
        return f"Error: No chunks found with score >= {request.chunk_min_score}", None

    ranked_document_results = _aggregate_standard_document_scores(selected_results)
    if not ranked_document_results:
        return "Error: No documents retrieved", None

    document_selection_error, document_hits = _select_top_d_documents(
        ranked_results=ranked_document_results,
        d=request.d,
        document_d_by_type=request.document_d_by_type,
        document_min_score_by_type=request.document_min_score_by_type,
    )
    if document_selection_error is not None:
        return document_selection_error, None
    if not document_hits:
        return "Error: No documents found with the configured per-type score thresholds", None

    allowed_doc_uids = {document_hit.doc_uid for document_hit in document_hits}
    allowed_ranked_chunk_results = [result for result in ranked_chunk_results if str(result["doc_uid"]) in allowed_doc_uids]
    if not allowed_ranked_chunk_results:
        return "Error: No chunks found in selected documents", None

    filtered_ranked_chunk_results = [result for result in selected_results if str(result["doc_uid"]) in allowed_doc_uids]
    if not filtered_ranked_chunk_results:
        return "Error: No chunks found in selected documents", None

    doc_uids_to_fetch = _collect_doc_uids_for_chunk_expansion(filtered_ranked_chunk_results, request)
    doc_chunks = _fetch_chunks(doc_uids=doc_uids_to_fetch, config=config)
    docs_to_expand_to_section = {document_hit.doc_uid for document_hit in document_hits if request.document_expand_to_section_by_type.get(document_hit.document_type, False)}
    expanded_results = _expand_chunks(
        ranked_results=allowed_ranked_chunk_results,
        results=filtered_ranked_chunk_results,
        doc_chunks=doc_chunks,
        expansion_config=ExpansionConfig(
            section_store=config.section_store,
            reference_store=config.reference_store,
            expand_to_section=request.expand_to_section,
            expand_to_section_doc_uids=docs_to_expand_to_section,
            expand=request.expand,
            full_doc_threshold=request.full_doc_threshold,
            reference_expand_enabled=request.reference_expand_enabled,
            reference_expand_depth=request.reference_expand_depth,
            reference_expand_max_chunks_per_seed=request.reference_expand_max_chunks_per_seed,
            reference_expand_max_chunks_per_doc=request.reference_expand_max_chunks_per_doc,
            reference_expand_section_max_chunks_per_target=request.reference_expand_section_max_chunks_per_target,
        ),
    )
    return (
        None,
        RetrievalResult(
            policy_name=request.policy_name,
            document_routing_source=request.document_routing_source,
            document_routing_post_processing=request.document_routing_post_processing,
            chunk_retrieval_mode=request.chunk_retrieval_mode,
            document_hits=document_hits,
            chunk_results=expanded_results,
            doc_chunks=doc_chunks,
        ),
    )

    return selected_results
