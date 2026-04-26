"""Compare generated approach detection diagnostics."""
#
# Example:
#   uv run python experiments/analysis/approach_detection/compare_approach_detection_diagnostics.py \
#     --input experiments/31_new_A_with_less_context_in_B/diagnostics/approach_detection_index.json \
#     --label exp31 \
#     --input experiments/32_same_as_previous_but_with_minimax/diagnostics/approach_detection_index.json \
#     --label exp32 \
#     --output-dir experiments/31_new_A_with_less_context_in_B/diagnostics/approach_detection_compare_exp32

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from experiments.analysis.approach_detection.approach_detection_contract import ApproachDetectionDiagnosticsComparer  # noqa: E402


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare approach detection diagnostics")
    parser.add_argument("--input", action="append", required=True, help="Run diagnostics JSON or experiment index JSON")
    parser.add_argument("--label", action="append", default=None, help="Optional label aligned with --input")
    parser.add_argument("--output-dir", required=True, help="Required comparison output directory")
    return parser


def main() -> None:
    """Run the CLI."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()
    input_paths = [Path(value) if Path(value).is_absolute() else REPO_ROOT / value for value in args.input]
    labels = args.label or []
    if labels and len(labels) != len(input_paths):
        raise ValueError("--label must be provided once per --input")
    inputs = [(labels[index] if labels else input_path.stem, input_path) for index, input_path in enumerate(input_paths)]
    output_dir = Path(args.output_dir) if Path(args.output_dir).is_absolute() else REPO_ROOT / args.output_dir
    ApproachDetectionDiagnosticsComparer(REPO_ROOT).compare(inputs=inputs, output_dir=output_dir)
    print(output_dir)


if __name__ == "__main__":
    main()
