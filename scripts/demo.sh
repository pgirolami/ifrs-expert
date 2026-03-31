#!/usr/bin/env bash

set -euo pipefail

DEMO_IFRS9_URL="https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2021/issued/part-a/ifrs-9-financial-instruments.pdf"
DEMO_IFRIC16_URL="https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2021/issued/part-a/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.pdf"
DEMO_IFRS9_PDF="/tmp/ifrs-9-financial-instruments.pdf"
DEMO_IFRIC16_PDF="/tmp/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.pdf"
DEMO_QUESTION="Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?"
LOG_PATH="logs/app.log"
TAIL_PID=""

load_dotenv() {
  if [ -f .env ]; then
    set -a
    # shellcheck disable=SC1091
    . ./.env
    set +a
  fi
}

validate_llm_configuration() {
  local provider
  provider="${LLM_PROVIDER:-}"

  case "${provider}" in
    openai)
      REQUIRED_API_KEY_NAME="OPENAI_API_KEY"
      REQUIRED_API_KEY_VALUE="${OPENAI_API_KEY:-}"
      ;;
    anthropic)
      REQUIRED_API_KEY_NAME="ANTHROPIC_API_KEY"
      REQUIRED_API_KEY_VALUE="${ANTHROPIC_API_KEY:-}"
      ;;
    mistral)
      REQUIRED_API_KEY_NAME="MISTRAL_API_KEY"
      REQUIRED_API_KEY_VALUE="${MISTRAL_API_KEY:-}"
      ;;
    "")
      echo "Error: LLM_PROVIDER is not set. Set it in the environment or .env to one of: openai, anthropic, mistral." >&2
      exit 1
      ;;
    *)
      echo "Error: Unsupported LLM_PROVIDER=${provider}. Allowed values: openai, anthropic, mistral." >&2
      exit 1
      ;;
  esac

  if [ -z "${REQUIRED_API_KEY_VALUE}" ]; then
    echo "Error: ${REQUIRED_API_KEY_NAME} is not set. Set it in the environment or .env." >&2
    exit 1
  fi

  echo "Using LLM_PROVIDER=${provider}"
}

start_log_tail() {
  mkdir -p logs
  touch "${LOG_PATH}"
  echo "Streaming ${LOG_PATH} while the answer command runs..."
  tail -n 0 -f "${LOG_PATH}" </dev/null &
  TAIL_PID="$!"
}

stop_log_tail() {
  if [ -n "${TAIL_PID}" ] && kill -0 "${TAIL_PID}" 2>/dev/null; then
    kill "${TAIL_PID}" 2>/dev/null || true
    wait "${TAIL_PID}" 2>/dev/null || true
  fi
}

wait_for_enter() {
  if [ -r /dev/tty ]; then
    printf '\nPress Enter to launch the Streamlit app...' > /dev/tty
    read -r _ < /dev/tty
    return
  fi

  echo
  echo "No interactive terminal detected. Launching the Streamlit app immediately."
}

main() {
  trap stop_log_tail EXIT

  load_dotenv
  validate_llm_configuration

  echo "Syncing dependencies with uv..."
  uv sync --all-groups

  echo "Downloading IFRS demo documents..."
  curl --fail --location --silent --show-error "${DEMO_IFRS9_URL}" --output "${DEMO_IFRS9_PDF}"
  curl --fail --location --silent --show-error "${DEMO_IFRIC16_URL}" --output "${DEMO_IFRIC16_PDF}"

  echo "Ingesting IFRS 9..."
  uv run python -m src.cli store "${DEMO_IFRS9_PDF}" --doc-uid ifrs-9

  echo "Ingesting IFRIC 16..."
  uv run python -m src.cli store "${DEMO_IFRIC16_PDF}" --doc-uid ifric-16

  echo "Asking demo question via the CLI..."
  start_log_tail
  printf '%s\n' "${DEMO_QUESTION}" | uv run python -m src.cli answer -k 5 -e 5 --min-score 0.55
  stop_log_tail
  TAIL_PID=""

  wait_for_enter
  exec uv run streamlit run streamlit_app.py
}

main "$@"
