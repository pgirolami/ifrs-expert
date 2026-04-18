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
            position=1,
        ),
        SectionRecord(
            section_id="sec-issue",
            doc_uid="ifric16",
            parent_section_id=None,
            level=2,
            title="Issue",
            section_lineage=["Issue"],
            position=2,
        ),
        SectionRecord(
            section_id="sec-scope",
            doc_uid="ifric16",
            parent_section_id=None,
            level=2,
            title="Scope",
            section_lineage=["Scope"],
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


def test_document_profile_builder_extracts_plural_issues_and_excludes_it_from_toc() -> None:
    """Plural Issues headings should populate issue_text and be excluded from TOC output."""
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
            position=1,
        ),
        SectionRecord(
            section_id="sec-scope",
            doc_uid="ifric16",
            parent_section_id=None,
            level=2,
            title="Scope",
            section_lineage=["Scope"],
            position=2,
        ),
        SectionRecord(
            section_id="sec-issues",
            doc_uid="ifric16",
            parent_section_id=None,
            level=2,
            title="Issues",
            section_lineage=["Issues"],
            position=3,
        ),
        SectionRecord(
            section_id="sec-issues-child",
            doc_uid="ifric16",
            parent_section_id="sec-issues",
            level=3,
            title="Foreign currency exposures",
            section_lineage=["Issues", "Foreign currency exposures"],
            position=4,
        ),
        SectionRecord(
            section_id="sec-consensus",
            doc_uid="ifric16",
            parent_section_id=None,
            level=2,
            title="Consensus",
            section_lineage=["Consensus"],
            position=5,
        ),
    ]
    closure_rows = [
        SectionClosureRow("sec-background", "sec-background", 0),
        SectionClosureRow("sec-scope", "sec-scope", 0),
        SectionClosureRow("sec-issues", "sec-issues", 0),
        SectionClosureRow("sec-issues", "sec-issues-child", 1),
        SectionClosureRow("sec-issues-child", "sec-issues-child", 0),
        SectionClosureRow("sec-consensus", "sec-consensus", 0),
    ]
    chunks = [
        Chunk(doc_uid="ifric16", chunk_number="1", page_start="", page_end="", chunk_id="c1", containing_section_id="sec-background", text="This Interpretation addresses hedges of net investments."),
        Chunk(doc_uid="ifric16", chunk_number="2", page_start="", page_end="", chunk_id="c2", containing_section_id="sec-scope", text="This Interpretation applies to IFRS 9 hedges of net investments."),
        Chunk(doc_uid="ifric16", chunk_number="3", page_start="", page_end="", chunk_id="c3", containing_section_id="sec-issues", text="The issues are which entity may hold the hedging instrument."),
        Chunk(doc_uid="ifric16", chunk_number="4", page_start="", page_end="", chunk_id="c4", containing_section_id="sec-issues-child", text="It also considers how the hedged risk is identified in consolidated financial statements."),
        Chunk(doc_uid="ifric16", chunk_number="5", page_start="", page_end="", chunk_id="c5", containing_section_id="sec-consensus", text="The consensus sets out the interpretation outcome."),
    ]

    built_profile = DocumentProfileBuilder().build(
        document=document,
        chunks=chunks,
        sections=sections,
        section_closure_rows=closure_rows,
    )

    assert built_profile.document.issue_text == ("The issues are which entity may hold the hedging instrument.\nIt also considers how the hedged risk is identified in consolidated financial statements.")
    assert built_profile.document.toc_text == "Consensus"
    assert "Issue: The issues are which entity may hold the hedging instrument." in built_profile.embedding_text
    assert "It also considers how the hedged risk is identified in consolidated financial statements." in built_profile.embedding_text
    assert "TOC: Consensus" in built_profile.embedding_text
    assert "Issues" not in built_profile.document.toc_text
    assert "Foreign currency exposures" not in built_profile.document.toc_text


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


def test_document_profile_builder_extracts_navis_intro_from_essentiel_generalites_section() -> None:
    """Navis documents should use the Généralités subsection under L'ESSENTIEL DE LA NORME as intro text."""
    document = DocumentRecord(
        doc_uid="navis-QRIFRS-C2A8E6F292F99E-EFL",
        source_type="html",
        source_title="CHAPITRE 4 Cadre conceptuel de l'information financière",
        source_url="https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&refId=C2A8E6F292F99E-EFL",
        canonical_url="https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&refId=C2A8E6F292F99E-EFL",
        captured_at="2026-04-05T10:00:00Z",
        source_domain="abonnes.efl.fr",
        document_type="NAVIS",
    )
    sections = [
        SectionRecord(
            section_id="chapter-1",
            doc_uid=document.doc_uid,
            parent_section_id=None,
            level=1,
            title="Cadre conceptuel de l'information financière",
            section_lineage=["Cadre conceptuel de l'information financière"],
            position=1,
        ),
        SectionRecord(
            section_id="essential",
            doc_uid=document.doc_uid,
            parent_section_id="chapter-1",
            level=2,
            title="L’ESSENTIEL DE LA NORME",
            section_lineage=["Cadre conceptuel de l'information financière", "L’ESSENTIEL DE LA NORME"],
            position=2,
        ),
        SectionRecord(
            section_id="generalites",
            doc_uid=document.doc_uid,
            parent_section_id="essential",
            level=3,
            title="A. Généralités",
            section_lineage=["Cadre conceptuel de l'information financière", "L’ESSENTIEL DE LA NORME", "A. Généralités"],
            position=3,
        ),
        SectionRecord(
            section_id="generalites-child",
            doc_uid=document.doc_uid,
            parent_section_id="generalites",
            level=4,
            title="Champ d'application",
            section_lineage=[
                "Cadre conceptuel de l'information financière",
                "L’ESSENTIEL DE LA NORME",
                "A. Généralités",
                "Champ d'application",
            ],
            position=4,
        ),
    ]
    closure_rows = [
        SectionClosureRow("chapter-1", "chapter-1", 0),
        SectionClosureRow("chapter-1", "essential", 1),
        SectionClosureRow("chapter-1", "generalites", 2),
        SectionClosureRow("chapter-1", "generalites-child", 3),
        SectionClosureRow("essential", "essential", 0),
        SectionClosureRow("essential", "generalites", 1),
        SectionClosureRow("essential", "generalites-child", 2),
        SectionClosureRow("generalites", "generalites", 0),
        SectionClosureRow("generalites", "generalites-child", 1),
        SectionClosureRow("generalites-child", "generalites-child", 0),
    ]
    chunks = [
        Chunk(
            doc_uid=document.doc_uid,
            chunk_number="12501",
            page_start="",
            page_end="",
            chunk_id="P8A8E6F292F99E-EFL",
            containing_section_id="generalites",
            text="Premier paragraphe d'introduction.",
        ),
        Chunk(
            doc_uid=document.doc_uid,
            chunk_number="12502",
            page_start="",
            page_end="",
            chunk_id="P8A8E6F292F99E-EFL-2",
            containing_section_id="generalites-child",
            text="Deuxième paragraphe d'introduction.",
        ),
    ]

    built_profile = DocumentProfileBuilder().build(
        document=document,
        chunks=chunks,
        sections=sections,
        section_closure_rows=closure_rows,
    )

    assert built_profile.document.intro_text == ("Premier paragraphe d'introduction.\nDeuxième paragraphe d'introduction.")
    assert "Introduction: Premier paragraphe d'introduction." in built_profile.embedding_text


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
            position=1,
        ),
        SectionRecord(
            section_id="sec-objective-sub",
            doc_uid="ifrs12",
            parent_section_id="sec-objective",
            level=3,
            title="Subsidiaries",
            section_lineage=["Objective", "Subsidiaries"],
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
            position=1,
        ),
        SectionRecord(
            section_id="sec-scope",
            doc_uid="ifrs9",
            parent_section_id=None,
            level=2,
            title="Scope",
            section_lineage=["Scope"],
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


def test_document_profile_builder_does_not_extract_navis_intro_without_matching_essentiel_parent() -> None:
    """Navis intro extraction should require Généralités to sit under an L'ESSENTIEL DE LA NORME section."""
    document = DocumentRecord(
        doc_uid="navis-QRIFRS-C2A8E6F292F99E-EFL",
        source_type="html",
        source_title="CHAPITRE 4 Cadre conceptuel de l'information financière",
        source_url="https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&refId=C2A8E6F292F99E-EFL",
        canonical_url="https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&refId=C2A8E6F292F99E-EFL",
        captured_at="2026-04-05T10:00:00Z",
        source_domain="abonnes.efl.fr",
        document_type="NAVIS",
    )
    sections = [
        SectionRecord(
            section_id="chapter-1",
            doc_uid=document.doc_uid,
            parent_section_id=None,
            level=1,
            title="Cadre conceptuel de l'information financière",
            section_lineage=["Cadre conceptuel de l'information financière"],
            position=1,
        ),
        SectionRecord(
            section_id="overview",
            doc_uid=document.doc_uid,
            parent_section_id="chapter-1",
            level=2,
            title="Présentation générale",
            section_lineage=["Cadre conceptuel de l'information financière", "Présentation générale"],
            position=2,
        ),
        SectionRecord(
            section_id="generalites",
            doc_uid=document.doc_uid,
            parent_section_id="overview",
            level=3,
            title="Généralités",
            section_lineage=["Cadre conceptuel de l'information financière", "Présentation générale", "Généralités"],
            position=3,
        ),
    ]
    closure_rows = [
        SectionClosureRow("chapter-1", "chapter-1", 0),
        SectionClosureRow("chapter-1", "overview", 1),
        SectionClosureRow("chapter-1", "generalites", 2),
        SectionClosureRow("overview", "overview", 0),
        SectionClosureRow("overview", "generalites", 1),
        SectionClosureRow("generalites", "generalites", 0),
    ]
    chunks = [
        Chunk(
            doc_uid=document.doc_uid,
            chunk_number="12501",
            page_start="",
            page_end="",
            chunk_id="P8A8E6F292F99E-EFL",
            containing_section_id="generalites",
            text="Texte qui ne doit pas être promu en introduction.",
        )
    ]

    built_profile = DocumentProfileBuilder().build(
        document=document,
        chunks=chunks,
        sections=sections,
        section_closure_rows=closure_rows,
    )

    assert built_profile.document.intro_text is None
    assert "Introduction:" not in built_profile.embedding_text


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
            position=1,
        ),
        SectionRecord(
            section_id="sec-scope",
            doc_uid="ifrs9",
            parent_section_id=None,
            level=2,
            title="Scope",
            section_lineage=["Scope"],
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
