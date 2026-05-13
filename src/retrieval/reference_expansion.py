"""Same-family reference expansion for retrieval chunks."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.models.document import resolve_standard_doc_uid
from src.models.provenance import Provenance
from src.models.reference import ContentReference
from src.retrieval.retrieval_contract import expand_chunk_number_range

if TYPE_CHECKING:
    from src.interfaces import ReferenceStoreProtocol, SearchResult
    from src.models.chunk import Chunk
    from src.models.section import SectionRecord
    from src.retrieval.chunk_expansion import ExpansionConfig, ExpansionState

logger = logging.getLogger(__name__)


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


@dataclass
class ReferenceExpansionContext:
    """Inputs needed to expand same-family references for seed chunks."""

    doc_chunks: dict[str, list[Chunk]]
    references_by_doc: dict[str, list[ContentReference]]
    result_score_by_chunk: dict[tuple[str, int], float]
    ranked_result_score_by_chunk: dict[tuple[str, int], float]
    expansion_config: ExpansionConfig
    state: ExpansionState
    added_chunks_by_doc: dict[str, int]


@dataclass
class ReferenceExpansionSeedState:
    """Per-seed expansion state used while traversing references."""

    source_standard_doc_uid: str
    chunks_added_for_seed: int = 0


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


def _expand_same_family_references(  # noqa: PLR0913
    *,
    seed_results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
    result_score_by_chunk: dict[tuple[str, int], float],
    ranked_result_score_by_chunk: dict[tuple[str, int], float],
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
        result_score_by_chunk=result_score_by_chunk,
        ranked_result_score_by_chunk=ranked_result_score_by_chunk,
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
        if reference.target_unit == "section":
            added_chunks += _expand_reference_target_section_roots(
                target_chunk=target_chunk,
                target_chunk_number=target_chunk_number,
                seed_state=seed_state,
                context=context,
            )
        elif target_chunk.id not in context.state.selected_ids_by_doc.get(seed_state.source_standard_doc_uid, set()):
            _add_selected_chunk(
                doc_uid=seed_state.source_standard_doc_uid,
                chunk_id=target_chunk.id,
                provenance=Provenance.EXPAND_TO_REFERENCED_CHUNK,
                state=context.state,
            )
            seed_state.chunks_added_for_seed += 1
            context.added_chunks_by_doc[seed_state.source_standard_doc_uid] = context.added_chunks_by_doc.get(seed_state.source_standard_doc_uid, 0) + 1
            added_chunks += 1
            logger.info(
                f"Added reference target: standard_doc_uid={seed_state.source_standard_doc_uid} "
                f"chunk_id={target_chunk.id} chunk_number={target_chunk.chunk_number} "
                f"provenance={Provenance.EXPAND_TO_REFERENCED_CHUNK.value} depth_remaining={depth_remaining}"
            )
        else:
            logger.info(f"Reference target already selected: standard_doc_uid={seed_state.source_standard_doc_uid} chunk_id={target_chunk.id} chunk_number={target_chunk.chunk_number}")
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


def _resolve_reference_target_section_db_id(
    *,
    target_chunk: Chunk,
    target_chunk_number: str,
    section_by_source_id: dict[str, SectionRecord],
) -> int | None:
    target_section = _resolve_chunk_section_record(
        chunk=target_chunk,
        section_by_source_id=section_by_source_id,
    )
    if target_section is None or target_section.db_id is None:
        return None
    if target_chunk.chunk_number == target_chunk_number:
        return target_section.db_id
    if target_section.parent_section_db_id is not None:
        return target_section.parent_section_db_id
    return target_section.db_id


def _resolve_chunk_section_record(
    *,
    chunk: Chunk,
    section_by_source_id: dict[str, SectionRecord],
) -> SectionRecord | None:
    if chunk.containing_section_id is None:
        return None
    return section_by_source_id.get(chunk.containing_section_id)


def _select_top_chunks_within_section_subtree(
    *,
    context: ReferenceExpansionContext,
    doc_uid: str,
    section_db_ids: set[int],
    section_db_id_by_source_id: dict[str, int],
    limit: int,
) -> list[Chunk]:
    if limit <= 0:
        logger.info(f"Skipping section-target top-n selection for doc_uid={doc_uid} because the configured limit is {limit}")
        return []
    scored_candidates: list[tuple[float, str, int, Chunk]] = []
    for chunk in context.doc_chunks.get(doc_uid, []):
        if chunk.id is None:
            continue
        chunk_score = context.ranked_result_score_by_chunk.get((doc_uid, chunk.id))
        if chunk_score is None:
            continue
        chunk_section_db_id = _resolve_chunk_section_db_id(
            chunk=chunk,
            section_db_id_by_source_id=section_db_id_by_source_id,
        )
        if chunk_section_db_id is None or chunk_section_db_id not in section_db_ids:
            continue
        scored_candidates.append((-chunk_score, chunk.chunk_number, chunk.id, chunk))
    scored_candidates.sort()
    selected_candidates = [candidate[3] for candidate in scored_candidates[:limit]]
    logger.info(f"Ranked section-target candidates for doc_uid={doc_uid} subtree_sections={len(section_db_ids)} candidate_count={len(scored_candidates)} selected_count={len(selected_candidates)} limit={limit}")
    for rank, candidate in enumerate(scored_candidates[:limit], start=1):
        logger.info(f"Section-target candidate rank={rank} doc_uid={doc_uid} chunk_id={candidate[2]} chunk_number={candidate[1]} score={-candidate[0]:.4f}")
    return selected_candidates


def _expand_reference_target_section_roots(
    *,
    target_chunk: Chunk,
    target_chunk_number: str,
    seed_state: ReferenceExpansionSeedState,
    context: ReferenceExpansionContext,
) -> int:
    section_store = context.expansion_config.section_store
    if section_store is None:
        logger.info(f"Skipping section-root selection for reference target chunk_number={target_chunk_number} because no section store is configured")
        return 0

    with section_store as active_section_store:
        sections_by_source_id = {section.section_id: section for section in active_section_store.get_sections_by_doc(seed_state.source_standard_doc_uid)}
        target_section_db_id = _resolve_reference_target_section_db_id(
            target_chunk=target_chunk,
            target_chunk_number=target_chunk_number,
            section_by_source_id=sections_by_source_id,
        )
        if target_section_db_id is None:
            logger.info(f"Skipping section-root selection for reference target chunk_number={target_chunk_number} because no containing section db id was resolved")
            return 0
        descendant_section_db_ids = set(active_section_store.get_descendant_section_db_ids(target_section_db_id))

    if not descendant_section_db_ids:
        logger.info(f"Skipping section-root selection for reference target chunk_number={target_chunk_number} because the section subtree is empty")
        return 0

    candidate_chunks = _select_top_chunks_within_section_subtree(
        context=context,
        doc_uid=seed_state.source_standard_doc_uid,
        section_db_ids=descendant_section_db_ids,
        section_db_id_by_source_id={section.section_id: section.db_id for section in sections_by_source_id.values() if section.db_id is not None},
        limit=context.expansion_config.reference_expand_section_max_chunks_per_target,
    )
    if not candidate_chunks:
        logger.info(f"Skipping section-root selection for reference target chunk_number={target_chunk_number} because no scored chunks were found in the subtree")
        return 0

    expanded_provenance = Provenance.TOP_SIMILARITY_FOR_SECTION_REFERENCE
    added_chunks = 0
    logger.info(f"Selecting top {len(candidate_chunks)} section roots for reference target chunk_number={target_chunk_number} anchor_chunk_number={target_chunk.chunk_number}")
    for chunk in candidate_chunks:
        if chunk.id is None:
            continue
        if chunk.id in context.state.selected_ids_by_doc.get(seed_state.source_standard_doc_uid, set()):
            logger.info(f"Section root already selected; keeping first provenance: standard_doc_uid={seed_state.source_standard_doc_uid} chunk_id={chunk.id} chunk_number={chunk.chunk_number}")
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
        chunk_key = (seed_state.source_standard_doc_uid, chunk.id)
        logger.info(
            f"Added section root candidate: standard_doc_uid={seed_state.source_standard_doc_uid} "
            f"chunk_id={chunk.id} chunk_number={chunk.chunk_number} score={context.result_score_by_chunk.get(chunk_key, 0.0):.4f} "
            f"provenance={expanded_provenance.value}"
        )
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
