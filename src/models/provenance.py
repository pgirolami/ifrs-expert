"""Provenance labels used across retrieval and answer artifacts."""

from __future__ import annotations

from enum import StrEnum


class Provenance(StrEnum):
    """Canonical provenance labels for retrieved chunks."""

    SIMILARITY = "similarity"
    SAME_FAMILY_REFERENCE = "ref_sf"
    SECTION_FAN_OUT_FROM_SEED = "exp_section_from_seed"
    SECTION_FAN_OUT_FROM_REFERENCE = "exp_sect_from_reference"
    FULL_DOCUMENT = "full_doc"


def coerce_provenance(value: object | None) -> Provenance:
    """Normalize a raw provenance value to the canonical enum."""
    if isinstance(value, Provenance):
        return value
    if isinstance(value, str):
        for provenance in Provenance:
            if provenance.value == value:
                return provenance
    return Provenance.SIMILARITY
