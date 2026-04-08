"""Document metadata model for IFRS Expert."""

from __future__ import annotations

from dataclasses import dataclass

DOCUMENT_TYPES: tuple[str, ...] = ("IFRS", "IAS", "IFRIC", "SIC", "PS")


def infer_document_type(doc_uid: str) -> str | None:
    """Infer the document type from the stored document UID."""
    normalized_doc_uid = doc_uid.strip().lower()
    for document_type in DOCUMENT_TYPES:
        if normalized_doc_uid.startswith(document_type.lower()):
            return document_type
    return None


@dataclass
class DocumentRecord:
    """Represents one source document stored in the local index."""

    doc_uid: str
    source_type: str
    source_title: str
    source_url: str | None
    canonical_url: str | None
    captured_at: str | None
    document_type: str | None = None
    background_text: str | None = None
    issue_text: str | None = None
    objective_text: str | None = None
    scope_text: str | None = None
    intro_text: str | None = None
    toc_text: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
