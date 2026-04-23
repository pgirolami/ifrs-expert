#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/../../.." && pwd)"

cd "${REPO_ROOT}"

uv run python experiments/analysis/run_q1_retrieval_mode_comparison.py \
  --output-dir "${SCRIPT_DIR}" \
  --fr-question-dir "${REPO_ROOT}/experiments/00_QUESTIONS/Q1" \
  --en-question-dir "${REPO_ROOT}/experiments/00_QUESTIONS/Q1en" \
  --fr-raw-policy-config "${SCRIPT_DIR}/policy.current.raw.yaml" \
  --fr-enriched-policy-config "${SCRIPT_DIR}/policy.current.enriched.yaml" \
  --en-control-policy-config "${SCRIPT_DIR}/policy.current.raw.yaml" \
  --priority-doc-uids "ifric16,ias39,ifrs9" \
  --target-doc-uids "ifric16,ias39,ifrs9"

mv -f "${SCRIPT_DIR}/generated_fr_raw_target_matrix.md" "${SCRIPT_DIR}/q1-target-retrieval__documents2-through-chunks__fr-raw-target-matrix.md"
mv -f "${SCRIPT_DIR}/generated_fr_enriched_target_matrix.md" "${SCRIPT_DIR}/q1-target-retrieval__documents2-through-chunks__fr-enriched-target-matrix.md"
mv -f "${SCRIPT_DIR}/generated_en_control_target_matrix.md" "${SCRIPT_DIR}/q1-target-retrieval__documents2-through-chunks__en-control-target-matrix.md"
mv -f "${SCRIPT_DIR}/generated_merged_delta_report.md" "${SCRIPT_DIR}/q1-target-retrieval__documents2-through-chunks__merged-delta-report.md"
mv -f "${SCRIPT_DIR}/generated_merged_delta_report.json" "${SCRIPT_DIR}/q1-target-retrieval__documents2-through-chunks__merged-delta-report.json"
mv -f "${SCRIPT_DIR}/generated_summary.md" "${SCRIPT_DIR}/q1-target-retrieval__documents2-through-chunks__summary.md"
mv -f "${SCRIPT_DIR}/generated_summary.json" "${SCRIPT_DIR}/q1-target-retrieval__documents2-through-chunks__summary.json"
