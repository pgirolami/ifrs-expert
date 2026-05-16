"""Store command adapter for the ingestion pipeline."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from src.db import ChunkStore, ContentReferenceStore, DocumentStore, SectionStore, init_db
from src.extraction import HtmlExtractor
from src.ingestion import models as ingestion_models
from src.ingestion.models import StoreCommandOptions, StoreCommandResult, StoreDependencies
from src.ingestion.pipeline import IngestionPipeline
from src.vector.document_store import DocumentVectorStore, get_document_id_map_path, get_document_index_path
from src.vector.store import VectorStore
from src.vector.title_store import TitleVectorStore

STORE_SCOPES = ingestion_models.STORE_SCOPES

if TYPE_CHECKING:
    from src.interfaces import ExtractorProtocol


class StoreCommand:
    """Thin CLI adapter that runs the ingestion pipeline."""

    def __init__(
        self,
        source_path: Path,
        extractor: ExtractorProtocol,
        dependencies: StoreDependencies,
        options: StoreCommandOptions | None = None,
    ) -> None:
        """Initialize the command with explicit options."""
        normalized_source_path = Path(source_path)
        resolved_options = options or StoreCommandOptions()
        self._pipeline = IngestionPipeline(
            source_path=normalized_source_path,
            extractor=extractor,
            dependencies=dependencies,
            options=resolved_options,
        )

    def execute(self) -> str:
        """Execute the store command and return CLI-facing text."""
        return self.execute_result().to_stdout()

    def execute_result(self) -> StoreCommandResult:
        """Execute the store command and return a structured result."""
        return self._pipeline.execute_result()


def build_store_dependencies() -> StoreDependencies:
    """Build the production dependencies for StoreCommand."""
    return StoreDependencies(
        chunk_store=ChunkStore(),
        document_store=DocumentStore(),
        vector_store=VectorStore(),
        init_db_fn=init_db,
        section_store=SectionStore(),
        reference_store=ContentReferenceStore(),
        title_vector_store=TitleVectorStore(),
        document_vector_store=DocumentVectorStore(),
        document_vector_store_factory=lambda representation: DocumentVectorStore(
            index_path=get_document_index_path(representation),
            id_map_path=get_document_id_map_path(representation),
        ),
    )


def _default_extractor_for_source(source_path: Path) -> ExtractorProtocol:
    """Select the default extractor for a source path based on its file suffix."""
    suffix = source_path.suffix.lower()
    if suffix == ".html":
        return HtmlExtractor(sidecar_path=source_path.with_suffix(".json"))

    message = f"Unsupported source type: {source_path}"
    raise ValueError(message)


def create_store_command(
    source_path: Path | None = None,
    extractor: ExtractorProtocol | None = None,
    dependencies: StoreDependencies | None = None,
    options: StoreCommandOptions | None = None,
) -> StoreCommand:
    """Create StoreCommand with real dependencies by default."""
    if source_path is None:
        message = "create_store_command() requires source_path"
        raise TypeError(message)

    resolved_dependencies = dependencies or build_store_dependencies()
    resolved_extractor = extractor or _default_extractor_for_source(source_path)
    return StoreCommand(
        source_path=source_path,
        extractor=resolved_extractor,
        dependencies=resolved_dependencies,
        options=options,
    )
