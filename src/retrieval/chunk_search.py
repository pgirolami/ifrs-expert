"""Chunk search, fetch, and top-k selection helpers."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from src.models.document import resolve_standard_doc_uid
from src.models.provenance import Provenance

if TYPE_CHECKING:
    from src.interfaces import SearchResult
    from src.models.chunk import Chunk
    from src.retrieval.models import RetrievalRequest
    from src.retrieval.pipeline import RetrievalPipelineConfig

logger = logging.getLogger(__name__)


def _search_chunks(query: str, config: RetrievalPipelineConfig) -> list[SearchResult]:
    with config.vector_store as vector_store:
        ranked_results = vector_store.search_all(query)
    for result in ranked_results:
        result["provenance"] = Provenance.TOP_SIMILARITY
    logger.info(f"Search returned {len(ranked_results)} raw chunk result(s)")
    return ranked_results


def _fetch_chunks(
    doc_uids: set[str],
    config: RetrievalPipelineConfig,
) -> dict[str, list[Chunk]]:
    config.init_db_fn()
    doc_chunks: dict[str, list[Chunk]] = {}
    with config.chunk_store as chunk_store:
        for doc_uid in sorted(doc_uids):
            doc_chunks[doc_uid] = chunk_store.get_chunks_by_doc(doc_uid)
    return doc_chunks


def _collect_doc_uids_for_chunk_expansion(
    selected_results: list[SearchResult],
    request: RetrievalRequest,
) -> set[str]:
    doc_uids = {str(result["doc_uid"]) for result in selected_results}
    if not request.reference_expand_enabled:
        return doc_uids
    standard_doc_uids = {resolve_standard_doc_uid(doc_uid) or doc_uid for doc_uid in doc_uids}
    doc_uids.update(standard_doc_uids)
    return doc_uids


def _select_top_k_per_document(
    ranked_results: list[SearchResult],
    k: int,
    min_score: float,
) -> list[SearchResult]:
    selected_results: list[SearchResult] = []
    counts_by_doc: dict[str, int] = {}
    for result in ranked_results:
        if result["score"] < min_score:
            continue
        doc_uid = result["doc_uid"]
        if counts_by_doc.get(doc_uid, 0) >= k:
            continue
        selected_results.append(result)
        counts_by_doc[doc_uid] = counts_by_doc.get(doc_uid, 0) + 1
    return selected_results
