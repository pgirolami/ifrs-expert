"""Provenance labels used across retrieval and answer artifacts."""

from __future__ import annotations

from enum import StrEnum


class Provenance(StrEnum):
    """Canonical provenance labels for retrieved chunks."""

    TOP_SIMILARITY = "top_similarity"
    TOP_SIMILARITY_FOR_SECTION_REFERENCE = "top_similarity_in_referenced_section"

    EXPAND_TO_ENCLOSING_SECTION = "enclosing_section_expansion"

    EXPAND_TO_REFERENCED_CHUNK = "referenced_chunk"
    EXPAND_TO_ENCLOSING_SECTION_OF_REFERENCED_CHUNK = "enclosing_section_expansion_for_referenced_chunk"

    FULL_DOCUMENT = "full_doc"
