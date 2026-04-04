.PHONY: dev lint format test test-retrieval build demo eval

EXPERIMENT_DIR ?=
DESCRIPTION ?=
FAMILY ?=
VARIANT ?=
PROVIDER ?=
EXTRA_ARGS ?=

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

eval:
	@if [ -z "$(EXPERIMENT_DIR)" ]; then \
		echo "Error: EXPERIMENT_DIR is required"; \
		exit 1; \
	fi
	uv run python scripts/run_promptfoo_eval.py \
		--experiment-dir "$(EXPERIMENT_DIR)" \
		$(if $(DESCRIPTION),--description "$(DESCRIPTION)") \
		$(if $(FAMILY),--family "$(FAMILY)") \
		$(if $(VARIANT),--variant "$(VARIANT)") \
		$(if $(PROVIDER),--provider "$(PROVIDER)") \
		-- $(EXTRA_ARGS)

demo:
	@bash scripts/demo.sh
