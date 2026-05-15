"""Run Promptfoo evals with one Promptfoo database per experiment."""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import shutil
import subprocess
from dataclasses import dataclass

from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence

logger = logging.getLogger(__name__)

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[1]
EXPERIMENTS_ROOT: Final[Path] = PROJECT_ROOT / "experiments"
PROMPTFOO_ARTIFACTS_DIR_ENV: Final[str] = "PROMPTFOO_ARTIFACTS_DIR"
PROMPTFOO_CONFIG_DIR_ENV: Final[str] = "PROMPTFOO_CONFIG_DIR"
PROMPTFOO_SKIP_DIAGNOSTICS_ENV: Final[str] = "PROMPTFOO_SKIP_DIAGNOSTICS"
DEFAULT_DESCRIPTION: Final[str] = "promptfoo eval"
DEFAULT_SUITE: Final[str] = "answer"
DEFAULT_POLICY_PATH: Final[Path] = PROJECT_ROOT / "config" / "policy.default.yaml"
DEFAULT_GLOSSARY_PATH: Final[Path] = PROJECT_ROOT / "config" / "en-fr-glossary.yaml"
DEFAULT_APPROACH_IDENTIFICATION_PROMPT_PATH: Final[Path] = PROJECT_ROOT / "prompts" / "answer_prompt_A.txt"
DEFAULT_APPLICABILITY_ANALYSIS_PROMPT_PATH: Final[Path] = PROJECT_ROOT / "prompts" / "answer_prompt_B.txt"


@dataclass(frozen=True)
class PromptfooRunLayout:
    """Paths associated with one archived Promptfoo run."""

    run_dir: Path
    artifacts_dir: Path
    metadata_path: Path
    promptfoo_config_dir: Path
    effective_config_dir: Path
    description: str


class PromptfooEvalRunner:
    """Build Promptfoo config, run the eval, and archive provider artifacts."""

    def __init__(
        self,
        project_root: Path,
        experiment_dir: Path,
        suite: str = DEFAULT_SUITE,
        promptfoo_config_dir: Path | None = None,
        now_fn: Callable[[], datetime] | None = None,
        command_runner: Callable[[list[str], dict[str, str], Path], subprocess.CompletedProcess[str]] | None = None,
    ) -> None:
        """Initialize the Promptfoo eval runner."""
        self._project_root = project_root
        self._experiment_dir = experiment_dir
        self._suite = suite
        self._promptfoo_config_dir = promptfoo_config_dir or experiment_dir / ".promptfoo"
        self._now_fn = now_fn or (lambda: datetime.now(tz=UTC))
        self._command_runner = command_runner or _run_command

    def run(self, promptfoo_args: Sequence[str], description: str | None) -> int:
        """Run Promptfoo and archive provider artifacts in the experiment directory."""
        run_layout = self._build_run_layout(description=description)
        run_layout.run_dir.mkdir(parents=True, exist_ok=False)
        run_layout.artifacts_dir.mkdir(parents=True, exist_ok=True)
        run_layout.promptfoo_config_dir.mkdir(parents=True, exist_ok=True)
        self._write_run_metadata(run_layout=run_layout, promptfoo_args=list(promptfoo_args), archived_artifacts={})

        env = os.environ.copy()
        env[PROMPTFOO_ARTIFACTS_DIR_ENV] = str(run_layout.artifacts_dir)
        env[PROMPTFOO_CONFIG_DIR_ENV] = str(run_layout.promptfoo_config_dir)
        skip_diagnostics = _should_skip_diagnostics(env)

        # Stage policy and prompts next to the config so relative paths resolve
        self._stage_effective_config(run_layout=run_layout)

        # Write promptfooconfig into the same directory as the staged files
        promptfoo_config_path = run_layout.run_dir / "promptfooconfig.yaml"

        logger.info(f"Building promptfooconfig.yaml to {promptfoo_config_path}")
        build_result = self._command_runner(
            ["npm", "run", "eval:build", "--", "--suite", self._suite, "--output", str(promptfoo_config_path)],
            env,
            self._project_root,
        )
        if build_result.returncode != 0:
            logger.error(f"Promptfoo config build failed with exit code {build_result.returncode}")
            return build_result.returncode

        archived_artifacts = self._archive_effective_artifacts(
            run_layout=run_layout,
            promptfoo_config_path=promptfoo_config_path,
        )
        self._write_run_metadata(
            run_layout=run_layout,
            promptfoo_args=list(promptfoo_args),
            archived_artifacts=archived_artifacts,
        )

        eval_command = [
            "npm",
            "exec",
            "--",
            "promptfoo",
            "eval",
            "-c",
            str(promptfoo_config_path),
            "--description",
            run_layout.description,
            *promptfoo_args,
        ]
        logger.info(f"Running Promptfoo eval with config {promptfoo_config_path} and database at {run_layout.promptfoo_config_dir}")
        eval_result = self._command_runner(eval_command, env, self._project_root)
        if eval_result.returncode != 0:
            logger.warning(f"Promptfoo eval finished with exit code {eval_result.returncode}; archived outputs remain available in {run_layout.run_dir} and experiment history remains available in {run_layout.promptfoo_config_dir}")

        diagnostics_exit_code = 0
        if not skip_diagnostics:
            if self._suite == "retrieve":
                diagnostics_exit_code = self._run_retrieval_diagnostics(env=env, run_layout=run_layout)
            if self._suite == "answer":
                diagnostics_exit_code = self._run_answer_diagnostics(env=env, run_layout=run_layout)

        if eval_result.returncode != 0:
            return eval_result.returncode
        return diagnostics_exit_code

    def _build_run_layout(self, description: str | None) -> PromptfooRunLayout:
        """Build the archive layout for one run."""
        resolved_description = description.strip() if description and description.strip() else DEFAULT_DESCRIPTION
        timestamp = self._now_fn().astimezone(UTC).strftime("%Y-%m-%d_%H-%M-%S")
        slug = _slugify(resolved_description)
        run_dir = self._experiment_dir / "runs" / f"{timestamp}_{slug}"
        return PromptfooRunLayout(
            run_dir=run_dir,
            artifacts_dir=run_dir / "artifacts",
            metadata_path=run_dir / "run.json",
            promptfoo_config_dir=self._promptfoo_config_dir,
            effective_config_dir=run_dir / "effective",
            description=resolved_description,
        )

    def _write_run_metadata(
        self,
        run_layout: PromptfooRunLayout,
        promptfoo_args: list[str],
        archived_artifacts: dict[str, object],
    ) -> None:
        """Write run metadata for reproducibility."""
        metadata = {
            "description": run_layout.description,
            "artifacts_path": self._format_path_for_metadata(run_layout.artifacts_dir),
            "promptfoo_config_dir": self._format_path_for_metadata(run_layout.promptfoo_config_dir),
            "promptfoo_args": promptfoo_args,
            "created_at_utc": self._now_fn().astimezone(UTC).isoformat(),
            "archived_artifacts": archived_artifacts,
        }
        run_layout.metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    def _stage_effective_config(self, run_layout: PromptfooRunLayout) -> None:
        """Copy effective policy and prompts next to the promptfooconfig.

        The promptfooconfig and the staged files live in the same directory so
        relative paths in the config resolve correctly at runtime.
        """
        effective_dir = run_layout.effective_config_dir
        effective_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DEFAULT_POLICY_PATH, effective_dir / DEFAULT_POLICY_PATH.name)
        shutil.copy2(DEFAULT_GLOSSARY_PATH, effective_dir / DEFAULT_GLOSSARY_PATH.name)
        shutil.copy2(DEFAULT_APPROACH_IDENTIFICATION_PROMPT_PATH, effective_dir / DEFAULT_APPROACH_IDENTIFICATION_PROMPT_PATH.name)
        shutil.copy2(DEFAULT_APPLICABILITY_ANALYSIS_PROMPT_PATH, effective_dir / DEFAULT_APPLICABILITY_ANALYSIS_PROMPT_PATH.name)

    def _archive_effective_artifacts(
        self,
        run_layout: PromptfooRunLayout,
        promptfoo_config_path: Path,
    ) -> dict[str, object]:
        """Copy effective policy and prompt templates into run directory with hashes.

        Files are already staged next to the config. This adds SHA256 hashes for
        reproducibility tracking only.
        """
        archived_dir = run_layout.effective_config_dir

        artifacts: dict[str, object] = {}
        artifacts["policy"] = self._copy_with_hash(
            source_path=archived_dir / DEFAULT_POLICY_PATH.name,
            destination_path=archived_dir / DEFAULT_POLICY_PATH.name,
        )
        artifacts["glossary"] = self._copy_with_hash(
            source_path=archived_dir / DEFAULT_GLOSSARY_PATH.name,
            destination_path=archived_dir / DEFAULT_GLOSSARY_PATH.name,
        )
        artifacts["approach_identification_prompt"] = self._copy_with_hash(
            source_path=archived_dir / DEFAULT_APPROACH_IDENTIFICATION_PROMPT_PATH.name,
            destination_path=archived_dir / DEFAULT_APPROACH_IDENTIFICATION_PROMPT_PATH.name,
        )
        artifacts["applicability_analysis_prompt"] = self._copy_with_hash(
            source_path=archived_dir / DEFAULT_APPLICABILITY_ANALYSIS_PROMPT_PATH.name,
            destination_path=archived_dir / DEFAULT_APPLICABILITY_ANALYSIS_PROMPT_PATH.name,
        )
        return artifacts

    def _copy_with_hash(self, source_path: Path, destination_path: Path) -> dict[str, str]:
        """Copy one file and return metadata including SHA256 hash.

        If source and destination are the same path (already staged), skips the copy
        and computes the hash from the existing file.
        """
        if not source_path.exists():
            message = f"Missing artifact source file: {source_path}"
            raise FileNotFoundError(message)
        if source_path != destination_path:
            shutil.copy2(source_path, destination_path)
        file_bytes = destination_path.read_bytes()
        digest = hashlib.sha256(file_bytes).hexdigest()
        return {
            "source_path": self._format_path_for_metadata(source_path),
            "archived_path": self._format_path_for_metadata(destination_path),
            "sha256": digest,
        }

    def _run_retrieval_diagnostics(self, env: dict[str, str], run_layout: PromptfooRunLayout) -> int:
        """Generate retrieval diagnostics for the archived run."""
        experiment_arg = self._format_path_for_metadata(run_layout.run_dir.parent.parent)
        diagnostics_commands = [
            [
                "uv",
                "run",
                "python",
                "experiments/analysis/document_routing/generate_document_routing_diagnostics.py",
                "--experiment",
                experiment_arg,
                "--run-id",
                run_layout.run_dir.name,
            ],
            [
                "uv",
                "run",
                "python",
                "experiments/analysis/target_chunk_retrieval/generate_target_chunk_retrieval_diagnostics.py",
                "--experiment",
                experiment_arg,
                "--run-id",
                run_layout.run_dir.name,
            ],
        ]
        return self._run_diagnostics_commands(
            env=env,
            diagnostics_commands=diagnostics_commands,
            diagnostics_name="retrieval",
        )

    def _run_answer_diagnostics(self, env: dict[str, str], run_layout: PromptfooRunLayout) -> int:
        """Generate answer diagnostics for the archived run."""
        experiment_arg = self._format_path_for_metadata(run_layout.run_dir.parent.parent)
        diagnostics_commands = [
            [
                "uv",
                "run",
                "python",
                "experiments/analysis/approach_detection/generate_approach_detection_diagnostics.py",
                "--experiment",
                experiment_arg,
                "--run-id",
                run_layout.run_dir.name,
            ],
        ]
        return self._run_diagnostics_commands(
            env=env,
            diagnostics_commands=diagnostics_commands,
            diagnostics_name="answer",
        )

    def _run_diagnostics_commands(
        self,
        env: dict[str, str],
        diagnostics_commands: list[list[str]],
        diagnostics_name: str,
    ) -> int:
        """Run one or more diagnostics commands and return the first failure code."""
        for command in diagnostics_commands:
            logger.info(f"Running {diagnostics_name} diagnostics command: {' '.join(command)}")
            result = self._command_runner(command, env, self._project_root)
            if result.returncode != 0:
                logger.error(f"{diagnostics_name.capitalize()} diagnostics command failed with exit code {result.returncode}: {' '.join(command)}")
                return result.returncode
        return 0

    def _format_path_for_metadata(self, path: Path) -> str:
        """Return a repo-relative path when possible, otherwise an absolute path."""
        try:
            return str(path.relative_to(self._project_root))
        except ValueError:
            return str(path)


def _slugify(value: str) -> str:
    """Convert free text to a filesystem-friendly slug."""
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized or "promptfoo-eval"


def _run_command(command: list[str], env: dict[str, str], cwd: Path) -> subprocess.CompletedProcess[str]:
    """Run one subprocess command and return its completion status."""
    return subprocess.run(command, cwd=cwd, env=env, check=False, text=True)  # noqa: S603


def _should_skip_diagnostics(env: dict[str, str]) -> bool:
    """Return whether post-eval diagnostics should be skipped."""
    raw_value = env.get(PROMPTFOO_SKIP_DIAGNOSTICS_ENV, "")
    normalized_value = raw_value.strip().lower()
    return normalized_value in {"1", "true", "yes", "on"}


def build_default_description(
    family: str | None,
    variant: str | None,
    provider: str | None,
) -> str:
    """Build a useful default run description from the active filters."""
    description_parts: list[str] = [DEFAULT_DESCRIPTION]
    if family is not None and family.strip():
        description_parts.append(f"family={family.strip()}")
    if variant is not None and variant.strip():
        description_parts.append(f"variant={variant.strip()}")
    if provider is not None and provider.strip():
        description_parts.append(f"provider={provider.strip()}")
    return " ".join(description_parts)


def build_promptfoo_args(
    base_args: Sequence[str],
    family: str | None,
    variant: str | None,
    provider: str | None,
) -> list[str]:
    """Build Promptfoo CLI args from shortcut filters plus passthrough args."""
    promptfoo_args: list[str] = []
    # Append '¤' suffix to match the delimiter-suffixed family and variant values in metadata.
    if family is not None and family.strip():
        promptfoo_args.extend(["--filter-metadata", f"family={family.strip()}¤"])
    if variant is not None and variant.strip():
        promptfoo_args.extend(["--filter-metadata", f"variant={variant.strip()}¤"])
    if provider is not None and provider.strip():
        promptfoo_args.extend(["--filter-targets", provider.strip()])
    promptfoo_args.extend(base_args)
    return promptfoo_args


def resolve_experiment_dir(project_root: Path, experiment_dir: Path) -> Path:
    """Resolve an experiment dir, prefixing the repo experiments/ root when needed."""
    if experiment_dir.is_absolute():
        return experiment_dir
    if experiment_dir.parts and experiment_dir.parts[0] == "experiments":
        return project_root / experiment_dir
    return project_root / "experiments" / experiment_dir


def resolve_promptfoo_config_dir(project_root: Path, promptfoo_config_dir: Path) -> Path:
    """Resolve a Promptfoo config dir relative to the project root when needed."""
    if promptfoo_config_dir.is_absolute():
        return promptfoo_config_dir
    return project_root / promptfoo_config_dir


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments for the Promptfoo eval runner."""
    parser = argparse.ArgumentParser(description="Run Promptfoo with an experiment-local database and archived provider artifacts")
    parser.add_argument(
        "--description",
        type=str,
        default=None,
        help="Human-readable description for the Promptfoo run and archive directory",
    )
    parser.add_argument(
        "--experiment-dir",
        type=Path,
        required=True,
        help="Experiment directory where archived Promptfoo runs are written. Relative paths are resolved under experiments/ unless already prefixed.",
    )
    parser.add_argument(
        "--family",
        type=str,
        default=None,
        help="Shortcut for `--filter-metadata family=<value>`",
    )
    parser.add_argument(
        "--variant",
        type=str,
        default=None,
        help="Shortcut for `--filter-metadata variant=<value>`",
    )
    parser.add_argument(
        "--provider",
        type=str,
        default=None,
        help="Shortcut for `--filter-targets <value>`",
    )
    parser.add_argument(
        "--suite",
        choices=("answer", "retrieve"),
        default=DEFAULT_SUITE,
        help="Promptfoo suite to build and run",
    )
    parser.add_argument(
        "promptfoo_args",
        nargs=argparse.REMAINDER,
        help="Additional arguments forwarded to `promptfoo eval` after `--`",
    )
    return parser.parse_args(argv)


def main() -> int:
    """Run the Promptfoo experiment runner CLI."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    args = parse_args()
    promptfoo_args = list(args.promptfoo_args)
    if promptfoo_args and promptfoo_args[0] == "--":
        promptfoo_args = promptfoo_args[1:]

    experiment_dir = resolve_experiment_dir(project_root=PROJECT_ROOT, experiment_dir=args.experiment_dir)
    promptfoo_config_dir_env = os.environ.get(PROMPTFOO_CONFIG_DIR_ENV)
    promptfoo_config_dir = resolve_promptfoo_config_dir(PROJECT_ROOT, Path(promptfoo_config_dir_env)) if promptfoo_config_dir_env else None
    runner = PromptfooEvalRunner(
        project_root=PROJECT_ROOT,
        experiment_dir=experiment_dir,
        suite=args.suite,
        promptfoo_config_dir=promptfoo_config_dir,
    )
    resolved_promptfoo_args = build_promptfoo_args(
        base_args=promptfoo_args,
        family=args.family,
        variant=args.variant,
        provider=args.provider,
    )
    description = args.description or build_default_description(
        family=args.family,
        variant=args.variant,
        provider=args.provider,
    )
    return runner.run(promptfoo_args=resolved_promptfoo_args, description=description)


if __name__ == "__main__":
    raise SystemExit(main())
