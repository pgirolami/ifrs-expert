"""Chunk data model for IFRS Expert."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Chunk:
    """Represents a structure-aware document chunk."""

    chunk_id: int | None = None
    doc_uid: str = ""
    section_path: str = ""
    page_start: str = ""
    page_end: str = ""
    source_anchor: str = ""
    text: str = ""
