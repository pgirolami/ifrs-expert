"""Section filtering for the store command.

This module provides filtering logic to exclude certain sections and chunks
from being stored based on their titles and content.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.chunk import Chunk
    from src.models.section import SectionClosureRow, SectionRecord

# Section titles to exclude (exact match, case-sensitive)
EXCLUDED_SECTION_TITLES: frozenset[str] = frozenset(
    {
        "References",
        "Contents",
        "Effective Date and transition",
        "Effective date",
        "Date of consensus",
        "Transition",
        "Table of Concordance",
        "Board Approvals",
        "Dissenting opinion",
        "Dissenting opinions",
    }
)

# Section title prefixes to exclude (case-sensitive)
EXCLUDED_SECTION_TITLE_PREFIXES: frozenset[str] = frozenset(
    {
        "Withdrawal of",
        "Amendments to",
        "Amendment to",
    }
)

# Text patterns to exclude chunks containing these patterns
EXCLUDED_CHUNK_TEXTS: frozenset[str] = frozenset(
    {
        "[Deleted]",
        "These paragraphs refer to amendments that are not yet effective",
        "This paragraph refers to amendments that are not yet effective",
    }
)


@dataclass(frozen=True)
class FilteredExtractionResult:
    """Result of filtering an extracted document."""

    chunks: list[Chunk]
    sections: list[SectionRecord]
    closure_rows: list[SectionClosureRow]
    excluded_section_count: int
    excluded_chunk_count: int
    excluded_section_titles: tuple[str, ...]
    excluded_chunk_ids: tuple[str, ...]


def filter_extraction(
    chunks: list[Chunk],
    sections: list[SectionRecord],
    closure_rows: list[SectionClosureRow],
) -> FilteredExtractionResult:
    """Filter out excluded sections and chunks.

    This function:
    1. Identifies sections with excluded titles (exact match or prefix match)
    2. Uses closure rows to find all descendants of excluded sections
    3. Filters out excluded sections and their closure rows
    4. Filters out chunks belonging to excluded sections
    5. Filters out chunks containing exactly "[Deleted]"

    Args:
        chunks: List of extracted chunks
        sections: List of extracted sections
        closure_rows: List of section ancestor/descendant relationships

    Returns:
        FilteredExtractionResult with unwanted sections and chunks removed
    """
    # Build a set of section IDs that directly matched a section filter
    directly_excluded_section_ids = _find_excluded_section_ids(sections)
    directly_excluded_section_ids |= _find_contextual_excluded_section_ids(sections, closure_rows)

    # Count of sections that directly matched a filter (for logging)
    excluded_section_count = len(directly_excluded_section_ids)

    # Track excluded section titles for logging
    excluded_section_titles = tuple(section.title for section in sections if section.section_id in directly_excluded_section_ids)

    section_by_id = {section.section_id: section for section in sections}
    descendant_excluded_section_ids = {section_id for section_id in directly_excluded_section_ids if _should_cascade_section_exclusion(section_by_id.get(section_id))}

    # Find all descendant section IDs of excluded sections
    descendant_ids = _find_descendant_section_ids(descendant_excluded_section_ids, closure_rows)
    excluded_section_ids = directly_excluded_section_ids | descendant_ids

    # Filter sections
    filtered_sections = [s for s in sections if s.section_id not in excluded_section_ids]

    # Filter closure rows (only keep rows where both ends are non-excluded)
    filtered_closure_rows = [row for row in closure_rows if row.ancestor_section_id not in excluded_section_ids and row.descendant_section_id not in excluded_section_ids]

    # Filter chunks - count and track those that directly match a chunk filter (by text)
    text_matched_chunk_ids: list[str] = []
    filtered_chunks = []
    for chunk in chunks:
        if any(pattern in chunk.text for pattern in EXCLUDED_CHUNK_TEXTS):
            text_matched_chunk_ids.append(chunk.chunk_id)
            continue
        if chunk.containing_section_id in excluded_section_ids:
            continue
        filtered_chunks.append(chunk)

    excluded_chunk_count = len(text_matched_chunk_ids)
    excluded_chunk_ids = tuple(text_matched_chunk_ids)

    return FilteredExtractionResult(
        chunks=filtered_chunks,
        sections=filtered_sections,
        closure_rows=filtered_closure_rows,
        excluded_section_count=excluded_section_count,
        excluded_chunk_count=excluded_chunk_count,
        excluded_section_titles=excluded_section_titles,
        excluded_chunk_ids=excluded_chunk_ids,
    )


def _find_excluded_section_ids(sections: list[SectionRecord]) -> set[str]:
    """Find section IDs that match exclusion criteria."""
    excluded_ids: set[str] = set()

    for section in sections:
        if _is_directly_excluded_section_title(section.title):
            excluded_ids.add(section.section_id)

    return excluded_ids


def _find_contextual_excluded_section_ids(
    sections: list[SectionRecord],
    closure_rows: list[SectionClosureRow],
) -> set[str]:
    """Find amendment section IDs that only belong in the TOC when outside appendices."""
    section_by_id = {section.section_id: section for section in sections}
    ancestor_ids_by_descendant: dict[str, set[str]] = {}
    for row in closure_rows:
        ancestor_ids_by_descendant.setdefault(row.descendant_section_id, set()).add(row.ancestor_section_id)

    contextual_excluded_ids: set[str] = set()
    for section in sections:
        if not _is_appendix_amendment_title(section.title):
            continue
        ancestor_ids = ancestor_ids_by_descendant.get(section.section_id, set())
        for ancestor_id in ancestor_ids:
            if ancestor_id == section.section_id:
                continue
            ancestor = section_by_id.get(ancestor_id)
            if ancestor is not None and _is_appendix_title(ancestor.title):
                contextual_excluded_ids.add(section.section_id)
                break

    return contextual_excluded_ids


def is_section_title_excluded(title: str) -> bool:
    """Check whether a section title should be excluded from storage and TOC generation."""
    if title in EXCLUDED_SECTION_TITLES:
        return True
    return any(title.startswith(prefix) for prefix in EXCLUDED_SECTION_TITLE_PREFIXES)


def _is_directly_excluded_section_title(title: str) -> bool:
    """Check whether a section title is excluded without applying amendment appendix context."""
    if title in EXCLUDED_SECTION_TITLES:
        return True
    return title.startswith("Withdrawal of")


def _is_appendix_title(title: str) -> bool:
    """Check whether a title refers to an appendix container."""
    return title.startswith("Appendix") or title == "Appendices"


def _should_cascade_section_exclusion(_section: SectionRecord | None) -> bool:
    """Check whether a directly excluded section should also exclude its descendants."""
    return True


def _is_appendix_amendment_title(title: str) -> bool:
    """Check whether a title is an amendment heading that should be excluded in appendices."""
    return title.startswith(("Amendments to", "Amendment to"))


def _find_descendant_section_ids(
    excluded_ids: set[str],
    closure_rows: list[SectionClosureRow],
) -> set[str]:
    """Find all descendant section IDs of excluded sections."""
    descendant_ids: set[str] = set()
    to_process = set(excluded_ids)

    # Build a map from ancestor to descendants
    ancestor_to_descendants: dict[str, set[str]] = {}
    for row in closure_rows:
        if row.ancestor_section_id not in ancestor_to_descendants:
            ancestor_to_descendants[row.ancestor_section_id] = set()
        ancestor_to_descendants[row.ancestor_section_id].add(row.descendant_section_id)

    # BFS to find all descendants
    while to_process:
        current = to_process.pop()
        descendants = ancestor_to_descendants.get(current, set())
        for descendant in descendants:
            if descendant not in descendant_ids:
                descendant_ids.add(descendant)
                to_process.add(descendant)

    return descendant_ids
