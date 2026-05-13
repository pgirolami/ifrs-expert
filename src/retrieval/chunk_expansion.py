"""Chunk, section, and same-family reference expansion for retrieval."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.models.provenance import Provenance
from src.retrieval.reference_expansion import _expand_same_family_references

if TYPE_CHECKING:
    from src.interfaces import ReadSectionStoreProtocol, ReferenceStoreProtocol, SearchResult
    from src.models.chunk import Chunk

logger = logging.getLogger(__name__)


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
    reference_expand_section_max_chunks_per_target: int


@dataclass
class ExpansionState:
    """Mutable expansion state shared across the post-retrieval stages."""

    selected_ids_by_doc: dict[str, set[int]]
    provenance_by_chunk: dict[tuple[str, int], Provenance]
    doc_order: list[str]

    chunks_added_for_seed: int = 0


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
        provenance_by_chunk[(doc_uid, chunk_id)] = Provenance(result["provenance"])
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
            source_provenance = state.provenance_by_chunk[(doc_uid, result["chunk_id"])]
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
        source_provenance = state.provenance_by_chunk[(doc_uid, chunk_id)]
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
                    "provenance": state.provenance_by_chunk[(doc_uid, chunk_id)],
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
    if source_provenance == Provenance.TOP_SIMILARITY:
        return Provenance.EXPAND_TO_ENCLOSING_SECTION
    if source_provenance == Provenance.TOP_SIMILARITY_FOR_SECTION_REFERENCE:
        return Provenance.EXPAND_TO_ENCLOSING_SECTION_OF_REFERENCED_CHUNK
    return Provenance.EXPAND_TO_ENCLOSING_SECTION_OF_REFERENCED_CHUNK


def _expand_chunks(
    ranked_results: list[SearchResult],
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
    ranked_result_score_by_chunk, _ = _init_expansion_state(ranked_results)
    seed_chunk_summary = ", ".join(f"{doc_uid}={len(chunk_ids)}" for doc_uid, chunk_ids in state.selected_ids_by_doc.items())
    logger.debug(f"Seed chunk summary: {seed_chunk_summary}")
    _expand_same_family_references(
        seed_results=results,
        doc_chunks=doc_chunks,
        result_score_by_chunk=result_score_by_chunk,
        ranked_result_score_by_chunk=ranked_result_score_by_chunk,
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
