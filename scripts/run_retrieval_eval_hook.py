"""Run focused retrieval evals from pre-commit with temporary experiment storage."""

from __future__ import annotations

import argparse
import logging
import os
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING, Final

logger = logging.getLogger(__name__)

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[1]
DEFAULT_STORAGE_ROOT: Final[Path] = Path(os.sep) / "tmp" / "ifrs-expert-precommit-evals"
DEFAULT_MAKE_TARGET: Final[str] = "eval-retrieve"
DEFAULT_RUN_PREFIX: Final[str] = "retrieval-eval-"

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence


@dataclass(frozen=True)
class RetrievalEvalPair:
    """One retrieval eval filter pair."""

    family: str
    variant: str


class RetrievalEvalHookRunner:
    """Run retrieval evals into a temporary repo-local experiment directory."""

    def __init__(
        self,
        project_root: Path,
        storage_root: Path,
        make_target: str = DEFAULT_MAKE_TARGET,
        now_fn: Callable[[], datetime] | None = None,
        command_runner: Callable[[list[str], Path, dict[str, str]], subprocess.CompletedProcess[str]] | None = None,
    ) -> None:
        """Initialize the retrieval eval hook runner."""
        self._project_root = project_root
        self._storage_root = storage_root
        self._make_target = make_target
        self._now_fn = now_fn or (lambda: datetime.now(tz=UTC))
        self._command_runner = command_runner or _run_command

    def run(self, pairs: Sequence[RetrievalEvalPair]) -> int:
        """Run each pair sequentially and keep the temp folder only on failure."""
        if not pairs:
            message = "At least one (family, variant) pair is required"
            raise ValueError(message)

        self._storage_root.mkdir(parents=True, exist_ok=True)
        self._cleanup_previous_runs()
        temp_root = self._create_temp_root()
        experiment_dir = temp_root / "experiment"
        experiment_dir.mkdir(parents=True, exist_ok=True)

        logger.info(f"Created temporary retrieval eval root at {temp_root}")

        exit_code = 0
        for pair in pairs:
            logger.info(f"Running retrieval eval for family={pair.family} variant={pair.variant}")
            result = self._run_make_eval(pair=pair, experiment_dir=experiment_dir)
            if result.returncode != 0:
                exit_code = result.returncode
                logger.error(f"Retrieval eval failed for family={pair.family} variant={pair.variant} with exit code {exit_code}; keeping temp root at {temp_root}")
                break

        if exit_code == 0:
            shutil.rmtree(temp_root)
            logger.info(f"Removed temporary retrieval eval root at {temp_root}")

        return exit_code

    def _cleanup_previous_runs(self) -> None:
        """Delete stale retrieval eval temp directories from prior runs."""
        if not self._storage_root.exists():
            return

        for child in sorted(self._storage_root.iterdir()):
            if child.is_symlink() or child.is_file():
                logger.info(f"Removing stale temp retrieval eval file {child}")
                child.unlink(missing_ok=True)
            elif child.is_dir():
                logger.info(f"Removing stale temp retrieval eval directory {child}")
                shutil.rmtree(child, ignore_errors=True)

    def _create_temp_root(self) -> Path:
        """Create a new temp root under the repo-local storage directory."""
        timestamp = self._now_fn().astimezone(UTC).strftime("%Y%m%dT%H%M%S")
        pid = os.getpid()
        return Path(tempfile.mkdtemp(prefix=f"{DEFAULT_RUN_PREFIX}{timestamp}-{pid}-", dir=self._storage_root))

    def _run_make_eval(self, pair: RetrievalEvalPair, experiment_dir: Path) -> subprocess.CompletedProcess[str]:
        """Invoke make for one family/variant pair."""
        env = os.environ.copy()
        env["EXPERIMENT_DIR"] = str(experiment_dir)
        env["FAMILY"] = pair.family
        env["VARIANT"] = pair.variant
        env["PROMPTFOO_SKIP_DIAGNOSTICS"] = "1"
        command = ["make", self._make_target]
        return self._command_runner(command, self._project_root, env)


def _run_command(command: list[str], cwd: Path, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    """Run one subprocess command and return its completion status."""
    return subprocess.run(command, cwd=cwd, env=env, check=False, text=True)  # noqa: S603


def parse_pairs(raw_pairs: Sequence[Sequence[str]] | None) -> list[RetrievalEvalPair]:
    """Convert parsed CLI pairs into typed filter objects."""
    if raw_pairs is None:
        return []

    pairs: list[RetrievalEvalPair] = []
    for family, variant in raw_pairs:
        family_value = family.strip()
        variant_value = variant.strip()
        if not family_value or not variant_value:
            continue
        pairs.append(RetrievalEvalPair(family=family_value, variant=variant_value))
    return pairs


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments for the retrieval eval hook."""
    parser = argparse.ArgumentParser(description="Run focused retrieval evals before commits")
    parser.add_argument(
        "--pair",
        action="append",
        nargs=2,
        metavar=("FAMILY", "VARIANT"),
        required=True,
        help="Run one retrieval eval for the given family and variant. Repeat to run several pairs.",
    )
    parser.add_argument(
        "--storage-root",
        type=Path,
        default=DEFAULT_STORAGE_ROOT,
        help="Repo-local root for temporary retrieval eval directories.",
    )
    parser.add_argument(
        "--make-target",
        type=str,
        default=DEFAULT_MAKE_TARGET,
        help="Make target used to launch the retrieval eval.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for the pre-commit retrieval eval helper."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    args = parse_args(argv)
    pairs = parse_pairs(args.pair)
    runner = RetrievalEvalHookRunner(
        project_root=PROJECT_ROOT,
        storage_root=args.storage_root,
        make_target=args.make_target,
    )
    return runner.run(pairs)


if __name__ == "__main__":
    raise SystemExit(main())
