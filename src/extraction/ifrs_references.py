"""Parser for IFRS `Refer:` references in annotations and paragraph text."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from bs4.element import Tag

from src.models.reference import ContentReference, ReferenceTargetUnit

SourceLocationType = Literal["chunk", "section"]

_WORD_JOINER_PATTERN = re.compile(r"[\u200b\u2060]")
_WHITESPACE_PATTERN = re.compile(r"\s+")
_ENCLOSING_BRACKETS_PATTERN = re.compile(r"^\[\s*(.*?)\s*\]$")
_LEADING_LABEL_PATTERN = re.compile(
    r"^(?:(?:Basis for Conclusions|Illustrative Examples|Implementation Guidance)\s+)?(?:paragraphs?|paras?|paras\.|paragraph|sections?|section)\s+",
    re.IGNORECASE,
)
_DOCUMENT_HINT_PATTERN = re.compile(r"^(IAS|IFRS|IFRIC|SIC|PS)\s+\d+[A-Z]?(?:\.\d+)*(?:\([a-zA-Z0-9]+\))?", re.IGNORECASE)
_TARGET_RANGE_SPLIT_PATTERN = re.compile(r"\s*-\s*")
_TARGET_CONJUNCTION_SPLIT_PATTERN = re.compile(r"\s*(?:,|;|\band\b)\s*", re.IGNORECASE)
_TARGET_RANGE_PART_COUNT = 2
_TRAILING_OPTION_SUFFIX_PATTERN = re.compile(r"(?:\s+(?:and|or)\s+|\s*,\s*)\([A-Za-z0-9]+\)\s*$", re.IGNORECASE)
_TARGET_UNIT_PATTERN_BY_LABEL: dict[str, ReferenceTargetUnit] = {
    "paragraph": "paragraph",
    "paragraphs": "paragraph",
    "para": "paragraph",
    "paras": "paragraph",
    "paras.": "paragraph",
    "section": "section",
    "sections": "section",
}


@dataclass(frozen=True)
class _ReferenceExtractionContext:
    source_doc_uid: str
    source_location_type: SourceLocationType
    source_chunk_id: str | None
    source_section_id: str | None
    annotation_raw_text: str


def extract_references_from_note(
    note: Tag,
    *,
    source_doc_uid: str,
    source_location_type: SourceLocationType,
    source_chunk_id: str | None = None,
    source_section_id: str | None = None,
) -> list[ContentReference]:
    """Parse one `Refer:` annotation into structured reference records."""
    if not is_refer_annotation(note):
        return []

    return _extract_references_from_tag(
        note,
        _ReferenceExtractionContext(
            source_doc_uid=source_doc_uid,
            source_location_type=source_location_type,
            source_chunk_id=source_chunk_id,
            source_section_id=source_section_id,
            annotation_raw_text=_normalize_annotation_text(note.get_text(" ", strip=True)),
        ),
    )


def extract_references_from_container(
    container: Tag,
    *,
    source_doc_uid: str,
    source_location_type: SourceLocationType,
    source_chunk_id: str | None = None,
    source_section_id: str | None = None,
) -> list[ContentReference]:
    """Parse any container that may include refer annotations and inline xrefs."""
    return _extract_references_from_tag(
        container,
        _ReferenceExtractionContext(
            source_doc_uid=source_doc_uid,
            source_location_type=source_location_type,
            source_chunk_id=source_chunk_id,
            source_section_id=source_section_id,
            annotation_raw_text=_normalize_annotation_text(container.get_text(" ", strip=True)),
        ),
    )


def is_refer_annotation(note: Tag) -> bool:
    """Return whether one tag is an IFRS `Refer:` annotation."""
    classes = _tag_classes(note)
    if "note" not in classes or "edu" not in classes:
        return False
    prefix_node = note.select_one(".edu_prefix")
    if not isinstance(prefix_node, Tag):
        return False
    return _normalize_annotation_text(prefix_node.get_text(" ", strip=True)).lower() == "refer:"


def _classify_target(
    target_raw_text: str,
    target_start: str | None,
) -> tuple[str, str | None]:
    if _DOCUMENT_HINT_PATTERN.match(target_raw_text):
        match = _DOCUMENT_HINT_PATTERN.match(target_raw_text)
        if match is not None:
            return "cross_document", match.group(0).upper()
    normalized_target = target_start or _normalize_reference_text(target_raw_text)
    lower_target = normalized_target.lower()
    if lower_target.startswith("bc"):
        return "basis_for_conclusions", None
    if lower_target.startswith("ie"):
        return "illustrative_examples", None
    if lower_target.startswith("ig"):
        return "implementation_guidance", None
    return "same_standard_paragraph", None


def _classify_target_unit(target_raw_text: str, target_start: str | None) -> ReferenceTargetUnit:
    normalized_target = _normalize_reference_text(target_raw_text)
    doc_hint_match = _DOCUMENT_HINT_PATTERN.match(normalized_target)
    if doc_hint_match is not None:
        normalized_target = normalized_target[doc_hint_match.end() :].strip()
    label_match = _LEADING_LABEL_PATTERN.match(normalized_target)
    if label_match is not None:
        label = label_match.group(0).strip().split()[-1].lower()
        target_unit = _TARGET_UNIT_PATTERN_BY_LABEL.get(label)
        if target_unit is not None:
            return target_unit
    if target_start is None and _DOCUMENT_HINT_PATTERN.match(target_raw_text):
        return "document"
    return "paragraph"


def _parse_target_bounds(target_raw_text: str) -> tuple[str | None, str | None]:
    target_entries = _parse_target_entries(target_raw_text)
    if not target_entries:
        return None, None
    return target_entries[0]


def _parse_target_entries(target_raw_text: str) -> list[tuple[str | None, str | None]]:
    normalized_target = _normalize_reference_text(target_raw_text)
    doc_hint_match = _DOCUMENT_HINT_PATTERN.match(normalized_target)
    has_doc_hint = doc_hint_match is not None
    if doc_hint_match is not None:
        normalized_target = normalized_target[doc_hint_match.end() :].strip()
    normalized_target = _LEADING_LABEL_PATTERN.sub("", normalized_target).strip()
    normalized_target = normalized_target.removeprefix("paragraphs ").removeprefix("paragraph ")
    normalized_target = normalized_target.removeprefix("paras ").removeprefix("paras. ")
    normalized_target = normalized_target.strip()

    if not normalized_target:
        if has_doc_hint:
            return [(None, None)]
        return []

    split_parts = [part.strip() for part in _TARGET_CONJUNCTION_SPLIT_PATTERN.split(normalized_target) if part.strip()]
    if not split_parts:
        split_parts = [normalized_target]

    target_bounds: list[tuple[str | None, str | None]] = []
    for part in split_parts:
        part_bounds = _parse_single_target_bounds(part)
        if part_bounds is None:
            continue
        target_bounds.append(part_bounds)
    return target_bounds


def _parse_single_target_bounds(target_text: str) -> tuple[str | None, str | None] | None:
    normalized_target = _strip_trailing_option_suffixes(target_text.strip())
    if not normalized_target:
        return None

    range_parts = _TARGET_RANGE_SPLIT_PATTERN.split(normalized_target, maxsplit=1)
    if len(range_parts) == _TARGET_RANGE_PART_COUNT:
        start = _clean_target_identifier(range_parts[0])
        end = _clean_target_identifier(range_parts[1])
        return (start or None), (end or None)
    return _clean_target_identifier(normalized_target) or None, None


def _normalize_annotation_text(text: str) -> str:
    normalized_text = _normalize_reference_text(text)
    match = _ENCLOSING_BRACKETS_PATTERN.match(normalized_text)
    if match is not None:
        normalized_text = match.group(1)
    return normalized_text.strip()


def _normalize_reference_text(text: str) -> str:
    normalized_text = text.replace("\xa0", " ")
    normalized_text = _WORD_JOINER_PATTERN.sub("", normalized_text)
    normalized_text = normalized_text.replace("\u2010", "-")
    normalized_text = normalized_text.replace("\u2011", "-")
    normalized_text = normalized_text.replace("\u2012", "-")
    normalized_text = normalized_text.replace("\u2013", "-")
    normalized_text = normalized_text.replace("\u2014", "-")
    normalized_text = _WHITESPACE_PATTERN.sub(" ", normalized_text)
    return normalized_text.strip()


def _clean_target_identifier(text: str) -> str:
    cleaned_text = _normalize_reference_text(text)
    while True:
        updated_text = re.sub(r"\([A-Za-z0-9]+\)$", "", cleaned_text).strip()
        if updated_text == cleaned_text:
            return cleaned_text
        cleaned_text = updated_text


def _strip_trailing_option_suffixes(text: str) -> str:
    cleaned_text = text.strip()
    while True:
        updated_text = _TRAILING_OPTION_SUFFIX_PATTERN.sub("", cleaned_text).strip()
        if updated_text == cleaned_text:
            return cleaned_text
        cleaned_text = updated_text


def _extract_references_from_tag(
    tag: Tag,
    context: _ReferenceExtractionContext,
) -> list[ContentReference]:
    references: list[ContentReference] = []
    for reference_tag in _collect_reference_tags(tag):
        if is_refer_annotation(reference_tag):
            references.extend(
                _build_references_from_anchor_container(
                    reference_tag,
                    context,
                ),
            )
            continue

        if reference_tag.name != "a" or "xref" not in _tag_classes(reference_tag):
            continue

        target_raw_text = _normalize_annotation_text(reference_tag.get_text(" ", strip=True))
        if not target_raw_text:
            continue
        references.extend(
            _build_content_references(
                context,
                target_raw_text=target_raw_text,
            ),
        )
    return references


def _collect_reference_tags(node: Tag) -> list[Tag]:
    reference_tags: list[Tag] = []
    if is_refer_annotation(node):
        return [node]

    for child in node.children:
        if not isinstance(child, Tag):
            continue
        if is_refer_annotation(child):
            reference_tags.append(child)
            continue
        if child.name == "a" and "xref" in _tag_classes(child):
            reference_tags.append(child)
            continue
        reference_tags.extend(_collect_reference_tags(child))
    return reference_tags


def _build_references_from_anchor_container(
    anchor_container: Tag,
    context: _ReferenceExtractionContext,
) -> list[ContentReference]:
    references: list[ContentReference] = []
    xref_nodes = [node for node in anchor_container.find_all("a", class_="xref") if isinstance(node, Tag)]
    for xref_node in xref_nodes:
        target_raw_text = _normalize_annotation_text(xref_node.get_text(" ", strip=True))
        if not target_raw_text:
            continue
        references.extend(
            _build_content_references(
                context,
                target_raw_text=target_raw_text,
            ),
        )
    return references


def _build_content_references(
    context: _ReferenceExtractionContext,
    target_raw_text: str,
) -> list[ContentReference]:
    target_entries = _parse_target_entries(target_raw_text)
    if not target_entries:
        return []

    target_kind, target_doc_hint = _classify_target(
        target_raw_text=target_raw_text,
        target_start=target_entries[0][0],
    )
    target_unit = _classify_target_unit(target_raw_text=target_raw_text, target_start=target_entries[0][0])

    references: list[ContentReference] = []
    for target_start, target_end in target_entries:
        references.append(
            ContentReference(
                source_doc_uid=context.source_doc_uid,
                source_location_type=context.source_location_type,
                annotation_raw_text=context.annotation_raw_text,
                target_raw_text=target_raw_text,
                target_kind=target_kind,
                target_unit=target_unit,
                target_doc_hint=target_doc_hint,
                target_start=target_start,
                target_end=target_end,
                parsed_ok=True,
                source_chunk_id=context.source_chunk_id,
                source_section_id=context.source_section_id,
            ),
        )
    return references


def _tag_classes(node: Tag) -> list[str]:
    class_value = node.get("class")
    if class_value is None:
        return []
    if isinstance(class_value, str):
        return class_value.split()
    return [str(css_class) for css_class in class_value]
