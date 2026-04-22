#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"

cd "${REPO_ROOT}"

uv run python experiments/analysis/run_q1_retrieval_mode_comparison.py \
  --output-dir "${SCRIPT_DIR}" \
  --fr-question-dir "${REPO_ROOT}/experiments/00_QUESTIONS/Q1" \
  --en-question-dir "${REPO_ROOT}/experiments/00_QUESTIONS/Q1en" \
  --fr-raw-policy-config "${SCRIPT_DIR}/policy.raw.yaml" \
  --fr-enriched-policy-config "${SCRIPT_DIR}/policy.enriched.yaml" \
  --en-control-policy-config "${SCRIPT_DIR}/policy.raw.yaml" \
  --priority-doc-uids "ifric16,ias39,ifrs9" \
  --target-doc-uids "ifric16,ias39,ifrs9"
