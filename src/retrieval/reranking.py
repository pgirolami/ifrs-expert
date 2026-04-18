"""Optional BGE-M3 sparse and late-interaction reranking for text retrieval."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol

import numpy as np

from src.vector.bge_m3_features import BgeM3BatchFeatures, BgeM3FeatureModelProtocol, CachedBgeM3FeatureModel, LexicalWeights

if TYPE_CHECKING:
    from numpy.typing import NDArray

    from src.interfaces import SearchResult
    from src.models.chunk import Chunk

logger = logging.getLogger(__name__)

TEXT_RERANKING_MODES = {"dense", "dense_sparse", "dense_multivector", "dense_sparse_multivector"}
SCORE_NORMALIZATION_MODES = {"none", "min_max"}


@dataclass(frozen=True)
class TextRerankingOptions:
    """Configuration for text-stage candidate narrowing and reranking."""

    mode: str
    top_k_initial: int
    top_k_final: int
    dense_weight: float
    sparse_weight: float
    multivector_weight: float
    score_normalization: str


@dataclass(frozen=True)
class CandidateSignalScores:
    """Per-candidate signal scores before fusion."""

    dense_score: float
    sparse_score: float | None = None
    multivector_score: float | None = None


@dataclass(frozen=True)
class _CandidateText:
    """Resolved candidate search hit plus its chunk text."""

    result: SearchResult
    text: str


class TextRerankerProtocol(Protocol):
    """Protocol for optional text-stage reranking implementations."""

    def rerank(
        self,
        query: str,
        candidates: list[SearchResult],
        doc_chunks: dict[str, list[Chunk]],
        options: TextRerankingOptions,
    ) -> list[SearchResult]:
        """Return the reranked candidate list."""


class FeatureCacheProtocol(Protocol):
    """Optional cache hook for document-side sparse and late-interaction features."""

    def get(self, text: str) -> BgeM3BatchFeatures | None:
        """Return cached features for one text when available."""

    def set(self, text: str, features: BgeM3BatchFeatures) -> None:
        """Store features for one text."""


class InMemoryFeatureCache:
    """Simple process-local feature cache keyed by full chunk text."""

    def __init__(self) -> None:
        """Initialize the in-memory feature cache."""
        self._features_by_text: dict[str, BgeM3BatchFeatures] = {}

    def get(self, text: str) -> BgeM3BatchFeatures | None:
        """Return cached features for one text when available."""
        return self._features_by_text.get(text)

    def set(self, text: str, features: BgeM3BatchFeatures) -> None:
        """Store features for one text."""
        self._features_by_text[text] = features


class BgeM3TextReranker:
    """Rerank dense candidates with optional sparse and late-interaction signals."""

    def __init__(
        self,
        feature_model: BgeM3FeatureModelProtocol | None = None,
        feature_cache: FeatureCacheProtocol | None = None,
    ) -> None:
        """Initialize the reranker with an optional feature model and cache hook."""
        self._feature_model = feature_model or CachedBgeM3FeatureModel()
        self._feature_cache = feature_cache or InMemoryFeatureCache()

    def rerank(
        self,
        query: str,
        candidates: list[SearchResult],
        doc_chunks: dict[str, list[Chunk]],
        options: TextRerankingOptions,
    ) -> list[SearchResult]:
        """Rerank one narrowed candidate set using the configured BGE-M3 signals."""
        validate_text_reranking_options(options)

        resolved_candidates = _resolve_candidate_texts(candidates=candidates, doc_chunks=doc_chunks)
        if not resolved_candidates:
            logger.warning("Skipping text reranking because no candidate chunk texts could be resolved")
            return []

        run_sparse = uses_sparse_reranking(options.mode)
        run_multivector = uses_multivector_reranking(options.mode)
        logger.info(f"Running text reranking mode={options.mode}; candidates={len(resolved_candidates)}; sparse_ran={run_sparse}; multivector_ran={run_multivector}")

        query_features = self._feature_model.encode(
            [query],
            return_dense=True,
            return_sparse=run_sparse,
            return_colbert_vecs=run_multivector,
        )
        document_features = self._get_document_features(
            texts=[candidate.text for candidate in resolved_candidates],
            run_sparse=run_sparse,
            run_multivector=run_multivector,
        )

        candidate_signal_scores: list[CandidateSignalScores] = []
        for index, candidate in enumerate(resolved_candidates):
            sparse_score = None
            multivector_score = None
            if run_sparse:
                query_sparse = _get_sparse_feature(query_features.lexical_weights, index=0)
                document_sparse = _get_sparse_feature(document_features.lexical_weights, index=index)
                sparse_score = compute_sparse_score(query_sparse, document_sparse)
            if run_multivector:
                query_colbert = _get_colbert_feature(query_features.colbert_vecs, index=0)
                document_colbert = _get_colbert_feature(document_features.colbert_vecs, index=index)
                multivector_score = compute_multivector_score(query_colbert, document_colbert)
            candidate_signal_scores.append(
                CandidateSignalScores(
                    dense_score=float(candidate.result["score"]),
                    sparse_score=sparse_score,
                    multivector_score=multivector_score,
                )
            )

        fused_scores = fuse_candidate_scores(
            candidate_signal_scores,
            dense_weight=options.dense_weight,
            sparse_weight=options.sparse_weight,
            multivector_weight=options.multivector_weight,
            score_normalization=options.score_normalization,
        )

        reranked_results: list[SearchResult] = []
        for candidate, fused_score in zip(resolved_candidates, fused_scores, strict=True):
            reranked_results.append(
                {
                    "doc_uid": candidate.result["doc_uid"],
                    "chunk_id": candidate.result["chunk_id"],
                    "score": fused_score,
                }
            )
        return sorted(reranked_results, key=lambda result: result["score"], reverse=True)

    def _get_document_features(
        self,
        texts: list[str],
        *,
        run_sparse: bool,
        run_multivector: bool,
    ) -> BgeM3BatchFeatures:
        dense_vectors: list[NDArray[np.float32]] = []
        lexical_weights: list[LexicalWeights] = []
        colbert_vecs: list[NDArray[np.float32]] = []
        uncached_texts: list[str] = []
        uncached_indexes: list[int] = []
        cached_features_by_index: dict[int, BgeM3BatchFeatures] = {}

        for index, text in enumerate(texts):
            cached_features = self._feature_cache.get(text)
            if cached_features is None:
                uncached_texts.append(text)
                uncached_indexes.append(index)
                continue
            cached_features_by_index[index] = cached_features

        encoded_uncached_features: list[BgeM3BatchFeatures] = []
        if uncached_texts:
            batched_features = self._feature_model.encode(
                uncached_texts,
                return_dense=True,
                return_sparse=run_sparse,
                return_colbert_vecs=run_multivector,
            )
            encoded_uncached_features = _split_batch_features(batched_features=batched_features)
            for uncached_index, features in zip(uncached_indexes, encoded_uncached_features, strict=True):
                cached_features_by_index[uncached_index] = features
                self._feature_cache.set(texts[uncached_index], features)

        del encoded_uncached_features

        for index in range(len(texts)):
            features = cached_features_by_index[index]
            dense_vectors.append(_get_dense_feature(features.dense_vecs, index=0))
            if run_sparse:
                lexical_weights.append(_get_sparse_feature(features.lexical_weights, index=0))
            if run_multivector:
                colbert_vecs.append(_get_colbert_feature(features.colbert_vecs, index=0))

        dense_array = np.vstack(dense_vectors).astype(np.float32)
        return BgeM3BatchFeatures(
            dense_vecs=dense_array,
            lexical_weights=lexical_weights if run_sparse else None,
            colbert_vecs=colbert_vecs if run_multivector else None,
        )


def validate_text_reranking_options(options: TextRerankingOptions) -> None:
    """Validate a reranking config before it reaches the model."""
    if options.mode not in TEXT_RERANKING_MODES:
        message = f"Unsupported text reranking mode: {options.mode}"
        raise ValueError(message)
    if options.top_k_initial <= 0:
        message = "top_k_initial must be > 0"
        raise ValueError(message)
    if options.top_k_final <= 0:
        message = "top_k_final must be > 0"
        raise ValueError(message)
    if options.top_k_initial < options.top_k_final:
        message = "top_k_initial must be >= top_k_final"
        raise ValueError(message)
    if options.score_normalization not in SCORE_NORMALIZATION_MODES:
        message = f"Unsupported score_normalization: {options.score_normalization}"
        raise ValueError(message)


def uses_sparse_reranking(mode: str) -> bool:
    """Return whether the reranking mode needs sparse lexical scoring."""
    return mode in {"dense_sparse", "dense_sparse_multivector"}


def uses_multivector_reranking(mode: str) -> bool:
    """Return whether the reranking mode needs late-interaction scoring."""
    return mode in {"dense_multivector", "dense_sparse_multivector"}


def compute_sparse_score(query_weights: LexicalWeights, document_weights: LexicalWeights) -> float:
    """Compute weighted token overlap between query and document lexical weights."""
    overlap_tokens = set(query_weights).intersection(document_weights)
    return float(sum(query_weights[token] * document_weights[token] for token in overlap_tokens))


def compute_multivector_score(
    query_vectors: NDArray[np.float32],
    document_vectors: NDArray[np.float32],
) -> float:
    """Compute a ColBERT-style late-interaction score over normalized token vectors."""
    normalized_query = _normalize_token_matrix(query_vectors)
    normalized_document = _normalize_token_matrix(document_vectors)
    token_similarity = normalized_query @ normalized_document.T
    per_query_token_max = np.max(token_similarity, axis=1)
    return float(np.mean(per_query_token_max))


def fuse_candidate_scores(
    candidate_signal_scores: list[CandidateSignalScores],
    *,
    dense_weight: float,
    sparse_weight: float,
    multivector_weight: float,
    score_normalization: str,
) -> list[float]:
    """Fuse dense, sparse, and late-interaction scores for one narrowed candidate set."""
    dense_scores = [signal_scores.dense_score for signal_scores in candidate_signal_scores]
    sparse_scores = [signal_scores.sparse_score for signal_scores in candidate_signal_scores]
    multivector_scores = [signal_scores.multivector_score for signal_scores in candidate_signal_scores]

    normalized_dense_scores = _normalize_scores(dense_scores, score_normalization)
    normalized_sparse_scores = _normalize_optional_scores(sparse_scores, score_normalization)
    normalized_multivector_scores = _normalize_optional_scores(multivector_scores, score_normalization)

    fused_scores: list[float] = []
    for index in range(len(candidate_signal_scores)):
        fused_score = dense_weight * normalized_dense_scores[index]
        if normalized_sparse_scores is not None:
            fused_score += sparse_weight * normalized_sparse_scores[index]
        if normalized_multivector_scores is not None:
            fused_score += multivector_weight * normalized_multivector_scores[index]
        fused_scores.append(float(fused_score))
    return fused_scores


def _resolve_candidate_texts(
    candidates: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
) -> list[_CandidateText]:
    resolved_candidates: list[_CandidateText] = []
    for candidate in candidates:
        matching_chunk = _find_chunk(doc_chunks=doc_chunks, doc_uid=candidate["doc_uid"], chunk_id=candidate["chunk_id"])
        if matching_chunk is None:
            logger.warning(f"Skipping rerank candidate because chunk text is missing for doc_uid={candidate['doc_uid']} chunk_id={candidate['chunk_id']}")
            continue
        resolved_candidates.append(_CandidateText(result=candidate, text=matching_chunk.text))
    return resolved_candidates


def _find_chunk(doc_chunks: dict[str, list[Chunk]], doc_uid: str, chunk_id: int) -> Chunk | None:
    for chunk in doc_chunks.get(doc_uid, []):
        if chunk.id == chunk_id:
            return chunk
    return None


def _split_batch_features(batched_features: BgeM3BatchFeatures) -> list[BgeM3BatchFeatures]:
    dense_vecs = batched_features.dense_vecs
    lexical_weights = batched_features.lexical_weights
    colbert_vecs = batched_features.colbert_vecs
    feature_count = _resolve_feature_count(
        dense_vecs=dense_vecs,
        lexical_weights=lexical_weights,
        colbert_vecs=colbert_vecs,
    )
    split_features: list[BgeM3BatchFeatures] = []
    for index in range(feature_count):
        dense_row = None if dense_vecs is None else dense_vecs[index : index + 1]
        sparse_row = None if lexical_weights is None else [lexical_weights[index]]
        colbert_row = None if colbert_vecs is None else [colbert_vecs[index]]
        split_features.append(BgeM3BatchFeatures(dense_vecs=dense_row, lexical_weights=sparse_row, colbert_vecs=colbert_row))
    return split_features


def _resolve_feature_count(
    *,
    dense_vecs: NDArray[np.float32] | None,
    lexical_weights: list[LexicalWeights] | None,
    colbert_vecs: list[NDArray[np.float32]] | None,
) -> int:
    if dense_vecs is not None:
        return int(dense_vecs.shape[0])
    if lexical_weights is not None:
        return len(lexical_weights)
    if colbert_vecs is not None:
        return len(colbert_vecs)
    message = "Expected at least one feature set when splitting BGE-M3 batch features"
    raise ValueError(message)


def _get_dense_feature(dense_vecs: NDArray[np.float32] | None, *, index: int) -> NDArray[np.float32]:
    if dense_vecs is None:
        message = "Dense vectors were required but missing"
        raise ValueError(message)
    return dense_vecs[index]


def _get_sparse_feature(lexical_weights: list[LexicalWeights] | None, *, index: int) -> LexicalWeights:
    if lexical_weights is None:
        message = "Sparse lexical weights were required but missing"
        raise ValueError(message)
    return lexical_weights[index]


def _get_colbert_feature(colbert_vecs: list[NDArray[np.float32]] | None, *, index: int) -> NDArray[np.float32]:
    if colbert_vecs is None:
        message = "ColBERT vectors were required but missing"
        raise ValueError(message)
    return colbert_vecs[index]


def _normalize_scores(scores: list[float], score_normalization: str) -> list[float]:
    if score_normalization == "none":
        return list(scores)
    if score_normalization != "min_max":
        message = f"Unsupported score_normalization: {score_normalization}"
        raise ValueError(message)

    min_score = min(scores)
    max_score = max(scores)
    if np.isclose(min_score, max_score):
        return [0.0 for _ in scores]
    return [float((score - min_score) / (max_score - min_score)) for score in scores]


def _normalize_optional_scores(
    scores: list[float | None],
    score_normalization: str,
) -> list[float] | None:
    present_scores = [score for score in scores if score is not None]
    if not present_scores:
        return None
    normalized_scores = _normalize_scores([float(score) for score in present_scores], score_normalization)
    score_iterator = iter(normalized_scores)
    return [float(next(score_iterator)) if score is not None else 0.0 for score in scores]


def _normalize_token_matrix(token_vectors: NDArray[np.float32]) -> NDArray[np.float32]:
    norms = np.linalg.norm(token_vectors, axis=1, keepdims=True)
    safe_norms = np.where(norms == 0.0, 1.0, norms)
    return token_vectors / safe_norms
