#!/usr/bin/env uv run python
"""
Probe script for experiment 34 — field availability + Q1.0 ranking per field.

Run from the repository root:
    uv run python experiments/34_retrieval_alternatives/probe_q1_field_availability.py

Outputs field-availability stats and per-field top-20 rankings for Q1.0.
Q1.0: "Est-ce que je peux appliquer une documentation de couverture dans les comptes
consolidés sur la partie change relative aux dividendes intragroupe pour lesquels
une créance à recevoir a été comptabilisée ?"
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure repo root is on sys.path so 'src' imports work from any cwd
_repo_root = Path(__file__).parent.parent.parent.resolve()
if str(_repo_root) not in sys.path:
    sys.path.insert(0, str(_repo_root))

import sqlite3

import numpy as np
from sentence_transformers import SentenceTransformer

# Matches the project's MAX_EMBEDDING_TEXT_CHARS = 8000 * 3 = 24000.
_TRUNCATE_CHARS = 24_000
# CPU is used because MPS hangs in this environment.
_EMBEDDING_MODEL = "BAAI/bge-m3"
_EMBEDDING_DEVICE = "cpu"


def _get_model() -> SentenceTransformer:
    """Load the embedding model (cached on first call)."""
    if not hasattr(_get_model, "_model"):
        _get_model._model = SentenceTransformer(_EMBEDDING_MODEL, device=_EMBEDDING_DEVICE)
    return _get_model._model  # type: ignore[return-value]


def _truncate(text: str) -> str:
    """Truncate text to the configured character budget."""
    return text[:_TRUNCATE_CHARS]

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

DB_PATH = Path("corpus/data/db/ifrs.db")
MODEL_NAME = "BAAI/bge-m3"
Q1_QUERY = (
    "Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés "
    "sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?"
)
TARGET_DOCS = frozenset(("ifrs9", "ifrs9-bc", "ifric16", "ifric16-bc"))
FIELDS = (
    "background_text",
    "issue_text",
    "objective_text",
    "scope_text",
    "intro_text",
    "toc_text",
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def load_field_stats(conn: sqlite3.Connection, field: str) -> tuple[int, float, int, int]:
    """Return (populated_count, avg_chars, min_chars, max_chars) for field."""
    row = conn.execute(f"""
        SELECT
            COUNT(*) AS total,
            ROUND(AVG(len), 1) AS avg_len,
            MIN(len) AS min_len,
            MAX(len) AS max_len
        FROM (
            SELECT LENGTH(TRIM(COALESCE({field}, ''))) AS len
            FROM documents
            WHERE LENGTH(TRIM(COALESCE({field}, ''))) > 0
        )
    """).fetchone()
    return (row[0], row[1], row[2], row[3])


def load_field_documents(conn: sqlite3.Connection, field: str) -> list[tuple[str, str]]:
    """Return [(doc_uid, text), ...] for docs with non-empty field."""
    rows = conn.execute(f"""
        SELECT doc_uid, {field}
        FROM documents
        WHERE LENGTH(TRIM(COALESCE({field}, ''))) > 0
        ORDER BY doc_uid
    """).fetchall()
    return [(r[0], r[1]) for r in rows]


def run_probe(query: str, doc_texts: list[tuple[str, str]], model_name: str) -> list[tuple[str, float]]:
    """Return [(doc_uid, score), ...] sorted by descending score."""
    doc_uids = [d[0] for d in doc_texts]
    texts = [_truncate(d[1]) for d in doc_texts]
    if not texts:
        return []

    model = _get_model()
    q_emb = model.encode([query]).astype("float32")
    q_emb = q_emb / np.linalg.norm(q_emb, axis=1, keepdims=True)
    embs = model.encode(texts, batch_size=1, show_progress_bar=False)
    embs = embs / np.linalg.norm(embs, axis=1, keepdims=True)
    scores = (embs @ q_emb.T).flatten()
    return sorted(zip(doc_uids, scores), key=lambda x: x[1], reverse=True)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("# Field availability\n")
    print("| Field | Populated docs | Avg chars | Min chars | Max chars |")
    print("| --- | ---: | ---: | ---: | ---: |")
    for field in FIELDS:
        total, avg, mn, mx = load_field_stats(conn, field)
        print(f"| `{field}` | {total} | {avg} | {mn} | {mx} |")

    print("\n# Q1.0 probe — top 20 per field\n")
    for field in FIELDS:
        docs = load_field_documents(conn, field)
        if not docs:
            print(f"## `{field}` — no populated documents\n")
            print("| Rank | doc_uid | Score |")
            print("| ---: | --- | ---: |")
            print("| — | _no documents_ | — |")
            print()
            continue

        ranked = run_probe(Q1_QUERY, docs, MODEL_NAME)

        print(f"## `{field}` — {len(docs)} documents\n")
        print("| Rank | doc_uid | Score | Target? |")
        print("| ---: | --- | ---: | --- |")
        for i, (uid, score) in enumerate(ranked[:20], 1):
            marker = " <<<" if uid in TARGET_DOCS else ""
            target_flag = "✅" if uid in TARGET_DOCS else ""
            print(f"| {i:2d} | `{uid}` | {score:.4f} | {target_flag}{marker} |")
        print()


if __name__ == "__main__":
    main()
