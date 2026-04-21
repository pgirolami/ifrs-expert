"""Normalize document_type values in IFRS processed JSON sidecars.

This script updates the JSON files in-place. It is intended for manual use on a
local processed-capture directory such as ~/Downloads/ifrs-expert/processed.
"""

from __future__ import annotations

import argparse
import json
import logging
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULT_ROOT = Path.home() / "Downloads" / "ifrs-expert" / "processed"
DOC_UID_COMPONENT_INDEX = 1


@dataclass(frozen=True)
class UpdateResult:
    """Summary of a single JSON file update."""

    path: Path
    old_document_type: str | None
    new_document_type: str
    changed: bool


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Normalize document_type values in processed IFRS JSON sidecars")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help=f"Directory containing processed JSON files (default: {DEFAULT_ROOT})")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing files")
    return parser


def _extract_doc_uid(path: Path) -> str:
    stem = path.stem
    parts = stem.split("--")
    if len(parts) > DOC_UID_COMPONENT_INDEX:
        return parts[DOC_UID_COMPONENT_INDEX]
    return stem


def _infer_document_type(doc_uid: str) -> str | None:
    suffix_map: dict[str, dict[str, str]] = {
        "ifrs": {"": "IFRS-S", "-bc": "IFRS-BC", "-ie": "IFRS-IE", "-ig": "IFRS-IG"},
        "ias": {"": "IAS-S", "-bc": "IAS-BC", "-ie": "IAS-IE", "-ig": "IAS-IG"},
        "ifric": {"": "IFRIC", "-bc": "IFRIC-BC", "-ie": "IFRIC-IE", "-ig": "IFRIC-IG"},
        "sic": {"": "SIC"},
        "ps": {"": "PS"},
        "navis": {"": "NAVIS"},
    }

    normalized_uid = doc_uid.lower()
    for prefix, mapping in suffix_map.items():
        if not normalized_uid.startswith(prefix):
            continue
        for suffix, document_type in sorted(mapping.items(), key=lambda item: len(item[0]), reverse=True):
            if suffix == "":
                return document_type
            if normalized_uid.endswith(suffix):
                return document_type
    return None


def _normalize_json_file(path: Path, *, dry_run: bool) -> UpdateResult:
    raw_text = path.read_text(encoding="utf-8")
    data = json.loads(raw_text)
    if not isinstance(data, dict):
        message = f"Expected top-level JSON object in {path}"
        raise TypeError(message)

    doc_uid = _extract_doc_uid(path)
    inferred_document_type = _infer_document_type(doc_uid)
    if inferred_document_type is None:
        message = f"Could not infer document_type for doc_uid={doc_uid} ({path})"
        raise ValueError(message)

    old_document_type_value = data.get("document_type")
    old_document_type = str(old_document_type_value) if old_document_type_value is not None else None
    changed = old_document_type != inferred_document_type
    if changed:
        data["document_type"] = inferred_document_type
        logger.info(f"{path.name}: {old_document_type!r} -> {inferred_document_type!r}")
        if not dry_run:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return UpdateResult(
        path=path,
        old_document_type=old_document_type,
        new_document_type=inferred_document_type,
        changed=changed,
    )


def main() -> int:
    """Normalize document_type fields in all JSON sidecars under the target root."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = _build_parser()
    args = parser.parse_args()

    root = args.root
    if not root.exists():
        message = f"Root directory not found: {root}"
        raise FileNotFoundError(message)

    json_paths = sorted(root.glob("*.json"))
    logger.info(f"Scanning {len(json_paths)} JSON files under {root}")

    changed_count = 0
    for json_path in json_paths:
        result = _normalize_json_file(json_path, dry_run=args.dry_run)
        if result.changed:
            changed_count += 1

    action = "would update" if args.dry_run else "updated"
    logger.info(f"{action} {changed_count} file(s) out of {len(json_paths)} scanned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
