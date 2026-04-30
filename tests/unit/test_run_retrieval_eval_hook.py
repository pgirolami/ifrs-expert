"""Tests for the retrieval eval pre-commit hook helper."""

from __future__ import annotations

import importlib.util
import sys
import subprocess
from datetime import UTC, datetime
from pathlib import Path
from types import ModuleType


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _script_path() -> Path:
    return _repo_root() / "scripts" / "run_retrieval_eval_hook.py"


def _load_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("tests_run_retrieval_eval_hook_module", _script_path())
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class RecordingCommandRunner:
    """Record make invocations and return configurable exit codes."""

    def __init__(self, return_codes: list[int]) -> None:
        self._return_codes = return_codes
        self.calls: list[tuple[list[str], Path, dict[str, str]]] = []

    def __call__(self, command: list[str], cwd: Path, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
        self.calls.append((command, cwd, env))
        return_code = self._return_codes[len(self.calls) - 1] if len(self.calls) - 1 < len(self._return_codes) else 0
        return subprocess.CompletedProcess(args=command, returncode=return_code, stdout="", stderr="")


def test_hook_runner_cleans_stale_temp_dirs_and_removes_successful_run(tmp_path: Path) -> None:
    """Runner should delete stale dirs up front and remove the temp root on success."""
    module = _load_module()

    storage_root = tmp_path / "retrieval-evals"
    stale_dir = storage_root / "stale-run"
    stale_nested = stale_dir / "experiment"
    stale_nested.mkdir(parents=True)
    fresh_file = storage_root / "leftover.txt"
    fresh_file.write_text("stale", encoding="utf-8")
    command_runner = RecordingCommandRunner([0, 0])

    runner = module.RetrievalEvalHookRunner(
        project_root=tmp_path,
        storage_root=storage_root,
        now_fn=lambda: datetime(2026, 4, 30, 12, 0, 0, tzinfo=UTC),
        command_runner=command_runner,
    )

    exit_code = runner.run(
        [
            module.RetrievalEvalPair(family="Q1", variant="Q1.4"),
            module.RetrievalEvalPair(family="Q1", variant="Q1.5"),
        ]
    )

    assert exit_code == 0
    assert not stale_dir.exists()
    assert not fresh_file.exists()
    assert not storage_root.exists() or not any(storage_root.iterdir())
    assert len(command_runner.calls) == 2


def test_hook_runner_keeps_temp_root_on_failure_and_stops_later_pairs(tmp_path: Path) -> None:
    """Runner should preserve the current temp root if a pair fails."""
    module = _load_module()

    storage_root = tmp_path / "retrieval-evals"
    command_runner = RecordingCommandRunner([0, 7, 0])
    runner = module.RetrievalEvalHookRunner(
        project_root=tmp_path,
        storage_root=storage_root,
        now_fn=lambda: datetime(2026, 4, 30, 12, 0, 0, tzinfo=UTC),
        command_runner=command_runner,
    )

    exit_code = runner.run(
        [
            module.RetrievalEvalPair(family="Q1", variant="Q1.4"),
            module.RetrievalEvalPair(family="Q1", variant="Q1.5"),
            module.RetrievalEvalPair(family="Q1", variant="Q1.2"),
        ]
    )

    assert exit_code == 7
    assert len(command_runner.calls) == 2
    _, _, env = command_runner.calls[0]
    temp_experiment_dir = Path(env["EXPERIMENT_DIR"])
    assert temp_experiment_dir.is_absolute()
    assert temp_experiment_dir.parent.exists()


def test_parse_pairs_trims_whitespace() -> None:
    """Parser should normalize whitespace in family and variant pairs."""
    module = _load_module()
    pairs = module.parse_pairs([[" Q1 ", " Q1.4 "], ["Q1", "Q1.5"]])
    assert pairs == [
        module.RetrievalEvalPair(family="Q1", variant="Q1.4"),
        module.RetrievalEvalPair(family="Q1", variant="Q1.5"),
    ]
