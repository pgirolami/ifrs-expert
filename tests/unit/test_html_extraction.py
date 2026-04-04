"""Tests for HTML extraction."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from src.extraction.html import HtmlExtractor, HtmlValidationError


def _example_html_path(slug: str) -> Path:
    examples_dir = Path(__file__).parent.parent.parent / "examples"
    return next(examples_dir.glob(f"*{slug}.html"))


def _example_chunks_path(slug: str) -> Path:
    examples_dir = Path(__file__).parent.parent.parent / "examples"
    return next(examples_dir.glob(f"*{slug}__CHUNKS.json"))


def _write_sidecar(sidecar_path: Path, canonical_url: str, title: str) -> None:
    sidecar_path.write_text(
        json.dumps(
            {
                "url": canonical_url,
                "title": title,
                "captured_at": "2026-04-04T14:23:10Z",
                "source_domain": "www.ifrs.org",
                "canonical_url": canonical_url,
                "extension_version": "0.1.0",
                "content_type": "text/html",
            }
        ),
        encoding="utf-8",
    )


class TestHtmlExtractor:
    """Tests for HTML extraction from IFRS captures."""

    @pytest.mark.parametrize(
        ("slug", "expected_doc_uid", "expected_anchor"),
        [
            ("ifrs9", "ifrs9", "IFRS09_2.4"),
            ("ifric16", "ifric16", "IFRIC16_1"),
        ],
    )
    def test_extract_returns_document_metadata_and_expected_chunks(
        self,
        slug: str,
        expected_doc_uid: str,
        expected_anchor: str,
        tmp_path: Path,
    ) -> None:
        """Representative IFRS HTML files should parse into stable paragraph chunks."""
        html_path = _example_html_path(slug)
        expected_chunks = json.loads(_example_chunks_path(slug).read_text(encoding="utf-8"))
        sidecar_path = tmp_path / f"{slug}.json"
        html_text = html_path.read_text(encoding="utf-8")
        canonical_prefix = "<link rel=\"canonical\"\n    href=\""
        start = html_text.index(canonical_prefix) + len(canonical_prefix)
        end = html_text.index("\">", start)
        html_canonical_url = html_text[start:end]
        _write_sidecar(sidecar_path=sidecar_path, canonical_url=html_canonical_url, title=f"Title for {slug}")

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        extracted_document = extractor.extract(source_path=html_path, explicit_doc_uid=None)

        assert extracted_document.document.doc_uid == expected_doc_uid
        assert extracted_document.document.source_type == "html"
        assert extracted_document.document.canonical_url == html_canonical_url
        assert extracted_document.chunks, "Expected at least one extracted HTML chunk"

        chunks_by_section = {chunk.section_path: chunk for chunk in extracted_document.chunks}
        for expected in expected_chunks:
            chunk = chunks_by_section.get(expected["section_path"])
            assert chunk is not None, f"Missing chunk for section {expected['section_path']}"
            assert _normalize(chunk.text) == _normalize(expected["text"])

        matching_chunk = chunks_by_section[expected_chunks[0]["section_path"]]
        assert matching_chunk.source_anchor == expected_anchor

    def test_extract_rejects_mismatched_canonical_urls(self, tmp_path: Path) -> None:
        """The sidecar canonical URL must match the saved HTML canonical URL."""
        html_path = _example_html_path("ifrs9")
        sidecar_path = tmp_path / "ifrs9.json"
        _write_sidecar(
            sidecar_path=sidecar_path,
            canonical_url="https://www.ifrs.org/content/does-not-match.html",
            title="IFRS 9",
        )

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        with pytest.raises(HtmlValidationError, match="canonical URL"):
            extractor.extract(source_path=html_path, explicit_doc_uid=None)

    def test_extract_requires_dc_identifier(self, tmp_path: Path) -> None:
        """HTML ingestion should fail fast when the stable identifier is missing."""
        html_path = tmp_path / "missing-identifier.html"
        html_path.write_text(
            """
            <html>
              <head>
                <link rel="canonical" href="https://www.ifrs.org/content/missing-id.html">
              </head>
              <body>
                <section class="ifrs-cmp-htmlviewer__section"></section>
              </body>
            </html>
            """,
            encoding="utf-8",
        )
        sidecar_path = tmp_path / "missing-identifier.json"
        _write_sidecar(
            sidecar_path=sidecar_path,
            canonical_url="https://www.ifrs.org/content/missing-id.html",
            title="Missing identifier",
        )

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        with pytest.raises(HtmlValidationError, match="DC.Identifier"):
            extractor.extract(source_path=html_path, explicit_doc_uid=None)


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
