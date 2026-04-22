"""Query embedding enrichment helpers for glossary-driven retrieval."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Protocol

import yaml

logger = logging.getLogger(__name__)

GLOSSARY_PATH = Path(__file__).parent.parent.parent / "config" / "en-fr-glossary.yaml"


@dataclass(frozen=True)
class GlossaryEntry:
    """One French-to-English glossary entry."""

    fr: str
    en: tuple[str, ...]


@dataclass(frozen=True)
class QueryEmbeddingText:
    """Embedding text produced from a question plus glossary expansions."""

    original_query: str
    embedding_text: str
    matched_french_terms: tuple[str, ...]
    appended_english_terms: tuple[str, ...]


class GlossarySourceProtocol(Protocol):
    """Protocol for loading glossary entries."""

    def load_entries(self) -> tuple[GlossaryEntry, ...]:
        """Load glossary entries."""


class FileGlossarySource:
    """Load glossary entries from the repository file."""

    def load_entries(self) -> tuple[GlossaryEntry, ...]:
        """Load the configured French-to-English glossary once."""
        return _load_glossary_entries_from_file()


@lru_cache(maxsize=1)
def _load_glossary_entries_from_file() -> tuple[GlossaryEntry, ...]:
    """Load the configured French-to-English glossary from disk."""
    if not GLOSSARY_PATH.exists():
        logger.warning(f"Glossary file not found at {GLOSSARY_PATH}; using raw query text for embeddings")
        return ()

    raw_data = yaml.safe_load(GLOSSARY_PATH.read_text(encoding="utf-8"))
    if not isinstance(raw_data, dict):
        logger.warning(f"Glossary file at {GLOSSARY_PATH} did not contain a mapping; using raw query text for embeddings")
        return ()

    raw_entries = raw_data.get("question_glossary")
    if not isinstance(raw_entries, list):
        logger.warning(f"Glossary file at {GLOSSARY_PATH} did not contain question_glossary entries; using raw query text for embeddings")
        return ()

    entries: list[GlossaryEntry] = []
    for raw_entry in raw_entries:
        if not isinstance(raw_entry, dict):
            continue
        fr_value = raw_entry.get("fr")
        en_values = raw_entry.get("en")
        if not isinstance(fr_value, str) or not isinstance(en_values, list):
            continue

        fr = fr_value.strip()
        english_terms = tuple(term.strip() for term in en_values if isinstance(term, str) and term.strip())
        if not fr or not english_terms:
            continue
        entries.append(GlossaryEntry(fr=fr, en=english_terms))

    logger.info(f"Loaded {len(entries)} query glossary entrie(s) from {GLOSSARY_PATH}")
    return tuple(entries)


FILE_GLOSSARY_SOURCE = FileGlossarySource()


def build_query_embedding_text(query: str, glossary_source: GlossarySourceProtocol | None = None) -> QueryEmbeddingText:
    """Append glossary-driven English terms to a query for embedding only."""
    source = glossary_source or FILE_GLOSSARY_SOURCE
    remaining_text = _normalize_whitespace(query)
    matched_french_terms: list[str] = []
    appended_english_terms: list[str] = []
    seen_english_terms: set[str] = set()
    ordered_entries = _ordered_glossary_entries(source)

    while True:
        match = _find_best_match(remaining_text, ordered_entries)
        if match is None:
            break

        entry, matched_span, matched_text = match
        matched_french_terms.append(entry.fr)
        logger.info(f"Glossary match fr='{entry.fr}' matched_text='{matched_text}' span={matched_span}; remaining_before='{remaining_text}'")
        remaining_text = _remove_matched_span(remaining_text, matched_span)
        logger.info(f"Remaining text after glossary removal: '{remaining_text}'")

        for english_term in entry.en:
            if english_term in seen_english_terms:
                continue
            seen_english_terms.add(english_term)
            appended_english_terms.append(english_term)

    embedding_text = f"{query.rstrip()}\n" + "\n".join(appended_english_terms) if appended_english_terms else query

    logger.info(f"Glossary query enrichment matched_french_terms={matched_french_terms}; appended_english_terms={appended_english_terms}")
    logger.info(f"Query text being embedded:\n{embedding_text}")
    return QueryEmbeddingText(
        original_query=query,
        embedding_text=embedding_text,
        matched_french_terms=tuple(matched_french_terms),
        appended_english_terms=tuple(appended_english_terms),
    )


def _normalize_whitespace(text: str) -> str:
    """Collapse repeated whitespace to make phrase matching robust to line breaks."""
    return " ".join(text.split())


def _ordered_glossary_entries(glossary_source: GlossarySourceProtocol) -> tuple[GlossaryEntry, ...]:
    """Return glossary entries sorted to prefer longest phrases first."""
    entries = glossary_source.load_entries()
    return tuple(
        sorted(
            entries,
            key=lambda entry: (
                -len(_normalize_whitespace(entry.fr).split()),
                -len(_normalize_whitespace(entry.fr)),
            ),
        )
    )


def _find_best_match(
    text: str,
    entries: tuple[GlossaryEntry, ...],
) -> tuple[GlossaryEntry, tuple[int, int], str] | None:
    """Find the longest glossary match in the current text."""
    best_match: tuple[GlossaryEntry, tuple[int, int], str] | None = None
    best_word_count = -1
    best_phrase_length = -1

    for entry in entries:
        phrase = _normalize_whitespace(entry.fr)
        parts = [_word_pattern(part) for part in phrase.split(" ") if part]
        if not parts:
            continue
        pattern = r"\b" + r"\s+".join(parts) + r"\b"
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match is None:
            continue

        word_count = len(phrase.split())
        phrase_length = len(phrase)
        if word_count > best_word_count or (word_count == best_word_count and phrase_length > best_phrase_length):
            best_word_count = word_count
            best_phrase_length = phrase_length
            best_match = (entry, match.span(), match.group(0))

    return best_match


def _remove_matched_span(text: str, span: tuple[int, int]) -> str:
    """Remove one matched span and normalize whitespace again."""
    start, end = span
    remaining = f"{text[:start]} {text[end:]}"
    return _normalize_whitespace(remaining)


def _word_pattern(word: str) -> str:
    """Build a singular/plural-tolerant regex fragment for one word."""
    if not word or not word[-1].isalpha():
        return re.escape(word)

    singular_word = word[:-1] if len(word) > 1 and word.lower().endswith(("s", "x")) else word
    return re.escape(singular_word) + r"(?:s|x)?"
