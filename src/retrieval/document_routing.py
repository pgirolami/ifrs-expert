"""Document routing helpers for retrieval."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from src.models.document import DOCUMENT_TYPES, infer_exact_document_type, resolve_standard_doc_uid
from src.retrieval.models import DocumentHit

if TYPE_CHECKING:
    from src.interfaces import DocumentSearchResult, SearchDocumentVectorStoreProtocol, SearchResult
    from src.retrieval.models import RetrievalRequest
    from src.retrieval.pipeline import RetrievalPipelineConfig

logger = logging.getLogger(__name__)


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
