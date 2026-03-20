#!/usr/bin/env python3
"""
PDF Extraction Approach #2: PyMuPDF (fitz) - Simplified Version
Uses PyMuPDF's layout analysis to extract section numbers and their corresponding text blocks.
"""

import json
import re
import fitz  # PyMuPDF
from typing import List, Dict


def extract_sections_from_pdf(pdf_path: str) -> List[Dict]:
    """
    Extract section numbers and their corresponding text blocks from PDF.

    Strategy:
    1. Use PyMuPDF's get_text("dict") to get blocks with coordinates
    2. Identify section numbers (short digit blocks on left margin)
    3. Extract text blocks that follow each section number
    """
    all_sections = []

    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):
        page = doc[page_num]
        page_number = page_num + 1  # 1-indexed

        # Get text with layout information
        text_dict = page.get_text("dict")

        sections_on_page = extract_sections_from_page(text_dict, page_number)
        all_sections.extend(sections_on_page)

    doc.close()

    return all_sections


def extract_sections_from_page(text_dict: dict, page_number: int) -> List[Dict]:
    """Extract sections from a single page's text dict."""

    # First pass: find all spans and their positions
    blocks = text_dict.get("blocks", [])

    # Find potential section number spans and all content spans
    section_spans = []  # (y, x0, x1, text)

    for block in blocks:
        if block.get("type") == 0:  # Text block
            bbox = block.get("bbox", [0, 0, 0, 0])

            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    span_text = span.get("text", "").strip()
                    span_bbox = span.get("bbox", [0, 0, 0, 0])
                    x0, y0 = span_bbox[0], span_bbox[1]

                    if x0 < 150 and span_text.isdigit() and len(span_text) <= 3:
                        # This is a potential section number
                        section_spans.append({"number": span_text, "y": y0, "x1": span_bbox[2]})

    # Sort by y position
    section_spans.sort(key=lambda s: s["y"])

    # Now extract text for each section using a different approach
    # Get full page text and find section boundaries
    results = []

    for i, section in enumerate(section_spans):
        section_num = section["number"]
        section_x = section["x1"]
        section_y = section["y"]

        # Skip page numbers (at bottom of page, y > 700)
        if section_y > 700:
            continue

        # Find the next section's y position
        if i + 1 < len(section_spans):
            next_y = section_spans[i + 1]["y"]
        else:
            next_y = float("inf")

        # Extract text from blocks in the vertical range
        section_text_lines = []

        for block in blocks:
            if block.get("type") == 0:
                bbox = block.get("bbox", [0, 0, 0, 0])
                block_y = bbox[1]
                block_x = bbox[0]

                # Skip blocks that are in the left margin (section numbers)
                if block_x < section_x + 20:
                    continue

                # Check if block is in the vertical range
                if section_y <= block_y < next_y:
                    # Extract text from lines
                    block_text = ""
                    for line in block.get("lines", []):
                        for span in line.get("spans", []):
                            block_text += span.get("text", "")
                        block_text += " "  # Add space between lines

                    if block_text.strip():
                        # Clean up the text
                        block_text = " ".join(block_text.split())
                        section_text_lines.append(block_text)

        # Join lines with newlines
        text = "\n".join(section_text_lines)

        # Filter out section titles and headers
        lines = text.split("\n")
        filtered_lines = []
        for line in lines:
            # Skip header text (all caps, short)
            if line.isupper() and len(line) < 30:
                continue
            # Skip section titles
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
    output_path = "output_pymupdf.json"

    print("Extracting sections using PyMuPDF...")
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
