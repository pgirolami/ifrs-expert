"""HTML extraction for IFRS Expert."""

from __future__ import annotations

import importlib
import json
import logging
import re
from dataclasses import dataclass
from datetime import datetime
from time import perf_counter
from typing import TYPE_CHECKING, Final, NoReturn, Protocol
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup
from bs4.element import PageElement, Tag

from src.models.document import DOCUMENT_TYPES
from src.models.section import SectionClosureRow, SectionRecord

if TYPE_CHECKING:
    from pathlib import Path

    from src.models.chunk import Chunk
    from src.models.extraction import ExtractedDocument

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
NAVIS_LIST_MARKER_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^(?:\d+|[A-Z]|[IVXLCDM]+)\.\s+",
    re.IGNORECASE,
)

logger = logging.getLogger(__name__)


class HtmlValidationError(ValueError):
    """Raised when an HTML capture pair fails validation."""


class SourceHtmlExtractor(Protocol):
    """Protocol implemented by source-specific HTML extractors."""

    def extract_from_soup(
        self,
        soup: BeautifulSoup,
        sidecar: HtmlSidecar,
        explicit_doc_uid: str | None,
    ) -> ExtractedDocument:
        """Extract a source-specific HTML capture from a parsed soup tree."""


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
    document_type: str | None
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
            document_type=_optional_document_type(payload.get("document_type")),
            page_ref_ids=_optional_string_tuple(payload.get("page_ref_ids")),
            page_titles=_optional_string_tuple(payload.get("page_titles")),
        )


@dataclass(frozen=True)
class _TocContextEntry:
    """One table-of-contents lineage entry for a Navis page."""

    anchor_id: str
    ref_id: str
    raw_text: str
    title: str
    kind: str


@dataclass(frozen=True)
class _PreviousNavisAnchor:
    """Anchor metadata immediately preceding a Navis heading or chunk."""

    anchor_id: str
    is_context_only: bool


@dataclass(frozen=True)
class _NavisHeading:
    """One inline Navis heading encountered in document order."""

    raw_text: str
    title: str
    kind: str
    anchor_id: str | None
    is_context_only: bool = False


@dataclass
class _NavisStructureState:
    """Mutable traversal state while extracting Navis sections and chunks."""

    active_sections_by_level: dict[int, SectionRecord]
    active_kinds_by_level: dict[int, str]
    active_context_only_by_level: dict[int, bool]
    sections: list[SectionRecord]
    section_by_id: dict[str, SectionRecord]
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


def _build_source_extractor(sidecar: HtmlSidecar) -> SourceHtmlExtractor:
    source_domain = sidecar.source_domain.lower()
    if source_domain == "abonnes.efl.fr":
        extractor_module = importlib.import_module("src.extraction.navis_html_extractor")
        return extractor_module.NavisHtmlExtractor()
    if source_domain == "ifrs.org" or source_domain.endswith(".ifrs.org"):
        extractor_module = importlib.import_module("src.extraction.ifrs_html_extractor")
        return extractor_module.IfrsHtmlExtractor()
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
    stripped_title = NAVIS_LIST_MARKER_PATTERN.sub("", stripped_title)
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


def _resolve_navis_heading_level(
    kind: str,
    active_kinds_by_level: dict[int, str],
    active_context_only_by_level: dict[int, bool],
) -> int:
    fixed_levels = {
        "title": 1,
        "chapter": 2,
    }
    if kind in fixed_levels:
        return fixed_levels[kind]

    highest_active_level = max(active_kinds_by_level, default=0)
    highest_active_kind = active_kinds_by_level.get(highest_active_level)
    highest_active_is_context_only = active_context_only_by_level.get(highest_active_level, False)

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
        return highest_active_level + 1 if highest_active_is_context_only else highest_active_level
    return highest_active_level + 1 if highest_active_kind in {"editorial", "section", "chapter", "title"} else 4


def _find_previous_navis_anchor(node: Tag) -> _PreviousNavisAnchor | None:
    current_sibling: PageElement | None = node.previous_sibling
    while current_sibling is not None:
        if isinstance(current_sibling, Tag) and current_sibling.name == "a":
            anchor_id = _tag_attribute_as_string(current_sibling, "id")
            if anchor_id and not anchor_id.startswith("_JV"):
                return _PreviousNavisAnchor(anchor_id=anchor_id, is_context_only=False)
            context_anchor_id = _tag_attribute_as_string(current_sibling, "data-ifrs-expert-context-ref-id")
            if context_anchor_id and not context_anchor_id.startswith("_JV"):
                return _PreviousNavisAnchor(anchor_id=context_anchor_id, is_context_only=True)
        current_sibling = current_sibling.previous_sibling
    return None


def _find_previous_named_anchor_id(node: Tag) -> str | None:
    previous_anchor = _find_previous_navis_anchor(node)
    if previous_anchor is None:
        return None
    return previous_anchor.anchor_id


def _get_highest_level_section(active_sections_by_level: dict[int, SectionRecord]) -> SectionRecord | None:
    if not active_sections_by_level:
        return None
    return active_sections_by_level[max(active_sections_by_level)]


def _extract_navis_chunk_text(node: Tag) -> str:
    fragment = BeautifulSoup(str(node), "html.parser")
    _remove_reference_only_educational_notes(fragment)
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


def _optional_document_type(value: object) -> str | None:
    document_type = _optional_string(value)
    if document_type is None:
        return None
    if document_type not in DOCUMENT_TYPES:
        supported_document_types = ", ".join(DOCUMENT_TYPES)
        _fail_validation(f"document_type must be one of {supported_document_types}")
    return document_type


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
    _remove_reference_only_educational_notes(fragment)
    for hidden_node in fragment.select('[style*="display: none"], [hidden], [aria-hidden="true"]'):
        hidden_node.decompose()

    text = fragment.get_text(" ", strip=True)
    return _normalize_whitespace(text)


def _remove_reference_only_educational_notes(fragment: BeautifulSoup) -> None:
    for note_node in fragment.select('[class~="note"][class~="edu"]'):
        note_node.decompose()


def _normalize_whitespace(text: str) -> str:
    normalized_text = text.replace("\xa0", " ")
    normalized_text = re.sub(r"\s+", " ", normalized_text).strip()
    normalized_text = re.sub(r"\s+([,.)\]])", r"\1", normalized_text)
    return re.sub(r"([([\]])\s+", r"\1", normalized_text)


def __getattr__(name: str) -> object:
    module_names = {
        "HtmlExtractor": "src.extraction.html_extractor",
        "IfrsHtmlExtractor": "src.extraction.ifrs_html_extractor",
        "NavisHtmlExtractor": "src.extraction.navis_html_extractor",
    }
    module_name = module_names.get(name)
    if module_name is None:
        message = f"module {__name__!r} has no attribute {name!r}"
        raise AttributeError(message)
    module = importlib.import_module(module_name)
    return getattr(module, name)
