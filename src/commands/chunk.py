"""Chunk command - extract chunks from an HTML capture file."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

from src.extraction import HtmlExtractor


class ChunkCommand:
    """Extract chunks from an HTML capture file."""

    def __init__(self, html_path: Path) -> None:
        """Initialize the chunk command."""
        self.html_path = html_path

    def execute(self) -> str:
        """Extract and return chunks from an HTML source as JSON."""
        if not self.html_path.exists():
            return f"Error: HTML file not found: {self.html_path}"

        try:
            extractor = HtmlExtractor(sidecar_path=self.html_path.with_suffix(".json"))
            extracted_document = extractor.extract(self.html_path, None)
            return json.dumps(
                [
                    {
                        "chunk_number": chunk.chunk_number,
                        "chunk_id": chunk.chunk_id,
                        "page_start": chunk.page_start,
                        "page_end": chunk.page_end,
                        "text": chunk.text,
                    }
                    for chunk in extracted_document.chunks
                ],
                indent=2,
                ensure_ascii=False,
            )
        except (OSError, ValueError) as error:
            return f"Error: {error}"
