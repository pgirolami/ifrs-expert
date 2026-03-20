"""Integration tests for PDF extraction."""

from pathlib import Path

import pytest

from src.pdf.extraction import extract_chunks


class TestExtractChunks:
    """Integration tests for extract_chunks function."""

    @pytest.fixture
    def ifrs16_pdf(self) -> Path:
        """Path to IFRS 16 test PDF."""
        return Path(__file__).parent.parent.parent / "examples" / "ifrs-16-leases_38-39.pdf"

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
