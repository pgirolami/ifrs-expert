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
        per_type_d = {"IFRS-S": 4, "IAS-S": 10, "IAS-BCIASC": 1, "IAS-SM": 1, "IFRIC": 6, "SIC": 6, "PS": 1, "NAVIS": 2}
    if per_type_min_score is None:
        per_type_min_score = {
            "IFRS-S": 0.53,
            "IAS-S": 0.4,
            "IAS-BCIASC": 0.62,
            "IAS-SM": 0.62,
            "IFRIC": 0.48,
            "SIC": 0.4,
            "PS": 0.4,
            "NAVIS": 0.6,
        }
    by_document_type = {
        doc_type: DocumentTypeRetrievalPolicy(d=d_val, min_score=ms_val, expand_to_section=expand_to_section_val)
        for doc_type, d_val, ms_val, expand_to_section_val in [
            # IFRS Standards and variants
            ("IFRS-S", per_type_d.get("IFRS-S", 4), per_type_min_score.get("IFRS-S", 0.53), True),
            ("IFRS-BC", per_type_d.get("IFRS-BC", 1), per_type_min_score.get("IFRS-BC", 0.62), False),
            ("IFRS-IE", per_type_d.get("IFRS-IE", 1), per_type_min_score.get("IFRS-IE", 0.6), False),
            ("IFRS-IG", per_type_d.get("IFRS-IG", 1), per_type_min_score.get("IFRS-IG", 0.56), True),
            # IAS Standards and variants
            ("IAS-S", per_type_d.get("IAS-S", 10), per_type_min_score.get("IAS-S", 0.4), True),
            ("IAS-BC", per_type_d.get("IAS-BC", 1), per_type_min_score.get("IAS-BC", 0.62), False),
            ("IAS-BCIASC", per_type_d.get("IAS-BCIASC", 1), per_type_min_score.get("IAS-BCIASC", 0.62), False),
            ("IAS-IE", per_type_d.get("IAS-IE", 1), per_type_min_score.get("IAS-IE", 0.6), False),
            ("IAS-IG", per_type_d.get("IAS-IG", 1), per_type_min_score.get("IAS-IG", 0.56), True),
            ("IAS-SM", per_type_d.get("IAS-SM", 1), per_type_min_score.get("IAS-SM", 0.62), False),
            # IFRIC Interpretations and variants
            ("IFRIC", per_type_d.get("IFRIC", 6), per_type_min_score.get("IFRIC", 0.48), True),
            ("IFRIC-BC", per_type_d.get("IFRIC-BC", 1), per_type_min_score.get("IFRIC-BC", 0.62), False),
            ("IFRIC-IE", per_type_d.get("IFRIC-IE", 1), per_type_min_score.get("IFRIC-IE", 0.6), False),
            ("IFRIC-IG", per_type_d.get("IFRIC-IG", 1), per_type_min_score.get("IFRIC-IG", 0.56), True),
            # SIC Interpretations and variants
            ("SIC", per_type_d.get("SIC", 6), per_type_min_score.get("SIC", 0.4), True),
            ("SIC-BC", per_type_d.get("SIC-BC", 1), per_type_min_score.get("SIC-BC", 0.62), False),
            ("SIC-IE", per_type_d.get("SIC-IE", 1), per_type_min_score.get("SIC-IE", 0.6), False),
            # Practice Statements and variants
            ("PS", per_type_d.get("PS", 1), per_type_min_score.get("PS", 0.4), True),
            ("PS-BC", per_type_d.get("PS-BC", 1), per_type_min_score.get("PS-BC", 0.62), False),
            # Other
            ("NAVIS", per_type_d.get("NAVIS", 2), per_type_min_score.get("NAVIS", 0.6), True),
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
