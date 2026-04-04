"""Ingest command - scan the inbox and route HTML/PDF sources through StoreCommand."""

from __future__ import annotations

import logging
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from src.commands.store import StoreCommandResult, create_store_command
from src.extraction import HtmlExtractor, PdfExtractor
from src.extraction.html import HtmlSidecar, HtmlValidationError
from src.interfaces import ExtractorProtocol

logger = logging.getLogger(__name__)

StoreCommandFactory = Callable[[Path, ExtractorProtocol, str | None], object]


@dataclass(frozen=True)
class CaptureDirectories:
    """Capture directory layout rooted under Downloads."""

    root: Path
    inbox: Path
    processed: Path
    failed: Path
    skipped: Path

    @classmethod
    def from_root(cls, root: Path) -> "CaptureDirectories":
        return cls(
            root=root,
            inbox=root / "inbox",
            processed=root / "processed",
            failed=root / "failed",
            skipped=root / "skipped",
        )

    def ensure_exists(self) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        self.inbox.mkdir(parents=True, exist_ok=True)
        self.processed.mkdir(parents=True, exist_ok=True)
        self.failed.mkdir(parents=True, exist_ok=True)
        self.skipped.mkdir(parents=True, exist_ok=True)


@dataclass(frozen=True)
class IngestItem:
    """One source item to process from the inbox."""

    kind: str
    source_path: Path
    related_paths: tuple[Path, ...]
    reference: str
    extractor: ExtractorProtocol | None
    explicit_doc_uid: str | None = None


class StoreCommandLike:
    """Structural typing helper for injected store commands."""

    def execute_result(self) -> StoreCommandResult:
        raise NotImplementedError


class IngestCommand:
    """Scan the fixed inbox directory and ingest discovered sources."""

    def __init__(
        self,
        capture_root: Path | None = None,
        store_command_factory: StoreCommandFactory | None = None,
    ) -> None:
        self._directories = CaptureDirectories.from_root(
            capture_root or (Path.home() / "Downloads" / "ifrs-expert")
        )
        self._store_command_factory = store_command_factory or self._default_store_command_factory

    def execute(self) -> str:
        """Run inbox discovery, storage, and archiving."""
        self._directories.ensure_exists()
        logger.info(f"Starting inbox scan in {self._directories.inbox}")

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
                store_command = self._store_command_factory(
                    item.source_path,
                    item.extractor,
                    item.explicit_doc_uid,
                )
                store_result = store_command.execute_result()
            except Exception as error:
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
                results.append(
                    f"Imported: {item.reference} -> doc_uid={store_result.doc_uid} ({store_result.chunk_count} chunks)"
                )
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
        summary_lines = [
            f"Processed {processed_count} item(s): {imported_count} imported, {skipped_count} skipped, {failed_count} failed"
        ]
        summary_lines.extend(results)
        return "\n".join(summary_lines)

    def _discover_items(self) -> tuple[list[IngestItem], list[_DiscoveryFailure]]:
        html_paths = sorted(self._directories.inbox.glob("*.html"))
        json_paths = sorted(self._directories.inbox.glob("*.json"))
        pdf_paths = sorted(self._directories.inbox.glob("*.pdf"))

        logger.info(f"Found {len(html_paths)} HTML file(s), {len(json_paths)} sidecar file(s), and {len(pdf_paths)} PDF file(s)")

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

        for pdf_path in pdf_paths:
            if not pdf_path.is_file():
                failures.append(
                    _DiscoveryFailure(
                        related_paths=(pdf_path,),
                        reference=str(pdf_path),
                        reason="PDF file is not readable",
                    )
                )
                continue
            try:
                pdf_path.open("rb").close()
            except OSError:
                failures.append(
                    _DiscoveryFailure(
                        related_paths=(pdf_path,),
                        reference=str(pdf_path),
                        reason="PDF file is not readable",
                    )
                )
                continue

            items.append(
                IngestItem(
                    kind="pdf",
                    source_path=pdf_path,
                    related_paths=(pdf_path,),
                    reference=str(pdf_path),
                    extractor=PdfExtractor(),
                )
            )

        items.sort(key=lambda item: item.source_path.name)
        return items, failures

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

    def _default_store_command_factory(
        self,
        source_path: Path,
        extractor: ExtractorProtocol,
        explicit_doc_uid: str | None,
    ) -> StoreCommandLike:
        return create_store_command(
            source_path=source_path,
            extractor=extractor,
            doc_uid=explicit_doc_uid,
        )


@dataclass(frozen=True)
class _DiscoveryFailure:
    """Represents a source that failed before StoreCommand execution."""

    related_paths: tuple[Path, ...]
    reference: str
    reason: str
