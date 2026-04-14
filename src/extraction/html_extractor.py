"""HTML extractor router for source-specific HTML capture handling."""

from __future__ import annotations

import logging
from time import perf_counter
from typing import TYPE_CHECKING

from bs4 import BeautifulSoup

from src.extraction.html import HtmlSidecar, _build_source_extractor, _elapsed_ms, _fail_validation

if TYPE_CHECKING:
    from pathlib import Path

    from src.models.extraction import ExtractedDocument

logger = logging.getLogger(__name__)


class HtmlExtractor:
    """Route an HTML capture pair to the appropriate source-specific extractor."""

    source_type = "html"
    skip_if_unchanged = True

    def __init__(self, sidecar_path: Path) -> None:
        """Initialize the extractor with the matching JSON sidecar path."""
        self._sidecar_path = sidecar_path

    def extract(self, source_path: Path, explicit_doc_uid: str | None) -> ExtractedDocument:
        """Extract an HTML capture into document metadata, chunks, and sections."""
        if not source_path.exists():
            _fail_validation(f"HTML file not found: {source_path}")
        if not self._sidecar_path.exists():
            _fail_validation(f"HTML sidecar not found: {self._sidecar_path}")

        sidecar_started_at = perf_counter()
        logger.info(f"Loading HTML sidecar from {self._sidecar_path}")
        sidecar = HtmlSidecar.from_path(self._sidecar_path)
        logger.info(f"Loaded HTML sidecar from {self._sidecar_path} in {_elapsed_ms(sidecar_started_at):.2f}ms; source_domain={sidecar.source_domain}, capture_format={sidecar.capture_format}, capture_mode={sidecar.capture_mode}")

        html_read_started_at = perf_counter()
        logger.info(f"Reading HTML source from {source_path}")
        html_text = source_path.read_text(encoding="utf-8")
        logger.info(f"Read HTML source from {source_path} in {_elapsed_ms(html_read_started_at):.2f}ms; html_chars={len(html_text)}")

        parse_started_at = perf_counter()
        logger.info(f"Parsing HTML source from {source_path} with BeautifulSoup(html.parser)")
        soup = BeautifulSoup(html_text, "html.parser")
        logger.info(f"Parsed HTML source from {source_path} in {_elapsed_ms(parse_started_at):.2f}ms")

        extractor = _build_source_extractor(sidecar)
        logger.info(f"Selected HTML source extractor {type(extractor).__name__} for source_domain={sidecar.source_domain}")
        extraction_started_at = perf_counter()
        extracted_document = extractor.extract_from_soup(
            soup=soup,
            sidecar=sidecar,
            explicit_doc_uid=explicit_doc_uid,
        )
        logger.info(
            f"HTML extraction completed for {source_path} in {_elapsed_ms(extraction_started_at):.2f}ms; "
            f"doc_uid={extracted_document.document.doc_uid}, chunk_count={len(extracted_document.chunks)}, "
            f"section_count={len(extracted_document.sections)}"
        )
        return extracted_document
