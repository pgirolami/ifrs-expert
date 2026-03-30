#!/usr/bin/env bash
set -euo pipefail

# Determine base directory (parent of script's directory)
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PROJECT_DIR="$SCRIPT_DIR/../../"

# Change to project directory for uv to find src module
cd "$PROJECT_DIR"

# First argument: directory containing question files (required)
QUESTIONS_DIR="${1:-}"

if [ -z "$QUESTIONS_DIR" ]; then
  echo "Usage: $0 <questions_dir> [K] [E] [MIN_SCORE] [F]"
  echo "  questions_dir: Directory containing Q*.txt question files"
  echo "  K: Number of chunks (default: 5)"
  echo "  E: Number of evaluations (default: 5)"
  echo "  MIN_SCORE: Minimum score threshold (default: 0.5)"
  echo "  F: Filter type (default: 0)"
  exit 1
fi

# Resolve to absolute path (relative to SCRIPT_DIR, not current working directory)
QUESTIONS_DIR="$(cd "$SCRIPT_DIR" && realpath "$QUESTIONS_DIR")"

# Default values for remaining parameters
K="${2:-5}"
E="${3:-5}"
MIN_SCORE="${4:-0.5}"
F="${5:-0}"

OUTPUT_DIR="$SCRIPT_DIR"
mkdir -p "$OUTPUT_DIR"

# Build filename suffix
if [ "$F" -gt 0 ]; then
  FILENAME_SUFFIX="_k=${K}_e=${E}_f=${F}_min-score=${MIN_SCORE}"
  CMD_SUFFIX="-f $F"
else
  FILENAME_SUFFIX="_k=${K}_e=${E}_min-score=${MIN_SCORE}"
  CMD_SUFFIX=""
fi

for question_file in "$QUESTIONS_DIR"/Q*.txt; do
  question_name="$(basename "$question_file" .txt)"
  
  # Start all 3 runs in parallel
  pids=()
  run_numbers=()
  for run in 1 2 3; do
    run_dir="$OUTPUT_DIR/${question_name}${FILENAME_SUFFIX}__run${run}"
    
    # Skip if already processed
    if [ -d "$run_dir" ] && [ -f "$run_dir/A-response.json" ]; then
      echo "Skipping $run_dir/ (already processed)"
      continue
    fi
    
    echo "Starting $question_file -> $run_dir/"
    
    mkdir -p "$run_dir"
    
    # Run in background and capture PID
    uv run python -m src.cli answer \
      --output-dir "$run_dir" \
      --save-all \
      -k "$K" -e "$E" --min-score "$MIN_SCORE" $CMD_SUFFIX \
      < "$question_file" &
    pids+=($!)
    run_numbers+=($run)
  done
  
  # Wait for all parallel runs to complete
  failed=0
  for i in "${!pids[@]}"; do
    pid=${pids[$i]}
    run=${run_numbers[$i]}
    if ! wait "$pid"; then
      echo "ERROR: Command failed for $question_name run $run"
      failed=1
    fi
  done
  
  if [ $failed -ne 0 ]; then
    echo "One or more runs failed for $question_name"
    echo "Check logs in: $OUTPUT_DIR/${question_name}${FILENAME_SUFFIX}__run{1,2,3}/"
    exit 1
  fi
  
  echo "All runs completed for $question_name"
done
