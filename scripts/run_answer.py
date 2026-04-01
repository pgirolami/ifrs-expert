"""Promptfoo wrapper for IFRS Expert.

Canonical Promptfoo `exec:` contract:
  argv[1] = rendered prompt
  argv[2] = provider options JSON
  argv[3] = context JSON

This wrapper reads the question from argv[1], can read provider-level options
from argv[2], and reads per-test mode from argv[3].test.options.mode when
available.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Final

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from dotenv import load_dotenv

from src.commands import AnswerOptions
from src.commands.answer import create_answer_command
from src.logging_config import setup_logging

PROMPT_ARG_INDEX: Final[int] = 1
PROVIDER_OPTIONS_ARG_INDEX: Final[int] = 2
CONTEXT_ARG_INDEX: Final[int] = 3
MIN_ARG_COUNT_FOR_PROVIDER_OPTIONS: Final[int] = 3
MIN_ARG_COUNT_FOR_CONTEXT: Final[int] = 4
DEFAULT_K: Final[int] = 5
DEFAULT_MIN_SCORE: Final[float] = 0.55
DEFAULT_EXPAND: Final[int] = 5

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
        "operational_points_fr": [
            "Vérifier si la créance est bien un élément monétaire intragroupe.",
            "Documenter formellement la relation de couverture et la méthode d'évaluation de l'efficacité.",
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


def _extract_mode(context: dict[str, object]) -> str | None:
    """Extract the eval mode from Promptfoo context."""
    test_data = context.get("test")
    if isinstance(test_data, dict):
        options = test_data.get("options")
        if isinstance(options, dict):
            mode = options.get("mode")
            if isinstance(mode, str) and mode in {"canned", "live"}:
                return mode

    prompt_data = context.get("prompt")
    if isinstance(prompt_data, dict):
        prompt_config = prompt_data.get("config")
        if isinstance(prompt_config, dict):
            mode = prompt_config.get("mode")
            if isinstance(mode, str) and mode in {"canned", "live"}:
                return mode

    return None


def _extract_question(prompt: str, mode: str | None) -> str:
    """Extract the question text from the rendered prompt."""
    stripped_prompt = prompt.strip()
    if mode is None:
        return stripped_prompt

    prefix = f"{mode} "
    if stripped_prompt.startswith(prefix):
        return stripped_prompt[len(prefix) :]

    return stripped_prompt


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
    if isinstance(value, dict):
        mappings.append(value)


def _candidate_llm_provider_mappings(
    provider_options: dict[str, object],
    context: dict[str, object],
) -> list[dict[str, object]]:
    """Return candidate mappings that may contain an LLM provider override."""
    mappings: list[dict[str, object]] = [provider_options]
    _append_mapping_if_dict(mappings, provider_options.get("config"))
    _append_mapping_if_dict(mappings, provider_options.get("env"))

    test_data = context.get("test")
    if isinstance(test_data, dict):
        _append_mapping_if_dict(mappings, test_data.get("options"))

    prompt_data = context.get("prompt")
    if isinstance(prompt_data, dict):
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


def _run_live(question: str, llm_provider: str | None) -> tuple[int, str]:
    """Run the real answer pipeline for one question."""
    load_dotenv()
    _apply_llm_provider_override(llm_provider)
    setup_logging()

    command = create_answer_command(
        query=question,
        options=AnswerOptions(k=DEFAULT_K, min_score=DEFAULT_MIN_SCORE, expand=DEFAULT_EXPAND),
    )
    result = command.execute()

    if result.error is not None:
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
    if mode is None:
        _write_stdout(_error_payload("Error: Missing mode in Promptfoo test options"))
        return 1

    question = _extract_question(prompt, mode)
    if not question:
        _write_stdout(_error_payload("Error: Missing question text"))
        return 1

    if mode == "canned":
        _write_stdout(CANNED_RESPONSE)
        return 0

    llm_provider = _extract_llm_provider(provider_options, context)
    exit_code, payload = _run_live(question, llm_provider)
    _write_stdout(payload)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
