# AGENTS.md — Project Guide for AI Assistants

> This file guides AI assistants working on the IFRS Expert implementation.
> It defines project structure, coding standards, and common patterns.

---

## Project Overview

**Project name:** IFRS Expert Assistant  
**Type:** Local AI assistant for IFRS accounting guidance  
**Core functionality:** Grounded Q&A, clarification-first workflow, memo drafting with citations  
**Target users:** Accounting professionals seeking IFRS guidance

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.11+ |
| Database | SQLite3 (via `sqlite3` stdlib) |
| UI | Streamlit |
| Vector Index | FAISS (via `faiss-cpu`) |
| Embeddings | `sentence-transformers` |
| Testing | `pytest` + `pytest-asyncio` |
| Type Checking | `ty` |
| Linting | `ruff` |
| Formatting | `ruff format` |

---

## Code Quality Standards

### Type Hints (Strict)

All code **must** use full type annotations. No `Any`, no implicit `Optional`.

```python
# ✅ Good
def get_chunk_by_id(chunk_id: str) -> Chunk | None:
    ...

# ❌ Bad
def get_chunk_by_id(chunkId):
    ...
```

Run `pyright --strict` before committing.

### No Bare Exceptions

Always catch specific exceptions:

```python
# ✅ Good
try:
    result = query.execute()
except sqlite3.OperationalError as e:
    logger.error(f"Database error: {e}")
    raise

# ❌ Bad
try:
    result = query.execute()
except:
    ...
```

### Async vs Sync

- **I/O-bound** (database, file, HTTP): use `async`/`await` with `asyncio`
- **CPU-bound**: keep synchronous in thread pool or use `run_in_executor`

Streamlit handlers run in the event loop—use `asyncio` carefully or run blocking calls in threads.

### F-strings (Required)

**Always use f-strings for string formatting.** No %-formatting, no `.format()`, even in logging.

```python
# ✅ Good
logger.info(f"Retrieved {len(chunks)} chunks for query")
logger.warning(f"Document not found: doc_uid={doc_uid}")
result_msg = f"Processed {count} items in {elapsed:.2f}s"

# ❌ Bad
logger.info("Retrieved %d chunks for query", len(chunks))
logger.warning("Document not found: doc_uid=%s", doc_uid)
result_msg = "Processed {} items".format(count)
```

### Logging

Use the following logging pattern:

```python
import logging

logger = logging.getLogger(__name__)
```

Use f-strings for all log messages:

```python
logger.debug(f"Entering function with params: {param1}, {param2}")
logger.info(f"Retrieved {len(chunks)} chunks for query: {query[:50]}...")
logger.warning(f"Document not found: doc_uid={doc_uid}")
logger.error(f"Database connection failed after {retries} attempts")
```

If the f-string parameter needs to do conditional processing, use a local variable to precompute the variable's text formatting:

```python
# variable time_ms has type (float | None)

# ✅ Good
time_ms_string = f"{time_ms:.2f}" if time_ms else ""
logger.info(f"Runtime was {time_ms_string}.")

# ❌ Bad
logger.info(f"Runtime was {time_ms:.2f}.")
```

| Level | Use |
|-------|-----|
| `DEBUG` | Detailed flow info, variable values |
| `INFO` | Normal operation events |
| `WARNING` | Recoverable issues (missing doc, fallback) |
| `ERROR` | Failures requiring attention |

Use logging throughout the code to tell the story of what's happening: I want to be able to read the logs and follow the execution path. You **don't** need a log for every function entry & exit but you should have a log for important things decided or computed within functions

### Naming Conventions & Class Preference

Follow these naming conventions:

| Category | Convention | Example |
|----------|------------|---------|
| Functions | snake_case | `get_user_data`, `calculate_total`, `fetch_documents` |
| Classes | PascalCase | `UserService`, `DataController`, `RetrievalEngine` |
| Constants | UPPER_SNAKE_CASE | `API_KEY`, `MAX_RETRIES`, `DEFAULT_TOP_K` |
| Modules/files | snake_case | `connection.py`, `query_builder.py` |
| Instance variables | snake_case | `self.user_id`, `self.result_count` |

**Classes over top-level functions:**

Prefer organizing related functionality into classes rather than having many top-level global functions.

```python
# ✅ Good - organized as a class
class DocumentStore:
    def __init__(self, db_path: Path):
        self._db_path = db_path
    
    def get_document(self, doc_id: str) -> Document | None:
        ...
    
    def list_documents(self, filters: list[str] | None = None) -> list[Document]:
        ...

# Usage
store = DocumentStore(db_path)
docs = store.list_documents()
```

```python
# ❌ Bad - scattered top-level functions
def get_document(doc_id: str) -> Document | None:
    ...

def list_documents(filters: list[str] | None = None) -> list[Document]:
    ...

def create_document(...) -> Document:
    ...

def update_document(...) -> Document:
    ...
```

**Exceptions for simple utilities:**

Simple pure functions that are clearly standalone (e.g., helpers, validators) are acceptable at module level.

```python
# Acceptable - simple utility functions
def validate_doc_id(doc_id: str) -> bool:
    """Validate document ID format."""
    return len(doc_id) > 0 and "/" not in doc_id

def normalize_whitespace(text: str) -> str:
    """Normalize whitespace in text."""
    return " ".join(text.split())
```

---

## Database Patterns

### Connection Management

Use SQLite's built-in context manager directly — no helper function needed:

```python
# src/db/connection.py
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / "data" / "db" / "ifrs.db"

# Usage: each function manages its own connection with a context manager
def insert_document(values: dict) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        conn.execute("INSERT INTO docs (...) VALUES (...)", values)

def fetch_document(doc_uid: str) -> dict | None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT * FROM docs WHERE doc_uid = ?",
            (doc_uid,)
        ).fetchone()
        return dict(row) if row else None
```

**Key points:**
- Use `with sqlite3.connect(path) as conn:` — SQLite's context manager handles commit/rollback automatically
- Set `row_factory` inside the context manager for each operation
- For read-only, use `mode="readonly"` parameter

### Schema Migration

Use versioned SQL migration files:

```python
migrations/
├── 001_create_docs.sql
├── 002_create_chunks.sql
└── 003_create_interactions.sql
```

Run migrations on startup:

```python
def run_migrations(conn: sqlite3.Connection) -> None:
    migrations_dir = Path(__file__).parent.parent / "migrations"
    for migration in sorted(migrations_dir.glob("*.sql")):
        conn.executescript(migration.read_text())
```

### Query Functions

Return typed dataclasses, not raw rows:

```python
@dataclass
class Document:
    doc_uid: str
    doc_family_id: str
    doc_title: str
    doc_type: str
    version_label: str
    is_latest: bool

def get_document_by_uid(conn: sqlite3.Connection, doc_uid: str) -> Document | None:
    row = conn.execute(
        "SELECT doc_uid, doc_family_id, doc_title, doc_type, version_label, is_latest "
        "FROM docs WHERE doc_uid = ?",
        (docUid,)
    ).fetchone()
    if row is None:
        return None
    return Document(**dict(row))
```

### Mutation Functions

Use the same typed dataclasses as the query functions return. If you have a good reason not to, prompt the user for review.

---

## Streamlit Patterns

### Session State Initialization

Always initialize session state at the top of `app.py`:

```python
if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_interaction" not in st.session_state:
    st.session_state.current_interaction = None
```

### Separation of UI and Logic

Keep Streamlit code minimal in `app.py`. Delegate to components:

```python
# src/ui/app.py
import streamlit as st
from src.ui.components import render_chat, render_citations

def main():
    st.title("IFRS Expert Assistant")
    
    render_chat()
    
    if st.session_state.get("show_citations"):
        render_citations(st.session_state.last_response.citations)
```

### Caching

Use `@st.cache_data` for expensive, deterministic operations:

```python
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "db" / "ifrs.db"

@st.cache_data(ttl=3600)
def load_corpus_stats() -> dict:
    with sqlite3.connect(DB_PATH) as conn:
        return {
            "doc_count": conn.execute("SELECT COUNT(*) FROM docs").fetchone()[0],
            "chunk_count": conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0],
        }
```

Use `@st.cache_resource` for singletons (FAISS index, embedder):

```python
@st.cache_resource
def get_faiss_index() -> faiss.Index:
    return faiss.read_index(str(INDEX_PATH))
```

---

## Testing Standards

### Test Organization

```
tests/
├── unit/              # Fast, isolated tests
├── integration/       # Tests requiring DB/index
└── fixtures/         # Shared test data
```

### Testing and Mocking

Follow `docs/testing_policy.md`.

Non-negotiable rules:
- Prefer dependency injection and small fakes over mocks and monkey-patching.
- Mock only external boundaries.
- Do not add bare `MagicMock`; use autospecced mocks only when a fake is not practical.
- Do not add new internal monkey-patching as routine test setup.
- Treat tests with more than two patches as refactoring candidates.

### Fixtures for Database

Use pytest fixtures for isolated test databases & give the test database a unique name:

```python
import pytest
import sqlite3
import tempfile
from pathlib import Path

@pytest.fixture
def temp_db():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        # Run migrations
        run_migrations(conn)
        yield conn
        conn.close()
```

### Test Naming

Follow `test_<module>_<behavior>` (snake_case):

```python
def test_retrieval_returns_chunk_metadata():
    ...

def test_intake_detects_missing_facts():
    ...
```

### Assertions

Use descriptive assertions:

```python
assert retrieved_chunks, "Expected at least one retrieved chunk"
assert chunk.doc_uid == expected_doc_uid, f"Expected {expected_doc_uid}, got {chunk.doc_uid}"
```

---

## Linting & Formatting

### Ruff Configuration (`ruff.toml`)

Do not ignore rules without user consent: fix the actual code issues.

### Pre-commit Hook

Install pre-commit to run checks before commits:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: local
    hooks:
      - id: ty
        name: ty
        entry: uv
        args: ["run", "ty"]
        language: system
        types: [python]
        pass_filenames: true
```

---

## Dependency Management

All dependency management, virtual environments, and package installation is done via [`uv`](https://github.com/astral-sh/uv).

### Workflow with uv

```bash
# Create virtual environment and install dependencies
uv venv
uv sync

# Add a new dependency
uv add package-name
uv add --dev package-name --group dev

# Update dependencies
uv lock --upgrade

# Run commands in the virtual environment
uv run streamlit run src/ui/app.py
uv run pytest tests/ -v
uv run pyright --strict

# Or activate the venv first
source .venv/bin/activate
streamlit run src/ui/app.py
```

---

## Common Patterns

### Result Types

Avoid returning `None` for errors. Use Result types:

```python
from dataclasses import dataclass

@dataclass
class RetrievalResult:
    chunks: list[Chunk]
    query: str
    latency_ms: float

@dataclass
class RetrievalError:
    message: str
    query: str

RetrievalOutcome = RetrievalResult | RetrievalError
```

### Configuration

Stable configuration lives in a YAML file. Use environment variables only for secrets or machine-specific overrides.

**`config.yaml`** (committed to repo):
```yaml
# config.yaml - stable configuration
database:
  path: "./corpus/data/db/ifrs.db"

retrieval:
  index_path: "./corpus/data/index/faiss.index"
  embedding_model: "sentence-transformers/all-MiniLM-L6-v2"
  top_k: 10

ingestion:
  chunk_size: 512
  chunk_overlap: 50

ui:
  title: "IFRS Expert Assistant"
  show_sources: true
```

**`config.yaml.example`** (for reference):
```yaml
# config.yaml.example - template with all options
# Copy to config.yaml and adjust values
```

**Loading configuration** (in `src/config.py`):
```python
import yaml
from pathlib import Path
from functools import lru_cache

CONFIG_PATH = Path(__file__).parent.parent / "config.yaml"

@lru_cache
def get_config() -> dict:
    """Load configuration from YAML file."""
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Config file not found: {CONFIG_PATH}")
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)

# Usage
config = get_config()
db_path = config["database"]["path"]
```

**Environment variables for overrides:**
```python
import os

# Override from environment (for secrets, CI, etc.)
API_KEY = os.environ.get("IFRS_API_KEY", config["api"]["key"])  # fallback to config
```

> **Why YAML?** It's human-readable, version-control friendly, and avoids hardcoding defaults in Python code.

### CLI Commands (Command Pattern)

CLI commands are implemented using the **Command Pattern** for better separation of concerns, testability, and extensibility.

**Structure:**
```
src/
├── cli.py                 # Entry point - parses args and dispatches to commands
└── commands/
    ├── __init__.py        # Exports all commands
    ├── store.py           # StoreCommand - ingest captures and store chunks
    ├── chunk.py           # ChunkCommand - manage chunks
    ├── query.py           # QueryCommand - run retrieval queries
    ├── list.py            # ListCommand - list documents/chunks
    └── answer.py          # AnswerCommand - answer questions
```

**Base Command Pattern:**

Each command is a class with:
- Constructor accepts dependencies/parameters
- `execute()` method returns the result (typically a string)

```python
class StoreCommand:
    """Extract chunks from an HTML capture and store them in the database and vector index."""

    def __init__(self, html_path: Path, doc_uid: str | None = None):
        self.html_path = html_path
        self.doc_uid = doc_uid or html_path.stem

    def execute(self) -> str:
        """Execute the command and return a result message."""
        if not self.html_path.exists():
            return f"Error: HTML file not found: {self.html_path}"

        try:
            # ... implementation ...
            return f"Stored {len(chunks)} chunks for doc_uid={self.doc_uid}"
        except Exception as e:
            logger.exception("Error storing chunks")
            return f"Error: {e}"
```

**CLI Entry Point** (`src/cli.py`):

The CLI entry point uses subparsers and dispatches to command classes:

```python
def main() -> None:
    parser = argparse.ArgumentParser(description="IFRS Expert CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Store subcommand
    store_parser = subparsers.add_parser("store", help="Store HTML capture chunks")
    store_parser.add_argument("html_path", type=Path, help="Path to HTML capture file")
    store_parser.add_argument("--doc-uid", type=str, help="Document UID")
    store_parser.set_defaults(func=_run_store)

    # Answer subcommand
    answer_parser = subparsers.add_parser("answer", help="Answer a question")
    answer_parser.add_argument("question", help="Question to answer")
    answer_parser.add_argument("--verbose", action="store_true")
    answer_parser.set_defaults(func=_run_answer)

    args = parser.parse_args()
    args.func(args)


def _run_store(args: argparse.Namespace) -> None:
    cmd = StoreCommand(html_path=args.html_path, doc_uid=args.doc_uid)
    print(cmd.execute())


def _run_answer(args: argparse.Namespace) -> None:
    cmd = AnswerCommand(question=args.question, verbose=args.verbose)
    print(cmd.execute())
```

**Running via uv:**

```bash
# Run CLI commands directly with Python module
uv run python -m src.cli store ./capture.html
uv run python -m src.cli answer "What is revenue recognition?"
uv run python -m src.cli list --doc-uid ifrs15

# Or read query from stdin
echo "What is revenue recognition?" | uv run python -m src.cli answer -k 5
```
uv run python -m src.cli list --doc-uid ifrs15

# Or read query from stdin
echo "What is revenue recognition?" | uv run python -m src.cli answer -k 5
```

**Or via Makefile:**
```bash
make dev      # Install all dependencies
make lint    # Run linters
make format  # Format code
make test    # Run tests
```

**Why Command Pattern?**
- ✅ **Testable:** Commands can be unit tested in isolation
- ✅ **Composable:** Easy to invoke commands from other code (e.g., Streamlit)
- ✅ **Separated:** CLI parsing logic is separate from business logic
- ✅ **Extensible:** Add new commands without modifying existing code

---

## CI/CD Expectations

All Pull Requests must pass:

1. **Format:** `make format`
2. **Lint:** `make lint`
4. **Test:** `make test`

Do not add rules to ignore in Ruff without user approval.

---

*Last updated: 2026-03-26*
