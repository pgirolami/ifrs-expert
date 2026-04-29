"""Tests for IFRS extraction of `Refer:` annotations."""

from __future__ import annotations

from bs4 import BeautifulSoup

from src.extraction.html import HtmlSidecar
from src.extraction.ifrs_html_extractor import IfrsHtmlExtractor


def test_ifrs_extraction_attaches_references_to_chunks_and_sections() -> None:
    """IFRS extraction should capture top-of-section and chunk-level `Refer:` annotations."""
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
              <span class="custom-select-option-checkbox__label">Standard</span>
            </div>
            <section class="ifrs-cmp-htmlviewer__section">
              <div class="topic nested1" id="IFRS09_0054">
                <h1>Recognition and derecognition</h1>
              </div>
              <div class="note edu" id="IFRS09_0054__IFRS09_E0001">
                <span class="edu_prefix">Refer:</span>
                <p>
                  <a class="xref" href="javascript:;">paragraphs BC4.1-BC4.45</a>,
                  <a class="xref" href="javascript:;">BC4.124-BC4.208</a>
                </p>
              </div>
              <div class="topic paragraph nested2 principles" id="IFRS09_4.1.1__IFRS09_P0001">
                <table>
                  <tbody>
                    <tr>
                      <td class="paragraph_col1"><div class="paranum"><p>4.1.1</p></div></td>
                      <td class="paragraph_col2">
                        <div class="body">
                          <p>This paragraph has an inline note <span class="note edu"><span class="edu_prefix">Refer:</span><a class="xref" href="javascript:;">paragraph 4.1.1(a)</a></span>.</p>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </section>
          </body>
        </html>
    """
    soup = BeautifulSoup(html, "html.parser")
    sidecar = HtmlSidecar(
        url="https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html",
        title="IFRS 9 Financial Instruments",
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
        document_type="IFRS-S",
        page_ref_ids=(),
        page_titles=(),
    )

    extracted_document = IfrsHtmlExtractor().extract_from_soup(soup=soup, sidecar=sidecar, explicit_doc_uid=None)

    assert extracted_document.chunks, "Expected a paragraph chunk to be extracted"
    assert extracted_document.references, "Expected parsed references to be extracted"

    references = extracted_document.references
    assert [reference.reference_order for reference in references] == [1, 2, 3]
    assert [reference.source_location_type for reference in references] == ["section", "section", "chunk"]
    assert references[0].source_section_id == "IFRS09_0054"
    assert references[1].source_section_id == "IFRS09_0054"
    assert references[2].source_chunk_id == "IFRS09_4.1.1__IFRS09_P0001"
    assert references[2].source_section_id == "IFRS09_0054"
    assert [reference.target_raw_text for reference in references] == [
        "paragraphs BC4.1-BC4.45",
        "BC4.124-BC4.208",
        "paragraph 4.1.1(a)",
    ]
    assert [reference.target_start for reference in references] == ["BC4.1", "BC4.124", "4.1.1"]
    assert [reference.target_kind for reference in references] == [
        "basis_for_conclusions",
        "basis_for_conclusions",
        "same_standard_paragraph",
    ]
    paragraph_chunk = next(chunk for chunk in extracted_document.chunks if chunk.chunk_id == "IFRS09_4.1.1__IFRS09_P0001")
    assert "Refer:" not in paragraph_chunk.text
