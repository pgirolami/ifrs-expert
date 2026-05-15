"""Typed retrieval policy catalogs and resolvers."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, NoReturn, cast

import yaml

if TYPE_CHECKING:
    from collections.abc import Mapping
    from pathlib import Path

from src.models.document import DOCUMENT_TYPES

logger = logging.getLogger(__name__)

DocumentSimilarityRepresentation = Literal["full", "background_and_issue", "scope", "toc"]
QueryEmbeddingMode = Literal["raw", "enriched"]
DocumentRoutingSource = Literal["all_documents", "top_chunk_results", "document_representation"]
DocumentRoutingPostProcessing = Literal["aggregate_to_main_variant", "main_variant_only"]
ChunkRetrievalMode = Literal["chunk_similarity", "title_similarity"]
SIMILARITY_REPRESENTATIONS: tuple[DocumentSimilarityRepresentation, ...] = ("full", "background_and_issue", "scope", "toc")
QUERY_EMBEDDING_MODES: tuple[QueryEmbeddingMode, ...] = ("raw", "enriched")
DOCUMENT_ROUTING_SOURCES: tuple[DocumentRoutingSource, ...] = ("all_documents", "top_chunk_results", "document_representation")
DOCUMENT_ROUTING_POST_PROCESSING_VALUES: tuple[DocumentRoutingPostProcessing, ...] = (
    "aggregate_to_main_variant",
    "main_variant_only",
)
CHUNK_RETRIEVAL_MODES: tuple[ChunkRetrievalMode, ...] = ("chunk_similarity", "title_similarity")


@dataclass(frozen=True)
class QueryingConfig:
    """One named querying configuration."""

    embedding_mode: QueryEmbeddingMode


@dataclass(frozen=True)
class DocumentRoutingTypeConfig:
    """Tuning for one exact document type within a routing profile."""

    d: int
    min_score: float
    expand_to_section: bool
    similarity_representation: DocumentSimilarityRepresentation | None = None


@dataclass(frozen=True)
class DocumentRoutingProfileConfig:
    """Document-routing tuning scoped to one routing strategy."""

    global_d: int
    by_document_type: dict[str, DocumentRoutingTypeConfig]


@dataclass(frozen=True)
class DocumentRoutingStrategyConfig:
    """One named document-routing strategy and its compatible profiles."""

    source: DocumentRoutingSource
    profiles: dict[str, DocumentRoutingProfileConfig] | None = None


@dataclass(frozen=True)
class DocumentRoutingPostProcessingConfig:
    """One named routing post-processing option."""

    document_post_processing: DocumentRoutingPostProcessing | None = None
    filter: str | None = None


@dataclass(frozen=True)
class ChunkRetrievalFilterConfig:
    """Chunk-retrieval score and top-k filtering settings."""

    min_score: float
    per_document_k: int


@dataclass(frozen=True)
class ChunkRetrievalExpansionConfig:
    """Chunk-retrieval expansion settings."""

    expand: int
    expand_to_section: bool
    full_doc_threshold: int
    reference_expansion: ReferenceExpansionConfig | None = None


@dataclass(frozen=True)
class ReferenceExpansionConfig:
    """Chunk-retrieval reference expansion settings."""

    enabled: bool
    depth: int
    max_chunks_per_seed: int
    max_chunks_per_doc: int
    section_target_max_chunks: int = 3


@dataclass(frozen=True)
class ChunkRetrievalProfileConfig:
    """Chunk-retrieval tuning scoped to one retrieval strategy."""

    filter: ChunkRetrievalFilterConfig
    expansion: ChunkRetrievalExpansionConfig | None = None


@dataclass(frozen=True)
class ChunkRetrievalStrategyConfig:
    """One named chunk-retrieval strategy and its compatible profiles."""

    mode: ChunkRetrievalMode
    profiles: dict[str, ChunkRetrievalProfileConfig]


@dataclass(frozen=True)
class DocumentRoutingReferenceConfig:
    """Reference to one routing strategy/profile/post-processing choice."""

    strategy: str
    profile: str | None
    post_processing: str


@dataclass(frozen=True)
class ChunkRetrievalReferenceConfig:
    """Reference to one chunk-retrieval strategy/profile choice."""

    strategy: str
    profile: str


@dataclass(frozen=True)
class RetrievalPolicyReferenceConfig:
    """One assembled retrieval policy reference in the catalog."""

    querying: str
    document_routing: DocumentRoutingReferenceConfig
    chunk_retrieval: ChunkRetrievalReferenceConfig


@dataclass(frozen=True)
class PromptsPolicy:
    """Reserved prompt policy section for future expansion."""

    answer_approach_identification_path: str | None = None
    answer_applicability_analysis_path: str | None = None


@dataclass(frozen=True)
class OutputPolicy:
    """Reserved output policy section for future expansion."""

    response_format: str | None = None


@dataclass(frozen=True)
class PolicyCatalog:
    """Root retrieval policy catalog loaded from YAML."""

    querying: dict[str, QueryingConfig]
    document_routing_strategies: dict[str, DocumentRoutingStrategyConfig]
    document_routing_post_processing: dict[str, DocumentRoutingPostProcessingConfig]
    chunk_retrieval_strategies: dict[str, ChunkRetrievalStrategyConfig]
    retrieval_policies: dict[str, RetrievalPolicyReferenceConfig]
    prompts: PromptsPolicy | None
    output: OutputPolicy | None


@dataclass(frozen=True)
class ResolvedQueryingPolicy:
    """Resolved querying settings used at runtime."""

    embedding_mode: QueryEmbeddingMode


@dataclass(frozen=True)
class ResolvedDocumentRoutingPolicy:
    """Resolved document-routing settings used at runtime."""

    strategy: str
    source: DocumentRoutingSource
    profile: str | None
    profile_config: DocumentRoutingProfileConfig | None
    post_processing: str
    post_processing_config: DocumentRoutingPostProcessingConfig


@dataclass(frozen=True)
class ResolvedChunkRetrievalPolicy:
    """Resolved chunk-retrieval settings used at runtime."""

    strategy: str
    mode: ChunkRetrievalMode
    profile: str
    profile_config: ChunkRetrievalProfileConfig


@dataclass(frozen=True)
class ResolvedRetrievalPolicy:
    """Resolved runtime retrieval policy assembled from the catalog."""

    policy_name: str
    querying: ResolvedQueryingPolicy
    document_routing: ResolvedDocumentRoutingPolicy
    chunk_retrieval: ResolvedChunkRetrievalPolicy
    legacy_document_stage: DocumentStageRetrievalPolicy | None = None

    @property
    def query_embedding_mode(self) -> QueryEmbeddingMode:
        """Compatibility accessor for the legacy flat policy shape."""
        return self.querying.embedding_mode

    @property
    def k(self) -> int:
        """Compatibility accessor for the chunk per-document top-k."""
        return self.chunk_retrieval.profile_config.filter.per_document_k

    @property
    def expand(self) -> int:
        """Compatibility accessor for chunk expansion depth."""
        expansion = self.chunk_retrieval.profile_config.expansion
        if expansion is None:
            return 0
        return expansion.expand

    @property
    def full_doc_threshold(self) -> int:
        """Compatibility accessor for chunk full-document threshold."""
        expansion = self.chunk_retrieval.profile_config.expansion
        if expansion is None:
            return 0
        return expansion.full_doc_threshold

    @property
    def reference_expansion(self) -> ReferenceExpansionConfig | None:
        """Compatibility accessor for chunk reference expansion settings."""
        expansion = self.chunk_retrieval.profile_config.expansion
        if expansion is None:
            return None
        return expansion.reference_expansion

    @property
    def expand_to_section(self) -> bool:
        """Compatibility accessor for chunk expansion to section subtree."""
        expansion = self.chunk_retrieval.profile_config.expansion
        if expansion is None:
            return False
        return expansion.expand_to_section

    @property
    def text(self) -> TextStageRetrievalPolicy:
        """Compatibility view of chunk retrieval thresholds."""
        return TextStageRetrievalPolicy(min_score=self.chunk_retrieval.profile_config.filter.min_score)

    @property
    def titles(self) -> TitleStageRetrievalPolicy:
        """Compatibility view of title retrieval thresholds."""
        return TitleStageRetrievalPolicy(min_score=self.chunk_retrieval.profile_config.filter.min_score)

    @property
    def documents(self) -> DocumentStageRetrievalPolicy:
        """Compatibility view of document-routing thresholds."""
        if self.legacy_document_stage is not None:
            return self.legacy_document_stage
        if self.document_routing.profile_config is None:
            message = "Document-stage compatibility data is not available for this policy"
            _raise_value_error(message)
        return DocumentStageRetrievalPolicy(
            global_d=self.document_routing.profile_config.global_d,
            by_document_type=_convert_document_routing_profile_by_document_type(self.document_routing.profile_config.by_document_type),
        )


@dataclass(frozen=True)
class TextStageRetrievalPolicy:
    """Compatibility view for chunk retrieval score thresholds."""

    min_score: float


@dataclass(frozen=True)
class TitleStageRetrievalPolicy:
    """Compatibility view for title retrieval score thresholds."""

    min_score: float


@dataclass(frozen=True)
class DocumentTypeRetrievalPolicy:
    """Compatibility view for one exact document type in the legacy flat shape."""

    d: int
    min_score: float
    expand_to_section: bool
    similarity_representation: str


@dataclass(frozen=True)
class DocumentStageRetrievalPolicy:
    """Compatibility view for document-stage retrieval settings."""

    global_d: int
    by_document_type: dict[str, DocumentTypeRetrievalPolicy]


@dataclass(frozen=True)
class PolicyConfig:
    """Compatibility wrapper for legacy callers that expect a single retrieval policy."""

    retrieval: ResolvedRetrievalPolicy
    prompts: PromptsPolicy | None
    output: OutputPolicy | None
    catalog: PolicyCatalog


# Compatibility alias for callers that still import the legacy flat retrieval policy name.
RetrievalPolicy = ResolvedRetrievalPolicy


def load_policy_catalog(path: Path) -> PolicyCatalog:
    """Load and validate a retrieval policy catalog from YAML."""
    if not path.exists():
        message = f"Policy config not found: {path}"
        raise FileNotFoundError(message)

    raw_data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if raw_data is None:
        message = f"Policy config is empty: {path}"
        _raise_value_error(message)

    root_mapping = _require_mapping(raw_data, context="root")
    querying = _parse_querying_catalog(_require_key(root_mapping, "querying", context="root"))
    document_routing_strategies = _parse_document_routing_strategies(_require_key(root_mapping, "document_routing_strategies", context="root"))
    document_routing_post_processing = _parse_document_routing_post_processing_catalog(_require_key(root_mapping, "document_routing_post_processing", context="root"))
    chunk_retrieval_strategies = _parse_chunk_retrieval_strategies(_require_key(root_mapping, "chunk_retrieval_strategies", context="root"))
    retrieval_policies = _parse_retrieval_policy_references(_require_key(root_mapping, "retrieval_policies", context="root"))
    prompts_policy = _parse_prompts_policy(root_mapping.get("prompts"))
    output_policy = _parse_output_policy(root_mapping.get("output"))

    logger.info(f"Loaded policy catalog from {path}")
    return PolicyCatalog(
        querying=querying,
        document_routing_strategies=document_routing_strategies,
        document_routing_post_processing=document_routing_post_processing,
        chunk_retrieval_strategies=chunk_retrieval_strategies,
        retrieval_policies=retrieval_policies,
        prompts=prompts_policy,
        output=output_policy,
    )


def load_policy_config(path: Path, policy_name: str) -> PolicyConfig:
    """Load a policy catalog and resolve the explicitly named retrieval policy."""
    catalog = load_policy_catalog(path)
    retrieval = resolve_retrieval_policy(catalog, policy_name)
    return PolicyConfig(retrieval=retrieval, prompts=catalog.prompts, output=catalog.output, catalog=catalog)


def resolve_retrieval_policy(catalog: PolicyCatalog, policy_name: str) -> ResolvedRetrievalPolicy:
    """Resolve one named assembled retrieval policy into runtime settings."""
    reference = catalog.retrieval_policies.get(policy_name)
    if reference is None:
        _raise_value_error(f"Unknown retrieval policy: {policy_name}")

    querying = _resolve_querying(catalog=catalog, querying_name=reference.querying)
    document_routing = _resolve_document_routing(catalog=catalog, reference=reference.document_routing)
    chunk_retrieval = _resolve_chunk_retrieval(catalog=catalog, reference=reference.chunk_retrieval)
    legacy_document_stage = _build_legacy_document_stage(catalog=catalog, document_routing=document_routing, chunk_retrieval=chunk_retrieval)
    resolved = ResolvedRetrievalPolicy(
        policy_name=policy_name,
        querying=querying,
        document_routing=document_routing,
        chunk_retrieval=chunk_retrieval,
        legacy_document_stage=legacy_document_stage,
    )
    logger.info(f"Resolved retrieval policy: {policy_name} -> source={resolved.document_routing.source}, chunk_mode={resolved.chunk_retrieval.mode}")
    return resolved


def _resolve_querying(catalog: PolicyCatalog, querying_name: str) -> ResolvedQueryingPolicy:
    querying = catalog.querying.get(querying_name)
    if querying is None:
        _raise_value_error(f"Unknown querying reference: {querying_name}")
    return ResolvedQueryingPolicy(embedding_mode=querying.embedding_mode)


def _resolve_document_routing(catalog: PolicyCatalog, reference: DocumentRoutingReferenceConfig) -> ResolvedDocumentRoutingPolicy:
    strategy = catalog.document_routing_strategies.get(reference.strategy)
    if strategy is None:
        _raise_value_error(f"Unknown document routing strategy: {reference.strategy}")
    post_processing_config = catalog.document_routing_post_processing.get(reference.post_processing)
    if post_processing_config is None:
        _raise_value_error(f"Unknown document routing post-processing: {reference.post_processing}")

    if strategy.source == "all_documents":
        if reference.profile is not None:
            _raise_value_error(f"Document routing profile is not allowed for strategy {reference.strategy}")
        if strategy.profiles:
            _raise_value_error(f"Document routing strategy {reference.strategy} must not define profiles")
        if post_processing_config.document_post_processing is not None or post_processing_config.filter is not None:
            _raise_value_error(f"Document routing post-processing {reference.post_processing} is not compatible with strategy {reference.strategy}")
        return ResolvedDocumentRoutingPolicy(
            strategy=reference.strategy,
            source=strategy.source,
            profile=None,
            profile_config=None,
            post_processing=reference.post_processing,
            post_processing_config=post_processing_config,
        )

    if strategy.profiles is None or not strategy.profiles:
        _raise_value_error(f"Document routing strategy {reference.strategy} requires profiles")
    if reference.profile is None:
        _raise_value_error(f"Document routing profile is required for strategy {reference.strategy}")
    profile_config = strategy.profiles.get(reference.profile)
    if profile_config is None:
        _raise_value_error(f"Unknown document routing profile: {reference.profile} for strategy {reference.strategy}")

    _validate_document_routing_profile(strategy_name=reference.strategy, profile_name=reference.profile, profile_config=profile_config)
    return ResolvedDocumentRoutingPolicy(
        strategy=reference.strategy,
        source=strategy.source,
        profile=reference.profile,
        profile_config=profile_config,
        post_processing=reference.post_processing,
        post_processing_config=post_processing_config,
    )


def _resolve_chunk_retrieval(catalog: PolicyCatalog, reference: ChunkRetrievalReferenceConfig) -> ResolvedChunkRetrievalPolicy:
    strategy = catalog.chunk_retrieval_strategies.get(reference.strategy)
    if strategy is None:
        _raise_value_error(f"Unknown chunk retrieval strategy: {reference.strategy}")
    profile_config = strategy.profiles.get(reference.profile)
    if profile_config is None:
        _raise_value_error(f"Unknown chunk retrieval profile: {reference.profile} for strategy {reference.strategy}")
    _validate_chunk_retrieval_profile(strategy_name=reference.strategy, mode=strategy.mode, profile_name=reference.profile, profile_config=profile_config)
    return ResolvedChunkRetrievalPolicy(strategy=reference.strategy, mode=strategy.mode, profile=reference.profile, profile_config=profile_config)


def _build_legacy_document_stage(
    catalog: PolicyCatalog,
    document_routing: ResolvedDocumentRoutingPolicy,
    chunk_retrieval: ResolvedChunkRetrievalPolicy,
) -> DocumentStageRetrievalPolicy | None:
    del chunk_retrieval
    if document_routing.profile_config is not None:
        return DocumentStageRetrievalPolicy(
            global_d=document_routing.profile_config.global_d,
            by_document_type=_convert_document_routing_profile_by_document_type(document_routing.profile_config.by_document_type),
        )

    fallback_profile = _first_document_routing_profile(catalog)
    if fallback_profile is None:
        return None
    return DocumentStageRetrievalPolicy(
        global_d=fallback_profile.global_d,
        by_document_type=_convert_document_routing_profile_by_document_type(fallback_profile.by_document_type),
    )


def _convert_document_routing_profile_by_document_type(
    by_document_type: dict[str, DocumentRoutingTypeConfig],
) -> dict[str, DocumentTypeRetrievalPolicy]:
    converted: dict[str, DocumentTypeRetrievalPolicy] = {}
    for document_type, document_type_config in by_document_type.items():
        similarity_representation = document_type_config.similarity_representation or "full"
        converted[document_type] = DocumentTypeRetrievalPolicy(
            d=document_type_config.d,
            min_score=document_type_config.min_score,
            expand_to_section=document_type_config.expand_to_section,
            similarity_representation=similarity_representation,
        )
    return converted


def _first_document_routing_profile(catalog: PolicyCatalog) -> DocumentRoutingProfileConfig | None:
    for strategy_name in ("through_chunks", "through_document_representation"):
        strategy = catalog.document_routing_strategies.get(strategy_name)
        if strategy is None or strategy.profiles is None:
            continue
        for profile in strategy.profiles.values():
            return profile
    for strategy in catalog.document_routing_strategies.values():
        if strategy.profiles is None:
            continue
        for profile in strategy.profiles.values():
            return profile
    return None


def _validate_document_routing_profile(
    *,
    strategy_name: str,
    profile_name: str,
    profile_config: DocumentRoutingProfileConfig,
) -> None:
    expected_document_types = set(DOCUMENT_TYPES)
    provided_document_types = set(profile_config.by_document_type)
    missing_document_types = sorted(expected_document_types - provided_document_types)
    unsupported_document_types = sorted(provided_document_types - expected_document_types)
    if missing_document_types:
        _raise_value_error(f"Missing document routing entries for strategy {strategy_name} profile {profile_name}: {', '.join(missing_document_types)}")
    if unsupported_document_types:
        _raise_value_error(f"Unsupported document routing entries for strategy {strategy_name} profile {profile_name}: {', '.join(unsupported_document_types)}")

    for document_type, document_type_config in profile_config.by_document_type.items():
        if document_type_config.d <= 0:
            _raise_value_error(f"document routing d for {strategy_name}.{profile_name}.{document_type} must be > 0")
        _require_score(document_type_config.min_score, context=f"document routing min_score for {strategy_name}.{profile_name}.{document_type}")
        if strategy_name == "through_chunks" and document_type_config.similarity_representation is not None:
            _raise_value_error(f"similarity_representation is not allowed for document routing strategy {strategy_name} profile {profile_name}")
        if strategy_name == "through_document_representation" and document_type_config.similarity_representation is None:
            _raise_value_error(f"similarity_representation is required for document routing strategy {strategy_name} profile {profile_name}")

    if profile_config.global_d <= 0:
        _raise_value_error(f"document routing global_d for {strategy_name}.{profile_name} must be > 0")


def _validate_chunk_retrieval_profile(
    *,
    strategy_name: str,
    mode: ChunkRetrievalMode,
    profile_name: str,
    profile_config: ChunkRetrievalProfileConfig,
) -> None:
    if profile_config.filter.per_document_k <= 0:
        _raise_value_error(f"chunk retrieval per_document_k for {strategy_name}.{profile_name} must be > 0")
    _require_score(profile_config.filter.min_score, context=f"chunk retrieval min_score for {strategy_name}.{profile_name}")
    if mode == "title_similarity":
        if profile_config.expansion is not None:
            _raise_value_error(f"chunk retrieval expansion is not allowed for title similarity strategy {strategy_name}")
        return
    if profile_config.expansion is None:
        _raise_value_error(f"chunk retrieval expansion is required for strategy {strategy_name}")
    if profile_config.expansion.expand < 0:
        _raise_value_error(f"chunk retrieval expand for {strategy_name}.{profile_name} must be >= 0")
    if profile_config.expansion.full_doc_threshold < 0:
        _raise_value_error(f"chunk retrieval full_doc_threshold for {strategy_name}.{profile_name} must be >= 0")
    _validate_reference_expansion_profile(
        strategy_name=strategy_name,
        profile_name=profile_name,
        reference_expansion=profile_config.expansion.reference_expansion,
    )


def _validate_reference_expansion_profile(
    *,
    strategy_name: str,
    profile_name: str,
    reference_expansion: ReferenceExpansionConfig | None,
) -> None:
    if reference_expansion is None:
        return
    if reference_expansion.depth < 0:
        _raise_value_error(f"chunk retrieval reference_expansion.depth for {strategy_name}.{profile_name} must be >= 0")
    if reference_expansion.max_chunks_per_seed < 0:
        _raise_value_error(f"chunk retrieval reference_expansion.max_chunks_per_seed for {strategy_name}.{profile_name} must be >= 0")
    if reference_expansion.max_chunks_per_doc < 0:
        _raise_value_error(f"chunk retrieval reference_expansion.max_chunks_per_doc for {strategy_name}.{profile_name} must be >= 0")
    if reference_expansion.section_target_max_chunks < 0:
        _raise_value_error(f"chunk retrieval reference_expansion.section_target_max_chunks for {strategy_name}.{profile_name} must be >= 0")


def _parse_querying_catalog(raw_querying: object) -> dict[str, QueryingConfig]:
    querying_mapping = _require_mapping(raw_querying, context="querying")
    parsed: dict[str, QueryingConfig] = {}
    for name, value in querying_mapping.items():
        config_mapping = _require_mapping(value, context=f"querying.{name}")
        parsed[name] = QueryingConfig(embedding_mode=_require_query_embedding_mode(_require_key(config_mapping, "embedding_mode", context=f"querying.{name}")))
    return parsed


def _parse_document_routing_post_processing_catalog(raw_catalog: object) -> dict[str, DocumentRoutingPostProcessingConfig]:
    catalog_mapping = _require_mapping(raw_catalog, context="document_routing_post_processing")
    parsed: dict[str, DocumentRoutingPostProcessingConfig] = {}
    for name, value in catalog_mapping.items():
        entry_mapping = _require_mapping(value, context=f"document_routing_post_processing.{name}")
        document_post_processing = _require_optional_post_processing(
            entry_mapping.get("document_post_processing"),
            context=f"document_routing_post_processing.{name}.document_post_processing",
        )
        filter_value = _require_optional_string(entry_mapping.get("filter"), context=f"document_routing_post_processing.{name}.filter")
        if document_post_processing is None and filter_value is None:
            parsed[name] = DocumentRoutingPostProcessingConfig()
        else:
            parsed[name] = DocumentRoutingPostProcessingConfig(document_post_processing=document_post_processing, filter=filter_value)
    return parsed


def _parse_document_routing_strategies(raw_strategies: object) -> dict[str, DocumentRoutingStrategyConfig]:
    strategy_mapping = _require_mapping(raw_strategies, context="document_routing_strategies")
    parsed: dict[str, DocumentRoutingStrategyConfig] = {}
    for strategy_name, value in strategy_mapping.items():
        strategy_config = _require_mapping(value, context=f"document_routing_strategies.{strategy_name}")
        source = _require_document_routing_source(_require_key(strategy_config, "source", context=f"document_routing_strategies.{strategy_name}"))
        raw_profiles = strategy_config.get("profiles")
        profiles = None if raw_profiles is None else _parse_document_routing_profiles(raw_profiles, strategy_name=strategy_name)
        if source == "all_documents" and profiles:
            _raise_value_error(f"Document routing strategy {strategy_name} must not define profiles")
        if source != "all_documents" and (profiles is None or not profiles):
            _raise_value_error(f"Document routing strategy {strategy_name} requires profiles")
        parsed[strategy_name] = DocumentRoutingStrategyConfig(source=source, profiles=profiles)
    return parsed


def _parse_document_routing_profiles(raw_profiles: object, *, strategy_name: str) -> dict[str, DocumentRoutingProfileConfig]:
    profile_mapping = _require_mapping(raw_profiles, context=f"document_routing_strategies.{strategy_name}.profiles")
    parsed: dict[str, DocumentRoutingProfileConfig] = {}
    for profile_name, value in profile_mapping.items():
        profile_config = _require_mapping(value, context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}")
        global_d = _require_positive_int(
            _require_key(profile_config, "global_d", context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}"),
            context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}.global_d",
        )
        by_document_type = _parse_document_routing_profile_by_document_type(
            _require_key(profile_config, "by_document_type", context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}"),
            strategy_name=strategy_name,
            profile_name=profile_name,
        )
        parsed[profile_name] = DocumentRoutingProfileConfig(global_d=global_d, by_document_type=by_document_type)
    return parsed


def _parse_document_routing_profile_by_document_type(
    raw_by_document_type: object,
    *,
    strategy_name: str,
    profile_name: str,
) -> dict[str, DocumentRoutingTypeConfig]:
    mapping = _require_mapping(raw_by_document_type, context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}.by_document_type")
    expected_document_types = set(DOCUMENT_TYPES)
    provided_document_types = set(mapping)
    missing_document_types = sorted(expected_document_types - provided_document_types)
    unsupported_document_types = sorted(provided_document_types - expected_document_types)
    if missing_document_types:
        _raise_value_error(f"Missing document routing by_document_type entries for strategy {strategy_name} profile {profile_name}: {', '.join(missing_document_types)}")
    if unsupported_document_types:
        _raise_value_error(f"Unsupported document routing by_document_type entries for strategy {strategy_name} profile {profile_name}: {', '.join(unsupported_document_types)}")

    parsed: dict[str, DocumentRoutingTypeConfig] = {}
    for document_type in DOCUMENT_TYPES:
        entry = _require_mapping(
            _require_key(mapping, document_type, context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}.by_document_type"),
            context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}.by_document_type.{document_type}",
        )
        similarity_representation = _require_optional_similarity_representation(
            entry.get("similarity_representation"),
            context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}.by_document_type.{document_type}.similarity_representation",
        )
        parsed[document_type] = DocumentRoutingTypeConfig(
            d=_require_positive_int(
                _require_key(entry, "d", context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}.by_document_type.{document_type}"),
                context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}.by_document_type.{document_type}.d",
            ),
            min_score=_require_score(
                _require_key(entry, "min_score", context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}.by_document_type.{document_type}"),
                context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}.by_document_type.{document_type}.min_score",
            ),
            expand_to_section=_require_bool(
                _require_key(entry, "expand_to_section", context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}.by_document_type.{document_type}"),
                context=f"document_routing_strategies.{strategy_name}.profiles.{profile_name}.by_document_type.{document_type}.expand_to_section",
            ),
            similarity_representation=similarity_representation,
        )
    return parsed


def _parse_chunk_retrieval_strategies(raw_strategies: object) -> dict[str, ChunkRetrievalStrategyConfig]:
    strategy_mapping = _require_mapping(raw_strategies, context="chunk_retrieval_strategies")
    parsed: dict[str, ChunkRetrievalStrategyConfig] = {}
    for strategy_name, value in strategy_mapping.items():
        strategy_config = _require_mapping(value, context=f"chunk_retrieval_strategies.{strategy_name}")
        mode = _require_chunk_retrieval_mode(_require_key(strategy_config, "mode", context=f"chunk_retrieval_strategies.{strategy_name}"))
        profiles = _parse_chunk_retrieval_profiles(_require_key(strategy_config, "profiles", context=f"chunk_retrieval_strategies.{strategy_name}"), strategy_name=strategy_name)
        parsed[strategy_name] = ChunkRetrievalStrategyConfig(mode=mode, profiles=profiles)
    return parsed


def _parse_chunk_retrieval_profiles(raw_profiles: object, *, strategy_name: str) -> dict[str, ChunkRetrievalProfileConfig]:
    profile_mapping = _require_mapping(raw_profiles, context=f"chunk_retrieval_strategies.{strategy_name}.profiles")
    parsed: dict[str, ChunkRetrievalProfileConfig] = {}
    for profile_name, value in profile_mapping.items():
        profile_config = _require_mapping(value, context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}")
        filter_config = _require_mapping(
            _require_key(profile_config, "filter", context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}"),
            context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.filter",
        )
        parsed_filter = ChunkRetrievalFilterConfig(
            min_score=_require_score(
                _require_key(filter_config, "min_score", context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.filter"),
                context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.filter.min_score",
            ),
            per_document_k=_require_positive_int(
                _require_key(filter_config, "per_document_k", context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.filter"),
                context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.filter.per_document_k",
            ),
        )
        raw_expansion = profile_config.get("expansion")
        if raw_expansion is None:
            parsed_expansion = None
        else:
            expansion_mapping = _require_mapping(raw_expansion, context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion")
            raw_reference_expansion = expansion_mapping.get("reference_expansion")
            if raw_reference_expansion is None:
                parsed_reference_expansion = None
            else:
                reference_mapping = _require_mapping(raw_reference_expansion, context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.reference_expansion")
                parsed_reference_expansion = ReferenceExpansionConfig(
                    enabled=_require_bool(
                        _require_key(reference_mapping, "enabled", context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.reference_expansion"),
                        context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.reference_expansion.enabled",
                    ),
                    depth=_require_non_negative_int(
                        _require_key(reference_mapping, "depth", context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.reference_expansion"),
                        context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.reference_expansion.depth",
                    ),
                    max_chunks_per_seed=_require_non_negative_int(
                        _require_key(reference_mapping, "max_chunks_per_seed", context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.reference_expansion"),
                        context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.reference_expansion.max_chunks_per_seed",
                    ),
                    max_chunks_per_doc=_require_non_negative_int(
                        _require_key(reference_mapping, "max_chunks_per_doc", context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.reference_expansion"),
                        context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.reference_expansion.max_chunks_per_doc",
                    ),
                    section_target_max_chunks=_require_non_negative_int(
                        reference_mapping.get("section_target_max_chunks", 3),
                        context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.reference_expansion.section_target_max_chunks",
                    ),
                )
            parsed_expansion = ChunkRetrievalExpansionConfig(
                expand=_require_non_negative_int(
                    _require_key(expansion_mapping, "expand", context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion"),
                    context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.expand",
                ),
                expand_to_section=_require_bool(
                    _require_key(expansion_mapping, "expand_to_section", context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion"),
                    context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.expand_to_section",
                ),
                full_doc_threshold=_require_non_negative_int(
                    _require_key(expansion_mapping, "full_doc_threshold", context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion"),
                    context=f"chunk_retrieval_strategies.{strategy_name}.profiles.{profile_name}.expansion.full_doc_threshold",
                ),
                reference_expansion=parsed_reference_expansion,
            )
        parsed[profile_name] = ChunkRetrievalProfileConfig(filter=parsed_filter, expansion=parsed_expansion)
    return parsed


def _parse_retrieval_policy_references(raw_retrieval_policies: object) -> dict[str, RetrievalPolicyReferenceConfig]:
    policy_mapping = _require_mapping(raw_retrieval_policies, context="retrieval_policies")
    parsed: dict[str, RetrievalPolicyReferenceConfig] = {}
    for policy_name, value in policy_mapping.items():
        policy_config = _require_mapping(value, context=f"retrieval_policies.{policy_name}")
        querying = _require_optional_string(_require_key(policy_config, "querying", context=f"retrieval_policies.{policy_name}"), context=f"retrieval_policies.{policy_name}.querying")
        if querying is None:
            _raise_value_error(f"retrieval_policies.{policy_name}.querying must be a non-empty string")
        document_routing_mapping = _require_mapping(
            _require_key(policy_config, "document_routing", context=f"retrieval_policies.{policy_name}"),
            context=f"retrieval_policies.{policy_name}.document_routing",
        )
        chunk_retrieval_mapping = _require_mapping(
            _require_key(policy_config, "chunk_retrieval", context=f"retrieval_policies.{policy_name}"),
            context=f"retrieval_policies.{policy_name}.chunk_retrieval",
        )
        parsed[policy_name] = RetrievalPolicyReferenceConfig(
            querying=querying,
            document_routing=DocumentRoutingReferenceConfig(
                strategy=_require_optional_string(
                    _require_key(document_routing_mapping, "strategy", context=f"retrieval_policies.{policy_name}.document_routing"),
                    context=f"retrieval_policies.{policy_name}.document_routing.strategy",
                )
                or "",
                profile=_require_optional_string(document_routing_mapping.get("profile"), context=f"retrieval_policies.{policy_name}.document_routing.profile"),
                post_processing=_require_optional_string(
                    _require_key(document_routing_mapping, "post_processing", context=f"retrieval_policies.{policy_name}.document_routing"),
                    context=f"retrieval_policies.{policy_name}.document_routing.post_processing",
                )
                or "",
            ),
            chunk_retrieval=ChunkRetrievalReferenceConfig(
                strategy=_require_optional_string(
                    _require_key(chunk_retrieval_mapping, "strategy", context=f"retrieval_policies.{policy_name}.chunk_retrieval"),
                    context=f"retrieval_policies.{policy_name}.chunk_retrieval.strategy",
                )
                or "",
                profile=_require_optional_string(
                    _require_key(chunk_retrieval_mapping, "profile", context=f"retrieval_policies.{policy_name}.chunk_retrieval"),
                    context=f"retrieval_policies.{policy_name}.chunk_retrieval.profile",
                )
                or "",
            ),
        )
    return parsed


def _parse_prompts_policy(raw_prompts_policy: object) -> PromptsPolicy | None:
    if raw_prompts_policy is None:
        return None
    prompts_mapping = _require_mapping(raw_prompts_policy, context="prompts")
    answer_approach_identification_path = _require_optional_string(prompts_mapping.get("answer_approach_identification_path"), context="prompts.answer_approach_identification_path")
    answer_applicability_analysis_path = _require_optional_string(prompts_mapping.get("answer_applicability_analysis_path"), context="prompts.answer_applicability_analysis_path")
    return PromptsPolicy(answer_approach_identification_path=answer_approach_identification_path, answer_applicability_analysis_path=answer_applicability_analysis_path)


def _parse_output_policy(raw_output_policy: object) -> OutputPolicy | None:
    if raw_output_policy is None:
        return None
    output_mapping = _require_mapping(raw_output_policy, context="output")
    response_format = _require_optional_string(output_mapping.get("response_format"), context="output.response_format")
    return OutputPolicy(response_format=response_format)


def _require_key(mapping: Mapping[str, object], key: str, context: str) -> object:
    if key in mapping:
        return mapping[key]
    _raise_value_error(f"Missing required key: {context}.{key}")
    return None


def _require_mapping(value: object, context: str) -> dict[str, object]:
    if not isinstance(value, dict):
        _raise_type_error(f"{context} must be a mapping")
    for key in value:
        if not isinstance(key, str):
            _raise_type_error(f"{context} contains a non-string key")
            return {}
    return {str(key): item for key, item in value.items()}


def _require_positive_int(value: object, context: str) -> int:
    if isinstance(value, int) and value > 0:
        return value
    _raise_value_error(f"{context} must be an integer > 0")
    return 0


def _require_non_negative_int(value: object, context: str) -> int:
    if isinstance(value, int) and value >= 0:
        return value
    _raise_value_error(f"{context} must be an integer >= 0")
    return 0


def _require_score(value: object, context: str) -> float:
    if isinstance(value, int | float):
        score = float(value)
        if 0.0 <= score <= 1.0:
            return score
    _raise_value_error(f"{context} must be a number between 0.0 and 1.0")
    return 0.0


def _require_bool(value: object, context: str) -> bool:
    if isinstance(value, bool):
        return value
    _raise_value_error(f"{context} must be a boolean")
    return False


def _require_optional_string(value: object, context: str) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        stripped_value = value.strip()
        if stripped_value:
            return stripped_value
    _raise_value_error(f"{context} must be a non-empty string when provided")
    return None


def _require_query_embedding_mode(value: object) -> QueryEmbeddingMode:
    if isinstance(value, str) and value in QUERY_EMBEDDING_MODES:
        return cast("QueryEmbeddingMode", value)
    _raise_value_error("embedding_mode must be one of: raw, enriched")
    return cast("QueryEmbeddingMode", "raw")


def _require_document_routing_source(value: object) -> DocumentRoutingSource:
    if isinstance(value, str) and value in DOCUMENT_ROUTING_SOURCES:
        return cast("DocumentRoutingSource", value)
    supported = ", ".join(DOCUMENT_ROUTING_SOURCES)
    _raise_value_error(f"source must be one of: {supported}")
    return cast("DocumentRoutingSource", "all_documents")


def _require_post_processing_name(value: object) -> DocumentRoutingPostProcessing:
    if isinstance(value, str) and value in DOCUMENT_ROUTING_POST_PROCESSING_VALUES:
        return cast("DocumentRoutingPostProcessing", value)
    supported = ", ".join(DOCUMENT_ROUTING_POST_PROCESSING_VALUES)
    _raise_value_error(f"post_processing must be one of: {supported}")
    return cast("DocumentRoutingPostProcessing", "aggregate_to_main_variant")


def _require_chunk_retrieval_mode(value: object) -> ChunkRetrievalMode:
    if isinstance(value, str) and value in CHUNK_RETRIEVAL_MODES:
        return cast("ChunkRetrievalMode", value)
    supported = ", ".join(CHUNK_RETRIEVAL_MODES)
    _raise_value_error(f"mode must be one of: {supported}")
    return cast("ChunkRetrievalMode", "chunk_similarity")


def _require_optional_similarity_representation(
    value: object,
    context: str,
) -> DocumentSimilarityRepresentation | None:
    if value is None:
        return None
    if isinstance(value, str) and value in SIMILARITY_REPRESENTATIONS:
        return cast("DocumentSimilarityRepresentation", value)
    supported_representations = ", ".join(SIMILARITY_REPRESENTATIONS)
    _raise_value_error(f"{context} must be one of: {supported_representations}")
    return None


def _require_optional_post_processing(
    value: object,
    context: str,
) -> DocumentRoutingPostProcessing | None:
    if value is None:
        return None
    if isinstance(value, str) and value in DOCUMENT_ROUTING_POST_PROCESSING_VALUES:
        return cast("DocumentRoutingPostProcessing", value)
    supported = ", ".join(DOCUMENT_ROUTING_POST_PROCESSING_VALUES)
    _raise_value_error(f"{context} must be one of: {supported}")
    return None


# Backwards-compatible helpers for the small amount of legacy code that still expects
# the original flat policy shape.
def _build_legacy_retrieval_policy(policy: ResolvedRetrievalPolicy) -> ResolvedRetrievalPolicy:
    return policy


def _raise_value_error(message: str) -> NoReturn:
    raise ValueError(message)


def _raise_type_error(message: str) -> NoReturn:
    raise TypeError(message)
