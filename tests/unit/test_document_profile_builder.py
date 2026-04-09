"""Tests for document-level representation building."""

from __future__ import annotations

from src.models.chunk import Chunk
from src.models.document import DocumentRecord
from src.models.section import SectionClosureRow, SectionRecord
from src.retrieval.document_profile_builder import DocumentProfileBuilder


def test_document_profile_builder_extracts_background_issue_and_scope_without_html_intro_fallback() -> None:
    """HTML documents should populate matched fields without inventing an intro fallback."""
    document = DocumentRecord(
        doc_uid="ifric16",
        source_type="html",
        source_title="IFRIC 16 Hedges of a Net Investment in a Foreign Operation",
        source_url="https://www.ifrs.org/ifric16.html",
        canonical_url="https://www.ifrs.org/ifric16.html",
        captured_at="2026-04-05T10:00:00Z",
    )
    sections = [
        SectionRecord(
            section_id="sec-background",
            doc_uid="ifric16",
            parent_section_id=None,
            level=2,
            title="Background",
            section_lineage=["Background"],
            embedding_text="Background",
            position=1,
        ),
        SectionRecord(
            section_id="sec-issue",
            doc_uid="ifric16",
            parent_section_id=None,
            level=2,
            title="Issue",
            section_lineage=["Issue"],
            embedding_text="Issue",
            position=2,
        ),
        SectionRecord(
            section_id="sec-scope",
            doc_uid="ifric16",
            parent_section_id=None,
            level=2,
            title="Scope",
            section_lineage=["Scope"],
            embedding_text="Scope",
            position=3,
        ),
    ]
    closure_rows = [
        SectionClosureRow("sec-background", "sec-background", 0),
        SectionClosureRow("sec-issue", "sec-issue", 0),
        SectionClosureRow("sec-scope", "sec-scope", 0),
    ]
    chunks = [
        Chunk(doc_uid="ifric16", chunk_number="1", page_start="", page_end="", chunk_id="c1", containing_section_id="sec-background", text="This Interpretation addresses hedges of net investments."),
        Chunk(doc_uid="ifric16", chunk_number="2", page_start="", page_end="", chunk_id="c2", containing_section_id="sec-issue", text="The issue is which entity may hold the hedging instrument."),
        Chunk(doc_uid="ifric16", chunk_number="3", page_start="", page_end="", chunk_id="c3", containing_section_id="sec-scope", text="This Interpretation applies to IFRS 9 hedges of net investments."),
    ]

    built_profile = DocumentProfileBuilder().build(
        document=document,
        chunks=chunks,
        sections=sections,
        section_closure_rows=closure_rows,
    )

    assert built_profile.document.background_text == "This Interpretation addresses hedges of net investments."
    assert built_profile.document.issue_text == "The issue is which entity may hold the hedging instrument."
    assert built_profile.document.scope_text == "This Interpretation applies to IFRS 9 hedges of net investments."
    assert built_profile.document.intro_text is None
    assert built_profile.document.toc_text is None
    assert "Title: IFRIC 16 Hedges of a Net Investment in a Foreign Operation" in built_profile.embedding_text
    assert "Background: This Interpretation addresses hedges of net investments." in built_profile.embedding_text
    assert "Issue: The issue is which entity may hold the hedging instrument." in built_profile.embedding_text
    assert "TOC:" not in built_profile.embedding_text
    assert "Introduction:" not in built_profile.embedding_text


def test_document_profile_builder_uses_pdf_fallback_intro() -> None:
    """PDF documents should fall back to leading chunk text when headings are unavailable."""
    document = DocumentRecord(
        doc_uid="ifrs9-pdf",
        source_type="pdf",
        source_title="IFRS 9",
        source_url=None,
        canonical_url=None,
        captured_at=None,
    )
    chunks = [
        Chunk(doc_uid="ifrs9-pdf", chunk_number="1", page_start="1", page_end="1", text="First paragraph."),
        Chunk(doc_uid="ifrs9-pdf", chunk_number="2", page_start="1", page_end="1", text="Second paragraph."),
    ]

    built_profile = DocumentProfileBuilder().build(
        document=document,
        chunks=chunks,
        sections=[],
        section_closure_rows=[],
    )

    assert built_profile.document.intro_text == "First paragraph.\nSecond paragraph."
    assert built_profile.document.background_text is None
    assert built_profile.document.issue_text is None
    assert "Introduction: First paragraph.\nSecond paragraph." in built_profile.embedding_text


def test_document_profile_builder_pulls_objective_subsections_into_document_representation() -> None:
    """Objective text should include descendant subsection chunks, not only direct section chunks."""
    document = DocumentRecord(
        doc_uid="ifrs12",
        source_type="html",
        source_title="IFRS 12",
        source_url="https://www.ifrs.org/ifrs12.html",
        canonical_url="https://www.ifrs.org/ifrs12.html",
        captured_at="2026-04-05T10:00:00Z",
    )
    sections = [
        SectionRecord(
            section_id="sec-objective",
            doc_uid="ifrs12",
            parent_section_id=None,
            level=2,
            title="Objective",
            section_lineage=["Objective"],
            embedding_text="Objective",
            position=1,
        ),
        SectionRecord(
            section_id="sec-objective-sub",
            doc_uid="ifrs12",
            parent_section_id="sec-objective",
            level=3,
            title="Subsidiaries",
            section_lineage=["Objective", "Subsidiaries"],
            embedding_text="Subsidiaries",
            position=2,
        ),
    ]
    closure_rows = [
        SectionClosureRow("sec-objective", "sec-objective", 0),
        SectionClosureRow("sec-objective", "sec-objective-sub", 1),
        SectionClosureRow("sec-objective-sub", "sec-objective-sub", 0),
    ]
    chunks = [
        Chunk(doc_uid="ifrs12", chunk_number="1", page_start="", page_end="", chunk_id="c1", containing_section_id="sec-objective", text="The objective is to require disclosure of interests."),
        Chunk(doc_uid="ifrs12", chunk_number="2", page_start="", page_end="", chunk_id="c2", containing_section_id="sec-objective-sub", text="These disclosures help users evaluate subsidiaries and related risks."),
    ]

    built_profile = DocumentProfileBuilder().build(
        document=document,
        chunks=chunks,
        sections=sections,
        section_closure_rows=closure_rows,
    )

    assert built_profile.document.objective_text == ("The objective is to require disclosure of interests.\nThese disclosures help users evaluate subsidiaries and related risks.")
    assert built_profile.document.toc_text is None
    assert "Objective: The objective is to require disclosure of interests." in built_profile.embedding_text
    assert "These disclosures help users evaluate subsidiaries and related risks." in built_profile.embedding_text
    assert "TOC:" not in built_profile.embedding_text


def test_document_profile_builder_uses_filtered_sections_for_toc_when_provided() -> None:
    """TOC should be able to exclude sections that are filtered out for persistence."""
    document = DocumentRecord(
        doc_uid="ifrs9",
        source_type="html",
        source_title="IFRS 9",
        source_url="https://www.ifrs.org/ifrs9.html",
        canonical_url="https://www.ifrs.org/ifrs9.html",
        captured_at="2026-04-05T10:00:00Z",
    )
    sections = [
        SectionRecord(
            section_id="sec-contents",
            doc_uid="ifrs9",
            parent_section_id=None,
            level=2,
            title="Contents",
            section_lineage=["Contents"],
            embedding_text="Contents",
            position=1,
        ),
        SectionRecord(
            section_id="sec-scope",
            doc_uid="ifrs9",
            parent_section_id=None,
            level=2,
            title="Scope",
            section_lineage=["Scope"],
            embedding_text="Scope",
            position=2,
        ),
    ]

    built_profile = DocumentProfileBuilder().build(
        document=document,
        chunks=[],
        sections=sections,
        section_closure_rows=[],
        toc_sections=[sections[1]],
    )

    assert built_profile.document.toc_text is None
    assert "TOC:" not in built_profile.embedding_text


def test_document_profile_builder_truncates_embedding_text_proportionally() -> None:
    """Embedding truncation should preserve the relative weight of larger parts."""
    document = DocumentRecord(
        doc_uid="ifrs9",
        source_type="html",
        source_title="Short title",
        source_url="https://www.ifrs.org/ifrs9.html",
        canonical_url="https://www.ifrs.org/ifrs9.html",
        captured_at="2026-04-05T10:00:00Z",
    )
    long_scope_text = "S" * 300
    short_issue_text = "I" * 30
    sections = [
        SectionRecord(
            section_id="sec-issue",
            doc_uid="ifrs9",
            parent_section_id=None,
            level=2,
            title="Issue",
            section_lineage=["Issue"],
            embedding_text="Issue",
            position=1,
        ),
        SectionRecord(
            section_id="sec-scope",
            doc_uid="ifrs9",
            parent_section_id=None,
            level=2,
            title="Scope",
            section_lineage=["Scope"],
            embedding_text="Scope",
            position=2,
        ),
    ]
    closure_rows = [
        SectionClosureRow("sec-issue", "sec-issue", 0),
        SectionClosureRow("sec-scope", "sec-scope", 0),
    ]
    chunks = [
        Chunk(doc_uid="ifrs9", chunk_number="1", page_start="", page_end="", chunk_id="c1", containing_section_id="sec-issue", text=short_issue_text),
        Chunk(doc_uid="ifrs9", chunk_number="2", page_start="", page_end="", chunk_id="c2", containing_section_id="sec-scope", text=long_scope_text),
    ]

    built_profile = DocumentProfileBuilder(max_embedding_chars=120).build(
        document=document,
        chunks=chunks,
        sections=sections,
        section_closure_rows=closure_rows,
    )

    embedding_lines = built_profile.embedding_text.splitlines()
    issue_value = next(line.removeprefix("Issue: ") for line in embedding_lines if line.startswith("Issue: "))
    scope_value = next(line.removeprefix("Scope: ") for line in embedding_lines if line.startswith("Scope: "))

    assert len(built_profile.embedding_text) <= 120
    assert built_profile.embedding_text.startswith("Title: Short title\n")
    assert len(scope_value) > len(issue_value)
    assert len(scope_value) >= len(issue_value) * 4
