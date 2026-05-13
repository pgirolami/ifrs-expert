"""Workflow stages for IFRS case analysis."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol, cast

from src.case_analysis.models import ApplicabilityAnalysisResult, AuthorityClassificationResult, RetrievedSourcePackage, ValidatedQuestion, ValidationFailure
from src.retrieval.pipeline import execute_retrieval
from src.retrieval.request_builder import build_retrieval_request

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.policy import RetrievalPolicy
    from src.retrieval.models import RetrievalRequest, RetrievalResult
    from src.retrieval.pipeline import RetrievalPipelineConfig

logger = logging.getLogger(__name__)


class ExecuteRetrievalFn(Protocol):
    """Callable contract for running the retrieval pipeline."""

    def __call__(self, *, request: RetrievalRequest, config: RetrievalPipelineConfig) -> tuple[str | None, RetrievalResult | None]:
        """Execute retrieval for a built request and pipeline config."""


class ValidateQuestionStage:
    """Validate the question and retrieval policy before workflow execution."""

    def execute(self, query: str, policy: RetrievalPolicy) -> ValidatedQuestion | ValidationFailure:
        """Return trimmed question text or a structured validation failure."""
        stripped_query = query.strip()
        if not stripped_query:
            return ValidationFailure(
                error_stage="validation",
                reason="empty_question",
                message="Error: Query cannot be empty",
            )

        policy_error = self._validate_policy(policy)
        if policy_error is not None:
            return policy_error

        return ValidatedQuestion(question=stripped_query)

    def _validate_policy(self, policy: RetrievalPolicy) -> ValidationFailure | None:
        """Validate policy values used by the answer workflow."""
        policy_checks = (
            (policy.expand < 0, "negative_expand", "Error: expand must be >= 0"),
            (policy.full_doc_threshold < 0, "negative_full_doc_threshold", "Error: full_doc_threshold must be >= 0"),
            (policy.k <= 0, "non_positive_k", "Error: retrieval.k in policy must be > 0"),
            (policy.documents.global_d <= 0, "non_positive_global_d", "Error: retrieval.documents.global_d in policy must be > 0"),
            (
                policy.document_routing.source not in {"all_documents", "top_chunk_results", "document_representation"},
                "unsupported_document_routing_source",
                "Error: document_routing.source in policy must be 'all_documents', 'top_chunk_results', or 'document_representation'",
            ),
            (
                policy.chunk_retrieval.mode not in {"chunk_similarity", "title_similarity"},
                "unsupported_chunk_retrieval_mode",
                "Error: chunk_retrieval.mode in policy must be 'chunk_similarity' or 'title_similarity'",
            ),
        )
        for failed, reason, message in policy_checks:
            if failed:
                return self._policy_failure(reason=reason, message=message)

        for document_type, cap in policy.documents.by_document_type.items():
            if cap.d <= 0:
                return self._policy_failure(reason="non_positive_document_cap", message=f"Error: per-type document cap for {document_type} must be > 0")

        return None

    def _policy_failure(self, reason: str, message: str) -> ValidationFailure:
        """Build a policy validation failure."""
        return ValidationFailure(error_stage="validation", reason=reason, message=message)


@dataclass(frozen=True)
class RetrieveSourceMaterialStage:
    """Run source retrieval without classifying authority."""

    pipeline_config: RetrievalPipelineConfig
    execute_retrieval_fn: ExecuteRetrievalFn = execute_retrieval

    def execute(self, question: str, policy: RetrievalPolicy) -> RetrievedSourcePackage | ValidationFailure:
        """Return retrieved source material or a structured retrieval failure."""
        logger.info(f"Retrieving source material for question='{question[:80]}' policy={policy.policy_name}")
        request = build_retrieval_request(
            query=question,
            policy=policy,
            chunk_min_score=policy.titles.min_score if policy.chunk_retrieval.mode == "title_similarity" else policy.text.min_score,
            expand_to_section=policy.expand_to_section if policy.document_routing.source == "all_documents" else True,
        )
        error, retrieval_result = self.execute_retrieval_fn(request=request, config=self.pipeline_config)
        if error is not None:
            logger.warning(f"Source retrieval failed: {error}")
            return ValidationFailure(error_stage="retrieval", reason="retrieval_error", message=error)
        if retrieval_result is None:
            message = "Error: Retrieval did not return a result"
            logger.error(message)
            return ValidationFailure(error_stage="retrieval", reason="missing_retrieval_result", message=message)

        source_package = RetrievedSourcePackage.from_retrieval_result(retrieval_result)
        logger.info(f"Retrieved source material docs={len(source_package.retrieved_doc_uids)} chunks={len(source_package.chunk_results)} policy={source_package.policy_name}")
        return source_package


@dataclass(frozen=True)
class JsonPromptStage:
    """Base stage for LLM prompts that must return JSON objects."""

    send_to_llm_fn: Callable[[str], str]
    error_stage: str
    result_name: str

    def execute(self, prompt_text: str) -> AuthorityClassificationResult | ApplicabilityAnalysisResult | ValidationFailure:
        """Call the LLM and validate that the response is a JSON object."""
        try:
            raw_response = self.send_to_llm_fn(prompt_text)
        except RuntimeError as e:
            logger.exception(f"{self.result_name} LLM call failed")
            return ValidationFailure(error_stage=self.error_stage, reason="llm_call_failed", message=f"Error: LLM call failed: {e}")

        try:
            parsed = json.loads(raw_response)
        except json.JSONDecodeError as e:
            logger.exception(f"Could not parse JSON response from {self.result_name}")
            return ValidationFailure(
                error_stage=f"{self.error_stage}_parse",
                reason="invalid_json",
                message=f"Error: LLM returned invalid JSON: {e}\n\nResponse was:\n{raw_response}",
            )

        if not isinstance(parsed, dict):
            logger.warning(f"{self.result_name} response parsed as JSON but was not an object")
            return ValidationFailure(
                error_stage=f"{self.error_stage}_parse",
                reason="invalid_contract",
                message=f"Error: LLM returned JSON that does not match the {self.result_name} object contract.",
            )

        payload = cast("dict[str, object]", parsed)
        if self.error_stage == "prompt_a":
            return AuthorityClassificationResult(raw_response=raw_response, payload=payload)
        return ApplicabilityAnalysisResult(raw_response=raw_response, payload=payload)


class ClassifyAuthorityStage(JsonPromptStage):
    """Run Prompt A and validate its typed authority-classification contract."""

    def __init__(self, send_to_llm_fn: Callable[[str], str]) -> None:
        """Initialize the Prompt A stage with an LLM sender."""
        super().__init__(send_to_llm_fn=send_to_llm_fn, error_stage="prompt_a", result_name="Prompt A")


class EvaluateApplicabilityStage(JsonPromptStage):
    """Run Prompt B and validate its typed applicability-analysis contract."""

    def __init__(self, send_to_llm_fn: Callable[[str], str]) -> None:
        """Initialize the Prompt B stage with an LLM sender."""
        super().__init__(send_to_llm_fn=send_to_llm_fn, error_stage="prompt_b", result_name="Prompt B")
