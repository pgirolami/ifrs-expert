"""Tests for glossary-driven query embedding enrichment."""

from __future__ import annotations

from dataclasses import dataclass

from src.retrieval.query_embedding import GlossaryEntry, build_query_embedding_text


@dataclass(frozen=True)
class FakeGlossarySource:
    """Simple fake glossary source for unit tests."""

    entries: tuple[GlossaryEntry, ...]

    def load_entries(self) -> tuple[GlossaryEntry, ...]:
        """Return the configured glossary entries."""
        return self.entries


def test_build_query_embedding_text_deduplicates_terms_and_prefers_longest_matches() -> None:
    """The longest overlapping glossary entry should match first, with deduped English terms."""
    source = FakeGlossarySource(
        entries=(
            GlossaryEntry(
                fr="relation de couverture",
                en=("hedge relationship",),
            ),
            GlossaryEntry(
                fr="relation de couverture documentée",
                en=("documented hedge relationship", "hedge relationship"),
            ),
        ),
    )

    result = build_query_embedding_text(
        "Une relation de couverture documentée puis une relation de couverture.",
        glossary_source=source,
    )

    assert result.matched_french_terms == (
        "relation de couverture documentée",
        "relation de couverture",
    )
    assert result.appended_english_terms == (
        "documented hedge relationship",
        "hedge relationship",
    )
    assert result.embedding_text == (
        "Une relation de couverture documentée puis une relation de couverture.\n"
        "documented hedge relationship\n"
        "hedge relationship"
    )


def test_build_query_embedding_text_matches_case_insensitive_and_plural_forms() -> None:
    """Glossary lookup should ignore case and tolerate singular/plural word forms."""
    source = FakeGlossarySource(
        entries=(
            GlossaryEntry(
                fr="dividendes intragroupe",
                en=("intragroup dividends",),
            ),
        ),
    )

    result = build_query_embedding_text(
        "Les DIVIDENDEs intragroupe ont été comptabilisés.",
        glossary_source=source,
    )

    assert result.matched_french_terms == ("dividendes intragroupe",)
    assert result.appended_english_terms == ("intragroup dividends",)
    assert result.embedding_text.endswith("\nintragroup dividends")
