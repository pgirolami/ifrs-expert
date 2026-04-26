"""Generate approach detection diagnostics for one saved answer run."""
#
# Example:
#   uv run python experiments/analysis/approach_detection/generate_approach_detection_diagnostics.py \
#     --experiment experiments/31_new_A_with_less_context_in_B \
#     --run-id 2026-04-10_17-44-35_promptfoo-eval-family-q1

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from experiments.analysis.approach_detection.approach_detection_contract import (  # noqa: E402
    DEFAULT_DIAGNOSTICS_DIRNAME,
    DEFAULT_LAYER_DIRNAME,
    ApproachDetectionDiagnosticsGenerator,
    resolve_experiment_dir,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate approach detection diagnostics")
    parser.add_argument("--experiment", required=True, help="Experiment directory or experiment number")
    parser.add_argument("--run-id", default=None, help="Run id; required when the experiment has multiple runs")
    return parser


def main() -> None:
    """Run the CLI."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()
    experiment_dir = resolve_experiment_dir(REPO_ROOT, args.experiment)
    generator = ApproachDetectionDiagnosticsGenerator(REPO_ROOT)
    diagnostics = generator.generate(experiment_dir=experiment_dir, run_id=args.run_id)
    output_dir = experiment_dir / "runs" / diagnostics.run_id / DEFAULT_DIAGNOSTICS_DIRNAME / DEFAULT_LAYER_DIRNAME
    generator.write_run_artifacts(diagnostics, output_dir)
    index_md_path, _ = generator.refresh_experiment_index(experiment_dir)
    print(index_md_path)


if __name__ == "__main__":
    main()
