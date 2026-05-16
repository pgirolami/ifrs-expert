"""Formatting helpers for answer workflow output."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.models.answer_command_result import RetrievedChunkHit
from src.models.document import infer_document_kind, infer_exact_document_type
from src.models.provenance import Provenance

if TYPE_CHECKING:
    from logging import Logger

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
    logger: Logger,
) -> list[OutputDocumentSections]:
    """Summarize retrieved sections per document."""
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


def build_retrieved_chunk_hits(results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> list[RetrievedChunkHit]:
    """Build serializable chunk hits from the retrieval result."""
    chunk_hits: list[RetrievedChunkHit] = []
    for result in results:
        doc_uid = str(result["doc_uid"])
        chunk_db_id = int(result["chunk_id"])
        score = float(result["score"])
        document_type = infer_exact_document_type(doc_uid)
        document_kind = infer_document_kind(doc_uid)
        for chunk in doc_chunks.get(doc_uid, []):
            if chunk.id != chunk_db_id:
                continue
            provenance_value = result.get("provenance")
            provenance = Provenance(provenance_value) if provenance_value is not None else None
            chunk_hits.append(
                RetrievedChunkHit(
                    doc_uid=doc_uid,
                    chunk_number=chunk.chunk_number,
                    chunk_id=chunk.chunk_id,
                    score=round(score, 4),
                    document_type=document_type,
                    document_kind=document_kind,
                    containing_section_id=chunk.containing_section_id,
                    containing_section_db_id=chunk.containing_section_db_id,
                    page_start=chunk.page_start,
                    page_end=chunk.page_end,
                    text=chunk.text,
                    provenance=provenance,
                )
            )
            break
    return chunk_hits


def build_chunk_summary(results: list[SearchResult], doc_chunks: dict[str, list[Chunk]], logger: Logger) -> str:
    """Render a human-readable retrieved-chunks summary."""
    if not results:
        return "Retrieved chunks:\n- none"
    summaries = build_output_document_sections(results=results, doc_chunks=doc_chunks, logger=logger)
    lines: list[str] = ["Retrieved chunks:"]
    for summary in summaries:
        sections_text = ", ".join(summary.section_labels) if summary.section_labels else "(no sections)"
        lines.append(f"- {summary.doc_uid}: {sections_text}")
    return "\n".join(lines)


def escape_xml(text: str) -> str:
    """Escape XML metacharacters in text."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")


def extract_prompt_content(full_output: str) -> str:
    """Trim prompt noise before the model content."""
    lines = full_output.split("\n")
    start_idx = 0
    for index, line in enumerate(lines):
        if line.startswith("You are an IFRS expert"):
            start_idx = index
            break
    return "\n".join(lines[start_idx:])


def extract_doc_uids_from_context(context: str) -> list[str]:
    """Extract unique document UIDs from rendered context XML."""
    doc_uids: list[str] = []
    for match in re.finditer(r'<Document\s+[^>]*name="([^"]+)"[^>]*>', context):
        doc_uid = match.group(1)
        if doc_uid not in doc_uids:
            doc_uids.append(doc_uid)
    return doc_uids


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
    logger: Logger,
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
