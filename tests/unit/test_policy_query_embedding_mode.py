"""Tests for retrieval.query_embedding_mode policy loading."""

from __future__ import annotations

from pathlib import Path

import pytest

from src.policy import load_policy_config


def test_load_policy_config_reads_default_query_embedding_mode() -> None:
    """The default policy should declare enriched query embedding mode."""
    project_root = Path(__file__).resolve().parents[2]
    policy = load_policy_config(project_root / "config" / "policy.default.yaml")

    assert policy.retrieval.query_embedding_mode == "enriched"


def test_load_policy_config_rejects_unknown_query_embedding_mode(tmp_path: Path) -> None:
    """Policy loading should reject unsupported query embedding modes."""
    project_root = Path(__file__).resolve().parents[2]
    default_policy_text = (project_root / "config" / "policy.default.yaml").read_text(encoding="utf-8")
    invalid_policy_text = default_policy_text.replace("embedding_mode: enriched", "embedding_mode: invalid", 1)
    policy_path = tmp_path / "policy.invalid.yaml"
    policy_path.write_text(invalid_policy_text, encoding="utf-8")

    with pytest.raises(ValueError, match="embedding_mode must be one of: raw, enriched"):
        load_policy_config(policy_path)
