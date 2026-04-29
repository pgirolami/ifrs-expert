"""Tests for IFRS `Refer:` annotation parsing."""

from __future__ import annotations

from bs4 import BeautifulSoup
from bs4.element import Tag

from src.extraction.ifrs_references import extract_references_from_note, is_refer_annotation


def _note_node(html: str) -> Tag:
    soup = BeautifulSoup(html, "html.parser")
    note = soup.select_one(".note.edu")
    assert isinstance(note, Tag), "Expected an IFRS note node in the test fixture"
    return note


def test_extract_references_cleans_subparagraph_suffixes() -> None:
    """Parenthetical subparagraph suffixes should be cleaned from the stored target text."""
    note = _note_node(
        """
        <span class="note edu">
          <span class="edu_prefix">Refer:</span>
          <a class="xref" href="javascript:;">paragraph 4.1.1(a)</a>
        </span>
        """,
    )

    references = extract_references_from_note(
        note,
        source_doc_uid="ifrs9",
        source_location_type="chunk",
        source_chunk_id="IFRS09_4.1.1",
        source_section_id="IFRS09_0054",
    )

    assert is_refer_annotation(note)
    assert len(references) == 1
    reference = references[0]
    assert reference.source_doc_uid == "ifrs9"
    assert reference.source_location_type == "chunk"
    assert reference.source_chunk_id == "IFRS09_4.1.1"
    assert reference.source_section_id == "IFRS09_0054"
    assert reference.annotation_raw_text == "Refer: paragraph 4.1.1(a)"
    assert reference.target_raw_text == "paragraph 4.1.1(a)"
    assert reference.target_start == "4.1.1"
    assert reference.target_end is None
    assert reference.target_kind == "same_standard_paragraph"
    assert reference.parsed_ok


def test_extract_references_handles_multiple_bc_targets() -> None:
    """One note can contain multiple basis-for-conclusions references."""
    note = _note_node(
        """
        <div class="note edu">
          <span class="edu_prefix">Refer:</span>
          <p>
            <a class="xref" href="javascript:;">paragraphs BC4.1-BC4.45</a>,
            <a class="xref" href="javascript:;">BC4.124-BC4.208</a>
          </p>
        </div>
        """,
    )

    references = extract_references_from_note(
        note,
        source_doc_uid="ifrs9",
        source_location_type="section",
        source_section_id="IFRS09_0054",
    )

    assert len(references) == 2
    assert [reference.target_raw_text for reference in references] == ["paragraphs BC4.1-BC4.45", "BC4.124-BC4.208"]
    assert [reference.target_start for reference in references] == ["BC4.1", "BC4.124"]
    assert [reference.target_end for reference in references] == ["BC4.45", "BC4.208"]
    assert all(reference.target_kind == "basis_for_conclusions" for reference in references)
    assert all(reference.parsed_ok for reference in references)


def test_extract_references_ignores_following_prose_outside_anchors() -> None:
    """Only anchor text should drive classification, not trailing prose in the same note."""
    note = _note_node(
        """
        <div class="note edu">
          <span class="edu_prefix">Refer:</span>
          <a class="xref" href="javascript:;">paragraphs 4.1.1-4.1.5</a>
          <span>Basis for Conclusions for the next paragraph.</span>
        </div>
        """,
    )

    references = extract_references_from_note(
        note,
        source_doc_uid="ifrs9",
        source_location_type="section",
        source_section_id="IFRS09_0054",
    )

    assert len(references) == 1
    reference = references[0]
    assert reference.target_kind == "same_standard_paragraph"
    assert reference.target_start == "4.1.1"
    assert reference.target_end == "4.1.5"


def test_extract_references_handles_cross_document_hints() -> None:
    """Cross-document hints should be preserved in the parsed reference payload."""
    note = _note_node(
        """
        <div class="note edu">
          <span class="edu_prefix">Refer:</span>
          <a class="xref" href="javascript:;">IAS 24 paragraph 9</a>
        </div>
        """,
    )

    references = extract_references_from_note(
        note,
        source_doc_uid="ifrs9",
        source_location_type="section",
        source_section_id="IFRS09_0054",
    )

    assert len(references) == 1
    reference = references[0]
    assert reference.target_doc_hint == "IAS 24"
    assert reference.target_start == "9"
    assert reference.target_end is None
    assert reference.target_kind == "cross_document"
