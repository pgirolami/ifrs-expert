# Plan — persist query embeddings in `data/cache/`

## Goal

Avoid recomputing the same query embedding across separate CLI runs during evals.

## Proposed approach

1. Add a file-backed query embedding cache in `src/vector/store.py`.
2. Store cached vectors under `data/cache/query_embeddings/`.
3. Use a deterministic filename derived from:
   - a cache schema version
   - the embedding model name
   - the normalized query text
4. Recommended filename strategy:

```text
{safe_model_name}--{sha256(cache_key)}.npy
```

Where:
- `safe_model_name` is a filesystem-safe slug like `baai_bge-m3`
- `cache_key` is `v1:{model_name}:{normalized_query}`
- `normalized_query` should be conservative, e.g. `query.strip()`

Example:

```text
data/cache/query_embeddings/baai_bge-m3--8f3c1d...ab.npy
```

## Why this naming

- avoids invalid filename characters from raw queries
- keeps filenames short even for long questions
- prevents collisions across embedding models
- allows future invalidation by bumping the `v1` cache version
- avoids leaking the full question text into the filename

## Implementation sketch

1. Add helpers to:
   - build the cache directory path
   - normalize the query
   - build the hashed cache filename
   - load/save `.npy` embeddings
2. In `VectorStore._search_with_k()`, try loading the cached query embedding first.
3. On cache miss, compute the embedding, normalize it, save it, then search FAISS.
4. Keep the rest of the FAISS search path unchanged.

## Tests

Add unit tests in `tests/unit/test_vector_store.py` for:

- same model + same query => same cache filename
- different queries => different filenames
- cached embedding is reused on a second search
- search result structure is unchanged when cache hits

## Validation

Run:

```bash
uv run pytest tests/unit/test_vector_store.py
```
