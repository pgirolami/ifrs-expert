"""Database connection management for IFRS Expert."""

from __future__ import annotations

import logging
import sqlite3
from pathlib import Path

logger = logging.getLogger(__name__)

DB_PATH: Path = Path(__file__).parent.parent.parent / "corpus" / "data" / "db" / "ifrs.db"


def get_db_path() -> Path:
    """Get the database path, creating its parent directory if needed."""
    db_path = DB_PATH
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return db_path


def init_db() -> None:
    """Initialize the database by applying pending migrations exactly once."""
    db_path = get_db_path()
    logger.info(f"Initializing database at {db_path}")

    migrations_dir = Path(__file__).parent.parent / "migrations"
    migration_files = sorted(migrations_dir.glob("*.sql"))

    with _configure_connection(sqlite3.connect(db_path)) as conn:
        conn.row_factory = sqlite3.Row
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS schema_migrations (
                name TEXT PRIMARY KEY,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        applied_migrations = {row["name"] for row in conn.execute("SELECT name FROM schema_migrations").fetchall()}

        applied_count = 0
        for migration_file in migration_files:
            if migration_file.name in applied_migrations:
                continue
            logger.debug(f"Running migration: {migration_file.name}")
            migration_sql = migration_file.read_text(encoding="utf-8")
            try:
                conn.executescript(migration_sql)
            except sqlite3.OperationalError as error:
                should_ignore_duplicate_document_kind = migration_file.name == "011_add_document_kind.sql" and "duplicate column name: document_kind" in str(error).lower()
                if not should_ignore_duplicate_document_kind:
                    raise
                logger.warning(f"Skipping duplicate document_kind column operation in {migration_file.name}")
            conn.execute(
                "INSERT INTO schema_migrations (name) VALUES (?)",
                (migration_file.name,),
            )
            applied_count += 1

        conn.commit()
        logger.info(f"Database initialized; applied {applied_count} new migration(s)")


def get_connection(*, read_only: bool = False) -> sqlite3.Connection:
    """Get a database connection."""
    db_path = get_db_path()
    if read_only:
        return _configure_connection(sqlite3.connect(f"file:{db_path}?mode=ro", uri=True))
    return _configure_connection(sqlite3.connect(db_path))


def _configure_connection(connection: sqlite3.Connection) -> sqlite3.Connection:
    """Apply required SQLite connection pragmas."""
    connection.execute("PRAGMA foreign_keys = ON")
    return connection
