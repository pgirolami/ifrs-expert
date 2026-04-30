"""Shared parsing helpers for declarative retrieval expectations."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, cast

import yaml

from src.models.document import resolve_document_type_from_doc_uid

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence
    from pathlib import Path


@dataclass(frozen=True)
class RequiredSectionRange:
    """One required inclusive chunk_number range for a document."""

    document: str
    start: str
    end: str
    chunk_numbers: tuple[str, ...]


@dataclass(frozen=True)
class RetrieveContract:
    """Declarative retrieval expectations for one family."""

    required_documents: tuple[str, ...]
    required_section_ranges: tuple[RequiredSectionRange, ...]


def load_retrieve_contract_from_family_path(family_path: Path) -> RetrieveContract:
    """Load the `assert_retrieve` contract from a family.yaml file."""
    raw_data = yaml.safe_load(family_path.read_text(encoding="utf-8"))
    if not isinstance(raw_data, dict):
        message = f"{family_path}: expected a mapping"
        raise TypeError(message)

    raw_contract = raw_data.get("assert_retrieve")
    if raw_contract is None:
        message = f"{family_path}: missing assert_retrieve"
        raise ValueError(message)
    return parse_retrieve_contract(raw_contract, context=f"{family_path}: assert_retrieve")


def parse_retrieve_contract(raw_contract: object, *, context: str) -> RetrieveContract:
    """Parse a declarative retrieval contract from YAML."""
    mapping = _require_mapping(raw_contract, context=context)
    required_documents = _parse_required_documents(mapping.get("required_documents"), context=f"{context}.required_documents")
    required_section_ranges = _parse_required_section_ranges(mapping.get("required_section_ranges"), context=f"{context}.required_section_ranges")
    if not required_documents:
        message = f"{context}: required_documents must not be empty"
        raise ValueError(message)
    return RetrieveContract(
        required_documents=required_documents,
        required_section_ranges=required_section_ranges,
    )


def build_promptfoo_retrieve_assertions(contract: RetrieveContract) -> list[dict[str, object]]:
    """Translate a declarative retrieval contract into Promptfoo assertions."""
    assertions: list[dict[str, object]] = [
        {
            "type": "javascript",
            "description": "Required Q1 authorities are in the top 5 with expected document types",
            "value": _render_required_documents_js(contract.required_documents),
        }
    ]
    assertions.extend(
        [
            {
                "type": "javascript",
                "description": f"Required chunk numbers are present for {required_range.document} {required_range.start}-{required_range.end}",
                "value": _render_required_range_js(required_range),
            }
            for required_range in contract.required_section_ranges
        ]
    )
    return assertions


def _render_required_documents_js(required_documents: tuple[str, ...]) -> str:
    expected_types = {}
    for doc_uid in required_documents:
        document_type = resolve_document_type_from_doc_uid(doc_uid)
        if document_type is None:
            message = f"Could not resolve document type for required document {doc_uid}"
            raise ValueError(message)
        expected_types[doc_uid] = document_type

    required_documents_js = _render_js_list(required_documents)
    expected_types_js = _render_js_object(expected_types)
    return "\n".join(
        [
            "const data = JSON.parse(output);",
            "if (!data || !Array.isArray(data.document_hits)) {",
            "  return false;",
            "}",
            f"const requiredDocuments = {required_documents_js};",
            f"const expectedTypes = {expected_types_js};",
            "const top5 = data.document_hits.slice(0, 5);",
            "return requiredDocuments.every((docUid) => {",
            "  const hit = top5.find((item) => item.doc_uid === docUid);",
            "  return hit?.document_type === expectedTypes[docUid];",
            "});",
        ]
    )


def _render_required_range_js(required_range: RequiredSectionRange) -> str:
    chunk_numbers_js = _render_js_list(list(required_range.chunk_numbers))
    return "\n".join(
        [
            "const data = JSON.parse(output);",
            "if (!data || !Array.isArray(data.chunks)) {",
            "  return false;",
            "}",
            f"const expectedChunkNumbers = {chunk_numbers_js};",
            f"const chunksForDocument = data.chunks.filter((item) => item.doc_uid === '{required_range.document}').map((item) => item.chunk_number);",
            "return expectedChunkNumbers.every((chunkNumber) => chunksForDocument.includes(chunkNumber));",
        ]
    )


def _parse_required_documents(value: object, *, context: str) -> tuple[str, ...]:
    sequence = _require_sequence(value, context=context)
    required_documents: list[str] = []
    for index, item in enumerate(sequence):
        doc_uid = _require_str(item, context=f"{context}[{index}]")
        required_documents.append(doc_uid)
    return tuple(required_documents)


def _parse_required_section_ranges(value: object, *, context: str) -> tuple[RequiredSectionRange, ...]:
    sequence = _require_sequence(value, context=context)
    required_ranges: list[RequiredSectionRange] = []
    for index, item in enumerate(sequence):
        mapping = _require_mapping(item, context=f"{context}[{index}]")
        document = _require_str(mapping.get("document"), context=f"{context}[{index}].document")
        start = _require_str(mapping.get("start"), context=f"{context}[{index}].start")
        end = _require_str(mapping.get("end"), context=f"{context}[{index}].end")
        chunk_numbers = expand_chunk_number_range(start=start, end=end)
        required_ranges.append(
            RequiredSectionRange(
                document=document,
                start=start,
                end=end,
                chunk_numbers=tuple(chunk_numbers),
            )
        )
    return tuple(required_ranges)


def expand_chunk_number_range(*, start: str, end: str) -> list[str]:
    """Expand one inclusive chunk_number range.

    The range syntax is strict about shared prefixes and leaf formats. It
    supports numeric leaf values such as ``B6.3.1`` through ``B6.3.6`` and
    alphabetic suffix ranges on the same numeric base, such as ``B4.1.9A``
    through ``B4.1.9E``.
    """
    start_parts = _parse_chunk_number_parts(start)
    end_parts = _parse_chunk_number_parts(end)
    if start_parts == end_parts:
        return [start]
    if len(start_parts) != len(end_parts):
        message = f"Unsupported chunk_number range {start!r}-{end!r}: mismatched depth"
        raise ValueError(message)
    if start_parts[:-1] != end_parts[:-1]:
        message = f"Unsupported chunk_number range {start!r}-{end!r}: ranges must share a prefix"
        raise ValueError(message)

    prefix = ".".join(str(part) for part in start_parts[:-1])
    return _expand_chunk_number_leaf_range(
        start=start,
        end=end,
        prefix=prefix,
        start_leaf=start_parts[-1],
        end_leaf=end_parts[-1],
    )


def _expand_chunk_number_leaf_range(*, start: str, end: str, prefix: str, start_leaf: str, end_leaf: str) -> list[str]:
    if start_leaf.isdigit() and end_leaf.isdigit():
        return _expand_numeric_leaf_range(start=start, end=end, prefix=prefix, start_leaf=start_leaf, end_leaf=end_leaf)

    start_label = _parse_leaf_label(start_leaf)
    end_label = _parse_leaf_label(end_leaf)
    if start_label is None or end_label is None:
        message = f"Unsupported chunk_number range {start!r}-{end!r}: expected numeric leaf values or matching alphabetic prefix/suffix ranges"
        raise ValueError(message)
    if start_label.prefix != end_label.prefix:
        message = f"Unsupported chunk_number range {start!r}-{end!r}: leaf prefixes must match"
        raise ValueError(message)
    if start_label.suffix is not None and start_label.numeric_base != end_label.numeric_base and end_label.suffix is not None:
        message = f"Unsupported chunk_number range {start!r}-{end!r}: cross-number ranges cannot start with an alphabetic suffix"
        raise ValueError(message)
    if start_label.suffix is not None and start_label.numeric_base != end_label.numeric_base and end_label.suffix is None:
        return _expand_suffixed_to_numeric_leaf_range(start=start, end=end, prefix=prefix, start_label=start_label, end_label=end_label)

    return _expand_numeric_like_leaf_range(start=start, end=end, prefix=prefix, start_label=start_label, end_label=end_label)


@dataclass(frozen=True)
class _LeafLabel:
    prefix: str
    numeric_base: int
    suffix: str | None = None


def _parse_leaf_label(value: str) -> _LeafLabel | None:
    match = re.fullmatch(r"(?P<prefix>[A-Z]*)(?P<numeric_base>\d+)(?P<suffix>[A-Z]?)", value)
    if match is None:
        return None
    suffix = match.group("suffix") or None
    return _LeafLabel(
        prefix=match.group("prefix"),
        numeric_base=int(match.group("numeric_base")),
        suffix=suffix,
    )


def _expand_numeric_like_leaf_range(*, start: str, end: str, prefix: str, start_label: _LeafLabel, end_label: _LeafLabel) -> list[str]:
    start_order = _leaf_suffix_order(start_label.suffix)
    end_order = _leaf_suffix_order(end_label.suffix)
    if (start_label.numeric_base, start_order) > (end_label.numeric_base, end_order):
        message = f"Unsupported chunk_number range {start!r}-{end!r}: start must be <= end"
        raise ValueError(message)

    values: list[str] = []
    extends_past_suffixed_leaf = start_label.suffix is not None and end_label.suffix is None and start_label.numeric_base < end_label.numeric_base
    for numeric_base in range(start_label.numeric_base, end_label.numeric_base + 1):
        is_start_base = numeric_base == start_label.numeric_base
        is_end_base = numeric_base == end_label.numeric_base

        suffix_start = start_order if is_start_base else 0
        suffix_end = 26 if is_start_base and extends_past_suffixed_leaf else end_order if is_end_base else 0
        if suffix_start > suffix_end:
            message = f"Unsupported chunk_number range {start!r}-{end!r}: start must be <= end"
            raise ValueError(message)

        for suffix_order in range(suffix_start, suffix_end + 1):
            rendered_leaf = _render_leaf_label_component(
                prefix=start_label.prefix,
                numeric_base=numeric_base,
                suffix=_leaf_suffix_from_order(suffix_order),
            )
            values.append(f"{prefix}.{rendered_leaf}" if prefix else rendered_leaf)
    return values


def _expand_suffixed_to_numeric_leaf_range(*, start: str, end: str, prefix: str, start_label: _LeafLabel, end_label: _LeafLabel) -> list[str]:
    values: list[str] = []
    start_order = _leaf_suffix_order(start_label.suffix)
    if (start_label.numeric_base, start_order) > (end_label.numeric_base, 0):
        message = f"Unsupported chunk_number range {start!r}-{end!r}: start must be <= end"
        raise ValueError(message)

    for numeric_base in range(start_label.numeric_base, end_label.numeric_base + 1):
        if numeric_base == start_label.numeric_base:
            suffix_start = start_order
            suffix_end = 26
        else:
            suffix_start = 0
            suffix_end = 0
        if numeric_base == end_label.numeric_base:
            suffix_end = 0
        if suffix_start > suffix_end:
            message = f"Unsupported chunk_number range {start!r}-{end!r}: start must be <= end"
            raise ValueError(message)
        for suffix_order in range(suffix_start, suffix_end + 1):
            rendered_leaf = _render_leaf_label_component(
                prefix=start_label.prefix,
                numeric_base=numeric_base,
                suffix=_leaf_suffix_from_order(suffix_order),
            )
            values.append(f"{prefix}.{rendered_leaf}" if prefix else rendered_leaf)
    return values


def _leaf_suffix_order(value: str | None) -> int:
    if value is None:
        return 0
    order = 0
    for char in value:
        order = (order * 26) + (ord(char) - ord("A") + 1)
    return order


def _leaf_suffix_from_order(value: int) -> str | None:
    if value == 0:
        return None
    characters: list[str] = []
    current = value
    while current > 0:
        current, remainder = divmod(current - 1, 26)
        characters.append(chr(ord("A") + remainder))
    return "".join(reversed(characters))


def _render_leaf_label_component(*, prefix: str, numeric_base: int, suffix: str | None) -> str:
    suffix_text = suffix or ""
    return f"{prefix}{numeric_base}{suffix_text}"


def _expand_numeric_leaf_range(*, start: str, end: str, prefix: str, start_leaf: str, end_leaf: str) -> list[str]:
    start_leaf_number = int(start_leaf)
    end_leaf_number = int(end_leaf)
    if start_leaf_number > end_leaf_number:
        message = f"Unsupported chunk_number range {start!r}-{end!r}: start must be <= end"
        raise ValueError(message)
    return [f"{prefix}.{leaf}" if prefix else str(leaf) for leaf in range(start_leaf_number, end_leaf_number + 1)]


def _parse_chunk_number_parts(value: str) -> tuple[str, ...]:
    parts = value.split(".")
    if not parts or any(part == "" for part in parts):
        message = f"Unsupported chunk_number {value!r}: expected dotted parts"
        raise ValueError(message)
    return tuple(parts)


def _render_js_list(values: Sequence[str]) -> str:
    return "[" + ", ".join(_render_js_string(value) for value in values) + "]"


def _render_js_object(values: Mapping[str, str]) -> str:
    entries = [f"{_render_js_string(key)}: {_render_js_string(value)}" for key, value in values.items()]
    return "{" + ", ".join(entries) + "}"


def _render_js_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace("'", "\\'")
    return f"'{escaped}'"


def _require_mapping(value: object, *, context: str) -> dict[str, object]:
    if not isinstance(value, dict):
        message = f"{context}: expected a mapping"
        raise TypeError(message)
    for key in value:
        if not isinstance(key, str):
            message = f"{context}: expected string keys"
            raise TypeError(message)
    return cast("dict[str, object]", value)


def _require_sequence(value: object, *, context: str) -> list[object]:
    if not isinstance(value, list):
        message = f"{context}: expected a sequence"
        raise TypeError(message)
    return cast("list[object]", value)


def _require_str(value: object, *, context: str) -> str:
    if not isinstance(value, str):
        message = f"{context}: expected a string"
        raise TypeError(message)
    return value
