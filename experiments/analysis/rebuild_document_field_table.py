"""Rebuild an experiment markdown table from the IFRS documents database.

This script exports one row per document with the raw contents of the document
representation fields. It intentionally leaves the Status column blank so the
result can be reviewed manually.
"""

from __future__ import annotations

import argparse
import logging
import sqlite3
from pathlib import Path

DEFAULT_DB_PATH = Path("corpus/data/db/ifrs.db")
DEFAULT_OUTPUT_PATH = Path("experiments/39_exhaustive_ifrs_ingestion_verification/EXPERIMENTS.md")
DEFAULT_GOAL = "Go over every single document on ifrs.org and ensure the fields in the database are properly populated"
MAX_CELL_CHARS = 1000

logger = logging.getLogger(__name__)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Rebuild an IFRS experiment table from the database")
    parser.add_argument("--db-path", type=Path, default=DEFAULT_DB_PATH, help=f"Path to the SQLite database (default: {DEFAULT_DB_PATH})")
    parser.add_argument("--output-path", type=Path, default=DEFAULT_OUTPUT_PATH, help=f"Path to the markdown file to overwrite (default: {DEFAULT_OUTPUT_PATH})")
    parser.add_argument("--goal", type=str, default=DEFAULT_GOAL, help="Goal text to place at the top of the markdown file")
    return parser


def _clean_cell(value: str | None) -> str:
    if value is None:
        return ""
    text = value.strip()
    if not text:
        return ""
    text = text.replace("|", r"\\|").replace("\n", "<br>")
    if len(text) <= MAX_CELL_CHARS:
        return text

    keep_chars = MAX_CELL_CHARS - 3
    head_chars = keep_chars // 2
    tail_chars = keep_chars - head_chars
    return f"{text[:head_chars]}<br><br><strong>(...)</strong><br><br>{text[-tail_chars:]}"


def _fetch_documents(db_path: Path) -> list[sqlite3.Row]:
    if not db_path.exists():
        message = f"Database file not found: {db_path}"
        raise FileNotFoundError(message)

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        return conn.execute(
            """
            SELECT doc_uid, background_text, issue_text, objective_text, scope_text, intro_text, toc_text
            FROM documents
            ORDER BY doc_uid
            """
        ).fetchall()


def _render_markdown(goal: str, rows: list[sqlite3.Row]) -> str:
    lines: list[str] = []
    lines.append("# Goal")
    lines.append("")
    lines.append(goal)
    lines.append("")
    lines.append("## Query result")
    lines.append("")
    lines.append(f"Total rows: {len(rows)}")
    lines.append("")
    lines.append("| doc_uid | Status | background_text | issue_text | objective_text | scope_text | intro_text | toc_text |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")

    lines.extend(
        [
            "| "
            + " | ".join(
                [
                    str(row["doc_uid"]),
                    "",
                    _clean_cell(row["background_text"]),
                    _clean_cell(row["issue_text"]),
                    _clean_cell(row["objective_text"]),
                    _clean_cell(row["scope_text"]),
                    _clean_cell(row["intro_text"]),
                    _clean_cell(row["toc_text"]),
                ]
            )
            + " |"
            for row in rows
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> int:
    """Run the table rebuild CLI."""
    parser = _build_parser()
    args = parser.parse_args()

    rows = _fetch_documents(args.db_path)
    markdown = _render_markdown(args.goal, rows)
    args.output_path.write_text(markdown, encoding="utf-8")
    logger.info(f"Wrote {args.output_path} with {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
