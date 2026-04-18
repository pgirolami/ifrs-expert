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
    k_per_type_overrides: dict[str, int] | None = None,
    chunk_limit_per_type: int | None = None,
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

    # STEP 1: Dense retrieval summary
    _log: list[str] = []
    _log.append("[Step 1 - Dense retrieval] "
                f"{len(ranked_results)} total chunks from {len({r['doc_uid'] for r in ranked_results})} docs")
    for dt in document_types:
        chunks = by_type.get(dt, [])
        docs = sorted({r["doc_uid"] for r in chunks})
        top = max((r["score"] for r in chunks), default=None)
        top_str = f"top={top:.4f}" if top is not None else "no chunks"
        _log.append(f"  {dt}: {len(chunks)} chunks, {len(docs)} docs ({top_str})")

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

    # Run BGE-M3 reranker SEPARATELY for each document type.
    # Each type's chunks are scored only against other chunks from the same type,
    # giving rarer document types a fair shot rather than letting NAVIS dominate
    # a global ranking.
    reranker = BgeM3TextReranker()
    per_type_reranked: dict[str, list[dict]] = {}
    _log.append(
        f"\n[Step 2 - Candidates to BGE-M3] top_k_per_type={top_k_per_type}:"
    )
    for doc_type in document_types:
        type_candidates = per_type_candidates.get(doc_type, [])
        _log.append(
            f"  {doc_type}: {len(type_candidates)} chunks "
            f"({len({c['doc_uid'] for c in type_candidates})} docs)"
        )
        if not type_candidates:
            _log.append(f"    -> SKIPPED (no candidates)")
            continue

        _log.append(f"    -> Running BGE-M3 reranking for {doc_type}...")
        reranked_for_type = reranker.rerank(
            query=_QUERY,
            candidates=type_candidates,
            doc_chunks=doc_chunks,
            options=TextRerankingOptions(
                mode=mode,
                top_k_initial=len(type_candidates),
                top_k_final=len(type_candidates),
                dense_weight=dense_weight,
                sparse_weight=sparse_weight,
                multivector_weight=multivector_weight,
                score_normalization=score_normalization,
                document_types=None,  # no per-type filter within a single-type pass
            ),
        )
        per_type_reranked[doc_type] = reranked_for_type
        # Log top 3 docs after BGE-M3 reranking
        by_doc: dict[str, dict] = {}
        for r in reranked_for_type:
            du = r["doc_uid"]
            if du not in by_doc:
                by_doc[du] = {"doc_uid": du, "top_score": r["score"], "n": 0}
            by_doc[du]["top_score"] = max(by_doc[du]["top_score"], r["score"])
            by_doc[du]["n"] += 1
        top3 = sorted(by_doc.values(), key=lambda d: d["top_score"], reverse=True)[:3]
        _log.append(
            f"    Top 3 after BGE-M3: "
            + ", ".join(f"{d['doc_uid']}({d['top_score']:.4f})" for d in top3)
        )

    _log.append("\n[Step 3 - Per-type selection] (after BGE-M3 reranking)")

    # Now apply per-type selection: for each document type, take its best k_per_type chunks
    # Group per-type reranked results by doc_uid
    selected_per_type: dict[str, list[dict]] = {}
    for doc_type in document_types:
        reranked_for_type = per_type_reranked.get(doc_type, [])

        # Group by doc_uid within this type
        by_doc: dict[str, dict] = {}
        for r in reranked_for_type:
            du = r["doc_uid"]
            if du not in by_doc:
                by_doc[du] = {"doc_uid": du, "chunks": [], "top_score": 0.0}
            by_doc[du]["chunks"].append(r)
            by_doc[du]["top_score"] = max(by_doc[du]["top_score"], r["score"])

        docs = sorted(by_doc.values(), key=lambda d: d["top_score"], reverse=True)

        # Per-type k: use override if set, else default
        k_this_type = (k_per_type_overrides or {}).get(doc_type, k_per_type)
        chunk_limit = chunk_limit_per_type if chunk_limit_per_type is not None else k_this_type * 3

        # STEP 4 LOG: per-type selection
        _log.append(
            f"  [Step 4 - Per-type selection] {doc_type}: k_per_type={k_this_type}, "
            f"chunk_limit={chunk_limit} | {len(docs)} docs compete: "
            + ", ".join(f"{d['doc_uid']}(top={d['top_score']:.4f}, {len(d['chunks'])} chunks)" for d in docs)
        )

        type_selected: list[dict] = []
        for doc_data in docs:
            if len(type_selected) >= chunk_limit:
                _log.append(
                    f"    DROPPED doc={doc_data['doc_uid']} "
                    f"(limit reached at {chunk_limit} chunks)"
                )
                break
            for chunk in sorted(doc_data["chunks"], key=lambda c: c["score"], reverse=True):
                if len(type_selected) >= chunk_limit:
                    break
                type_selected.append(chunk)

        # Log which docs were dropped
        kept_docs = {c["doc_uid"] for c in type_selected}
        for d in docs:
            if d["doc_uid"] not in kept_docs:
                _log.append(f"    DROPPED doc={d['doc_uid']} (top={d['top_score']:.4f}, {len(d['chunks'])} chunks)")

        selected_per_type[doc_type] = type_selected
        _log.append(
            f"  [Step 4 - Kept] {doc_type}: "
            f"{len(type_selected)} chunks from {len(kept_docs)} docs: "
            + ", ".join(f"{c['doc_uid']}({c['score']:.4f})" for c in type_selected[:3])
            + (" ..." if len(type_selected) > 3 else "")
        )

    # STEP 5: Merge + global sort
    all_selected: list[dict] = []
    for chunks in selected_per_type.values():
        all_selected.extend(chunks)
    all_selected_sorted = sorted(all_selected, key=lambda r: r["score"], reverse=True)
    _log.append(f"\n  [Step 5 - Merge] {len(all_selected_sorted)} chunks total from "
                f"{len({c['doc_uid'] for c in all_selected_sorted})} docs, sorted by BGE score")
    _log.append("    Top 5 after merge: "
                + ", ".join(f"{c['doc_uid']}({c['score']:.4f})" for c in all_selected_sorted[:5]))

    # STEP 6: Final per-doc selection (k=5 per doc)
    from src.retrieval.pipeline import _select_top_k_per_document

    final_selected = _select_top_k_per_document(
        ranked_results=all_selected_sorted,
        k=5,
        min_score=0.0,
    )
    _log.append(f"\n  [Step 6 - Final per-doc] {len(final_selected)} chunks from "
                f"{len({c['doc_uid'] for c in final_selected})} docs: "
                + ", ".join(f"{c['doc_uid']}({c['score']:.4f})" for c in final_selected))

    # Build step log for return
    step_log = list(_log)

    # Build per-type debug scores
    per_type_debug: dict[str, list[dict]] = {}
    for doc_type in document_types:
        reranked_for_type = per_type_reranked.get(doc_type, [])
        by_doc = {}
        for r in reranked_for_type:
            du = r["doc_uid"]
            if du not in by_doc:
                by_doc[du] = {"doc_uid": du, "top_score": r["score"], "n_chunks": 0}
            by_doc[du]["top_score"] = max(by_doc[du]["top_score"], r["score"])
            by_doc[du]["n_chunks"] += 1
        docs = sorted(by_doc.values(), key=lambda d: d["top_score"], reverse=True)
        per_type_debug[doc_type] = docs

    return {
        "status": "ok",
        "reranked": final_selected,
        "per_type_results": {
            dt: [c["doc_uid"] for c in sorted(chunks, key=lambda x: x["score"], reverse=True)]
            for dt, chunks in selected_per_type.items()
            if chunks
        },
        "per_type_debug": per_type_debug,
        "step_log": step_log,
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
            document_types=payload.get("document_types") or list(DOCUMENT_TYPES),
            mode=payload["mode"],
            dense_weight=payload["dense_weight"],
            sparse_weight=payload["sparse_weight"],
            multivector_weight=payload["multivector_weight"],
            score_normalization=payload["score_normalization"],
            top_k_per_type=payload.get("top_k_per_type", 500),
            k_per_type=payload.get("k_per_type", 10),
            k_per_type_overrides=payload.get("k_per_type_overrides"),
            chunk_limit_per_type=payload.get("chunk_limit_per_type"),
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
