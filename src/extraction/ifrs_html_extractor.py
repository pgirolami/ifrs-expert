"""IFRS-specific HTML extractor implementation."""

from __future__ import annotations

from pathlib import PurePosixPath
from typing import TYPE_CHECKING

from bs4.element import Tag

from src.extraction.html import (
    TABLE_ROW_WITH_LABEL_CELL_COUNT,
    HtmlSidecar,
    _build_section_closure_rows,
    _extract_chapter_key,
    _extract_direct_heading,
    _extract_heading_title,
    _extract_nested_level,
    _extract_raw_heading_text,
    _fail_validation,
    _flatten_inline_text,
    _get_highest_level_section,
    _get_nearest_ancestor_section,
    _get_parent_section,
    _is_hidden,
    _normalize_whitespace,
    _SectionTraversalState,
    _tag_attribute_as_string,
    _tag_classes,
)
from src.models.chunk import Chunk
from src.models.document import DocumentRecord, resolve_document_kind_from_document_type, resolve_document_type
from src.models.extraction import ExtractedDocument
from src.models.section import SectionRecord

if TYPE_CHECKING:
    from collections.abc import Iterable

    from bs4 import BeautifulSoup


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

        shell_canonical_url = self._extract_shell_canonical_url(soup)
        variant = self._extract_variant_metadata(soup=soup, shell_canonical_url=shell_canonical_url)

        identifier_tag = soup.select_one('meta[name="DC.Identifier"]')
        if not isinstance(identifier_tag, Tag):
            _fail_validation('HTML is missing meta[name="DC.Identifier"]')
        doc_uid = _tag_attribute_as_string(identifier_tag, "content")
        if not doc_uid:
            _fail_validation("HTML DC.Identifier must be non-empty")

        resolved_document_type = self._resolve_document_type(doc_uid=doc_uid, variant=variant)
        if sidecar.canonical_url != variant.canonical_url:
            _fail_validation("HTML canonical URL does not match sidecar canonical URL")
        if sidecar.document_type != resolved_document_type:
            _fail_validation("HTML resolved document_type does not match sidecar document_type")

        content_root = soup.select_one("section.ifrs-cmp-htmlviewer__section")
        if not isinstance(content_root, Tag):
            _fail_validation("HTML is missing the IFRS content root")

        chunks, sections = self._extract_structure(doc_uid=doc_uid, content_root=content_root)
        section_closure_rows = _build_section_closure_rows(sections)

        return ExtractedDocument(
            document=DocumentRecord(
                doc_uid=doc_uid,
                source_type=self.source_type,
                source_title=variant.normalized_title,
                source_url=sidecar.url,
                canonical_url=variant.canonical_url,
                captured_at=sidecar.captured_at,
                source_domain=sidecar.source_domain,
                document_type=resolved_document_type,
                document_kind=resolve_document_kind_from_document_type(resolved_document_type),
            ),
            chunks=chunks,
            sections=sections,
            section_closure_rows=section_closure_rows,
        )

    def _extract_shell_canonical_url(self, soup: BeautifulSoup) -> str:
        canonical_tag = soup.select_one('link[rel="canonical"]')
        if not isinstance(canonical_tag, Tag):
            _fail_validation('HTML is missing link[rel="canonical"]')
        canonical_url = _tag_attribute_as_string(canonical_tag, "href")
        if not canonical_url:
            _fail_validation("HTML canonical URL must be non-empty")
        return canonical_url

    def _extract_variant_metadata(self, soup: BeautifulSoup, shell_canonical_url: str) -> _IfrsVariantMetadata:
        checked_input = soup.select_one('input[name="documentType"][checked]')
        if not isinstance(checked_input, Tag):
            _fail_validation('HTML is missing input[name="documentType"][checked]')

        variant_value = _tag_attribute_as_string(checked_input, "value")
        if not variant_value:
            _fail_validation("Checked IFRS documentType value must be non-empty")

        variant_label_node = checked_input.find_next_sibling("span")
        if not isinstance(variant_label_node, Tag):
            _fail_validation("Checked IFRS documentType is missing its label")
        variant_label = _normalize_whitespace(variant_label_node.get_text(" ", strip=True))
        if not variant_label:
            _fail_validation("Checked IFRS documentType label must be non-empty")

        shell_title = ""
        if soup.title is not None:
            shell_title = _normalize_whitespace(soup.title.get_text(" ", strip=True))
        if not shell_title:
            _fail_validation("HTML page title must be non-empty")

        normalized_title = shell_title if variant_label == "Standard" else f"{shell_title} - {variant_label}"
        canonical_url = f"{shell_canonical_url}{variant_value}"
        variant_slug = PurePosixPath(variant_value).name.removesuffix(".html")
        if not variant_slug:
            _fail_validation("Checked IFRS documentType value must resolve to a document slug")

        return _IfrsVariantMetadata(
            label=variant_label,
            value=variant_value,
            slug=variant_slug,
            canonical_url=canonical_url,
            normalized_title=normalized_title,
        )

    def _resolve_document_type(self, doc_uid: str, variant: _IfrsVariantMetadata) -> str | None:
        normalized_doc_uid = doc_uid.strip().lower()
        if normalized_doc_uid.startswith("ifrs"):
            if normalized_doc_uid != variant.slug.lower():
                _fail_validation("HTML checked IFRS documentType does not match DC.Identifier")
            try:
                return IFRS_VARIANT_LABEL_TO_DOCUMENT_TYPE[variant.label]
            except KeyError as error:
                _fail_validation(f"Unsupported IFRS documentType label: {variant.label}", cause=error)
        if normalized_doc_uid.startswith("ifric"):
            try:
                return IFRIC_VARIANT_LABEL_TO_DOCUMENT_TYPE[variant.label]
            except KeyError as error:
                _fail_validation(f"Unsupported IFRIC documentType label: {variant.label}", cause=error)
        if normalized_doc_uid.startswith("ias"):
            try:
                return IAS_VARIANT_LABEL_TO_DOCUMENT_TYPE[variant.label]
            except KeyError as error:
                _fail_validation(f"Unsupported IAS documentType label: {variant.label}", cause=error)
        return resolve_document_type(doc_uid)

    def _extract_structure(self, doc_uid: str, content_root: Tag) -> tuple[list[Chunk], list[SectionRecord]]:
        chunks: list[Chunk] = []
        sections: list[SectionRecord] = []
        traversal_state = _SectionTraversalState(active_sections_by_level={}, chapter_sections_by_prefix={})

        for node in content_root.find_all(["div", "table"]):
            if not isinstance(node, Tag):
                continue
            annotation_chunk = self._maybe_extract_annotation_chunk(
                doc_uid=doc_uid,
                node=node,
                active_sections_by_level=traversal_state.active_sections_by_level,
            )
            if annotation_chunk is not None:
                chunks.append(annotation_chunk)
                continue

            paragraph_chunk = self._maybe_extract_paragraph_chunk(
                doc_uid=doc_uid,
                node=node,
                active_sections_by_level=traversal_state.active_sections_by_level,
            )
            if paragraph_chunk is not None:
                chunks.append(paragraph_chunk)
                continue

            section = self._extract_section(doc_uid=doc_uid, node=node, traversal_state=traversal_state)
            if section is None:
                continue

            self._register_section(node=node, section=section, traversal_state=traversal_state, sections=sections)

            section_body_chunk = self._extract_section_body_chunk(doc_uid=doc_uid, node=node, section=section)
            if section_body_chunk is not None:
                chunks.append(section_body_chunk)

            if doc_uid.endswith("-ig"):
                guidance_chunk = self._extract_guidance_chunk(doc_uid=doc_uid, node=node, section=section)
                if guidance_chunk is not None:
                    chunks.append(guidance_chunk)

        return chunks, sections

    def _maybe_extract_annotation_chunk(
        self,
        doc_uid: str,
        node: Tag,
        active_sections_by_level: dict[int, SectionRecord],
    ) -> Chunk | None:
        if node.name != "table" or "edu_fn_table" not in _tag_classes(node):
            return None
        return self._extract_annotation_chunk(
            doc_uid=doc_uid,
            annotation_table=node,
            active_sections_by_level=active_sections_by_level,
        )

    def _maybe_extract_paragraph_chunk(
        self,
        doc_uid: str,
        node: Tag,
        active_sections_by_level: dict[int, SectionRecord],
    ) -> Chunk | None:
        if node.name != "div":
            return None
        nested_level = _extract_nested_level(node)
        classes = _tag_classes(node)
        if nested_level is None or "paragraph" not in classes or "topic" not in classes:
            return None
        return self._extract_chunk(
            doc_uid=doc_uid,
            paragraph=node,
            active_sections_by_level=active_sections_by_level,
        )

    def _register_section(
        self,
        node: Tag,
        section: SectionRecord,
        traversal_state: _SectionTraversalState,
        sections: list[SectionRecord],
    ) -> None:
        nested_level = _extract_nested_level(node)
        if nested_level is None:
            return
        traversal_state.position += 1
        sections.append(section)
        chapter_key = _extract_chapter_key(_extract_raw_heading_text(_extract_direct_heading(node) or node))
        if chapter_key is not None:
            traversal_state.chapter_sections_by_prefix[chapter_key] = section
        traversal_state.active_sections_by_level = {level: active_section for level, active_section in traversal_state.active_sections_by_level.items() if level < nested_level}
        traversal_state.active_sections_by_level[nested_level] = section

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

    def _extract_section_body_chunk(self, doc_uid: str, node: Tag, section: SectionRecord) -> Chunk | None:
        normalized_title = _normalize_whitespace(section.title).lower()
        if normalized_title not in {"objective", "scope", "background", "issue", "issues", "introduction"}:
            return None
        if self._has_topic_paragraph_descendant(node):
            return None

        show_hide = node.find("div", class_="show-hide", recursive=False)
        if not isinstance(show_hide, Tag):
            return None
        body_container = show_hide.find("div", class_="body", recursive=False)
        if not isinstance(body_container, Tag):
            body_container = show_hide

        text_lines = self._extract_body_lines(body_container, include_hidden=True)
        text = "\n".join(line for line in text_lines if line)
        if not text:
            return None

        return Chunk(
            doc_uid=doc_uid,
            chunk_number=section.section_id,
            page_start="",
            page_end="",
            chunk_id=f"{section.section_id}__BODY",
            text=text,
            containing_section_id=section.section_id,
        )

    def _extract_guidance_chunk(self, doc_uid: str, node: Tag, section: SectionRecord) -> Chunk | None:
        title_prefix = section.title.split(" ", 1)[0].strip()
        if "." not in title_prefix:
            return None

        show_hide = node.find("div", class_="show-hide", recursive=False)
        if not isinstance(show_hide, Tag):
            return None
        body_container = show_hide.find("div", class_="body", recursive=False)
        if not isinstance(body_container, Tag):
            return None

        text_lines = self._extract_body_lines(body_container, include_hidden=True)
        text = "\n".join(line for line in text_lines if line)
        if not text:
            return None

        return Chunk(
            doc_uid=doc_uid,
            chunk_number=title_prefix,
            page_start="",
            page_end="",
            chunk_id=section.section_id,
            text=text,
            containing_section_id=section.section_id,
        )

    def _extract_annotation_chunk(
        self,
        doc_uid: str,
        annotation_table: Tag,
        active_sections_by_level: dict[int, SectionRecord],
    ) -> Chunk | None:
        chunk_number_tag = annotation_table.select_one("td.edu_fn_col1")
        body_tag = annotation_table.select_one("td.edu_fn_col2")
        if not isinstance(chunk_number_tag, Tag) or not isinstance(body_tag, Tag):
            return None

        chunk_number = _normalize_whitespace(chunk_number_tag.get_text(" ", strip=True))
        if not chunk_number:
            return None

        title_tag = body_tag.select_one(".edu_fn_ece_title")
        title_lines = self._extract_body_lines(title_tag, include_hidden=True) if isinstance(title_tag, Tag) else []
        body_lines = self._extract_body_lines(body_tag, include_hidden=True, skip_nodes=[title_tag] if isinstance(title_tag, Tag) else [])
        text = "\n".join(line for line in [*title_lines, *body_lines] if line)
        if not text:
            return None

        containing_section = _get_highest_level_section(active_sections_by_level)
        return Chunk(
            doc_uid=doc_uid,
            chunk_number=chunk_number,
            page_start="",
            page_end="",
            chunk_id=_tag_attribute_as_string(annotation_table, "id") or chunk_number,
            text=text,
            containing_section_id=containing_section.section_id if containing_section is not None else None,
        )

    def _has_topic_paragraph_descendant(self, node: Tag) -> bool:
        for descendant in node.find_all("div"):
            classes = _tag_classes(descendant)
            if "topic" in classes and "paragraph" in classes:
                return True
        return False

    def _extract_body_lines(
        self,
        node: Tag,
        *,
        include_hidden: bool = False,
        skip_nodes: Iterable[Tag | None] = (),
    ) -> list[str]:
        skipped_node_ids = {id(candidate) for candidate in skip_nodes if candidate is not None}
        return self._extract_body_lines_internal(node, include_hidden=include_hidden, skipped_node_ids=skipped_node_ids)

    def _extract_body_lines_internal(
        self,
        node: Tag,
        *,
        include_hidden: bool,
        skipped_node_ids: set[int],
    ) -> list[str]:
        if id(node) in skipped_node_ids or self._is_reference_only_educational_note(node):
            return []
        if not include_hidden and _is_hidden(node):
            return []

        if node.name in {"a", "em", "i", "p", "span", "strong", "sup", "sub"}:
            text = _flatten_inline_text(node)
            return [text] if text else []

        lines: list[str] = []
        relevant_children = self._get_relevant_children(
            node=node,
            include_hidden=include_hidden,
            skipped_node_ids=skipped_node_ids,
        )

        if not relevant_children:
            text = _flatten_inline_text(node)
            return [text] if text else []

        for child in relevant_children:
            child_lines = self._extract_child_lines(
                child=child,
                include_hidden=include_hidden,
                skipped_node_ids=skipped_node_ids,
            )
            if child_lines:
                lines.extend(child_lines)

        return lines

    def _get_relevant_children(
        self,
        node: Tag,
        *,
        include_hidden: bool,
        skipped_node_ids: set[int],
    ) -> list[Tag]:
        child_tags = [child for child in node.children if isinstance(child, Tag)]
        return [child for child in child_tags if id(child) not in skipped_node_ids and not self._is_reference_only_educational_note(child) and (include_hidden or not _is_hidden(child))]

    def _extract_child_lines(
        self,
        child: Tag,
        *,
        include_hidden: bool,
        skipped_node_ids: set[int],
    ) -> list[str]:
        if child.name == "table":
            return self._extract_table_lines(child, include_hidden=include_hidden, skipped_node_ids=skipped_node_ids)
        if child.name in {"a", "em", "i", "p", "span", "strong", "sup", "sub"}:
            text = _flatten_inline_text(child)
            return [text] if text else []

        child_lines = self._extract_body_lines_internal(child, include_hidden=include_hidden, skipped_node_ids=skipped_node_ids)
        if child_lines:
            return child_lines

        text = _flatten_inline_text(child)
        return [text] if text else []

    def _extract_table_lines(
        self,
        table: Tag,
        *,
        include_hidden: bool,
        skipped_node_ids: set[int],
    ) -> list[str]:
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
            if id(row) in skipped_node_ids or self._is_reference_only_educational_note(row):
                continue
            if not include_hidden and _is_hidden(row):
                continue
            cells = row.find_all("td", recursive=False)
            if len(cells) >= TABLE_ROW_WITH_LABEL_CELL_COUNT:
                label = _flatten_inline_text(cells[0]).replace(" ", "")
                body_lines = self._extract_body_lines_internal(cells[1], include_hidden=include_hidden, skipped_node_ids=skipped_node_ids)
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

    def _is_reference_only_educational_note(self, node: Tag) -> bool:
        classes = set(_tag_classes(node))
        return "note" in classes and "edu" in classes


class _IfrsVariantMetadata:
    def __init__(self, label: str, value: str, slug: str, canonical_url: str, normalized_title: str) -> None:
        self.label = label
        self.value = value
        self.slug = slug
        self.canonical_url = canonical_url
        self.normalized_title = normalized_title


IFRS_VARIANT_LABEL_TO_DOCUMENT_TYPE: dict[str, str] = {
    "Standard": "IFRS-S",
    "Basis for Conclusions": "IFRS-BC",
    "Illustrative Examples": "IFRS-IE",
    "Implementation Guidance": "IFRS-IG",
}
IFRIC_VARIANT_LABEL_TO_DOCUMENT_TYPE: dict[str, str] = {
    "Standard": "IFRIC",
    "Basis for Conclusions": "IFRIC-BC",
    "Illustrative Examples": "IFRIC-IE",
    "Implementation Guidance": "IFRIC-IG",
}
IAS_VARIANT_LABEL_TO_DOCUMENT_TYPE: dict[str, str] = {
    "Standard": "IAS-S",
    "Basis for Conclusions": "IAS-BC",
    "Basis for Conclusions IASC": "IAS-BCIASC",
    "Illustrative Examples": "IAS-IE",
    "Implementation Guidance": "IAS-IG",
    "Supporting Materials": "IAS-SM",
}
