"""Document metadata model for IFRS Expert."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DocumentRecord:
    """Represents one source document stored in the local index."""

    doc_uid: str
    source_type: str
    source_title: str
    source_url: str | None
    canonical_url: str | None
    captured_at: str | None
    created_at: str | None = None
    updated_at: str | None = None
