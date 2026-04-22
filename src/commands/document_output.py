"""Helpers for document-level output formatting and logging."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import logging

    from src.interfaces import SearchResult
    from src.models.chunk import Chunk

TOP_CHUNK_PREVIEW_CHARS = 30


@dataclass(frozen=True)
class OutputDocumentSections:
    """Output summary for one document and its selected section labels."""

    doc_uid: str
    section_labels: list[str]


def build_output_document_sections(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
    logger: logging.Logger,
) -> list[OutputDocumentSections]:
    """Group selected chunks by document and log the top chunk for each output document."""
    doc_order, chunk_ids_by_doc = _index_selected_chunk_ids_by_doc(results)
    top_chunk_by_doc = _build_top_chunk_by_doc(results)

    summaries: list[OutputDocumentSections] = []
    for doc_uid in doc_order:
        section_labels = _build_section_labels_for_doc(
            doc_uid=doc_uid,
            doc_chunks=doc_chunks,
            chunk_ids_by_doc=chunk_ids_by_doc,
            top_chunk_by_doc=top_chunk_by_doc,
            logger=logger,
        )
        summaries.append(OutputDocumentSections(doc_uid=doc_uid, section_labels=section_labels))
    return summaries


def _index_selected_chunk_ids_by_doc(results: list[SearchResult]) -> tuple[list[str], dict[str, set[int]]]:
    doc_order: list[str] = []
    chunk_ids_by_doc: dict[str, set[int]] = {}
    for result in results:
        doc_uid = str(result["doc_uid"])
        chunk_id = int(result["chunk_id"])
        if doc_uid not in chunk_ids_by_doc:
            chunk_ids_by_doc[doc_uid] = set()
            doc_order.append(doc_uid)
        chunk_ids_by_doc[doc_uid].add(chunk_id)
    return doc_order, chunk_ids_by_doc


def _build_top_chunk_by_doc(results: list[SearchResult]) -> dict[str, tuple[int, float]]:
    top_chunk_by_doc: dict[str, tuple[int, float]] = {}
    for result in results:
        doc_uid = str(result["doc_uid"])
        chunk_id = int(result["chunk_id"])
        score = float(result["score"])
        existing_top_chunk = top_chunk_by_doc.get(doc_uid)
        if existing_top_chunk is None or score > existing_top_chunk[1]:
            top_chunk_by_doc[doc_uid] = (chunk_id, score)
    return top_chunk_by_doc


def _build_section_labels_for_doc(
    *,
    doc_uid: str,
    doc_chunks: dict[str, list[Chunk]],
    chunk_ids_by_doc: dict[str, set[int]],
    top_chunk_by_doc: dict[str, tuple[int, float]],
    logger: logging.Logger,
) -> list[str]:
    section_labels: list[str] = []
    seen_sections: set[str] = set()
    top_chunk_logged = False
    top_chunk_id, top_chunk_score = top_chunk_by_doc.get(doc_uid, (-1, 0.0))
    for chunk in doc_chunks.get(doc_uid, []):
        chunk_id = chunk.id
        if chunk_id is None:
            continue
        if chunk_id not in chunk_ids_by_doc.get(doc_uid, set()):
            continue
        section_label = chunk.chunk_number or f"chunk {chunk_id}"
        if not top_chunk_logged and chunk_id == top_chunk_id:
            section_preview = " ".join(chunk.text.split())[:TOP_CHUNK_PREVIEW_CHARS]
            logger.info(f"Output document top chunk doc_uid={doc_uid}; section_number={section_label}; score={top_chunk_score:.4f}; section_text_preview='{section_preview}'")
            top_chunk_logged = True
        if section_label in seen_sections:
            continue
        seen_sections.add(section_label)
        section_labels.append(section_label)
    return section_labels
