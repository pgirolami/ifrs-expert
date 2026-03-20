.PHONY: dev lint format test test-retrieval build

dev:
	uv sync --all-groups

lint:
	uv run ruff format --check && uv run ruff check && uv run ty check src/

format:
	uv run ruff format .

test:
	uv run pytest

test-retrieval:
	uv run pytest tests/retrieval/ --no-cov

build:
	uv build
