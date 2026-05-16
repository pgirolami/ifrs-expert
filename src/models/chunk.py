"""Chunk data model for IFRS Expert."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Chunk:
    """Represents a structure-aware document chunk."""

    id: int | None = None
    doc_uid: str = ""
    chunk_number: str = ""
    page_start: str = ""
    page_end: str = ""
    chunk_id: str = ""
    text: str = ""
    containing_section_id: str | None = None
    containing_section_db_id: int | None = None
