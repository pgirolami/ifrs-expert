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
              <div class="topic paragraph nested2 principles" id="IFRS09_4.1.5__IFRS09_P0234">
                <table>
                  <tbody>
                    <tr>
                      <td class="paragraph_col1"><div class="paranum"><p>4.1.5</p></div></td>
                      <td class="paragraph_col2">
                        <div class="body">
                          <p>Despite <a class="xref" href="javascript:;">paragraphs 4.1.1-4.1.4</a>, an entity may, at initial recognition, irrevocably designate a financial asset as measured at fair value through profit or loss if doing so eliminates or significantly reduces a measurement or recognition inconsistency (sometimes referred to as an 'accounting mismatch') that would otherwise arise from measuring assets or liabilities or recognising the gains and losses on them on different bases (see <a class="xref" href="javascript:;">paragraphs B4.1.29- B4.1.32</a>).</p>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="topic paragraph nested2 principles" id="IFRS09_4.2.1__IFRS09_P0236">
                <table>
                  <tbody>
                    <tr>
                      <td class="paragraph_col1"><div class="paranum"><p>4.2.1</p></div></td>
                      <td class="paragraph_col2">
                        <div class="body">
                          <p>An entity shall classify all financial liabilities as subsequently measured at <span class="definition" title="The amount at which the financial asset or financial liability is measured at initial recognition minus principal repayments, plus or minus the cumulative amortisation using the effective interest method of any difference between that initial amount and the maturity amount and, for financial assets adjusted for any loss allowance."><a class="xrefdef" href="javascript:;">amortised cost</a></span>,<span class="note edu" style="display: block;"> [<span class="edu_prefix">Refer:</span><a class="xref" href="javascript:;">paragraphs 5.3.1 and 5.3.2</a>]</span> except for: <a class="xref" href="javascript:;">3.2.15</a>, <a class="xref" href="javascript:;">3.2.17</a>, <a class="xref" href="javascript:;">Section 5.5</a>, <a class="xref" href="javascript:;">5.5.1</a>, and <a class="xref" href="javascript:;">IFRS 15</a>.</p>
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
    assert [reference.reference_order for reference in references] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert [reference.source_location_type for reference in references] == [
        "section",
        "section",
        "chunk",
        "chunk",
        "chunk",
        "chunk",
        "chunk",
        "chunk",
        "chunk",
        "chunk",
        "chunk",
    ]
    assert references[0].source_section_id == "IFRS09_0054"
    assert references[1].source_section_id == "IFRS09_0054"
    assert references[2].source_chunk_id == "IFRS09_4.1.5__IFRS09_P0234"
    assert references[2].source_section_id == "IFRS09_0054"
    assert references[4].source_chunk_id == "IFRS09_4.2.1__IFRS09_P0236"
    assert references[4].source_section_id == "IFRS09_0054"
    assert [reference.target_raw_text for reference in references] == [
        "paragraphs BC4.1-BC4.45",
        "BC4.124-BC4.208",
        "paragraphs 4.1.1-4.1.4",
        "paragraphs B4.1.29- B4.1.32",
        "paragraphs 5.3.1 and 5.3.2",
        "paragraphs 5.3.1 and 5.3.2",
        "3.2.15",
        "3.2.17",
        "Section 5.5",
        "5.5.1",
        "IFRS 15",
    ]
    assert [reference.target_start for reference in references] == [
        "BC4.1",
        "BC4.124",
        "4.1.1",
        "B4.1.29",
        "5.3.1",
        "5.3.2",
        "3.2.15",
        "3.2.17",
        "5.5",
        "5.5.1",
        None,
    ]
    assert [reference.target_kind for reference in references] == [
        "basis_for_conclusions",
        "basis_for_conclusions",
        "same_standard_paragraph",
        "same_standard_paragraph",
        "same_standard_paragraph",
        "same_standard_paragraph",
        "same_standard_paragraph",
        "same_standard_paragraph",
        "same_standard_paragraph",
        "same_standard_paragraph",
        "cross_document",
    ]
    assert references[-1].target_doc_hint == "IFRS 15"
    paragraph_chunk = next(chunk for chunk in extracted_document.chunks if chunk.chunk_id == "IFRS09_4.1.5__IFRS09_P0234")
    assert "Refer:" not in paragraph_chunk.text


def test_ifrs_extraction_deduplicates_inline_note_references() -> None:
    """The same inline note should only be stored once even if the DOM walk sees it twice."""
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
              <div class="topic paragraph nested2 principles" id="IFRS09_4.2.1__IFRS09_P0236">
                <table>
                  <tbody>
                    <tr>
                      <td class="paragraph_col1"><div class="paranum"><p>4.2.1</p></div></td>
                      <td class="paragraph_col2">
                        <div class="body">
                          <p>Paragraph text <span class="note edu"><span class="edu_prefix">Refer:</span><a class="xref" href="javascript:;">paragraph 5.3.1</a></span>.</p>
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

    assert [reference.target_start for reference in extracted_document.references] == ["5.3.1"]
