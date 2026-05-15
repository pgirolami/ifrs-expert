"""Tests for Promptfoo experiment runner."""

from __future__ import annotations

import importlib.util
import json
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from types import ModuleType


def _repo_root() -> Path:
    """Return repository root."""
    return Path(__file__).resolve().parents[2]


def _script_path() -> Path:
    """Return Promptfoo experiment runner path."""
    return _repo_root() / "scripts" / "run_promptfoo_eval.py"


def _load_module() -> ModuleType:
    """Load scripts/run_promptfoo_eval.py as module."""
    spec = importlib.util.spec_from_file_location("tests_run_promptfoo_eval_module", _script_path())
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@dataclass
class FakeCompletedProcess:
    """Minimal subprocess result."""

    returncode: int = 0


class RecordingCommandRunner:
    """Record subprocess calls from runner."""

    def __init__(self) -> None:
        self.calls: list[tuple[list[str], dict[str, str], Path]] = []

    def __call__(self, command: list[str], env: dict[str, str], cwd: Path) -> FakeCompletedProcess:
        self.calls.append((command, env, cwd))
        return FakeCompletedProcess()


def test_build_promptfoo_args_adds_filters() -> None:
    module = _load_module()

    args = module.build_promptfoo_args(
        base_args=["--no-cache"],
        family="Q1",
        variant="Q1.0",
        provider="MiniMax",
    )

    assert args == [
        "--filter-metadata",
        "family=Q1¤",
        "--filter-metadata",
        "variant=Q1.0¤",
        "--filter-targets",
        "MiniMax",
        "--no-cache",
    ]


def test_build_default_description_includes_filters() -> None:
    module = _load_module()
    description = module.build_default_description("Q1", "Q1.0", "MiniMax")
    assert description == "promptfoo eval family=Q1 variant=Q1.0 provider=MiniMax"


def test_promptfoo_eval_runner_creates_timestamped_layout(tmp_path: Path) -> None:
    module = _load_module()
    runner = module.PromptfooEvalRunner(
        project_root=tmp_path,
        experiment_dir=tmp_path / "experiments" / "promptfoo_regression",
        suite="answer",
        now_fn=lambda: datetime(2026, 4, 4, 9, 15, 0, tzinfo=UTC),
        command_runner=RecordingCommandRunner(),
    )

    layout = runner._build_run_layout(description="Q1 live")

    assert layout.run_dir == tmp_path / "experiments" / "promptfoo_regression" / "runs" / "2026-04-04_09-15-00_q1-live"
    assert layout.artifacts_dir == layout.run_dir / "artifacts"


def test_runner_sets_env_and_writes_metadata(tmp_path: Path) -> None:
    module = _load_module()
    command_runner = RecordingCommandRunner()
    runner = module.PromptfooEvalRunner(
        project_root=tmp_path,
        experiment_dir=tmp_path / "experiments" / "promptfoo_regression",
        suite="answer",
        now_fn=lambda: datetime(2026, 4, 4, 9, 15, 0, tzinfo=UTC),
        command_runner=command_runner,
    )

    # Seed expected artifact sources so archive step succeeds.
    (tmp_path / "config").mkdir(parents=True, exist_ok=True)
    (tmp_path / "prompts").mkdir(parents=True, exist_ok=True)
    (tmp_path / "config" / "policy.default.yaml").write_text("retrieval: {}", encoding="utf-8")
    (tmp_path / "config" / "en-fr-glossary.yaml").write_text("question_glossary: []", encoding="utf-8")
    (tmp_path / "prompts" / "answer_prompt_A.txt").write_text("A", encoding="utf-8")
    (tmp_path / "prompts" / "answer_prompt_B.txt").write_text("B", encoding="utf-8")

    # Patch module-level paths for isolated temp project.
    module.DEFAULT_POLICY_PATH = tmp_path / "config" / "policy.default.yaml"
    module.DEFAULT_GLOSSARY_PATH = tmp_path / "config" / "en-fr-glossary.yaml"
    module.DEFAULT_APPROACH_IDENTIFICATION_PATH = tmp_path / "prompts" / "answer_prompt_A.txt"
    module.DEFAULT_APPLICABILITY_ANALYSIS_PATH = tmp_path / "prompts" / "answer_prompt_B.txt"

    exit_code = runner.run(promptfoo_args=["--filter-metadata", "family=Q1"], description="Q1 live")

    assert exit_code == 0
    assert len(command_runner.calls) == 3

    build_command, build_env, _ = command_runner.calls[0]
    assert build_command[:3] == ["npm", "run", "eval:build"]
    assert "--suite" in build_command
    assert "answer" in build_command
    assert module.PROMPTFOO_ARTIFACTS_DIR_ENV in build_env
    assert module.PROMPTFOO_CONFIG_DIR_ENV in build_env

    run_dirs = sorted((tmp_path / "experiments" / "promptfoo_regression" / "runs").iterdir())
    run_dir = run_dirs[0]
    effective_dir = run_dir / "effective"
    assert (effective_dir / "en-fr-glossary.yaml").read_text(encoding="utf-8") == "question_glossary: []"
    metadata = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    assert metadata["description"] == "Q1 live"
    assert "archived_artifacts" in metadata
    assert "glossary" in metadata["archived_artifacts"]
    assert metadata["archived_artifacts"]["glossary"]["archived_path"].endswith("effective/en-fr-glossary.yaml")

    approach_detection_command, _, _ = command_runner.calls[2]
    assert approach_detection_command == [
        "uv",
        "run",
        "python",
        "experiments/analysis/approach_detection/generate_approach_detection_diagnostics.py",
        "--experiment",
        "experiments/promptfoo_regression",
        "--run-id",
        "2026-04-04_09-15-00_q1-live",
    ]


def test_runner_passes_retrieve_suite_to_builder(tmp_path: Path) -> None:
    """Runner should forward suite=retrieve into the build command."""
    module = _load_module()
    command_runner = RecordingCommandRunner()
    runner = module.PromptfooEvalRunner(
        project_root=tmp_path,
        experiment_dir=tmp_path / "experiments" / "promptfoo_regression",
        suite="retrieve",
        now_fn=lambda: datetime(2026, 4, 4, 9, 15, 0, tzinfo=UTC),
        command_runner=command_runner,
    )

    (tmp_path / "config").mkdir(parents=True, exist_ok=True)
    (tmp_path / "prompts").mkdir(parents=True, exist_ok=True)
    (tmp_path / "config" / "policy.default.yaml").write_text("retrieval: {}", encoding="utf-8")
    (tmp_path / "config" / "en-fr-glossary.yaml").write_text("question_glossary: []", encoding="utf-8")
    (tmp_path / "prompts" / "answer_prompt_A.txt").write_text("A", encoding="utf-8")
    (tmp_path / "prompts" / "answer_prompt_B.txt").write_text("B", encoding="utf-8")
    module.DEFAULT_POLICY_PATH = tmp_path / "config" / "policy.default.yaml"
    module.DEFAULT_GLOSSARY_PATH = tmp_path / "config" / "en-fr-glossary.yaml"
    module.DEFAULT_APPROACH_IDENTIFICATION_PATH = tmp_path / "prompts" / "answer_prompt_A.txt"
    module.DEFAULT_APPLICABILITY_ANALYSIS_PATH = tmp_path / "prompts" / "answer_prompt_B.txt"

    exit_code = runner.run(promptfoo_args=[], description="retrieve suite")

    assert exit_code == 0
    assert len(command_runner.calls) == 4

    build_command, _, _ = command_runner.calls[0]
    assert "--suite" in build_command
    assert "retrieve" in build_command

    eval_command, _, _ = command_runner.calls[1]
    assert eval_command[:4] == ["npm", "exec", "--", "promptfoo"]

    document_routing_command, _, _ = command_runner.calls[2]
    assert document_routing_command == [
        "uv",
        "run",
        "python",
        "experiments/analysis/document_routing/generate_document_routing_diagnostics.py",
        "--experiment",
        "experiments/promptfoo_regression",
        "--run-id",
        "2026-04-04_09-15-00_retrieve-suite",
    ]

    target_chunk_command, _, _ = command_runner.calls[3]
    assert target_chunk_command == [
        "uv",
        "run",
        "python",
        "experiments/analysis/target_chunk_retrieval/generate_target_chunk_retrieval_diagnostics.py",
        "--experiment",
        "experiments/promptfoo_regression",
        "--run-id",
        "2026-04-04_09-15-00_retrieve-suite",
    ]


def test_runner_supports_experiment_dirs_outside_project_root(tmp_path: Path) -> None:
    """Runner should fall back to absolute paths when experiment dirs live outside the repo root."""
    module = _load_module()
    command_runner = RecordingCommandRunner()
    project_root = tmp_path / "repo"
    experiment_dir = tmp_path / "external" / "promptfoo_regression"
    project_root.mkdir()

    (project_root / "config").mkdir(parents=True, exist_ok=True)
    (project_root / "prompts").mkdir(parents=True, exist_ok=True)
    (project_root / "config" / "policy.default.yaml").write_text("retrieval: {}", encoding="utf-8")
    (project_root / "config" / "en-fr-glossary.yaml").write_text("question_glossary: []", encoding="utf-8")
    (project_root / "prompts" / "answer_prompt_A.txt").write_text("A", encoding="utf-8")
    (project_root / "prompts" / "answer_prompt_B.txt").write_text("B", encoding="utf-8")
    module.DEFAULT_POLICY_PATH = project_root / "config" / "policy.default.yaml"
    module.DEFAULT_GLOSSARY_PATH = project_root / "config" / "en-fr-glossary.yaml"
    module.DEFAULT_APPROACH_IDENTIFICATION_PATH = project_root / "prompts" / "answer_prompt_A.txt"
    module.DEFAULT_APPLICABILITY_ANALYSIS_PATH = project_root / "prompts" / "answer_prompt_B.txt"

    runner = module.PromptfooEvalRunner(
        project_root=project_root,
        experiment_dir=experiment_dir,
        suite="answer",
        now_fn=lambda: datetime(2026, 4, 4, 9, 15, 0, tzinfo=UTC),
        command_runner=command_runner,
    )

    exit_code = runner.run(promptfoo_args=[], description="external experiment")

    assert exit_code == 0
    metadata = json.loads((experiment_dir / "runs" / "2026-04-04_09-15-00_external-experiment" / "run.json").read_text(encoding="utf-8"))
    assert metadata["artifacts_path"].startswith(str((experiment_dir / "runs").resolve()))
    assert metadata["promptfoo_config_dir"].startswith(str((experiment_dir / ".promptfoo").resolve()))
    assert command_runner.calls[2][0][0:4] == ["uv", "run", "python", "experiments/analysis/approach_detection/generate_approach_detection_diagnostics.py"]
    assert command_runner.calls[2][0][5] == str(experiment_dir.resolve())
