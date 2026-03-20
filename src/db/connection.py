"""Database connection management for IFRS Expert."""

import logging
import sqlite3
from pathlib import Path

logger = logging.getLogger(__name__)

# Database path - data directory relative to project root
DB_PATH: Path = Path(__file__).parent.parent.parent / "data" / "db" / "ifrs.db"


def get_db_path() -> Path:
    """Get the database path, creating directory if needed."""
    db_path = DB_PATH
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return db_path


def init_db() -> None:
    """Initialize the database by running migrations."""
    db_path = get_db_path()
    logger.info(f"Initializing database at {db_path}")

    migrations_dir = Path(__file__).parent.parent / "migrations"

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row

        # Run all migration files in order
        for migration_file in sorted(migrations_dir.glob("*.sql")):
            logger.debug(f"Running migration: {migration_file.name}")
            conn.executescript(migration_file.read_text())

        conn.commit()
        logger.info(
            f"Database initialized with {len(list(migrations_dir.glob('*.sql')))} migrations"
        )


def get_connection(*, read_only: bool = False) -> sqlite3.Connection:
    """Get a database connection.

    Args:
        read_only: If True, open in read-only mode.

    Returns:
        SQLite connection with Row factory set.
    """
    db_path = get_db_path()
    if read_only:
        return sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    return sqlite3.connect(db_path)
