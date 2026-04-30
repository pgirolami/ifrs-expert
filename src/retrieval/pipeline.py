"""Shared retrieval pipeline for text, title, and document-first retrieval."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.models.document import DOCUMENT_TYPES, infer_exact_document_type, resolve_standard_doc_uid
from src.models.provenance import Provenance, coerce_provenance
from src.models.reference import ContentReference
from src.retrieval.models import DocumentHit, RetrievalRequest, RetrievalResult
from src.retrieval.query_embedding import build_query_embedding_text
from src.retrieval.retrieval_contract import expand_chunk_number_range
from src.retrieval.title_retrieval import (
    TitleRetrievalConfig,
    TitleRetrievalOptions,
    flatten_title_hits,
    retrieve_title_hits,
)

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from src.interfaces import (
        DocumentSearchResult,
        ReadChunkStoreProtocol,
        ReadSectionStoreProtocol,
        ReferenceStoreProtocol,
        SearchDocumentVectorStoreProtocol,
        SearchResult,
        SearchTitleVectorStoreProtocol,
        SearchVectorStoreProtocol,
    )
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
    reference_store: ReferenceStoreProtocol | None = None
    title_vector_store: SearchTitleVectorStoreProtocol | None = None
    title_index_path_fn: Callable[[], Path] | None = None
    document_vector_store: SearchDocumentVectorStoreProtocol | None = None
    document_vector_store_factory: Callable[[str], SearchDocumentVectorStoreProtocol] | None = None
    document_index_path_fn: Callable[[str], Path] | None = None


@dataclass(frozen=True)
class ExpansionConfig:
    """Options for post-retrieval chunk expansion."""

    section_store: ReadSectionStoreProtocol | None
    reference_store: ReferenceStoreProtocol | None
    expand_to_section: bool
    expand_to_section_doc_uids: set[str] | None
    expand: int
    full_doc_threshold: int
    reference_expand_enabled: bool
    reference_expand_depth: int
    reference_expand_max_chunks_per_seed: int
    reference_expand_max_chunks_per_doc: int


@dataclass
class ExpansionState:
    """Mutable expansion state shared across the post-retrieval stages."""

    selected_ids_by_doc: dict[str, set[int]]
    provenance_by_chunk: dict[tuple[str, int], Provenance]
    doc_order: list[str]


@dataclass
class ReferenceExpansionContext:
    """Inputs needed to expand same-family references for seed chunks."""

    doc_chunks: dict[str, list[Chunk]]
    references_by_doc: dict[str, list[ContentReference]]
    expansion_config: ExpansionConfig
    state: ExpansionState
    added_chunks_by_doc: dict[str, int]


@dataclass
class ReferenceExpansionSeedState:
    """Per-seed expansion state used while traversing references."""

    source_standard_doc_uid: str
    chunks_added_for_seed: int = 0


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
    filtered_ranked_chunk_results = [result for result in selected_results if str(result["doc_uid"]) in allowed_doc_uids]
    if not filtered_ranked_chunk_results:
        return "Error: No chunks found in selected documents", None

    doc_uids_to_fetch = _collect_doc_uids_for_chunk_expansion(filtered_ranked_chunk_results, request)
    doc_chunks = _fetch_chunks(doc_uids=doc_uids_to_fetch, config=config)
    docs_to_expand_to_section = {document_hit.doc_uid for document_hit in document_hits if request.document_expand_to_section_by_type.get(document_hit.document_type, False)}
    expanded_results = _expand_chunks(
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


def _aggregate_standard_document_scores(
    selected_results: list[SearchResult],
) -> list[DocumentSearchResult]:
    ranked_by_standard_doc_uid: dict[str, float] = {}
    for result in selected_results:
        raw_doc_uid = str(result["doc_uid"])
        standard_doc_uid = resolve_standard_doc_uid(raw_doc_uid)
        if standard_doc_uid is None:
            logger.debug(f"Skipping chunk candidate doc_uid={raw_doc_uid} because it could not be mapped to a standard doc_uid")
            continue
        score = float(result["score"])
        existing_score = ranked_by_standard_doc_uid.get(standard_doc_uid)
        if existing_score is None or score > existing_score:
            ranked_by_standard_doc_uid[standard_doc_uid] = score
    ranked_results_output: list[DocumentSearchResult] = [{"doc_uid": doc_uid, "score": score} for doc_uid, score in ranked_by_standard_doc_uid.items()]
    ranked_results_output.sort(key=lambda item: item["score"], reverse=True)
    logger.info(f"Aggregated {len(selected_results)} chunk result(s) into {len(ranked_results_output)} standard document candidate(s)")
    return ranked_results_output


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
    *,
    consolidate_variants_to_standard: bool,
) -> list[DocumentSearchResult]:
    ranked_by_doc_uid: dict[str, float] = {}
    required_representations = sorted(set(document_similarity_representation_by_type.values()))
    for representation in required_representations:
        document_vector_store = _get_document_vector_store(config=config, representation=representation)
        with document_vector_store as active_document_vector_store:
            ranked_results = active_document_vector_store.search_all(query)
        for result in ranked_results:
            _merge_document_search_result(
                ranked_by_doc_uid=ranked_by_doc_uid,
                result=result,
                representation=representation,
                document_similarity_representation_by_type=document_similarity_representation_by_type,
                consolidate_variants_to_standard=consolidate_variants_to_standard,
            )

    ranked_results_output: list[DocumentSearchResult] = [{"doc_uid": doc_uid, "score": score} for doc_uid, score in ranked_by_doc_uid.items()]
    ranked_results_output.sort(key=lambda item: item["score"], reverse=True)
    logger.info(f"Document search across representations returned {len(ranked_results_output)} unique candidate(s); representations={required_representations}; consolidate_to_standard={consolidate_variants_to_standard}")
    return ranked_results_output


def _merge_document_search_result(
    *,
    ranked_by_doc_uid: dict[str, float],
    result: DocumentSearchResult,
    representation: str,
    document_similarity_representation_by_type: dict[str, str],
    consolidate_variants_to_standard: bool,
) -> None:
    raw_doc_uid = str(result["doc_uid"])
    document_type = infer_exact_document_type(raw_doc_uid)
    if document_type is None:
        logger.debug(f"Skipping unresolved document candidate doc_uid={raw_doc_uid} during representation={representation}")
        return

    configured_representation = document_similarity_representation_by_type.get(document_type)
    if configured_representation != representation:
        return

    doc_uid = raw_doc_uid
    if consolidate_variants_to_standard:
        standard_doc_uid = resolve_standard_doc_uid(raw_doc_uid)
        if standard_doc_uid is None:
            logger.debug(f"Skipping document candidate doc_uid={raw_doc_uid} because it could not be mapped to a standard doc_uid")
            return
        if standard_doc_uid != raw_doc_uid:
            logger.debug(f"Consolidating variant document doc_uid={raw_doc_uid} to standard doc_uid={standard_doc_uid} for representation={representation}")
        doc_uid = standard_doc_uid

    score = float(result["score"])
    existing_score = ranked_by_doc_uid.get(doc_uid)
    if existing_score is None:
        ranked_by_doc_uid[doc_uid] = score
        if consolidate_variants_to_standard and doc_uid != raw_doc_uid:
            logger.debug(f"Recorded consolidated document doc_uid={doc_uid} score={score:.4f} from variant doc_uid={raw_doc_uid}")
        return

    if score > existing_score:
        logger.debug(f"Updating consolidated document doc_uid={doc_uid} score={existing_score:.4f} -> {score:.4f} from candidate doc_uid={raw_doc_uid}")
        ranked_by_doc_uid[doc_uid] = score
    elif consolidate_variants_to_standard:
        logger.debug(f"Keeping consolidated document doc_uid={doc_uid} existing_score={existing_score:.4f} >= candidate_score={score:.4f} from doc_uid={raw_doc_uid}")


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
) -> tuple[dict[tuple[str, int], float], ExpansionState]:
    result_score_by_chunk: dict[tuple[str, int], float] = {}
    doc_order: list[str] = []
    selected_ids_by_doc: dict[str, set[int]] = {}
    provenance_by_chunk: dict[tuple[str, int], Provenance] = {}
    for result in results:
        doc_uid = result["doc_uid"]
        chunk_id = result["chunk_id"]
        if doc_uid not in selected_ids_by_doc:
            selected_ids_by_doc[doc_uid] = set()
            doc_order.append(doc_uid)
        selected_ids_by_doc[doc_uid].add(chunk_id)
        result_score_by_chunk[(doc_uid, chunk_id)] = result["score"]
        provenance_by_chunk[(doc_uid, chunk_id)] = coerce_provenance(result.get("provenance"))
    return result_score_by_chunk, ExpansionState(
        selected_ids_by_doc=selected_ids_by_doc,
        provenance_by_chunk=provenance_by_chunk,
        doc_order=doc_order,
    )


def _include_full_documents(
    doc_chunks: dict[str, list[Chunk]],
    state: ExpansionState,
    full_doc_threshold: int,
) -> set[str]:
    full_doc_docs: set[str] = set()
    if full_doc_threshold <= 0:
        logger.debug("Skipping full-document inclusion because the threshold is disabled")
        return full_doc_docs
    for doc_uid, chunks in doc_chunks.items():
        doc_text_size = sum(len(chunk.text) for chunk in chunks)
        if doc_text_size >= full_doc_threshold:
            logger.debug(f"Keeping doc_uid={doc_uid} out of full-document inclusion; size={doc_text_size} threshold={full_doc_threshold}")
            continue
        full_doc_docs.add(doc_uid)
        logger.info(f"Including full document doc_uid={doc_uid}; size={doc_text_size} threshold={full_doc_threshold} chunks={len(chunks)}")
        for chunk in chunks:
            if chunk.id is not None:
                _add_selected_chunk(
                    doc_uid=doc_uid,
                    chunk_id=chunk.id,
                    provenance=Provenance.FULL_DOCUMENT,
                    state=state,
                )
    return full_doc_docs


def _expand_to_section_subtrees(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
    section_store: ReadSectionStoreProtocol | None,
    state: ExpansionState,
    expand_to_section_doc_uids: set[str] | None,
) -> None:
    if section_store is None:
        logger.info("Skipping section expansion because no section store is configured")
        return

    logger.info(
        "Starting section expansion: "
        f"seed_docs={len({str(result['doc_uid']) for result in results})} "
        f"results={len(results)} "
        f"expand_to_section_doc_uids={sorted(expand_to_section_doc_uids) if expand_to_section_doc_uids is not None else 'all'}"
    )

    descendant_section_db_ids_by_section_db_id: dict[int, set[int]] = {}
    section_db_id_by_source_id_by_doc: dict[str, dict[str, int]] = {}
    with section_store as active_section_store:
        for result in results:
            doc_uid = result["doc_uid"]
            chunk_id = result["chunk_id"]
            logger.info(f"Considering section expansion root doc_uid={doc_uid} chunk_id={chunk_id} score={result['score']:.4f}")
            if expand_to_section_doc_uids is not None and doc_uid not in expand_to_section_doc_uids:
                logger.info(f"Skipping section expansion root doc_uid={doc_uid} chunk_id={chunk_id} because it is not configured for section fan-out")
                continue
            if doc_uid not in section_db_id_by_source_id_by_doc:
                section_db_id_by_source_id_by_doc[doc_uid] = {section.section_id: section.db_id for section in active_section_store.get_sections_by_doc(doc_uid) if section.db_id is not None}
            matching_chunk = _find_chunk_by_id(
                chunks=doc_chunks.get(doc_uid, []),
                chunk_id=chunk_id,
            )
            if matching_chunk is None:
                logger.info(f"Skipping section expansion root doc_uid={doc_uid} chunk_id={chunk_id} because the chunk is missing from the fetched doc set")
                continue
            containing_section_db_id = _resolve_chunk_section_db_id(
                chunk=matching_chunk,
                section_db_id_by_source_id=section_db_id_by_source_id_by_doc[doc_uid],
            )
            if containing_section_db_id is None:
                logger.info(f"Skipping section expansion root doc_uid={doc_uid} chunk_id={chunk_id} because no containing section db id was resolved")
                continue
            if containing_section_db_id not in descendant_section_db_ids_by_section_db_id:
                descendant_section_db_ids_by_section_db_id[containing_section_db_id] = set(active_section_store.get_descendant_section_db_ids(containing_section_db_id))
            descendant_section_db_ids = descendant_section_db_ids_by_section_db_id[containing_section_db_id]
            source_provenance = coerce_provenance(state.provenance_by_chunk.get((doc_uid, result["chunk_id"])))
            expanded_provenance = _section_expansion_provenance(source_provenance)
            added_for_root = 0
            for chunk in doc_chunks.get(doc_uid, []):
                chunk_section_db_id = _resolve_chunk_section_db_id(
                    chunk=chunk,
                    section_db_id_by_source_id=section_db_id_by_source_id_by_doc[doc_uid],
                )
                if chunk.id is None or chunk_section_db_id not in descendant_section_db_ids:
                    continue
                _add_selected_chunk(
                    doc_uid=doc_uid,
                    chunk_id=chunk.id,
                    provenance=expanded_provenance,
                    state=state,
                )
                added_for_root += 1
            logger.info(
                f"Expanded section root doc_uid={doc_uid} chunk_id={chunk_id} through section_db_id={containing_section_db_id} descendants={len(descendant_section_db_ids)} provenance={expanded_provenance.value} added={added_for_root}"
            )
    logger.info("Completed section expansion")


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
    state: ExpansionState,
    expand: int,
) -> None:
    logger.info(f"Starting neighbour expansion: expand={expand} seed_results={len(results)}")
    for result in results:
        doc_uid = result["doc_uid"]
        chunk_id = result["chunk_id"]
        chunks = doc_chunks.get(doc_uid, [])
        source_provenance = coerce_provenance(state.provenance_by_chunk.get((doc_uid, chunk_id)))
        expanded_provenance = _section_expansion_provenance(source_provenance)
        for index, chunk in enumerate(chunks):
            if chunk.id != chunk_id:
                continue
            start_index = max(0, index - expand)
            end_index = min(len(chunks), index + expand + 1)
            added = 0
            for surrounding_chunk in chunks[start_index:end_index]:
                if surrounding_chunk.id is not None:
                    _add_selected_chunk(
                        doc_uid=doc_uid,
                        chunk_id=surrounding_chunk.id,
                        provenance=expanded_provenance,
                        state=state,
                    )
                    added += 1
            logger.debug(f"Expanded doc_uid={doc_uid} chunk_id={chunk_id} around index={index} window={start_index}:{end_index} provenance={expanded_provenance.value} added={added}")
            break
    logger.info("Completed neighbour expansion")


def _build_expanded_chunk_results(
    state: ExpansionState,
    doc_chunks: dict[str, list[Chunk]],
    result_score_by_chunk: dict[tuple[str, int], float],
) -> list[SearchResult]:
    expanded_results: list[SearchResult] = []
    for doc_uid in state.doc_order:
        for chunk in doc_chunks.get(doc_uid, []):
            chunk_id = chunk.id
            if chunk_id is None:
                continue
            if chunk_id not in state.selected_ids_by_doc.get(doc_uid, set()):
                continue
            expanded_results.append(
                {
                    "doc_uid": doc_uid,
                    "chunk_id": chunk_id,
                    "score": result_score_by_chunk.get((doc_uid, chunk_id), 0.0),
                    "provenance": state.provenance_by_chunk.get((doc_uid, chunk_id), Provenance.SIMILARITY),
                }
            )
    return expanded_results


def _add_selected_chunk(
    *,
    doc_uid: str,
    chunk_id: int,
    provenance: Provenance,
    state: ExpansionState,
) -> None:
    if doc_uid not in state.selected_ids_by_doc:
        state.selected_ids_by_doc[doc_uid] = set()
        state.doc_order.append(doc_uid)
    if chunk_id in state.selected_ids_by_doc[doc_uid]:
        return
    state.selected_ids_by_doc[doc_uid].add(chunk_id)
    state.provenance_by_chunk[(doc_uid, chunk_id)] = provenance


def _section_expansion_provenance(source_provenance: Provenance) -> Provenance:
    if source_provenance == Provenance.SIMILARITY:
        return Provenance.SECTION_FAN_OUT_FROM_SEED
    return Provenance.SECTION_FAN_OUT_FROM_REFERENCE


def _build_chunk_number_lookup(chunks: list[Chunk]) -> dict[str, Chunk]:
    lookup: dict[str, Chunk] = {}
    for chunk in chunks:
        lookup[chunk.chunk_number] = chunk
    return lookup


def _resolve_reference_target_chunk_numbers(reference: object) -> list[str]:
    chunk_numbers: list[str] = []
    if isinstance(reference, ContentReference) and reference.target_kind == "same_standard_paragraph" and reference.target_unit in {"paragraph", "section"} and reference.target_start is not None:
        if reference.target_end is None:
            chunk_numbers = [reference.target_start]
        else:
            try:
                chunk_numbers = expand_chunk_number_range(start=reference.target_start, end=reference.target_end)
            except ValueError:
                logger.warning(f"Skipping unresolved reference range {reference.target_start}-{reference.target_end} for source_doc_uid={reference.source_doc_uid}")
    return chunk_numbers


def _expand_same_family_references(
    *,
    seed_results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
    expansion_config: ExpansionConfig,
    state: ExpansionState,
) -> None:
    if not expansion_config.reference_expand_enabled or expansion_config.reference_expand_depth <= 0:
        logger.info(f"Skipping reference expansion because it is disabled or depth is zero; enabled={expansion_config.reference_expand_enabled} depth={expansion_config.reference_expand_depth}")
        return
    if expansion_config.reference_store is None:
        logger.info("Skipping reference expansion because no reference store is configured")
        return

    logger.info(
        "Starting same-family reference expansion: "
        f"seed_results={len(seed_results)} depth={expansion_config.reference_expand_depth} "
        f"max_chunks_per_seed={expansion_config.reference_expand_max_chunks_per_seed} "
        f"max_chunks_per_doc={expansion_config.reference_expand_max_chunks_per_doc}"
    )
    context = ReferenceExpansionContext(
        doc_chunks=doc_chunks,
        references_by_doc={},
        expansion_config=expansion_config,
        state=state,
        added_chunks_by_doc={},
    )
    for seed_result in seed_results:
        logger.debug(f"Traversing reference seed doc_uid={seed_result['doc_uid']} chunk_id={seed_result['chunk_id']} score={seed_result['score']:.4f}")
        _expand_reference_seed(seed_result=seed_result, context=context)
    logger.info("Completed same-family reference expansion")


def _load_references_by_doc(
    *,
    reference_store: ReferenceStoreProtocol,
    doc_uids: list[str],
) -> dict[str, list[ContentReference]]:
    references_by_doc: dict[str, list[ContentReference]] = {}
    with reference_store as active_reference_store:
        for doc_uid in doc_uids:
            references_by_doc[doc_uid] = list(active_reference_store.get_references_by_doc(doc_uid))
    return references_by_doc


def _load_references_for_doc(
    *,
    doc_uid: str,
    context: ReferenceExpansionContext,
) -> list[ContentReference]:
    if doc_uid in context.references_by_doc:
        return context.references_by_doc[doc_uid]
    reference_store = context.expansion_config.reference_store
    if reference_store is None:
        return []
    references_by_doc = _load_references_by_doc(reference_store=reference_store, doc_uids=[doc_uid])
    references = references_by_doc.get(doc_uid, [])
    context.references_by_doc[doc_uid] = references
    logger.debug(f"Loaded {len(references)} reference(s) for doc_uid={doc_uid}")
    return references


def _expand_reference_seed(
    *,
    seed_result: SearchResult,
    context: ReferenceExpansionContext,
) -> int:
    source_doc_uid = str(seed_result["doc_uid"])
    source_standard_doc_uid = resolve_standard_doc_uid(source_doc_uid)
    if source_standard_doc_uid is None:
        logger.debug(f"Skipping reference seed doc_uid={source_doc_uid} because it cannot be resolved to a standard doc")
        return 0

    target_doc_chunks = context.doc_chunks.get(source_standard_doc_uid, [])
    if not target_doc_chunks:
        logger.debug(f"Skipping reference seed doc_uid={source_doc_uid} because target doc_uid={source_standard_doc_uid} has no fetched chunks")
        return 0

    seed_chunk = _find_chunk_by_id(context.doc_chunks.get(source_doc_uid, []), seed_result["chunk_id"])
    if seed_chunk is None:
        logger.debug(f"Skipping reference seed doc_uid={source_doc_uid} chunk_id={seed_result['chunk_id']} because the chunk is missing from the fetched doc set")
        return 0

    seed_state = ReferenceExpansionSeedState(
        source_standard_doc_uid=source_standard_doc_uid,
    )
    processed_source_chunks: set[tuple[str, int]] = set()
    logger.debug(f"Reference seed resolved: source_doc_uid={source_doc_uid} standard_doc_uid={source_standard_doc_uid} chunk_number={seed_chunk.chunk_number} target_chunks={len(target_doc_chunks)}")
    _expand_reference_source_chunk(
        source_chunk=seed_chunk,
        depth_remaining=context.expansion_config.reference_expand_depth,
        seed_state=seed_state,
        context=context,
        processed_source_chunks=processed_source_chunks,
    )
    logger.debug(f"Reference seed complete: source_doc_uid={source_doc_uid} added_chunks={seed_state.chunks_added_for_seed}")
    return seed_state.chunks_added_for_seed


def _expand_reference_source_chunk(
    *,
    source_chunk: Chunk,
    depth_remaining: int,
    seed_state: ReferenceExpansionSeedState,
    context: ReferenceExpansionContext,
    processed_source_chunks: set[tuple[str, int]],
) -> int:
    if depth_remaining <= 0:
        logger.debug(f"Stopping reference traversal for chunk_id={source_chunk.id} because depth is exhausted")
        return 0
    source_chunk_id = source_chunk.id
    if source_chunk_id is None:
        return 0
    source_doc_uid = source_chunk.doc_uid
    source_key = (source_doc_uid, source_chunk_id)
    if source_key in processed_source_chunks:
        logger.debug(f"Skipping already-processed reference source chunk doc_uid={source_doc_uid} chunk_id={source_chunk_id}")
        return 0
    processed_source_chunks.add(source_key)

    source_standard_doc_uid = resolve_standard_doc_uid(source_doc_uid)
    if source_standard_doc_uid is None:
        logger.debug(f"Skipping source chunk doc_uid={source_doc_uid} chunk_id={source_chunk_id} because it cannot resolve to a standard doc")
        return 0

    references = _load_references_for_doc(doc_uid=source_doc_uid, context=context)
    matching_references = _filter_seed_references(source_chunk, references)
    if not matching_references:
        logger.debug(f"No matching references found for doc_uid={source_doc_uid} chunk_number={source_chunk.chunk_number}")
        return 0

    logger.info(f"Traversing references for source_doc_uid={source_doc_uid} chunk_number={source_chunk.chunk_number} matched_references={len(matching_references)} depth_remaining={depth_remaining}")
    added_chunks = 0
    for reference in matching_references:
        if context.expansion_config.reference_expand_max_chunks_per_seed > 0 and seed_state.chunks_added_for_seed >= context.expansion_config.reference_expand_max_chunks_per_seed:
            logger.info(f"Stopping reference expansion for source_doc_uid={source_doc_uid} because max_chunks_per_seed={context.expansion_config.reference_expand_max_chunks_per_seed} was reached")
            break
        added_chunks += _expand_reference_targets_for_seed(
            reference=reference,
            seed_state=seed_state,
            context=context,
            depth_remaining=depth_remaining,
            processed_source_chunks=processed_source_chunks,
        )
    return added_chunks


def _expand_reference_targets_for_seed(
    *,
    reference: ContentReference,
    seed_state: ReferenceExpansionSeedState,
    context: ReferenceExpansionContext,
    depth_remaining: int,
    processed_source_chunks: set[tuple[str, int]],
) -> int:
    added_chunks = 0
    target_chunks_by_number = _build_chunk_number_lookup(context.doc_chunks.get(seed_state.source_standard_doc_uid, []))
    target_chunk_numbers = _resolve_reference_target_chunk_numbers(reference)
    for target_chunk_number in target_chunk_numbers:
        logger.info(
            f"Considering reference target: source_doc_uid={reference.source_doc_uid} "
            f"source_chunk_id={reference.source_chunk_id} target_kind={reference.target_kind} "
            f"target_chunk_number={target_chunk_number} standard_doc_uid={seed_state.source_standard_doc_uid} "
            f"depth_remaining={depth_remaining}"
        )
        if context.expansion_config.reference_expand_max_chunks_per_seed > 0 and seed_state.chunks_added_for_seed >= context.expansion_config.reference_expand_max_chunks_per_seed:
            logger.info(f"Stopping target following for source_doc_uid={reference.source_doc_uid} because max_chunks_per_seed={context.expansion_config.reference_expand_max_chunks_per_seed} was reached")
            break
        if context.expansion_config.reference_expand_max_chunks_per_doc > 0 and context.added_chunks_by_doc.get(seed_state.source_standard_doc_uid, 0) >= context.expansion_config.reference_expand_max_chunks_per_doc:
            logger.info(f"Stopping target following for standard_doc_uid={seed_state.source_standard_doc_uid} because max_chunks_per_doc={context.expansion_config.reference_expand_max_chunks_per_doc} was reached")
            break
        target_chunk = target_chunks_by_number.get(target_chunk_number)
        if target_chunk is None and reference.target_unit == "section":
            target_chunk = _find_first_chunk_with_prefix(
                chunks=context.doc_chunks.get(seed_state.source_standard_doc_uid, []),
                chunk_number_prefix=target_chunk_number,
            )
        if target_chunk is None or target_chunk.id is None:
            logger.info(f"Missing target chunk for source_doc_uid={reference.source_doc_uid} target_chunk_number={target_chunk_number} standard_doc_uid={seed_state.source_standard_doc_uid}")
            continue
        if target_chunk.id not in context.state.selected_ids_by_doc.get(seed_state.source_standard_doc_uid, set()):
            _add_selected_chunk(
                doc_uid=seed_state.source_standard_doc_uid,
                chunk_id=target_chunk.id,
                provenance=Provenance.SAME_FAMILY_REFERENCE,
                state=context.state,
            )
            seed_state.chunks_added_for_seed += 1
            context.added_chunks_by_doc[seed_state.source_standard_doc_uid] = context.added_chunks_by_doc.get(seed_state.source_standard_doc_uid, 0) + 1
            added_chunks += 1
            logger.info(
                f"Added reference target: standard_doc_uid={seed_state.source_standard_doc_uid} "
                f"chunk_id={target_chunk.id} chunk_number={target_chunk.chunk_number} "
                f"provenance={Provenance.SAME_FAMILY_REFERENCE.value} depth_remaining={depth_remaining}"
            )
        else:
            logger.info(f"Reference target already selected: standard_doc_uid={seed_state.source_standard_doc_uid} chunk_id={target_chunk.id} chunk_number={target_chunk.chunk_number}")
        if reference.target_unit == "section":
            added_chunks += _expand_reference_target_section_subtree(
                target_chunk=target_chunk,
                target_chunk_number=target_chunk_number,
                seed_state=seed_state,
                context=context,
                processed_source_chunks=processed_source_chunks,
            )
        if depth_remaining > 1:
            logger.info(f"Descending into next-hop reference traversal from standard_doc_uid={seed_state.source_standard_doc_uid} chunk_number={target_chunk.chunk_number} remaining_depth={depth_remaining - 1}")
            added_chunks += _expand_reference_source_chunk(
                source_chunk=target_chunk,
                depth_remaining=depth_remaining - 1,
                seed_state=seed_state,
                context=context,
                processed_source_chunks=processed_source_chunks,
            )
    return added_chunks


def _find_first_chunk_with_prefix(
    *,
    chunks: list[Chunk],
    chunk_number_prefix: str,
) -> Chunk | None:
    prefix_with_separator = f"{chunk_number_prefix}."
    for chunk in chunks:
        if chunk.chunk_number == chunk_number_prefix or chunk.chunk_number.startswith(prefix_with_separator):
            return chunk
    return None


def _expand_reference_target_section_subtree(
    *,
    target_chunk: Chunk,
    target_chunk_number: str,
    seed_state: ReferenceExpansionSeedState,
    context: ReferenceExpansionContext,
    processed_source_chunks: set[tuple[str, int]],
) -> int:
    logger.info(f"Starting section fan-out for reference target chunk_number={target_chunk_number} anchor_chunk_number={target_chunk.chunk_number}")
    expanded_provenance = _section_expansion_provenance(Provenance.SAME_FAMILY_REFERENCE)
    added_chunks = 0
    target_chunk_prefix = f"{target_chunk_number}."
    for chunk in context.doc_chunks.get(seed_state.source_standard_doc_uid, []):
        if chunk.id is None:
            continue
        if chunk.chunk_number != target_chunk_number and not chunk.chunk_number.startswith(target_chunk_prefix):
            continue
        if (chunk.doc_uid, chunk.id) in processed_source_chunks:
            continue
        if chunk.id in context.state.selected_ids_by_doc.get(seed_state.source_standard_doc_uid, set()):
            continue
        _add_selected_chunk(
            doc_uid=seed_state.source_standard_doc_uid,
            chunk_id=chunk.id,
            provenance=expanded_provenance,
            state=context.state,
        )
        seed_state.chunks_added_for_seed += 1
        context.added_chunks_by_doc[seed_state.source_standard_doc_uid] = context.added_chunks_by_doc.get(seed_state.source_standard_doc_uid, 0) + 1
        added_chunks += 1
        logger.info(f"Added section fan-out target: standard_doc_uid={seed_state.source_standard_doc_uid} chunk_id={chunk.id} chunk_number={chunk.chunk_number} provenance={expanded_provenance.value}")
    return added_chunks


def _filter_seed_references(seed_chunk: Chunk, references: list[ContentReference]) -> list[ContentReference]:
    matching_references: list[ContentReference] = []
    for reference in references:
        if reference.source_location_type == "chunk" and reference.source_chunk_id == seed_chunk.chunk_id:
            matching_references.append(reference)
            continue
        if reference.source_location_type == "section" and reference.source_section_id is not None and reference.source_section_id == seed_chunk.containing_section_id:
            matching_references.append(reference)
    return matching_references


def _expand_chunks(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
    expansion_config: ExpansionConfig,
) -> list[SearchResult]:
    if not expansion_config.expand_to_section and expansion_config.expand <= 0 and expansion_config.full_doc_threshold <= 0 and not expansion_config.reference_expand_enabled:
        logger.info("Skipping chunk expansion because all expansion stages are disabled")
        return results

    logger.info(
        "Starting chunk expansion pipeline: "
        f"seed_results={len(results)} doc_count={len(doc_chunks)} "
        f"expand_to_section={expansion_config.expand_to_section} expand={expansion_config.expand} "
        f"full_doc_threshold={expansion_config.full_doc_threshold} "
        f"reference_expand_enabled={expansion_config.reference_expand_enabled} "
        f"reference_expand_depth={expansion_config.reference_expand_depth}"
    )
    result_score_by_chunk, state = _init_expansion_state(results)
    seed_chunk_summary = ", ".join(f"{doc_uid}={len(chunk_ids)}" for doc_uid, chunk_ids in state.selected_ids_by_doc.items())
    logger.debug(f"Seed chunk summary: {seed_chunk_summary}")
    _expand_same_family_references(
        seed_results=results,
        doc_chunks=doc_chunks,
        expansion_config=expansion_config,
        state=state,
    )
    current_results = _build_expanded_chunk_results(
        state=state,
        doc_chunks=doc_chunks,
        result_score_by_chunk=result_score_by_chunk,
    )
    if expansion_config.expand_to_section:
        _expand_to_section_subtrees(
            results=current_results,
            doc_chunks=doc_chunks,
            section_store=expansion_config.section_store,
            state=state,
            expand_to_section_doc_uids=expansion_config.expand_to_section_doc_uids,
        )
    full_doc_docs = _include_full_documents(
        doc_chunks=doc_chunks,
        state=state,
        full_doc_threshold=expansion_config.full_doc_threshold,
    )
    if expansion_config.expand > 0:
        _expand_with_neighbour_chunks(
            results=_build_expanded_chunk_results(state=state, doc_chunks=doc_chunks, result_score_by_chunk=result_score_by_chunk),
            doc_chunks=doc_chunks,
            state=state,
            expand=expansion_config.expand,
        )
    expanded_results = _build_expanded_chunk_results(state=state, doc_chunks=doc_chunks, result_score_by_chunk=result_score_by_chunk)
    logger.info(f"Completed chunk expansion pipeline: final_docs={len(state.selected_ids_by_doc)} final_chunks={len(expanded_results)} doc_order={state.doc_order}")
    for doc_uid in full_doc_docs:
        doc_size = sum(len(chunk.text) for chunk in doc_chunks.get(doc_uid, []))
        logger.info(f"Full doc inclusion: {doc_uid} (size={doc_size} < threshold={expansion_config.full_doc_threshold})")
    return expanded_results
