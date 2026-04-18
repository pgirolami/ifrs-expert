"""Tests for HTML extraction."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from src.extraction.html import HtmlExtractor, HtmlValidationError, _normalize_navis_heading_title


def _example_html_path(slug: str) -> Path:
    examples_dir = Path(__file__).parent.parent.parent / "examples"
    return next(examples_dir.glob(f"*{slug}.html"))


def _example_chunks_path(slug: str) -> Path:
    examples_dir = Path(__file__).parent.parent.parent / "examples"
    return next(examples_dir.glob(f"*{slug}__CHUNKS.json"))


def _example_sections_path(slug: str) -> Path:
    examples_dir = Path(__file__).parent.parent.parent / "examples"
    return next(examples_dir.glob(f"*{slug}__SECTIONS.json"))


def _write_sidecar(
    sidecar_path: Path,
    canonical_url: str,
    title: str,
    source_domain: str = "www.ifrs.org",
    document_type: str | None = None,
    url: str | None = None,
) -> None:
    payload: dict[str, str] = {
        "url": url or canonical_url,
        "title": title,
        "captured_at": "2026-04-04T14:23:10Z",
        "source_domain": source_domain,
        "canonical_url": canonical_url,
        "extension_version": "0.1.0",
        "content_type": "text/html",
    }
    if document_type is not None:
        payload["document_type"] = document_type
    sidecar_path.write_text(json.dumps(payload), encoding="utf-8")


def _extract_ifrs_variant_metadata(html_path: Path) -> dict[str, str]:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    canonical_tag = soup.select_one('link[rel="canonical"]')
    identifier_tag = soup.select_one('meta[name="DC.Identifier"]')
    checked_input = soup.select_one('input[name="documentType"][checked]')
    if canonical_tag is None or identifier_tag is None or checked_input is None:
        raise AssertionError(f"Expected IFRS fixture metadata in {html_path}")

    shell_canonical_url = str(canonical_tag.get("href", "")).strip()
    variant_value = str(checked_input.get("value", "")).strip()
    variant_label_node = checked_input.find_next_sibling("span")
    variant_label = variant_label_node.get_text(" ", strip=True) if variant_label_node is not None else "Standard"
    doc_uid = str(identifier_tag.get("content", "")).strip()
    shell_title = soup.title.get_text(" ", strip=True) if soup.title is not None else doc_uid

    if variant_label == "Standard":
        normalized_title = shell_title
    else:
        normalized_title = f"{shell_title} - {variant_label}"

    if doc_uid.startswith("ifrs"):
        document_type = {
            "Standard": "IFRS-S",
            "Basis for Conclusions": "IFRS-BC",
            "Illustrative Examples": "IFRS-IE",
            "Implementation Guidance": "IFRS-IG",
        }[variant_label]
    elif doc_uid.startswith("ias"):
        document_type = {
            "Standard": "IAS-S",
            "Basis for Conclusions": "IAS-BC",
            "Illustrative Examples": "IAS-IE",
            "Implementation Guidance": "IAS-IG",
        }[variant_label]
    elif doc_uid.startswith("ifric"):
        document_type = {
            "Standard": "IFRIC",
            "Basis for Conclusions": "IFRIC-BC",
            "Illustrative Examples": "IFRIC-IE",
            "Implementation Guidance": "IFRIC-IG",
        }[variant_label]
    elif doc_uid.startswith("sic"):
        document_type = "SIC"
    else:
        document_type = "PS"

    return {
        "doc_uid": doc_uid,
        "document_type": document_type,
        "title": normalized_title,
        "canonical_url": f"{shell_canonical_url}{variant_value}",
        "url": f"https://www.ifrs.org/issued-standards/list-of-standards/{html_path.stem}.html{variant_value.removesuffix('.html')}/",
    }


def _write_ifrs_sidecar(sidecar_path: Path, html_path: Path) -> dict[str, str]:
    sidecar_payload = _extract_ifrs_variant_metadata(html_path)
    _write_sidecar(
        sidecar_path=sidecar_path,
        canonical_url=sidecar_payload["canonical_url"],
        title=sidecar_payload["title"],
        document_type=sidecar_payload["document_type"],
        url=sidecar_payload["url"],
    )
    return sidecar_payload


def _ifrs_fixture_base(name: str) -> Path:
    return Path(__file__).parent.parent.parent / "examples" / "IFRS" / name


def _navis_example_base(name: str) -> Path:
    base_path = Path(__file__).parent.parent.parent / "examples" / "Lefebvre-Navis" / name
    if not base_path.with_suffix(".html").exists() or not base_path.with_suffix(".json").exists():
        pytest.skip("Navis fixtures are not available in this worktree")
    return base_path


class TestHtmlExtractor:
    """Tests for HTML extraction from IFRS captures."""

    @pytest.mark.parametrize(
        ("slug", "expected_doc_uid", "expected_chunk_id", "expected_document_type"),
        [
            ("ifrs9", "ifrs9", "IFRS09_2.4", "IFRS-S"),
            ("ifric16", "ifric16", "IFRIC16_1", "IFRIC"),
        ],
    )
    def test_extract_returns_document_metadata_expected_chunks_and_sections(
        self,
        slug: str,
        expected_doc_uid: str,
        expected_chunk_id: str,
        expected_document_type: str,
        tmp_path: Path,
    ) -> None:
        """Representative IFRS HTML files should parse into stable chunks and sections."""
        html_path = _example_html_path(slug)
        expected_chunks = json.loads(_example_chunks_path(slug).read_text(encoding="utf-8"))
        expected_sections = json.loads(_example_sections_path(slug).read_text(encoding="utf-8"))
        sidecar_path = tmp_path / f"{slug}.json"
        sidecar_payload = _write_ifrs_sidecar(sidecar_path=sidecar_path, html_path=html_path)

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        extracted_document = extractor.extract(source_path=html_path, explicit_doc_uid=None)

        assert extracted_document.document.doc_uid == expected_doc_uid
        assert extracted_document.document.source_type == "html"
        assert extracted_document.document.canonical_url == sidecar_payload["canonical_url"]
        assert extracted_document.document.document_type == expected_document_type
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
            assert section.parent_section_id == expected.get("section_parent_id")

    @pytest.mark.parametrize(
        ("basename", "expected_doc_uid", "expected_document_type"),
        [
            ("20260414T094554Z--ifrs-9-financial-instruments", "ifrs9", "IFRS-S"),
            ("20260414T094602Z--ifrs-9-financial-instruments", "ifrs9-ig", "IFRS-IG"),
            ("20260414T094610Z--ifrs-9-financial-instruments", "ifrs9-ie", "IFRS-IE"),
            ("20260414T094615Z--ifrs-9-financial-instruments", "ifrs9-bc", "IFRS-BC"),
        ],
    )
    def test_extract_returns_expected_ifrs_variant_metadata(
        self,
        basename: str,
        expected_doc_uid: str,
        expected_document_type: str,
    ) -> None:
        """IFRS fixture captures should preserve distinct variant metadata and representative chunks."""
        base_path = _ifrs_fixture_base(basename)
        html_path = base_path.with_suffix(".html")
        sidecar_path = base_path.with_suffix(".json")
        expected_sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
        expected_chunks = json.loads(base_path.with_name(f"{basename}__CHUNKS.json").read_text(encoding="utf-8"))
        expected_sections = json.loads(base_path.with_name(f"{basename}__SECTIONS.json").read_text(encoding="utf-8"))

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        extracted_document = extractor.extract(source_path=html_path, explicit_doc_uid=None)

        assert extracted_document.document.doc_uid == expected_doc_uid
        assert extracted_document.document.document_type == expected_document_type
        assert extracted_document.document.source_title == expected_sidecar["title"]
        assert extracted_document.document.canonical_url == expected_sidecar["canonical_url"]
        assert extracted_document.document.source_url == expected_sidecar["url"]

        chunks_by_number = {chunk.chunk_number: chunk for chunk in extracted_document.chunks}
        for expected in expected_chunks:
            chunk = chunks_by_number.get(expected["section_path"])
            assert chunk is not None, f"Missing chunk for number {expected['section_path']}"
            assert _normalize(chunk.text) == _normalize(expected["text"])
            assert chunk.containing_section_id == expected["section_id"]

        matching_chunk = chunks_by_number[expected_chunks[0]["section_path"]]
        assert matching_chunk.chunk_id, "Expected representative chunk to preserve a stable chunk_id"

        sections_by_id = {section.section_id: section for section in extracted_document.sections}
        for expected in expected_sections:
            section = sections_by_id.get(expected["section_id"])
            assert section is not None, f"Missing section {expected['section_id']}"
            assert expected["section_name"] in section.title
            assert section.parent_section_id == expected.get("section_parent_id")

    @pytest.mark.parametrize(
        ("relative_html_path", "expected_doc_uid", "expected_document_type"),
        [
            (
                "www.ifrs.org__issued-standards__list-of-standards__ifrs-9-financial-instruments.html__content__dam__ifrs__publications__html-standards__english__2026__issued__ifrs9.html",
                "ifrs9",
                "IFRS-S",
            ),
            (
                "www.ifrs.org__issued-standards__list-of-standards__ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html__content__dam__ifrs__publications__html-standards__english__2026__issued__ifric16.html",
                "ifric16",
                "IFRIC",
            ),
        ],
    )
    def test_demo_fixture_sidecars_remain_ingestable(
        self,
        relative_html_path: str,
        expected_doc_uid: str,
        expected_document_type: str,
    ) -> None:
        """Demo HTML fixtures should keep sidecars aligned with the saved HTML metadata."""
        examples_dir = Path(__file__).parent.parent.parent / "examples"
        html_path = examples_dir / relative_html_path
        sidecar_path = html_path.with_suffix(".json")

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        extracted_document = extractor.extract(source_path=html_path, explicit_doc_uid=None)

        assert extracted_document.document.doc_uid == expected_doc_uid
        assert extracted_document.document.document_type == expected_document_type

    def test_extract_builds_recursive_section_closure_rows(self, tmp_path: Path) -> None:
        """Section closure rows should include recursive descendants for subtree expansion."""
        html_path = _example_html_path("ifrs9")
        sidecar_path = tmp_path / "ifrs9.json"
        _write_ifrs_sidecar(sidecar_path=sidecar_path, html_path=html_path)

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
        sidecar_payload = _write_ifrs_sidecar(sidecar_path=sidecar_path, html_path=html_path)
        _write_sidecar(
            sidecar_path=sidecar_path,
            canonical_url="https://www.ifrs.org/content/does-not-match.html",
            title=sidecar_payload["title"],
            document_type=sidecar_payload["document_type"],
            url=sidecar_payload["url"],
        )

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        with pytest.raises(HtmlValidationError, match="canonical URL"):
            extractor.extract(source_path=html_path, explicit_doc_uid=None)

    def test_extract_rejects_mismatched_document_types(self, tmp_path: Path) -> None:
        """The sidecar document_type must match the resolved IFRS variant."""
        html_path = _example_html_path("ifrs9")
        sidecar_path = tmp_path / "ifrs9.json"
        sidecar_payload = _write_ifrs_sidecar(sidecar_path=sidecar_path, html_path=html_path)
        _write_sidecar(
            sidecar_path=sidecar_path,
            canonical_url=sidecar_payload["canonical_url"],
            title=sidecar_payload["title"],
            document_type="IFRS-BC",
            url=sidecar_payload["url"],
        )

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        with pytest.raises(HtmlValidationError, match="document_type"):
            extractor.extract(source_path=html_path, explicit_doc_uid=None)

    def test_extract_requires_dc_identifier(self, tmp_path: Path) -> None:
        """HTML ingestion should fail fast when the stable identifier is missing."""
        html_path = tmp_path / "missing-identifier.html"
        html_path.write_text(
            """
            <html>
              <head>
                <title>IFRS - Missing identifier</title>
                <link rel="canonical" href="https://www.ifrs.org/content/missing-id.html">
              </head>
              <body>
                <div class="custom-select-option">
                  <input name="documentType" type="radio" value="/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html" checked>
                  <span class="custom-select-option-checkbox__label">Standard</span>
                </div>
                <section class="ifrs-cmp-htmlviewer__section"></section>
              </body>
            </html>
            """,
            encoding="utf-8",
        )
        sidecar_path = tmp_path / "missing-identifier.json"
        _write_sidecar(
            sidecar_path=sidecar_path,
            canonical_url=("https://www.ifrs.org/content/missing-id.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html"),
            title="IFRS - Missing identifier",
            document_type="IFRS-S",
            url="https://www.ifrs.org/content/missing-id.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/",
        )

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        with pytest.raises(HtmlValidationError, match="DC.Identifier"):
            extractor.extract(source_path=html_path, explicit_doc_uid=None)

    @pytest.mark.parametrize(
        ("basename", "expected_doc_uid", "expected_section_id", "expected_parent_section_id"),
        [
            (
                "20260412T190013Z--document",
                "navis-QRIFRS-N2D7D9D1995F171F-EFL",
                "N2D7D9D1995F171F-EFL",
                "S2B0D9D1995F171F-EFL",
            ),
            (
                "20260412T190029Z--document",
                "navis-QRIFRS-C2A8E6F292F99E-EFL",
                "C2A8E6F292F99E-EFL",
                "T1A42F43DD29C5-EFL",
            ),
        ],
    )
    def test_extract_returns_expected_navis_chunks_and_sections(
        self,
        basename: str,
        expected_doc_uid: str,
        expected_section_id: str,
        expected_parent_section_id: str,
    ) -> None:
        """Representative Navis HTML files should parse into stable chunks and TOC-backed sections."""
        base_path = _navis_example_base(basename)
        html_path = base_path.with_suffix(".html")
        sidecar_path = base_path.with_suffix(".json")
        expected_chunks = json.loads(base_path.with_name(f"{basename}__CHUNKS.json").read_text(encoding="utf-8"))

        extractor = HtmlExtractor(sidecar_path=sidecar_path)

        extracted_document = extractor.extract(source_path=html_path, explicit_doc_uid=None)

        assert extracted_document.document.doc_uid == expected_doc_uid
        assert extracted_document.document.document_type == "NAVIS"
        assert extracted_document.document.source_domain == "abonnes.efl.fr"
        assert extracted_document.sections, "Expected Navis section extraction to produce section rows"
        assert extracted_document.section_closure_rows, "Expected Navis section extraction to produce closure rows"

        sections_by_id = {section.section_id: section for section in extracted_document.sections}
        assert expected_section_id in sections_by_id
        assert sections_by_id[expected_section_id].parent_section_id == expected_parent_section_id

        chunks_by_number = {chunk.chunk_number: chunk for chunk in extracted_document.chunks}
        for expected in expected_chunks:
            chunk = chunks_by_number.get(expected["section_path"])
            assert chunk is not None, f"Missing Navis chunk for number {expected['section_path']}"
            assert _normalize(chunk.text) == _normalize(expected["text"])
            assert chunk.chunk_id == expected["section_id"]

    def test_extract_uses_ref_id_from_toc_links_for_navis_section_identity(self) -> None:
        """Navis section ids should come from the TOC refId, not the DOM anchor id."""
        base_path = _navis_example_base("20260412T190029Z--document")
        extractor = HtmlExtractor(sidecar_path=base_path.with_suffix(".json"))

        extracted_document = extractor.extract(source_path=base_path.with_suffix(".html"), explicit_doc_uid=None)

        sections_by_id = {section.section_id: section for section in extracted_document.sections}
        assert "C2A8E6F292F99E-EFL" in sections_by_id
        assert "A004-000" not in sections_by_id

    def test_extract_returns_expected_navis_chapter_bundle_chunks_and_sections(self, tmp_path: Path) -> None:
        """Synthetic Navis chapter bundles should ingest as one chapter-level document."""
        base_path = _navis_example_base("20260412T190029Z--document")
        soup = BeautifulSoup(base_path.with_suffix(".html").read_text(encoding="utf-8"), "html.parser")
        content_root = soup.select_one("#documentContent .question.question-export")
        assert content_root is not None, "Expected the Navis example to contain the content root"

        bundle_html_path = tmp_path / "navis-chapter-bundle.html"
        bundle_sidecar_path = tmp_path / "navis-chapter-bundle.json"
        manifest_payload = {
            "chapter_ref_id": "C2A8E6F292F99E-EFL",
            "chapter_title": "CHAPITRE 4 Cadre conceptuel de l'information financière (Cadre conceptuel de l'IASB)",
            "product_key": "QRIFRS",
            "page_ref_ids": ["P8A8E6F292F99E-EFL"],
            "page_titles": ["Généralités"],
        }
        manifest_json = json.dumps(manifest_payload)
        bundle_html_path.write_text(
            """
            <!DOCTYPE html>
            <html>
              <head>
                <meta charset="utf-8">
                <title>CHAPITRE 4 Cadre conceptuel de l'information financière (Cadre conceptuel de l'IASB)</title>
              </head>
              <body>
                <script id="ifrs-expert-navis-manifest" type="application/json">"""
            + manifest_json
            + """</script>
                <div id="ifrs-expert-navis-bundle" data-chapter-ref-id="C2A8E6F292F99E-EFL">
                  <section class="ifrs-expert-navis-page" data-page-ref-id="P8A8E6F292F99E-EFL" data-page-title="Généralités">
                    """
            + str(content_root)
            + """
                  </section>
                </div>
              </body>
            </html>
            """,
            encoding="utf-8",
        )
        bundle_sidecar_path.write_text(
            json.dumps(
                {
                    "url": "https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&uaId=000K&refId=C2A8E6F292F99E-EFL",
                    "title": "CHAPITRE 4 Cadre conceptuel de l'information financière (Cadre conceptuel de l'IASB)",
                    "captured_at": "2026-04-12T19:00:29Z",
                    "source_domain": "abonnes.efl.fr",
                    "canonical_url": "https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&uaId=000K&refId=C2A8E6F292F99E-EFL",
                    "extension_version": "0.1.0",
                    "content_type": "text/html",
                    "capture_format": "navis-chapter-bundle/v1",
                    "capture_mode": "chapter",
                    "product_key": "QRIFRS",
                    "root_ref_id": "N24F9F491387ED-EFL",
                    "chapter_ref_id": "C2A8E6F292F99E-EFL",
                    "chapter_title": "CHAPITRE 4 Cadre conceptuel de l'information financière (Cadre conceptuel de l'IASB)",
                    "page_ref_ids": ["P8A8E6F292F99E-EFL"],
                    "page_titles": ["Généralités"],
                }
            ),
            encoding="utf-8",
        )

        extractor = HtmlExtractor(sidecar_path=bundle_sidecar_path)
        extracted_document = extractor.extract(source_path=bundle_html_path, explicit_doc_uid=None)

        assert extracted_document.document.doc_uid == "navis-QRIFRS-C2A8E6F292F99E-EFL"
        sections_by_id = {section.section_id: section for section in extracted_document.sections}
        assert sections_by_id["C2A8E6F292F99E-EFL"].parent_section_id is None
        assert any(chunk.chunk_number == "12501" for chunk in extracted_document.chunks)
        assert any(chunk.chunk_id == "P8A8E6F292F99E-EFL" for chunk in extracted_document.chunks)

    def test_extract_deduplicates_navis_context_headings_without_repeated_anchor_ids(self, tmp_path: Path) -> None:
        """Navis bundle context headings should preserve hierarchy via data attributes without duplicating raw anchor ids."""
        bundle_html_path = tmp_path / "navis-context-bundle.html"
        bundle_sidecar_path = tmp_path / "navis-context-bundle.json"
        manifest_payload = {
            "chapter_ref_id": "C-TEST-EFL",
            "chapter_title": "CHAPITRE TEST",
            "product_key": "QRIFRS",
            "page_ref_ids": ["N-LEAF-1-EFL", "N-LEAF-2-EFL"],
            "page_titles": ["Leaf One", "Leaf Two"],
        }
        manifest_json = json.dumps(manifest_payload)
        bundle_html_path.write_text(
            """
            <!DOCTYPE html>
            <html>
              <head>
                <meta charset="utf-8">
                <title>CHAPITRE TEST</title>
              </head>
              <body>
                <script id="ifrs-expert-navis-manifest" type="application/json">"""
            + manifest_json
            + """</script>
                <div id="ifrs-expert-navis-bundle" data-chapter-ref-id="C-TEST-EFL">
                  <section class="ifrs-expert-navis-page" data-page-ref-id="N-LEAF-1-EFL" data-page-title="Leaf One">
                    <div class="question question-export">
                      <a data-ifrs-expert-context-ref-id="N-ANCESTOR-EFL" data-ifrs-expert-context-only="true"></a>
                      <div class="qw-level qw-level-4"><div class="qw-level-wrapper"><div class="qw-level-title">A. Généralités</div></div></div>
                      <a id="N-LEAF-1-EFL"></a>
                      <div class="qw-level qw-level-7"><div class="qw-level-wrapper"><div class="qw-level-title">Leaf One</div></div></div>
                      <a id="P-LEAF-1-EFL"></a>
                      <div class="qw-par qw-par-p"><div class="qw-p-no"><span class="qw-art">10001</span></div><div class="qw-p-body"><span class="BASEXAlinea">Premier texte.</span></div></div>
                    </div>
                  </section>
                  <section class="ifrs-expert-navis-page" data-page-ref-id="N-LEAF-2-EFL" data-page-title="Leaf Two">
                    <div class="question question-export">
                      <a data-ifrs-expert-context-ref-id="N-ANCESTOR-EFL" data-ifrs-expert-context-only="true"></a>
                      <div class="qw-level qw-level-4"><div class="qw-level-wrapper"><div class="qw-level-title">A. Généralités</div></div></div>
                      <a id="N-LEAF-2-EFL"></a>
                      <div class="qw-level qw-level-7"><div class="qw-level-wrapper"><div class="qw-level-title">Leaf Two</div></div></div>
                      <a id="P-LEAF-2-EFL"></a>
                      <div class="qw-par qw-par-p"><div class="qw-p-no"><span class="qw-art">10002</span></div><div class="qw-p-body"><span class="BASEXAlinea">Deuxième texte.</span></div></div>
                    </div>
                  </section>
                </div>
              </body>
            </html>
            """,
            encoding="utf-8",
        )
        bundle_sidecar_path.write_text(
            json.dumps(
                {
                    "url": "https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&uaId=000K&refId=C-TEST-EFL",
                    "title": "CHAPITRE TEST",
                    "captured_at": "2026-04-12T19:00:29Z",
                    "source_domain": "abonnes.efl.fr",
                    "canonical_url": "https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&uaId=000K&refId=C-TEST-EFL",
                    "extension_version": "0.1.0",
                    "content_type": "text/html",
                    "capture_format": "navis-chapter-bundle/v1",
                    "capture_mode": "chapter",
                    "product_key": "QRIFRS",
                    "root_ref_id": "N24F9F491387ED-EFL",
                    "chapter_ref_id": "C-TEST-EFL",
                    "chapter_title": "CHAPITRE TEST",
                    "page_ref_ids": ["N-LEAF-1-EFL", "N-LEAF-2-EFL"],
                    "page_titles": ["Leaf One", "Leaf Two"],
                }
            ),
            encoding="utf-8",
        )

        extractor = HtmlExtractor(sidecar_path=bundle_sidecar_path)
        extracted_document = extractor.extract(source_path=bundle_html_path, explicit_doc_uid=None)

        sections_by_id = {section.section_id: section for section in extracted_document.sections}
        assert len(extracted_document.sections) == 4
        assert sections_by_id["N-ANCESTOR-EFL"].title == "Généralités"
        assert sections_by_id["N-LEAF-1-EFL"].parent_section_id == "N-ANCESTOR-EFL"
        assert sections_by_id["N-LEAF-2-EFL"].parent_section_id == "N-ANCESTOR-EFL"
        assert [chunk.chunk_id for chunk in extracted_document.chunks] == ["P-LEAF-1-EFL", "P-LEAF-2-EFL"]

    @pytest.mark.parametrize(
        ("raw_title", "expected_title"),
        [
            ("1. Généralités", "Généralités"),
            ("A. Généralités", "Généralités"),
            ("II. Généralités", "Généralités"),
            ("i. Généralités", "Généralités"),
            ("CHAPITRE 4 Cadre conceptuel", "Cadre conceptuel"),
            ("Sans numérotation", "Sans numérotation"),
        ],
    )
    def test_normalize_navis_heading_title_strips_supported_leading_list_markers(
        self,
        raw_title: str,
        expected_title: str,
    ) -> None:
        """Navis heading normalization should strip leading list markers from section titles."""
        assert _normalize_navis_heading_title(raw_title) == expected_title

    def test_extract_rejects_navis_sidecars_with_mismatched_ref_ids(self, tmp_path: Path) -> None:
        """Navis sidecar url and canonical_url must point to the same refId."""
        base_path = _navis_example_base("20260412T190029Z--document")
        html_path = base_path.with_suffix(".html")
        sidecar_path = tmp_path / "broken-navis.json"
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
