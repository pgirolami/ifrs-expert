"""Shared vector and embedding text limits."""

MAX_TOKENS_FOR_EMBEDDING = 8000  # Approximate max tokens for the BAAI/bge-m3 embedding model
MAX_EMBEDDING_TEXT_CHARS = 3 * MAX_TOKENS_FOR_EMBEDDING
