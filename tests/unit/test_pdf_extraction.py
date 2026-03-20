"""Tests for PDF extraction."""

import pytest

from src.pdf.extraction import extract_page_number, is_section_number


class TestIsSectionNumber:
    """Tests for is_section_number function."""

    def test_alphanumeric_sections(self):
        """Test alphanumeric section numbers like B43."""
        assert is_section_number("B43") is True
        assert is_section_number("B44") is True
        assert is_section_number("A1") is True
        assert is_section_number("IAS39") is True

    def test_dotted_numeric_sections(self):
        """Test dotted numeric sections like 1.1, 2.1."""
        assert is_section_number("1.1") is True
        assert is_section_number("2.1") is True
        assert is_section_number("10.5") is True
        assert is_section_number("1.2.3") is True

    def test_plain_numeric_sections(self):
        """Test plain numeric sections."""
        assert is_section_number("1") is True
        assert is_section_number("42") is True

    def test_invalid_sections(self):
        """Test invalid section numbers."""
        assert is_section_number("") is False
        assert is_section_number("abc") is False  # Letters only
        assert is_section_number("Hello") is False
        assert is_section_number("section") is False

    def test_length_limit(self):
        """Test that very long strings are rejected."""
        assert is_section_number("verylongsectionname") is False


class TestExtractPageNumber:
    """Tests for extract_page_number function."""

    def test_extract_page_number_from_footer(self):
        """Test extracting page number from footer area."""
        blocks = [
            {
                "type": 0,
                "bbox": [50, 710, 200, 730],
                "lines": [
                    {
                        "spans": [
                            {"text": "A856", "bbox": [100, 715, 120, 725]},
                        ],
                    },
                ],
            },
        ]
        result = extract_page_number(blocks)
        assert result == "A856"

    def test_extract_page_number_not_in_footer(self):
        """Test that text above footer is not extracted."""
        blocks = [
            {
                "type": 0,
                "bbox": [50, 100, 200, 120],
                "lines": [
                    {
                        "spans": [
                            {"text": "Some text", "bbox": [100, 105, 120, 115]},
                        ],
                    },
                ],
            },
        ]
        result = extract_page_number(blocks)
        assert result is None

    def test_extract_page_number_empty_blocks(self):
        """Test with empty blocks list."""
        result = extract_page_number([])
        assert result is None
