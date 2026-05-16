"""Ingest command - scan the capture root and route HTML sources through StoreCommand."""

from __future__ import annotations

import logging
from dataclasses import dataclass, replace
from pathlib import Path
from typing import TYPE_CHECKING, Protocol

from src.commands.store import (
    STORE_SCOPES,
    StoreCommandOptions,
    StoreCommandResult,
    StoreDependencies,
    build_store_dependencies,
    create_store_command,
)
from src.extraction import HtmlExtractor
from src.extraction.html import HtmlSidecar, HtmlValidationError

if TYPE_CHECKING:
    from src.interfaces import ExtractorProtocol

logger = logging.getLogger(__name__)


class StoreCommandFactory(Protocol):
    """Callable contract for ingest store command factories."""

    def __call__(self, source_path: Path, extractor: ExtractorProtocol, options: StoreCommandOptions | None = None) -> StoreCommandLike:
        """Create one store command for a source path."""
        ...


class CreateStoreCommandFn(Protocol):
    """Callable contract for the underlying store command constructor."""

    def __call__(
        self,
        source_path: Path,
        extractor: ExtractorProtocol,
        dependencies: StoreDependencies,
        options: StoreCommandOptions | None = None,
    ) -> StoreCommandLike:
        """Create one store command with explicit dependencies."""
        ...


@dataclass(frozen=True)
class CaptureDirectories:
    """Capture directory layout rooted under Downloads."""

    root: Path
    processed: Path
    failed: Path
    skipped: Path

    @classmethod
    def from_root(cls, root: Path) -> CaptureDirectories:
        """Build the standard capture directory layout from a root path."""
        return cls(
            root=root,
            processed=root / "processed",
            failed=root / "failed",
            skipped=root / "skipped",
        )

    def ensure_exists(self) -> None:
        """Create the capture directories when they do not already exist."""
        self.root.mkdir(parents=True, exist_ok=True)
        self.processed.mkdir(parents=True, exist_ok=True)
        self.failed.mkdir(parents=True, exist_ok=True)
        self.skipped.mkdir(parents=True, exist_ok=True)


@dataclass(frozen=True)
class IngestItem:
    """One source item to process from the capture root."""

    kind: str
    source_path: Path
    related_paths: tuple[Path, ...]
    reference: str
    extractor: ExtractorProtocol | None
    explicit_doc_uid: str | None = None


class StoreCommandLike(Protocol):
    """Structural typing helper for injected store commands."""

    def execute_result(self) -> StoreCommandResult:
        """Execute storage and return the structured result."""


class SharedDependenciesStoreCommandFactory:
    """Create store commands that reuse one dependency bundle across an ingest run."""

    def __init__(
        self,
        dependencies: StoreDependencies | None = None,
        create_store_command_fn: CreateStoreCommandFn = create_store_command,
    ) -> None:
        """Initialize the factory with shared dependencies and a command constructor."""
        self._dependencies = dependencies or build_store_dependencies()
        self._create_store_command_fn = create_store_command_fn

    def __call__(
        self,
        source_path: Path,
        extractor: ExtractorProtocol,
        options: StoreCommandOptions | None = None,
    ) -> StoreCommandLike:
        """Create one StoreCommand while reusing the shared dependencies."""
        return self._create_store_command_fn(
            source_path=source_path,
            extractor=extractor,
            dependencies=self._dependencies,
            options=options,
        )


class IngestCommand:
    """Scan the capture root directory and ingest discovered sources."""

    def __init__(
        self,
        capture_root: Path | None = None,
        store_command_factory: StoreCommandFactory | None = None,
        store_dependencies: StoreDependencies | None = None,
        store_options: StoreCommandOptions | None = None,
    ) -> None:
        """Initialize the ingest command with its capture root and store factory."""
        self._directories = CaptureDirectories.from_root(capture_root or (Path.home() / "Downloads" / "ifrs-expert"))
        self._store_options = store_options or StoreCommandOptions()
        self._store_command_factory = store_command_factory or SharedDependenciesStoreCommandFactory(dependencies=store_dependencies)

    def execute(self) -> str:
        """Run discovery, storage, and archiving."""
        scope_error = self._get_scope_error()
        if scope_error is not None:
            return f"Error: {scope_error}"

        self._directories.ensure_exists()
        logger.info(f"Starting scan in {self._directories.root} with scope={self._store_options.scope}, force_store={self._store_options.force_store}")

        items, failures = self._discover_items()
        results: list[str] = []
        imported_count = 0
        skipped_count = 0
        failed_count = len(failures)

        for failure in failures:
            self._archive_paths(paths=failure.related_paths, destination_dir=self._directories.failed)
            results.append(f"Failed: {failure.reference} ({failure.reason})")

        for item in items:
            if item.extractor is None:
                failed_count += 1
                self._archive_paths(paths=item.related_paths, destination_dir=self._directories.failed)
                results.append(f"Failed: {item.reference} (invalid extractor)")
                continue

            try:
                item_store_options = replace(self._store_options, explicit_doc_uid=item.explicit_doc_uid)
                store_command = self._store_command_factory(
                    source_path=item.source_path,
                    extractor=item.extractor,
                    options=item_store_options,
                )
                store_result = store_command.execute_result()
            except (OSError, RuntimeError, ValueError) as error:
                store_result = StoreCommandResult(
                    status="failed",
                    doc_uid=item.source_path.stem,
                    chunk_count=0,
                    embedding_count=0,
                    reason=str(error),
                )

            if store_result.status == "stored":
                imported_count += 1
                self._archive_paths(paths=item.related_paths, destination_dir=self._directories.processed)
                results.append(f"Imported: {item.reference} -> doc_uid={store_result.doc_uid} ({store_result.chunk_count} chunks)")
                continue

            if store_result.status == "skipped":
                skipped_count += 1
                self._archive_paths(paths=item.related_paths, destination_dir=self._directories.skipped)
                reason = store_result.reason or "unchanged content"
                results.append(f"Skipped: {item.reference} ({reason})")
                continue

            failed_count += 1
            self._archive_paths(paths=item.related_paths, destination_dir=self._directories.failed)
            reason = store_result.reason or "unknown error"
            results.append(f"Failed: {item.reference} ({reason})")

        processed_count = imported_count + skipped_count + failed_count
        summary_lines = [f"Processed {processed_count} item(s): {imported_count} imported, {skipped_count} skipped, {failed_count} failed"]
        summary_lines.extend(results)
        return "\n".join(summary_lines)

    def _discover_items(self) -> tuple[list[IngestItem], list[_DiscoveryFailure]]:
        html_paths = sorted(self._directories.root.glob("*.html"))
        json_paths = sorted(self._directories.root.glob("*.json"))

        logger.info(f"Found {len(html_paths)} HTML file(s) and {len(json_paths)} sidecar file(s)")

        items: list[IngestItem] = []
        failures: list[_DiscoveryFailure] = []

        html_by_stem = {path.stem: path for path in html_paths}
        json_by_stem = {path.stem: path for path in json_paths}

        all_html_stems = sorted(set(html_by_stem) | set(json_by_stem))
        for stem in all_html_stems:
            html_path = html_by_stem.get(stem)
            json_path = json_by_stem.get(stem)
            if html_path is None and json_path is not None:
                failures.append(
                    _DiscoveryFailure(
                        related_paths=(json_path,),
                        reference=str(json_path),
                        reason="missing HTML file",
                    )
                )
                continue
            if json_path is None and html_path is not None:
                failures.append(
                    _DiscoveryFailure(
                        related_paths=(html_path,),
                        reference=str(html_path),
                        reason="missing sidecar JSON",
                    )
                )
                continue
            if html_path is None or json_path is None:
                continue

            try:
                sidecar = HtmlSidecar.from_path(json_path)
            except HtmlValidationError as error:
                failures.append(
                    _DiscoveryFailure(
                        related_paths=(html_path, json_path),
                        reference=str(html_path),
                        reason=str(error),
                    )
                )
                continue

            items.append(
                IngestItem(
                    kind="html",
                    source_path=html_path,
                    related_paths=(html_path, json_path),
                    reference=sidecar.canonical_url,
                    extractor=HtmlExtractor(sidecar_path=json_path),
                )
            )

        items.sort(key=lambda item: item.source_path.name)
        return items, failures

    def _get_scope_error(self) -> str | None:
        if self._store_options.scope in STORE_SCOPES:
            return None
        supported_scopes = ", ".join(STORE_SCOPES)
        return f"scope must be one of {supported_scopes}"

    def _archive_paths(self, paths: tuple[Path, ...], destination_dir: Path) -> None:
        for path in paths:
            if not path.exists():
                continue
            destination = destination_dir / path.name
            suffix_count = 1
            while destination.exists():
                destination = destination_dir / f"{path.stem}--{suffix_count}{path.suffix}"
                suffix_count += 1
            path.rename(destination)
            logger.info(f"Moved {path} to {destination}")


@dataclass(frozen=True)
class _DiscoveryFailure:
    """Represents a source that failed before StoreCommand execution."""

    related_paths: tuple[Path, ...]
    reference: str
    reason: str
