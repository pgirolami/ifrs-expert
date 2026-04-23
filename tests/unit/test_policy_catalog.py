"""Tests for the retrieval policy catalog and resolver."""

from __future__ import annotations

from pathlib import Path

import pytest

from src.policy import load_policy_catalog, resolve_retrieval_policy


def test_load_policy_catalog_reads_default_catalog() -> None:
    """The default policy file should load as a policy catalog."""
    project_root = Path(__file__).resolve().parents[2]
    catalog = load_policy_catalog(project_root / "config" / "policy.default.yaml")

    assert "enriched" in catalog.querying
    assert "documents2_through_chunks__enriched" in catalog.retrieval_policies
    assert "dense_chunks" in catalog.chunk_retrieval_strategies
    assert "through_chunks" in catalog.document_routing_strategies


def test_resolve_retrieval_policy_resolves_strategy_scoped_profiles() -> None:
    """The resolver should assemble strategy-scoped routing and chunk retrieval profiles."""
    project_root = Path(__file__).resolve().parents[2]
    catalog = load_policy_catalog(project_root / "config" / "policy.default.yaml")

    policy = resolve_retrieval_policy(catalog, "full_documents__enriched")

    assert policy.querying.embedding_mode == "enriched"
    assert policy.document_routing.source == "document_representation"
    assert policy.document_routing.profile == "q1_authority_family_full_repr"
    assert policy.document_routing.profile_config.by_document_type["IFRS-S"].similarity_representation == "full"
    assert policy.chunk_retrieval.mode == "chunk_similarity"
    assert policy.chunk_retrieval.profile == "default"
    assert policy.chunk_retrieval.profile_config.filter.per_document_k == 5


def test_resolve_retrieval_policy_rejects_unknown_querying_reference(tmp_path: Path) -> None:
    """Unknown querying references should fail fast."""
    project_root = Path(__file__).resolve().parents[2]
    catalog_text = (project_root / "config" / "policy.default.yaml").read_text(encoding="utf-8")
    invalid_text = catalog_text.replace("querying: enriched", "querying: missing_querying", 1)
    policy_path = tmp_path / "policy.invalid.yaml"
    policy_path.write_text(invalid_text, encoding="utf-8")

    catalog = load_policy_catalog(policy_path)

    with pytest.raises(ValueError, match="Unknown querying reference: missing_querying"):
        resolve_retrieval_policy(catalog, "documents2_through_chunks__enriched")


def test_resolve_retrieval_policy_rejects_strategy_profile_mismatch(tmp_path: Path) -> None:
    """Chunk retrieval profiles should be scoped to the chosen strategy."""
    project_root = Path(__file__).resolve().parents[2]
    catalog_text = (project_root / "config" / "policy.default.yaml").read_text(encoding="utf-8")
    invalid_text = catalog_text.replace("profile: titles_default", "profile: default", 1)
    policy_path = tmp_path / "policy.invalid.yaml"
    policy_path.write_text(invalid_text, encoding="utf-8")

    catalog = load_policy_catalog(policy_path)

    with pytest.raises(ValueError, match="Unknown chunk retrieval profile: default for strategy title_chunks"):
        resolve_retrieval_policy(catalog, "titles__enriched")
