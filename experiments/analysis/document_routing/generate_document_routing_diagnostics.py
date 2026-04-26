"""Generate run-level document routing diagnostics."""
#
# Example:
#   uv run python experiments/analysis/document_routing/generate_document_routing_diagnostics.py \
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
    DEFAULT_DIAGNOSTICS_DIRNAME,
    DEFAULT_LAYER_DIRNAME,
    DocumentRoutingDiagnosticsGenerator,
    resolve_experiment_dir,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate document routing diagnostics for one Promptfoo run")
    parser.add_argument("--experiment", required=True, help="Experiment directory or experiment number")
    parser.add_argument("--run-id", default=None, help="Run directory name, required when the experiment has more than one run")
    return parser


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()
    experiment_dir = resolve_experiment_dir(REPO_ROOT, args.experiment)
    generator = DocumentRoutingDiagnosticsGenerator(REPO_ROOT)
    diagnostics = generator.generate(experiment_dir=experiment_dir, run_id=args.run_id)
    output_dir = experiment_dir / "runs" / diagnostics.run_id / DEFAULT_DIAGNOSTICS_DIRNAME / DEFAULT_LAYER_DIRNAME
    generator.write_run_artifacts(diagnostics, output_dir)
    generator.refresh_experiment_index(experiment_dir)


if __name__ == "__main__":
    main()
