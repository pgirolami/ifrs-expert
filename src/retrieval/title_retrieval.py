"""Shared title-retrieval helpers for query-titles and answer flows."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.commands.constants import DEFAULT_MIN_SCORE, DEFAULT_RETRIEVAL_K

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from src.interfaces import ReadChunkStoreProtocol, ReadSectionStoreProtocol, SearchTitleVectorStoreProtocol, TitleSearchResult
    from src.models.chunk import Chunk
    from src.models.section import SectionRecord


@dataclass(frozen=True)
class TitleRetrievalConfig:
    """Dependencies required for title retrieval."""

    title_vector_store: SearchTitleVectorStoreProtocol
    section_store: ReadSectionStoreProtocol
    chunk_store: ReadChunkStoreProtocol
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[], Path]


@dataclass(frozen=True)
class TitleRetrievalOptions:
    """Options for title retrieval."""

    k: int = DEFAULT_RETRIEVAL_K
    min_score: float = DEFAULT_MIN_SCORE


@dataclass(frozen=True)
class TitleRetrievalHit:
    """One matched section title and its resolved paragraph chunks."""

    section: SectionRecord
    score: float
    chunks: list[Chunk]


@dataclass(frozen=True)
class _SectionResolutionContext:
    """Resolved section lookup state for title expansion."""

    sections_by_key: dict[tuple[str, str], SectionRecord]
    section_db_id_by_source_id_by_doc: dict[str, dict[str, int]]
    descendant_db_ids_by_key: dict[tuple[str, str], list[int]]


def retrieve_title_hits(
    query: str,
    config: TitleRetrievalConfig,
    options: TitleRetrievalOptions,
) -> tuple[str | None, list[TitleRetrievalHit]]:
    """Retrieve matched title sections and expand them to descendant chunks."""
    index_path = config.index_path_fn()
    if not index_path.exists():
        return "Error: No title index found. Please run 'store' command first.", []

    with config.title_vector_store as title_vector_store:
        ranked_results = title_vector_store.search_all(query)

    if not ranked_results:
        return "Error: No title sections retrieved", []

    selected_results = _select_top_k_per_document(ranked_results, options.k, options.min_score)
    if not selected_results:
        return f"Error: No title sections found with score >= {options.min_score}", []

    config.init_db_fn()

    doc_uids = list({result["doc_uid"] for result in selected_results})
    doc_chunks: dict[str, list[Chunk]] = {}

    with config.chunk_store as chunk_store, config.section_store as section_store:
        for doc_uid in doc_uids:
            doc_chunks[doc_uid] = chunk_store.get_chunks_by_doc(doc_uid)
        resolution_context = _build_section_resolution_context(
            selected_results=selected_results,
            doc_uids=doc_uids,
            section_store=section_store,
        )

    hits = _build_hits(
        selected_results=selected_results,
        doc_chunks=doc_chunks,
        resolution_context=resolution_context,
    )
    return None, hits


def flatten_title_hits(hits: list[TitleRetrievalHit]) -> list[Chunk]:
    """Flatten hits into one ordered unique chunk list."""
    unique_chunks: list[Chunk] = []
    seen_chunk_ids: set[tuple[str, int]] = set()
    for hit in hits:
        for chunk in hit.chunks:
            if chunk.id is None:
                continue
            chunk_key = (chunk.doc_uid, chunk.id)
            if chunk_key in seen_chunk_ids:
                continue
            seen_chunk_ids.add(chunk_key)
            unique_chunks.append(chunk)
    return unique_chunks


def _select_top_k_per_document(
    ranked_results: list[TitleSearchResult],
    k: int,
    min_score: float,
) -> list[TitleSearchResult]:
    selected_results: list[TitleSearchResult] = []
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


def _build_section_resolution_context(
    selected_results: list[TitleSearchResult],
    doc_uids: list[str],
    section_store: ReadSectionStoreProtocol,
) -> _SectionResolutionContext:
    sections_by_key: dict[tuple[str, str], SectionRecord] = {}
    section_db_id_by_source_id_by_doc: dict[str, dict[str, int]] = {}
    descendant_db_ids_by_key: dict[tuple[str, str], list[int]] = {}

    for doc_uid in doc_uids:
        sections = section_store.get_sections_by_doc(doc_uid)
        section_db_id_by_source_id_by_doc[doc_uid] = {section.section_id: section.db_id for section in sections if section.db_id is not None}
        for section in sections:
            sections_by_key[(doc_uid, section.section_id)] = section

    for result in selected_results:
        section_key = (result["doc_uid"], result["section_id"])
        section = sections_by_key.get(section_key)
        if section is None:
            section = section_store.get_section_by_source_id(
                doc_uid=result["doc_uid"],
                section_id=result["section_id"],
            )
            if section is not None:
                sections_by_key[section_key] = section
        if section is None or section.db_id is None:
            continue
        descendant_db_ids_by_key[section_key] = section_store.get_descendant_section_db_ids(section.db_id)

    return _SectionResolutionContext(
        sections_by_key=sections_by_key,
        section_db_id_by_source_id_by_doc=section_db_id_by_source_id_by_doc,
        descendant_db_ids_by_key=descendant_db_ids_by_key,
    )


def _build_hits(
    selected_results: list[TitleSearchResult],
    doc_chunks: dict[str, list[Chunk]],
    resolution_context: _SectionResolutionContext,
) -> list[TitleRetrievalHit]:
    hits: list[TitleRetrievalHit] = []

    for result in selected_results:
        doc_uid = result["doc_uid"]
        section_key = (doc_uid, result["section_id"])
        section = resolution_context.sections_by_key.get(section_key)
        if section is None:
            continue

        descendant_db_ids = set(
            resolution_context.descendant_db_ids_by_key.get(
                section_key,
                [section.db_id] if section.db_id is not None else [],
            )
        )
        section_db_id_by_source_id = resolution_context.section_db_id_by_source_id_by_doc.get(doc_uid, {})
        matched_chunks = [chunk for chunk in doc_chunks.get(doc_uid, []) if _resolve_chunk_section_db_id(chunk, section_db_id_by_source_id) in descendant_db_ids]

        hits.append(TitleRetrievalHit(section=section, score=result["score"], chunks=matched_chunks))

    return hits


def _resolve_chunk_section_db_id(
    chunk: Chunk,
    section_db_id_by_source_id: dict[str, int],
) -> int | None:
    if chunk.containing_section_db_id is not None:
        return chunk.containing_section_db_id
    if chunk.containing_section_id is None:
        return None
    return section_db_id_by_source_id.get(chunk.containing_section_id)
