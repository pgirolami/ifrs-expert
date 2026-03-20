"""Chunk command - extract chunks from a PDF file."""

from pathlib import Path

from src.pdf import extract_chunks


class ChunkCommand:
    """Extract chunks from a PDF file."""

    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

    def execute(self) -> str:
        if not self.pdf_path.exists():
            return f"Error: PDF file not found: {self.pdf_path}"

        try:
            chunks = extract_chunks(self.pdf_path)
            import json
            return json.dumps([{"section_path": c.section_path, "page_start": c.page_start, "page_end": c.page_end, "text": c.text} for c in chunks], indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Error: {e}"
