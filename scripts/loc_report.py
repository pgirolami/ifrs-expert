"""Report line counts for simplification target files."""

from pathlib import Path

TARGET_FILES = (
    Path("src/commands/answer.py"),
    Path("src/retrieval/pipeline.py"),
    Path("src/retrieval/document_profile_builder.py"),
    Path("src/commands/store.py"),
    Path("tests/unit/test_answer_command.py"),
    Path("tests/unit/test_store_command.py"),
)


class LocReporter:
    """Print simple LOC metrics for tracked simplification targets."""

    def __init__(self, target_files: tuple[Path, ...] = TARGET_FILES) -> None:
        self._target_files = target_files

    def run(self) -> str:
        rows = ["file,loc"]
        for path in self._target_files:
            line_count = self._count_lines(path)
            rows.append(f"{path},{line_count}")
        return "\n".join(rows)

    def _count_lines(self, path: Path) -> int:
        with path.open("r", encoding="utf-8") as file_handle:
            return sum(1 for _ in file_handle)


if __name__ == "__main__":
    print(LocReporter().run())
