"""HTML extraction for IFRS Expert."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Final, NoReturn
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from bs4.element import Tag

from src.models.chunk import Chunk
from src.models.document import DocumentRecord
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


class HtmlValidationError(ValueError):
    """Raised when an HTML capture pair fails validation."""


@dataclass
class _SectionTraversalState:
    """Mutable traversal state while extracting sections from HTML."""

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

        return cls(
            url=payload["url"],
            title=payload["title"],
            captured_at=payload["captured_at"],
            source_domain=payload["source_domain"],
            canonical_url=payload["canonical_url"],
            extension_version=_optional_string(payload.get("extension_version")),
            content_type=_optional_string(payload.get("content_type")),
        )


class HtmlExtractor:
    """Extractor implementation for IFRS HTML capture pairs."""

    source_type = "html"
    skip_if_unchanged = True

    def __init__(self, sidecar_path: Path) -> None:
        """Initialize the extractor with the matching JSON sidecar path."""
        self._sidecar_path = sidecar_path

    def extract(self, source_path: Path, explicit_doc_uid: str | None) -> ExtractedDocument:
        """Extract an HTML capture into document metadata, chunks, and sections."""
        del explicit_doc_uid

        if not source_path.exists():
            _fail_validation(f"HTML file not found: {source_path}")
        if not self._sidecar_path.exists():
            _fail_validation(f"HTML sidecar not found: {self._sidecar_path}")

        sidecar = HtmlSidecar.from_path(self._sidecar_path)
        soup = BeautifulSoup(source_path.read_text(encoding="utf-8"), "html.parser")

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
    normalized_text = re.sub(r"\s+([,.;:)?\]])", r"\1", normalized_text)
    return re.sub(r"([([\]])\s+", r"\1", normalized_text)
