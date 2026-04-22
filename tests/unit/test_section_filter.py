"""Tests for the section filter module."""

from __future__ import annotations

from src.commands.section_filter import (
    EXCLUDED_CHUNK_TEXTS,
    EXCLUDED_SECTION_TITLES,
    EXCLUDED_SECTION_TITLE_PREFIXES,
    filter_extraction,
)
from src.retrieval.document_profile_builder import _build_toc_text
from src.models.chunk import Chunk
from src.models.section import SectionClosureRow, SectionRecord


def test_excluded_section_titles_constant_contains_expected_values() -> None:
    """The excluded section titles constant contains all expected values."""
    expected_titles = {
        "References",
        "Contents",
        "Effective Date and transition",
        "Effective date",
        "Date of consensus",
        "Transition",
        "Table of Concordance",
        "Board Approvals",
        "Dissenting opinion",
        "Dissenting opinions",
    }
    assert EXCLUDED_SECTION_TITLES == expected_titles


def test_excluded_section_prefixes_constant_contains_expected_values() -> None:
    """The excluded section title prefixes contain the expected values."""
    expected_prefixes = {"Withdrawal of", "Amendments to", "Amendment to"}
    assert EXCLUDED_SECTION_TITLE_PREFIXES == expected_prefixes


def test_excluded_chunk_texts_constant_has_expected_values() -> None:
    """The excluded chunk texts constant contains all expected patterns."""
    expected_texts = {
        "[Deleted]",
        "These paragraphs refer to amendments that are not yet effective",
        "This paragraph refers to amendments that are not yet effective",
    }
    assert EXCLUDED_CHUNK_TEXTS == expected_texts


def test_filter_excludes_sections_with_exact_title_match() -> None:
    """Sections with exact title matches should be excluded."""
    sections = [
        _make_section("sec1", "References"),
        _make_section("sec2", "Main Content"),
        _make_section("sec3", "Effective date"),
    ]
    chunks = [_make_chunk("chunk1", "sec1"), _make_chunk("chunk2", "sec2")]
    closure_rows = []

    result = filter_extraction(chunks, sections, closure_rows)

    assert len(result.sections) == 1
    assert result.sections[0].section_id == "sec2"
    assert result.excluded_section_count == 2
    assert len(result.chunks) == 1
    assert result.chunks[0].chunk_id == "chunk2"


def test_filter_excludes_sections_with_prefix_match() -> None:
    """Sections with title prefixes should be excluded."""
    sections = [
        _make_section("sec1", "Withdrawal of IAS 37"),
        _make_section("sec2", "Amendments to IFRS 3"),
        _make_section("sec3", "Main Content"),
        _make_section("sec4", "Withdrawal"),
    ]
    chunks = [_make_chunk("chunk1", "sec1"), _make_chunk("chunk2", "sec2"), _make_chunk("chunk3", "sec3")]
    closure_rows = []

    result = filter_extraction(chunks, sections, closure_rows)

    assert len(result.sections) == 3
    assert {s.section_id for s in result.sections} == {"sec2", "sec3", "sec4"}
    assert result.excluded_section_count == 1
    assert len(result.chunks) == 2
    assert {c.chunk_id for c in result.chunks} == {"chunk2", "chunk3"}


def test_filter_excludes_amendment_titles_only_within_appendix() -> None:
    """Amendment titles should be excluded when they appear inside Appendix sections."""
    sections = [
        _make_section("sec-appendix", "Appendix A"),
        _make_section("sec-amendment-in-appendix", "Amendments to IFRS 3"),
        _make_section("sec-amendment-child", "Background of appendix amendment"),
        _make_section("sec-amendment-outside", "Amendments to IAS 1"),
        _make_section("sec-main", "Main Content"),
    ]
    chunks = [
        _make_chunk("chunk-appendix", "sec-appendix"),
        _make_chunk("chunk-appendix-amendment", "sec-amendment-in-appendix"),
        _make_chunk("chunk-appendix-child", "sec-amendment-child"),
        _make_chunk("chunk-outside-amendment", "sec-amendment-outside"),
        _make_chunk("chunk-main", "sec-main"),
    ]
    closure_rows = [
        _make_closure("sec-appendix", "sec-amendment-in-appendix", 1),
        _make_closure("sec-amendment-in-appendix", "sec-amendment-child", 2),
    ]

    result = filter_extraction(chunks, sections, closure_rows)

    assert {section.section_id for section in result.sections} == {"sec-appendix", "sec-amendment-outside", "sec-main"}
    assert {chunk.chunk_id for chunk in result.chunks} == {"chunk-appendix", "chunk-outside-amendment", "chunk-main"}
    assert result.excluded_section_count == 1
    assert result.excluded_section_titles == ("Amendments to IFRS 3",)


def test_filter_excludes_descendant_sections() -> None:
    """Child sections of excluded sections should also be excluded."""
    sections = [
        _make_section("sec1", "References"),
        _make_section("sec2", "Reference Item 1"),
        _make_section("sec3", "Reference Item 2"),
        _make_section("sec4", "Main Content"),
    ]
    chunks = [
        _make_chunk("chunk1", "sec1"),
        _make_chunk("chunk2", "sec2"),
        _make_chunk("chunk3", "sec3"),
        _make_chunk("chunk4", "sec4"),
    ]
    # Closure rows: sec1 has children sec2, sec3; sec2 has child sec4
    closure_rows = [
        _make_closure("sec1", "sec2", 1),  # sec1 excluded -> sec2 excluded
        _make_closure("sec1", "sec3", 1),  # sec1 excluded -> sec3 excluded
        _make_closure("sec2", "sec4", 2),  # sec2 excluded (via sec1) -> sec4 excluded
    ]

    # sec1 "References" is excluded, so all its descendants (sec2, sec3, sec4) should also be excluded
    result = filter_extraction(chunks, sections, closure_rows)

    # All sections and chunks are excluded because sec1 triggers cascade
    assert len(result.sections) == 0
    assert len(result.chunks) == 0
    # But only 1 section directly matched a filter (sec1 "References")
    assert result.excluded_section_count == 1
    assert result.excluded_section_titles == ("References",)


def test_filter_excludes_chunks_with_deleted_text() -> None:
    """Chunks containing [Deleted] should be excluded."""
    sections = [_make_section("sec1", "Main Content")]
    chunks = [
        _make_chunk("chunk1", "sec1", text="Some content"),
        _make_chunk("chunk2", "sec1", text="[Deleted]"),
        _make_chunk("chunk3", "sec1", text="[Deleted] with surrounding text"),  # Contains [Deleted]
        _make_chunk("chunk4", "sec1", text="More content"),
    ]
    closure_rows = []

    result = filter_extraction(chunks, sections, closure_rows)

    assert len(result.chunks) == 2
    assert {c.chunk_id for c in result.chunks} == {"chunk1", "chunk4"}
    assert result.excluded_chunk_count == 2


def test_filter_excludes_chunks_with_pending_amendment_text() -> None:
    """Chunks containing pending amendment notice text should be excluded."""
    sections = [_make_section("sec1", "Main Content")]
    chunks = [
        _make_chunk("chunk1", "sec1", text="Some content"),
        _make_chunk(
            "chunk2",
            "sec1",
            text="[These paragraphs refer to amendments that are not yet effective, and are therefore not included in this edition.]",
        ),
        _make_chunk(
            "chunk3",
            "sec1",
            text="[This paragraph refers to amendments that are not yet effective, and is therefore not included in this edition.]",
        ),
        _make_chunk("chunk4", "sec1", text="More content"),
    ]
    closure_rows: list[SectionClosureRow] = []

    result = filter_extraction(chunks, sections, closure_rows)

    assert len(result.chunks) == 2
    assert {c.chunk_id for c in result.chunks} == {"chunk1", "chunk4"}
    assert result.excluded_chunk_count == 2


def test_filter_excludes_descendants_of_withdrawal_wrappers() -> None:
    """Withdrawal wrapper sections should remove their descendants too."""
    sections = [
        _make_section("sec-withdrawal", "Withdrawal of IAS 36 (issued 1998)"),
        _make_section("sec-appendix-a", "Appendix A"),
        _make_section("sec-main", "Main Content"),
    ]
    chunks = [
        _make_chunk("chunk-withdrawal", "sec-withdrawal"),
        _make_chunk("chunk-appendix-a", "sec-appendix-a"),
        _make_chunk("chunk-main", "sec-main"),
    ]
    closure_rows = [
        _make_closure("sec-withdrawal", "sec-appendix-a", 1),
    ]

    result = filter_extraction(chunks, sections, closure_rows)

    assert {section.section_id for section in result.sections} == {"sec-main"}
    assert {chunk.chunk_id for chunk in result.chunks} == {"chunk-main"}
    assert result.excluded_section_count == 1
    assert result.excluded_section_titles == ("Withdrawal of IAS 36 (issued 1998)",)


def test_filter_excludes_board_approvals_sections() -> None:
    """Board Approvals should be excluded from stored sections and chunks."""
    sections = [
        _make_section("sec-board", "Board Approvals"),
        _make_section("sec-main", "Main Content"),
    ]
    chunks = [_make_chunk("chunk-board", "sec-board"), _make_chunk("chunk-main", "sec-main")]

    result = filter_extraction(chunks, sections, [])

    assert {section.section_id for section in result.sections} == {"sec-main"}
    assert {chunk.chunk_id for chunk in result.chunks} == {"chunk-main"}
    assert result.excluded_section_count == 1
    assert result.excluded_section_titles == ("Board Approvals",)


def test_toc_exclusions_match_storage_exclusions_for_representative_sections() -> None:
    """The TOC and storage filters should exclude the same representative section titles."""
    sections = [
        _make_section("sec-main", "Main Content"),
        _make_section("sec-board", "Board Approvals"),
        _make_section("sec-ref", "References"),
        SectionRecord(
            section_id="sec-appendix",
            doc_uid="test-doc",
            parent_section_id=None,
            level=1,
            title="Appendix A",
            section_lineage=["Appendix A"],
            position=3,
        ),
        SectionRecord(
            section_id="sec-amendment-in-appendix",
            doc_uid="test-doc",
            parent_section_id="sec-appendix",
            level=2,
            title="Amendments to IFRS 3",
            section_lineage=["Appendix A", "Amendments to IFRS 3"],
            position=4,
        ),
        SectionRecord(
            section_id="sec-amendment-child",
            doc_uid="test-doc",
            parent_section_id="sec-amendment-in-appendix",
            level=3,
            title="Background of appendix amendment",
            section_lineage=["Appendix A", "Amendments to IFRS 3", "Background of appendix amendment"],
            position=5,
        ),
        _make_section("sec-amendment-outside", "Amendments to IAS 1"),
    ]
    closure_rows = [
        _make_closure("sec-appendix", "sec-amendment-in-appendix", 1),
        _make_closure("sec-amendment-in-appendix", "sec-amendment-child", 2),
    ]

    filtered = filter_extraction(chunks=[], sections=sections, closure_rows=closure_rows)
    toc_text = _build_toc_text("ias-test", sections, closure_rows)

    assert toc_text is not None
    assert {section.title for section in filtered.sections} == set(toc_text.splitlines())
    assert {section.title for section in sections} - {section.title for section in filtered.sections} == {
        "Board Approvals",
        "References",
        "Amendments to IFRS 3",
        "Background of appendix amendment",
    }


def test_toc_exclusions_match_storage_exclusions_for_withdrawal_wrappers() -> None:
    """Withdrawal wrappers should be excluded from both storage and TOC without dropping their descendants."""
    sections = [
        _make_section("sec-main", "Main Content"),
        _make_section("sec-withdrawal", "Withdrawal of IAS 36 (issued 1998)"),
        SectionRecord(
            section_id="sec-appendix",
            doc_uid="test-doc",
            parent_section_id="sec-withdrawal",
            level=2,
            title="Appendix A",
            section_lineage=["Withdrawal of IAS 36 (issued 1998)", "Appendix A"],
            position=2,
        ),
    ]
    closure_rows = [
        _make_closure("sec-withdrawal", "sec-appendix", 1),
    ]

    filtered = filter_extraction(chunks=[], sections=sections, closure_rows=closure_rows)
    toc_text = _build_toc_text("ias-test", sections, closure_rows)

    assert toc_text is not None
    assert {section.title for section in filtered.sections} == set(toc_text.splitlines())
    assert {section.title for section in filtered.sections} == {"Main Content"}
    assert {section.title for section in sections} - {section.title for section in filtered.sections} == {
        "Withdrawal of IAS 36 (issued 1998)",
        "Appendix A",
    }


def test_filter_excludes_chunks_from_excluded_sections() -> None:
    """Chunks belonging to excluded sections should be excluded."""
    sections = [
        _make_section("sec1", "Main Content"),
        _make_section("sec2", "References"),
    ]
    chunks = [
        _make_chunk("chunk1", "sec1", text="Main content text"),
        _make_chunk("chunk2", "sec2", text="Reference content"),
        _make_chunk("chunk3", "sec1", text="More main content"),
    ]
    closure_rows = []

    result = filter_extraction(chunks, sections, closure_rows)

    assert len(result.sections) == 1
    assert len(result.chunks) == 2
    assert {c.chunk_id for c in result.chunks} == {"chunk1", "chunk3"}


def test_filter_filters_closure_rows_correctly() -> None:
    """Closure rows with excluded sections should be filtered out."""
    sections = [
        _make_section("sec1", "Main Content"),
        _make_section("sec2", "Effective date"),
        _make_section("sec3", "Sub-section"),
    ]
    chunks = [_make_chunk("chunk1", "sec1"), _make_chunk("chunk2", "sec2"), _make_chunk("chunk3", "sec3")]
    # sec2 "Effective date" is excluded
    # sec3 is child of both sec1 and sec2
    closure_rows = [
        _make_closure("sec1", "sec3", 1),  # Keep: both sec1 and sec3 are non-excluded (sec3 gets excluded via sec2)
        _make_closure("sec2", "sec3", 1),  # Filter: sec2 is excluded
    ]

    result = filter_extraction(chunks, sections, closure_rows)

    # sec2 "Effective date" is excluded, and sec3 is a descendant of sec2
    # so sec3 is also excluded via closure row
    assert len(result.sections) == 1
    assert {s.section_id for s in result.sections} == {"sec1"}
    # No closure rows remain because sec3 is excluded
    assert len(result.closure_rows) == 0
    assert len(result.chunks) == 1  # Only chunk1 remains (sec2's chunk excluded, sec3's chunk excluded)


def test_filter_with_nested_excluded_sections() -> None:
    """Nested excluded sections should be completely filtered."""
    sections = [
        _make_section("sec1", "Contents"),
        _make_section("sec2", "Chapter 1"),
        _make_section("sec3", "Chapter 2"),
        _make_section("sec4", "Section 2.1"),
    ]
    chunks = [
        _make_chunk("chunk1", "sec1"),
        _make_chunk("chunk2", "sec2"),
        _make_chunk("chunk3", "sec3"),
        _make_chunk("chunk4", "sec4"),
    ]
    # "Contents" is excluded (exact match)
    # sec1 -> sec2, sec3
    # sec3 -> sec4
    closure_rows = [
        _make_closure("sec1", "sec2", 1),
        _make_closure("sec1", "sec3", 1),
        _make_closure("sec3", "sec4", 1),
    ]

    result = filter_extraction(chunks, sections, closure_rows)

    # sec1 "Contents" is excluded, so all descendants (sec2, sec3, sec4) are also excluded
    assert len(result.sections) == 0
    assert len(result.chunks) == 0
    # But only 1 section directly matched a filter (sec1 "Contents")
    assert result.excluded_section_count == 1
    assert result.excluded_section_titles == ("Contents",)


def test_filter_preserves_sections_without_closure_rows() -> None:
    """Sections without closure row relationships should be preserved."""
    sections = [
        _make_section("sec1", "Main Content"),
        _make_section("sec2", "Another Section"),
    ]
    chunks = [_make_chunk("chunk1", "sec1"), _make_chunk("chunk2", "sec2")]
    closure_rows: list[SectionClosureRow] = []

    result = filter_extraction(chunks, sections, closure_rows)

    assert len(result.sections) == 2
    assert len(result.chunks) == 2
    assert result.excluded_section_count == 0
    assert result.excluded_chunk_count == 0


def test_filter_case_sensitive_matching() -> None:
    """Section title matching should be case-sensitive."""
    sections = [
        _make_section("sec1", "references"),  # lowercase - should NOT match
        _make_section("sec2", "REFERENCES"),  # uppercase - should NOT match
        _make_section("sec3", "References"),  # exact case - should match
    ]
    chunks = [
        _make_chunk("chunk1", "sec1"),
        _make_chunk("chunk2", "sec2"),
        _make_chunk("chunk3", "sec3"),
    ]
    closure_rows: list[SectionClosureRow] = []

    result = filter_extraction(chunks, sections, closure_rows)

    assert len(result.sections) == 2
    assert {s.section_id for s in result.sections} == {"sec1", "sec2"}
    assert len(result.chunks) == 2


def test_filter_ignores_table_of_concordance_and_dissenting_sections_with_descendants() -> None:
    """Table of Concordance and dissenting opinion sections should be excluded with their children."""
    sections = [
        _make_section("sec1", "Table of Concordance"),
        _make_section("sec2", "Appendix A"),
        _make_section("sec3", "Dissenting opinions"),
        _make_section("sec4", "Child dissenting note"),
        _make_section("sec5", "Main Content"),
    ]
    chunks = [
        _make_chunk("chunk1", "sec1"),
        _make_chunk("chunk2", "sec2"),
        _make_chunk("chunk3", "sec3"),
        _make_chunk("chunk4", "sec4"),
        _make_chunk("chunk5", "sec5"),
    ]
    closure_rows = [
        _make_closure("sec1", "sec2", 1),
        _make_closure("sec3", "sec4", 1),
    ]

    result = filter_extraction(chunks, sections, closure_rows)

    assert len(result.sections) == 1
    assert result.sections[0].section_id == "sec5"
    assert len(result.chunks) == 1
    assert result.chunks[0].chunk_id == "chunk5"
    assert result.excluded_section_count == 2


def test_filter_empty_input() -> None:
    """Filtering empty input should return empty result with zero counts."""
    result = filter_extraction(chunks=[], sections=[], closure_rows=[])

    assert len(result.sections) == 0
    assert len(result.chunks) == 0
    assert len(result.closure_rows) == 0
    assert result.excluded_section_count == 0
    assert result.excluded_chunk_count == 0


def _make_section(section_id: str, title: str) -> SectionRecord:
    """Helper to create a SectionRecord for testing."""
    return SectionRecord(
        section_id=section_id,
        doc_uid="test-doc",
        parent_section_id=None,
        level=1,
        title=title,
        section_lineage=[title],
        position=0,
    )


def _make_chunk(chunk_id: str, section_id: str, text: str = "Test content") -> Chunk:
    """Helper to create a Chunk for testing."""
    return Chunk(
        id=0,
        doc_uid="test-doc",
        chunk_number=chunk_id,
        page_start="",
        page_end="",
        chunk_id=chunk_id,
        text=text,
        containing_section_id=section_id,
    )


def _make_closure(ancestor_id: str, descendant_id: str, depth: int) -> SectionClosureRow:
    """Helper to create a SectionClosureRow for testing."""
    return SectionClosureRow(
        ancestor_section_id=ancestor_id,
        descendant_section_id=descendant_id,
        depth=depth,
    )
