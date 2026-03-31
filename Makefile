DEMO_IFRS9_URL := https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2021/issued/part-a/ifrs-9-financial-instruments.pdf
DEMO_IFRIC16_URL := https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2021/issued/part-a/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.pdf
DEMO_IFRS9_PDF := /tmp/ifrs-9-financial-instruments.pdf
DEMO_IFRIC16_PDF := /tmp/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.pdf

.PHONY: dev lint format test test-retrieval build demo

dev:
	uv sync --all-groups

types:
	uv run ty check src/

lint:
	uv run ty check src/ && uv run ruff format --check && uv run ruff check

format:
	uv run ruff format .

test:
	uv run pytest

test-retrieval:
	uv run pytest tests/retrieval/ --no-cov

build:
	uv build

demo:
	@set -eu; \
	if [ -f .env ]; then \
		set -a; \
		. ./.env; \
		set +a; \
	fi; \
	provider="$${LLM_PROVIDER:-}"; \
	case "$$provider" in \
		openai) api_key_name="OPENAI_API_KEY"; api_key_value="$${OPENAI_API_KEY:-}" ;; \
		anthropic) api_key_name="ANTHROPIC_API_KEY"; api_key_value="$${ANTHROPIC_API_KEY:-}" ;; \
		mistral) api_key_name="MISTRAL_API_KEY"; api_key_value="$${MISTRAL_API_KEY:-}" ;; \
		"") echo "Error: LLM_PROVIDER is not set. Set it in the environment or .env to one of: openai, anthropic, mistral." >&2; exit 1 ;; \
		*) echo "Error: Unsupported LLM_PROVIDER=$$provider. Allowed values: openai, anthropic, mistral." >&2; exit 1 ;; \
	esac; \
	if [ -z "$$api_key_value" ]; then \
		echo "Error: $$api_key_name is not set. Set it in the environment or .env." >&2; \
		exit 1; \
	fi; \
	echo "Using LLM_PROVIDER=$$provider"; \
	echo "Syncing dependencies with uv..."; \
	uv sync --all-groups; \
	echo "Downloading IFRS demo documents..."; \
	curl --fail --location --silent --show-error "$(DEMO_IFRS9_URL)" --output "$(DEMO_IFRS9_PDF)"; \
	curl --fail --location --silent --show-error "$(DEMO_IFRIC16_URL)" --output "$(DEMO_IFRIC16_PDF)"; \
	echo "Ingesting IFRS 9..."; \
	uv run python -m src.cli store "$(DEMO_IFRS9_PDF)" --doc-uid ifrs-9; \
	echo "Ingesting IFRIC 16..."; \
	uv run python -m src.cli store "$(DEMO_IFRIC16_PDF)" --doc-uid ifric-16; \
	echo "Asking demo question via the CLI..."; \
	question='Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?'; \
	printf '%s\n' "$$question" | uv run python -m src.cli answer -k 5 -e 5 --min-score 0.55; \
	printf '\nPress Enter to launch the Streamlit app...'; \
	read -r _; \
	exec uv run streamlit run streamlit_app.py
