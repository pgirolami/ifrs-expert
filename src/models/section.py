"""Section models for title retrieval."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class SectionRecord:
    """One indexed section heading extracted from an HTML standards document."""

    section_id: str
    doc_uid: str
    parent_section_id: str | None
    level: int
    title: str
    section_lineage: list[str] = field(default_factory=list)
    position: int = 0
    db_id: int | None = None
    parent_section_db_id: int | None = None


@dataclass(frozen=True)
class SectionClosureRow:
    """One ancestor/descendant relationship between indexed sections."""

    ancestor_section_id: str
    descendant_section_id: str
    depth: int
    ancestor_section_db_id: int | None = None
    descendant_section_db_id: int | None = None
