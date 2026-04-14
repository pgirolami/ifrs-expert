"""Document metadata model for IFRS Expert."""

from __future__ import annotations

import importlib
import sqlite3
from dataclasses import dataclass

DOCUMENT_TYPES: tuple[str, ...] = (
    "IFRS",
    "IFRS-S",
    "IFRS-BC",
    "IFRS-IE",
    "IFRS-IG",
    "IAS",
    "IFRIC",
    "SIC",
    "PS",
    "NAVIS",
)
DOCUMENT_TYPE_FAMILIES: tuple[str, ...] = ("IFRS", "IAS", "IFRIC", "SIC", "PS", "NAVIS")


def resolve_document_type_from_doc_uid(doc_uid: str) -> str | None:
    """Resolve a document type from doc_uid as a fallback for non-HTML sources."""
    normalized_doc_uid = doc_uid.strip().lower()
    if not normalized_doc_uid:
        return None

    if normalized_doc_uid.startswith("ifrs"):
        for suffix, document_type in (
            ("-bc", "IFRS-BC"),
            ("-ie", "IFRS-IE"),
            ("-ig", "IFRS-IG"),
        ):
            if normalized_doc_uid.startswith("ifrs") and suffix in normalized_doc_uid:
                return document_type
        return "IFRS"

    for document_type in DOCUMENT_TYPE_FAMILIES:
        if normalized_doc_uid.startswith(document_type.lower()):
            return document_type
    return None


def resolve_document_type(doc_uid: str, explicit_document_type: str | None = None) -> str | None:
    """Resolve a document type from explicit metadata first, then doc_uid fallback."""
    if explicit_document_type is not None and explicit_document_type in DOCUMENT_TYPES:
        return explicit_document_type
    return resolve_document_type_from_doc_uid(doc_uid)


def document_type_to_family(document_type: str | None) -> str | None:
    """Map exact document types to the retrieval family used by the pipeline."""
    if document_type is None:
        return None
    if document_type.startswith("IFRS"):
        return "IFRS"
    if document_type in DOCUMENT_TYPE_FAMILIES:
        return document_type
    return None


def infer_document_type(doc_uid: str) -> str | None:
    """Infer the exact document type from persisted metadata, with a doc_uid fallback."""
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

    return resolve_document_type_from_doc_uid(normalized_doc_uid)


def infer_document_family(doc_uid: str) -> str | None:
    """Infer the retrieval family from persisted metadata or doc_uid fallback."""
    return document_type_to_family(infer_document_type(doc_uid))


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
