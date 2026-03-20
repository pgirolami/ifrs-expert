"""PDF extraction logic for IFRS Expert."""

from pathlib import Path
from typing import TypedDict

import fitz

from src.models.chunk import Chunk


class SpanDict(TypedDict):
    """Type for a span in PyMuPDF's dict output."""

    text: str
    bbox: list[float]


class LineDict(TypedDict):
    """Type for a line in PyMuPDF's dict output."""

    spans: list[SpanDict]


class BlockDict(TypedDict):
    """Type for a block in PyMuPDF's dict output."""

    type: int
    bbox: list[float]
    lines: list[LineDict]


class PageDict(TypedDict):
    """Type for a page in PyMuPDF's dict output."""

    blocks: list[BlockDict]


class SpanContent(TypedDict):
    """Type for collected span content."""

    page: str
    page_index: int
    text: str
    x0: float
    y: float
    x1: float


class Section(TypedDict):
    """Type for a section."""

    number: str
    y: float
    x1: float
    page: str
    page_index: int


def is_section_number(text: str) -> bool:
    """Check if text is a valid section number.

    Handles patterns like:
    - B43, B44 (alphanumeric)
    - 1.1, 2.1 (dotted numeric)
    - 1, 2 (numeric)
    """
    if not text or len(text) > 8:
        return False

    # Remove dots and check if alphanumeric
    cleaned = text.replace(".", "")
    return cleaned.isalnum() and not cleaned.isalpha()


def extract_page_number(blocks: list[BlockDict]) -> str | None:
    """Extract the page number from footer area of the page."""
    for block in blocks:
        if block.get("type") == 0:
            bbox = block.get("bbox", [0, 0, 0, 0])
            # Page numbers are typically in the footer area (y > 700)
            if bbox[1] > 700:
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        span_text = span.get("text", "").strip()
                        # Look for page number pattern (e.g., "A856", "2", etc.)
                        if span_text and len(span_text) <= 10:
                            # Check if it's alphanumeric starting with a letter or just digits
                            if span_text[0].isalpha() or span_text[0].isdigit():
                                if span_text.replace(" ", "").isalnum():
                                    return span_text
                            return span_text
    return None


def extract_chunks(pdf_path: Path) -> list[Chunk]:
    """Extract chunks from a PDF file.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        List of Chunk objects.
    """
    doc: fitz.Document = fitz.open(str(pdf_path))

    # Collect all spans from all pages with page info
    all_content: list[SpanContent] = []

    for page_num in range(len(doc)):
        page: fitz.Page = doc[page_num]
        text_dict: PageDict = page.get_text("dict")
        blocks: list[BlockDict] = text_dict.get("blocks", [])

        # Get page number from footer
        page_number: str | None = extract_page_number(blocks)
        if page_number is None:
            page_number = str(page_num + 1)

        # Collect all spans
        for block in blocks:
            if block.get("type") == 0:
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        span_text: str = span.get("text", "")
                        span_bbox: list[float] = span.get("bbox", [0, 0, 0, 0])
                        x0, y0, x1 = span_bbox[0], span_bbox[1], span_bbox[2]
                        all_content.append(
                            {
                                "page": page_number,
                                "page_index": page_num,
                                "text": span_text,
                                "x0": x0,
                                "y": y0,
                                "x1": x1,
                            }
                        )

    doc.close()

    # Sort by page_index, then y, then x
    all_content.sort(key=lambda s: (s["page_index"], s["y"], s["x0"]))

    # Find section numbers
    sections: list[Section] = []
    for span in all_content:
        text: str = span["text"].strip()
        # Skip footer area
        if span["y"] > 700:
            continue
        # Section numbers: left margin, valid section number pattern
        if span["x0"] < 150 and is_section_number(text):
            sections.append(
                {
                    "number": text,
                    "y": span["y"],
                    "x1": span["x1"],
                    "page": span["page"],
                    "page_index": span["page_index"],
                }
            )

    # Sort sections by page, then y
    sections.sort(key=lambda s: (s["page_index"], s["y"]))

    # Deduplicate sections (same section can appear on multiple pages)
    seen: set[str] = set()
    unique_sections: list[Section] = []
    for s in sections:
        if s["number"] not in seen:
            seen.add(s["number"])
            unique_sections.append(s)
    sections = unique_sections

    # Extract text for each section
    results: list[Chunk] = []

    for i, section in enumerate(sections):
        section_num: str = section["number"]
        section_y: float = section["y"]
        section_x_end: float = section["x1"]
        section_page: str = section["page"]
        section_page_index: int = section["page_index"]

        # Find next section's page and y
        next_page_index: float
        next_y: float
        if i + 1 < len(sections):
            next_section: Section = sections[i + 1]
            next_page_index = next_section["page_index"]
            next_y = next_section["y"]
        else:
            next_page_index = float("inf")
            next_y = float("inf")

        section_text_parts: list[str] = []

        # Collect text from all pages from current section to next section
        # For each page, content ends at the next section's y position (if on same page)
        # or at the end of the page content (if on intermediate pages)

        for span in all_content:
            # Skip footer
            if span["y"] > 700:
                continue

            # Determine the upper y bound for this span's page
            page_upper_y: float = float("inf")

            # If on same page as current section
            if span["page_index"] == section_page_index:
                if span["y"] < section_y:
                    continue
                # Use next section's y as upper bound
                page_upper_y = next_y

            # If on the page where next section starts
            elif span["page_index"] == next_page_index:
                # Content should be BEFORE next section starts
                page_upper_y = next_y

            # If between current section and next section pages
            elif span["page_index"] > section_page_index and span["page_index"] < next_page_index:
                # Include all content on intermediate pages
                pass
            else:
                # Outside the range
                continue

            # Check if within bounds
            if span["page_index"] == next_page_index and span["y"] >= page_upper_y:
                continue

            # Skip section numbers
            text: str = span["text"]
            if text.strip() == section_num:
                continue
            if is_section_number(text.strip()) and span["x0"] < 150:
                continue

            # Skip spans in left margin (where section numbers are)
            if span["x0"] < section_x_end + 15:
                # But keep spans that have meaningful content
                if text.strip() and len(text.strip()) > 3:
                    pass  # Could be content, but check more
                else:
                    continue

            if text.strip():
                section_text_parts.append(text.strip())

        # Join text, trying to preserve paragraph structure
        text: str = "\n".join(section_text_parts)

        # Clean up text
        lines: list[str] = text.split("\n")
        cleaned_lines: list[str] = []
        for line in lines:
            # Skip header text (all caps, short)
            if line.isupper() and len(line) < 30:
                continue
            # Skip section titles
            if "Identification" in line and len(line) < 60:
                continue
            # Clean up whitespace but preserve structure
            cleaned: str = " ".join(line.split())
            if cleaned:
                cleaned_lines.append(cleaned)

        # Final pass: filter out section headers/titles
        # These are typically short lines, all caps, or contain specific patterns
        final_lines: list[str] = []
        for line in cleaned_lines:
            # Skip all caps short lines (likely headers)
            if line.isupper() and len(line) < 40:
                continue
            # Skip lines that are just a few words AND look like titles
            if len(line.split()) <= 8 and line[0].isupper():
                # Check if it looks like a title (contains title-related words)
                if any(
                    word in line.lower()
                    for word in [
                        "title",
                        "disclosure",
                        "identification",
                        "measurement",
                        "recognition",
                        "lessee",
                        "paragraph",
                    ]
                ):
                    continue
            final_lines.append(line)

        text = "\n".join(final_lines)

        # Determine page_end - track which pages content appears on
        page_end: str = section_page
        content_pages: set[str] = set()
        for span in all_content:
            if span["page_index"] < section_page_index:
                continue
            if span["page_index"] > next_page_index:
                continue
            if span["y"] > 700:  # Skip footer
                continue
            if span["page_index"] == section_page_index and span["y"] < section_y:
                continue
            if (
                next_page_index != float("inf")
                and span["page_index"] == next_page_index
                and span["y"] >= next_y
            ):
                continue
            if span["text"].strip():
                content_pages.add(span["page"])

        if content_pages:
            page_end = sorted(content_pages)[-1]  # Last page in the set

        results.append(
            Chunk(
                section_path=section_num,
                page_start=section_page,
                page_end=page_end,
                text=text,
            )
        )

    return results
