"""Analyze document routing diagnostics and append findings to EXPERIMENTS.md."""
#
# Example:
#   uv run python experiments/analysis/document_routing/analyze_document_routing_diagnostics.py \
#     --experiment experiments/44_retrieval_non_regression_test

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
    DocumentRoutingDiagnosticsAnalyzer,
    resolve_experiment_dir,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze document routing diagnostics")
    parser.add_argument("--experiment", required=True, help="Experiment directory or experiment number")
    parser.add_argument("--input", default=None, help="Path to a run JSON, experiment index JSON, or comparison JSON")
    parser.add_argument("--section-title", default=None, help="Markdown section title")
    return parser


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()
    experiment_dir = resolve_experiment_dir(REPO_ROOT, args.experiment)
    input_path = None
    if args.input is not None:
        input_path = Path(args.input) if Path(args.input).is_absolute() else REPO_ROOT / args.input
    analyzer = DocumentRoutingDiagnosticsAnalyzer(REPO_ROOT)
    analyzer.analyze(experiment_dir=experiment_dir, input_path=input_path, section_title=args.section_title)


if __name__ == "__main__":
    main()
