"""Shared retrieval pipeline for text, title, and document-first retrieval."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.models.document import DOCUMENT_TYPES, infer_exact_document_type
from src.retrieval.models import DocumentHit, RetrievalRequest, RetrievalResult
from src.retrieval.title_retrieval import TitleRetrievalConfig, TitleRetrievalOptions, flatten_title_hits, retrieve_title_hits

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from src.interfaces import DocumentSearchResult, ReadChunkStoreProtocol, ReadSectionStoreProtocol, SearchDocumentVectorStoreProtocol, SearchResult, SearchTitleVectorStoreProtocol, SearchVectorStoreProtocol
    from src.models.chunk import Chunk

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class RetrievalPipelineConfig:
    """Dependencies required by the shared retrieval pipeline."""

    vector_store: SearchVectorStoreProtocol
    chunk_store: ReadChunkStoreProtocol
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[], Path]
    section_store: ReadSectionStoreProtocol | None = None
    title_vector_store: SearchTitleVectorStoreProtocol | None = None
    title_index_path_fn: Callable[[], Path] | None = None
    document_vector_store: SearchDocumentVectorStoreProtocol | None = None
    document_vector_store_factory: Callable[[str], SearchDocumentVectorStoreProtocol] | None = None
    document_index_path_fn: Callable[[str], Path] | None = None


@dataclass(frozen=True)
class ExpansionConfig:
    """Options for post-retrieval chunk expansion."""

    section_store: ReadSectionStoreProtocol | None
    expand_to_section: bool
    expand_to_section_doc_uids: set[str] | None
    expand: int
    full_doc_threshold: int


def execute_retrieval(
    request: RetrievalRequest,
    config: RetrievalPipelineConfig,
) -> tuple[str | None, RetrievalResult | None]:
    """Execute the shared retrieval pipeline for one request."""
    if request.retrieval_mode == "titles":
        return _execute_title_retrieval(request=request, config=config)
    if request.retrieval_mode == "documents":
        return _execute_document_retrieval(request=request, config=config)
    return _execute_text_retrieval(request=request, config=config)


def _execute_text_retrieval(
    request: RetrievalRequest,
    config: RetrievalPipelineConfig,
) -> tuple[str | None, RetrievalResult | None]:
    index_error = _get_chunk_index_error(config=config)
    if index_error is not None:
        return index_error, None

    ranked_results = _search_chunks(query=request.query, config=config)
    if not ranked_results:
        return "Error: No chunks retrieved", None

    selected_results = _select_top_k_per_document(
        ranked_results=ranked_results,
        k=request.k,
        min_score=request.chunk_min_score,
    )
    if not selected_results:
        return f"Error: No chunks found with score >= {request.chunk_min_score}", None

    doc_chunks = _fetch_chunks(selected_results=selected_results, config=config)
    expanded_results = _expand_chunks(
        results=selected_results,
        doc_chunks=doc_chunks,
        expansion_config=ExpansionConfig(
            section_store=config.section_store,
            expand_to_section=request.expand_to_section,
            expand_to_section_doc_uids=None,
            expand=request.expand,
            full_doc_threshold=request.full_doc_threshold,
        ),
    )
    return (
        None,
        RetrievalResult(
            retrieval_mode="text",
            document_hits=[],
            chunk_results=expanded_results,
            doc_chunks=doc_chunks,
        ),
    )


def _execute_title_retrieval(
    request: RetrievalRequest,
    config: RetrievalPipelineConfig,
) -> tuple[str | None, RetrievalResult | None]:
    if config.section_store is None or config.title_vector_store is None or config.title_index_path_fn is None:
        return "Error: Title retrieval is not configured.", None

    error, hits = retrieve_title_hits(
        query=request.query,
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
            retrieval_mode="titles",
            document_hits=[],
            chunk_results=chunk_results,
            doc_chunks=doc_chunks,
        ),
    )


def _execute_document_retrieval(  # noqa: PLR0911
    request: RetrievalRequest,
    config: RetrievalPipelineConfig,
) -> tuple[str | None, RetrievalResult | None]:
    prerequisite_error = _get_document_retrieval_prerequisite_error(config=config, request=request)
    if prerequisite_error is not None:
        return prerequisite_error, None

    ranked_document_results = _search_documents_by_representation(
        query=request.query,
        config=config,
        document_similarity_representation_by_type=request.document_similarity_representation_by_type,
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
    ranked_chunk_results = _search_chunks(query=request.query, config=config)
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

    doc_chunks = _fetch_chunks(selected_results=selected_results, config=config)
    docs_to_expand_to_section = {document_hit.doc_uid for document_hit in document_hits if request.document_expand_to_section_by_type.get(document_hit.document_type, False)}
    expanded_results = _expand_chunks(
        results=selected_results,
        doc_chunks=doc_chunks,
        expansion_config=ExpansionConfig(
            section_store=config.section_store,
            expand_to_section=request.expand_to_section,
            expand_to_section_doc_uids=docs_to_expand_to_section,
            expand=request.expand,
            full_doc_threshold=request.full_doc_threshold,
        ),
    )
    return (
        None,
        RetrievalResult(
            retrieval_mode="documents",
            document_hits=document_hits,
            chunk_results=expanded_results,
            doc_chunks=doc_chunks,
        ),
    )


def _get_document_retrieval_prerequisite_error(
    config: RetrievalPipelineConfig,
    request: RetrievalRequest,
) -> str | None:
    if config.document_vector_store is None and config.document_vector_store_factory is None:
        return "Error: Document retrieval is not configured."
    document_index_error = _get_document_index_error(
        config=config,
        requested_representations=set(request.document_similarity_representation_by_type.values()),
    )
    if document_index_error is not None:
        return document_index_error
    return _get_chunk_index_error(config=config)


def _get_chunk_index_error(config: RetrievalPipelineConfig) -> str | None:
    index_path = config.index_path_fn()
    if index_path.exists():
        return None
    logger.error(f"Missing vector index at {index_path}; corpus must be built before running queries")
    return "Error: No index found. Please run 'store' command first."


def _get_document_index_error(
    config: RetrievalPipelineConfig,
    requested_representations: set[str],
) -> str | None:
    if config.document_index_path_fn is None:
        return "Error: Document retrieval is not configured."
    for representation in sorted(requested_representations):
        try:
            document_index_path = config.document_index_path_fn(representation)
        except TypeError:
            document_index_path = config.document_index_path_fn()  # type: ignore[call-arg]
        if document_index_path.exists():
            continue
        logger.error(f"Missing document vector index at {document_index_path} for representation={representation}; corpus must be built before running queries")
        return "Error: No document index found. Please run 'store' command first."
    return None


def _search_documents_by_representation(
    query: str,
    config: RetrievalPipelineConfig,
    document_similarity_representation_by_type: dict[str, str],
) -> list[DocumentSearchResult]:
    ranked_by_doc_uid: dict[str, float] = {}
    required_representations = sorted(set(document_similarity_representation_by_type.values()))
    for representation in required_representations:
        document_vector_store = _get_document_vector_store(config=config, representation=representation)
        with document_vector_store as active_document_vector_store:
            ranked_results = active_document_vector_store.search_all(query)
        for result in ranked_results:
            doc_uid = str(result["doc_uid"])
            document_type = infer_exact_document_type(doc_uid)
            if document_type is None:
                continue
            configured_representation = document_similarity_representation_by_type.get(document_type)
            if configured_representation != representation:
                continue
            score = float(result["score"])
            existing_score = ranked_by_doc_uid.get(doc_uid)
            if existing_score is None or score > existing_score:
                ranked_by_doc_uid[doc_uid] = score

    ranked_results_output: list[DocumentSearchResult] = [{"doc_uid": doc_uid, "score": score} for doc_uid, score in ranked_by_doc_uid.items()]
    ranked_results_output.sort(key=lambda item: item["score"], reverse=True)
    logger.info(f"Document search across representations returned {len(ranked_results_output)} unique candidate(s); representations={required_representations}")
    return ranked_results_output


def _get_document_vector_store(
    config: RetrievalPipelineConfig,
    representation: str,
) -> SearchDocumentVectorStoreProtocol:
    if config.document_vector_store_factory is not None:
        return config.document_vector_store_factory(representation)
    if config.document_vector_store is not None:
        return config.document_vector_store
    message = "Error: Document retrieval is not configured."
    raise RuntimeError(message)


def _search_chunks(query: str, config: RetrievalPipelineConfig) -> list[SearchResult]:
    with config.vector_store as vector_store:
        ranked_results = vector_store.search_all(query)
    logger.info(f"Search returned {len(ranked_results)} raw chunk result(s)")
    return ranked_results


def _fetch_chunks(
    selected_results: list[SearchResult],
    config: RetrievalPipelineConfig,
) -> dict[str, list[Chunk]]:
    config.init_db_fn()
    doc_chunks: dict[str, list[Chunk]] = {}
    with config.chunk_store as chunk_store:
        for doc_uid in dict.fromkeys(result["doc_uid"] for result in selected_results):
            doc_chunks[doc_uid] = chunk_store.get_chunks_by_doc(doc_uid)
    return doc_chunks


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


def _select_top_d_documents(
    ranked_results: list[DocumentSearchResult],
    d: int,
    document_d_by_type: dict[str, int],
    document_min_score_by_type: dict[str, float],
) -> tuple[str | None, list[DocumentHit]]:
    document_hits: list[DocumentHit] = []
    selected_count_by_type = dict.fromkeys(DOCUMENT_TYPES, 0)
    for document_type in DOCUMENT_TYPES:
        if document_type not in document_min_score_by_type:
            return f"Error: Missing per-type document min score for {document_type}", []

    for result in ranked_results:
        doc_uid = str(result["doc_uid"])
        score = float(result["score"])
        document_type = infer_exact_document_type(doc_uid)
        if document_type is None:
            return f"Error: Could not resolve exact document_type for candidate doc_uid={doc_uid}", []
        if document_type not in document_d_by_type:
            return f"Error: Missing per-type document cap for {document_type}", []
        if score < document_min_score_by_type[document_type]:
            continue
        if selected_count_by_type[document_type] >= document_d_by_type[document_type]:
            continue
        document_hits.append(DocumentHit(doc_uid=doc_uid, score=score, document_type=document_type))
        selected_count_by_type[document_type] += 1
        if len(document_hits) >= d:
            break
    return None, document_hits


def _init_expansion_state(
    results: list[SearchResult],
) -> tuple[dict[tuple[str, int], float], list[str], dict[str, set[int]]]:
    result_score_by_chunk: dict[tuple[str, int], float] = {}
    doc_order: list[str] = []
    selected_ids_by_doc: dict[str, set[int]] = {}
    for result in results:
        doc_uid = result["doc_uid"]
        chunk_id = result["chunk_id"]
        if doc_uid not in selected_ids_by_doc:
            selected_ids_by_doc[doc_uid] = set()
            doc_order.append(doc_uid)
        selected_ids_by_doc[doc_uid].add(chunk_id)
        result_score_by_chunk[(doc_uid, chunk_id)] = result["score"]
    return result_score_by_chunk, doc_order, selected_ids_by_doc


def _include_full_documents(
    doc_chunks: dict[str, list[Chunk]],
    selected_ids_by_doc: dict[str, set[int]],
    full_doc_threshold: int,
) -> set[str]:
    full_doc_docs: set[str] = set()
    for doc_uid, chunks in doc_chunks.items():
        doc_text_size = sum(len(chunk.text) for chunk in chunks)
        if full_doc_threshold <= 0 or doc_text_size >= full_doc_threshold:
            continue
        full_doc_docs.add(doc_uid)
        for chunk in chunks:
            if chunk.id is not None:
                selected_ids_by_doc[doc_uid].add(chunk.id)
    return full_doc_docs


def _expand_to_section_subtrees(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
    section_store: ReadSectionStoreProtocol | None,
    selected_ids_by_doc: dict[str, set[int]],
    expand_to_section_doc_uids: set[str] | None,
) -> None:
    if section_store is None:
        logger.info("Skipping section expansion because no section store is configured")
        return

    descendant_section_db_ids_by_section_db_id: dict[int, set[int]] = {}
    section_db_id_by_source_id_by_doc: dict[str, dict[str, int]] = {}
    with section_store as active_section_store:
        for result in results:
            doc_uid = result["doc_uid"]
            if expand_to_section_doc_uids is not None and doc_uid not in expand_to_section_doc_uids:
                continue
            if doc_uid not in section_db_id_by_source_id_by_doc:
                section_db_id_by_source_id_by_doc[doc_uid] = {section.section_id: section.db_id for section in active_section_store.get_sections_by_doc(doc_uid) if section.db_id is not None}
            matching_chunk = _find_chunk_by_id(
                chunks=doc_chunks.get(doc_uid, []),
                chunk_id=result["chunk_id"],
            )
            if matching_chunk is None:
                continue
            containing_section_db_id = _resolve_chunk_section_db_id(
                chunk=matching_chunk,
                section_db_id_by_source_id=section_db_id_by_source_id_by_doc[doc_uid],
            )
            if containing_section_db_id is None:
                continue
            if containing_section_db_id not in descendant_section_db_ids_by_section_db_id:
                descendant_section_db_ids_by_section_db_id[containing_section_db_id] = set(active_section_store.get_descendant_section_db_ids(containing_section_db_id))
            descendant_section_db_ids = descendant_section_db_ids_by_section_db_id[containing_section_db_id]
            for chunk in doc_chunks.get(doc_uid, []):
                chunk_section_db_id = _resolve_chunk_section_db_id(
                    chunk=chunk,
                    section_db_id_by_source_id=section_db_id_by_source_id_by_doc[doc_uid],
                )
                if chunk.id is None or chunk_section_db_id not in descendant_section_db_ids:
                    continue
                selected_ids_by_doc[doc_uid].add(chunk.id)


def _find_chunk_by_id(chunks: list[Chunk], chunk_id: int) -> Chunk | None:
    for chunk in chunks:
        if chunk.id == chunk_id:
            return chunk
    return None


def _resolve_chunk_section_db_id(
    chunk: Chunk,
    section_db_id_by_source_id: dict[str, int],
) -> int | None:
    if chunk.containing_section_db_id is not None:
        return chunk.containing_section_db_id
    if chunk.containing_section_id is None:
        return None
    return section_db_id_by_source_id.get(chunk.containing_section_id)


def _expand_with_neighbour_chunks(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
    selected_ids_by_doc: dict[str, set[int]],
    expand: int,
) -> None:
    for result in results:
        doc_uid = result["doc_uid"]
        chunk_id = result["chunk_id"]
        chunks = doc_chunks.get(doc_uid, [])
        for index, chunk in enumerate(chunks):
            if chunk.id != chunk_id:
                continue
            start_index = max(0, index - expand)
            end_index = min(len(chunks), index + expand + 1)
            for surrounding_chunk in chunks[start_index:end_index]:
                if surrounding_chunk.id is not None:
                    selected_ids_by_doc[doc_uid].add(surrounding_chunk.id)
            break


def _build_expanded_chunk_results(
    doc_order: list[str],
    doc_chunks: dict[str, list[Chunk]],
    selected_ids_by_doc: dict[str, set[int]],
    result_score_by_chunk: dict[tuple[str, int], float],
) -> list[SearchResult]:
    expanded_results: list[SearchResult] = []
    for doc_uid in doc_order:
        for chunk in doc_chunks.get(doc_uid, []):
            chunk_id = chunk.id
            if chunk_id is None:
                continue
            if chunk_id not in selected_ids_by_doc.get(doc_uid, set()):
                continue
            expanded_results.append(
                {
                    "doc_uid": doc_uid,
                    "chunk_id": chunk_id,
                    "score": result_score_by_chunk.get((doc_uid, chunk_id), 0.0),
                }
            )
    return expanded_results


def _expand_chunks(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
    expansion_config: ExpansionConfig,
) -> list[SearchResult]:
    if not expansion_config.expand_to_section and expansion_config.expand <= 0 and expansion_config.full_doc_threshold <= 0:
        return results

    result_score_by_chunk, doc_order, selected_ids_by_doc = _init_expansion_state(results)
    if expansion_config.expand_to_section:
        _expand_to_section_subtrees(
            results=results,
            doc_chunks=doc_chunks,
            section_store=expansion_config.section_store,
            selected_ids_by_doc=selected_ids_by_doc,
            expand_to_section_doc_uids=expansion_config.expand_to_section_doc_uids,
        )
    full_doc_docs = _include_full_documents(
        doc_chunks=doc_chunks,
        selected_ids_by_doc=selected_ids_by_doc,
        full_doc_threshold=expansion_config.full_doc_threshold,
    )
    if expansion_config.expand > 0:
        _expand_with_neighbour_chunks(
            results=results,
            doc_chunks=doc_chunks,
            selected_ids_by_doc=selected_ids_by_doc,
            expand=expansion_config.expand,
        )
    expanded_results = _build_expanded_chunk_results(
        doc_order=doc_order,
        doc_chunks=doc_chunks,
        selected_ids_by_doc=selected_ids_by_doc,
        result_score_by_chunk=result_score_by_chunk,
    )
    for doc_uid in full_doc_docs:
        doc_size = sum(len(chunk.text) for chunk in doc_chunks.get(doc_uid, []))
        logger.info(f"Full doc inclusion: {doc_uid} (size={doc_size} < threshold={expansion_config.full_doc_threshold})")
    return expanded_results
