#!/usr/bin/env bash

set -euo pipefail


DEMO_IFRIC16_HTML="examples/www.ifrs.org__issued-standards__list-of-standards__ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html__content__dam__ifrs__publications__html-standards__english__2026__issued__ifric16.html"
DEMO_IFRS9_HTML="examples/www.ifrs.org__issued-standards__list-of-standards__ifrs-9-financial-instruments.html__content__dam__ifrs__publications__html-standards__english__2026__issued__ifrs9.html"


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
  local required_api_key_name=""
  local required_api_key_value=""
  local required_model_name=""
  local required_model_value=""
  local codex_auth_path=""
  provider="${LLM_PROVIDER:-}"

  case "${provider}" in
    openai)
      required_api_key_name="OPENAI_API_KEY"
      required_api_key_value="${OPENAI_API_KEY:-}"
      required_model_name="OPENAI_MODEL"
      required_model_value="${OPENAI_MODEL:-}"
      ;;
    openai-codex)
      required_model_name="OPENAI_CODEX_MODEL"
      required_model_value="${OPENAI_CODEX_MODEL:-}"
      codex_auth_path="${CODEX_AUTH_FILE:-$HOME/.codex/auth.json}"
      ;;
    anthropic)
      required_api_key_name="ANTHROPIC_API_KEY"
      required_api_key_value="${ANTHROPIC_API_KEY:-}"
      required_model_name="ANTHROPIC_MODEL"
      required_model_value="${ANTHROPIC_MODEL:-}"
      ;;
    mistral)
      required_api_key_name="MISTRAL_API_KEY"
      required_api_key_value="${MISTRAL_API_KEY:-}"
      required_model_name="MISTRAL_MODEL"
      required_model_value="${MISTRAL_MODEL:-}"
      ;;
    minimax)
      required_api_key_name="MINIMAX_API_KEY"
      required_api_key_value="${MINIMAX_API_KEY:-}"
      required_model_name="MINIMAX_MODEL"
      required_model_value="${MINIMAX_MODEL:-}"
      ;;
    ollama)
      required_model_name="OLLAMA_MODEL"
      required_model_value="${OLLAMA_MODEL:-}"
      ;;
    "")
      echo "Error: LLM_PROVIDER is not set. Set it in the environment or .env to one of: openai, openai-codex, anthropic, mistral." >&2
      exit 1
      ;;
    *)
      echo "Error: Unsupported LLM_PROVIDER=${provider}. Allowed values: openai, openai-codex, anthropic, mistral." >&2
      exit 1
      ;;
  esac

  if [ -n "${required_api_key_name}" ] && [ -z "${required_api_key_value}" ]; then
    echo "Error: ${required_api_key_name} is not set. Set it in the environment or .env." >&2
    exit 1
  fi

  if [ -n "${required_model_name}" ] && [ -z "${required_model_value}" ]; then
    echo "Error: ${required_model_name} is not set. Set it in the environment or .env." >&2
    exit 1
  fi

  if [ -n "${codex_auth_path}" ] && [ ! -f "${codex_auth_path}" ]; then
    echo "Error: Codex auth file not found at ${codex_auth_path}. Run 'codex login' first or set CODEX_AUTH_FILE." >&2
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
    read -r _ < /dev/tty
    return
  fi

  echo
  echo "No interactive terminal detected: not waiting"
}

main() {
  trap stop_log_tail EXIT

  load_dotenv
  validate_llm_configuration

  echo "Syncing dependencies with uv..."
  uv sync --all-groups

  echo "Ingesting IFRS 9..."
  uv run python -m src.cli store "${DEMO_IFRS9_HTML}" --doc-uid ifrs9

  echo "Ingesting IFRIC 16..."
  uv run python -m src.cli store "${DEMO_IFRIC16_HTML}" --doc-uid ifric16


  echo "Ingesting NAXIS (1/2)..."
  uv run python -m src.cli store examples/Lefebvre-Naxis/20260412T190013Z--document.html
  echo "Ingesting NAXIS (2/2)..."
  uv run python -m src.cli store examples/Lefebvre-Naxis/20260412T190029Z--document.html

  echo "Asking demo question via the CLI..."
  start_log_tail
  printf '%s\n' "${DEMO_QUESTION}" | uv run python -m src.cli answer --policy-config=config/policy.default.yaml --output-dir=/tmp/demo/
  stop_log_tail
  TAIL_PID=""

  echo "Above is the JSON response, see the generated markdown in /tmp/demo\nPress Enter when done"
  ls -lah /tmp/demo/


  wait_for_enter
  echo 'Press Enter to launch the Streamlit app...'
  wait_for_enter
  exec uv run streamlit run streamlit_app.py
}

main "$@"
