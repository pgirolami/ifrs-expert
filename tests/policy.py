"""Policy helpers for tests."""

from __future__ import annotations

from pathlib import Path

from src.policy import (
    DocumentStageRetrievalPolicy,
    DocumentTypeRetrievalPolicy,
    PolicyConfig,
    RetrievalPolicy,
    TextStageRetrievalPolicy,
    TitleStageRetrievalPolicy,
    load_policy_config,
)


def load_test_policy_config() -> PolicyConfig:
    """Load the repository default policy config for tests."""
    project_root = Path(__file__).resolve().parents[1]
    return load_policy_config(project_root / "config" / "policy.default.yaml")


def load_test_retrieval_policy() -> RetrievalPolicy:
    """Load the retrieval portion of the default policy for command-options tests."""
    return load_test_policy_config().retrieval


def make_retrieval_policy(
    *,
    k: int = 5,
    d: int = 5,
    chunk_min_score: float = 0.53,
    expand: int = 0,
    full_doc_threshold: int = 0,
    expand_to_section: bool = True,
    mode: str = "text",
    per_type_d: dict[str, int] | None = None,
    per_type_min_score: dict[str, float] | None = None,
) -> RetrievalPolicy:
    """Build a RetrievalPolicy with specific numeric values for targeted tests."""
    if per_type_d is None:
        per_type_d = {"IFRS-S": 4, "IAS": 4, "IFRIC": 6, "SIC": 6, "PS": 1, "NAVIS": 2}
    if per_type_min_score is None:
        per_type_min_score = {
            "IFRS-S": 0.53,
            "IAS": 0.4,
            "IFRIC": 0.48,
            "SIC": 0.4,
            "PS": 0.4,
            "NAVIS": 0.6,
        }
    by_document_type = {
        doc_type: DocumentTypeRetrievalPolicy(d=d_val, min_score=ms_val, expand_to_section=True)
        for doc_type, d_val, ms_val in [
            ("IFRS-S", per_type_d.get("IFRS-S", 4), per_type_min_score.get("IFRS-S", 0.53)),
            ("IFRS-BC", per_type_d.get("IFRS-BC", 2), per_type_min_score.get("IFRS-BC", 0.5)),
            ("IFRS-IE", per_type_d.get("IFRS-IE", 2), per_type_min_score.get("IFRS-IE", 0.5)),
            ("IFRS-IG", per_type_d.get("IFRS-IG", 2), per_type_min_score.get("IFRS-IG", 0.5)),
            ("IAS", per_type_d.get("IAS", 4), per_type_min_score.get("IAS", 0.4)),
            ("IFRIC", per_type_d.get("IFRIC", 6), per_type_min_score.get("IFRIC", 0.48)),
            ("SIC", per_type_d.get("SIC", 6), per_type_min_score.get("SIC", 0.4)),
            ("PS", per_type_d.get("PS", 1), per_type_min_score.get("PS", 0.4)),
            ("NAVIS", per_type_d.get("NAVIS", 2), per_type_min_score.get("NAVIS", 0.6)),
        ]
    }
    return RetrievalPolicy(
        mode=mode,
        k=k,
        expand=expand,
        full_doc_threshold=full_doc_threshold,
        expand_to_section=expand_to_section,
        text=TextStageRetrievalPolicy(min_score=chunk_min_score),
        titles=TitleStageRetrievalPolicy(min_score=0.6),
        documents=DocumentStageRetrievalPolicy(global_d=d, by_document_type=by_document_type),
    )
