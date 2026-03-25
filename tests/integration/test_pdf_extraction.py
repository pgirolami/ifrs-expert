"""Integration tests for PDF extraction."""

import json
from pathlib import Path

import pytest

from src.pdf.extraction import extract_chunks


class TestExtractChunks:
    """Integration tests for extract_chunks function."""

    @pytest.fixture
    def ifrs16_pdf(self) -> Path:
        """Path to IFRS 16 test PDF."""
        return Path(__file__).parent.parent.parent / "examples" / "ifrs-16-leases_38-39.pdf"

    @pytest.fixture
    def ifrs9_appendix_issue_pdf(self) -> Path:
        """Path to IFRS 9 appendix issue test PDF."""
        return Path(__file__).parent.parent.parent / "examples" / "ifrs-9-appendix-issue.pdf"

    @pytest.fixture
    def ifrs9_appendix_issue_expected(self) -> list[dict]:
        """Expected chunks for IFRS 9 appendix issue test."""
        json_path = Path(__file__).parent.parent.parent / "examples" / "ifrs-9-appendix-issue.json"
        with open(json_path) as f:
            return json.load(f)

    def test_extract_chunks_returns_list(self, ifrs16_pdf):
        """Test that extract_chunks returns a list."""
        if not ifrs16_pdf.exists():
            pytest.skip("IFRS 16 PDF not found")

        chunks = extract_chunks(ifrs16_pdf)
        assert isinstance(chunks, list)
        assert len(chunks) > 0

    def test_extract_chunks_structure(self, ifrs16_pdf):
        """Test that chunks have correct structure."""
        if not ifrs16_pdf.exists():
            pytest.skip("IFRS 16 PDF not found")

        chunks = extract_chunks(ifrs16_pdf)
        chunk = chunks[0]

        assert hasattr(chunk, "section_path")
        assert hasattr(chunk, "page_start")
        assert hasattr(chunk, "page_end")
        assert hasattr(chunk, "text")

    def test_extract_ifrs16_sections(self, ifrs16_pdf):
        """Test extracting IFRS 16 sections."""
        if not ifrs16_pdf.exists():
            pytest.skip("IFRS 16 PDF not found")

        chunks = extract_chunks(ifrs16_pdf)
        section_paths = [c.section_path for c in chunks]

        # Should contain B43, B44, etc.
        assert "B43" in section_paths
        assert "B44" in section_paths
        assert "B45" in section_paths

    def test_extract_ifrs16_page_numbers(self, ifrs16_pdf):
        """Test page numbers are extracted correctly."""
        if not ifrs16_pdf.exists():
            pytest.skip("IFRS 16 PDF not found")

        chunks = extract_chunks(ifrs16_pdf)
        chunks_by_section = {c.section_path: c for c in chunks}

        # B43 should be on page A856
        assert chunks_by_section["B43"].page_start == "A856"
        assert chunks_by_section["B43"].page_end == "A856"

    def test_extract_ifrs16_multipage_section(self, ifrs16_pdf):
        """Test extracting sections that span multiple pages."""
        if not ifrs16_pdf.exists():
            pytest.skip("IFRS 16 PDF not found")

        chunks = extract_chunks(ifrs16_pdf)
        chunks_by_section = {c.section_path: c for c in chunks}

        # B48 should span A856-A857
        b48 = chunks_by_section.get("B48")
        if b48:
            assert b48.page_start == "A856"
            assert b48.page_end == "A857"

    def test_extract_chunks_text_not_empty(self, ifrs16_pdf):
        """Test that extracted text is not empty."""
        if not ifrs16_pdf.exists():
            pytest.skip("IFRS 16 PDF not found")

        chunks = extract_chunks(ifrs16_pdf)
        for chunk in chunks:
            assert len(chunk.text) > 0
            assert chunk.text.strip() != ""

    def test_ifrs16_b44_not_contain_legal_title(self, ifrs16_pdf):
        """Test that section B44 does not contain 'Legal title to the underlying asset'.

        This title appears after B44 content but is the title for B45.
        """
        if not ifrs16_pdf.exists():
            pytest.skip("IFRS 16 PDF not found")

        chunks = extract_chunks(ifrs16_pdf)
        chunks_by_section = {c.section_path: c for c in chunks}

        b44 = chunks_by_section.get("B44")
        assert b44 is not None, "Section B44 should exist"
        assert "Legal title to the underlying asset" not in b44.text

    def test_ifrs16_b47_not_contain_lessee_disclosures(self, ifrs16_pdf):
        """Test that section B47 does not contain 'Lessee disclosures (paragraph 59)'.

        This title appears after B47 content but is the title for B48.
        """
        if not ifrs16_pdf.exists():
            pytest.skip("IFRS 16 PDF not found")

        chunks = extract_chunks(ifrs16_pdf)
        chunks_by_section = {c.section_path: c for c in chunks}

        b47 = chunks_by_section.get("B47")
        assert b47 is not None, "Section B47 should exist"
        assert "Lessee disclosures (paragraph 59)" not in b47.text

    def test_ifrs9_appendix_issue_extracts_correctly(
        self, ifrs9_appendix_issue_pdf, ifrs9_appendix_issue_expected
    ):
        """Test that section 7.3.2 does not contain 'Appendix A' and ends at A427.

        This is the main bug being fixed - section 7.3.2 ends at the bottom of A427,
        but Appendix A starts on page A428.
        """
        if not ifrs9_appendix_issue_pdf.exists():
            pytest.skip("IFRS 9 appendix issue PDF not found")

        chunks = extract_chunks(ifrs9_appendix_issue_pdf)
        chunks_by_section = {c.section_path: c for c in chunks}

        # Check each expected chunk
        for expected in ifrs9_appendix_issue_expected:
            section = expected["section_path"]
            chunk = chunks_by_section.get(section)
            assert chunk is not None, f"Section {section} should exist"

            # Check page_end
            assert chunk.page_end == expected["page_end"], (
                f"Section {section} should end at {expected['page_end']}, "
                f"got {chunk.page_end}"
            )

            # Check text doesn't contain title from next section
            if "Appendix A" in expected["text"]:
                assert "Appendix A" not in chunk.text, (
                    f"Section {section} should not contain 'Appendix A'"
                )
