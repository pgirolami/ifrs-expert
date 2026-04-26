"""Analyze approach detection diagnostics and append findings to EXPERIMENTS.md."""
#
# Example:
#   uv run python experiments/analysis/approach_detection/analyze_approach_detection_diagnostics.py \
#     --experiment experiments/31_new_A_with_less_context_in_B

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
    ApproachDetectionDiagnosticsAnalyzer,
    resolve_experiment_dir,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze approach detection diagnostics")
    parser.add_argument("--experiment", required=True, help="Experiment directory or experiment number")
    parser.add_argument("--input", default=None, help="Path to a run JSON, experiment index JSON, or comparison JSON")
    parser.add_argument("--section-title", default=None, help="Markdown section title")
    return parser


def main() -> None:
    """Run the CLI."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()
    experiment_dir = resolve_experiment_dir(REPO_ROOT, args.experiment)
    input_path = None if args.input is None else Path(args.input)
    if input_path is not None and not input_path.is_absolute():
        input_path = REPO_ROOT / input_path
    ApproachDetectionDiagnosticsAnalyzer(REPO_ROOT).analyze(
        experiment_dir=experiment_dir,
        input_path=input_path,
        section_title=args.section_title,
    )


if __name__ == "__main__":
    main()
