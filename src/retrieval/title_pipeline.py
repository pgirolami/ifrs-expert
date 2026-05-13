"""Title-based retrieval strategy."""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.retrieval.models import RetrievalResult
from src.retrieval.title_retrieval import TitleRetrievalConfig, TitleRetrievalOptions, flatten_title_hits, retrieve_title_hits

if TYPE_CHECKING:
    from src.interfaces import SearchResult
    from src.models.chunk import Chunk
    from src.retrieval.models import RetrievalRequest
    from src.retrieval.pipeline import RetrievalPipelineConfig


def _execute_title_retrieval(
    request: RetrievalRequest,
    query_for_embedding: str,
    config: RetrievalPipelineConfig,
) -> tuple[str | None, RetrievalResult | None]:
    if config.section_store is None or config.title_vector_store is None or config.title_index_path_fn is None:
        return "Error: Title retrieval is not configured.", None

    error, hits = retrieve_title_hits(
        query=query_for_embedding,
        config=TitleRetrievalConfig(
            title_vector_store=config.title_vector_store,
            section_store=config.section_store,
            chunk_store=config.chunk_store,
            init_db_fn=config.init_db_fn,
            index_path_fn=config.title_index_path_fn,
        ),
        options=TitleRetrievalOptions(k=request.k, min_score=request.chunk_min_score),
    )
    if error is not None:
        return error, None

    selected_chunks = flatten_title_hits(hits)
    if not selected_chunks:
        return "Error: No chunks retrieved", None

    doc_chunks: dict[str, list[Chunk]] = {}
    chunk_results: list[SearchResult] = []
    for doc_uid in dict.fromkeys(chunk.doc_uid for chunk in selected_chunks):
        chunks_for_doc = sorted(
            (chunk for chunk in selected_chunks if chunk.doc_uid == doc_uid),
            key=lambda chunk: chunk.id or 0,
        )
        doc_chunks[doc_uid] = chunks_for_doc
        for chunk in chunks_for_doc:
            if chunk.id is None:
                continue
            chunk_results.append({"doc_uid": doc_uid, "chunk_id": chunk.id, "score": 0.0})

    return (
        None,
        RetrievalResult(
            policy_name=request.policy_name,
            document_routing_source=request.document_routing_source,
            document_routing_post_processing=request.document_routing_post_processing,
            chunk_retrieval_mode=request.chunk_retrieval_mode,
            document_hits=[],
            chunk_results=chunk_results,
            doc_chunks=doc_chunks,
        ),
    )
