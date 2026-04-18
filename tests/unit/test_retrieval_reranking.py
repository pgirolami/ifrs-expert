"""Tests for text-stage BGE-M3 reranking modes."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from src.interfaces import SearchResult
from src.models.chunk import Chunk
from src.policy import load_policy_config
from src.retrieval.models import RetrievalRequest
from src.retrieval.pipeline import RetrievalPipelineConfig, execute_retrieval
from src.retrieval.reranking import CandidateSignalScores, BgeM3TextReranker, TextRerankingOptions, fuse_candidate_scores
from src.vector.bge_m3_features import BgeM3BatchFeatures
from tests.fakes import InMemoryChunkStore


class _MockVectorStore:
    """Simple chunk vector store fake for reranking tests."""

    def __init__(self, search_results: list[SearchResult]) -> None:
        self._search_results = search_results

    def __enter__(self) -> "_MockVectorStore":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[SearchResult]:
        del query
        return list(self._search_results)


class _MockIndexPath:
    """Simple index-path fake that always exists."""

    def exists(self) -> bool:
        return True


class _RecordingTextReranker:
    """Pipeline fake that records the narrowed candidate set."""

    def __init__(self, reranked_results: list[SearchResult]) -> None:
        self.calls: list[tuple[str, list[SearchResult], TextRerankingOptions]] = []
        self._reranked_results = reranked_results

    def rerank(
        self,
        query: str,
        candidates: list[SearchResult],
        doc_chunks: dict[str, list[Chunk]],
        options: TextRerankingOptions,
    ) -> list[SearchResult]:
        del doc_chunks
        self.calls.append((query, list(candidates), options))
        return list(self._reranked_results)


class _FailingTextReranker:
    """Dense-mode guard fake that should never be called."""

    def rerank(
        self,
        query: str,
        candidates: list[SearchResult],
        doc_chunks: dict[str, list[Chunk]],
        options: TextRerankingOptions,
    ) -> list[SearchResult]:
        del query, candidates, doc_chunks, options
        raise AssertionError("Dense mode should not call the text reranker")


class _FakeBgeM3Model:
    """Deterministic fake BGE-M3 model returning sparse and colbert features."""

    def __init__(self) -> None:
        self.calls: list[tuple[tuple[str, ...], bool, bool, bool]] = []

    def encode(
        self,
        texts: list[str],
        *,
        return_dense: bool,
        return_sparse: bool,
        return_colbert_vecs: bool,
    ) -> BgeM3BatchFeatures:
        self.calls.append((tuple(texts), return_dense, return_sparse, return_colbert_vecs))
        dense_vecs = np.asarray(
            [
                [1.0, 0.0] if text == "query" else [0.9, 0.1] if text == "candidate-a" else [0.4, 0.6]
                for text in texts
            ],
            dtype=np.float32,
        )
        lexical_weights = [
            {"shared": 1.0, "query_only": 0.5}
            if text == "query"
            else {"shared": 1.0}
            if text == "candidate-a"
            else {"query_only": 0.1}
            for text in texts
        ]
        colbert_vecs = [
            np.asarray([[1.0, 0.0], [0.0, 1.0]], dtype=np.float32)
            if text == "query"
            else np.asarray([[1.0, 0.0], [0.0, 1.0]], dtype=np.float32)
            if text == "candidate-a"
            else np.asarray([[0.0, 1.0], [1.0, 0.0]], dtype=np.float32)
            for text in texts
        ]
        return BgeM3BatchFeatures(
            dense_vecs=dense_vecs,
            lexical_weights=lexical_weights,
            colbert_vecs=colbert_vecs,
        )


def _build_chunk_store() -> InMemoryChunkStore:
    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="1.1", page_start="A1", page_end="A1", text="candidate-a"),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="1.2", page_start="A2", page_end="A2", text="candidate-b"),
                Chunk(id=3, doc_uid="ias7", chunk_number="2.1", page_start="B1", page_end="B1", text="candidate-b"),
            ]
        )
    return chunk_store


def _build_request(text_search_mode: str) -> RetrievalRequest:
    return RetrievalRequest(
        query="query",
        retrieval_mode="text",
        text_search_mode=text_search_mode,
        k=5,
        d=5,
        document_d_by_type={},
        document_min_score_by_type={},
        document_expand_to_section_by_type={},
        chunk_min_score=0.0,
        expand_to_section=False,
        expand=0,
        full_doc_threshold=0,
        top_k_initial=2,
        top_k_final=1,
        dense_weight=1.0,
        sparse_weight=0.5,
        multivector_weight=0.5,
        score_normalization="none",
    )


def test_load_policy_config_parses_text_reranking_fields(tmp_path: Path) -> None:
    """Policy loader should parse the text-stage reranking fields."""
    config_path = tmp_path / "policy.yaml"
    config_path.write_text(
        """
retrieval:
  mode: text
  k: 5
  expand: 0
  full_doc_threshold: 0
  expand_to_section: true
  text:
    mode: dense_sparse_multivector
    min_score: 0.4
    top_k_initial: 12
    top_k_final: 5
    score_normalization: min_max
    fusion:
      dense: 1.0
      sparse: 0.3
      multivector: 0.7
  titles:
    min_score: 0.6
  documents:
    global_d: 1
    by_document_type:
      IFRS-S: {d: 1, min_score: 0.5, expand_to_section: true}
      IFRS-BC: {d: 1, min_score: 0.5, expand_to_section: false}
      IFRS-IE: {d: 1, min_score: 0.5, expand_to_section: false}
      IFRS-IG: {d: 1, min_score: 0.5, expand_to_section: true}
      IAS-S: {d: 1, min_score: 0.5, expand_to_section: true}
      IAS-BC: {d: 1, min_score: 0.5, expand_to_section: false}
      IAS-IE: {d: 1, min_score: 0.5, expand_to_section: false}
      IAS-IG: {d: 1, min_score: 0.5, expand_to_section: true}
      IFRIC: {d: 1, min_score: 0.5, expand_to_section: true}
      IFRIC-BC: {d: 1, min_score: 0.5, expand_to_section: false}
      IFRIC-IE: {d: 1, min_score: 0.5, expand_to_section: false}
      SIC: {d: 1, min_score: 0.5, expand_to_section: true}
      SIC-BC: {d: 1, min_score: 0.5, expand_to_section: false}
      SIC-IE: {d: 1, min_score: 0.5, expand_to_section: false}
      NAVIS: {d: 1, min_score: 0.5, expand_to_section: true}
      PS: {d: 1, min_score: 0.5, expand_to_section: true}
      PS-BC: {d: 1, min_score: 0.5, expand_to_section: false}
""".strip(),
        encoding="utf-8",
    )

    policy = load_policy_config(config_path).retrieval

    assert policy.text.mode == "dense_sparse_multivector"
    assert policy.text.top_k_initial == 12
    assert policy.text.top_k_final == 5
    assert policy.text.score_normalization == "min_max"
    assert policy.text.dense_weight == 1.0
    assert policy.text.sparse_weight == 0.3
    assert policy.text.multivector_weight == 0.7


def test_load_policy_config_rejects_invalid_reranking_window(tmp_path: Path) -> None:
    """Policy loader should reject top_k_initial values below top_k_final."""
    config_path = tmp_path / "invalid-policy.yaml"
    config_path.write_text(
        """
retrieval:
  mode: text
  k: 5
  expand: 0
  full_doc_threshold: 0
  expand_to_section: true
  text:
    mode: dense_sparse
    min_score: 0.4
    top_k_initial: 4
    top_k_final: 5
  titles:
    min_score: 0.6
  documents:
    global_d: 1
    by_document_type:
      IFRS-S: {d: 1, min_score: 0.5, expand_to_section: true}
      IFRS-BC: {d: 1, min_score: 0.5, expand_to_section: false}
      IFRS-IE: {d: 1, min_score: 0.5, expand_to_section: false}
      IFRS-IG: {d: 1, min_score: 0.5, expand_to_section: true}
      IAS-S: {d: 1, min_score: 0.5, expand_to_section: true}
      IAS-BC: {d: 1, min_score: 0.5, expand_to_section: false}
      IAS-IE: {d: 1, min_score: 0.5, expand_to_section: false}
      IAS-IG: {d: 1, min_score: 0.5, expand_to_section: true}
      IFRIC: {d: 1, min_score: 0.5, expand_to_section: true}
      IFRIC-BC: {d: 1, min_score: 0.5, expand_to_section: false}
      IFRIC-IE: {d: 1, min_score: 0.5, expand_to_section: false}
      SIC: {d: 1, min_score: 0.5, expand_to_section: true}
      SIC-BC: {d: 1, min_score: 0.5, expand_to_section: false}
      SIC-IE: {d: 1, min_score: 0.5, expand_to_section: false}
      NAVIS: {d: 1, min_score: 0.5, expand_to_section: true}
      PS: {d: 1, min_score: 0.5, expand_to_section: true}
      PS-BC: {d: 1, min_score: 0.5, expand_to_section: false}
""".strip(),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="top_k_initial"):
        load_policy_config(config_path)


def test_dense_text_mode_keeps_existing_pipeline_path() -> None:
    """Dense text mode should bypass the reranker entirely."""
    request = _build_request(text_search_mode="dense")
    chunk_store = _build_chunk_store()
    error, retrieval_result = execute_retrieval(
        request=request,
        config=RetrievalPipelineConfig(
            vector_store=_MockVectorStore(
                [
                    {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.91},
                    {"doc_uid": "ifrs9", "chunk_id": 2, "score": 0.82},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=_MockIndexPath,
            text_reranker=_FailingTextReranker(),
        ),
    )

    assert error is None
    assert retrieval_result is not None
    assert [chunk["chunk_id"] for chunk in retrieval_result.chunk_results] == [1, 2]
    assert [chunk["score"] for chunk in retrieval_result.chunk_results] == [0.91, 0.82]


def test_reranking_modes_only_process_the_narrowed_candidate_set() -> None:
    """Reranking should receive only the configured dense top_k_initial candidates."""
    request = _build_request(text_search_mode="dense_sparse")
    chunk_store = _build_chunk_store()
    text_reranker = _RecordingTextReranker(
        reranked_results=[
            {"doc_uid": "ifrs9", "chunk_id": 2, "score": 0.99},
            {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.98},
        ]
    )

    error, retrieval_result = execute_retrieval(
        request=request,
        config=RetrievalPipelineConfig(
            vector_store=_MockVectorStore(
                [
                    {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.91},
                    {"doc_uid": "ifrs9", "chunk_id": 2, "score": 0.82},
                    {"doc_uid": "ias7", "chunk_id": 3, "score": 0.81},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=_MockIndexPath,
            text_reranker=text_reranker,
        ),
    )

    assert error is None
    assert retrieval_result is not None
    assert len(text_reranker.calls) == 1
    _, narrowed_candidates, options = text_reranker.calls[0]
    assert [(candidate["doc_uid"], candidate["chunk_id"]) for candidate in narrowed_candidates] == [("ifrs9", 1), ("ifrs9", 2)]
    assert options.top_k_initial == 2
    assert options.top_k_final == 1
    assert [chunk["chunk_id"] for chunk in retrieval_result.chunk_results] == [2]


def test_fuse_candidate_scores_uses_requested_weights() -> None:
    """Score fusion should apply the configured weighted sum."""
    fused_scores = fuse_candidate_scores(
        [
            CandidateSignalScores(dense_score=0.8, sparse_score=0.2, multivector_score=0.3),
            CandidateSignalScores(dense_score=0.5, sparse_score=0.9, multivector_score=0.1),
        ],
        dense_weight=0.5,
        sparse_weight=0.25,
        multivector_weight=0.25,
        score_normalization="none",
    )

    assert fused_scores == pytest.approx([0.525, 0.5])


def test_dense_sparse_mode_only_requests_sparse_features() -> None:
    """The sparse hybrid path should not request colbert vectors."""
    model = _FakeBgeM3Model()
    reranker = BgeM3TextReranker(feature_model=model)
    reranked = reranker.rerank(
        query="query",
        candidates=[
            {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.7},
            {"doc_uid": "ifrs9", "chunk_id": 2, "score": 0.6},
        ],
        doc_chunks={
            "ifrs9": [
                Chunk(id=1, doc_uid="ifrs9", text="candidate-a"),
                Chunk(id=2, doc_uid="ifrs9", text="candidate-b"),
            ]
        },
        options=TextRerankingOptions(
            mode="dense_sparse",
            top_k_initial=2,
            top_k_final=2,
            dense_weight=1.0,
            sparse_weight=1.0,
            multivector_weight=0.0,
            score_normalization="none",
        ),
    )

    assert [candidate["chunk_id"] for candidate in reranked] == [1, 2]
    assert model.calls == [
        (("query",), True, True, False),
        (("candidate-a", "candidate-b"), True, True, False),
    ]


def test_dense_multivector_mode_only_requests_colbert_features() -> None:
    """The multi-vector hybrid path should not request sparse features."""
    model = _FakeBgeM3Model()
    reranker = BgeM3TextReranker(feature_model=model)
    reranked = reranker.rerank(
        query="query",
        candidates=[
            {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.7},
            {"doc_uid": "ifrs9", "chunk_id": 2, "score": 0.6},
        ],
        doc_chunks={
            "ifrs9": [
                Chunk(id=1, doc_uid="ifrs9", text="candidate-a"),
                Chunk(id=2, doc_uid="ifrs9", text="candidate-b"),
            ]
        },
        options=TextRerankingOptions(
            mode="dense_multivector",
            top_k_initial=2,
            top_k_final=2,
            dense_weight=1.0,
            sparse_weight=0.0,
            multivector_weight=1.0,
            score_normalization="none",
        ),
    )

    assert [candidate["chunk_id"] for candidate in reranked] == [1, 2]
    assert model.calls == [
        (("query",), True, False, True),
        (("candidate-a", "candidate-b"), True, False, True),
    ]


def test_dense_sparse_multivector_mode_requests_all_signals() -> None:
    """The full hybrid path should request both sparse and colbert features."""
    model = _FakeBgeM3Model()
    reranker = BgeM3TextReranker(feature_model=model)
    reranked = reranker.rerank(
        query="query",
        candidates=[
            {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.7},
            {"doc_uid": "ifrs9", "chunk_id": 2, "score": 0.6},
        ],
        doc_chunks={
            "ifrs9": [
                Chunk(id=1, doc_uid="ifrs9", text="candidate-a"),
                Chunk(id=2, doc_uid="ifrs9", text="candidate-b"),
            ]
        },
        options=TextRerankingOptions(
            mode="dense_sparse_multivector",
            top_k_initial=2,
            top_k_final=2,
            dense_weight=1.0,
            sparse_weight=1.0,
            multivector_weight=1.0,
            score_normalization="none",
        ),
    )

    assert [candidate["chunk_id"] for candidate in reranked] == [1, 2]
    assert model.calls == [
        (("query",), True, True, True),
        (("candidate-a", "candidate-b"), True, True, True),
    ]
