#!/usr/bin/env python3
"""Promptfoo wrapper for IFRS Expert.

Canonical Promptfoo `exec:` contract:
  argv[1] = rendered prompt
  argv[2] = provider options JSON
  argv[3] = context JSON

This wrapper reads the question from argv[1] and reads per-test mode from
argv[3].test.options.mode when available.
"""

from __future__ import annotations

import json
import subprocess
import sys
from typing import Final

CANNED_RESPONSE: Final[str] = json.dumps(
    {
        "assumptions_fr": [
            "La question porte sur des comptes consolidés IFRS.",
            "Le dividende intragroupe a été comptabilisé en créance.",
        ],
        "recommendation": {
            "answer": "oui_sous_conditions",
            "justification": "Une documentation de couverture peut être envisagée sous IFRS 9 si l'analyse pertinente est celle d'un élément monétaire intragroupe reconnu créant une exposition de change résiduelle au niveau consolidé et si les exigences de documentation, de désignation et d'efficacité sont respectées.",
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


def _load_context() -> dict[str, object]:
    if len(sys.argv) < 4:
        return {}

    try:
        raw_context = json.loads(sys.argv[3])
    except json.JSONDecodeError:
        return {}

    return raw_context if isinstance(raw_context, dict) else {}


def _extract_mode(context: dict[str, object]) -> str | None:
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
    stripped_prompt = prompt.strip()
    if mode is None:
        return stripped_prompt

    prefix = f"{mode} "
    if stripped_prompt.startswith(prefix):
        return stripped_prompt[len(prefix) :]

    return stripped_prompt


def _run_live(question: str) -> tuple[int, str]:
    result = subprocess.run(
        ["uv", "run", "python", "-m", "src.cli", "answer", "-k", "5", "--min-score", "0.3"],
        input=question,
        capture_output=True,
        text=True,
        timeout=120,
    )

    if result.returncode != 0:
        stderr_lines = result.stderr.strip().splitlines() if result.stderr else []
        error_lines = [line for line in stderr_lines if line.startswith("Error:")]
        error_message = error_lines[0] if error_lines else "Error: Command failed"
        return 1, json.dumps({"error": error_message}, ensure_ascii=False)

    output = result.stdout.strip()
    if not output:
        return 1, json.dumps({"error": "Error: Empty response from CLI"}, ensure_ascii=False)

    return 0, output


def main() -> int:
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Error: Missing prompt argument"}, ensure_ascii=False))
        return 1

    prompt = sys.argv[1]
    context = _load_context()
    mode = _extract_mode(context)
    if mode is None:
        print(json.dumps({"error": "Error: Missing mode in Promptfoo test options"}, ensure_ascii=False))
        return 1

    question = _extract_question(prompt, mode)
    if not question:
        print(json.dumps({"error": "Error: Missing question text"}, ensure_ascii=False))
        return 1

    if mode == "canned":
        print(CANNED_RESPONSE)
        return 0

    exit_code, payload = _run_live(question)
    print(payload)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
