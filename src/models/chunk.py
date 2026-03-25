"""Chunk data model for IFRS Expert."""

from dataclasses import dataclass


@dataclass
class Chunk:
    """Represents a document chunk extracted from a PDF."""

    chunk_id: int = 0
    doc_uid: str = ""
    section_path: str = ""
    page_start: str = ""
    page_end: str = ""
    text: str = ""
