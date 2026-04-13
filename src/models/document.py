"""Document metadata model for IFRS Expert."""

from __future__ import annotations

import importlib
import sqlite3
from dataclasses import dataclass

DOCUMENT_TYPES: tuple[str, ...] = ("IFRS", "IAS", "IFRIC", "SIC", "PS", "NAVIS")


def derive_document_type_from_doc_uid(doc_uid: str) -> str | None:
    """Derive the document type from a doc_uid prefix as a legacy fallback."""
    normalized_doc_uid = doc_uid.strip().lower()
    for document_type in DOCUMENT_TYPES:
        if normalized_doc_uid.startswith(document_type.lower()):
            return document_type
    return None


def infer_document_type(doc_uid: str) -> str | None:
    """Infer the document type from persisted metadata, with a prefix fallback."""
    normalized_doc_uid = doc_uid.strip()
    if not normalized_doc_uid:
        return None

    try:
        connection_module = importlib.import_module("src.db.connection")
        with connection_module.get_connection(read_only=True) as connection:
            connection.row_factory = sqlite3.Row
            row = connection.execute(
                "SELECT document_type FROM documents WHERE doc_uid = ?",
                (normalized_doc_uid,),
            ).fetchone()
    except sqlite3.OperationalError:
        row = None

    if row is not None:
        document_type = row["document_type"]
        if isinstance(document_type, str) and document_type.strip():
            return document_type

    return derive_document_type_from_doc_uid(normalized_doc_uid)


@dataclass
class DocumentRecord:
    """Represents one source document stored in the local index."""

    doc_uid: str
    source_type: str
    source_title: str
    source_url: str | None
    canonical_url: str | None
    captured_at: str | None
    source_domain: str | None = None
    document_type: str | None = None
    background_text: str | None = None
    issue_text: str | None = None
    objective_text: str | None = None
    scope_text: str | None = None
    intro_text: str | None = None
    toc_text: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
