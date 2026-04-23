#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"

cd "${REPO_ROOT}"

uv run python experiments/analysis/run_q1_retrieve_target_matrix.py \
  --output "${SCRIPT_DIR}/q1-target-retrieval__documents2-through-chunks__single-run.md" \
  --policy-config "${REPO_ROOT}/config/policy.default.yaml" \
  --retrieval-policy standards_only_through_chunks__enriched \
  --priority-doc-uids "ifric16,ias39,ifrs9"

uv run python experiments/analysis/run_q1_target_recall_summary.py \
  --output-dir "${SCRIPT_DIR}/runs/summary" \
  --question-dir "${REPO_ROOT}/experiments/00_QUESTIONS/Q1" \
  --policy-config "${REPO_ROOT}/config/policy.default.yaml" \
  --retrieval-policy standards_only_through_chunks__enriched
