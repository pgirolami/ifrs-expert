"""Tests for Chunk model."""

import pytest

from src.models.chunk import Chunk as PdfChunk


class TestPdfChunk:
    """Tests for the PDF Chunk dataclass."""

    def test_create_chunk(self):
        """Test creating a Chunk."""
        chunk = PdfChunk(
            section_path="B43",
            page_start="A856",
            page_end="A857",
            text="Some text content",
        )
        assert chunk.section_path == "B43"
        assert chunk.page_start == "A856"
        assert chunk.page_end == "A857"
        assert chunk.text == "Some text content"

    def test_chunk_attributes(self):
        """Test chunk has expected attributes."""
        chunk = PdfChunk(section_path="1.1", page_start="1", page_end="2", text="test")
        assert hasattr(chunk, "section_path")
        assert hasattr(chunk, "page_start")
        assert hasattr(chunk, "page_end")
        assert hasattr(chunk, "text")
