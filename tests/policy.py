"""Policy helpers for tests."""

from __future__ import annotations

from pathlib import Path

from src.policy import (
    ChunkRetrievalExpansionConfig,
    ChunkRetrievalFilterConfig,
    ChunkRetrievalProfileConfig,
    DocumentRoutingPostProcessingConfig,
    DocumentRoutingProfileConfig,
    DocumentRoutingTypeConfig,
    DocumentStageRetrievalPolicy,
    DocumentTypeRetrievalPolicy,
    PolicyConfig,
    QueryEmbeddingMode,
    ResolvedChunkRetrievalPolicy,
    ResolvedDocumentRoutingPolicy,
    ResolvedQueryingPolicy,
    ResolvedRetrievalPolicy,
    RetrievalPolicy,
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
    query_embedding_mode: QueryEmbeddingMode = "raw",
) -> RetrievalPolicy:
    """Build a resolved retrieval policy with compatibility accessors for targeted tests."""
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

    per_type_similarity_representation: dict[str, str] = {
        "IFRS-S": "full",
        "IFRS-BC": "full",
        "IFRS-IE": "full",
        "IFRS-IG": "full",
        "IAS-S": "full",
        "IAS-BC": "full",
        "IAS-IE": "full",
        "IAS-IG": "full",
        "IAS-BCIASC": "full",
        "IAS-SM": "full",
        "IFRIC": "full",
        "IFRIC-BC": "full",
        "IFRIC-IE": "full",
        "IFRIC-IG": "full",
        "SIC": "full",
        "SIC-BC": "full",
        "SIC-IE": "full",
        "PS": "full",
        "PS-BC": "full",
        "NAVIS": "full",
    }
    legacy_by_document_type = {
        document_type: DocumentTypeRetrievalPolicy(
            d=d_val,
            min_score=ms_val,
            expand_to_section=expand_to_section_val,
            similarity_representation=per_type_similarity_representation.get(document_type),
        )
        for document_type, d_val, ms_val, expand_to_section_val in [
            ("IFRS-S", per_type_d.get("IFRS-S", 4), per_type_min_score.get("IFRS-S", 0.53), True),
            ("IFRS-BC", per_type_d.get("IFRS-BC", 1), per_type_min_score.get("IFRS-BC", 0.62), False),
            ("IFRS-IE", per_type_d.get("IFRS-IE", 1), per_type_min_score.get("IFRS-IE", 0.6), False),
            ("IFRS-IG", per_type_d.get("IFRS-IG", 1), per_type_min_score.get("IFRS-IG", 0.56), True),
            ("IAS-S", per_type_d.get("IAS-S", 10), per_type_min_score.get("IAS-S", 0.4), True),
            ("IAS-BC", per_type_d.get("IAS-BC", 1), per_type_min_score.get("IAS-BC", 0.62), False),
            ("IAS-BCIASC", per_type_d.get("IAS-BCIASC", 1), per_type_min_score.get("IAS-BCIASC", 0.62), False),
            ("IAS-IE", per_type_d.get("IAS-IE", 1), per_type_min_score.get("IAS-IE", 0.6), False),
            ("IAS-IG", per_type_d.get("IAS-IG", 1), per_type_min_score.get("IAS-IG", 0.56), True),
            ("IAS-SM", per_type_d.get("IAS-SM", 1), per_type_min_score.get("IAS-SM", 0.62), False),
            ("IFRIC", per_type_d.get("IFRIC", 6), per_type_min_score.get("IFRIC", 0.48), True),
            ("IFRIC-BC", per_type_d.get("IFRIC-BC", 1), per_type_min_score.get("IFRIC-BC", 0.62), False),
            ("IFRIC-IE", per_type_d.get("IFRIC-IE", 1), per_type_min_score.get("IFRIC-IE", 0.6), False),
            ("IFRIC-IG", per_type_d.get("IFRIC-IG", 1), per_type_min_score.get("IFRIC-IG", 0.56), True),
            ("SIC", per_type_d.get("SIC", 6), per_type_min_score.get("SIC", 0.4), True),
            ("SIC-BC", per_type_d.get("SIC-BC", 1), per_type_min_score.get("SIC-BC", 0.62), False),
            ("SIC-IE", per_type_d.get("SIC-IE", 1), per_type_min_score.get("SIC-IE", 0.6), False),
            ("PS", per_type_d.get("PS", 1), per_type_min_score.get("PS", 0.4), True),
            ("PS-BC", per_type_d.get("PS-BC", 1), per_type_min_score.get("PS-BC", 0.62), False),
            ("NAVIS", per_type_d.get("NAVIS", 2), per_type_min_score.get("NAVIS", 0.6), True),
        ]
    }

    legacy_document_stage = DocumentStageRetrievalPolicy(global_d=d, by_document_type=legacy_by_document_type)
    if mode == "titles":
        querying = ResolvedQueryingPolicy(embedding_mode=query_embedding_mode)
        chunk_profile = ChunkRetrievalProfileConfig(
            filter=ChunkRetrievalFilterConfig(min_score=chunk_min_score, per_document_k=k),
            expansion=None,
        )
        chunk_retrieval = ResolvedChunkRetrievalPolicy(strategy="title_chunks", mode="title_similarity", profile="titles_default", profile_config=chunk_profile)
        document_routing = ResolvedDocumentRoutingPolicy(
            strategy="return_all",
            source="all_documents",
            profile=None,
            profile_config=None,
            post_processing="none",
            post_processing_config=DocumentRoutingPostProcessingConfig(),
        )
        return ResolvedRetrievalPolicy(
            querying=querying,
            document_routing=document_routing,
            chunk_retrieval=chunk_retrieval,
            legacy_document_stage=legacy_document_stage,
            legacy_mode=mode,
        )

    querying = ResolvedQueryingPolicy(embedding_mode=query_embedding_mode)
    chunk_profile = ChunkRetrievalProfileConfig(
        filter=ChunkRetrievalFilterConfig(min_score=chunk_min_score, per_document_k=k),
        expansion=ChunkRetrievalExpansionConfig(expand=expand, expand_to_section=expand_to_section, full_doc_threshold=full_doc_threshold),
    )
    chunk_retrieval = ResolvedChunkRetrievalPolicy(strategy="dense_chunks", mode="chunk_similarity", profile="default", profile_config=chunk_profile)

    if mode == "documents2-through-chunks":
        document_routing = ResolvedDocumentRoutingPolicy(
            strategy="through_chunks",
            source="top_chunk_results",
            profile="q1_authority_family",
            profile_config=DocumentRoutingProfileConfig(global_d=d, by_document_type=legacy_by_document_type),
            post_processing="aggregate_to_main_variant",
            post_processing_config=DocumentRoutingPostProcessingConfig(document_post_processing="aggregate_to_main_variant"),
        )
    elif mode == "documents":
        document_routing = ResolvedDocumentRoutingPolicy(
            strategy="through_document_representation",
            source="document_representation",
            profile="q1_authority_family_full_repr",
            profile_config=DocumentRoutingProfileConfig(global_d=d, by_document_type=legacy_by_document_type),
            post_processing="none",
            post_processing_config=DocumentRoutingPostProcessingConfig(),
        )
    elif mode == "documents2":
        document_routing = ResolvedDocumentRoutingPolicy(
            strategy="through_document_representation",
            source="document_representation",
            profile="q1_authority_family_full_repr",
            profile_config=DocumentRoutingProfileConfig(global_d=d, by_document_type=legacy_by_document_type),
            post_processing="none",
            post_processing_config=DocumentRoutingPostProcessingConfig(),
        )
    else:
        document_routing = ResolvedDocumentRoutingPolicy(
            strategy="return_all",
            source="all_documents",
            profile=None,
            profile_config=None,
            post_processing="none",
            post_processing_config=DocumentRoutingPostProcessingConfig(),
        )

    return ResolvedRetrievalPolicy(
        querying=querying,
        document_routing=document_routing,
        chunk_retrieval=chunk_retrieval,
        legacy_document_stage=legacy_document_stage,
        legacy_mode=mode,
    )
