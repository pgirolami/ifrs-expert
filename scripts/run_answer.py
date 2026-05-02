"""Promptfoo wrapper for IFRS Expert.

Canonical Promptfoo `exec:` contract:
  argv[1] = rendered prompt
  argv[2] = provider options JSON
  argv[3] = context JSON

This wrapper reads the question from argv[1], can read provider-level options
from argv[2], and reads per-test mode from argv[3].test.options.mode when
available. When Promptfoo does not pass a mode, the wrapper defaults to live.
"""

from __future__ import annotations

import json
import logging
import os
import re
import sys
from dataclasses import dataclass
from dataclasses import field as dataclass_field
from pathlib import Path
from typing import TYPE_CHECKING, Final, cast

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from dotenv import load_dotenv  # noqa: E402

from src.answer_artifacts import save_answer_command_result  # noqa: E402
from src.commands import AnswerOptions  # noqa: E402
from src.commands.answer import create_answer_command  # noqa: E402
from src.logging_config import setup_logging  # noqa: E402
from src.policy import load_policy_catalog, resolve_retrieval_policy  # noqa: E402

if TYPE_CHECKING:
    from src.models.answer_command_result import AnswerCommandResult

logger = logging.getLogger(__name__)

PROMPT_ARG_INDEX: Final[int] = 1
PROVIDER_OPTIONS_ARG_INDEX: Final[int] = 2
CONTEXT_ARG_INDEX: Final[int] = 3
MIN_ARG_COUNT_FOR_PROVIDER_OPTIONS: Final[int] = 3
MIN_ARG_COUNT_FOR_CONTEXT: Final[int] = 4
PROMPTFOO_ARTIFACTS_DIR_ENV: Final[str] = "PROMPTFOO_ARTIFACTS_DIR"

CANNED_JUSTIFICATION: Final[str] = (
    "Une documentation de couverture peut être envisagée sous IFRS 9 si l'analyse "
    "pertinente est celle d'un élément monétaire intragroupe reconnu créant une "
    "exposition de change résiduelle au niveau consolidé et si les exigences de "
    "documentation, de désignation et d'efficacité sont respectées."
)

CANNED_RESPONSE: Final[str] = json.dumps(
    {
        "assumptions_fr": [
            "La question porte sur des comptes consolidés IFRS.",
            "Le dividende intragroupe a été comptabilisé en créance.",
        ],
        "recommendation": {
            "answer": "oui_sous_conditions",
            "justification": CANNED_JUSTIFICATION,
        },
        "approaches": [
            {
                "normalized_label": "cash_flow_hedge",
                "applicability": "non",
                "references": ["IFRS 9.6.3.6"],
            },
            {
                "normalized_label": "fair_value_hedge",
                "applicability": "oui_sous_conditions",
                "references": ["IFRS 9.6.3.6", "IFRS 9.6.4.1"],
            },
            {
                "normalized_label": "net_investment_hedge",
                "applicability": "non",
                "references": ["IFRIC 16.8", "IFRIC 16.11"],
            },
        ],
    },
    ensure_ascii=False,
)


def _write_stdout(payload: str) -> None:
    """Write one UTF-8 payload line to stdout."""
    sys.stdout.buffer.write(payload.encode("utf-8") + b"\n")


def _error_payload(message: str) -> str:
    """Build a JSON error payload."""
    return json.dumps({"error": message}, ensure_ascii=False)


def _load_provider_options() -> dict[str, object]:
    """Load Promptfoo provider options from argv when available."""
    if len(sys.argv) < MIN_ARG_COUNT_FOR_PROVIDER_OPTIONS:
        logger.debug("No provider options argv, using empty config")
        return {}

    try:
        raw_provider_options = json.loads(sys.argv[PROVIDER_OPTIONS_ARG_INDEX])
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse provider options JSON: {e}")

    if not isinstance(raw_provider_options, dict):
        raise ValueError(f"Provider options must be a JSON object, got {type(raw_provider_options).__name__}")

    return raw_provider_options


def _load_context() -> dict[str, object]:
    """Load Promptfoo context from argv when available."""
    if len(sys.argv) < MIN_ARG_COUNT_FOR_CONTEXT:
        logger.debug("No context argv, using empty context")
        return {}

    try:
        raw_context = json.loads(sys.argv[CONTEXT_ARG_INDEX])
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse context JSON: {e}")

    if not isinstance(raw_context, dict):
        raise ValueError(f"Context must be a JSON object, got {type(raw_context).__name__}")

    return raw_context


def _as_object_mapping(value: object) -> dict[str, object]:
    """Return a dict[str, object] view when the value is a string-keyed dict."""
    if not isinstance(value, dict):
        raise ValueError(f"Expected dict, got {type(value).__name__}")
    for key in value:
        if not isinstance(key, str):
            raise ValueError(f"Dict keys must be str, got {type(key).__name__}")
    return cast("dict[str, object]", value)


def _extract_mode(context: dict[str, object]) -> str:
    """Extract the eval mode from Promptfoo context, defaulting to live."""
    try:
        test_data = _as_object_mapping(context.get("test"))
    except ValueError:
        test_data = None

    if test_data is not None:
        try:
            options = _as_object_mapping(test_data.get("options"))
        except ValueError:
            options = None
        if options is not None:
            mode = options.get("mode")
            if isinstance(mode, str) and mode in {"canned", "live"}:
                return mode

    try:
        prompt_data = _as_object_mapping(context.get("prompt"))
    except ValueError:
        prompt_data = None
    if prompt_data is not None:
        try:
            prompt_config = _as_object_mapping(prompt_data.get("config"))
        except ValueError:
            prompt_config = None
        if prompt_config is not None:
            mode = prompt_config.get("mode")
            if isinstance(mode, str) and mode in {"canned", "live"}:
                return mode

    return "live"


def _extract_question(prompt: str, mode: str) -> str:
    """Extract the question text from the rendered prompt."""
    stripped_prompt = prompt.strip()
    prefix = f"{mode} "
    if stripped_prompt.startswith(prefix):
        return stripped_prompt[len(prefix) :]

    return stripped_prompt


@dataclass
class ExtractionOptions:
    """Options extracted from Promptfoo provider options or context mappings."""

    policy_config: str
    retrieval_policy: str
    output_dir: str | None = None
    base_path: Path | None = None
    config_kv: dict[str, str] = dataclass_field(default_factory=dict)


AliasKey = str | tuple[str, ...]


def _iter_alias_keys(keys: AliasKey) -> tuple[str, ...]:
    """Normalize one key or tuple of keys into a tuple for lookup."""
    if isinstance(keys, str):
        return (keys,)
    return keys


def _extract_raw_value_from_mapping(mapping: dict[str, object], keys: AliasKey) -> tuple[object | None, bool]:
    """Extract the first matching raw value from a mapping using alias keys.

    Returns (value, found). found=False means the key is absent.
    """
    for key in _iter_alias_keys(keys):
        if key in mapping:
            return mapping[key], True
    return None, False


def _extract_int_from_mapping(mapping: dict[str, object], key: AliasKey, fallback: int) -> int:
    """Extract an integer override from one mapping."""
    value, found = _extract_raw_value_from_mapping(mapping, key)
    if not found:
        return fallback
    if not isinstance(value, int | float):
        raise ValueError(f"Expected int for {key}, got {type(value).__name__}")
    if value < 0:
        raise ValueError(f"Expected non-negative int for {key}, got {value}")
    return int(value)


def _extract_float_from_mapping(mapping: dict[str, object], key: AliasKey, fallback: float) -> float:
    """Extract a float override from one mapping."""
    value, found = _extract_raw_value_from_mapping(mapping, key)
    if not found:
        return fallback
    if not isinstance(value, int | float):
        raise ValueError(f"Expected float for {key}, got {type(value).__name__}")
    if not (0.0 <= float(value) <= 1.0):
        raise ValueError(f"Expected float in [0, 1] for {key}, got {value}")
    return float(value)


def _extract_optional_float_from_mapping(mapping: dict[str, object], key: AliasKey, fallback: float | None) -> float | None:
    """Extract an optional float override from one mapping."""
    value, found = _extract_raw_value_from_mapping(mapping, key)
    if not found:
        return fallback
    if not isinstance(value, int | float):
        raise ValueError(f"Expected float for {key}, got {type(value).__name__}")
    if not (0.0 <= float(value) <= 1.0):
        raise ValueError(f"Expected float in [0, 1] for {key}, got {value}")
    return float(value)


def _extract_bool_from_mapping(mapping: dict[str, object], key: AliasKey, *, fallback: bool) -> bool:
    """Extract a boolean override from one mapping."""
    value, found = _extract_raw_value_from_mapping(mapping, key)
    if not found:
        return fallback
    if not isinstance(value, bool):
        raise ValueError(f"Expected bool for {key}, got {type(value).__name__}")
    return value


def _extract_optional_string_from_mapping(
    mapping: dict[str, object],
    key: AliasKey,
    fallback: str | None,
) -> str | None:
    """Extract an optional non-empty string override from one mapping."""
    value, found = _extract_raw_value_from_mapping(mapping, key)
    if not found:
        return fallback
    if not isinstance(value, str):
        raise ValueError(f"Expected str for {key}, got {type(value).__name__}")
    stripped_value = value.strip()
    if not stripped_value:
        raise ValueError(f"Expected non-empty string for {key}")
    return stripped_value


def _build_config_kv(mapping: dict[str, object]) -> dict[str, str]:
    """Build a dict of string key-value pairs from a mapping, excluding nested dicts, id and basePath."""
    result: dict[str, str] = {}
    for key, value in mapping.items():
        if key in {"basePath", "id"}:
            continue
        if isinstance(value, bool):
            result[str(key)] = "true" if value else "false"
            continue
        if isinstance(value, (str, int, float)):
            result[str(key)] = str(value)
    return result


def _merge_config_kv(base: dict[str, str], overlay: dict[str, str]) -> dict[str, str]:
    """Merge overlay into base, overlay wins on key collision."""
    merged = dict(base)
    merged.update(overlay)
    return merged


def _build_effective_config_kv(
    options: ExtractionOptions,
    llm_provider: str | None,
) -> dict[str, str]:
    """Build concise artifact config metadata from effective options."""
    result: dict[str, str] = {
        "policy-config": options.policy_config,
        "retrieval-policy": options.retrieval_policy,
    }
    if llm_provider is not None:
        result["llm_provider"] = llm_provider
    return result


def _extract_required_policy_config(mapping: dict[str, object]) -> str | None:
    """Extract policy-config value from one mapping when present."""
    raw_value, found = _extract_raw_value_from_mapping(mapping, ("policy-config", "policy_config"))
    if not found:
        return None
    if not isinstance(raw_value, str):
        raise ValueError(f"Expected str for policy-config, got {type(raw_value).__name__}")
    policy_config = raw_value.strip()
    if not policy_config:
        raise ValueError("Expected non-empty string for policy-config")
    return policy_config


def _extract_required_retrieval_policy(mapping: dict[str, object]) -> str | None:
    """Extract retrieval-policy value from one mapping when present."""
    raw_value, found = _extract_raw_value_from_mapping(mapping, ("retrieval-policy", "retrieval_policy"))
    if not found:
        return None
    if not isinstance(raw_value, str):
        raise ValueError(f"Expected str for retrieval-policy, got {type(raw_value).__name__}")
    retrieval_policy = raw_value.strip()
    if not retrieval_policy:
        raise ValueError("Expected non-empty string for retrieval-policy")
    return retrieval_policy


def _extract_options(
    provider_options: dict[str, object],
    context: dict[str, object],
) -> ExtractionOptions:
    """Extract mandatory policy-config and runtime options."""
    output_dir: str | None = None
    policy_config: str | None = None
    retrieval_policy: str | None = None
    base_path: Path | None = None

    for mapping in _candidate_llm_provider_mappings(provider_options, context):
        if policy_config is None:
            policy_config = _extract_required_policy_config(mapping)
        if retrieval_policy is None:
            retrieval_policy = _extract_required_retrieval_policy(mapping)
        output_dir = _extract_optional_string_from_mapping(mapping, ("output-dir", "output_dir"), output_dir)
        if base_path is None:
            base_path_value = _extract_optional_string_from_mapping(mapping, ("basePath", "base_path"), None)
            if base_path_value is not None:
                base_path = Path(base_path_value)

    if policy_config is None:
        message = "Missing required provider option: policy-config"
        raise ValueError(message)
    if retrieval_policy is None:
        message = "Missing required provider option: retrieval-policy"
        raise ValueError(message)

    options = ExtractionOptions(
        policy_config=policy_config,
        retrieval_policy=retrieval_policy,
        output_dir=output_dir,
        base_path=base_path,
    )
    options.config_kv = _build_effective_config_kv(
        options=options,
        llm_provider=_extract_llm_provider(provider_options, context),
    )
    return options


def _resolve_path_relative_to_base_path(path_value: str, base_path: Path | None) -> Path:
    """Resolve a Promptfoo path against basePath when the path is relative."""
    path = Path(path_value)
    if path.is_absolute():
        return path
    if base_path is not None:
        return base_path / path
    return PROJECT_ROOT / path


def _extract_llm_provider_from_mapping(mapping: dict[str, object]) -> str | None:
    """Extract an LLM provider override from one mapping."""
    for key in ("llm_provider", "llmProvider", "LLM_PROVIDER"):
        value = mapping.get(key)
        if isinstance(value, str):
            provider = value.strip()
            if provider:
                return provider
    return None


def _append_mapping_if_dict(
    mappings: list[dict[str, object]],
    value: object,
) -> None:
    """Append a value when it is a dict[str, object]; skip silently otherwise."""
    if value is None:
        return
    try:
        mapping = _as_object_mapping(value)
    except ValueError:
        return
    mappings.append(mapping)


def _candidate_llm_provider_mappings(
    provider_options: dict[str, object],
    context: dict[str, object],
) -> list[dict[str, object]]:
    """Return candidate mappings that may contain an LLM provider override."""
    mappings: list[dict[str, object]] = [provider_options]
    _append_mapping_if_dict(mappings, provider_options.get("config"))
    _append_mapping_if_dict(mappings, provider_options.get("env"))

    test_data = context.get("test")
    if test_data is not None:
        try:
            test_mapping = _as_object_mapping(test_data)
        except ValueError:
            test_mapping = None
        if test_mapping is not None:
            _append_mapping_if_dict(mappings, test_mapping.get("options"))

    prompt_data = context.get("prompt")
    if prompt_data is not None:
        try:
            prompt_mapping = _as_object_mapping(prompt_data)
        except ValueError:
            prompt_mapping = None
        if prompt_mapping is not None:
            _append_mapping_if_dict(mappings, prompt_mapping.get("config"))

    return mappings


def _extract_llm_provider(
    provider_options: dict[str, object],
    context: dict[str, object],
) -> str | None:
    """Extract an LLM provider override, preferring provider options."""
    for mapping in _candidate_llm_provider_mappings(provider_options, context):
        provider_override = _extract_llm_provider_from_mapping(mapping)
        if provider_override is not None:
            return provider_override

    return None


def _apply_llm_provider_override(llm_provider: str | None) -> None:
    """Apply an LLM provider override to the process environment."""
    if llm_provider is None:
        return

    os.environ["LLM_PROVIDER"] = llm_provider


def _slugify_component(value: str) -> str:
    """Normalize one path component for Promptfoo artifacts."""
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized or "default"


def _build_config_dirname(config_kv: dict[str, str]) -> str:
    """Build the config portion of the artifact directory name from key-value pairs."""
    if not config_kv:
        return _slugify_component(os.environ.get("LLM_PROVIDER", "default"))

    parts = [f"{key}={value}" for key, value in sorted(config_kv.items())]
    return "__".join(parts)


def _artifact_output_dir(
    context: dict[str, object],
    config_kv: dict[str, str],
) -> Path:
    """Build the Promptfoo artifact output directory from context metadata and config kv."""
    base_dir = os.environ.get(PROMPTFOO_ARTIFACTS_DIR_ENV)
    if base_dir is None or not base_dir.strip():
        raise ValueError(f"Missing required environment variable: {PROMPTFOO_ARTIFACTS_DIR_ENV}")

    family = "unknown-family"
    variant = "unknown-variant"
    test_data = _as_object_mapping(context.get("test"))
    if test_data is not None:
        metadata = _as_object_mapping(test_data.get("metadata"))
        if metadata is not None:
            family_value = metadata.get("family")
            if isinstance(family_value, str) and family_value.strip():
                # Strip the '¤' delimiter used for exact promptfoo filtering
                family = family_value.strip().rstrip("¤")
            variant_value = metadata.get("variant")
            if isinstance(variant_value, str) and variant_value.strip():
                # Strip the '¤' delimiter used for exact promptfoo filtering
                variant = variant_value.strip().rstrip("¤")

    config_component = _build_config_dirname(config_kv)
    output_dir = Path(base_dir) / family / variant / config_component

    repeat_index = context.get("repeatIndex")
    if isinstance(repeat_index, int) and repeat_index > 0:
        output_dir = output_dir / f"repeat-{repeat_index}"

    return output_dir


def _write_promptfoo_artifacts(
    result: AnswerCommandResult,
    context: dict[str, object],
    config_kv: dict[str, str],
) -> None:
    """Persist answer artifacts when Promptfoo archiving is enabled."""
    try:
        output_dir = _artifact_output_dir(context=context, config_kv=config_kv)
    except ValueError as error:
        logger.info(f"Skipping Promptfoo answer artifact export: {error}")
        return
    save_answer_command_result(result=result, output_dir=output_dir)
    logger.info(f"Saved Promptfoo answer artifacts to {output_dir}")


def _run_live(
    question: str,
    llm_provider: str | None,
    context: dict[str, object],
    options: ExtractionOptions,
) -> tuple[int, str]:
    """Run the real answer pipeline for one question."""
    load_dotenv()
    _apply_llm_provider_override(llm_provider)
    setup_logging()

    policy_config_path = _resolve_path_relative_to_base_path(options.policy_config, options.base_path)
    output_dir = _resolve_path_relative_to_base_path(options.output_dir, options.base_path) if options.output_dir is not None else None
    logger.debug(f"Resolved Promptfoo answer paths: policy_config_path={policy_config_path}, output_dir={output_dir}, base_path={options.base_path}")
    policy_catalog = load_policy_catalog(policy_config_path)
    retrieval_policy = resolve_retrieval_policy(policy_catalog, options.retrieval_policy)
    command = create_answer_command(
        query=question,
        options=AnswerOptions(
            policy=retrieval_policy,
            output_dir=output_dir,
        ),
    )
    result = command.execute()
    _write_promptfoo_artifacts(result=result, context=context, config_kv=options.config_kv)

    if result.error is not None:
        logger.error(f"Answer pipeline failed during Promptfoo live run: {result.error}")
        return 1, _error_payload(result.error)

    if result.prompt_b_raw_response is not None:
        return 0, result.prompt_b_raw_response

    if result.prompt_b_memo_markdown is not None:
        return 0, result.prompt_b_memo_markdown

    return 1, _error_payload("Error: Empty response from CLI")


def main() -> int:
    """Run the Promptfoo wrapper entry point."""
    if len(sys.argv) <= PROMPT_ARG_INDEX:
        _write_stdout(_error_payload("Error: Missing prompt argument"))
        return 1

    setup_logging()
    try:
        prompt = sys.argv[PROMPT_ARG_INDEX]
        provider_options = _load_provider_options()
        context = _load_context()
        mode = _extract_mode(context)
        question = _extract_question(prompt, mode)
        if not question:
            _write_stdout(_error_payload("Error: Missing question text"))
            return 1

        if mode == "canned":
            _write_stdout(CANNED_RESPONSE)
            return 0

        llm_provider = _extract_llm_provider(provider_options, context)
        extraction_options = _extract_options(provider_options, context)
        exit_code, payload = _run_live(question, llm_provider, context, extraction_options)
    except Exception as error:
        logger.exception(f"Promptfoo answer wrapper failed: {error}")
        _write_stdout(_error_payload(f"Error: {error}"))
        return 1

    _write_stdout(payload)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
