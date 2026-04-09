"""Run Promptfoo evals with one Promptfoo database per experiment."""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
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
DEFAULT_DESCRIPTION: Final[str] = "promptfoo eval"


@dataclass(frozen=True)
class PromptfooRunLayout:
    """Paths associated with one archived Promptfoo run."""

    run_dir: Path
    artifacts_dir: Path
    metadata_path: Path
    promptfoo_config_dir: Path
    description: str


class PromptfooEvalRunner:
    """Build Promptfoo config, run the eval, and archive provider artifacts."""

    def __init__(
        self,
        project_root: Path,
        experiment_dir: Path,
        promptfoo_config_dir: Path | None = None,
        now_fn: Callable[[], datetime] | None = None,
        command_runner: Callable[[list[str], dict[str, str], Path], subprocess.CompletedProcess[str]] | None = None,
    ) -> None:
        """Initialize the Promptfoo eval runner."""
        self._project_root = project_root
        self._experiment_dir = experiment_dir
        self._promptfoo_config_dir = promptfoo_config_dir or experiment_dir / ".promptfoo"
        self._now_fn = now_fn or (lambda: datetime.now(tz=UTC))
        self._command_runner = command_runner or _run_command

    def run(self, promptfoo_args: Sequence[str], description: str | None) -> int:
        """Run Promptfoo and archive provider artifacts in the experiment directory."""
        run_layout = self._build_run_layout(description=description)
        run_layout.run_dir.mkdir(parents=True, exist_ok=False)
        run_layout.artifacts_dir.mkdir(parents=True, exist_ok=True)
        run_layout.promptfoo_config_dir.mkdir(parents=True, exist_ok=True)
        self._write_run_metadata(run_layout=run_layout, promptfoo_args=list(promptfoo_args))

        env = os.environ.copy()
        env[PROMPTFOO_ARTIFACTS_DIR_ENV] = str(run_layout.artifacts_dir)
        env[PROMPTFOO_CONFIG_DIR_ENV] = str(run_layout.promptfoo_config_dir)

        promptfoo_config_path = run_layout.run_dir / "promptfooconfig.yaml"

        logger.info(f"Building promptfooconfig.yaml to {promptfoo_config_path}")
        build_result = self._command_runner(
            ["npm", "run", "eval:build", "--", "--output", str(promptfoo_config_path)],
            env,
            self._project_root,
        )
        if build_result.returncode != 0:
            logger.error(f"Promptfoo config build failed with exit code {build_result.returncode}")
            return build_result.returncode

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
        return eval_result.returncode

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
            description=resolved_description,
        )

    def _write_run_metadata(self, run_layout: PromptfooRunLayout, promptfoo_args: list[str]) -> None:
        """Write run metadata for reproducibility."""
        metadata = {
            "description": run_layout.description,
            "artifacts_path": str(run_layout.artifacts_dir.relative_to(self._project_root)),
            "promptfoo_config_dir": str(run_layout.promptfoo_config_dir.relative_to(self._project_root)),
            "promptfoo_args": promptfoo_args,
            "created_at_utc": self._now_fn().astimezone(UTC).isoformat(),
        }
        run_layout.metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")


def _slugify(value: str) -> str:
    """Convert free text to a filesystem-friendly slug."""
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized or "promptfoo-eval"


def _run_command(command: list[str], env: dict[str, str], cwd: Path) -> subprocess.CompletedProcess[str]:
    """Run one subprocess command and return its completion status."""
    return subprocess.run(command, cwd=cwd, env=env, check=False, text=True)  # noqa: S603


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
