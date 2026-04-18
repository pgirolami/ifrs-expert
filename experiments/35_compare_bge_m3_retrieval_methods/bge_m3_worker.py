#!/usr/bin/env python
"""Standalone BGE-M3 reranking worker for use in subprocess workers.

This script is run as a standalone Python file in a subprocess to avoid
the Apple Silicon SIGSEGV issue with FlagEmbedding + multiprocessing.
The subprocess must pre-import FlagEmbedding BEFORE importing bge_m3_features.
"""

import json
import os
import sys
from pathlib import Path

# Force CPU-only on Apple Silicon before ANY torch import
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"
os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "0"
os.environ["PYTHONHASHSEED"] = "0"

# Add repo to path
repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))

# CRITICAL: Pre-import FlagEmbedding BEFORE importing bge_m3_features.
# Without this pre-import, M3Embedder can SIGSEGV on Apple Silicon
# in spawn subprocess workers.
import FlagEmbedding  # noqa: F401

# Now safe to import bge_m3_features
from src.models.chunk import Chunk


def rerank(
    ranked_results: list[dict],
    mode: str,
    dense_weight: float,
    sparse_weight: float,
    multivector_weight: float,
    score_normalization: str,
    top_k_initial: int,
    top_k_final: int,
    doc_chunks_override: dict | None = None,
) -> dict:
    """Run BGE-M3 reranking and return results as JSON-serializable dict.

    When doc_chunks_override is provided, those chunks are used directly and the
    database lookup is skipped. This is used when doc_chunks have already been
    fetched in the caller (e.g., per-type retrieval in the main process).
    """
    from src.db import ChunkStore, init_db
    from src.retrieval.reranking import BgeM3TextReranker, TextRerankingOptions

    if doc_chunks_override is not None:
        # doc_chunks_override contains dicts; convert to Chunk objects for the reranker.
        candidates = ranked_results  # use as-is (already top_k_initial per type)
        doc_chunks: dict[str, list[Chunk]] = {
            du: [
                Chunk(
                    id=cd["id"],
                    doc_uid=cd["doc_uid"],
                    text=cd["text"],
                    chunk_number=cd["chunk_number"],
                    page_start=cd["page_start"],
                    page_end=cd["page_end"],
                )
                for cd in chunk_dicts
            ]
            for du, chunk_dicts in doc_chunks_override.items()
        }
    else:
        init_db()
        chunk_store = ChunkStore()
        candidates = ranked_results[:top_k_initial]
        doc_uids = list(dict.fromkeys(c["doc_uid"] for c in candidates))
        doc_chunks = {}
        with chunk_store as cs:
            for du in doc_uids:
                doc_chunks[du] = cs.get_chunks_by_doc(du)

    reranker = BgeM3TextReranker()
    reranked = reranker.rerank(
        query=_QUERY,
        candidates=candidates,
        doc_chunks=doc_chunks,
        options=TextRerankingOptions(
            mode=mode,
            top_k_initial=top_k_initial,
            top_k_final=top_k_final,
            dense_weight=dense_weight,
            sparse_weight=sparse_weight,
            multivector_weight=multivector_weight,
            score_normalization=score_normalization,
            document_types=None,  # Already filtered per-type in caller
        ),
    )

    return {
        "status": "ok",
        "reranked": reranked,
        "doc_chunks": {
            du: [
                {
                    "id": c.id,
                    "doc_uid": c.doc_uid,
                    "text": c.text,
                    "chunk_number": c.chunk_number,
                    "page_start": c.page_start,
                    "page_end": c.page_end,
                }
                for c in chunks
            ]
            for du, chunks in doc_chunks.items()
        },
    }


def rerank_per_type(
    ranked_results: list[dict],
    doc_chunks_override: dict,
    document_types: list[str],
    mode: str,
    dense_weight: float,
    sparse_weight: float,
    multivector_weight: float,
    score_normalization: str,
    top_k_per_type: int,
    k_per_type: int,
) -> dict:
    """Run BGE-M3 reranking separately for each document type, then merge results.

    This gives every document type a fair shot: each type's candidates are ranked
    independently by BGE-M3, and the per-type top documents are merged at the end.
    This is the "method 8" approach.

    Args:
        ranked_results: Full dense retrieval results (all chunks, not sliced).
        doc_chunks_override: Pre-fetched chunk data keyed by doc_uid.
        document_types: List of all document types to process.
        mode: BGE-M3 reranking mode.
        dense_weight, sparse_weight, multivector_weight: Fusion weights.
        score_normalization: Score normalization mode.
        top_k_per_type: Number of dense candidates to consider per document type.
        k_per_type: Number of chunks to select per document within each type.

    Returns:
        Merged reranking results across all document types.
    """
    from src.retrieval.reranking import BgeM3TextReranker, TextRerankingOptions

    # Build doc_type lookup from doc_chunks_override
    doc_type_by_uid: dict[str, str] = {}
    for du in doc_chunks_override:
        doc_type_by_uid[du] = _infer_doc_type(du)

    # Group ranked_results by document type
    by_type: dict[str, list[dict]] = {dt: [] for dt in document_types}
    for result in ranked_results:
        doc_type = doc_type_by_uid.get(result["doc_uid"])
        if doc_type in by_type:
            by_type[doc_type].append(result)

    # Take top_k_per_type candidates per type (sorted by dense score)
    per_type_candidates: dict[str, list[dict]] = {}
    for doc_type in document_types:
        sorted_type = sorted(by_type[doc_type], key=lambda r: r["score"], reverse=True)
        per_type_candidates[doc_type] = sorted_type[:top_k_per_type]

    # Build doc_chunks as Chunk objects
    doc_chunks: dict[str, list[Chunk]] = {
        du: [
            Chunk(
                id=cd["id"],
                doc_uid=cd["doc_uid"],
                text=cd["text"],
                chunk_number=cd["chunk_number"],
                page_start=cd["page_start"],
                page_end=cd["page_end"],
            )
            for cd in chunk_dicts
        ]
        for du, chunk_dicts in doc_chunks_override.items()
    }

    # Run BGE-M3 reranker once with all per-type candidates
    # (the reranker will score all candidates, no top_k filtering needed here)
    all_candidates: list[dict] = []
    for dt in document_types:
        all_candidates.extend(per_type_candidates[dt])

    if not all_candidates:
        return {
            "status": "ok",
            "reranked": [],
            "per_type_results": {},
            "doc_chunks": {},
        }

    reranker = BgeM3TextReranker()
    reranked = reranker.rerank(
        query=_QUERY,
        candidates=all_candidates,
        doc_chunks=doc_chunks,
        options=TextRerankingOptions(
            mode=mode,
            top_k_initial=len(all_candidates),
            top_k_final=len(all_candidates),
            dense_weight=dense_weight,
            sparse_weight=sparse_weight,
            multivector_weight=multivector_weight,
            score_normalization=score_normalization,
            document_types=document_types,  # tell reranker to filter per-type
        ),
    )

    # Now apply per-type selection: for each document type, take its best k_per_type chunks
    # Group reranked results by doc_uid → doc_type
    by_doc: dict[str, dict] = {}
    for r in reranked:
        du = r["doc_uid"]
        doc_type = doc_type_by_uid.get(du)
        if doc_type not in by_doc:
            by_doc[du] = {"doc_uid": du, "doc_type": doc_type, "chunks": [], "top_score": 0.0}
        by_doc[du]["chunks"].append(r)
        by_doc[du]["top_score"] = max(by_doc[du]["top_score"], r["score"])

    # Group documents by type
    docs_by_type: dict[str, list[dict]] = {dt: [] for dt in document_types}
    for doc_data in by_doc.values():
        dt = doc_data["doc_type"]
        if dt in docs_by_type:
            docs_by_type[dt].append(doc_data)

    # Per-type selection: for each type, sort docs by score, take top chunks
    selected_per_type: dict[str, list[dict]] = {}
    for doc_type in document_types:
        docs = sorted(docs_by_type[doc_type], key=lambda d: d["top_score"], reverse=True)
        type_selected: list[dict] = []
        for doc_data in docs:
            if len(type_selected) >= k_per_type * 3:  # reasonable limit
                break
            for chunk in sorted(doc_data["chunks"], key=lambda c: c["score"], reverse=True):
                if len(type_selected) >= k_per_type * 3:
                    break
                type_selected.append(chunk)
        selected_per_type[doc_type] = type_selected

    # Merge all per-type selected chunks, sort globally, apply min_score filter
    all_selected: list[dict] = []
    for chunks in selected_per_type.values():
        all_selected.extend(chunks)
    all_selected_sorted = sorted(all_selected, key=lambda r: r["score"], reverse=True)

    # Final per-doc selection
    from src.retrieval.pipeline import _select_top_k_per_document

    final_selected = _select_top_k_per_document(
        ranked_results=all_selected_sorted,
        k=5,  # global k
        min_score=0.0,  # no min_score filter at this stage
    )

    return {
        "status": "ok",
        "reranked": final_selected,
        "per_type_results": {
            dt: [c["doc_uid"] for c in sorted(chunks, key=lambda x: x["score"], reverse=True)]
            for dt, chunks in selected_per_type.items()
            if chunks
        },
        "doc_chunks": {
            du: [
                {
                    "id": c.id,
                    "doc_uid": c.doc_uid,
                    "text": c.text,
                    "chunk_number": c.chunk_number,
                    "page_start": c.page_start,
                    "page_end": c.page_end,
                }
                for c in chunk_list
            ]
            for du, chunk_list in doc_chunks.items()
        },
    }


def _infer_doc_type(doc_uid: str) -> str:
    """Infer document type from doc_uid string."""
    uid_lower = doc_uid.lower()
    if uid_lower.startswith("navis-"):
        return "NAVIS"
    if "-bc" in uid_lower:
        prefix = uid_lower.split("-bc")[0]
        if prefix.startswith("ifrs"):
            return "IFRS-BC"
        if prefix.startswith("ias"):
            return "IAS-BC"
        if prefix.startswith("ifric"):
            return "IFRIC-BC"
        if prefix.startswith("sic"):
            return "SIC-BC"
        if prefix.startswith("ps"):
            return "PS-BC"
    if "-ig" in uid_lower:
        prefix = uid_lower.split("-ig")[0]
        if prefix.startswith("ifrs"):
            return "IFRS-IG"
        if prefix.startswith("ias"):
            return "IAS-IG"
        if prefix.startswith("ifric"):
            return "IFRIC-IG"
    if "-ie" in uid_lower:
        prefix = uid_lower.split("-ie")[0]
        if prefix.startswith("ifrs"):
            return "IFRS-IE"
        if prefix.startswith("ias"):
            return "IAS-IE"
        if prefix.startswith("ifric"):
            return "IFRIC-IE"
        if prefix.startswith("sic"):
            return "SIC-IE"
    if uid_lower.startswith("ifrs"):
        return "IFRS-S"
    if uid_lower.startswith("ias"):
        return "IAS-S"
    if uid_lower.startswith("ifric"):
        return "IFRIC"
    if uid_lower.startswith("sic"):
        return "SIC"
    if uid_lower.startswith("ps"):
        return "PS"
    return "unknown"


_QUERY = (
    "Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés "
    "sur la partie change relative aux dividendes intragroupe pour lesquels une créance à "
    "recevoir a été comptabilisée ?"
)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Standalone BGE-M3 reranking worker")
    parser.add_argument("--input", type=str, required=True, help="Path to JSON input file")
    parser.add_argument("--output", type=str, required=True, help="Path to JSON output file")
    parser.add_argument(
        "--mode",
        type=str,
        default="rerank",
        choices=["rerank", "per_type"],
        help="rerank: standard BGE-M3 reranking; per_type: per-document-type reranking",
    )
    args = parser.parse_args()

    with open(args.input) as f:
        payload = json.load(f)

    if args.mode == "per_type":
        from src.models.document import DOCUMENT_TYPES

        result = rerank_per_type(
            ranked_results=payload["ranked_results"],
            doc_chunks_override=payload.get("doc_chunks_override"),
            document_types=list(DOCUMENT_TYPES),
            mode=payload["mode"],
            dense_weight=payload["dense_weight"],
            sparse_weight=payload["sparse_weight"],
            multivector_weight=payload["multivector_weight"],
            score_normalization=payload["score_normalization"],
            top_k_per_type=payload.get("top_k_per_type", 100),
            k_per_type=payload.get("k_per_type", 3),
        )
    else:
        result = rerank(
            ranked_results=payload["ranked_results"],
            mode=payload["mode"],
            dense_weight=payload["dense_weight"],
            sparse_weight=payload["sparse_weight"],
            multivector_weight=payload["multivector_weight"],
            score_normalization=payload["score_normalization"],
            top_k_initial=payload["top_k_initial"],
            top_k_final=payload["top_k_final"],
            doc_chunks_override=payload.get("doc_chunks_override"),
        )

    with open(args.output, "w") as f:
        json.dump(result, f)
