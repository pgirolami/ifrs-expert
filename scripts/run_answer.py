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
from src.commands.constants import (  # noqa: E402
    DEFAULT_D_FOR_IAS_DOCUMENTS,
    DEFAULT_D_FOR_IFRIC_DOCUMENTS,
    DEFAULT_D_FOR_IFRS_DOCUMENTS,
    DEFAULT_D_FOR_PS_DOCUMENTS,
    DEFAULT_D_FOR_SIC_DOCUMENTS,
    DEFAULT_EXPAND,
    DEFAULT_FULL_DOC_THRESHOLD,
    DEFAULT_MIN_SCORE_FOR_IAS_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_IFRIC_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_IFRS_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_PS_DOCUMENTS,
    DEFAULT_MIN_SCORE_FOR_SIC_DOCUMENTS,
    DEFAULT_RETRIEVAL_K,
    DEFAULT_RETRIEVE_CONTENT_MIN_SCORE,
    DEFAULT_RETRIEVE_DOCUMENT_D,
)
from src.logging_config import setup_logging  # noqa: E402

if TYPE_CHECKING:
    from src.models.answer_command_result import AnswerCommandResult

logger = logging.getLogger(__name__)

PROMPT_ARG_INDEX: Final[int] = 1
PROVIDER_OPTIONS_ARG_INDEX: Final[int] = 2
CONTEXT_ARG_INDEX: Final[int] = 3
MIN_ARG_COUNT_FOR_PROVIDER_OPTIONS: Final[int] = 3
MIN_ARG_COUNT_FOR_CONTEXT: Final[int] = 4
DEFAULT_K: Final[int] = DEFAULT_RETRIEVAL_K
DEFAULT_MIN_SCORE: Final[float] = DEFAULT_RETRIEVE_CONTENT_MIN_SCORE
DEFAULT_RETRIEVAL_MODE: Final[str] = "text"
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
        return {}

    try:
        raw_provider_options = json.loads(sys.argv[PROVIDER_OPTIONS_ARG_INDEX])
    except json.JSONDecodeError:
        return {}

    return raw_provider_options if isinstance(raw_provider_options, dict) else {}


def _load_context() -> dict[str, object]:
    """Load Promptfoo context from argv when available."""
    if len(sys.argv) < MIN_ARG_COUNT_FOR_CONTEXT:
        return {}

    try:
        raw_context = json.loads(sys.argv[CONTEXT_ARG_INDEX])
    except json.JSONDecodeError:
        return {}

    return raw_context if isinstance(raw_context, dict) else {}


def _as_object_mapping(value: object) -> dict[str, object] | None:
    """Return a dict[str, object] view when the value is a string-keyed dict."""
    if not isinstance(value, dict):
        return None
    for key in value:
        if not isinstance(key, str):
            return None
    return cast("dict[str, object]", value)


def _extract_mode(context: dict[str, object]) -> str:
    """Extract the eval mode from Promptfoo context, defaulting to live."""
    test_data = _as_object_mapping(context.get("test"))
    if test_data is not None:
        options = _as_object_mapping(test_data.get("options"))
        if options is not None:
            mode = options.get("mode")
            if isinstance(mode, str) and mode in {"canned", "live"}:
                return mode

    prompt_data = _as_object_mapping(context.get("prompt"))
    if prompt_data is not None:
        prompt_config = _as_object_mapping(prompt_data.get("config"))
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

    k: int = DEFAULT_K
    min_score: float = DEFAULT_MIN_SCORE
    d: int = DEFAULT_RETRIEVE_DOCUMENT_D
    doc_min_score: float | None = None
    ifrs_d: int = DEFAULT_D_FOR_IFRS_DOCUMENTS
    ias_d: int = DEFAULT_D_FOR_IAS_DOCUMENTS
    ifric_d: int = DEFAULT_D_FOR_IFRIC_DOCUMENTS
    sic_d: int = DEFAULT_D_FOR_SIC_DOCUMENTS
    ps_d: int = DEFAULT_D_FOR_PS_DOCUMENTS
    ifrs_min_score: float = DEFAULT_MIN_SCORE_FOR_IFRS_DOCUMENTS
    ias_min_score: float = DEFAULT_MIN_SCORE_FOR_IAS_DOCUMENTS
    ifric_min_score: float = DEFAULT_MIN_SCORE_FOR_IFRIC_DOCUMENTS
    sic_min_score: float = DEFAULT_MIN_SCORE_FOR_SIC_DOCUMENTS
    ps_min_score: float = DEFAULT_MIN_SCORE_FOR_PS_DOCUMENTS
    content_min_score: float | None = None
    expand_to_section: bool = False
    expand: int = DEFAULT_EXPAND
    full_doc_threshold: int = DEFAULT_FULL_DOC_THRESHOLD
    retrieval_mode: str = DEFAULT_RETRIEVAL_MODE
    output_dir: str | None = None
    save_all: bool = False
    # Key-value pairs for artifact directory naming
    config_kv: dict[str, str] = dataclass_field(default_factory=dict)


AliasKey = str | tuple[str, ...]


def _iter_alias_keys(keys: AliasKey) -> tuple[str, ...]:
    """Normalize one key or tuple of keys into a tuple for lookup."""
    if isinstance(keys, str):
        return (keys,)
    return keys


def _extract_raw_value_from_mapping(mapping: dict[str, object], keys: AliasKey) -> object | None:
    """Extract the first matching raw value from a mapping using alias keys."""
    for key in _iter_alias_keys(keys):
        if key in mapping:
            return mapping[key]
    return None


def _extract_int_from_mapping(mapping: dict[str, object], key: AliasKey, fallback: int) -> int:
    """Extract an integer override from one mapping."""
    value = _extract_raw_value_from_mapping(mapping, key)
    if isinstance(value, int | float) and value >= 0:
        return int(value)
    return fallback


def _extract_float_from_mapping(mapping: dict[str, object], key: AliasKey, fallback: float) -> float:
    """Extract a float override from one mapping."""
    value = _extract_raw_value_from_mapping(mapping, key)
    if isinstance(value, int | float) and 0.0 <= value <= 1.0:
        return float(value)
    return fallback


def _extract_optional_float_from_mapping(mapping: dict[str, object], key: AliasKey, fallback: float | None) -> float | None:
    """Extract an optional float override from one mapping."""
    value = _extract_raw_value_from_mapping(mapping, key)
    if isinstance(value, int | float) and 0.0 <= value <= 1.0:
        return float(value)
    return fallback


def _extract_bool_from_mapping(mapping: dict[str, object], key: AliasKey, *, fallback: bool) -> bool:
    """Extract a boolean override from one mapping."""
    value = _extract_raw_value_from_mapping(mapping, key)
    if isinstance(value, bool):
        return value
    return fallback


def _extract_optional_string_from_mapping(
    mapping: dict[str, object],
    key: AliasKey,
    fallback: str | None,
) -> str | None:
    """Extract an optional non-empty string override from one mapping."""
    value = _extract_raw_value_from_mapping(mapping, key)
    if isinstance(value, str):
        stripped_value = value.strip()
        if stripped_value:
            return stripped_value
    return fallback


def _extract_retrieval_mode_from_mapping(mapping: dict[str, object], fallback: str) -> str:
    """Extract a retrieval mode override from one mapping."""
    value = _extract_raw_value_from_mapping(mapping, ("retrieval-mode", "retrieval_mode"))
    if isinstance(value, str) and value in {"text", "titles", "documents"}:
        return value
    return fallback


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
    """Build concise artifact config metadata from effective non-default options."""
    default_options = ExtractionOptions()
    result: dict[str, str] = {}
    if llm_provider is not None:
        result["llm_provider"] = llm_provider

    option_pairs: tuple[tuple[str, object | None, object | None], ...] = (
        ("k", options.k, default_options.k),
        ("min-score", options.min_score, default_options.min_score),
        ("d", options.d, default_options.d),
        ("doc-min-score", options.doc_min_score, default_options.doc_min_score),
        ("ifrs-d", options.ifrs_d, default_options.ifrs_d),
        ("ias-d", options.ias_d, default_options.ias_d),
        ("ifric-d", options.ifric_d, default_options.ifric_d),
        ("sic-d", options.sic_d, default_options.sic_d),
        ("ps-d", options.ps_d, default_options.ps_d),
        ("ifrs-min-score", options.ifrs_min_score, default_options.ifrs_min_score),
        ("ias-min-score", options.ias_min_score, default_options.ias_min_score),
        ("ifric-min-score", options.ifric_min_score, default_options.ifric_min_score),
        ("sic-min-score", options.sic_min_score, default_options.sic_min_score),
        ("ps-min-score", options.ps_min_score, default_options.ps_min_score),
        ("content-min-score", options.content_min_score, default_options.content_min_score),
        ("expand-to-section", options.expand_to_section, default_options.expand_to_section),
        ("expand", options.expand, default_options.expand),
        ("full-doc-threshold", options.full_doc_threshold, default_options.full_doc_threshold),
        ("retrieval-mode", options.retrieval_mode, default_options.retrieval_mode),
        ("save-all", options.save_all, default_options.save_all),
    )

    for key, value, default_value in option_pairs:
        if value is None or value == default_value:
            continue
        if isinstance(value, bool):
            result[key] = "true" if value else "false"
            continue
        result[key] = str(value)

    return result


def _extract_options(
    provider_options: dict[str, object],
    context: dict[str, object],
) -> ExtractionOptions:
    """Extract AnswerOptions overrides from Promptfoo provider options and context."""
    k = DEFAULT_K
    min_score = DEFAULT_MIN_SCORE
    d = DEFAULT_RETRIEVE_DOCUMENT_D
    doc_min_score: float | None = None
    ifrs_d = DEFAULT_D_FOR_IFRS_DOCUMENTS
    ias_d = DEFAULT_D_FOR_IAS_DOCUMENTS
    ifric_d = DEFAULT_D_FOR_IFRIC_DOCUMENTS
    sic_d = DEFAULT_D_FOR_SIC_DOCUMENTS
    ps_d = DEFAULT_D_FOR_PS_DOCUMENTS
    ifrs_min_score = DEFAULT_MIN_SCORE_FOR_IFRS_DOCUMENTS
    ias_min_score = DEFAULT_MIN_SCORE_FOR_IAS_DOCUMENTS
    ifric_min_score = DEFAULT_MIN_SCORE_FOR_IFRIC_DOCUMENTS
    sic_min_score = DEFAULT_MIN_SCORE_FOR_SIC_DOCUMENTS
    ps_min_score = DEFAULT_MIN_SCORE_FOR_PS_DOCUMENTS
    content_min_score: float | None = None
    expand_to_section = False
    expand = DEFAULT_EXPAND
    full_doc_threshold = DEFAULT_FULL_DOC_THRESHOLD
    retrieval_mode = DEFAULT_RETRIEVAL_MODE
    output_dir: str | None = None
    save_all = False

    for mapping in _candidate_llm_provider_mappings(provider_options, context):
        k = _extract_int_from_mapping(mapping, "k", k)
        min_score = _extract_float_from_mapping(mapping, ("min-score", "min_score"), min_score)
        d = _extract_int_from_mapping(mapping, "d", d)
        doc_min_score = _extract_optional_float_from_mapping(mapping, ("doc-min-score", "doc_min_score"), doc_min_score)
        ifrs_d = _extract_int_from_mapping(mapping, ("ifrs-d", "ifrs_d"), ifrs_d)
        ias_d = _extract_int_from_mapping(mapping, ("ias-d", "ias_d"), ias_d)
        ifric_d = _extract_int_from_mapping(mapping, ("ifric-d", "ifric_d"), ifric_d)
        sic_d = _extract_int_from_mapping(mapping, ("sic-d", "sic_d"), sic_d)
        ps_d = _extract_int_from_mapping(mapping, ("ps-d", "ps_d"), ps_d)
        ifrs_min_score = _extract_float_from_mapping(mapping, ("ifrs-min-score", "ifrs_min_score"), ifrs_min_score)
        ias_min_score = _extract_float_from_mapping(mapping, ("ias-min-score", "ias_min_score"), ias_min_score)
        ifric_min_score = _extract_float_from_mapping(mapping, ("ifric-min-score", "ifric_min_score"), ifric_min_score)
        sic_min_score = _extract_float_from_mapping(mapping, ("sic-min-score", "sic_min_score"), sic_min_score)
        ps_min_score = _extract_float_from_mapping(mapping, ("ps-min-score", "ps_min_score"), ps_min_score)
        content_min_score = _extract_optional_float_from_mapping(
            mapping,
            ("content-min-score", "content_min_score"),
            content_min_score,
        )
        expand_to_section = _extract_bool_from_mapping(
            mapping,
            ("expand-to-section", "expand_to_section"),
            fallback=expand_to_section,
        )
        # Support both 'e' and 'expand' keys.
        expand = _extract_int_from_mapping(mapping, "e", _extract_int_from_mapping(mapping, "expand", expand))
        full_doc_threshold = _extract_int_from_mapping(
            mapping,
            ("f", "full-doc-threshold", "full_doc_threshold"),
            full_doc_threshold,
        )
        retrieval_mode = _extract_retrieval_mode_from_mapping(mapping, retrieval_mode)
        output_dir = _extract_optional_string_from_mapping(mapping, ("output-dir", "output_dir"), output_dir)
        save_all = _extract_bool_from_mapping(mapping, ("save-all", "save_all"), fallback=save_all)

    options = ExtractionOptions(
        k=k,
        min_score=min_score,
        d=d,
        doc_min_score=doc_min_score,
        ifrs_d=ifrs_d,
        ias_d=ias_d,
        ifric_d=ifric_d,
        sic_d=sic_d,
        ps_d=ps_d,
        ifrs_min_score=ifrs_min_score,
        ias_min_score=ias_min_score,
        ifric_min_score=ifric_min_score,
        sic_min_score=sic_min_score,
        ps_min_score=ps_min_score,
        content_min_score=content_min_score,
        expand_to_section=expand_to_section,
        expand=expand,
        full_doc_threshold=full_doc_threshold,
        retrieval_mode=retrieval_mode,
        output_dir=output_dir,
        save_all=save_all,
    )
    options.config_kv = _build_effective_config_kv(
        options=options,
        llm_provider=_extract_llm_provider(provider_options, context),
    )
    return options


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
    """Append a value when it is a dict[str, object]."""
    mapping = _as_object_mapping(value)
    if mapping is not None:
        mappings.append(mapping)


def _candidate_llm_provider_mappings(
    provider_options: dict[str, object],
    context: dict[str, object],
) -> list[dict[str, object]]:
    """Return candidate mappings that may contain an LLM provider override."""
    mappings: list[dict[str, object]] = [provider_options]
    _append_mapping_if_dict(mappings, provider_options.get("config"))
    _append_mapping_if_dict(mappings, provider_options.get("env"))

    test_data = _as_object_mapping(context.get("test"))
    if test_data is not None:
        _append_mapping_if_dict(mappings, test_data.get("options"))

    prompt_data = _as_object_mapping(context.get("prompt"))
    if prompt_data is not None:
        _append_mapping_if_dict(mappings, prompt_data.get("config"))

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
) -> Path | None:
    """Build the Promptfoo artifact output directory from context metadata and config kv."""
    base_dir = os.environ.get(PROMPTFOO_ARTIFACTS_DIR_ENV)
    if base_dir is None or not base_dir.strip():
        return None

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
    output_dir = _artifact_output_dir(context=context, config_kv=config_kv)
    if output_dir is None:
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

    command = create_answer_command(
        query=question,
        options=AnswerOptions(
            k=options.k,
            min_score=options.min_score,
            d=options.d,
            doc_min_score=options.doc_min_score,
            ifrs_d=options.ifrs_d,
            ias_d=options.ias_d,
            ifric_d=options.ifric_d,
            sic_d=options.sic_d,
            ps_d=options.ps_d,
            ifrs_min_score=options.ifrs_min_score,
            ias_min_score=options.ias_min_score,
            ifric_min_score=options.ifric_min_score,
            sic_min_score=options.sic_min_score,
            ps_min_score=options.ps_min_score,
            content_min_score=options.content_min_score,
            expand_to_section=options.expand_to_section,
            expand=options.expand,
            full_doc_threshold=options.full_doc_threshold,
            retrieval_mode=options.retrieval_mode,
            output_dir=(Path(options.output_dir) if options.output_dir is not None else None),
            save_all=options.save_all,
        ),
    )
    result = command.execute()
    _write_promptfoo_artifacts(result=result, context=context, config_kv=options.config_kv)

    if result.error is not None:
        logger.error(f"Answer pipeline failed during Promptfoo live run: {result.error}")
        return 1, _error_payload(result.error)

    if result.prompt_b_raw_response is not None:
        return 0, result.prompt_b_raw_response

    if result.prompt_b_markdown is not None:
        return 0, result.prompt_b_markdown

    return 1, _error_payload("Error: Empty response from CLI")


def main() -> int:
    """Run the Promptfoo wrapper entry point."""
    if len(sys.argv) <= PROMPT_ARG_INDEX:
        _write_stdout(_error_payload("Error: Missing prompt argument"))
        return 1

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
    _write_stdout(payload)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
