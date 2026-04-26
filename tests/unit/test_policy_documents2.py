"""Tests for the documents2 retrieval modes in policy loading."""

from __future__ import annotations

from pathlib import Path

from tests.policy import make_retrieval_policy
from src.policy import load_policy_config


def test_load_policy_config_accepts_documents2_through_chunks_mode() -> None:
    """Policy config should load the current documents2-through-chunks retrieval mode."""
    project_root = Path(__file__).resolve().parents[2]
    policy_path = project_root / "config" / "policy.default.yaml"

    config = load_policy_config(policy_path)

    if config.retrieval.mode != "documents2-through-chunks":
        message = f"Expected documents2-through-chunks mode, got {config.retrieval.mode}"
        raise AssertionError(message)


def test_make_retrieval_policy_accepts_documents2_mode() -> None:
    """Legacy documents2 mode should still be constructible for compatibility."""
    policy = make_retrieval_policy(mode="documents2")

    if policy.mode != "documents2":
        message = f"Expected documents2 mode, got {policy.mode}"
        raise AssertionError(message)
