"""Tests for persistent BGE-M3 feature caching."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from src.vector.bge_m3_features import BgeM3BatchFeatures, CachedBgeM3FeatureModel


@dataclass
class _RecordingBgeM3FeatureModel:
    """Fake BGE-M3 feature model used to verify cache reuse."""

    calls: list[tuple[tuple[str, ...], bool, bool, bool]]

    def encode(
        self,
        texts: list[str],
        *,
        return_dense: bool,
        return_sparse: bool,
        return_colbert_vecs: bool,
    ) -> BgeM3BatchFeatures:
        """Return deterministic features for the requested texts."""
        self.calls.append((tuple(texts), return_dense, return_sparse, return_colbert_vecs))
        dense_vectors = np.asarray([[float(len(text)), 1.0] for text in texts], dtype=np.float32)
        lexical_weights = [{text: float(index + 1)} for index, text in enumerate(texts)]
        colbert_vectors = [
            np.asarray([[float(index + 1), float(len(text))]], dtype=np.float32)
            for index, text in enumerate(texts)
        ]
        return BgeM3BatchFeatures(
            dense_vecs=dense_vectors,
            lexical_weights=lexical_weights,
            colbert_vecs=colbert_vectors,
        )


def test_cached_bge_m3_feature_model_reuses_disk_cache(tmp_path: Path) -> None:
    """Feature cache should persist sparse and colbert outputs across instances."""
    first_model = _RecordingBgeM3FeatureModel(calls=[])
    cache_dir = tmp_path / "query_cache"
    cached_model = CachedBgeM3FeatureModel(
        feature_model=first_model,
        cache_dir=cache_dir,
    )

    first_result = cached_model.encode(
        ["query text", "document text"],
        return_dense=True,
        return_sparse=True,
        return_colbert_vecs=True,
    )

    assert len(first_model.calls) == 1
    assert cache_dir.exists() is True
    assert list(cache_dir.glob("*.npz"))
    assert first_result.lexical_weights == [{"query text": 1.0}, {"document text": 2.0}]

    second_model = _RecordingBgeM3FeatureModel(calls=[])
    reloaded_cached_model = CachedBgeM3FeatureModel(
        feature_model=second_model,
        cache_dir=cache_dir,
    )

    second_result = reloaded_cached_model.encode(
        ["query text", "document text"],
        return_dense=False,
        return_sparse=True,
        return_colbert_vecs=True,
    )

    assert second_model.calls == []
    assert second_result.dense_vecs is None
    assert second_result.lexical_weights == [{"query text": 1.0}, {"document text": 2.0}]
    assert second_result.colbert_vecs is not None
    assert len(second_result.colbert_vecs) == 2
