"""Workflow stages for IFRS case analysis."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol

from src.case_analysis.models import RetrievedSourcePackage, ValidatedQuestion, ValidationFailure
from src.retrieval.pipeline import execute_retrieval
from src.retrieval.request_builder import build_retrieval_request

if TYPE_CHECKING:
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
