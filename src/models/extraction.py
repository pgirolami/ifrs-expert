"""Extraction result models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.chunk import Chunk
    from src.models.document import DocumentRecord
    from src.models.section import SectionClosureRow, SectionRecord


@dataclass
class ExtractedDocument:
    """Structured extraction result returned by a source extractor."""

    document: DocumentRecord
    chunks: list[Chunk]
    sections: list[SectionRecord] = field(default_factory=list)
    section_closure_rows: list[SectionClosureRow] = field(default_factory=list)
