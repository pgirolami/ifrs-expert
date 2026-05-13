"""Report LOC for codebase simplification target files."""

from pathlib import Path

TARGET_FILES = [
    Path("src/commands/answer.py"),
    Path("src/retrieval/pipeline.py"),
    Path("src/retrieval/document_profile_builder.py"),
    Path("src/commands/store.py"),
    Path("tests/unit/test_answer_command.py"),
    Path("tests/unit/test_store_command.py"),
]


def count_lines(path: Path) -> int:
    """Return the number of text lines in path."""
    return len(path.read_text(encoding="utf-8").splitlines())


def main() -> None:
    """Print a markdown file-size table for simplification tracking."""
    print("| File | LOC |")
    print("| --- | ---: |")
    total = 0
    for path in TARGET_FILES:
        line_count = count_lines(path)
        total += line_count
        print(f"| `{path}` | {line_count} |")
    print(f"| **Total** | **{total}** |")


if __name__ == "__main__":
    main()
