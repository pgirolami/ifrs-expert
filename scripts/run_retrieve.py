"""Promptfoo wrapper for retrieval-only regression runs.

Promptfoo passes:
  argv[1] = rendered prompt
  argv[2] = provider options JSON
  argv[3] = context JSON

This wrapper forwards the question to `src.cli retrieve --json` so the
retrieval suite can run without any LLM calls.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Final

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[1]
PROMPT_ARG_INDEX: Final[int] = 1
PROVIDER_OPTIONS_ARG_INDEX: Final[int] = 2
CONTEXT_ARG_INDEX: Final[int] = 3
MIN_ARG_COUNT_FOR_PROVIDER_OPTIONS: Final[int] = 3
MIN_ARG_COUNT_FOR_CONTEXT: Final[int] = 4
PROMPTFOO_ARTIFACTS_DIR_ENV: Final[str] = "PROMPTFOO_ARTIFACTS_DIR"
QUERY_EMBEDDING_ARTIFACT_NAME: Final[str] = "query_embedding.txt"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.retrieval.query_embedding import build_query_embedding_text

if TYPE_CHECKING:
    from collections.abc import Sequence


@dataclass(frozen=True)
class ExtractionOptions:
    """Options extracted from Promptfoo provider config."""

    policy_config: str
    retrieval_policy: str
    base_path: Path | None = None


def _write_stdout(payload: str) -> None:
    """Write one UTF-8 payload line to stdout."""
    sys.stdout.buffer.write(payload.encode("utf-8") + b"\n")


def _error_payload(message: str) -> str:
    """Build a JSON error payload."""
    return json.dumps({"error": message}, ensure_ascii=False)


def _load_json_arg(index: int) -> dict[str, object]:
    """Load a positional JSON argument when available."""
    if len(sys.argv) < index + 1:
        return {}
    raw_value = sys.argv[index]
    try:
        parsed = json.loads(raw_value)
    except json.JSONDecodeError as error:
        raise ValueError(f"Failed to parse argv[{index}] as JSON: {error}") from error
    if not isinstance(parsed, dict):
        raise ValueError(f"Expected argv[{index}] to be a JSON object, got {type(parsed).__name__}")
    for key in parsed:
        if not isinstance(key, str):
            raise ValueError(f"Expected argv[{index}] keys to be strings")
    return parsed


def _as_object_mapping(value: object) -> dict[str, object]:
    """Return a string-keyed mapping when the value is a dict."""
    if not isinstance(value, dict):
        raise ValueError(f"Expected dict, got {type(value).__name__}")
    for key in value:
        if not isinstance(key, str):
            raise ValueError(f"Expected string keys, got {type(key).__name__}")
    return value


def _iter_candidate_mappings(provider_options: dict[str, object], context: dict[str, object]) -> list[dict[str, object]]:
    """Return mappings that may contain provider overrides."""
    mappings: list[dict[str, object]] = [provider_options]

    for candidate in (provider_options.get("config"), provider_options.get("env")):
        if isinstance(candidate, dict):
            mappings.append(candidate)

    try:
        test_data = _as_object_mapping(context.get("test"))
    except ValueError:
        test_data = None
    if test_data is not None:
        options = test_data.get("options")
        if isinstance(options, dict):
            mappings.append(options)

    try:
        prompt_data = _as_object_mapping(context.get("prompt"))
    except ValueError:
        prompt_data = None
    if prompt_data is not None:
        prompt_config = prompt_data.get("config")
        if isinstance(prompt_config, dict):
            mappings.append(prompt_config)

    return mappings


def _extract_required_string(mapping: dict[str, object], keys: Sequence[str]) -> str | None:
    """Extract a non-empty string from a mapping using fallback keys."""
    for key in keys:
        value = mapping.get(key)
        if not isinstance(value, str):
            continue
        stripped_value = value.strip()
        if stripped_value:
            return stripped_value
    return None


def _extract_options(provider_options: dict[str, object], context: dict[str, object]) -> ExtractionOptions:
    """Extract mandatory policy and retrieval policy values."""
    policy_config: str | None = None
    retrieval_policy: str | None = None
    base_path: Path | None = None

    for mapping in _iter_candidate_mappings(provider_options, context):
        if policy_config is None:
            policy_config = _extract_required_string(mapping, ("policy-config", "policy_config"))
        if retrieval_policy is None:
            retrieval_policy = _extract_required_string(mapping, ("retrieval-policy", "retrieval_policy"))
        if base_path is None:
            base_path_value = _extract_required_string(mapping, ("basePath", "base_path"))
            if base_path_value is not None:
                base_path = Path(base_path_value)

    if policy_config is None:
        raise ValueError("Missing required provider option: policy-config")
    if retrieval_policy is None:
        raise ValueError("Missing required provider option: retrieval-policy")

    return ExtractionOptions(policy_config=policy_config, retrieval_policy=retrieval_policy, base_path=base_path)


def _resolve_policy_config_path(policy_config: str, base_path: Path | None) -> Path:
    """Resolve policy-config relative to Promptfoo's basePath when needed."""
    path = Path(policy_config)
    if path.is_absolute():
        return path
    if base_path is not None:
        return base_path / path
    return PROJECT_ROOT / path


def _resolve_artifacts_dir() -> Path | None:
    """Return the Promptfoo artifacts directory when configured."""
    raw_value = os.environ.get(PROMPTFOO_ARTIFACTS_DIR_ENV)
    if raw_value is None:
        return None
    stripped_value = raw_value.strip()
    if not stripped_value:
        return None
    return Path(stripped_value)


def _clean_metadata_value(value: object, fallback: str) -> str:
    """Normalize Promptfoo metadata values for filesystem use."""
    if not isinstance(value, str):
        return fallback
    cleaned = value.strip().removesuffix("¤").strip()
    if not cleaned:
        return fallback
    return cleaned


def _safe_path_segment(value: str, fallback: str) -> str:
    """Convert a metadata value into a filesystem-friendly segment."""
    normalized = re.sub(r"[^a-zA-Z0-9._-]+", "-", value).strip("-._")
    return normalized or fallback


def _extract_test_metadata(context: dict[str, object]) -> dict[str, str]:
    """Extract Promptfoo test metadata for artifact naming."""
    test_data = context.get("test")
    if not isinstance(test_data, dict):
        return {}

    metadata = test_data.get("metadata")
    if not isinstance(metadata, dict):
        return {}

    return {
        "family": _clean_metadata_value(metadata.get("family"), "unknown-family"),
        "variant": _clean_metadata_value(metadata.get("variant"), "unknown-variant"),
        "question_path": _clean_metadata_value(metadata.get("question_path"), "unknown-question"),
    }


def _write_query_embedding_artifact(question: str, context: dict[str, object]) -> None:
    """Persist the embedded query text for later inspection."""
    artifacts_dir = _resolve_artifacts_dir()
    if artifacts_dir is None:
        return

    metadata = _extract_test_metadata(context)
    family_segment = _safe_path_segment(metadata.get("family", "unknown-family"), "unknown-family")
    variant_segment = _safe_path_segment(metadata.get("variant", "unknown-variant"), "unknown-variant")
    artifact_dir = artifacts_dir / family_segment / variant_segment
    artifact_path = artifact_dir / QUERY_EMBEDDING_ARTIFACT_NAME

    query_embedding = build_query_embedding_text(question)
    artifact_dir.mkdir(parents=True, exist_ok=True)
    artifact_path.write_text(query_embedding.embedding_text.rstrip() + "\n", encoding="utf-8")


def _run_retrieve(question: str, options: ExtractionOptions, context: dict[str, object]) -> tuple[int, str]:
    """Run the real retrieval pipeline and capture stdout."""
    policy_config_path = _resolve_policy_config_path(options.policy_config, options.base_path)
    command = [
        sys.executable,
        "-m",
        "src.cli",
        "retrieve",
        "--policy-config",
        str(policy_config_path),
        "--retrieval-policy",
        options.retrieval_policy,
        "--json",
    ]
    try:
        _write_query_embedding_artifact(question=question, context=context)
    except Exception:
        # The artifact is for debugging only; retrieval should still run.
        pass
    completed_process = subprocess.run(  # noqa: S603
        command,
        cwd=PROJECT_ROOT,
        input=question,
        text=True,
        capture_output=True,
        check=False,
        env=os.environ.copy(),
    )
    if completed_process.returncode != 0:
        error_text = completed_process.stderr.strip() or completed_process.stdout.strip() or f"retrieve failed with exit code {completed_process.returncode}"
        return completed_process.returncode, _error_payload(error_text)

    stdout_text = completed_process.stdout.strip()
    if not stdout_text:
        return 1, _error_payload("Error: Empty response from retrieve command")
    return 0, stdout_text


def main() -> int:
    """Run the Promptfoo wrapper entry point."""
    if len(sys.argv) <= PROMPT_ARG_INDEX:
        _write_stdout(_error_payload("Error: Missing prompt argument"))
        return 1

    prompt = sys.argv[PROMPT_ARG_INDEX]
    question = prompt.strip()
    if not question:
        _write_stdout(_error_payload("Error: Missing question text"))
        return 1

    try:
        provider_options = _load_json_arg(PROVIDER_OPTIONS_ARG_INDEX) if len(sys.argv) >= MIN_ARG_COUNT_FOR_PROVIDER_OPTIONS else {}
        context = _load_json_arg(CONTEXT_ARG_INDEX) if len(sys.argv) >= MIN_ARG_COUNT_FOR_CONTEXT else {}
        options = _extract_options(provider_options=provider_options, context=context)
    except ValueError as error:
        _write_stdout(_error_payload(f"Error: {error}"))
        return 1

    exit_code, payload = _run_retrieve(question=question, options=options, context=context)
    _write_stdout(payload)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
