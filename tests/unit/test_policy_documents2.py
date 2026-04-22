"""Tests for the documents2 retrieval modes in policy loading."""

from __future__ import annotations

from pathlib import Path

from src.policy import load_policy_config


def test_load_policy_config_accepts_documents2_mode() -> None:
    """Policy config should accept documents2 as a retrieval mode."""
    project_root = Path(__file__).resolve().parents[2]
    policy_path = project_root / "config" / "policy.default.yaml"

    config = load_policy_config(policy_path)

    if config.retrieval.mode != "documents2":
        message = f"Expected documents2 mode, got {config.retrieval.mode}"
        raise AssertionError(message)


def test_load_policy_config_accepts_documents2_through_chunks_mode(tmp_path: Path) -> None:
    """Policy config should accept documents2-through-chunks as a retrieval mode."""
    project_root = Path(__file__).resolve().parents[2]
    policy_path = project_root / "config" / "policy.default.yaml"
    temp_policy_path = tmp_path / "policy.yaml"
    temp_policy_path.write_text(policy_path.read_text(encoding="utf-8").replace("mode: documents2", "mode: documents2-through-chunks"), encoding="utf-8")

    config = load_policy_config(temp_policy_path)

    if config.retrieval.mode != "documents2-through-chunks":
        message = f"Expected documents2-through-chunks mode, got {config.retrieval.mode}"
        raise AssertionError(message)
