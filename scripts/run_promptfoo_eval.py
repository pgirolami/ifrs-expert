"""Run Promptfoo evals and archive each run under the experiment directory."""

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
DEFAULT_DESCRIPTION: Final[str] = "promptfoo eval"


@dataclass(frozen=True)
class PromptfooRunLayout:
    """Paths associated with one archived Promptfoo run."""

    run_dir: Path
    report_path: Path
    artifacts_dir: Path
    metadata_path: Path
    description: str


class PromptfooEvalRunner:
    """Build Promptfoo config, run the eval, and archive HTML and artifacts."""

    def __init__(
        self,
        project_root: Path,
        experiment_dir: Path,
        now_fn: Callable[[], datetime] | None = None,
        command_runner: Callable[[list[str], dict[str, str], Path], subprocess.CompletedProcess[str]] | None = None,
    ) -> None:
        """Initialize the Promptfoo eval runner."""
        self._project_root = project_root
        self._experiment_dir = experiment_dir
        self._now_fn = now_fn or (lambda: datetime.now(tz=UTC))
        self._command_runner = command_runner or _run_command

    def run(self, promptfoo_args: Sequence[str], description: str | None) -> int:
        """Run Promptfoo and archive the HTML report and answer artifacts."""
        run_layout = self._build_run_layout(description=description)
        run_layout.run_dir.mkdir(parents=True, exist_ok=False)
        run_layout.artifacts_dir.mkdir(parents=True, exist_ok=True)
        self._write_run_metadata(run_layout=run_layout, promptfoo_args=list(promptfoo_args))

        env = os.environ.copy()
        env[PROMPTFOO_ARTIFACTS_DIR_ENV] = str(run_layout.artifacts_dir)

        logger.info(f"Building promptfooconfig.yaml before running Promptfoo into {run_layout.run_dir}")
        build_result = self._command_runner(["npm", "run", "eval:build"], env, self._project_root)
        if build_result.returncode != 0:
            logger.error(f"Promptfoo config build failed with exit code {build_result.returncode}")
            return build_result.returncode

        eval_command = [
            "npm",
            "exec",
            "--",
            "promptfoo",
            "eval",
            "--description",
            run_layout.description,
            "-o",
            str(run_layout.report_path),
            *promptfoo_args,
        ]
        logger.info(f"Running Promptfoo eval with archived HTML report at {run_layout.report_path}")
        completed_process = self._command_runner(eval_command, env, self._project_root)
        if completed_process.returncode != 0:
            logger.warning(
                f"Promptfoo eval finished with exit code {completed_process.returncode}; archived outputs remain available in {run_layout.run_dir}"
            )
        return completed_process.returncode

    def _build_run_layout(self, description: str | None) -> PromptfooRunLayout:
        """Build the archive layout for one run."""
        resolved_description = description.strip() if description and description.strip() else DEFAULT_DESCRIPTION
        timestamp = self._now_fn().astimezone(UTC).strftime("%Y-%m-%d_%H-%M-%S")
        slug = _slugify(resolved_description)
        run_dir = self._experiment_dir / "runs" / f"{timestamp}_{slug}"
        return PromptfooRunLayout(
            run_dir=run_dir,
            report_path=run_dir / "report.html",
            artifacts_dir=run_dir / "artifacts",
            metadata_path=run_dir / "run.json",
            description=resolved_description,
        )

    def _write_run_metadata(self, run_layout: PromptfooRunLayout, promptfoo_args: list[str]) -> None:
        """Write run metadata for reproducibility."""
        metadata = {
            "description": run_layout.description,
            "report_path": str(run_layout.report_path.relative_to(self._project_root)),
            "artifacts_path": str(run_layout.artifacts_dir.relative_to(self._project_root)),
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


def build_promptfoo_args(
    base_args: Sequence[str],
    family: str | None,
    variant: str | None,
    provider: str | None,
) -> list[str]:
    """Build Promptfoo CLI args from shortcut filters plus passthrough args."""
    promptfoo_args: list[str] = []
    if family is not None and family.strip():
        promptfoo_args.extend(["--filter-metadata", f"family={family.strip()}"])
    if variant is not None and variant.strip():
        promptfoo_args.extend(["--filter-metadata", f"variant={variant.strip()}"])
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


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments for the Promptfoo eval runner."""
    parser = argparse.ArgumentParser(description="Run Promptfoo and archive the HTML report and provider artifacts")
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
    runner = PromptfooEvalRunner(project_root=PROJECT_ROOT, experiment_dir=experiment_dir)
    resolved_promptfoo_args = build_promptfoo_args(
        base_args=promptfoo_args,
        family=args.family,
        variant=args.variant,
        provider=args.provider,
    )
    return runner.run(promptfoo_args=resolved_promptfoo_args, description=args.description)


if __name__ == "__main__":
    raise SystemExit(main())
