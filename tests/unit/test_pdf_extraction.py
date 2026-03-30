"""Tests for PDF extraction functionality."""

from pathlib import Path

import pytest


class TestIsSectionNumber:
    """Tests for is_section_number function."""

    def test_alphanumeric_sections(self):
        """Test alphanumeric section numbers like B43."""
        from src.pdf.extraction import is_section_number

        assert is_section_number("B43") is True
        assert is_section_number("B44") is True
        assert is_section_number("B1") is True
        assert is_section_number("A1") is True

    def test_dotted_numeric_sections(self):
        """Test dotted numeric section numbers like 1.1, 2.1."""
        from src.pdf.extraction import is_section_number

        assert is_section_number("1.1") is True
        assert is_section_number("2.1") is True
        assert is_section_number("1.2.3") is True
        assert is_section_number("10.5") is True

    def test_plain_numeric_sections(self):
        """Test plain numeric section numbers like 1, 2."""
        from src.pdf.extraction import is_section_number

        assert is_section_number("1") is True
        assert is_section_number("23") is True
        assert is_section_number("100") is True

    def test_invalid_sections(self):
        """Test invalid section numbers."""
        from src.pdf.extraction import is_section_number

        # Letters only
        assert is_section_number("ABC") is False
        assert is_section_number("abc") is False

        # Special characters
        assert is_section_number("B43!") is False
        assert is_section_number("1-1") is False

        # Empty
        assert is_section_number("") is False

    def test_length_limit(self):
        """Test length limit for section numbers."""
        from src.pdf.extraction import is_section_number

        # Too long
        assert is_section_number("123456789") is False
        assert is_section_number("B123456789") is False


class TestExtractPageNumber:
    """Tests for extract_page_number_from_footer function."""

    def test_extract_page_number_from_footer(self):
        """Test extracting page number from footer."""
        from src.pdf.extraction import BlockDict, extract_page_number_from_footer

        blocks: list[BlockDict] = [
            {
                "type": 0,
                "bbox": [0, 720, 100, 750],
                "lines": [
                    {
                        "spans": [
                            {"text": "A856", "bbox": [50, 730, 80, 745]},
                        ]
                    }
                ],
            }
        ]

        result = extract_page_number_from_footer(blocks)
        assert result == "A856"

    def test_extract_page_number_not_in_footer(self):
        """Test that non-footer text is not extracted."""
        from src.pdf.extraction import BlockDict, extract_page_number_from_footer

        blocks: list[BlockDict] = [
            {
                "type": 0,
                "bbox": [0, 100, 100, 150],
                "lines": [
                    {
                        "spans": [
                            {"text": "Some text", "bbox": [50, 110, 80, 130]},
                        ]
                    }
                ],
            }
        ]

        result = extract_page_number_from_footer(blocks)
        assert result is None

    def test_extract_page_number_empty_blocks(self):
        """Test empty blocks."""
        from src.pdf.extraction import BlockDict, extract_page_number_from_footer

        result = extract_page_number_from_footer([])
        assert result is None

        minimal_block: BlockDict = {"type": 1, "bbox": [0, 0, 0, 0], "lines": []}
        result = extract_page_number_from_footer([minimal_block])
        assert result is None


class TestExtractChunks:
    """Tests for extract_chunks function."""

    def test_ifrs9_section_6_5_2_not_truncated(self):
        """Test that section 6.5.2 is fully extracted with complete ending.

        Regression test: section 6.5.2 was being truncated because the bold
        content within the section (like "(a)", "(b)", "(c)") was being incorrectly
        used as a boundary, cutting off the "IAS 21." reference at the end.
        """
        from src.pdf.extraction import extract_chunks

        pdf_path = Path("../examples/ifrs/ifrs-9-financial-instruments 2025 required.pdf")
        chunks = extract_chunks(pdf_path)

        # Find section 6.5.2
        chunk_6_5_2 = None
        for chunk in chunks:
            if chunk.section_path == "6.5.2":
                chunk_6_5_2 = chunk
                break

        assert chunk_6_5_2 is not None, "Section 6.5.2 not found in extracted chunks"

        # Verify the section ends with "IAS 21." (the complete reference)
        assert chunk_6_5_2.text.endswith("IAS 21."), (
            f"Section 6.5.2 is truncated. Expected to end with 'IAS 21.' but got: "
            f"...{chunk_6_5_2.text[-100:]}"
        )

        # Verify the full content includes the complete hedge of net investment text
        assert "hedge of a net investment in a foreign operation as defined in" in chunk_6_5_2.text
        assert "IAS 21." in chunk_6_5_2.text
