"""Reference data model for IFRS annotation ingestion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass
class ContentReference:
    """One parsed IFRS `Refer:` annotation target."""

    id: int | None = None
    source_doc_uid: str = ""
    source_location_type: Literal["chunk", "section"] = "chunk"
    reference_order: int = 0
    annotation_raw_text: str = ""
    target_raw_text: str = ""
    target_kind: str = "unknown"
    target_doc_hint: str | None = None
    target_start: str | None = None
    target_end: str | None = None
    parsed_ok: bool = False
    source_chunk_id: str | None = None
    source_chunk_db_id: int | None = None
    source_section_id: str | None = None
    source_section_db_id: int | None = None
