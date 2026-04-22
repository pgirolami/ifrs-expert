"""Typed policy configuration loaded from YAML."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, cast

import yaml

if TYPE_CHECKING:
    from pathlib import Path

from src.models.document import DOCUMENT_TYPES

logger = logging.getLogger(__name__)

DocumentSimilarityRepresentation = Literal["full", "background_and_issue", "scope", "toc"]
SIMILARITY_REPRESENTATIONS: tuple[DocumentSimilarityRepresentation, ...] = ("full", "background_and_issue", "scope", "toc")


@dataclass(frozen=True)
class DocumentTypeRetrievalPolicy:
    """Retrieval settings for one exact document type."""

    d: int
    min_score: float
    expand_to_section: bool
    similarity_representation: DocumentSimilarityRepresentation


@dataclass(frozen=True)
class DocumentStageRetrievalPolicy:
    """Document-stage retrieval settings."""

    global_d: int
    by_document_type: dict[str, DocumentTypeRetrievalPolicy]


@dataclass(frozen=True)
class TextStageRetrievalPolicy:
    """Text-stage retrieval settings."""

    min_score: float


@dataclass(frozen=True)
class TitleStageRetrievalPolicy:
    """Title-stage retrieval settings."""

    min_score: float


@dataclass(frozen=True)
class RetrievalPolicy:
    """Top-level retrieval policy settings."""

    mode: str
    k: int
    expand: int
    full_doc_threshold: int
    expand_to_section: bool
    text: TextStageRetrievalPolicy
    titles: TitleStageRetrievalPolicy
    documents: DocumentStageRetrievalPolicy


@dataclass(frozen=True)
class PromptsPolicy:
    """Reserved prompt policy section for future expansion."""

    answer_prompt_a_path: str | None = None
    answer_prompt_b_path: str | None = None


@dataclass(frozen=True)
class OutputPolicy:
    """Reserved output policy section for future expansion."""

    response_format: str | None = None


@dataclass(frozen=True)
class PolicyConfig:
    """Root policy configuration."""

    retrieval: RetrievalPolicy
    prompts: PromptsPolicy | None
    output: OutputPolicy | None


def load_policy_config(path: Path) -> PolicyConfig:
    """Load and validate a policy configuration from YAML."""
    if not path.exists():
        message = f"Policy config not found: {path}"
        raise FileNotFoundError(message)

    raw_data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if raw_data is None:
        message = f"Policy config is empty: {path}"
        raise ValueError(message)

    root_mapping = _require_mapping(raw_data, context="root")
    retrieval_mapping = _require_mapping(_require_key(root_mapping, "retrieval", context="root"), context="root.retrieval")

    prompts_policy = _parse_prompts_policy(root_mapping.get("prompts"))
    output_policy = _parse_output_policy(root_mapping.get("output"))

    retrieval_policy = _parse_retrieval_policy(retrieval_mapping)
    logger.info(f"Loaded policy config from {path}")
    return PolicyConfig(retrieval=retrieval_policy, prompts=prompts_policy, output=output_policy)


def _parse_retrieval_policy(retrieval_mapping: dict[str, object]) -> RetrievalPolicy:
    mode = _require_retrieval_mode(_require_key(retrieval_mapping, "mode", context="retrieval"))
    k = _require_positive_int(_require_key(retrieval_mapping, "k", context="retrieval"), context="retrieval.k")
    expand = _require_non_negative_int(_require_key(retrieval_mapping, "expand", context="retrieval"), context="retrieval.expand")
    full_doc_threshold = _require_non_negative_int(
        _require_key(retrieval_mapping, "full_doc_threshold", context="retrieval"),
        context="retrieval.full_doc_threshold",
    )
    expand_to_section = _require_bool(
        _require_key(retrieval_mapping, "expand_to_section", context="retrieval"),
        context="retrieval.expand_to_section",
    )

    text_mapping = _require_mapping(_require_key(retrieval_mapping, "text", context="retrieval"), context="retrieval.text")
    text_min_score = _require_score(
        _require_key(text_mapping, "min_score", context="retrieval.text"),
        context="retrieval.text.min_score",
    )

    titles_mapping = _require_mapping(_require_key(retrieval_mapping, "titles", context="retrieval"), context="retrieval.titles")
    title_min_score = _require_score(
        _require_key(titles_mapping, "min_score", context="retrieval.titles"),
        context="retrieval.titles.min_score",
    )

    documents_mapping = _require_mapping(_require_key(retrieval_mapping, "documents", context="retrieval"), context="retrieval.documents")
    global_d = _require_positive_int(_require_key(documents_mapping, "global_d", context="retrieval.documents"), context="retrieval.documents.global_d")

    by_document_type_mapping = _require_mapping(
        _require_key(documents_mapping, "by_document_type", context="retrieval.documents"),
        context="retrieval.documents.by_document_type",
    )
    by_document_type = _parse_document_type_policies(by_document_type_mapping)

    return RetrievalPolicy(
        mode=mode,
        k=k,
        expand=expand,
        full_doc_threshold=full_doc_threshold,
        expand_to_section=expand_to_section,
        text=TextStageRetrievalPolicy(min_score=text_min_score),
        titles=TitleStageRetrievalPolicy(min_score=title_min_score),
        documents=DocumentStageRetrievalPolicy(
            global_d=global_d,
            by_document_type=by_document_type,
        ),
    )


def _parse_document_type_policies(by_document_type_mapping: dict[str, object]) -> dict[str, DocumentTypeRetrievalPolicy]:
    expected_document_types = set(DOCUMENT_TYPES)
    provided_document_types = set(by_document_type_mapping)

    missing_document_types = sorted(expected_document_types - provided_document_types)
    if missing_document_types:
        message = f"Missing retrieval.documents.by_document_type entries for: {', '.join(missing_document_types)}"
        raise ValueError(message)

    unsupported_document_types = sorted(provided_document_types - expected_document_types)
    if unsupported_document_types:
        message = f"Unsupported retrieval.documents.by_document_type entries: {', '.join(unsupported_document_types)}"
        raise ValueError(message)

    parsed: dict[str, DocumentTypeRetrievalPolicy] = {}
    for document_type in DOCUMENT_TYPES:
        entry = _require_mapping(
            _require_key(by_document_type_mapping, document_type, context="retrieval.documents.by_document_type"),
            context=f"retrieval.documents.by_document_type.{document_type}",
        )
        parsed[document_type] = DocumentTypeRetrievalPolicy(
            d=_require_positive_int(
                _require_key(entry, "d", context=f"retrieval.documents.by_document_type.{document_type}"),
                context=f"retrieval.documents.by_document_type.{document_type}.d",
            ),
            min_score=_require_score(
                _require_key(entry, "min_score", context=f"retrieval.documents.by_document_type.{document_type}"),
                context=f"retrieval.documents.by_document_type.{document_type}.min_score",
            ),
            expand_to_section=_require_bool(
                _require_key(entry, "expand_to_section", context=f"retrieval.documents.by_document_type.{document_type}"),
                context=f"retrieval.documents.by_document_type.{document_type}.expand_to_section",
            ),
            similarity_representation=_require_document_similarity_representation(
                _require_key(entry, "similarity_representation", context=f"retrieval.documents.by_document_type.{document_type}"),
                context=f"retrieval.documents.by_document_type.{document_type}.similarity_representation",
            ),
        )
    return parsed


def _parse_prompts_policy(raw_prompts_policy: object) -> PromptsPolicy | None:
    if raw_prompts_policy is None:
        return None
    prompts_mapping = _require_mapping(raw_prompts_policy, context="prompts")
    answer_prompt_a_path = _require_optional_string(prompts_mapping.get("answer_prompt_a_path"), context="prompts.answer_prompt_a_path")
    answer_prompt_b_path = _require_optional_string(prompts_mapping.get("answer_prompt_b_path"), context="prompts.answer_prompt_b_path")
    return PromptsPolicy(answer_prompt_a_path=answer_prompt_a_path, answer_prompt_b_path=answer_prompt_b_path)


def _parse_output_policy(raw_output_policy: object) -> OutputPolicy | None:
    if raw_output_policy is None:
        return None
    output_mapping = _require_mapping(raw_output_policy, context="output")
    response_format = _require_optional_string(output_mapping.get("response_format"), context="output.response_format")
    return OutputPolicy(response_format=response_format)


def _require_key(mapping: dict[str, object], key: str, context: str) -> object:
    if key in mapping:
        return mapping[key]
    message = f"Missing required key: {context}.{key}"
    raise ValueError(message)


def _require_mapping(value: object, context: str) -> dict[str, object]:
    if not isinstance(value, dict):
        message = f"{context} must be a mapping"
        raise TypeError(message)
    for key in value:
        if not isinstance(key, str):
            message = f"{context} contains a non-string key"
            raise TypeError(message)
    return {str(key): item for key, item in value.items()}


def _require_positive_int(value: object, context: str) -> int:
    if isinstance(value, int) and value > 0:
        return value
    message = f"{context} must be an integer > 0"
    raise ValueError(message)


def _require_non_negative_int(value: object, context: str) -> int:
    if isinstance(value, int) and value >= 0:
        return value
    message = f"{context} must be an integer >= 0"
    raise ValueError(message)


def _require_score(value: object, context: str) -> float:
    if isinstance(value, int | float):
        score = float(value)
        if 0.0 <= score <= 1.0:
            return score
    message = f"{context} must be a number between 0.0 and 1.0"
    raise ValueError(message)


def _require_bool(value: object, context: str) -> bool:
    if isinstance(value, bool):
        return value
    message = f"{context} must be a boolean"
    raise ValueError(message)


def _require_optional_string(value: object, context: str) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        stripped_value = value.strip()
        if stripped_value:
            return stripped_value
    message = f"{context} must be a non-empty string when provided"
    raise ValueError(message)


def _require_retrieval_mode(value: object) -> str:
    if isinstance(value, str) and value in {"text", "titles", "documents", "documents2"}:
        return value
    message = "retrieval.mode must be one of: text, titles, documents, documents2"
    raise ValueError(message)


def _require_document_similarity_representation(
    value: object,
    context: str,
) -> DocumentSimilarityRepresentation:
    if isinstance(value, str) and value in SIMILARITY_REPRESENTATIONS:
        return cast("DocumentSimilarityRepresentation", value)
    supported_representations = ", ".join(SIMILARITY_REPRESENTATIONS)
    message = f"{context} must be one of: {supported_representations}"
    raise ValueError(message)
