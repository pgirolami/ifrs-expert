"""Tests for HTML extraction."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from src.extraction.html import HtmlExtractor, HtmlSidecar, HtmlValidationError, _extract_heading_title, _flatten_inline_text, _normalize_navis_heading_title
from src.extraction.ifrs_html_extractor import IAS_VARIANT_LABEL_TO_DOCUMENT_TYPE, IfrsHtmlExtractor
from src.retrieval.document_profile_builder import DocumentProfileBuilder

SECTION_TITLE_EDU_REFERENCE_SUFFIX_PATTERN = re.compile(r"\s+E\d+(?:\s*,\s*E\d+)*$", re.IGNORECASE)


def _normalize_section_title_for_test(title: str) -> str:
    return SECTION_TITLE_EDU_REFERENCE_SUFFIX_PATTERN.sub("", title).strip()


def _example_html_path(slug: str) -> Path:
    examples_dir = Path(__file__).parent.parent.parent / "examples"
    return next(examples_dir.glob(f"*{slug}.html"))


def _example_chunks_path(slug: str) -> Path:
    examples_dir = Path(__file__).parent.parent.parent / "examples"
    return next(examples_dir.glob(f"*{slug}__CHUNKS.json"))


def _example_sections_path(slug: str) -> Path:
    examples_dir = Path(__file__).parent.parent.parent / "examples"
    return next(examples_dir.glob(f"*{slug}__SECTIONS.json"))


def test_ias_variant_labels_map_to_separate_document_types() -> None:
    assert IAS_VARIANT_LABEL_TO_DOCUMENT_TYPE["Basis for Conclusions IASC"] == "IAS-BCIASC"
    assert IAS_VARIANT_LABEL_TO_DOCUMENT_TYPE["Supporting Materials"] == "IAS-SM"


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
            "Basis for Conclusions IASC": "IAS-BCIASC",
            "Supporting Materials": "IAS-SM",
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
            assert _normalize_section_title_for_test(expected["section_name"]) in section.title

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
            assert _normalize_section_title_for_test(expected["section_name"]) in section.title

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

    def test_extract_strips_educational_notes_and_keeps_top_level_sections(self) -> None:
        """IFRS extraction should drop note/edu content and keep top-level sections with children."""
        html = """
            <html>
              <head>
                <title>IFRS 9 Financial Instruments</title>
                <link rel="canonical" href="https://www.ifrs.org/content/ifrs9.html">
                <meta name="DC.Identifier" content="ifrs9">
              </head>
              <body>
                <div class="custom-select-option">
                  <input name="documentType" type="radio" value="/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html" checked>
                  <span class="custom-select-option-checkbox__label">Basis for Conclusions</span>
                </div>
                <section class="ifrs-cmp-htmlviewer__section">
                  <div class="nested1" id="sec-top-level">
                    <h1>Top level heading</h1>
                  </div>
                  <div class="nested2 paragraph topic" id="para-1">
                    <table>
                      <tr>
                        <td class="paragraph_col1"><div class="paranum"><p>1</p></div></td>
                        <td class="paragraph_col2">
                          <div class="body">
                            <div class="note edu"><p>[Refer: paragraphs 4–6, 17 and 18]</p></div>
                          </div>
                        </td>
                      </tr>
                    </table>
                  </div>
                </section>
              </body>
            </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        sidecar = HtmlSidecar(
            url="https://www.ifrs.org/content/ifrs9.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html",
            title="IFRS 9 Financial Instruments - Basis for Conclusions",
            captured_at="2026-04-04T14:23:10Z",
            source_domain="www.ifrs.org",
            canonical_url="https://www.ifrs.org/content/ifrs9.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html",
            extension_version=None,
            content_type=None,
            capture_format=None,
            capture_mode=None,
            product_key=None,
            root_ref_id=None,
            chapter_ref_id=None,
            chapter_title=None,
            document_type="IFRS-BC",
            page_ref_ids=(),
            page_titles=(),
        )

        extracted_document = IfrsHtmlExtractor().extract_from_soup(soup=soup, sidecar=sidecar, explicit_doc_uid=None)

        section_titles = {section.title for section in extracted_document.sections}
        assert "Top level heading" in section_titles
        assert extracted_document.chunks == []
        note_body = BeautifulSoup("<div class='body'><div class='note edu'><p>[Refer: paragraphs 4–6]</p></div></div>", "html.parser").div
        assert note_body is not None
        assert _flatten_inline_text(note_body) == ""

    def test_extract_falls_back_to_section_body_for_objective_without_paragraph_wrapper(self) -> None:
        """IAS objective sections without a paragraph wrapper should still emit a chunk."""
        html = """
            <html>
              <head>
                <title>IFRS - IAS 12 Income Taxes</title>
                <link rel="canonical" href="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ias-12-income-taxes.html">
                <meta name="DC.Identifier" content="ias12">
              </head>
              <body>
                <div class="custom-select-option">
                  <input name="documentType" type="radio" value="/content/dam/ifrs/publications/html-standards/english/2026/issued/ias12.html" checked>
                  <span class="custom-select-option-checkbox__label">Standard</span>
                </div>
                <section class="ifrs-cmp-htmlviewer__section">
                  <div class="topic nested1" id="IAS12_TI0002">
                    <h1>International Accounting Standard 12 Income Taxes</h1>
                  </div>
                  <div class="topic nested2" id="IAS12_0011">
                    <h2>Objective</h2>
                    <div class="show-hide" style="display: none;">
                      <div class="body">
                        <div class="bodydiv">
                          <p>The objective of this Standard is to prescribe the accounting treatment for income taxes.</p>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="topic nested2" id="IAS12_g1-4">
                    <h2>Scope</h2>
                    <div class="show-hide" style="display: none;">
                      <div class="topic paragraph nested3 principles" id="IAS12_1">
                        <table>
                          <tbody>
                            <tr>
                              <td class="paragraph_col1"><div class="paranum"><p>1</p></div></td>
                              <td class="paragraph_col2"><div class="body"><p>This Standard shall be applied in accounting for income taxes.</p></div></td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </section>
              </body>
            </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        sidecar = HtmlSidecar(
            url="https://www.ifrs.org/issued-standards/list-of-standards/ias-12-income-taxes.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ias12.html",
            title="IFRS - IAS 12 Income Taxes",
            captured_at="2026-04-04T14:23:10Z",
            source_domain="www.ifrs.org",
            canonical_url="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ias-12-income-taxes.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ias12.html",
            extension_version=None,
            content_type=None,
            capture_format=None,
            capture_mode=None,
            product_key=None,
            root_ref_id=None,
            chapter_ref_id=None,
            chapter_title=None,
            document_type="IAS-S",
            page_ref_ids=(),
            page_titles=(),
        )

        extracted_document = IfrsHtmlExtractor().extract_from_soup(soup=soup, sidecar=sidecar, explicit_doc_uid=None)

        objective_chunk = next((chunk for chunk in extracted_document.chunks if chunk.containing_section_id == "IAS12_0011"), None)
        scope_chunk = next((chunk for chunk in extracted_document.chunks if chunk.containing_section_id == "IAS12_g1-4"), None)

        assert objective_chunk is not None, "Expected IAS 12 Objective text to be emitted as a chunk"
        assert objective_chunk.text.startswith("The objective of this Standard is to prescribe the accounting treatment for income taxes.")
        assert scope_chunk is not None, "Expected IAS 12 Scope text to continue emitting a chunk"
        assert scope_chunk.text.startswith("This Standard shall be applied in accounting for income taxes.")
        assert extracted_document.document.document_type == "IAS-S"

    def test_extract_strips_educational_references_from_ias_section_titles(self) -> None:
        """IAS section titles should ignore inline educational references like E1/E2."""
        html = """
            <html>
              <head>
                <title>IFRS - IAS 19 Employee Benefits</title>
                <link rel="canonical" href="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ias-19-employee-benefits.html">
                <meta name="DC.Identifier" content="ias19">
              </head>
              <body>
                <div class="custom-select-option">
                  <input name="documentType" type="radio" value="/content/dam/ifrs/publications/html-standards/english/2026/issued/ias19.html" checked>
                  <span class="custom-select-option-checkbox__label">Standard</span>
                </div>
                <section class="ifrs-cmp-htmlviewer__section">
                  <div class="topic nested1" id="IAS19_rubric">
                    <h1>International Accounting Standard 19 Employee Benefits</h1>
                  </div>
                  <div class="topic nested2" id="IAS19_g2-7">
                    <h2 class="title topictitle2 expand_cursor" id="IAS19_g2-7__IAS19_g2-7_TI">Scope<span class="ph"><a href="javascript:;"><span class="fn_eduref" style="">E1,</span></a><a href="javascript:;"><span class="fn_eduref" style="">E2</span></a></span><span class="expand">+</span></h2>
                    <div class="show-hide">
                      <div class="body">
                        <div class="bodydiv">
                          <p>This Standard shall be applied by an employer in accounting for all employee benefits, except those to which IFRS 2 applies.</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </section>
              </body>
            </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        sidecar = HtmlSidecar(
            url="https://www.ifrs.org/issued-standards/list-of-standards/ias-19-employee-benefits.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ias19.html",
            title="IFRS - IAS 19 Employee Benefits",
            captured_at="2026-04-04T14:23:10Z",
            source_domain="www.ifrs.org",
            canonical_url="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ias-19-employee-benefits.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ias19.html",
            extension_version=None,
            content_type=None,
            capture_format=None,
            capture_mode=None,
            product_key=None,
            root_ref_id=None,
            chapter_ref_id=None,
            chapter_title=None,
            document_type="IAS-S",
            page_ref_ids=(),
            page_titles=(),
        )

        extracted_document = IfrsHtmlExtractor().extract_from_soup(soup=soup, sidecar=sidecar, explicit_doc_uid=None)
        built_profile = DocumentProfileBuilder().build(
            document=extracted_document.document,
            chunks=extracted_document.chunks,
            sections=extracted_document.sections,
            section_closure_rows=extracted_document.section_closure_rows,
        )

        scope_section_titles = [section.title for section in extracted_document.sections if section.section_id == "IAS19_g2-7"]
        assert scope_section_titles == ["Scope"], f"Expected the section title to be normalized without the inline references, got {scope_section_titles}"
        assert built_profile.document.scope_text is not None, "Expected IAS 19 scope_text to populate from the scope section body"
        assert built_profile.document.scope_text.startswith("This Standard shall be applied by an employer in accounting for all employee benefits")
        assert "Scope: This Standard shall be applied by an employer" in built_profile.embedding_text

    def test_extract_populates_scope_from_descendant_chunks_under_title_like_root(self) -> None:
        """Basis for Conclusions scope text should include descendant chunks when the scope section has no direct chunks."""
        html = """
            <html>
              <head>
                <title>IAS 2 Inventories - Basis for Conclusions</title>
                <link rel="canonical" href="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ias-2-inventories.html">
                <meta name="DC.Identifier" content="ias2-bc">
              </head>
              <body>
                <div class="custom-select-option">
                  <input name="documentType" type="radio" value="/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html" checked>
                  <span class="custom-select-option-checkbox__label">Basis for Conclusions</span>
                </div>
                <section class="ifrs-cmp-htmlviewer__section">
                  <div class="topic nested1" id="IAS02_rubric">
                    <h1>Basis for Conclusions on IAS 2 Inventories</h1>
                  </div>
                  <div class="topic nested2" id="IAS02_gBC4-BC8">
                    <h2 class="title topictitle2 expand_cursor" id="IAS02_gBC4-BC8__IAS02_gBC4-BC8_TI">Scope<span class="expand">–</span></h2>
                    <div class="show-hide" style="display: block;">
                      <div class="body"></div>
                      <div class="topic nested3" id="IAS02_gBC4-BC5">
                        <h3 class="title topictitle3 indented expand_cursor" id="IAS02_gBC4-BC5__IAS02_gBC4-BC5_TI">Reference to historical cost system<span class="expand">–</span></h3>
                        <div class="show-hide" style="display: block;">
                          <div class="topic paragraph nested4" id="IAS02_BC4">
                            <table>
                              <tbody>
                                <tr>
                                  <td class="paragraph_col1"><div class="paranum"><p>BC4</p></div></td>
                                  <td class="paragraph_col2"><div class="body"><p class="p">Both the objective and the scope of the previous version of IAS 2 referred to the accounting treatment for inventories under the historical cost system.</p></div></td>
                                </tr>
                              </tbody>
                            </table>
                          </div>
                        </div>
                      </div>
                      <div class="topic nested3" id="IAS02_gBC6-BC8">
                        <h3 class="title topictitle3 indented expand_cursor" id="IAS02_gBC6-BC8__IAS02_gBC6-BC8_TI">Inventories of broker-traders<span class="expand">–</span></h3>
                        <div class="show-hide" style="display: block;">
                          <div class="topic paragraph nested4" id="IAS02_BC6">
                            <table>
                              <tbody>
                                <tr>
                                  <td class="paragraph_col1"><div class="paranum"><p>BC6</p></div></td>
                                  <td class="paragraph_col2"><div class="body"><p class="p">The Board decided that the Standard should not apply to the measurement of inventories of broker-traders when measured at fair value less costs to sell.</p></div></td>
                                </tr>
                              </tbody>
                            </table>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </section>
              </body>
            </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        sidecar = HtmlSidecar(
            url="https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html",
            title="IAS 2 Inventories - Basis for Conclusions",
            captured_at="2026-04-04T14:23:10Z",
            source_domain="www.ifrs.org",
            canonical_url="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ias-2-inventories.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html",
            extension_version=None,
            content_type=None,
            capture_format=None,
            capture_mode=None,
            product_key=None,
            root_ref_id=None,
            chapter_ref_id=None,
            chapter_title=None,
            document_type="IAS-BC",
            page_ref_ids=(),
            page_titles=(),
        )

        extracted_document = IfrsHtmlExtractor().extract_from_soup(soup=soup, sidecar=sidecar, explicit_doc_uid=None)
        built_profile = DocumentProfileBuilder().build(
            document=extracted_document.document,
            chunks=extracted_document.chunks,
            sections=extracted_document.sections,
            section_closure_rows=extracted_document.section_closure_rows,
        )

        scope_section_titles = [section.title for section in extracted_document.sections if section.section_id == "IAS02_gBC4-BC8"]
        assert scope_section_titles == ["Scope"], f"Expected the scope title to normalize cleanly, got {scope_section_titles}"
        assert built_profile.document.scope_text is not None, "Expected IAS 2 BC scope_text to populate from descendant chunks"
        assert "historical cost system" in built_profile.document.scope_text
        assert "broker-traders" in built_profile.document.scope_text

    def test_extract_normalizes_educational_note_suffixes_with_different_markup(self) -> None:
        """IAS titles should normalize trailing educational-note suffixes even when markup differs."""
        html = """
            <html>
              <head>
                <title>IFRS - IAS 2 Inventories</title>
                <link rel="canonical" href="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ias-2-inventories.html">
                <meta name="DC.Identifier" content="ias2">
              </head>
              <body>
                <div class="custom-select-option">
                  <input name="documentType" type="radio" value="/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html" checked>
                  <span class="custom-select-option-checkbox__label">Standard</span>
                </div>
                <section class="ifrs-cmp-htmlviewer__section">
                  <div class="topic nested1" id="IAS2_rubric">
                    <h1>International Accounting Standard 2 Inventories</h1>
                  </div>
                  <div class="topic nested2" id="IAS02_g28-33">
                    <h3 class="title topictitle3 indented expand_cursor" id="IAS02_g28-33__IAS02_g28-33_TI">Net realisable value<span class="ph"><a href="javascript:;"><span class="fn_eduref" style="">E8</span></a></span><span class="expand">–</span></h3>
                    <div class="show-hide">
                      <div class="body">
                        <div class="bodydiv">
                          <p>Inventories should be measured at the lower of cost and net realisable value.</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </section>
              </body>
            </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        sidecar = HtmlSidecar(
            url="https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html",
            title="IFRS - IAS 2 Inventories",
            captured_at="2026-04-04T14:23:10Z",
            source_domain="www.ifrs.org",
            canonical_url="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ias-2-inventories.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html",
            extension_version=None,
            content_type=None,
            capture_format=None,
            capture_mode=None,
            product_key=None,
            root_ref_id=None,
            chapter_ref_id=None,
            chapter_title=None,
            document_type="IAS-S",
            page_ref_ids=(),
            page_titles=(),
        )

        extracted_document = IfrsHtmlExtractor().extract_from_soup(soup=soup, sidecar=sidecar, explicit_doc_uid=None)
        section_titles = [section.title for section in extracted_document.sections if section.section_id == "IAS02_g28-33"]
        assert section_titles == ["Net realisable value"], f"Expected the section title to be normalized without the E8 suffix, got {section_titles}"

    def test_extract_registers_board_approvals_as_section_without_id(self) -> None:
        """Board Approvals should be extracted as a section so descendants can be linked to it."""
        html = """
            <html>
              <head>
                <title>IFRS - IAS 28 Investments in Associates and Joint Ventures - Basis for Conclusions</title>
                <link rel="canonical" href="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ias-28-investments-in-associates-and-joint-ventures.html">
                <meta name="DC.Identifier" content="ias28">
              </head>
              <body>
                <div class="custom-select-option">
                  <input name="documentType" type="radio" value="/content/dam/ifrs/publications/html-standards/english/2026/issued/ias28.html" checked>
                  <span class="custom-select-option-checkbox__label">Basis for Conclusions</span>
                </div>
                <section class="ifrs-cmp-htmlviewer__section">
                  <div class="topic nested1" id="IAS28_rubric">
                    <h1>Basis for Conclusions on IAS 28 Investments in Associates and Joint Ventures</h1>
                  </div>
                  <div class="nested2 backmatter">
                    <h2 class="title topictitle2 expand_cursor">Board Approvals<span class="expand">–</span></h2>
                    <div class="show-hide" style="display: block;">
                      <div class="topic nested3" id="IAS28_gDO1-DO3">
                        <h4 class="title topictitle4" id="ariaid-title130"><span class="ph variant">Dissenting opinion on amendment issued in May 2008</span></h4>
                        <div class="show-hide">
                          <div class="body"></div>
                          <div class="topic paragraph nested6 noprinciples" id="IAS28_DO1">
                            <table>
                              <tbody>
                                <tr>
                                  <td class="paragraph_col1"><div class="paranum"><p>DO1</p></div></td>
                                  <td class="paragraph_col2"><div class="body"><p class="p">Mr Yamada voted against one of the amendments to IAS 28.</p></div></td>
                                </tr>
                              </tbody>
                            </table>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </section>
              </body>
            </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        sidecar = HtmlSidecar(
            url="https://www.ifrs.org/issued-standards/list-of-standards/ias-28-investments-in-associates-and-joint-ventures.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ias28.html",
            title="IFRS - IAS 28 Investments in Associates and Joint Ventures - Basis for Conclusions",
            captured_at="2026-04-04T14:23:10Z",
            source_domain="www.ifrs.org",
            canonical_url="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ias-28-investments-in-associates-and-joint-ventures.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ias28.html",
            extension_version=None,
            content_type=None,
            capture_format=None,
            capture_mode=None,
            product_key=None,
            root_ref_id=None,
            chapter_ref_id=None,
            chapter_title=None,
            document_type="IAS-BC",
            page_ref_ids=(),
            page_titles=(),
        )

        extracted_document = IfrsHtmlExtractor().extract_from_soup(soup=soup, sidecar=sidecar, explicit_doc_uid=None)

        board_approvals_sections = [section for section in extracted_document.sections if section.title == "Board Approvals"]
        dissent_sections = [section for section in extracted_document.sections if "Dissent" in section.title]
        dissent_chunk_ids = [chunk.chunk_id for chunk in extracted_document.chunks if chunk.chunk_number == "DO1"]

        assert board_approvals_sections, "Expected Board Approvals to be extracted as a section"
        assert dissent_sections, "Expected dissent subsection(s) to remain linked under Board Approvals"
        assert dissent_chunk_ids == ["IAS28_DO1"], f"Expected the dissent chunk to be preserved, got {dissent_chunk_ids}"
        assert dissent_sections[0].parent_section_id == board_approvals_sections[0].section_id

    def test_extract_registers_appendices_as_section_without_id(self) -> None:
        """Appendices should be extracted as a real section so appendix content is not parented to Transition."""
        html = """
            <html>
              <head>
                <title>IFRIC 16 Hedges of a Net Investment in a Foreign Operation</title>
                <link rel="canonical" href="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html">
                <meta name="DC.Identifier" content="ifric16">
              </head>
              <body>
                <div class="custom-select-option">
                  <input name="documentType" type="radio" value="/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16.html" checked>
                  <span class="custom-select-option-checkbox__label">Standard</span>
                </div>
                <section class="ifrs-cmp-htmlviewer__section">
                  <div class="topic nested1" id="IFRIC16_rubric">
                    <h1>IFRIC Interpretation 16 Hedges of a Net Investment in a Foreign Operation</h1>
                  </div>
                  <div class="topic nested2" id="IFRIC16_g18-19">
                    <h2 class="title topictitle2">Transition</h2>
                    <div class="show-hide" style="display: block;">
                      <div class="body"></div>
                    </div>
                  </div>
                  <div class="nested2 appendices">
                    <h2 class="title topictitle2 expand_cursor">Appendices<span class="expand">–</span></h2>
                    <div class="show-hide" style="display: block;">
                      <div class="topic nested3" aria-labelledby="IFRIC16_APP__IFRIC16_APP_TI" id="IFRIC16_APP">
                        <h3 class="title topictitle3 expand_cursor" id="IFRIC16_APP__IFRIC16_APP_TI">Appendix<span class="ph linebreak"></span>Application guidance<span class="expand">–</span></h3>
                        <div class="show-hide" style="display: block;">
                          <div class="topic paragraph nested4" id="IFRIC16_AG1">
                            <table><tbody><tr><td class="paragraph_col1"><div class="paranum"><p>AG1</p></div></td><td class="paragraph_col2"><div class="body"><p class="p">Example appendix content.</p></div></td></tr></tbody></table>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </section>
              </body>
            </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        sidecar = HtmlSidecar(
            url="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16.html",
            title="IFRIC 16 Hedges of a Net Investment in a Foreign Operation",
            captured_at="2026-04-04T14:23:10Z",
            source_domain="www.ifrs.org",
            canonical_url="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifric16.html",
            extension_version=None,
            content_type=None,
            capture_format=None,
            capture_mode=None,
            product_key=None,
            root_ref_id=None,
            chapter_ref_id=None,
            chapter_title=None,
            document_type="IFRIC",
            page_ref_ids=(),
            page_titles=(),
        )

        extracted_document = IfrsHtmlExtractor().extract_from_soup(soup=soup, sidecar=sidecar, explicit_doc_uid=None)
        appendix_sections = [section for section in extracted_document.sections if section.title == "Appendices"]
        appendix_heading_sections = [section for section in extracted_document.sections if section.title == "Appendix Application guidance"]
        appendix_chunks = [chunk for chunk in extracted_document.chunks if chunk.chunk_id == "IFRIC16_AG1"]

        assert appendix_sections, "Expected Appendices to be extracted as a section"
        assert appendix_heading_sections, "Expected appendix guidance to be extracted"
        assert appendix_chunks, "Expected appendix content to be extracted"
        assert appendix_heading_sections[0].parent_section_id == appendix_sections[0].section_id
        assert appendix_chunks[0].containing_section_id == appendix_heading_sections[0].section_id

    def test_extract_preserves_years_in_heading_titles(self) -> None:
        """Heading titles like 2003 revision should keep the year instead of stripping it."""
        html = """
            <html>
              <head>
                <title>IFRS - IAS 27 Consolidated and Separate Financial Statements - Basis for Conclusions</title>
                <link rel="canonical" href="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ias-27-consolidated-and-separate-financial-statements.html">
                <meta name="DC.Identifier" content="ias27">
              </head>
              <body>
                <div class="custom-select-option">
                  <input name="documentType" type="radio" value="/content/dam/ifrs/publications/html-standards/english/2026/issued/ias27.html" checked>
                  <span class="custom-select-option-checkbox__label">Basis for Conclusions</span>
                </div>
                <section class="ifrs-cmp-htmlviewer__section">
                  <div class="topic nested1" id="IAS27_rubric">
                    <h1>Basis for Conclusions on IAS 27 Consolidated and Separate Financial Statements</h1>
                  </div>
                  <div class="topic nested2" id="IAS27_gBC9-BC10">
                    <h3 class="title topictitle3 indented expand_cursor" id="IAS27_gBC9-BC10__IAS27_gBC9-BC10_TI">2003 revision<span class="expand">+</span></h3>
                    <div class="show-hide">
                      <div class="topic paragraph nested4" id="IAS27_BC9">
                        <table>
                          <tbody>
                            <tr>
                              <td class="paragraph_col1"><div class="paranum"><p>BC9</p></div></td>
                              <td class="paragraph_col2"><div class="body"><p class="p">The Board made revisions in 2003 to clarify the accounting requirements.</p></div></td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </section>
              </body>
            </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        sidecar = HtmlSidecar(
            url="https://www.ifrs.org/issued-standards/list-of-standards/ias-27-consolidated-and-separate-financial-statements.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ias27.html",
            title="IFRS - IAS 27 Consolidated and Separate Financial Statements - Basis for Conclusions",
            captured_at="2026-04-04T14:23:10Z",
            source_domain="www.ifrs.org",
            canonical_url="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ias-27-consolidated-and-separate-financial-statements.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ias27.html",
            extension_version=None,
            content_type=None,
            capture_format=None,
            capture_mode=None,
            product_key=None,
            root_ref_id=None,
            chapter_ref_id=None,
            chapter_title=None,
            document_type="IAS-BC",
            page_ref_ids=(),
            page_titles=(),
        )

        extracted_document = IfrsHtmlExtractor().extract_from_soup(soup=soup, sidecar=sidecar, explicit_doc_uid=None)
        section_titles = [section.title for section in extracted_document.sections if section.section_id == "IAS27_gBC9-BC10"]
        assert section_titles == ["2003 revision"], f"Expected the year to be preserved in the title, got {section_titles}"

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

    def test_extract_heading_title_strips_inline_footnote_markers(self) -> None:
        """Heading titles should drop inline footnote references such as fn_ref markers."""
        heading = BeautifulSoup(
            '<h2 class="title topictitle2 expand_cursor" id="IAS33_ex6__IAS33_ex6_TI">'
            'Example&nbsp;6 Convertible bonds'
            '<span class="ph"><a href="javascript:;">'
            '<span class="fn_ref" title="This example does not illustrate the classification of the components of convertible financial instruments as liabilities and equity or the classification of related interest and dividends as expenses and equity as required by&nbsp;IAS&nbsp;32.">1</span>'
            '</a></span>'
            '<span class="expand">+</span>'
            '</h2>',
            "html.parser",
        ).h2
        assert heading is not None
        assert _extract_heading_title(heading) == "Example 6 Convertible bonds"

    def test_extract_heading_title_preserves_appendix_subtitles(self) -> None:
        """Appendix headings should keep their subtitles instead of collapsing to a generic label."""
        heading = BeautifulSoup(
            '<h3 class="title topictitle3 expand_cursor" id="IAS36_APPA__IAS36_APPA_TI">'
            'Appendix&nbsp;A<span class="ph linebreak"></span>Using present value techniques to measure value in use'
            '<span class="expand">+</span>'
            '</h3>',
            "html.parser",
        ).h3
        assert heading is not None
        assert _extract_heading_title(heading) == "Appendix A Using present value techniques to measure value in use"

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
