"""Compare run-level document routing diagnostics."""
#
# Example:
#   uv run python experiments/analysis/document_routing/compare_document_routing_diagnostics.py \
#     --input experiments/44_retrieval_non_regression_test/diagnostics/document_routing_index.json \
#     --label exp44-left \
#     --input experiments/44_retrieval_non_regression_test/diagnostics/document_routing_index.json \
#     --label exp44-right \
#     --output-dir experiments/44_retrieval_non_regression_test/diagnostics/document_routing_compare_self

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from experiments.analysis.document_routing.document_routing_contract import (
    DocumentRoutingDiagnosticsComparer,
    resolve_experiment_dir,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare document routing diagnostics")
    parser.add_argument("--input", action="append", required=True, help="Path to a run JSON or experiment index JSON")
    parser.add_argument("--label", action="append", default=[], help="Label for the matching --input")
    parser.add_argument("--output-dir", required=True, help="Directory for comparison artifacts")
    parser.add_argument("--target-documents", default=None, help="Comma-separated list of target documents to compare")
    return parser


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()
    comparer = DocumentRoutingDiagnosticsComparer(REPO_ROOT)
    input_paths = [Path(value) if Path(value).is_absolute() else REPO_ROOT / value for value in args.input]
    labels = args.label or []
    if labels and len(labels) != len(input_paths):
        raise ValueError("Number of --label values must match number of --input values")
    labeled_inputs = [
        (labels[index] if index < len(labels) else input_path.stem, input_path)
        for index, input_path in enumerate(input_paths)
    ]
    target_documents = None if args.target_documents is None else [item.strip().lower() for item in args.target_documents.split(",") if item.strip()]
    output_dir = Path(args.output_dir) if Path(args.output_dir).is_absolute() else REPO_ROOT / args.output_dir
    comparer.compare(labeled_inputs, output_dir, target_documents=target_documents)


if __name__ == "__main__":
    main()
