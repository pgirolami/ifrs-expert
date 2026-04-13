"""HTML extraction for IFRS Expert."""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from datetime import datetime
from time import perf_counter
from typing import TYPE_CHECKING, Final, NoReturn
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup
from bs4.element import PageElement, Tag

from src.models.chunk import Chunk
from src.models.document import DocumentRecord, derive_document_type_from_doc_uid
from src.models.extraction import ExtractedDocument
from src.models.section import SectionClosureRow, SectionRecord

if TYPE_CHECKING:
    from pathlib import Path

INLINE_TEXT_TAGS: Final[set[str]] = {"a", "em", "i", "p", "span", "strong", "sup", "sub"}
REQUIRED_SIDECAR_FIELDS: Final[tuple[str, ...]] = (
    "url",
    "title",
    "captured_at",
    "source_domain",
    "canonical_url",
)
TABLE_ROW_WITH_LABEL_CELL_COUNT: Final[int] = 2
HEADING_TAG_NAMES: Final[tuple[str, ...]] = ("h1", "h2", "h3", "h4", "h5", "h6")
HEADING_PREFIX_PATTERN: Final[re.Pattern[str]] = re.compile(r"^(?:Chapter\s+[A-Za-z0-9.]+|[A-Z]?\d+(?:\.\d+)*)\s+")
SUBSECTION_PREFIX_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z]?\d+\.\d+")
NAVIS_DOC_UID_TOKEN_PATTERN: Final[re.Pattern[str]] = re.compile(r"[^A-Za-z0-9-]+")
NAVIS_TITLE_PREFIX_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^(?:TITRE\s+[A-Z0-9IVXLCM]+|CHAPITRE\s+[A-Z0-9IVXLCM]+|SECTION\s+[A-Z0-9IVXLCM]+)\s+",
    re.IGNORECASE,
)
NAVIS_EDITORIAL_TITLES: Final[set[str]] = {"QUESTIONS/REPONSES PRATIQUES"}
NAVIS_CHAPTER_BUNDLE_CAPTURE_FORMAT: Final[str] = "navis-chapter-bundle/v1"

logger = logging.getLogger(__name__)


class HtmlValidationError(ValueError):
    """Raised when an HTML capture pair fails validation."""


@dataclass
class _SectionTraversalState:
    """Mutable traversal state while extracting IFRS sections from HTML."""

    active_sections_by_level: dict[int, SectionRecord]
    chapter_sections_by_prefix: dict[str, SectionRecord]
    position: int = 0


@dataclass(frozen=True)
class HtmlSidecar:
    """Validated HTML sidecar metadata."""

    url: str
    title: str
    captured_at: str
    source_domain: str
    canonical_url: str
    extension_version: str | None
    content_type: str | None
    capture_format: str | None
    capture_mode: str | None
    product_key: str | None
    root_ref_id: str | None
    chapter_ref_id: str | None
    chapter_title: str | None
    page_ref_ids: tuple[str, ...]
    page_titles: tuple[str, ...]

    @classmethod
    def from_path(cls, sidecar_path: Path) -> HtmlSidecar:
        """Load and validate an HTML sidecar file."""
        try:
            payload = json.loads(sidecar_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            _fail_validation("invalid sidecar JSON", cause=error)

        for field_name in REQUIRED_SIDECAR_FIELDS:
            value = payload.get(field_name)
            if not isinstance(value, str) or not value.strip():
                _fail_validation(f"missing required sidecar field: {field_name}")

        _validate_http_url(payload["url"], field_name="url")
        _validate_http_url(payload["canonical_url"], field_name="canonical_url")

        try:
            datetime.fromisoformat(payload["captured_at"])
        except ValueError as error:
            _fail_validation("captured_at must be an ISO-8601 timestamp", cause=error)

        source_domain = payload["source_domain"].strip().lower()
        if not source_domain:
            _fail_validation("source_domain must be non-empty")

        return cls(
            url=payload["url"],
            title=payload["title"],
            captured_at=payload["captured_at"],
            source_domain=source_domain,
            canonical_url=payload["canonical_url"],
            extension_version=_optional_string(payload.get("extension_version")),
            content_type=_optional_string(payload.get("content_type")),
            capture_format=_optional_string(payload.get("capture_format")),
            capture_mode=_optional_string(payload.get("capture_mode")),
            product_key=_optional_string(payload.get("product_key")),
            root_ref_id=_optional_string(payload.get("root_ref_id")),
            chapter_ref_id=_optional_string(payload.get("chapter_ref_id")),
            chapter_title=_optional_string(payload.get("chapter_title")),
            page_ref_ids=_optional_string_tuple(payload.get("page_ref_ids")),
            page_titles=_optional_string_tuple(payload.get("page_titles")),
        )


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


class IfrsHtmlExtractor:
    """Extractor implementation for IFRS HTML capture pairs."""

    source_type = "html"
    skip_if_unchanged = True

    def extract_from_soup(
        self,
        soup: BeautifulSoup,
        sidecar: HtmlSidecar,
        explicit_doc_uid: str | None,
    ) -> ExtractedDocument:
        """Extract an IFRS HTML capture from a parsed soup and sidecar."""
        del explicit_doc_uid

        canonical_url = self._extract_canonical_url(soup)
        if canonical_url != sidecar.canonical_url:
            _fail_validation("HTML canonical URL does not match sidecar canonical URL")

        identifier_tag = soup.select_one('meta[name="DC.Identifier"]')
        if not isinstance(identifier_tag, Tag):
            _fail_validation('HTML is missing meta[name="DC.Identifier"]')
        doc_uid = _tag_attribute_as_string(identifier_tag, "content")
        if not doc_uid:
            _fail_validation("HTML DC.Identifier must be non-empty")

        content_root = soup.select_one("section.ifrs-cmp-htmlviewer__section")
        if not isinstance(content_root, Tag):
            _fail_validation("HTML is missing the IFRS content root")

        chunks, sections = self._extract_structure(doc_uid=doc_uid, content_root=content_root)
        section_closure_rows = _build_section_closure_rows(sections)

        return ExtractedDocument(
            document=DocumentRecord(
                doc_uid=doc_uid,
                source_type=self.source_type,
                source_title=sidecar.title,
                source_url=sidecar.url,
                canonical_url=sidecar.canonical_url,
                captured_at=sidecar.captured_at,
                source_domain=sidecar.source_domain,
                document_type=derive_document_type_from_doc_uid(doc_uid),
            ),
            chunks=chunks,
            sections=sections,
            section_closure_rows=section_closure_rows,
        )

    def _extract_canonical_url(self, soup: BeautifulSoup) -> str:
        canonical_tag = soup.select_one('link[rel="canonical"]')
        if not isinstance(canonical_tag, Tag):
            _fail_validation('HTML is missing link[rel="canonical"]')
        canonical_url = _tag_attribute_as_string(canonical_tag, "href")
        if not canonical_url:
            _fail_validation("HTML canonical URL must be non-empty")
        _validate_http_url(canonical_url, field_name="canonical URL")
        return canonical_url

    def _extract_structure(self, doc_uid: str, content_root: Tag) -> tuple[list[Chunk], list[SectionRecord]]:
        chunks: list[Chunk] = []
        sections: list[SectionRecord] = []
        traversal_state = _SectionTraversalState(active_sections_by_level={}, chapter_sections_by_prefix={})

        for node in content_root.find_all("div"):
            nested_level = _extract_nested_level(node)
            if nested_level is None:
                continue

            classes = _tag_classes(node)
            if "paragraph" in classes and "topic" in classes:
                chunk = self._extract_chunk(
                    doc_uid=doc_uid,
                    paragraph=node,
                    active_sections_by_level=traversal_state.active_sections_by_level,
                )
                if chunk is not None:
                    chunks.append(chunk)
                continue

            if "topic" not in classes:
                continue

            section = self._extract_section(doc_uid=doc_uid, node=node, traversal_state=traversal_state)
            if section is None:
                continue

            traversal_state.position += 1
            sections.append(section)
            chapter_key = _extract_chapter_key(_extract_raw_heading_text(_extract_direct_heading(node) or node))
            if chapter_key is not None:
                traversal_state.chapter_sections_by_prefix[chapter_key] = section
            traversal_state.active_sections_by_level = {level: active_section for level, active_section in traversal_state.active_sections_by_level.items() if level < nested_level}
            traversal_state.active_sections_by_level[nested_level] = section

        return chunks, sections

    def _extract_section(
        self,
        doc_uid: str,
        node: Tag,
        traversal_state: _SectionTraversalState,
    ) -> SectionRecord | None:
        heading = _extract_direct_heading(node)
        if heading is None:
            return None

        nested_level = _extract_nested_level(node)
        if nested_level is None:
            return None

        raw_heading_text = _extract_raw_heading_text(heading)
        title = _extract_heading_title(heading)
        if title is None:
            return None

        if nested_level == 1:
            return None

        section_id = _tag_attribute_as_string(node, "id")
        if not section_id:
            return None

        parent_section = _get_parent_section(
            active_sections_by_level=traversal_state.active_sections_by_level,
            chapter_sections_by_prefix=traversal_state.chapter_sections_by_prefix,
            nested_level=nested_level,
            raw_heading_text=raw_heading_text,
        )
        section_lineage = [title] if parent_section is None else [*parent_section.section_lineage, title]

        return SectionRecord(
            section_id=section_id,
            doc_uid=doc_uid,
            parent_section_id=parent_section.section_id if parent_section is not None else None,
            level=nested_level,
            title=title,
            section_lineage=section_lineage,
            embedding_text=title,
            position=traversal_state.position,
        )

    def _extract_chunk(
        self,
        doc_uid: str,
        paragraph: Tag,
        active_sections_by_level: dict[int, SectionRecord],
    ) -> Chunk | None:
        chunk_number_tag = paragraph.select_one("td.paragraph_col1 .paranum > p")
        body_tag = paragraph.select_one("td.paragraph_col2 > .body")
        if not isinstance(chunk_number_tag, Tag) or not isinstance(body_tag, Tag):
            return None

        chunk_number = _normalize_whitespace(chunk_number_tag.get_text(" ", strip=True))
        if not chunk_number:
            return None

        text_lines = self._extract_body_lines(body_tag)
        text = "\n".join(line for line in text_lines if line)
        if not text:
            return None

        nested_level = _extract_nested_level(paragraph)
        containing_section = None
        if nested_level is not None:
            containing_section = _get_nearest_ancestor_section(
                active_sections_by_level=active_sections_by_level,
                nested_level=nested_level,
            )

        return Chunk(
            doc_uid=doc_uid,
            chunk_number=chunk_number,
            page_start="",
            page_end="",
            chunk_id=_tag_attribute_as_string(paragraph, "id"),
            text=text,
            containing_section_id=containing_section.section_id if containing_section is not None else None,
        )

    def _extract_body_lines(self, node: Tag) -> list[str]:
        if _is_hidden(node):
            return []

        if node.name in INLINE_TEXT_TAGS:
            text = _flatten_inline_text(node)
            return [text] if text else []

        lines: list[str] = []
        visible_children = [child for child in node.children if isinstance(child, Tag) and not _is_hidden(child)]

        if not visible_children:
            text = _flatten_inline_text(node)
            return [text] if text else []

        for child in visible_children:
            if child.name == "table":
                lines.extend(self._extract_table_lines(child))
                continue
            if child.name in INLINE_TEXT_TAGS:
                text = _flatten_inline_text(child)
                if text:
                    lines.append(text)
                continue

            child_lines = self._extract_body_lines(child)
            if child_lines:
                lines.extend(child_lines)
                continue

            text = _flatten_inline_text(child)
            if text:
                lines.append(text)

        return lines

    def _extract_table_lines(self, table: Tag) -> list[str]:
        bodies = table.find_all("tbody", recursive=False)
        row_containers = bodies or [table]
        rows: list[Tag] = []
        for container in row_containers:
            rows.extend(container.find_all("tr", recursive=False))

        if not rows:
            text = _flatten_inline_text(table)
            return [text] if text else []

        lines: list[str] = []
        for row in rows:
            if _is_hidden(row):
                continue
            cells = row.find_all("td", recursive=False)
            if len(cells) >= TABLE_ROW_WITH_LABEL_CELL_COUNT:
                label = _flatten_inline_text(cells[0]).replace(" ", "")
                body_lines = self._extract_body_lines(cells[1])
                if body_lines:
                    lines.append(f"{label}{body_lines[0]}")
                    lines.extend(body_lines[1:])
                    continue
                if label:
                    lines.append(label)
                    continue

            text = _flatten_inline_text(row)
            if text:
                lines.append(text)
        return lines


@dataclass(frozen=True)
class _TocContextEntry:
    """One table-of-contents lineage entry for a Navis page."""

    anchor_id: str
    ref_id: str
    raw_text: str
    title: str
    kind: str


@dataclass(frozen=True)
class _NavisHeading:
    """One inline Navis heading encountered in document order."""

    raw_text: str
    title: str
    kind: str
    anchor_id: str | None


@dataclass
class _NavisStructureState:
    """Mutable traversal state while extracting Navis sections and chunks."""

    active_sections_by_level: dict[int, SectionRecord]
    active_kinds_by_level: dict[int, str]
    sections: list[SectionRecord]
    chunks: list[Chunk]
    seen_section_ids: set[str]
    seen_chunk_ids: set[str]
    position: int = 0
    matched_context_index: int = 0


@dataclass(frozen=True)
class _SectionRecordDraft:
    """Draft data needed to construct one section record."""

    section_id: str
    title: str
    level: int
    position: int


@dataclass(frozen=True)
class _NavisBundleManifest:
    """Machine-readable metadata for one synthetic Navis chapter bundle."""

    chapter_ref_id: str
    chapter_title: str
    page_ref_ids: tuple[str, ...]
    page_titles: tuple[str, ...]
    product_key: str | None


class NavisHtmlExtractor:
    """Extractor implementation for EFL/Navis rendered DOM capture pairs."""

    source_type = "html"
    skip_if_unchanged = True

    def extract_from_soup(
        self,
        soup: BeautifulSoup,
        sidecar: HtmlSidecar,
        explicit_doc_uid: str | None,
    ) -> ExtractedDocument:
        """Extract a Navis HTML capture from a parsed soup and sidecar."""
        del explicit_doc_uid

        logger.info(f"Starting Navis HTML extraction for canonical_url={sidecar.canonical_url}, capture_format={sidecar.capture_format}")
        validation_started_at = perf_counter()
        self._validate_sidecar_urls(sidecar)
        doc_uid = self._derive_doc_uid(sidecar)
        logger.info(f"Validated Navis sidecar URLs and derived doc_uid={doc_uid} in {_elapsed_ms(validation_started_at):.2f}ms")

        if sidecar.capture_format == NAVIS_CHAPTER_BUNDLE_CAPTURE_FORMAT:
            logger.info(f"Detected Navis chapter bundle capture for doc_uid={doc_uid}")
            return self._extract_bundle_document(soup=soup, sidecar=sidecar, doc_uid=doc_uid)

        content_root = soup.select_one("#documentContent .question.question-export")
        if not isinstance(content_root, Tag):
            _fail_validation("HTML is missing the Navis content root")

        toc_context = self._build_toc_context(soup=soup, sidecar=sidecar)
        chunks, sections = self._extract_structure(doc_uid=doc_uid, content_root=content_root, toc_context=toc_context)
        section_closure_rows = _build_section_closure_rows(sections)

        return ExtractedDocument(
            document=DocumentRecord(
                doc_uid=doc_uid,
                source_type=self.source_type,
                source_title=sidecar.title,
                source_url=sidecar.url,
                canonical_url=sidecar.canonical_url,
                captured_at=sidecar.captured_at,
                source_domain=sidecar.source_domain,
                document_type="NAVIS",
            ),
            chunks=chunks,
            sections=sections,
            section_closure_rows=section_closure_rows,
        )

    def _validate_sidecar_urls(self, sidecar: HtmlSidecar) -> None:
        canonical_parts = urlparse(sidecar.canonical_url)
        source_parts = urlparse(sidecar.url)
        if canonical_parts.netloc.lower() != "abonnes.efl.fr":
            _fail_validation("Navis canonical_url must point to abonnes.efl.fr")
        if source_parts.netloc.lower() != "abonnes.efl.fr":
            _fail_validation("Navis url must point to abonnes.efl.fr")

        canonical_ref_id = self._get_query_param_value(sidecar.canonical_url, "refId")
        url_ref_id = self._get_query_param_value(sidecar.url, "refId")
        if not canonical_ref_id or not url_ref_id or canonical_ref_id != url_ref_id:
            _fail_validation("Navis sidecar url and canonical_url must contain the same refId")

        canonical_key = self._get_query_param_value(sidecar.canonical_url, "key")
        url_key = self._get_query_param_value(sidecar.url, "key")
        if not canonical_key or not url_key or canonical_key != url_key:
            _fail_validation("Navis sidecar url and canonical_url must contain the same key")

    def _derive_doc_uid(self, sidecar: HtmlSidecar) -> str:
        key = sidecar.product_key or self._get_query_param_value(sidecar.canonical_url, "key")
        ref_id = sidecar.chapter_ref_id or self._get_query_param_value(sidecar.canonical_url, "refId")
        if not key or not ref_id:
            fallback_slug = _slugify_doc_uid_token(sidecar.title)
            return f"navis-{fallback_slug}"
        return f"navis-{_slugify_doc_uid_token(key)}-{_slugify_doc_uid_token(ref_id)}"

    def _build_toc_context(self, soup: BeautifulSoup, sidecar: HtmlSidecar) -> list[_TocContextEntry]:
        ref_id = self._get_query_param_value(sidecar.canonical_url, "refId")
        if not ref_id:
            return []

        toc_anchor = self._find_toc_anchor_by_ref_id(soup=soup, ref_id=ref_id)
        if not isinstance(toc_anchor, Tag):
            _fail_validation(f"Could not locate Navis TOC entry for refId={ref_id}")

        toc_anchor_id = _tag_attribute_as_string(toc_anchor, "id")
        if not toc_anchor_id:
            _fail_validation(f"Navis TOC entry for refId={ref_id} is missing an id")

        context: list[_TocContextEntry] = []
        for anchor_id in _build_toc_anchor_lineage_ids(toc_anchor_id):
            lineage_anchor = soup.select_one(f'a[id="{anchor_id}"]')
            if not isinstance(lineage_anchor, Tag):
                continue
            raw_text = _normalize_whitespace(lineage_anchor.get_text(" ", strip=True))
            lineage_ref_id = _extract_navis_ref_id_from_anchor(lineage_anchor)
            if not raw_text or not lineage_ref_id:
                continue
            title = _normalize_navis_heading_title(raw_text)
            kind = _classify_navis_heading(raw_text=raw_text, classes=_tag_classes(lineage_anchor))
            if title and kind is not None:
                context.append(
                    _TocContextEntry(
                        anchor_id=anchor_id,
                        ref_id=lineage_ref_id,
                        raw_text=raw_text,
                        title=title,
                        kind=kind,
                    )
                )
        return context

    def _extract_bundle_document(
        self,
        soup: BeautifulSoup,
        sidecar: HtmlSidecar,
        doc_uid: str,
    ) -> ExtractedDocument:
        manifest_started_at = perf_counter()
        manifest = self._extract_bundle_manifest(soup=soup, sidecar=sidecar)
        logger.info(f"Extracted Navis bundle manifest for doc_uid={doc_uid} in {_elapsed_ms(manifest_started_at):.2f}ms; chapter_ref_id={manifest.chapter_ref_id}, manifest_page_count={len(manifest.page_ref_ids)}")

        bundle_root = soup.select_one("#ifrs-expert-navis-bundle")
        if not isinstance(bundle_root, Tag):
            _fail_validation("HTML is missing the Navis bundle root")

        page_nodes = [node for node in bundle_root.select("section.ifrs-expert-navis-page") if isinstance(node, Tag)]
        if not page_nodes:
            _fail_validation("HTML Navis bundle does not contain any page fragments")
        logger.info(f"Located Navis bundle root for doc_uid={doc_uid}; page_fragment_count={len(page_nodes)}")

        structure_started_at = perf_counter()
        chunks, sections = self._extract_bundle_structure(
            doc_uid=doc_uid,
            page_nodes=page_nodes,
            manifest=manifest,
        )
        logger.info(f"Extracted Navis bundle structure for doc_uid={doc_uid} in {_elapsed_ms(structure_started_at):.2f}ms; chunk_count={len(chunks)}, section_count={len(sections)}")
        closure_started_at = perf_counter()
        section_closure_rows = _build_section_closure_rows(sections)
        logger.info(f"Built Navis section closure rows for doc_uid={doc_uid} in {_elapsed_ms(closure_started_at):.2f}ms; closure_row_count={len(section_closure_rows)}")

        return ExtractedDocument(
            document=DocumentRecord(
                doc_uid=doc_uid,
                source_type=self.source_type,
                source_title=manifest.chapter_title,
                source_url=sidecar.url,
                canonical_url=sidecar.canonical_url,
                captured_at=sidecar.captured_at,
                source_domain=sidecar.source_domain,
                document_type="NAVIS",
            ),
            chunks=chunks,
            sections=sections,
            section_closure_rows=section_closure_rows,
        )

    def _extract_bundle_manifest(self, soup: BeautifulSoup, sidecar: HtmlSidecar) -> _NavisBundleManifest:
        manifest_payload: dict[str, object] = {}
        manifest_tag = soup.select_one("#ifrs-expert-navis-manifest")
        if isinstance(manifest_tag, Tag):
            manifest_text = manifest_tag.string or manifest_tag.get_text("", strip=True)
            if manifest_text:
                try:
                    parsed_manifest = json.loads(manifest_text)
                except json.JSONDecodeError as error:
                    _fail_validation("Navis bundle manifest is not valid JSON", cause=error)
                if not isinstance(parsed_manifest, dict):
                    _fail_validation("Navis bundle manifest must be a JSON object")
                manifest_payload = parsed_manifest

        chapter_ref_id = _optional_string(manifest_payload.get("chapter_ref_id")) or sidecar.chapter_ref_id
        chapter_title = _optional_string(manifest_payload.get("chapter_title")) or sidecar.chapter_title or sidecar.title
        if chapter_ref_id is None or chapter_title is None:
            _fail_validation("Navis chapter bundles must define chapter_ref_id and chapter_title")

        page_ref_ids = _optional_string_tuple(manifest_payload.get("page_ref_ids")) or sidecar.page_ref_ids
        page_titles = _optional_string_tuple(manifest_payload.get("page_titles")) or sidecar.page_titles
        product_key = _optional_string(manifest_payload.get("product_key")) or sidecar.product_key

        return _NavisBundleManifest(
            chapter_ref_id=chapter_ref_id,
            chapter_title=chapter_title,
            page_ref_ids=page_ref_ids,
            page_titles=page_titles,
            product_key=product_key,
        )

    def _extract_bundle_structure(
        self,
        doc_uid: str,
        page_nodes: list[Tag],
        manifest: _NavisBundleManifest,
    ) -> tuple[list[Chunk], list[SectionRecord]]:
        logger.info(f"Starting Navis bundle structure walk for doc_uid={doc_uid}; page_fragment_count={len(page_nodes)}, chapter_ref_id={manifest.chapter_ref_id}")
        state = _NavisStructureState(
            active_sections_by_level={},
            active_kinds_by_level={},
            sections=[],
            chunks=[],
            seen_section_ids=set(),
            seen_chunk_ids=set(),
        )

        chapter_section = _build_section_record(
            doc_uid=doc_uid,
            draft=_SectionRecordDraft(
                section_id=manifest.chapter_ref_id,
                title=_normalize_navis_heading_title(manifest.chapter_title),
                level=1,
                position=state.position,
            ),
            parent_section=None,
        )
        state.position += 1
        state.sections.append(chapter_section)
        state.seen_section_ids.add(chapter_section.section_id)
        state.active_sections_by_level[1] = chapter_section
        state.active_kinds_by_level[1] = "chapter"

        total_pages = len(page_nodes)
        for page_index, page_node in enumerate(page_nodes, start=1):
            content_root = page_node.select_one(".question.question-export")
            if not isinstance(content_root, Tag):
                _fail_validation("Navis bundle page fragment is missing .question.question-export")

            page_ref_id = _tag_attribute_as_string(page_node, "data-page-ref-id") or f"page-{page_index}"
            page_title = _tag_attribute_as_string(page_node, "data-page-title") or ""
            chunks_before = len(state.chunks)
            sections_before = len(state.sections)
            page_started_at = perf_counter()
            logger.info(f"Walking Navis bundle page {page_index}/{total_pages} for doc_uid={doc_uid}; page_ref_id={page_ref_id}, page_title={page_title!r}")
            self._append_bundle_page_structure(
                doc_uid=doc_uid,
                content_root=content_root,
                state=state,
            )
            logger.info(
                f"Finished Navis bundle page {page_index}/{total_pages} for doc_uid={doc_uid} in {_elapsed_ms(page_started_at):.2f}ms; added_chunks={len(state.chunks) - chunks_before}, added_sections={len(state.sections) - sections_before}"
            )

        return state.chunks, state.sections

    def _append_bundle_page_structure(
        self,
        doc_uid: str,
        content_root: Tag,
        state: _NavisStructureState,
    ) -> None:
        for child in content_root.children:
            if not isinstance(child, Tag):
                continue
            heading = self._build_navis_heading(child)
            if heading is not None:
                if heading.kind in {"title", "chapter"}:
                    continue
                self._append_bundle_heading(doc_uid=doc_uid, heading=heading, state=state)
                continue
            self._append_chunk(doc_uid=doc_uid, child=child, state=state)

    def _append_bundle_heading(
        self,
        doc_uid: str,
        heading: _NavisHeading,
        state: _NavisStructureState,
    ) -> None:
        level = _resolve_navis_heading_level(
            kind=heading.kind,
            active_kinds_by_level=state.active_kinds_by_level,
        )
        self._prune_navis_state(state=state, level=level)
        parent_section = state.active_sections_by_level.get(level - 1)
        section = _build_section_record(
            doc_uid=doc_uid,
            draft=_SectionRecordDraft(
                section_id=heading.anchor_id or f"{doc_uid}::{state.position}",
                title=heading.title,
                level=level,
                position=state.position,
            ),
            parent_section=parent_section,
        )
        if section.section_id in state.seen_section_ids:
            return
        state.position += 1
        state.active_sections_by_level[level] = section
        state.active_kinds_by_level[level] = heading.kind
        state.sections.append(section)
        state.seen_section_ids.add(section.section_id)

    def _extract_structure(
        self,
        doc_uid: str,
        content_root: Tag,
        toc_context: list[_TocContextEntry],
    ) -> tuple[list[Chunk], list[SectionRecord]]:
        inline_headings = self._collect_inline_headings(content_root)
        base_context, matched_context = _split_navis_toc_context(toc_context, inline_headings)
        state = _NavisStructureState(
            active_sections_by_level={},
            active_kinds_by_level={},
            sections=[],
            chunks=[],
            seen_section_ids=set(),
            seen_chunk_ids=set(),
        )

        self._seed_toc_context(doc_uid=doc_uid, base_context=base_context, state=state)

        for child in content_root.children:
            if not isinstance(child, Tag):
                continue
            if self._append_heading_section(doc_uid=doc_uid, child=child, base_context=base_context, matched_context=matched_context, state=state):
                continue
            self._append_chunk(doc_uid=doc_uid, child=child, state=state)

        return state.chunks, state.sections

    def _seed_toc_context(
        self,
        doc_uid: str,
        base_context: list[_TocContextEntry],
        state: _NavisStructureState,
    ) -> None:
        for context_entry in base_context:
            level = len(state.active_sections_by_level) + 1
            parent_section = state.active_sections_by_level.get(level - 1)
            section = _build_section_record(
                doc_uid=doc_uid,
                draft=_SectionRecordDraft(
                    section_id=context_entry.ref_id,
                    title=context_entry.title,
                    level=level,
                    position=state.position,
                ),
                parent_section=parent_section,
            )
            if section.section_id in state.seen_section_ids:
                continue
            state.position += 1
            state.sections.append(section)
            state.seen_section_ids.add(section.section_id)
            state.active_sections_by_level[level] = section
            state.active_kinds_by_level[level] = context_entry.kind

    def _append_heading_section(
        self,
        doc_uid: str,
        child: Tag,
        base_context: list[_TocContextEntry],
        matched_context: list[_TocContextEntry],
        state: _NavisStructureState,
    ) -> bool:
        heading = self._build_navis_heading(child)
        if heading is None:
            return False

        level = _resolve_navis_heading_level(
            kind=heading.kind,
            active_kinds_by_level=state.active_kinds_by_level,
        )
        if state.matched_context_index < len(matched_context) and matched_context[state.matched_context_index].title == heading.title:
            level = len(base_context) + state.matched_context_index + 1
            state.matched_context_index += 1

        self._prune_navis_state(state=state, level=level)
        parent_section = state.active_sections_by_level.get(level - 1)
        section = _build_section_record(
            doc_uid=doc_uid,
            draft=_SectionRecordDraft(
                section_id=heading.anchor_id or f"{doc_uid}::{state.position}",
                title=heading.title,
                level=level,
                position=state.position,
            ),
            parent_section=parent_section,
        )
        if section.section_id in state.seen_section_ids:
            return True
        state.position += 1
        state.active_sections_by_level[level] = section
        state.active_kinds_by_level[level] = heading.kind
        state.sections.append(section)
        state.seen_section_ids.add(section.section_id)
        return True

    def _append_chunk(self, doc_uid: str, child: Tag, state: _NavisStructureState) -> None:
        if not _is_navis_chunk_tag(child):
            return
        chunk = self._extract_chunk(
            doc_uid=doc_uid,
            paragraph=child,
            active_sections_by_level=state.active_sections_by_level,
        )
        if chunk is not None:
            chunk_identity = chunk.chunk_id or chunk.chunk_number
            if chunk_identity in state.seen_chunk_ids:
                return
            state.chunks.append(chunk)
            state.seen_chunk_ids.add(chunk_identity)

    def _build_navis_heading(self, child: Tag) -> _NavisHeading | None:
        if not _is_navis_heading_tag(child):
            return None
        raw_text = _extract_navis_heading_text(child)
        if not raw_text:
            return None
        kind = _classify_navis_heading(raw_text=raw_text, classes=_tag_classes(child))
        if kind is None:
            return None
        title = _normalize_navis_heading_title(raw_text)
        if not title:
            return None
        return _NavisHeading(
            raw_text=raw_text,
            title=title,
            kind=kind,
            anchor_id=_find_previous_named_anchor_id(child),
        )

    def _prune_navis_state(self, state: _NavisStructureState, level: int) -> None:
        state.active_sections_by_level = {existing_level: existing_section for existing_level, existing_section in state.active_sections_by_level.items() if existing_level < level}
        state.active_kinds_by_level = {existing_level: existing_kind for existing_level, existing_kind in state.active_kinds_by_level.items() if existing_level < level}

    def _collect_inline_headings(self, content_root: Tag) -> list[_NavisHeading]:
        headings: list[_NavisHeading] = []
        for child in content_root.children:
            if not isinstance(child, Tag) or not _is_navis_heading_tag(child):
                continue
            raw_text = _extract_navis_heading_text(child)
            if not raw_text:
                continue
            kind = _classify_navis_heading(raw_text=raw_text, classes=_tag_classes(child))
            if kind is None:
                continue
            title = _normalize_navis_heading_title(raw_text)
            if not title:
                continue
            headings.append(
                _NavisHeading(
                    raw_text=raw_text,
                    title=title,
                    kind=kind,
                    anchor_id=_find_previous_named_anchor_id(child),
                )
            )
        return headings

    def _find_toc_anchor_by_ref_id(self, soup: BeautifulSoup, ref_id: str) -> Tag | None:
        for anchor in soup.select("#sommaire a[href], #tocTree a[href]"):
            if not isinstance(anchor, Tag):
                continue
            if _extract_navis_ref_id_from_anchor(anchor) == ref_id:
                return anchor
        return soup.select_one(f'a[data-ref-id="{ref_id}"]')

    def _extract_chunk(
        self,
        doc_uid: str,
        paragraph: Tag,
        active_sections_by_level: dict[int, SectionRecord],
    ) -> Chunk | None:
        chunk_number_tag = paragraph.select_one("div.qw-p-no")
        body_tag = paragraph.select_one("div.qw-p-body")
        if not isinstance(chunk_number_tag, Tag) or not isinstance(body_tag, Tag):
            return None

        chunk_number = _normalize_whitespace(chunk_number_tag.get_text(" ", strip=True))
        if not chunk_number:
            return None

        text = _extract_navis_chunk_text(body_tag)
        if not text:
            return None

        containing_section = _get_highest_level_section(active_sections_by_level)
        return Chunk(
            doc_uid=doc_uid,
            chunk_number=chunk_number,
            page_start="",
            page_end="",
            chunk_id=_find_previous_named_anchor_id(paragraph) or "",
            text=text,
            containing_section_id=containing_section.section_id if containing_section is not None else None,
        )

    def _get_query_param_value(self, url: str, key: str) -> str | None:
        query_values = parse_qs(urlparse(url).query).get(key)
        if not query_values:
            return None
        first_value = query_values[0].strip()
        return first_value or None


def _build_source_extractor(sidecar: HtmlSidecar) -> IfrsHtmlExtractor | NavisHtmlExtractor:
    source_domain = sidecar.source_domain.lower()
    if source_domain == "abonnes.efl.fr":
        return NavisHtmlExtractor()
    if source_domain == "ifrs.org" or source_domain.endswith(".ifrs.org"):
        return IfrsHtmlExtractor()
    message = f"unsupported HTML source_domain: {sidecar.source_domain}"
    raise HtmlValidationError(message)


def _build_section_record(
    doc_uid: str,
    draft: _SectionRecordDraft,
    parent_section: SectionRecord | None,
) -> SectionRecord:
    section_lineage = [draft.title] if parent_section is None else [*parent_section.section_lineage, draft.title]
    return SectionRecord(
        section_id=draft.section_id,
        doc_uid=doc_uid,
        parent_section_id=parent_section.section_id if parent_section is not None else None,
        level=draft.level,
        title=draft.title,
        section_lineage=section_lineage,
        embedding_text=draft.title,
        position=draft.position,
    )


def _build_section_closure_rows(sections: list[SectionRecord]) -> list[SectionClosureRow]:
    section_by_id = {section.section_id: section for section in sections}
    closure_rows: list[SectionClosureRow] = []

    for section in sections:
        current_section: SectionRecord | None = section
        depth = 0
        while current_section is not None:
            closure_rows.append(
                SectionClosureRow(
                    ancestor_section_id=current_section.section_id,
                    descendant_section_id=section.section_id,
                    depth=depth,
                )
            )
            parent_section_id = current_section.parent_section_id
            current_section = section_by_id.get(parent_section_id) if parent_section_id is not None else None
            depth += 1

    return closure_rows


def _extract_nested_level(node: Tag) -> int | None:
    for css_class in _tag_classes(node):
        match = re.fullmatch(r"nested(\d+)", css_class)
        if match is not None:
            return int(match.group(1))
    return None


def _tag_classes(node: Tag) -> list[str]:
    class_value = node.get("class")
    if class_value is None:
        return []
    if isinstance(class_value, str):
        return class_value.split()
    return [str(css_class) for css_class in class_value]


def _extract_direct_heading(node: Tag) -> Tag | None:
    for tag_name in HEADING_TAG_NAMES:
        heading = node.find(tag_name, recursive=False)
        if isinstance(heading, Tag):
            return heading
    return None


def _extract_raw_heading_text(heading: Tag) -> str:
    text_parts = [_normalize_whitespace(text) for text in heading.stripped_strings]
    meaningful_parts = [part for part in text_parts if part and part != "+"]
    return _normalize_whitespace(" ".join(meaningful_parts))


def _extract_heading_title(heading: Tag) -> str | None:
    raw_heading_text = _extract_raw_heading_text(heading)
    if not raw_heading_text:
        return None

    if raw_heading_text.startswith("Appendix"):
        return "Appendix"

    heading_text = re.sub(r"\s*\+\s*$", "", raw_heading_text).strip()
    heading_text = HEADING_PREFIX_PATTERN.sub("", heading_text)
    return heading_text or None


def _get_parent_section(
    active_sections_by_level: dict[int, SectionRecord],
    chapter_sections_by_prefix: dict[str, SectionRecord],
    nested_level: int,
    raw_heading_text: str,
) -> SectionRecord | None:
    nearest_ancestor = _get_nearest_ancestor_section(
        active_sections_by_level=active_sections_by_level,
        nested_level=nested_level,
    )
    if nearest_ancestor is not None:
        return nearest_ancestor

    chapter_prefix = _extract_major_prefix(raw_heading_text)
    if chapter_prefix is not None and chapter_prefix in chapter_sections_by_prefix:
        return chapter_sections_by_prefix[chapter_prefix]

    same_level_section = active_sections_by_level.get(nested_level)
    if same_level_section is not None and SUBSECTION_PREFIX_PATTERN.match(raw_heading_text):
        return same_level_section

    return None


def _extract_chapter_key(raw_heading_text: str) -> str | None:
    match = re.match(r"^Chapter\s+([A-Za-z0-9.]+)", raw_heading_text)
    if match is None:
        return None
    return match.group(1)


def _extract_major_prefix(raw_heading_text: str) -> str | None:
    match = re.match(r"^([A-Z]?\d+)\.", raw_heading_text)
    if match is None:
        return None
    return match.group(1)


def _get_nearest_ancestor_section(
    active_sections_by_level: dict[int, SectionRecord],
    nested_level: int,
) -> SectionRecord | None:
    parent_levels = [level for level in active_sections_by_level if level < nested_level]
    if not parent_levels:
        return None
    nearest_level = max(parent_levels)
    return active_sections_by_level[nearest_level]


def _split_navis_toc_context(
    toc_context: list[_TocContextEntry],
    inline_headings: list[_NavisHeading],
) -> tuple[list[_TocContextEntry], list[_TocContextEntry]]:
    if not toc_context or not inline_headings:
        return toc_context, []

    first_inline_title = inline_headings[0].title
    start_index = next((index for index, entry in enumerate(toc_context) if entry.title == first_inline_title), len(toc_context))
    if start_index == len(toc_context):
        return toc_context, []

    matched_count = 0
    while start_index + matched_count < len(toc_context) and matched_count < len(inline_headings) and toc_context[start_index + matched_count].title == inline_headings[matched_count].title:
        matched_count += 1

    return toc_context[:start_index], toc_context[start_index : start_index + matched_count]


def _build_toc_anchor_lineage_ids(anchor_id: str) -> list[str]:
    parts = anchor_id.split("-")
    lineage_ids: list[str] = []
    current = parts[0]
    lineage_ids.append(current)
    for part in parts[1:]:
        current = f"{current}-{part}"
        lineage_ids.append(current)
    return lineage_ids


def _is_navis_heading_tag(node: Tag) -> bool:
    classes = _tag_classes(node)
    return node.name == "div" and "qw-level" in classes


def _is_navis_chunk_tag(node: Tag) -> bool:
    classes = _tag_classes(node)
    return node.name == "div" and "qw-par" in classes and "qw-par-p" in classes


def _extract_navis_heading_text(node: Tag) -> str:
    return _normalize_whitespace(node.get_text(" ", strip=True))


def _normalize_navis_heading_title(raw_text: str) -> str:
    stripped_title = NAVIS_TITLE_PREFIX_PATTERN.sub("", raw_text).strip()
    return _normalize_whitespace(stripped_title)


def _classify_navis_heading(raw_text: str, classes: list[str]) -> str | None:
    lowered_text = raw_text.lower()
    if "qw-level-8" in classes:
        return None

    prefix_rules: tuple[tuple[str, str], ...] = (
        ("titre ", "title"),
        ("chapitre ", "chapter"),
        ("section ", "section"),
    )
    for prefix, kind in prefix_rules:
        if lowered_text.startswith(prefix):
            return kind

    normalized_title = _normalize_navis_heading_title(raw_text)
    if normalized_title in NAVIS_EDITORIAL_TITLES or normalized_title.startswith("L'ESSENTIEL"):
        return "editorial"

    class_rules: tuple[tuple[str, str], ...] = (
        ("qw-level-1", "title"),
        ("qw-level-2", "chapter"),
        ("qw-level-3", "editorial"),
        ("qw-level-7", "leaf"),
    )
    for css_class, kind in class_rules:
        if css_class in classes:
            return kind

    return "leaf"


def _resolve_navis_heading_level(kind: str, active_kinds_by_level: dict[int, str]) -> int:
    fixed_levels = {
        "title": 1,
        "chapter": 2,
    }
    if kind in fixed_levels:
        return fixed_levels[kind]

    highest_active_level = max(active_kinds_by_level, default=0)
    highest_active_kind = active_kinds_by_level.get(highest_active_level)

    if kind == "editorial":
        return highest_active_level + 1 if highest_active_kind == "chapter" else 3

    if kind == "section":
        if highest_active_kind == "leaf":
            next_level = highest_active_level
        elif highest_active_kind == "editorial":
            next_level = highest_active_level + 1
        else:
            next_level = max(4, highest_active_level + 1)
        return next_level

    if highest_active_kind == "leaf":
        return highest_active_level
    return highest_active_level + 1 if highest_active_kind in {"editorial", "section", "chapter", "title"} else 4


def _find_previous_named_anchor_id(node: Tag) -> str | None:
    current_sibling: PageElement | None = node.previous_sibling
    while current_sibling is not None:
        if isinstance(current_sibling, Tag) and current_sibling.name == "a":
            anchor_id = _tag_attribute_as_string(current_sibling, "id")
            if anchor_id and not anchor_id.startswith("_JV"):
                return anchor_id
        current_sibling = current_sibling.previous_sibling
    return None


def _get_highest_level_section(active_sections_by_level: dict[int, SectionRecord]) -> SectionRecord | None:
    if not active_sections_by_level:
        return None
    return active_sections_by_level[max(active_sections_by_level)]


def _extract_navis_chunk_text(node: Tag) -> str:
    fragment = BeautifulSoup(str(node), "html.parser")
    for hidden_node in fragment.select('[style*="display: none"], [hidden], [aria-hidden="true"]'):
        hidden_node.decompose()

    line_break_marker = "__IFRS_EXPERT_LINE_BREAK__"
    for line_break in fragment.find_all("br"):
        line_break.replace_with(f" {line_break_marker} ")

    text = fragment.get_text(" ", strip=True).replace(line_break_marker, "\n")
    normalized_lines = [_normalize_navis_text_line(line) for line in text.splitlines()]

    meaningful_lines: list[str] = []
    for line in normalized_lines:
        if not line:
            continue
        if meaningful_lines and meaningful_lines[-1].endswith(":") and line.startswith("-"):
            meaningful_lines[-1] = f"{meaningful_lines[-1]}{line}"
            continue
        meaningful_lines.append(line)

    return "\n".join(meaningful_lines)


def _normalize_navis_text_line(text: str) -> str:
    normalized_text = _normalize_whitespace(text)
    normalized_text = re.sub(r"\(\s+", "(", normalized_text)
    normalized_text = re.sub(r"\s+\)", ")", normalized_text)
    normalized_text = normalized_text.replace(": -", ":-")
    normalized_text = re.sub(r":\s+-", ":-", normalized_text)
    normalized_text = re.sub(r"(\d)\s+(er|re|e|ème|eme)\b", r"\1\2", normalized_text, flags=re.IGNORECASE)
    return re.sub(r"([A-Za-zÀ-ÿ])'\s+([A-Za-zÀ-ÿ])", r"\1'\2", normalized_text)


def _extract_navis_ref_id_from_anchor(anchor: Tag) -> str | None:
    href = _tag_attribute_as_string(anchor, "href")
    if href:
        href_ref_id_values = parse_qs(urlparse(href).query).get("refId")
        if href_ref_id_values:
            href_ref_id = href_ref_id_values[0].strip()
            if href_ref_id:
                return href_ref_id

    data_ref_id = _tag_attribute_as_string(anchor, "data-ref-id")
    if data_ref_id:
        return data_ref_id

    return None


def _slugify_doc_uid_token(value: str) -> str:
    normalized_value = value.strip()
    slug = NAVIS_DOC_UID_TOKEN_PATTERN.sub("-", normalized_value).strip("-")
    return slug or "document"


def _elapsed_ms(started_at: float) -> float:
    return (perf_counter() - started_at) * 1000


def _fail_validation(message: str, *, cause: Exception | None = None) -> NoReturn:
    if cause is None:
        raise HtmlValidationError(message)
    raise HtmlValidationError(message) from cause


def _optional_string(value: object) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        stripped = value.strip()
        return stripped or None
    _fail_validation("optional sidecar fields must be strings when present")


def _optional_string_tuple(value: object) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        _fail_validation("optional sidecar list fields must be arrays of strings when present")

    normalized_values: list[str] = []
    for item in value:
        normalized_item = _optional_string(item)
        if normalized_item is None:
            _fail_validation("optional sidecar list fields must not contain empty values")
        normalized_values.append(normalized_item)
    return tuple(normalized_values)


def _validate_http_url(value: str, field_name: str) -> None:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        _fail_validation(f"{field_name} must be an HTTP or HTTPS URL")


def _is_hidden(node: Tag) -> bool:
    style = _tag_attribute_as_string(node, "style")
    return "display: none" in style.lower() or node.has_attr("hidden") or _tag_attribute_as_string(node, "aria-hidden") == "true"


def _tag_attribute_as_string(node: Tag, attribute_name: str) -> str:
    attribute_value = node.get(attribute_name)
    if isinstance(attribute_value, str):
        return attribute_value.strip()
    return ""


def _flatten_inline_text(node: Tag) -> str:
    fragment = BeautifulSoup(str(node), "html.parser")
    for hidden_node in fragment.select('[style*="display: none"], [hidden], [aria-hidden="true"]'):
        hidden_node.decompose()

    text = fragment.get_text(" ", strip=True)
    return _normalize_whitespace(text)


def _normalize_whitespace(text: str) -> str:
    normalized_text = text.replace("\xa0", " ")
    normalized_text = re.sub(r"\s+", " ", normalized_text).strip()
    normalized_text = re.sub(r"\s+([,.)\]])", r"\1", normalized_text)
    return re.sub(r"([([\]])\s+", r"\1", normalized_text)
