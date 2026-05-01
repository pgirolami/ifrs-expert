"""Logging configuration for IFRS Expert."""

from __future__ import annotations

import logging
from pathlib import Path


def setup_logging() -> None:
    """Configure logging to write to ./logs/app.log with plain-text format."""
    logs_dir = Path("logs")
    logs_dir.mkdir(parents=True, exist_ok=True)
    log_path = logs_dir / "app.log"

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    for handler in list(root_logger.handlers):
        if isinstance(handler, logging.FileHandler) and Path(handler.baseFilename) == log_path.resolve():
            continue
        root_logger.removeHandler(handler)
        handler.close()

    for handler in root_logger.handlers:
        if isinstance(handler, logging.FileHandler) and Path(handler.baseFilename) == log_path.resolve():
            break
    else:
        handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
        handler.setLevel(logging.INFO)

        formatter = logging.Formatter(fmt="%(asctime)s - %(message)s", datefmt="%H:%M:%S")
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)

    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("huggingface_hub").setLevel(logging.WARNING)
    logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
