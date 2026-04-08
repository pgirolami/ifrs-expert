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
    background_text: str | None = None
    issue_text: str | None = None
    objective_text: str | None = None
    scope_text: str | None = None
    intro_text: str | None = None
    toc_text: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
