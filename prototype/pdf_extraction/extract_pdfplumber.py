#!/usr/bin/env python3
"""
PDF Extraction Approach #1: pdfplumber
Uses coordinate-based extraction to identify section numbers and their corresponding text blocks.
"""

import json
import pdfplumber
from typing import List, Dict, Tuple


def extract_sections_from_pdf(pdf_path: str) -> List[Dict]:
    """
    Extract section numbers and their corresponding text blocks from PDF.

    Strategy:
    1. Find all potential section numbers (digits at left margin)
    2. For each section number, find the text to its right
    3. Continue until the next section number appears
    """
    all_sections = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            page_number = page_num + 1  # 1-indexed
            sections_on_page = extract_sections_from_page(page, page_number)
            all_sections.extend(sections_on_page)

    return all_sections


def extract_sections_from_page(page, page_number: int) -> List[Dict]:
    """Extract sections from a single page."""
    chars = page.chars

    # Find all potential section numbers (digits) on the left margin
    # Section numbers typically appear at x < 150 and are short (1-3 digits)
    section_candidates = []

    for c in chars:
        if c["text"].isdigit():
            x0 = c["x0"]
            # Only consider digits on the left side (likely section numbers)
            if x0 < 150:
                y = round(c["top"])
                # Check if this digit is part of an existing section candidate
                existing = None
                for sec in section_candidates:
                    if abs(sec["y"] - y) < 5:  # Same line
                        existing = sec
                        break

                if existing:
                    existing["chars"].append(c)
                else:
                    section_candidates.append({"y": y, "chars": [c]})

    # Convert chars to section numbers and sort by y position
    sections = []
    for sec in section_candidates:
        sec["chars"].sort(key=lambda c: c["x0"])
        text = "".join([c["text"] for c in sec["chars"]])
        # Filter out non-section numbers (too long, or page numbers at bottom)
        if len(text) <= 3:
            sections.append(
                {"y": sec["y"], "number": text, "x1": max([c["x1"] for c in sec["chars"]])}
            )

    sections.sort(key=lambda s: s["y"])

    # Now extract text for each section
    results = []
    for i, section in enumerate(sections):
        section_num = section["number"]
        section_x = section["x1"]  # Right edge of section number
        section_y = section["y"]

        # Skip page numbers (at bottom of page, y > 700)
        if section_y > 700:
            continue

        # Find the next section's y position (or end of page)
        if i + 1 < len(sections):
            next_y = sections[i + 1]["y"]
        else:
            next_y = 10000  # End of page

        # Extract text in the region to the right of section number
        # and between this section and the next
        section_text_chars = []

        for c in chars:
            # Must be to the right of section number (with small margin)
            if c["x0"] > section_x + 10:
                # Must be in the vertical range between this section and next
                if c["top"] >= section_y and c["top"] < next_y:
                    section_text_chars.append(c)

        # Sort by position (top to bottom, left to right)
        section_text_chars.sort(key=lambda c: (c["top"], c["x0"]))

        # Group by similar y to reconstruct lines
        lines = []
        current_line = []
        current_y = None

        for c in section_text_chars:
            if current_y is None:
                current_y = c["top"]
                current_line.append(c)
            elif abs(c["top"] - current_y) < 5:
                # Same line
                current_line.append(c)
            else:
                # New line - save current and start new
                if current_line:
                    current_line.sort(key=lambda c: c["x0"])
                    lines.append("".join([c["text"] for c in current_line]))
                current_line = [c]
                current_y = c["top"]

        # Don't forget the last line
        if current_line:
            current_line.sort(key=lambda c: c["x0"])
            lines.append("".join([c["text"] for c in current_line]))

        # Join lines with newlines
        text = "\n".join(lines)

        # Filter out header text (APRIL 2024 at top) and section titles
        lines = text.split("\n")
        filtered_lines = []
        for line in lines:
            # Skip header text (all caps, short)
            if line.isupper() and len(line) < 30:
                continue
            # Skip section titles (contain specific patterns)
            if "Identification" in line and len(line) < 60:
                continue
            if line.strip():
                filtered_lines.append(line)

        text = "\n".join(filtered_lines)

        results.append(
            {
                "section_path": section_num,
                "page_start": str(page_number),
                "page_end": str(page_number),
                "text": text,
            }
        )

    return results


def main():
    pdf_path = "../../../examples/iasb ifrs example.pdf"
    output_path = "output_pdfplumber.json"

    print("Extracting sections using pdfplumber...")
    sections = extract_sections_from_pdf(pdf_path)

    # Save output
    with open(output_path, "w") as f:
        json.dump(sections, f, indent=2)

    print(f"Extracted {len(sections)} sections")
    print(f"Output saved to {output_path}")

    # Print first few sections
    for s in sections[:5]:
        print(f"\nSection {s['section_path']} (page {s['page_start']}):")
        print(f"  {s['text'][:100]}...")


if __name__ == "__main__":
    main()
