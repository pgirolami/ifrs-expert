"""Build document-level retrieval representations from extracted content."""

from __future__ import annotations

import logging
from dataclasses import dataclass, replace
from typing import TYPE_CHECKING

from src.vector.constants import MAX_EMBEDDING_TEXT_CHARS

if TYPE_CHECKING:
    from src.models.chunk import Chunk
    from src.models.document import DocumentRecord
    from src.models.section import SectionClosureRow, SectionRecord

logger = logging.getLogger(__name__)

SECTION_FIELD_BY_NORMALIZED_TITLE: dict[str, str] = {
    "background": "background_text",
    "issue": "issue_text",
    "objective": "objective_text",
    "scope": "scope_text",
    "introduction": "intro_text",
}
EMBEDDING_LABEL_BY_FIELD: dict[str, str] = {
    "source_title": "Title",
    "background_text": "Background",
    "issue_text": "Issue",
    "objective_text": "Objective",
    "scope_text": "Scope",
    "intro_text": "Introduction",
}


@dataclass(frozen=True)
class BuiltDocumentProfile:
    """One enriched document record plus its transient embedding text."""

    document: DocumentRecord
    embedding_text: str


@dataclass(frozen=True)
class _EmbeddingPart:
    """One labeled part of the document representation."""

    field_name: str
    label: str
    text: str


class DocumentProfileBuilder:
    """Build a compact document-level representation for retrieval."""

    def __init__(self, max_embedding_chars: int = MAX_EMBEDDING_TEXT_CHARS) -> None:
        """Initialize the document profile builder."""
        self._max_embedding_chars = max_embedding_chars

    def build(
        self,
        document: DocumentRecord,
        chunks: list[Chunk],
        sections: list[SectionRecord],
        section_closure_rows: list[SectionClosureRow],
    ) -> BuiltDocumentProfile:
        """Build one enriched document record and its embedding text."""
        logger.info(f"Building document representation for doc_uid={document.doc_uid}, source_type={document.source_type}, chunk_count={len(chunks)}, section_count={len(sections)}")
        descendant_ids_by_ancestor = _build_descendant_ids_by_ancestor(section_closure_rows)
        field_values = _extract_section_field_values(
            doc_uid=document.doc_uid,
            chunks=chunks,
            sections=sections,
            descendant_ids_by_ancestor=descendant_ids_by_ancestor,
        )

        if field_values.get("intro_text") is None:
            intro_text = _build_intro_fallback(doc_uid=document.doc_uid, source_type=document.source_type, chunks=chunks)
            if intro_text is not None:
                field_values["intro_text"] = intro_text

        enriched_document = replace(
            document,
            background_text=field_values.get("background_text"),
            issue_text=field_values.get("issue_text"),
            objective_text=field_values.get("objective_text"),
            scope_text=field_values.get("scope_text"),
            intro_text=field_values.get("intro_text"),
        )
        embedding_text = _build_embedding_text(
            document=enriched_document,
            max_embedding_chars=self._max_embedding_chars,
        )
        populated_fields = [field_name for field_name in ("background_text", "issue_text", "objective_text", "scope_text", "intro_text") if getattr(enriched_document, field_name) is not None]
        logger.info(f"Built document representation for doc_uid={document.doc_uid}; populated_fields={populated_fields}, embedding_chars={len(embedding_text)}")
        return BuiltDocumentProfile(document=enriched_document, embedding_text=embedding_text)


def _build_descendant_ids_by_ancestor(
    section_closure_rows: list[SectionClosureRow],
) -> dict[str, set[str]]:
    descendant_ids_by_ancestor: dict[str, set[str]] = {}
    for row in section_closure_rows:
        descendant_ids_by_ancestor.setdefault(row.ancestor_section_id, set()).add(row.descendant_section_id)
    logger.info(f"Built descendant-id map for document representation with {len(descendant_ids_by_ancestor)} ancestor sections")
    return descendant_ids_by_ancestor


def _extract_section_field_values(
    doc_uid: str,
    chunks: list[Chunk],
    sections: list[SectionRecord],
    descendant_ids_by_ancestor: dict[str, set[str]],
) -> dict[str, str]:
    field_values: dict[str, str] = {}
    for section in sorted(sections, key=lambda item: item.position):
        normalized_title = _normalize_section_title(section.title)
        field_name = SECTION_FIELD_BY_NORMALIZED_TITLE.get(normalized_title)
        if field_name is None:
            continue
        if field_name in field_values:
            logger.info(f"Skipping section title={section.title!r} for doc_uid={doc_uid} because field {field_name} is already populated")
            continue

        descendant_ids = descendant_ids_by_ancestor.get(section.section_id, {section.section_id})
        matching_text = _collect_section_text(
            doc_uid=doc_uid,
            field_name=field_name,
            section_title=section.title,
            chunks=chunks,
            descendant_ids=descendant_ids,
        )
        if matching_text:
            field_values[field_name] = matching_text
            logger.info(f"Populated {field_name} for doc_uid={doc_uid} from section title={section.title!r} with {len(matching_text)} chars")
        else:
            logger.info(f"Matched section title={section.title!r} for doc_uid={doc_uid}, but found no chunk text for {field_name}")

    return field_values


def _normalize_section_title(title: str) -> str:
    return " ".join(title.strip().lower().split())


def _collect_section_text(
    doc_uid: str,
    field_name: str,
    section_title: str,
    chunks: list[Chunk],
    descendant_ids: set[str],
) -> str | None:
    matching_chunks = [chunk.text for chunk in chunks if chunk.containing_section_id in descendant_ids and chunk.text]
    if not matching_chunks:
        return None

    section_text = "\n".join(matching_chunks)
    logger.info(f"Collected {len(matching_chunks)} chunk(s) for doc_uid={doc_uid}, field={field_name}, section_title={section_title!r}, raw_chars={len(section_text)}")
    return section_text


def _build_intro_fallback(doc_uid: str, source_type: str, chunks: list[Chunk]) -> str | None:
    if source_type != "pdf":
        logger.info(f"Skipping introduction fallback for doc_uid={doc_uid} because source_type={source_type} is not pdf")
        return None

    if not chunks:
        logger.warning(f"Cannot build intro fallback for doc_uid={doc_uid} because there are no chunks")
        return None

    intro_text = "\n".join(chunk.text for chunk in chunks if chunk.text)
    if not intro_text:
        logger.warning(f"Cannot build intro fallback for doc_uid={doc_uid} because all candidate chunks are empty")
        return None

    logger.info(f"Built PDF introduction fallback for doc_uid={doc_uid} with raw_chars={len(intro_text)}")
    return intro_text


def _build_embedding_text(document: DocumentRecord, max_embedding_chars: int) -> str:
    parts = _build_embedding_parts(document)
    if not parts:
        logger.warning(f"Built empty document embedding text for doc_uid={document.doc_uid}")
        return ""

    title_part = next((part for part in parts if part.field_name == "source_title"), None)
    truncatable_parts = [part for part in parts if part.field_name != "source_title"]

    title_line = _build_part_line(title_part) if title_part is not None else None
    title_text_chars = len(title_part.text) if title_part is not None else 0
    title_chars = len(title_line) if title_line is not None else 0
    newline_after_title_chars = 1 if title_line is not None and truncatable_parts else 0
    line_prefix_chars = sum(len(f"{part.label}: ") for part in truncatable_parts)
    newline_chars = max(0, len(truncatable_parts) - 1)
    raw_content_chars = sum(len(part.text) for part in truncatable_parts)
    available_content_chars = max_embedding_chars - title_chars - newline_after_title_chars - line_prefix_chars - newline_chars

    logger.info(
        f"Building embedding text for doc_uid={document.doc_uid}; title_chars={title_chars}, "
        f"truncatable_part_count={len(truncatable_parts)}, raw_content_chars={raw_content_chars}, "
        f"line_prefix_chars={line_prefix_chars}, newline_chars={newline_chars}, "
        f"max_embedding_chars={max_embedding_chars}, available_content_chars={available_content_chars}"
    )

    lines: list[str] = []
    if title_line is not None:
        logger.info(f"Preserving full title for doc_uid={document.doc_uid} with chars={title_text_chars}")
        lines.append(title_line)

    if not truncatable_parts:
        embedding_text = "\n".join(lines)
        logger.info(f"Built embedding text for doc_uid={document.doc_uid} with chars={len(embedding_text)}")
        return embedding_text

    if available_content_chars <= 0:
        logger.warning(f"No content budget remains after preserving the title for doc_uid={document.doc_uid}; omitting non-title parts")
        embedding_text = "\n".join(lines)
        logger.info(f"Built embedding text for doc_uid={document.doc_uid} with chars={len(embedding_text)}")
        return embedding_text

    truncated_texts_by_field = _truncate_parts_proportionally(
        doc_uid=document.doc_uid,
        parts=truncatable_parts,
        available_content_chars=available_content_chars,
    )
    lines.extend(_build_part_line(part, truncated_texts_by_field[part.field_name]) for part in truncatable_parts if truncated_texts_by_field[part.field_name])
    embedding_text = "\n".join(lines)
    logger.info(f"Built embedding text for doc_uid={document.doc_uid} with chars={len(embedding_text)}")
    return embedding_text


def _build_embedding_parts(document: DocumentRecord) -> list[_EmbeddingPart]:
    parts: list[_EmbeddingPart] = []
    for field_name in (
        "source_title",
        "background_text",
        "issue_text",
        "objective_text",
        "scope_text",
        "intro_text",
    ):
        field_value = getattr(document, field_name)
        if field_value is None or not field_value.strip():
            continue
        parts.append(
            _EmbeddingPart(
                field_name=field_name,
                label=EMBEDDING_LABEL_BY_FIELD[field_name],
                text=field_value,
            )
        )
    return parts


def _build_part_line(part: _EmbeddingPart, text: str | None = None) -> str:
    resolved_text = part.text if text is None else text
    return f"{part.label}: {resolved_text}"


def _truncate_parts_proportionally(
    doc_uid: str,
    parts: list[_EmbeddingPart],
    available_content_chars: int,
) -> dict[str, str]:
    raw_content_chars = sum(len(part.text) for part in parts)
    if raw_content_chars <= available_content_chars:
        logger.info(f"No proportional truncation needed for doc_uid={doc_uid}; raw_content_chars={raw_content_chars}, available_content_chars={available_content_chars}")
        return {part.field_name: part.text for part in parts}

    budgets = _allocate_proportional_budgets(parts=parts, available_content_chars=available_content_chars)
    truncated_texts_by_field: dict[str, str] = {}
    for part in parts:
        raw_len = len(part.text)
        raw_share_percent = (raw_len / raw_content_chars) * 100 if raw_content_chars > 0 else 0.0
        allocated_chars = budgets[part.field_name]
        allocated_share_percent = (allocated_chars / available_content_chars) * 100 if available_content_chars > 0 else 0.0
        if raw_len > allocated_chars:
            logger.warning(
                f"Truncating document part for doc_uid={doc_uid}, field={part.field_name}, label={part.label}; "
                f"raw_chars={raw_len}, allocated_chars={allocated_chars}, "
                f"raw_share_percent={raw_share_percent:.2f}, allocated_share_percent={allocated_share_percent:.2f}"
            )
        else:
            logger.info(
                f"Keeping full document part for doc_uid={doc_uid}, field={part.field_name}, label={part.label}; "
                f"raw_chars={raw_len}, allocated_chars={allocated_chars}, "
                f"raw_share_percent={raw_share_percent:.2f}, allocated_share_percent={allocated_share_percent:.2f}"
            )
        truncated_texts_by_field[part.field_name] = part.text[:allocated_chars].rstrip()
    return truncated_texts_by_field


def _allocate_proportional_budgets(
    parts: list[_EmbeddingPart],
    available_content_chars: int,
) -> dict[str, int]:
    raw_lengths_by_field = {part.field_name: len(part.text) for part in parts}
    raw_total = sum(raw_lengths_by_field.values())
    if raw_total == 0:
        return {part.field_name: 0 for part in parts}

    minimum_budget_per_part = 1 if available_content_chars >= len(parts) else 0
    budgets = {part.field_name: minimum_budget_per_part for part in parts}
    remaining_budget = available_content_chars - (minimum_budget_per_part * len(parts))
    remaining_budget = max(remaining_budget, 0)

    raw_lengths_after_minimum = {part.field_name: max(0, raw_lengths_by_field[part.field_name] - minimum_budget_per_part) for part in parts}
    weighted_total_after_minimum = sum(raw_lengths_after_minimum.values())
    if weighted_total_after_minimum == 0:
        return budgets

    fractional_allocations: list[tuple[float, str]] = []
    for part in parts:
        field_name = part.field_name
        max_additional_chars = raw_lengths_after_minimum[field_name]
        if max_additional_chars == 0:
            fractional_allocations.append((0.0, field_name))
            continue
        exact_additional_chars = (remaining_budget * max_additional_chars) / weighted_total_after_minimum
        floored_additional_chars = min(max_additional_chars, int(exact_additional_chars))
        budgets[field_name] += floored_additional_chars
        fractional_allocations.append((exact_additional_chars - floored_additional_chars, field_name))

    distributed_budget = sum(budgets.values())
    leftover_budget = available_content_chars - distributed_budget
    for _, field_name in sorted(fractional_allocations, reverse=True):
        if leftover_budget <= 0:
            break
        if budgets[field_name] >= raw_lengths_by_field[field_name]:
            continue
        budgets[field_name] += 1
        leftover_budget -= 1

    return budgets
