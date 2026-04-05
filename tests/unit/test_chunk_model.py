"""Tests for Chunk model."""

from src.models.chunk import Chunk


class TestChunk:
    """Tests for the Chunk dataclass."""

    def test_create_chunk(self) -> None:
        """Test creating a chunk."""
        chunk = Chunk(
            chunk_number="B43",
            page_start="A856",
            page_end="A857",
            chunk_id="IFRS16_B43",
            containing_section_id=None,
            text="Some text content",
        )
        assert chunk.chunk_number == "B43"
        assert chunk.page_start == "A856"
        assert chunk.page_end == "A857"
        assert chunk.chunk_id == "IFRS16_B43"
        assert chunk.text == "Some text content"

    def test_chunk_attributes(self) -> None:
        """Test chunk has expected attributes."""
        chunk = Chunk(chunk_number="1.1", page_start="1", page_end="2", chunk_id="IFRS09_1.1", text="test")
        assert hasattr(chunk, "id")
        assert hasattr(chunk, "chunk_number")
        assert hasattr(chunk, "page_start")
        assert hasattr(chunk, "page_end")
        assert hasattr(chunk, "chunk_id")
        assert hasattr(chunk, "containing_section_id")
        assert hasattr(chunk, "text")
