"""HTML extraction for IFRS Expert."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

from src.models.chunk import Chunk
from src.models.document import DocumentRecord
from src.models.extraction import ExtractedDocument

INLINE_TEXT_TAGS = {"a", "em", "i", "p", "span", "strong", "sup", "sub"}
REQUIRED_SIDECAR_FIELDS = ("url", "title", "captured_at", "source_domain", "canonical_url")


class HtmlValidationError(ValueError):
    """Raised when an HTML capture pair fails validation."""


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
    def from_path(cls, sidecar_path: Path) -> "HtmlSidecar":
        """Load and validate an HTML sidecar file."""
        try:
            payload = json.loads(sidecar_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise HtmlValidationError("invalid sidecar JSON") from error

        for field_name in REQUIRED_SIDECAR_FIELDS:
            value = payload.get(field_name)
            if not isinstance(value, str) or not value.strip():
                raise HtmlValidationError(f"missing required sidecar field: {field_name}")

        _validate_http_url(payload["url"], field_name="url")
        _validate_http_url(payload["canonical_url"], field_name="canonical_url")

        try:
            datetime.fromisoformat(payload["captured_at"].replace("Z", "+00:00"))
        except ValueError as error:
            raise HtmlValidationError("captured_at must be an ISO-8601 timestamp") from error

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
        self._sidecar_path = sidecar_path

    def extract(self, source_path: Path, explicit_doc_uid: str | None) -> ExtractedDocument:
        """Extract an HTML capture into document metadata and paragraph chunks."""
        del explicit_doc_uid

        if not source_path.exists():
            raise HtmlValidationError(f"HTML file not found: {source_path}")
        if not self._sidecar_path.exists():
            raise HtmlValidationError(f"HTML sidecar not found: {self._sidecar_path}")

        sidecar = HtmlSidecar.from_path(self._sidecar_path)
        soup = BeautifulSoup(source_path.read_text(encoding="utf-8"), "html.parser")

        canonical_url = self._extract_canonical_url(soup)
        if canonical_url != sidecar.canonical_url:
            raise HtmlValidationError("HTML canonical URL does not match sidecar canonical URL")

        identifier_tag = soup.select_one('meta[name="DC.Identifier"]')
        if not isinstance(identifier_tag, Tag):
            raise HtmlValidationError("HTML is missing meta[name=\"DC.Identifier\"]")
        doc_uid = identifier_tag.get("content", "").strip()
        if not doc_uid:
            raise HtmlValidationError("HTML DC.Identifier must be non-empty")

        content_root = soup.select_one("section.ifrs-cmp-htmlviewer__section")
        if not isinstance(content_root, Tag):
            raise HtmlValidationError("HTML is missing the IFRS content root")

        chunks = self._extract_chunks(doc_uid=doc_uid, content_root=content_root)

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
        )

    def _extract_canonical_url(self, soup: BeautifulSoup) -> str:
        canonical_tag = soup.select_one('link[rel="canonical"]')
        if not isinstance(canonical_tag, Tag):
            raise HtmlValidationError("HTML is missing link[rel=\"canonical\"]")
        canonical_url = canonical_tag.get("href", "").strip()
        if not canonical_url:
            raise HtmlValidationError("HTML canonical URL must be non-empty")
        _validate_http_url(canonical_url, field_name="canonical URL")
        return canonical_url

    def _extract_chunks(self, doc_uid: str, content_root: Tag) -> list[Chunk]:
        chunks: list[Chunk] = []
        paragraph_nodes = content_root.select("div.topic.paragraph[id]")
        for paragraph in paragraph_nodes:
            section_tag = paragraph.select_one("td.paragraph_col1 .paranum > p")
            body_tag = paragraph.select_one("td.paragraph_col2 > .body")
            if not isinstance(section_tag, Tag) or not isinstance(body_tag, Tag):
                continue

            section_path = _normalize_whitespace(section_tag.get_text(" ", strip=True))
            if not section_path:
                continue

            text_lines = self._extract_body_lines(body_tag)
            text = "\n".join(line for line in text_lines if line)
            if not text:
                continue

            chunks.append(
                Chunk(
                    doc_uid=doc_uid,
                    section_path=section_path,
                    page_start="",
                    page_end="",
                    source_anchor=paragraph.get("id", "").strip(),
                    text=text,
                )
            )
        return chunks

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
        row_containers = bodies if bodies else [table]
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
            if len(cells) >= 2:
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


def _optional_string(value: object) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        stripped = value.strip()
        return stripped or None
    raise HtmlValidationError("optional sidecar fields must be strings when present")


def _validate_http_url(value: str, field_name: str) -> None:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise HtmlValidationError(f"{field_name} must be an HTTP or HTTPS URL")


def _is_hidden(node: Tag) -> bool:
    style = node.get("style", "")
    return "display: none" in style.lower() or node.has_attr("hidden") or node.get("aria-hidden") == "true"


def _flatten_inline_text(node: Tag) -> str:
    fragment = BeautifulSoup(str(node), "html.parser")
    for hidden_node in fragment.select('[style*="display: none"], [hidden], [aria-hidden="true"]'):
        hidden_node.decompose()

    text = fragment.get_text(" ", strip=True)
    return _normalize_whitespace(text)


def _normalize_whitespace(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+([,.;:)?\]])", r"\1", text)
    text = re.sub(r"([([\]])\s+", r"\1", text)
    return text
