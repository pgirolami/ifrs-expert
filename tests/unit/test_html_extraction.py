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


def _example_sections_path(slug: str) -> Path:
    examples_dir = Path(__file__).parent.parent.parent / "examples"
    return next(examples_dir.glob(f"*{slug}__SECTIONS.json"))


def _write_sidecar(sidecar_path: Path, canonical_url: str, title: str, source_domain: str = "www.ifrs.org") -> None:
    sidecar_path.write_text(
        json.dumps(
            {
                "url": canonical_url,
                "title": title,
                "captured_at": "2026-04-04T14:23:10Z",
                "source_domain": source_domain,
                "canonical_url": canonical_url,
                "extension_version": "0.1.0",
                "content_type": "text/html",
            }
        ),
        encoding="utf-8",
    )


def _naxis_example_base(name: str) -> Path:
    return Path(__file__).parent.parent.parent / "examples" / "Lefebvre-Naxis" / name


class TestHtmlExtractor:
    """Tests for HTML extraction from IFRS captures."""

    @pytest.mark.parametrize(
        ("slug", "expected_doc_uid", "expected_chunk_id"),
        [
            ("ifrs9", "ifrs9", "IFRS09_2.4"),
            ("ifric16", "ifric16", "IFRIC16_1"),
        ],
    )
    def test_extract_returns_document_metadata_expected_chunks_and_sections(
        self,
        slug: str,
        expected_doc_uid: str,
        expected_chunk_id: str,
        tmp_path: Path,
    ) -> None:
        """Representative IFRS HTML files should parse into stable chunks and sections."""
        html_path = _example_html_path(slug)
        expected_chunks = json.loads(_example_chunks_path(slug).read_text(encoding="utf-8"))
        expected_sections = json.loads(_example_sections_path(slug).read_text(encoding="utf-8"))
        sidecar_path = tmp_path / f"{slug}.json"
        html_text = html_path.read_text(encoding="utf-8")
        canonical_prefix = '<link rel="canonical"\n    href="'
        start = html_text.index(canonical_prefix) + len(canonical_prefix)
        end = html_text.index('">', start)
        html_canonical_url = html_text[start:end]
        _write_sidecar(sidecar_path=sidecar_path, canonical_url=html_canonical_url, title=f"Title for {slug}")

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        extracted_document = extractor.extract(source_path=html_path, explicit_doc_uid=None)

        assert extracted_document.document.doc_uid == expected_doc_uid
        assert extracted_document.document.source_type == "html"
        assert extracted_document.document.canonical_url == html_canonical_url
        assert extracted_document.chunks, "Expected at least one extracted HTML chunk"
        assert extracted_document.sections, "Expected at least one extracted HTML section"
        assert extracted_document.section_closure_rows, "Expected ancestor/descendant section rows"

        chunks_by_number = {chunk.chunk_number: chunk for chunk in extracted_document.chunks}
        for expected in expected_chunks:
            chunk = chunks_by_number.get(expected["section_path"])
            assert chunk is not None, f"Missing chunk for number {expected['section_path']}"
            assert _normalize(chunk.text) == _normalize(expected["text"])
            assert chunk.containing_section_id == expected["section_id"]

        matching_chunk = chunks_by_number[expected_chunks[0]["section_path"]]
        assert matching_chunk.chunk_id == expected_chunk_id

        sections_by_id = {section.section_id: section for section in extracted_document.sections}
        for expected in expected_sections:
            section = sections_by_id.get(expected["section_id"])
            assert section is not None, f"Missing section {expected['section_id']}"
            assert expected["section_name"] in section.title
            assert section.embedding_text == section.title
            assert section.parent_section_id == expected.get("section_parent_id")

    def test_extract_builds_recursive_section_closure_rows(self, tmp_path: Path) -> None:
        """Section closure rows should include recursive descendants for subtree expansion."""
        html_path = _example_html_path("ifrs9")
        sidecar_path = tmp_path / "ifrs9.json"
        html_text = html_path.read_text(encoding="utf-8")
        canonical_prefix = '<link rel="canonical"\n    href="'
        start = html_text.index(canonical_prefix) + len(canonical_prefix)
        end = html_text.index('">', start)
        html_canonical_url = html_text[start:end]
        _write_sidecar(sidecar_path=sidecar_path, canonical_url=html_canonical_url, title="IFRS 9")

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        extracted_document = extractor.extract(source_path=html_path, explicit_doc_uid=None)

        closure_pairs = {(row.ancestor_section_id, row.descendant_section_id, row.depth) for row in extracted_document.section_closure_rows}

        assert ("IFRS09_0054", "IFRS09_0054", 0) in closure_pairs
        assert ("IFRS09_0054", "IFRS09_g3.1.1-3.1.2", 1) in closure_pairs
        assert ("IFRS09_g3.1.1-3.1.2", "IFRS09_g3.1.1-3.1.2", 0) in closure_pairs

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

    @pytest.mark.parametrize(
        ("basename", "expected_doc_uid", "expected_section_id", "expected_parent_section_id"),
        [
            (
                "20260412T190013Z--document",
                "naxis-qrifrs-n2d7d9d1995f171f-efl",
                "N2D7D9D1995F171F-EFL",
                "S2B0D9D1995F171F-EFL",
            ),
            (
                "20260412T190029Z--document",
                "naxis-qrifrs-c2a8e6f292f99e-efl",
                "C2A8E6F292F99E-EFL",
                "T1A42F43DD29C5-EFL",
            ),
        ],
    )
    def test_extract_returns_expected_naxis_chunks_and_sections(
        self,
        basename: str,
        expected_doc_uid: str,
        expected_section_id: str,
        expected_parent_section_id: str,
    ) -> None:
        """Representative Naxis HTML files should parse into stable chunks and TOC-backed sections."""
        base_path = _naxis_example_base(basename)
        html_path = base_path.with_suffix(".html")
        sidecar_path = base_path.with_suffix(".json")
        expected_chunks = json.loads(base_path.with_name(f"{basename}__CHUNKS.json").read_text(encoding="utf-8"))

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        extracted_document = extractor.extract(source_path=html_path, explicit_doc_uid=None)

        assert extracted_document.document.doc_uid == expected_doc_uid
        assert extracted_document.document.document_type == "NAXIS"
        assert extracted_document.document.source_domain == "abonnes.efl.fr"
        assert extracted_document.sections, "Expected Naxis section extraction to produce section rows"
        assert extracted_document.section_closure_rows, "Expected Naxis section extraction to produce closure rows"

        sections_by_id = {section.section_id: section for section in extracted_document.sections}
        assert expected_section_id in sections_by_id
        assert sections_by_id[expected_section_id].parent_section_id == expected_parent_section_id

        chunks_by_number = {chunk.chunk_number: chunk for chunk in extracted_document.chunks}
        for expected in expected_chunks:
            chunk = chunks_by_number.get(expected["section_path"])
            assert chunk is not None, f"Missing Naxis chunk for number {expected['section_path']}"
            assert _normalize(chunk.text) == _normalize(expected["text"])
            assert chunk.chunk_id == expected["section_id"]

    def test_extract_uses_ref_id_from_toc_links_for_naxis_section_identity(self) -> None:
        """Naxis section ids should come from the TOC refId, not the DOM anchor id."""
        base_path = _naxis_example_base("20260412T190029Z--document")
        extractor = HtmlExtractor(sidecar_path=base_path.with_suffix(".json"))

        extracted_document = extractor.extract(source_path=base_path.with_suffix(".html"), explicit_doc_uid=None)

        sections_by_id = {section.section_id: section for section in extracted_document.sections}
        assert "C2A8E6F292F99E-EFL" in sections_by_id
        assert "A004-000" not in sections_by_id

    def test_extract_rejects_naxis_sidecars_with_mismatched_ref_ids(self, tmp_path: Path) -> None:
        """Naxis sidecar url and canonical_url must point to the same refId."""
        base_path = _naxis_example_base("20260412T190029Z--document")
        html_path = base_path.with_suffix(".html")
        sidecar_path = tmp_path / "broken-naxis.json"
        sidecar_path.write_text(
            json.dumps(
                {
                    "url": "https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&uaId=000K&refId=C2A8E6F292F99E-EFL",
                    "title": "Mémento IFRS 2026",
                    "captured_at": "2026-04-12T19:00:29Z",
                    "source_domain": "abonnes.efl.fr",
                    "canonical_url": "https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&uaId=000K&refId=DIFFERENT-EFL",
                    "extension_version": "0.1.0",
                    "content_type": "text/html",
                }
            ),
            encoding="utf-8",
        )

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        with pytest.raises(HtmlValidationError, match="same refId"):
            extractor.extract(source_path=html_path, explicit_doc_uid=None)


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
