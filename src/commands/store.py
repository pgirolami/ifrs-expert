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
        **legacy_kwargs: object,
    ) -> None:
        """Initialize the command and preserve legacy keyword options."""
        resolved_options = _resolve_store_command_options(options=options, legacy_kwargs=legacy_kwargs)
        if legacy_kwargs:
            unexpected_keys = ", ".join(sorted(legacy_kwargs))
            message = f"Unexpected keyword arguments: {unexpected_keys}"
            raise TypeError(message)
        normalized_source_path = Path(source_path)
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


def _resolve_store_command_options(
    options: StoreCommandOptions | None,
    legacy_kwargs: dict[str, object],
) -> StoreCommandOptions:
    resolved_explicit_doc_uid = options.explicit_doc_uid if options is not None else None
    resolved_scope = options.scope if options is not None else "all"
    resolved_force_store = options.force_store if options is not None else False

    resolved_explicit_doc_uid = _pop_legacy_optional_string(legacy_kwargs, "doc_uid", resolved_explicit_doc_uid)
    resolved_explicit_doc_uid = _pop_legacy_optional_string(
        legacy_kwargs,
        "explicit_doc_uid",
        resolved_explicit_doc_uid,
    )
    resolved_scope = _pop_legacy_string(legacy_kwargs, "scope", resolved_scope)
    resolved_force_store = _pop_legacy_bool(legacy_kwargs, "force_store", resolved_force_store)
    resolved_force_store = _pop_legacy_bool(legacy_kwargs, "force_restore", resolved_force_store)

    return StoreCommandOptions(
        explicit_doc_uid=resolved_explicit_doc_uid,
        scope=resolved_scope,
        force_store=resolved_force_store,
    )


def _pop_legacy_optional_string(
    legacy_kwargs: dict[str, object],
    key: str,
    current_value: str | None,
) -> str | None:
    if key not in legacy_kwargs:
        return current_value
    value = legacy_kwargs.pop(key)
    if value is None:
        return None
    if not isinstance(value, str):
        message = f"{key} must be a string or None, got {type(value).__name__}"
        raise TypeError(message)
    return value


def _pop_legacy_string(
    legacy_kwargs: dict[str, object],
    key: str,
    current_value: str,
) -> str:
    if key not in legacy_kwargs:
        return current_value
    value = legacy_kwargs.pop(key)
    if not isinstance(value, str):
        message = f"{key} must be a string, got {type(value).__name__}"
        raise TypeError(message)
    return value


def _pop_legacy_bool(
    legacy_kwargs: dict[str, object],
    key: str,
    current_value: object,
) -> bool:
    if key not in legacy_kwargs:
        return bool(current_value)
    value = legacy_kwargs.pop(key)
    if not isinstance(value, bool):
        message = f"{key} must be a bool, got {type(value).__name__}"
        raise TypeError(message)
    return value


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
    **legacy_kwargs: object,
) -> StoreCommand:
    """Create StoreCommand with real dependencies by default."""
    resolved_options = _resolve_store_command_options(options=options, legacy_kwargs=legacy_kwargs)
    if legacy_kwargs:
        unexpected_keys = ", ".join(sorted(legacy_kwargs))
        message = f"Unexpected keyword arguments: {unexpected_keys}"
        raise TypeError(message)
    if source_path is None:
        message = "create_store_command() requires source_path"
        raise TypeError(message)

    resolved_dependencies = dependencies or build_store_dependencies()
    resolved_extractor = extractor or _default_extractor_for_source(source_path)
    return StoreCommand(
        source_path=source_path,
        extractor=resolved_extractor,
        dependencies=resolved_dependencies,
        options=resolved_options,
    )
