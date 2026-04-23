"""Shared parsing helpers for declarative retrieval expectations."""

from __future__ import annotations

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

    The range syntax is strict about shared prefixes and numeric leaf values,
    but it allows an alphanumeric prefix in earlier components, such as
    ``B6.3.1`` through ``B6.3.6``.
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
    if not start_parts[-1].isdigit() or not end_parts[-1].isdigit():
        message = f"Unsupported chunk_number range {start!r}-{end!r}: expected numeric leaf values"
        raise ValueError(message)

    start_leaf = int(start_parts[-1])
    end_leaf = int(end_parts[-1])
    if start_leaf > end_leaf:
        message = f"Unsupported chunk_number range {start!r}-{end!r}: start must be <= end"
        raise ValueError(message)

    prefix = ".".join(str(part) for part in start_parts[:-1])
    return [f"{prefix}.{leaf}" if prefix else str(leaf) for leaf in range(start_leaf, end_leaf + 1)]


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
