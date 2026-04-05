"""Tests for the Promptfoo experiment runner."""

from __future__ import annotations

import importlib.util
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from types import ModuleType


def _repo_root() -> Path:
    """Return the repository root."""
    return Path(__file__).resolve().parents[2]


def _script_path() -> Path:
    """Return the Promptfoo experiment runner path."""
    return _repo_root() / "scripts" / "run_promptfoo_eval.py"


def _load_run_promptfoo_eval_module() -> ModuleType:
    """Load scripts/run_promptfoo_eval.py as a module for unit tests."""
    spec = importlib.util.spec_from_file_location("tests_run_promptfoo_eval_module", _script_path())
    if spec is None:
        msg = "Expected a module spec for scripts/run_promptfoo_eval.py"
        raise RuntimeError(msg)
    if spec.loader is None:
        msg = "Expected a loader for scripts/run_promptfoo_eval.py"
        raise RuntimeError(msg)

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@dataclass
class FakeCompletedProcess:
    """Minimal subprocess result for runner tests."""

    returncode: int = 0


class RecordingCommandRunner:
    """Record subprocess invocations made by the experiment runner."""

    def __init__(self) -> None:
        self.calls: list[tuple[list[str], dict[str, str], Path]] = []

    def __call__(self, command: list[str], env: dict[str, str], cwd: Path) -> FakeCompletedProcess:
        self.calls.append((command, env, cwd))
        return FakeCompletedProcess()


def test_promptfoo_eval_runner_creates_timestamped_run_layout(tmp_path: Path) -> None:
    """The runner should archive each eval under the promptfoo experiment folder."""
    run_promptfoo_eval = _load_run_promptfoo_eval_module()
    runner = run_promptfoo_eval.PromptfooEvalRunner(
        project_root=tmp_path,
        experiment_dir=tmp_path / "experiments" / "promptfoo_regression",
        now_fn=lambda: datetime(2026, 4, 4, 9, 15, 0, tzinfo=UTC),
        command_runner=RecordingCommandRunner(),
    )

    run_layout = runner._build_run_layout(description="Q1 live mistral")

    assert run_layout.run_dir == tmp_path / "experiments" / "promptfoo_regression" / "runs" / "2026-04-04_09-15-00_q1-live-mistral"
    assert run_layout.artifacts_dir == run_layout.run_dir / "artifacts"
    assert run_layout.promptfoo_config_dir == tmp_path / "experiments" / "promptfoo_regression" / ".promptfoo"


def test_build_promptfoo_args_adds_family_variant_and_provider_filters() -> None:
    """Shortcut CLI options should translate into Promptfoo filter arguments."""
    run_promptfoo_eval = _load_run_promptfoo_eval_module()

    promptfoo_args = run_promptfoo_eval.build_promptfoo_args(
        base_args=["--no-cache"],
        family="Q1",
        variant="Q1.0",
        provider="Mistral Large 3",
    )

    assert promptfoo_args == [
        "--filter-metadata",
        "family=Q1",
        "--filter-metadata",
        "variant=Q1.0",
        "--filter-targets",
        "Mistral Large 3",
        "--no-cache",
    ]


def test_resolve_experiment_dir_prefixes_repo_experiments_root() -> None:
    """Bare experiment names should resolve under the repository experiments directory."""
    run_promptfoo_eval = _load_run_promptfoo_eval_module()

    resolved_path = run_promptfoo_eval.resolve_experiment_dir(
        project_root=Path("/repo"),
        experiment_dir=Path("promptfoo_regression"),
    )

    assert resolved_path == Path("/repo") / "experiments" / "promptfoo_regression"


def test_parse_args_requires_experiment_dir() -> None:
    """The CLI should require an explicit experiment directory."""
    run_promptfoo_eval = _load_run_promptfoo_eval_module()

    try:
        run_promptfoo_eval.parse_args([])
    except SystemExit as error:
        assert error.code == 2
    else:
        raise AssertionError("Expected parse_args to require --experiment-dir")


def test_promptfoo_eval_runner_sets_experiment_config_dir_and_artifact_env(tmp_path: Path) -> None:
    """The runner should expose the artifact directory and experiment-local Promptfoo config directory."""
    run_promptfoo_eval = _load_run_promptfoo_eval_module()
    command_runner = RecordingCommandRunner()
    runner = run_promptfoo_eval.PromptfooEvalRunner(
        project_root=tmp_path,
        experiment_dir=tmp_path / "experiments" / "promptfoo_regression",
        now_fn=lambda: datetime(2026, 4, 4, 9, 15, 0, tzinfo=UTC),
        command_runner=command_runner,
    )

    exit_code = runner.run(
        promptfoo_args=["--filter-metadata", "family=Q1"],
        description="Q1 live mistral",
    )

    assert exit_code == 0
    assert len(command_runner.calls) == 2

    build_command, build_env, build_cwd = command_runner.calls[0]
    assert build_command == ["npm", "run", "eval:build"]
    assert build_cwd == tmp_path
    assert build_env[run_promptfoo_eval.PROMPTFOO_ARTIFACTS_DIR_ENV].endswith("artifacts")
    assert build_env[run_promptfoo_eval.PROMPTFOO_CONFIG_DIR_ENV].endswith(".promptfoo")

    eval_command, eval_env, eval_cwd = command_runner.calls[1]
    assert eval_command[:5] == ["npm", "exec", "--", "promptfoo", "eval"]
    assert "--description" in eval_command
    assert "Q1 live mistral" in eval_command
    assert "-o" not in eval_command
    assert eval_command[-2:] == ["--filter-metadata", "family=Q1"]
    assert eval_cwd == tmp_path
    assert eval_env[run_promptfoo_eval.PROMPTFOO_ARTIFACTS_DIR_ENV] == build_env[run_promptfoo_eval.PROMPTFOO_ARTIFACTS_DIR_ENV]
    assert eval_env[run_promptfoo_eval.PROMPTFOO_CONFIG_DIR_ENV] == build_env[run_promptfoo_eval.PROMPTFOO_CONFIG_DIR_ENV]


def test_promptfoo_eval_runner_uses_explicit_config_dir_when_provided(tmp_path: Path) -> None:
    """An explicit Promptfoo config dir should override the default experiment-local path."""
    run_promptfoo_eval = _load_run_promptfoo_eval_module()
    custom_promptfoo_config_dir = tmp_path / "custom-promptfoo"
    runner = run_promptfoo_eval.PromptfooEvalRunner(
        project_root=tmp_path,
        experiment_dir=tmp_path / "experiments" / "promptfoo_regression",
        promptfoo_config_dir=custom_promptfoo_config_dir,
        now_fn=lambda: datetime(2026, 4, 4, 9, 15, 0, tzinfo=UTC),
        command_runner=RecordingCommandRunner(),
    )

    run_layout = runner._build_run_layout(description="Q1 live mistral")

    assert run_layout.promptfoo_config_dir == custom_promptfoo_config_dir
