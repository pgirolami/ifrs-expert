.PHONY: dev lint format test test-retrieval build demo eval eval-view eval-list eval-show guard-experiment-dir

EXPERIMENT_DIR ?=
DESCRIPTION ?=
FAMILY ?=
VARIANT ?=
PROVIDER ?=
EXTRA_ARGS ?=
EVAL_ID ?=

ifeq ($(filter /%,$(EXPERIMENT_DIR)),)
ifneq ($(filter experiments/%,$(EXPERIMENT_DIR)),)
RESOLVED_EXPERIMENT_DIR := $(EXPERIMENT_DIR)
else
RESOLVED_EXPERIMENT_DIR := experiments/$(EXPERIMENT_DIR)
endif
else
RESOLVED_EXPERIMENT_DIR := $(EXPERIMENT_DIR)
endif


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

guard-experiment-dir:
	@if [ -z "$(EXPERIMENT_DIR)" ]; then \
		echo "Error: EXPERIMENT_DIR is required"; \
		exit 1; \
	fi

eval: guard-experiment-dir
	PROMPTFOO_CONFIG_DIR="$(RESOLVED_EXPERIMENT_DIR)/.promptfoo" uv run python scripts/run_promptfoo_eval.py \
		--experiment-dir "$(EXPERIMENT_DIR)" \
		$(if $(DESCRIPTION),--description "$(DESCRIPTION)") \
		$(if $(FAMILY),--family "$(FAMILY)") \
		$(if $(VARIANT),--variant "$(VARIANT)") \
		$(if $(PROVIDER),--provider "$(PROVIDER)") \
		-- $(EXTRA_ARGS)

eval-view: guard-experiment-dir
	PROMPTFOO_CONFIG_DIR="$(RESOLVED_EXPERIMENT_DIR)/.promptfoo" npm exec -- promptfoo view -y

eval-list: guard-experiment-dir
	PROMPTFOO_CONFIG_DIR="$(RESOLVED_EXPERIMENT_DIR)/.promptfoo" npm exec -- promptfoo list evals

eval-show: guard-experiment-dir
	PROMPTFOO_CONFIG_DIR="$(RESOLVED_EXPERIMENT_DIR)/.promptfoo" npm exec -- promptfoo show eval $(EVAL_ID)

demo:
	@bash scripts/demo.sh
