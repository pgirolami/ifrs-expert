"""Tests for the documents2 retrieval modes in policy loading."""

from __future__ import annotations

from pathlib import Path

from src.policy import load_policy_config
from tests.policy import make_retrieval_policy


def test_load_policy_config_accepts_explicit_documents2_through_chunks_mode() -> None:
    """Policy config should load an explicit documents2-through-chunks policy."""
    project_root = Path(__file__).resolve().parents[2]
    policy_path = project_root / "config" / "policy.default.yaml"

    config = load_policy_config(policy_path, "documents2_through_chunks__enriched")

    if config.retrieval.policy_name != "documents2_through_chunks__enriched":
        message = f"Expected documents2_through_chunks__enriched policy, got {config.retrieval.policy_name}"
        raise AssertionError(message)
    if config.retrieval.document_routing.source != "top_chunk_results":
        message = f"Expected top_chunk_results source, got {config.retrieval.document_routing.source}"
        raise AssertionError(message)


def test_make_retrieval_policy_accepts_documents2_mode() -> None:
    """Test helper should still construct a document-representation policy for old document tests."""
    policy = make_retrieval_policy(mode="documents2")

    if policy.policy_name != "documents2":
        message = f"Expected documents2 policy name, got {policy.policy_name}"
        raise AssertionError(message)
    if policy.document_routing.source != "document_representation":
        message = f"Expected document_representation source, got {policy.document_routing.source}"
        raise AssertionError(message)
