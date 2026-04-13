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

    @property
    def section_path(self) -> str:
        """Backward-compatible alias for chunk_number during migration."""
        return self.chunk_number

    @section_path.setter
    def section_path(self, value: str) -> None:
        self.chunk_number = value

    @property
    def source_anchor(self) -> str:
        """Backward-compatible alias for chunk_id during migration."""
        return self.chunk_id

    @source_anchor.setter
    def source_anchor(self, value: str) -> None:
        self.chunk_id = value
