"""PDF extraction logic for IFRS Expert."""

from pathlib import Path
from typing import TypedDict

import fitz

from src.models.chunk import Chunk

# Section number validation thresholds
MAX_SECTION_NUMBER_LENGTH = 8
MIN_SECTION_TEXT_LENGTH = 3
MAX_PAGE_NUMBER_LENGTH = 10

# PDF coordinate thresholds
FOOTER_Y_THRESHOLD = 700
LEFT_MARGIN_THRESHOLD = 150
SECTION_X_BUFFER = 15
MIN_CONTENT_LENGTH = 3

# Page header detection thresholds (document identifiers like "IFRS 9" at top of pages)
PAGE_HEADER_MAX_LENGTH = 20
PAGE_HEADER_Y_THRESHOLD = 150
PAGE_HEADER_X_THRESHOLD = 200

# Header detection thresholds
HEADER_MAX_LENGTH = 30
IDENTIFICATION_MAX_LENGTH = 60
SHORT_TITLE_LENGTH = 40
TITLE_WORD_COUNT = 8

# PDF flags
BOLD_TEXT_FLAG = 20


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
    flags: int


class SectionMarker(TypedDict):
    """Type for a section marker (number found in left margin)."""

    number: str
    y: float
    x1: float
    page: str
    page_index: int
    is_bold_title: bool


def is_section_number(text: str) -> bool:
    """Check if text is a valid section number.

    Handles patterns like:
    - B43, B44 (alphanumeric)
    - 1.1, 2.1 (dotted numeric)
    - 1, 2 (numeric)
    """
    if not text or len(text) > MAX_SECTION_NUMBER_LENGTH:
        return False

    # Remove dots and check if alphanumeric
    cleaned = text.replace(".", "")
    return cleaned.isalnum() and not cleaned.isalpha()


def is_section_title(text: str) -> bool:
    """Check if text looks like a section title (not a section number).

    Section titles are typically:
    - Title case or all caps
    - Not matching section number patterns
    - Not just numbers/letters combinations
    """
    if not text:
        return False

    if is_section_number(text):
        return False

    if len(text) < MIN_SECTION_TEXT_LENGTH:
        return False

    title_starters = [
        "appendix",
        "defined",
        "scope",
        "objective",
        "recognition",
        "measurement",
        "derecognition",
        "presentation",
        "disclosure",
        "initial",
        "subsequent",
        "impairment",
        "hedge",
        "embedded",
        "effective",
        "contract",
        "financial",
        "lease",
        "revenue",
    ]

    lower_text = text.lower()
    return any(lower_text.startswith(starter) for starter in title_starters)


def extract_page_number_from_footer(blocks: list[BlockDict]) -> str | None:
    """Extract the page number from footer area of the page."""
    for block in blocks:
        if block.get("type") == 0:
            bbox = block.get("bbox", [0, 0, 0, 0])
            if bbox[1] > FOOTER_Y_THRESHOLD:
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        span_text = span.get("text", "").strip()
                        if span_text and len(span_text) <= MAX_PAGE_NUMBER_LENGTH and (span_text[0].isalpha() or span_text[0].isdigit()) and span_text.replace(" ", "").isalnum():
                            return span_text
    return None


def is_page_header_text(span: SpanContent) -> bool:
    """Check if span is a page header (document identifier like 'IFRS 9')."""
    text = span["text"]
    if not text:
        return False

    # Must be all caps, short, at top of page, in left margin
    return text.isupper() and len(text) < PAGE_HEADER_MAX_LENGTH and span["y"] < PAGE_HEADER_Y_THRESHOLD and span["x0"] < PAGE_HEADER_X_THRESHOLD


def is_in_left_margin(span: SpanContent, margin_x_threshold: float) -> bool:
    """Check if span is in the left margin area."""
    return span["x0"] < margin_x_threshold


def is_footer_text(span: SpanContent) -> bool:
    """Check if span is in the footer area of the page."""
    return span["y"] > FOOTER_Y_THRESHOLD


def is_standalone_section_number(span: SpanContent, section_num: str) -> bool:
    """Check if span is the section number itself (not content)."""
    text = span["text"].strip()
    return text == section_num


def is_meaningful_content(span: SpanContent) -> bool:
    """Check if span has meaningful content (not just a heading)."""
    text = span["text"].strip()
    if not text:
        return False
    return len(text) > MIN_CONTENT_LENGTH


def is_likely_header_line(line: str) -> bool:
    """Check if a line looks like a section header (all caps, short, no numbers)."""
    if not line:
        return False
    return line.isupper() and len(line) < HEADER_MAX_LENGTH and not any(c.isdigit() for c in line)


def is_identification_header(line: str) -> bool:
    """Check if line is an Identification section header."""
    return "Identification" in line and len(line) < IDENTIFICATION_MAX_LENGTH


def is_short_title_line(line: str) -> bool:
    """Check if a line looks like a short title (few words, title-like)."""
    if not line:
        return False

    words = line.split()
    if len(words) > TITLE_WORD_COUNT:
        return False

    if not line[0].isupper():
        return False

    title_indicators = ["title", "disclosure", "identification", "measurement", "recognition", "lessee", "paragraph"]
    return any(word in line.lower() for word in title_indicators)


def collect_all_spans_from_pdf(pdf_path: Path) -> list[SpanContent]:
    """Load PDF and collect all text spans with their positions."""
    doc: fitz.Document = fitz.open(str(pdf_path))
    all_content: list[SpanContent] = []

    for page_num in range(len(doc)):
        page: fitz.Page = doc[page_num]
        text_dict: PageDict = page.get_text("dict")
        blocks: list[BlockDict] = text_dict.get("blocks", [])

        # Get page number from footer
        page_number = extract_page_number_from_footer(blocks)
        if page_number is None:
            page_number = str(page_num + 1)

        # Collect all text spans
        for block in blocks:
            if block.get("type") == 0:
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        span_text: str = span.get("text", "")
                        span_bbox: list[float] = span.get("bbox", [0, 0, 0, 0])
                        x0, y0, x1 = span_bbox[0], span_bbox[1], span_bbox[2]
                        span_flags: int = span.get("flags", 0)
                        all_content.append(
                            {
                                "page": page_number,
                                "page_index": page_num,
                                "text": span_text,
                                "x0": x0,
                                "y": y0,
                                "x1": x1,
                                "flags": span_flags,
                            },
                        )

    doc.close()

    # Sort by page, then vertical position, then horizontal position
    all_content.sort(key=lambda s: (s["page_index"], s["y"], s["x0"]))
    return all_content


def find_section_markers(all_content: list[SpanContent]) -> list[SectionMarker]:
    """Find section numbers in the left margin of the PDF."""
    sections: list[SectionMarker] = []

    for span in all_content:
        text = span["text"].strip()

        # Skip footer area
        if is_footer_text(span):
            continue

        # Look for section numbers in left margin
        if is_in_left_margin(span, LEFT_MARGIN_THRESHOLD) and is_section_number(text):
            is_bold = span.get("flags", 0) == BOLD_TEXT_FLAG
            sections.append(
                {
                    "number": text,
                    "y": span["y"],
                    "x1": span["x1"],
                    "page": span["page"],
                    "page_index": span["page_index"],
                    "is_bold_title": is_bold,
                },
            )

    # Sort by page, then vertical position
    sections.sort(key=lambda s: (s["page_index"], s["y"]))

    # Deduplicate (same section can appear on multiple pages)
    seen: set[str] = set()
    unique_sections: list[SectionMarker] = []
    for s in sections:
        if s["number"] not in seen:
            seen.add(s["number"])
            unique_sections.append(s)

    return unique_sections


def find_bold_title_after_section(
    section: SectionMarker,
    next_section: SectionMarker | None,
    all_content: list[SpanContent],
) -> tuple[int, float] | None:
    """Find the next bold title that marks a section boundary.

    Looks for bold text on a different page than current section,
    which indicates a new major section starts.
    """
    section_page = section["page_index"]
    section_y = section["y"]

    next_page = next_section["page_index"] if next_section else float("inf")
    next_y = next_section["y"] if next_section else float("inf")

    for span in all_content:
        # Skip pages before current section
        if span["page_index"] < section_page:
            continue
        # Skip past the next section
        if span["page_index"] > next_page:
            continue

        # Skip if on same page and before current section
        if span["page_index"] == section_page and span["y"] <= section_y:
            continue

        # Skip the next section itself
        if span["page_index"] == next_page and span["y"] >= next_y:
            continue

        # Look for bold text on a different page
        if span.get("flags", 0) == BOLD_TEXT_FLAG and span["page_index"] != section_page:
            return (span["page_index"], span["y"])

    return None


def is_section_number_in_margin(span: SpanContent, section_num: str) -> bool:
    """Check if span is a section number in the left margin."""
    if is_standalone_section_number(span, section_num):
        return True
    text = span["text"].strip()
    return is_in_left_margin(span, LEFT_MARGIN_THRESHOLD) and is_section_number(text)


def is_within_page_boundaries(
    span: SpanContent,
    section: SectionMarker,
    next_section: SectionMarker | None,
    bold_boundary: tuple[int, float] | None,
) -> bool:
    """Check if span is within the page boundaries for the section."""
    section_page = section["page_index"]
    section_y = section["y"]
    next_page = next_section["page_index"] if next_section else float("inf")
    next_y = next_section["y"] if next_section else float("inf")

    span_page = span["page_index"]
    span_y = span["y"]

    # On section's page
    if span_page == section_page:
        return span_y >= section_y

    # On next section's page
    if span_page == next_page:
        return span_y < next_y

    # On intermediate pages - check for bold boundary
    if bold_boundary:
        bold_page, bold_y = bold_boundary
        if span_page == bold_page:
            return span_y < bold_y

    # Between sections
    return section_page < span_page < next_page


def is_within_horizontal_boundaries(span: SpanContent, section_x_end: float) -> bool:
    """Check if span is within horizontal content boundaries."""
    # If in left margin, must have meaningful content
    if is_in_left_margin(span, section_x_end + SECTION_X_BUFFER):
        return is_meaningful_content(span)
    return True


def determine_content_boundaries(
    span: SpanContent,
    section: SectionMarker,
    next_section: SectionMarker | None,
    bold_boundary: tuple[int, float] | None,
) -> bool:
    """Determine if a span is within the content boundaries of a section.

    Returns True if the span should be included in the section's content.
    """
    section_x_end = section["x1"]

    # Skip footer
    if is_footer_text(span):
        return False

    # Skip page headers
    if is_page_header_text(span):
        return False

    # Skip section numbers in left margin
    if is_section_number_in_margin(span, section["number"]):
        return False

    # Check vertical boundaries
    if not is_within_page_boundaries(span, section, next_section, bold_boundary):
        return False

    # Check horizontal boundaries
    return is_within_horizontal_boundaries(span, section_x_end)


def extract_text_for_section(
    section: SectionMarker,
    next_section: SectionMarker | None,
    all_content: list[SpanContent],
) -> str:
    """Extract and clean text content for a single section."""
    # Find bold title boundary
    bold_boundary = find_bold_title_after_section(section, next_section, all_content)

    # Collect text spans within boundaries
    text_parts: list[str] = []

    for span in all_content:
        if determine_content_boundaries(span, section, next_section, bold_boundary):
            text = span["text"].strip()
            if text:
                text_parts.append(text)

    # Join and clean the text
    raw_text = "\n".join(text_parts)
    return clean_extracted_text(raw_text)


def clean_extracted_text(text: str) -> str:
    """Clean up extracted text by removing headers and short titles."""
    if not text:
        return ""

    lines = text.split("\n")
    cleaned_lines: list[str] = []

    for line in lines:
        # Skip likely headers
        if is_likely_header_line(line):
            continue
        # Skip short titles
        if is_short_title_line(line):
            continue

        # Clean whitespace but preserve structure
        cleaned = " ".join(line.split())
        if cleaned:
            cleaned_lines.append(cleaned)

    return "\n".join(cleaned_lines)


def track_pages_with_content(
    section: SectionMarker,
    next_section: SectionMarker | None,
    all_content: list[SpanContent],
    bold_boundary: tuple[int, float] | None,
) -> dict[int, str]:
    """Track which pages have content for this section."""
    section_page = section["page_index"]
    next_page = next_section["page_index"] if next_section else float("inf")
    section_y = section["y"]
    next_y = next_section["y"] if next_section else float("inf")
    bold_page = bold_boundary[0] if bold_boundary else -1

    content_pages: dict[int, str] = {}

    for span in all_content:
        span_page = span["page_index"]
        span_y = span["y"]

        # Skip pages outside range
        if span_page < section_page or span_page > next_page:
            continue

        # Skip footer
        if is_footer_text(span):
            continue

        # On section's page, skip content before section
        if span_page == section_page and span_y < section_y:
            continue

        # Skip bold boundary page (belongs to next section)
        if bold_boundary and span_page == bold_page:
            continue

        # Skip if past next section
        if span_page == next_page and span_y >= next_y:
            continue

        if span["text"].strip():
            content_pages[span_page] = span["page"]

    return content_pages


def extract_chunks(pdf_path: Path) -> list[Chunk]:
    """Extract structured chunks from a PDF file.

    Identifies sections by finding section numbers in the left margin,
    then extracts the content between section markers.
    """
    # Phase 1: Collect all spans from PDF
    all_content = collect_all_spans_from_pdf(pdf_path)

    # Phase 2: Identify section markers
    sections = find_section_markers(all_content)

    # Phase 3: Extract text for each section
    results: list[Chunk] = []

    for i, section in enumerate(sections):
        # Find next section to determine content boundaries
        next_section = sections[i + 1] if i + 1 < len(sections) else None

        # Extract text content
        text = extract_text_for_section(section, next_section, all_content)

        # Determine page range
        bold_boundary = find_bold_title_after_section(section, next_section, all_content)
        content_pages = track_pages_with_content(section, next_section, all_content, bold_boundary)

        page_start = section["page"]
        if content_pages:
            last_content_page_index = max(content_pages)
            page_end = content_pages[last_content_page_index]
        else:
            page_end = section["page"]

        results.append(
            Chunk(
                section_path=section["number"],
                page_start=page_start,
                page_end=page_end,
                text=text,
            ),
        )

    return results
