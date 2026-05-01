"""Tests for shared logging configuration."""

from __future__ import annotations

import logging
from pathlib import Path

from src.logging_config import setup_logging


def test_setup_logging_keeps_file_output_and_removes_console_handlers(tmp_path: Path, monkeypatch) -> None:
    """setup_logging should keep logs in the file and remove non-file handlers."""
    monkeypatch.chdir(tmp_path)

    root_logger = logging.getLogger()
    original_handlers = list(root_logger.handlers)
    original_level = root_logger.level

    try:
        for handler in list(root_logger.handlers):
            root_logger.removeHandler(handler)
            handler.close()

        console_handler = logging.StreamHandler()
        root_logger.addHandler(console_handler)

        setup_logging()

        handlers = list(root_logger.handlers)
        assert len(handlers) == 1
        assert isinstance(handlers[0], logging.FileHandler)
        assert Path(handlers[0].baseFilename) == tmp_path / "logs" / "app.log"

        logging.getLogger("src.retrieval.query_embedding").info("test message")
        log_text = (tmp_path / "logs" / "app.log").read_text(encoding="utf-8")
        assert "test message" in log_text
    finally:
        for handler in list(root_logger.handlers):
            root_logger.removeHandler(handler)
            handler.close()
        for handler in original_handlers:
            root_logger.addHandler(handler)
        root_logger.setLevel(original_level)

