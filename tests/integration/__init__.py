"""Integration tests for IFRS Expert."""

import pytest
from pathlib import Path


class TestPdfExtractionIntegration:
    """Integration tests for PDF extraction."""

    def test_extract_chunks_from_pdf(self):
        """Test extracting chunks from actual PDF."""
        from src.pdf.extraction import extract_chunks

        pdf_path = Path("examples/ifrs-16-leases_38-39.pdf")
        if not pdf_path.exists():
            pytest.skip("PDF file not found")

        chunks = extract_chunks(pdf_path)

        assert len(chunks) > 0
        assert chunks[0].section_path == "B43"

    def test_extract_chunks_with_section_numbers(self):
        """Test that extracted chunks have correct section numbers."""
        from src.pdf.extraction import extract_chunks

        pdf_path = Path("examples/ifrs-16-leases_38-39.pdf")
        if not pdf_path.exists():
            pytest.skip("PDF file not found")

        chunks = extract_chunks(pdf_path)

        section_paths = [c.section_path for c in chunks]
        assert "B43" in section_paths
        assert "B44" in section_paths
        assert "B45" in section_paths
        assert "B46" in section_paths
        assert "B47" in section_paths
        assert "B48" in section_paths
        assert "B49" in section_paths
        assert "B50" in section_paths

    def test_chunks_have_required_fields(self):
        """Test that chunks have all required fields."""
        from src.pdf.extraction import extract_chunks

        pdf_path = Path("examples/ifrs-16-leases_38-39.pdf")
        if not pdf_path.exists():
            pytest.skip("PDF file not found")

        chunks = extract_chunks(pdf_path)

        for chunk in chunks:
            assert chunk.section_path
            assert chunk.page_start
            assert chunk.page_end
            assert chunk.text

    def test_chunks_page_numbers(self):
        """Test that chunks have correct page numbers."""
        from src.pdf.extraction import extract_chunks

        pdf_path = Path("examples/ifrs-16-leases_38-39.pdf")
        if not pdf_path.exists():
            pytest.skip("PDF file not found")

        chunks = extract_chunks(pdf_path)

        # B48 spans pages A856-A857
        b48 = next((c for c in chunks if c.section_path == "B48"), None)
        assert b48 is not None
        assert b48.page_start == "A856"
        assert b48.page_end == "A857"
