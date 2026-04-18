"""BGE-M3 feature extraction for sparse and late-interaction reranking.

On Apple Silicon (M2 MacBook Air), M3Embedder's encode() can crash in multiprocessing
subprocess workers unless FlagEmbedding is imported BEFORE the multiprocessing context
is created. This module therefore pre-imports FlagEmbedding at the top level so that
its init-time pool creation happens safely in the main process. Subprocess workers
(e.g. bge_m3_worker.py) must also pre-import FlagEmbedding before importing this
module to maintain the same safe ordering.
"""

from __future__ import annotations

import hashlib
import importlib
import logging
import re
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from threading import Lock
from typing import TYPE_CHECKING, Protocol, cast

import numpy as np
from FlagEmbedding.inference.embedder.encoder_only.m3 import M3Embedder

from src.vector.model_cache import EMBEDDING_MODEL

if TYPE_CHECKING:
    from numpy.typing import NDArray

logger = logging.getLogger(__name__)

LexicalWeights = dict[str, float]
EXPECTED_FEATURE_NDIM = 2
BGE_M3_FEATURE_CACHE_VERSION = "v1"


@dataclass(frozen=True)
class BgeM3BatchFeatures:
    """BGE-M3 features for one encoded batch."""

    dense_vecs: NDArray[np.float32] | None
    lexical_weights: list[LexicalWeights] | None
    colbert_vecs: list[NDArray[np.float32]] | None


class BgeM3FeatureModelProtocol(Protocol):
    """Protocol for BGE-M3 sparse and colbert feature extraction."""

    def encode(
        self,
        texts: list[str],
        *,
        return_dense: bool,
        return_sparse: bool,
        return_colbert_vecs: bool,
    ) -> BgeM3BatchFeatures:
        """Encode one query-plus-candidate batch."""


class RawBgeM3ModelProtocol(Protocol):
    """Minimal instance surface used from BGEM3FlagModel."""

    def encode(
        self,
        texts: list[str],
        *,
        return_dense: bool,
        return_sparse: bool,
        return_colbert_vecs: bool,
    ) -> dict[str, object]:
        """Encode one batch and return the raw FlagEmbedding payload."""


class BgeM3ModelFactoryProtocol(Protocol):
    """Callable constructor surface for BGEM3FlagModel."""

    def __call__(self, model_name: str, *, use_fp16: bool) -> RawBgeM3ModelProtocol:
        """Create one BGEM3FlagModel instance."""


class FlagEmbeddingModuleProtocol(Protocol):
    """Minimal module surface needed from the FlagEmbedding package."""

    BGEM3FlagModel: BgeM3ModelFactoryProtocol


BgeM3FeatureModelFactory = Callable[[str], BgeM3FeatureModelProtocol]


@dataclass
class _FeatureModelCacheState:
    """Mutable process-wide state for the BGE-M3 feature model cache."""

    factory: BgeM3FeatureModelFactory | None = None


_FEATURE_MODEL_CACHE: dict[str, BgeM3FeatureModelProtocol] = {}
_FEATURE_MODEL_CACHE_LOCK = Lock()
_FEATURE_MODEL_CACHE_STATE = _FeatureModelCacheState()


class _FlagEmbeddingBgeM3Model:
    """Thin adapter over FlagEmbedding's BGEM3FlagModel."""

    def __init__(self, model_name: str) -> None:
        flag_embedding_module = _load_flag_embedding_module()
        self._model = flag_embedding_module.BGEM3FlagModel(model_name, use_fp16=False)

    def encode(
        self,
        texts: list[str],
        *,
        return_dense: bool,
        return_sparse: bool,
        return_colbert_vecs: bool,
    ) -> BgeM3BatchFeatures:
        raw_output = self._model.encode(
            texts,
            return_dense=return_dense,
            return_sparse=return_sparse,
            return_colbert_vecs=return_colbert_vecs,
        )
        dense_vecs = _coerce_dense_vectors(raw_output.get("dense_vecs")) if return_dense else None
        lexical_weights = _coerce_lexical_weights(raw_output.get("lexical_weights")) if return_sparse else None
        colbert_vecs = _coerce_colbert_vectors(raw_output.get("colbert_vecs")) if return_colbert_vecs else None
        return BgeM3BatchFeatures(
            dense_vecs=dense_vecs,
            lexical_weights=lexical_weights,
            colbert_vecs=colbert_vecs,
        )


class CachedBgeM3FeatureModel:
    """Disk-backed BGE-M3 feature model using the project's existing hash cache pattern."""

    def __init__(
        self,
        feature_model: BgeM3FeatureModelProtocol | None = None,
        *,
        cache_dir: Path | None = None,
        model_name: str = EMBEDDING_MODEL,
    ) -> None:
        """Initialize the disk-backed BGE-M3 feature cache."""
        self._feature_model = feature_model or get_bge_m3_feature_model(model_name)
        self._cache_dir = cache_dir
        self._model_name = model_name

    def encode(
        self,
        texts: list[str],
        *,
        return_dense: bool,
        return_sparse: bool,
        return_colbert_vecs: bool,
    ) -> BgeM3BatchFeatures:
        """Encode texts while persisting and reusing full BGE-M3 feature bundles."""
        cached_features_by_index: dict[int, BgeM3BatchFeatures] = {}
        uncached_indexes: list[int] = []
        uncached_texts: list[str] = []

        for index, text in enumerate(texts):
            cached_features = _load_cached_features(
                text,
                cache_dir=self._cache_dir,
                model_name=self._model_name,
            )
            if cached_features is not None:
                cached_features_by_index[index] = cached_features
                continue
            uncached_indexes.append(index)
            uncached_texts.append(text)

        if uncached_texts:
            encoded_features = self._feature_model.encode(
                uncached_texts,
                return_dense=True,
                return_sparse=True,
                return_colbert_vecs=True,
            )
            split_features = _split_batch_features(encoded_features)
            for index, features in zip(uncached_indexes, split_features, strict=True):
                cached_features_by_index[index] = features
                _save_cached_features(
                    texts[index],
                    features,
                    cache_dir=self._cache_dir,
                    model_name=self._model_name,
                )

        return _build_requested_batch_features(
            features_by_index=cached_features_by_index,
            feature_count=len(texts),
            return_dense=return_dense,
            return_sparse=return_sparse,
            return_colbert_vecs=return_colbert_vecs,
        )


def get_bge_m3_feature_model(model_name: str = EMBEDDING_MODEL) -> BgeM3FeatureModelProtocol:
    """Return a cached BGE-M3 feature model.

    Performs a warmup encode on first creation to avoid Apple Silicon MPS
    SIGSEGV crashes on first encode call (triggered by MLP layer init).
    """
    with _FEATURE_MODEL_CACHE_LOCK:
        cached_model = _FEATURE_MODEL_CACHE.get(model_name)
        if cached_model is not None:
            return cached_model

        logger.info(f"Loading BGE-M3 feature model: {model_name}")
        model_factory = _FEATURE_MODEL_CACHE_STATE.factory or _default_bge_m3_feature_model_factory
        model = model_factory(model_name)

        # Warmup: encode a dummy string to trigger PyTorch weight initialization
        # before any caller tries to encode. Without this, the first encode call
        # in a fresh Python process (e.g. multiprocessing spawn) can SIGSEGV
        # on Apple Silicon due to MLP layer lazy initialization with MPS backend.
        # Only warmup with return_dense=True to minimize crash surface.
        _warmup_bge_m3_model(model)

        _FEATURE_MODEL_CACHE[model_name] = model
        return model


class _BgeM3CpuModel:
    """BGE-M3 feature model that runs encoding on CPU only (no multiprocessing).

    Wraps FlagEmbedding's M3Embedder and overrides encode() to use
    encode_single_device instead of encode(), bypassing the multi-process
    pool that causes SIGSEGV on Apple Silicon.
    """

    def __init__(self, model_name: str) -> None:
        self._model = M3Embedder(
            model_name,
            normalize_embeddings=True,
            use_fp16=False,
            devices=["cpu"],
            return_dense=True,
            return_sparse=False,
            return_colbert_vecs=False,
        )

    def encode(
        self,
        texts: list[str],
        *,
        return_dense: bool,
        return_sparse: bool,
        return_colbert_vecs: bool,
    ) -> BgeM3BatchFeatures:
        # Use encode_single_device to avoid the multi-process pool on Apple Silicon
        raw_output = self._model.encode_single_device(
            texts,
            device="cpu",
            return_dense=return_dense,
            return_sparse=return_sparse,
            return_colbert_vecs=return_colbert_vecs,
        )
        dense_vecs = _coerce_dense_vectors(raw_output.get("dense_vecs")) if return_dense else None
        lexical_weights = _coerce_lexical_weights(raw_output.get("lexical_weights")) if return_sparse else None
        colbert_vecs = _coerce_colbert_vectors(raw_output.get("colbert_vecs")) if return_colbert_vecs else None
        return BgeM3BatchFeatures(
            dense_vecs=dense_vecs,
            lexical_weights=lexical_weights,
            colbert_vecs=colbert_vecs,
        )


def _warmup_bge_m3_model(model: BgeM3FeatureModelProtocol) -> None:
    """Run a minimal dummy encode to trigger PyTorch lazy weight initialization.

    Only requests return_dense=True to minimize memory/CPU load on Apple Silicon.
    A single warmup encode is sufficient to prevent SIGSEGV on first real encode.
    """
    try:
        model.encode(
            ["warmup"],
            return_dense=True,
            return_sparse=False,
            return_colbert_vecs=False,
        )
        logger.info("BGE-M3 warmup encode completed successfully")
    except OSError as e:
        logger.warning(f"BGE-M3 warmup encode failed (OSError): {e}")
    except RuntimeError as e:
        logger.warning(f"BGE-M3 warmup encode failed (RuntimeError): {e}")


def clear_bge_m3_feature_model_cache() -> None:
    """Clear the process-wide BGE-M3 feature model cache."""
    with _FEATURE_MODEL_CACHE_LOCK:
        _FEATURE_MODEL_CACHE.clear()


def set_bge_m3_feature_model_factory(factory: BgeM3FeatureModelFactory | None) -> None:
    """Override the BGE-M3 feature model factory used by the shared cache."""
    with _FEATURE_MODEL_CACHE_LOCK:
        _FEATURE_MODEL_CACHE_STATE.factory = factory


def _default_bge_m3_feature_model_factory(model_name: str) -> BgeM3FeatureModelProtocol:
    return _BgeM3CpuModel(model_name)


def _load_flag_embedding_module() -> FlagEmbeddingModuleProtocol:
    try:
        return cast("FlagEmbeddingModuleProtocol", importlib.import_module("FlagEmbedding"))
    except ImportError as error:
        message = "BGE-M3 sparse or multi-vector retrieval requires the FlagEmbedding package. Install it before using retrieval.text.mode values other than 'dense'."
        raise RuntimeError(message) from error


def _default_feature_cache_dir() -> Path:
    return Path(__file__).parent.parent.parent / ".cache" / "query_embeddings"


def _normalize_text_for_cache(text: str) -> str:
    return text.strip()


def _slugify_path_component(value: str) -> str:
    lowered = value.lower()
    return re.sub(r"[^a-z0-9._-]+", "_", lowered)


def _resolve_feature_cache_dir(cache_dir: Path | None) -> Path:
    resolved_cache_dir = cache_dir or _default_feature_cache_dir()
    resolved_cache_dir.mkdir(parents=True, exist_ok=True)
    return resolved_cache_dir


def _get_feature_cache_path(text: str, *, cache_dir: Path | None, model_name: str) -> Path:
    normalized_text = _normalize_text_for_cache(text)
    cache_key = f"{BGE_M3_FEATURE_CACHE_VERSION}:{model_name}:{normalized_text}"
    cache_key_hash = hashlib.sha256(cache_key.encode("utf-8")).hexdigest()
    model_slug = _slugify_path_component(model_name)
    return _resolve_feature_cache_dir(cache_dir) / f"{model_slug}--{cache_key_hash}.npz"


def _coerce_dense_vectors(value: object) -> NDArray[np.float32]:
    if value is None:
        message = "BGE-M3 dense_vecs were missing from the model output"
        raise ValueError(message)
    dense_vecs = np.asarray(value, dtype=np.float32)
    if dense_vecs.ndim != EXPECTED_FEATURE_NDIM:
        message = f"Expected BGE-M3 dense_vecs to be 2D, got shape={dense_vecs.shape}"
        raise ValueError(message)
    return dense_vecs


def _coerce_lexical_weights(value: object) -> list[LexicalWeights]:
    if not isinstance(value, list):
        message = "BGE-M3 lexical_weights were missing from the model output"
        raise TypeError(message)

    normalized_weights: list[LexicalWeights] = []
    for row in value:
        if not isinstance(row, dict):
            message = "BGE-M3 lexical_weights rows must be mappings"
            raise TypeError(message)
        normalized_row: LexicalWeights = {}
        for token_id, weight in row.items():
            token_text = str(token_id)
            if isinstance(weight, np.floating | int | float):
                normalized_row[token_text] = float(weight)
            else:
                message = "BGE-M3 lexical_weights values must be numeric"
                raise TypeError(message)
        normalized_weights.append(normalized_row)
    return normalized_weights


def _coerce_colbert_vectors(value: object) -> list[NDArray[np.float32]]:
    if not isinstance(value, list):
        message = "BGE-M3 colbert_vecs were missing from the model output"
        raise TypeError(message)

    normalized_vectors: list[NDArray[np.float32]] = []
    for row in value:
        row_vectors = np.asarray(row, dtype=np.float32)
        if row_vectors.ndim != EXPECTED_FEATURE_NDIM:
            message = f"Expected BGE-M3 colbert_vecs rows to be 2D, got shape={row_vectors.shape}"
            raise ValueError(message)
        normalized_vectors.append(cast("NDArray[np.float32]", row_vectors))
    return normalized_vectors


def _load_cached_features(text: str, *, cache_dir: Path | None, model_name: str) -> BgeM3BatchFeatures | None:
    cache_path = _get_feature_cache_path(text, cache_dir=cache_dir, model_name=model_name)
    if not cache_path.exists():
        return None
    try:
        cached_payload = np.load(cache_path, allow_pickle=False)
    except (OSError, ValueError) as error:
        logger.warning(f"Could not load cached BGE-M3 features from {cache_path}: {error}")
        return None

    has_dense = bool(int(cached_payload["has_dense"][0]))
    has_sparse = bool(int(cached_payload["has_sparse"][0]))
    has_colbert = bool(int(cached_payload["has_colbert"][0]))
    dense_vecs = None
    lexical_weights = None
    colbert_vecs = None

    if has_dense:
        dense_vecs = _coerce_dense_vectors(cached_payload["dense_vec"].reshape(1, -1))
    if has_sparse:
        lexical_tokens = cached_payload["lexical_tokens"].tolist()
        lexical_values = cached_payload["lexical_values"].astype(np.float32).tolist()
        lexical_weights = [{str(token): float(weight) for token, weight in zip(lexical_tokens, lexical_values, strict=True)}]
    if has_colbert:
        colbert_array = np.asarray(cached_payload["colbert_vecs"], dtype=np.float32)
        if colbert_array.ndim != EXPECTED_FEATURE_NDIM:
            logger.warning(f"Ignoring cached BGE-M3 colbert_vecs with invalid shape {colbert_array.shape} at {cache_path}")
            return None
        colbert_vecs = [colbert_array]

    logger.info(f"Loaded cached BGE-M3 features from {cache_path}")
    return BgeM3BatchFeatures(dense_vecs=dense_vecs, lexical_weights=lexical_weights, colbert_vecs=colbert_vecs)


def _save_cached_features(text: str, features: BgeM3BatchFeatures, *, cache_dir: Path | None, model_name: str) -> None:
    cache_path = _get_feature_cache_path(text, cache_dir=cache_dir, model_name=model_name)
    dense_vec = np.empty((0,), dtype=np.float32)
    lexical_tokens = np.asarray([], dtype=str)
    lexical_values = np.asarray([], dtype=np.float32)
    colbert_vecs = np.empty((0, 0), dtype=np.float32)

    if features.dense_vecs is not None:
        dense_vec = _coerce_dense_vectors(features.dense_vecs)[0]
    if features.lexical_weights is not None:
        lexical_weights = features.lexical_weights[0]
        lexical_tokens = np.asarray(list(lexical_weights.keys()), dtype=str)
        lexical_values = np.asarray(list(lexical_weights.values()), dtype=np.float32)
    if features.colbert_vecs is not None:
        colbert_vecs = _coerce_colbert_vectors(features.colbert_vecs)[0]

    try:
        np.savez_compressed(
            cache_path,
            has_dense=np.asarray([1 if features.dense_vecs is not None else 0], dtype=np.uint8),
            dense_vec=dense_vec,
            has_sparse=np.asarray([1 if features.lexical_weights is not None else 0], dtype=np.uint8),
            lexical_tokens=lexical_tokens,
            lexical_values=lexical_values,
            has_colbert=np.asarray([1 if features.colbert_vecs is not None else 0], dtype=np.uint8),
            colbert_vecs=colbert_vecs,
        )
    except OSError as error:
        logger.warning(f"Could not save cached BGE-M3 features to {cache_path}: {error}")
        return
    logger.info(f"Saved cached BGE-M3 features to {cache_path}")


def _build_requested_batch_features(
    *,
    features_by_index: dict[int, BgeM3BatchFeatures],
    feature_count: int,
    return_dense: bool,
    return_sparse: bool,
    return_colbert_vecs: bool,
) -> BgeM3BatchFeatures:
    dense_rows: list[NDArray[np.float32]] = []
    sparse_rows: list[LexicalWeights] = []
    colbert_rows: list[NDArray[np.float32]] = []

    for index in range(feature_count):
        features = features_by_index[index]
        if return_dense:
            dense_rows.append(_coerce_dense_vectors(features.dense_vecs)[0])
        if return_sparse:
            sparse_rows.append(_coerce_lexical_weights(features.lexical_weights)[0])
        if return_colbert_vecs:
            colbert_rows.append(_coerce_colbert_vectors(features.colbert_vecs)[0])

    dense_vecs = np.vstack(dense_rows).astype(np.float32) if return_dense else None
    return BgeM3BatchFeatures(
        dense_vecs=dense_vecs,
        lexical_weights=sparse_rows if return_sparse else None,
        colbert_vecs=colbert_rows if return_colbert_vecs else None,
    )


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
