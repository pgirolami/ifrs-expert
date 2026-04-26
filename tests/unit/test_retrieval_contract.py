"""Tests for declarative retrieval contract parsing helpers."""

from __future__ import annotations

from src.retrieval.retrieval_contract import expand_chunk_number_range


def test_expand_chunk_number_range_handles_alphabetic_leaf_suffix() -> None:
    """Chunk-number ranges should support labels like B4.1.9A through B4.1.9E."""
    assert expand_chunk_number_range(start="B4.1.9A", end="B4.1.9E") == [
        "B4.1.9A",
        "B4.1.9B",
        "B4.1.9C",
        "B4.1.9D",
        "B4.1.9E",
    ]


def test_expand_chunk_number_range_handles_alphanumeric_prefix() -> None:
    """Chunk-number ranges should support labels like B6.3.1 through B6.3.6."""
    assert expand_chunk_number_range(start="B6.3.1", end="B6.3.6") == [
        "B6.3.1",
        "B6.3.2",
        "B6.3.3",
        "B6.3.4",
        "B6.3.5",
        "B6.3.6",
    ]


def test_expand_chunk_number_range_still_rejects_mismatched_prefixes() -> None:
    """Range expansion should stay strict about shared prefixes."""
    try:
        expand_chunk_number_range(start="B6.3.1", end="B7.3.6")
    except ValueError as error:
        assert "ranges must share a prefix" in str(error)
    else:  # pragma: no cover - defensive
        raise AssertionError("Expected ValueError")
