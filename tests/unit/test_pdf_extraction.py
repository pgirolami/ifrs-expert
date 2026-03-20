"""Tests for PDF extraction functionality."""

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
    """Tests for extract_page_number function."""

    def test_extract_page_number_from_footer(self):
        """Test extracting page number from footer."""
        from src.pdf.extraction import extract_page_number

        blocks = [
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

        result = extract_page_number(blocks)
        assert result == "A856"

    def test_extract_page_number_not_in_footer(self):
        """Test that non-footer text is not extracted."""
        from src.pdf.extraction import extract_page_number

        blocks = [
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

        result = extract_page_number(blocks)
        assert result is None

    def test_extract_page_number_empty_blocks(self):
        """Test empty blocks."""
        from src.pdf.extraction import extract_page_number

        result = extract_page_number([])
        assert result is None

        result = extract_page_number([{"type": 1}])
        assert result is None
