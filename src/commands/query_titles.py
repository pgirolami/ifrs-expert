"""Query titles command - search for similar section titles and expand to chunks."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.commands.constants import DEFAULT_VERBOSE
from src.db import ChunkStore, SectionStore, init_db
from src.retrieval.title_retrieval import TitleRetrievalConfig, TitleRetrievalHit, TitleRetrievalOptions, retrieve_title_hits
from src.vector.title_store import TitleVectorStore, get_title_index_path

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from src.interfaces import ReadChunkStoreProtocol, ReadSectionStoreProtocol, SearchTitleVectorStoreProtocol
    from src.policy import RetrievalPolicy

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class QueryTitlesConfig:
    """Configuration for QueryTitlesCommand."""

    title_vector_store: SearchTitleVectorStoreProtocol
    section_store: ReadSectionStoreProtocol
    chunk_store: ReadChunkStoreProtocol
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[], Path]


@dataclass(frozen=True)
class QueryTitlesOptions:
    """Options for the query-titles command."""

    policy: RetrievalPolicy
    verbose: bool = DEFAULT_VERBOSE


class QueryTitlesCommand:
    """Search for similar section titles and expand results to matching chunks."""

    def __init__(self, query: str, config: QueryTitlesConfig, options: QueryTitlesOptions) -> None:
        """Initialize the query-titles command."""
        self.query = query
        self._config = config
        self._options = options

    def execute(self) -> str:
        """Execute the title-search workflow and return formatted results."""
        if not self.query or not self.query.strip():
            return "Error: Query cannot be empty"

        retrieval_policy = self._options.policy
        error, hits = retrieve_title_hits(
            query=self.query,
            config=TitleRetrievalConfig(
                title_vector_store=self._config.title_vector_store,
                section_store=self._config.section_store,
                chunk_store=self._config.chunk_store,
                init_db_fn=self._config.init_db_fn,
                index_path_fn=self._config.index_path_fn,
            ),
            options=TitleRetrievalOptions(k=retrieval_policy.k, min_score=retrieval_policy.titles.min_score),
        )
        if error is not None:
            return error

        if self._options.verbose:
            return f"{self._options}\n{self._build_verbose_output(hits)}"
        return json.dumps(self._build_json_output(hits), indent=2, ensure_ascii=False)

    def _build_json_output(self, hits: list[TitleRetrievalHit]) -> list[dict[str, object]]:
        """Build the JSON output payload for title-query results."""
        return [
            {
                "doc_uid": hit.section.doc_uid,
                "section_id": hit.section.section_id,
                "section_lineage": hit.section.section_lineage,
                "title": hit.section.title,
                "score": round(hit.score, 4),
                "chunks": [
                    {
                        "id": chunk.id,
                        "chunk_number": chunk.chunk_number,
                        "chunk_id": chunk.chunk_id,
                        "containing_section_id": chunk.containing_section_id,
                        "containing_section_db_id": chunk.containing_section_db_id,
                        "text": chunk.text,
                    }
                    for chunk in hit.chunks
                ],
            }
            for hit in hits
        ]

    def _build_verbose_output(self, hits: list[TitleRetrievalHit]) -> str:
        """Build the verbose text output for title-query results."""
        lines: list[str] = []
        for hit in hits:
            lines.append(f"\n--- Score: {hit.score:.4f} ---")
            lines.append(f"Document: {hit.section.doc_uid}")
            lines.append(f"Section: {' > '.join(hit.section.section_lineage)}")
            lines.extend(f"- {chunk.chunk_number}: {chunk.text[:120]}" for chunk in hit.chunks)
        return "\n".join(lines)


def create_query_titles_command(query: str, options: QueryTitlesOptions) -> QueryTitlesCommand:
    """Create QueryTitlesCommand with real dependencies."""
    config = QueryTitlesConfig(
        title_vector_store=TitleVectorStore(),
        section_store=SectionStore(),
        chunk_store=ChunkStore(),
        init_db_fn=init_db,
        index_path_fn=get_title_index_path,
    )
    return QueryTitlesCommand(query=query, config=config, options=options)
