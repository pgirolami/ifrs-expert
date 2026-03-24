#!/usr/bin/env bash
set -euo pipefail

# Default values
K="${1:-5}"
E="${2:-5}"
MIN_SCORE="${3:-0.5}"
F="${4:-0}"
RUN_LLM="${5:-true}"  # Set to "false" to skip LLM call

OUTPUT_DIR="experiments/03_proper_context_hierarchical_retrieval"
mkdir -p "$OUTPUT_DIR"

# Build filename suffix
if [ "$F" -gt 0 ]; then
  FILENAME_SUFFIX="_k=${K}_e=${E}_f=${F}_min-score=${MIN_SCORE}"
  CMD_SUFFIX="-f $F"
else
  FILENAME_SUFFIX="_k=${K}_e=${E}_min-score=${MIN_SCORE}"
  CMD_SUFFIX=""
fi

for question_file in experiments/Q1.*.txt; do
  question_name="$(basename "$question_file" .txt)"
  prompt_file="$OUTPUT_DIR/${question_name}${FILENAME_SUFFIX}.prompt"
  response_file="$OUTPUT_DIR/${question_name}${FILENAME_SUFFIX}.response"

  echo "Running $question_file -> $prompt_file"
  uv run python -m src.cli answer -k "$K" -e "$E" --min-score "$MIN_SCORE" $CMD_SUFFIX < "$question_file" > "$prompt_file"

  if [ "$RUN_LLM" = "true" ]; then
    session_jsonl="$OUTPUT_DIR/${question_name}${FILENAME_SUFFIX%\.prompt}.jsonl"
    session_html="${session_jsonl%.jsonl}.html"
    rm -rf "$session_jsonl" "$session_html"
    echo "Sending prompt in $prompt_file to LLM -> $response_file"
#    pi -p --provider openai-codex --model gpt-5.4 --thinking high --no-skills --no-tools --no-extensions --no-prompt-templates --no-themes --system-prompt "" --session "$session_jsonl" "@$prompt_file" "" > "$response_file" 2>&1
    pi -p --provider openai-codex --model gpt-5.4 --thinking high --no-skills --no-tools --no-extensions --no-prompt-templates --no-themes --system-prompt "" "@$prompt_file" "" > "$response_file"
    
    if [ -f "$session_jsonl" ]; then
      echo "Exporting session to HTML -> $session_html"
      pi --export "$session_jsonl" "$session_html"
    fi
  fi
done
