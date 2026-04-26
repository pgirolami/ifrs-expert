"""Compare target chunk retrieval diagnostics."""
#
# Example:
#   uv run python experiments/analysis/target_chunk_retrieval/compare_target_chunk_retrieval_diagnostics.py \
#     --input experiments/44_retrieval_non_regression_test/diagnostics/target_chunk_retrieval_index.json \
#     --label exp44-left \
#     --input experiments/44_retrieval_non_regression_test/diagnostics/target_chunk_retrieval_index.json \
#     --label exp44-right \
#     --output-dir experiments/44_retrieval_non_regression_test/diagnostics/target_chunk_retrieval_compare_self

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from experiments.analysis.target_chunk_retrieval.target_chunk_retrieval_contract import (
    TargetChunkRetrievalDiagnosticsComparer,
)  # noqa: E402


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare target chunk retrieval diagnostics")
    parser.add_argument("--input", action="append", required=True, help="Path to a run JSON or experiment index JSON")
    parser.add_argument("--label", action="append", default=[], help="Label for the matching --input")
    parser.add_argument("--output-dir", required=True, help="Directory for comparison artifacts")
    return parser


def main() -> None:
    """Run the CLI."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()
    input_paths = [Path(value) if Path(value).is_absolute() else REPO_ROOT / value for value in args.input]
    labels = args.label or []
    if labels and len(labels) != len(input_paths):
        message = "Number of --label values must match number of --input values"
        raise ValueError(message)
    labeled_inputs = [(labels[index] if index < len(labels) else input_path.stem, input_path) for index, input_path in enumerate(input_paths)]
    output_dir = Path(args.output_dir) if Path(args.output_dir).is_absolute() else REPO_ROOT / args.output_dir
    TargetChunkRetrievalDiagnosticsComparer(REPO_ROOT).compare(labeled_inputs, output_dir)


if __name__ == "__main__":
    main()
