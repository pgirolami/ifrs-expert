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
	@bash scripts/demo.sh
