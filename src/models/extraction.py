"""Extraction result models."""

from __future__ import annotations

from dataclasses import dataclass

from src.models.chunk import Chunk
from src.models.document import DocumentRecord


@dataclass
class ExtractedDocument:
    """Structured extraction result returned by a source extractor."""

    document: DocumentRecord
    chunks: list[Chunk]
