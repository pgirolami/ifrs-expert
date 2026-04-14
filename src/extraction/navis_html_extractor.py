"""Navis-specific HTML extractor implementation."""

from __future__ import annotations

import json
import logging
from time import perf_counter
from typing import TYPE_CHECKING
from urllib.parse import parse_qs, urlparse

from bs4.element import Tag

from src.extraction.html import (
    NAVIS_CHAPTER_BUNDLE_CAPTURE_FORMAT,
    HtmlSidecar,
    _build_section_closure_rows,
    _build_section_record,
    _build_toc_anchor_lineage_ids,
    _classify_navis_heading,
    _elapsed_ms,
    _extract_navis_chunk_text,
    _extract_navis_heading_text,
    _extract_navis_ref_id_from_anchor,
    _fail_validation,
    _find_previous_named_anchor_id,
    _find_previous_navis_anchor,
    _get_highest_level_section,
    _is_navis_chunk_tag,
    _is_navis_heading_tag,
    _NavisBundleManifest,
    _NavisHeading,
    _NavisStructureState,
    _normalize_navis_heading_title,
    _optional_string,
    _optional_string_tuple,
    _resolve_navis_heading_level,
    _SectionRecordDraft,
    _slugify_doc_uid_token,
    _split_navis_toc_context,
    _tag_attribute_as_string,
    _tag_classes,
    _TocContextEntry,
)
from src.models.chunk import Chunk
from src.models.document import DocumentRecord
from src.models.extraction import ExtractedDocument

if TYPE_CHECKING:
    from bs4 import BeautifulSoup

    from src.models.section import SectionRecord

logger = logging.getLogger(__name__)


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
            raw_text = " ".join(lineage_anchor.get_text(" ", strip=True).split())
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
            active_context_only_by_level={},
            sections=[],
            section_by_id={},
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
        state.section_by_id[chapter_section.section_id] = chapter_section
        state.seen_section_ids.add(chapter_section.section_id)
        state.active_sections_by_level[1] = chapter_section
        state.active_kinds_by_level[1] = "chapter"
        state.active_context_only_by_level[1] = False

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
            active_context_only_by_level=state.active_context_only_by_level,
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
            existing_section = state.section_by_id[section.section_id]
            state.active_sections_by_level[level] = existing_section
            state.active_kinds_by_level[level] = heading.kind
            state.active_context_only_by_level[level] = heading.is_context_only
            return
        state.position += 1
        state.active_sections_by_level[level] = section
        state.active_kinds_by_level[level] = heading.kind
        state.active_context_only_by_level[level] = heading.is_context_only
        state.sections.append(section)
        state.section_by_id[section.section_id] = section
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
            active_context_only_by_level={},
            sections=[],
            section_by_id={},
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
            state.section_by_id[section.section_id] = section
            state.seen_section_ids.add(section.section_id)
            state.active_sections_by_level[level] = section
            state.active_kinds_by_level[level] = context_entry.kind
            state.active_context_only_by_level[level] = False

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
            active_context_only_by_level=state.active_context_only_by_level,
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
            existing_section = state.section_by_id[section.section_id]
            state.active_sections_by_level[level] = existing_section
            state.active_kinds_by_level[level] = heading.kind
            state.active_context_only_by_level[level] = heading.is_context_only
            return True
        state.position += 1
        state.active_sections_by_level[level] = section
        state.active_kinds_by_level[level] = heading.kind
        state.active_context_only_by_level[level] = heading.is_context_only
        state.sections.append(section)
        state.section_by_id[section.section_id] = section
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
        previous_anchor = _find_previous_navis_anchor(child)
        return _NavisHeading(
            raw_text=raw_text,
            title=title,
            kind=kind,
            anchor_id=previous_anchor.anchor_id if previous_anchor is not None else None,
            is_context_only=previous_anchor.is_context_only if previous_anchor is not None else False,
        )

    def _prune_navis_state(self, state: _NavisStructureState, level: int) -> None:
        state.active_sections_by_level = {existing_level: existing_section for existing_level, existing_section in state.active_sections_by_level.items() if existing_level < level}
        state.active_kinds_by_level = {existing_level: existing_kind for existing_level, existing_kind in state.active_kinds_by_level.items() if existing_level < level}
        state.active_context_only_by_level = {existing_level: is_context_only for existing_level, is_context_only in state.active_context_only_by_level.items() if existing_level < level}

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
            previous_anchor = _find_previous_navis_anchor(child)
            headings.append(
                _NavisHeading(
                    raw_text=raw_text,
                    title=title,
                    kind=kind,
                    anchor_id=previous_anchor.anchor_id if previous_anchor is not None else None,
                    is_context_only=previous_anchor.is_context_only if previous_anchor is not None else False,
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

        chunk_number = " ".join(chunk_number_tag.get_text(" ", strip=True).split())
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
