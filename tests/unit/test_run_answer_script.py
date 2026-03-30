"""Regression tests for the Promptfoo wrapper script."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def test_run_answer_script_supports_direct_execution_from_repo_root() -> None:
    """The Promptfoo wrapper should run as a direct script from the repo root."""
    repo_root = Path(__file__).resolve().parents[2]
    script_path = repo_root / "scripts" / "run_answer.py"
    context = json.dumps({"test": {"options": {"mode": "canned"}}}, ensure_ascii=False)

    result = subprocess.run(
        [sys.executable, str(script_path), "Question de test", "{}", context],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr

    payload = json.loads(result.stdout)
    assert payload["recommendation"]["answer"] == "oui_sous_conditions"
    assert len(payload["approaches"]) == 3
