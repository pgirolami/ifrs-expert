#!/usr/bin/env bash
set -euo pipefail

# Determine base directory (parent of script's directory)
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PROJECT_DIR="$SCRIPT_DIR/../../"

# Change to project directory for uv to find src module
cd "$PROJECT_DIR"

# Default values
K="${1:-5}"
E="${2:-5}"
MIN_SCORE="${3:-0.5}"
F="${4:-0}"

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

for question_file in "$PROJECT_DIR"/experiments/00_QUESTIONS/Q*.txt; do
  question_name="$(basename "$question_file" .txt)"
  
  for run in 1 2 3; do
    run_dir="$OUTPUT_DIR/${question_name}${FILENAME_SUFFIX}__run${run}"
    
    # Skip if already processed
    if [ -d "$run_dir" ] && [ -f "$run_dir/B-response.md" ]; then
      echo "Skipping $run_dir/ (already processed)"
      continue
    fi
    
    echo "Running $question_file -> $run_dir/"
    
    mkdir -p "$run_dir"
    
    uv run python -m src.cli answer \
      --output-dir "$run_dir" \
      --save-all \
      -k "$K" -e "$E" --min-score "$MIN_SCORE" $CMD_SUFFIX \
      < "$question_file"
  done
done
