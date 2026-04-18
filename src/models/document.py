"""Document metadata model for IFRS Expert."""

from __future__ import annotations

import importlib
import sqlite3
from dataclasses import dataclass
from pathlib import Path

DOCUMENT_TYPES: tuple[str, ...] = (
    # IFRS Standards and variants
    "IFRS-S",
    "IFRS-BC",
    "IFRS-IE",
    "IFRS-IG",
    # IAS Standards and variants
    "IAS-S",
    "IAS-BC",
    "IAS-IE",
    "IAS-IG",
    # IFRIC Interpretations and variants
    "IFRIC",
    "IFRIC-BC",
    "IFRIC-IE",
    "IFRIC-IG",
    # SIC Interpretations and variants
    "SIC",
    "SIC-BC",
    "SIC-IE",
    # Practice Statements and variants
    "PS",
    "PS-BC",
    # Other
    "NAVIS",
)
DOCUMENT_TYPE_FAMILIES: tuple[str, ...] = ("IFRS", "IAS", "IFRIC", "SIC", "PS", "NAVIS")
DOCUMENT_KIND_BY_TYPE: dict[str, str] = {
    # IFRS Standards and variants
    "IFRS-S": "standard",
    "IFRS-IG": "implementation_guidance",
    "IFRS-IE": "illustrative_examples",
    "IFRS-BC": "basis_for_conclusions",
    # IAS Standards and variants
    "IAS-S": "standard",
    "IAS-IG": "implementation_guidance",
    "IAS-IE": "illustrative_examples",
    "IAS-BC": "basis_for_conclusions",
    # IFRIC Interpretations and variants
    "IFRIC": "interpretation",
    "IFRIC-IE": "illustrative_examples",
    "IFRIC-IG": "implementation_guidance",
    "IFRIC-BC": "basis_for_conclusions",
    # SIC Interpretations and variants
    "SIC": "interpretation",
    "SIC-IE": "illustrative_examples",
    "SIC-BC": "basis_for_conclusions",
    # Practice Statements and variants
    "PS": "standard",
    "PS-BC": "basis_for_conclusions",
    # Other
    "NAVIS": "interpretation",
}
DOCUMENT_KINDS: tuple[str, ...] = (
    "standard",
    "interpretation",
    "implementation_guidance",
    "illustrative_examples",
    "basis_for_conclusions",
)
DEFAULT_DB_PATH: Path = Path(__file__).parent.parent.parent / "corpus" / "data" / "db" / "ifrs.db"


# Family configuration for doc_uid resolution
# Each entry: (prefix, [(suffix, variant_type), ...], base_type)
_FAMILY_VARIANT_CONFIG: tuple[tuple[str, tuple[tuple[str, str], ...], str], ...] = (
    ("ifrs", (("-bc", "IFRS-BC"), ("-ie", "IFRS-IE"), ("-ig", "IFRS-IG")), "IFRS-S"),
    ("ias", (("-bc", "IAS-BC"), ("-ie", "IAS-IE"), ("-ig", "IAS-IG")), "IAS-S"),
    ("ifric", (("-bc", "IFRIC-BC"), ("-ie", "IFRIC-IE"), ("-ig", "IFRIC-IG")), "IFRIC"),
    ("sic", (("-bc", "SIC-BC"), ("-ie", "SIC-IE")), "SIC"),
    ("ps", (("-bc", "PS-BC"),), "PS"),
)


def _resolve_type_from_family(normalized_doc_uid: str, prefix: str, variants: tuple[tuple[str, str], ...], base_type: str) -> str:
    """Check if doc_uid matches a family prefix and resolve variant or base type."""
    if not normalized_doc_uid.startswith(prefix):
        return ""
    for suffix, variant_type in variants:
        if suffix in normalized_doc_uid:
            return variant_type
    return base_type


def resolve_document_type_from_doc_uid(doc_uid: str) -> str | None:
    """Resolve a document type from doc_uid as a fallback for non-HTML sources.

    Handles all standard families and their variant suffixes:
    - IFRS: -bc (Basis for Conclusions), -ie (Illustrative Examples), -ig (Implementation Guidance)
    - IAS: -bc, -ie, -ig (same variants as IFRS)
    - IFRIC: -bc, -ie
    - SIC: -bc, -ie
    - PS: -bc
    """
    normalized_doc_uid = doc_uid.strip().lower()
    if not normalized_doc_uid:
        return None

    # Check each configured family
    for prefix, variants, base_type in _FAMILY_VARIANT_CONFIG:
        result = _resolve_type_from_family(normalized_doc_uid, prefix, variants, base_type)
        if result:
            return result

    # Fallback for other families (NAVIS, etc.)
    for document_type in DOCUMENT_TYPE_FAMILIES:
        if normalized_doc_uid.startswith(document_type.lower()):
            return document_type
    return None


def resolve_document_type(doc_uid: str, explicit_document_type: str | None = None) -> str | None:
    """Resolve a document type from explicit metadata first, then doc_uid fallback."""
    if explicit_document_type is not None:
        normalized_document_type = explicit_document_type.strip().upper()
        if normalized_document_type and normalized_document_type in DOCUMENT_TYPES:
            return normalized_document_type
    return resolve_document_type_from_doc_uid(doc_uid)


def resolve_document_kind_from_document_type(document_type: str | None) -> str | None:
    """Resolve a document kind from an exact document type."""
    if document_type is None:
        return None
    return DOCUMENT_KIND_BY_TYPE.get(document_type)


def resolve_document_kind(document_type: str | None, explicit_document_kind: str | None = None) -> str | None:
    """Resolve a document kind from explicit metadata first, then document type mapping."""
    if explicit_document_kind is not None and explicit_document_kind in DOCUMENT_KINDS:
        return explicit_document_kind
    return resolve_document_kind_from_document_type(document_type)


def document_type_to_family(document_type: str | None) -> str | None:
    """Map exact document types to retrieval families."""
    if document_type is None:
        return None
    if document_type.startswith("IFRS"):
        return "IFRS"
    if document_type in DOCUMENT_TYPE_FAMILIES:
        return document_type
    return None


def _get_persisted_document_type(doc_uid: str, *, use_default_db_guard: bool) -> str | None:
    normalized_doc_uid = doc_uid.strip()
    if not normalized_doc_uid:
        return None

    connection_module = importlib.import_module("src.db.connection")
    if use_default_db_guard and connection_module.DB_PATH == DEFAULT_DB_PATH:
        return None

    try:
        with connection_module.get_connection(read_only=True) as connection:
            connection.row_factory = sqlite3.Row
            row = connection.execute(
                "SELECT document_type FROM documents WHERE doc_uid = ?",
                (normalized_doc_uid,),
            ).fetchone()
    except sqlite3.OperationalError:
        row = None

    if row is None:
        return None

    document_type = row["document_type"]
    if isinstance(document_type, str) and document_type.strip():
        return document_type.strip()
    return None


def infer_document_type(doc_uid: str) -> str | None:
    """Infer exact document type from persisted metadata, then doc_uid fallback."""
    persisted_document_type = _get_persisted_document_type(doc_uid, use_default_db_guard=True)
    if persisted_document_type is not None:
        return persisted_document_type
    return resolve_document_type_from_doc_uid(doc_uid)


def infer_persisted_document_type(doc_uid: str) -> str | None:
    """Infer exact document type from persisted metadata when available."""
    persisted_document_type = _get_persisted_document_type(doc_uid, use_default_db_guard=False)
    if persisted_document_type is not None:
        return persisted_document_type
    return resolve_document_type_from_doc_uid(doc_uid)


def infer_exact_document_type(doc_uid: str) -> str | None:
    """Infer exact document type and ensure it is supported."""
    document_type = infer_persisted_document_type(doc_uid)
    if document_type in DOCUMENT_TYPES:
        return document_type
    return None


def infer_document_kind(doc_uid: str) -> str | None:
    """Infer document kind from persisted or fallback document type."""
    return resolve_document_kind_from_document_type(infer_exact_document_type(doc_uid))


def infer_document_family(doc_uid: str) -> str | None:
    """Infer the retrieval family from persisted metadata or doc_uid fallback."""
    return document_type_to_family(infer_persisted_document_type(doc_uid))


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
    document_kind: str | None = None
    background_text: str | None = None
    issue_text: str | None = None
    objective_text: str | None = None
    scope_text: str | None = None
    intro_text: str | None = None
    toc_text: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
