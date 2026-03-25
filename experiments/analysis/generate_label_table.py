"""Generate label frequency table for experiments."""

import json
import sys
from collections import defaultdict
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.stability_scorer import extract_normalized_labels


def load_b_response(run_dir: Path) -> dict | None:
    """Load B-response.md file, parsing JSON from markdown."""
    b_response_path = run_dir / "B-response.md"
    if not b_response_path.exists():
        return None

    content = b_response_path.read_text()
    content = content.strip()
    content = content.removeprefix("```json")
    content = content.removeprefix("```")
    content = content.removesuffix("```")
    content = content.strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return None


def process_experiment(exp_dir: Path) -> dict[str, dict[str, int]]:
    """Process one experiment directory and return label counts per question."""
    run_dirs = sorted([d for d in exp_dir.iterdir() if d.is_dir() and "__run" in d.name])

    # Group runs by question
    runs_by_question: dict[str, list[Path]] = {}
    for run_dir in run_dirs:
        parts = run_dir.name.split("__run")
        if len(parts) >= 2:
            question_id = parts[0]
            if question_id not in runs_by_question:
                runs_by_question[question_id] = []
            runs_by_question[question_id].append(run_dir)

    # Count labels per question
    label_counts: dict[str, dict[str, int]] = {}  # question -> label -> count

    for question_id, run_paths in sorted(runs_by_question.items()):
        label_counts[question_id] = defaultdict(int)
        for run_path in sorted(run_paths):
            b_response = load_b_response(run_path)
            if b_response:
                labels = extract_normalized_labels(b_response)
                for label in labels:
                    label_counts[question_id][label] += 1

    return {q: dict(counts) for q, counts in label_counts.items()}


def format_table(exp_name: str, label_counts: dict[str, dict[str, int]]) -> str:
    """Format the label counts as a markdown table."""
    # Collect all labels and all questions
    all_labels: set[str] = set()
    all_questions: list[str] = []
    
    for question_id, counts in label_counts.items():
        all_questions.append(question_id)
        all_labels.update(counts.keys())
    
    # Sort questions properly (numeric sort)
    def question_sort_key(q: str) -> tuple[int, float]:
        # Extract numeric part: Q1.1 -> (1, 1), Q1.10 -> (1, 10), Q1.2 -> (1, 2)
        import re
        match = re.match(r"Q(\d+)\.(\d+)", q)
        if match:
            return (int(match.group(1)), int(match.group(2)))
        return (0, 0)
    
    all_questions.sort(key=question_sort_key)
    all_labels = sorted(all_labels)
    
    if not all_labels or not all_questions:
        return f"No data for {exp_name}"
    
    # Build header - short question IDs
    short_questions = [q.replace("_k=5_e=5_min-score=0.5", "") for q in all_questions]
    header = "| normalized_label | " + " | ".join(short_questions) + " | Total |\n"
    separator = "|------------------|" + "|".join(["---" for _ in all_questions]) + "|------|\n"
    
    # Build rows
    rows = []
    for label in all_labels:
        row = f"| {label} |"
        total = 0
        for question_id in all_questions:
            count = label_counts[question_id].get(label, 0)
            row += f" {count} |"
            total += count
        row += f" {total} |"
        rows.append(row)
    
    return f"### {exp_name}\n\n{header}{separator}" + "\n".join(rows)


def main():
    experiments_dir = Path("experiments")
    
    # Process experiments 07 and 08
    exp_07_dir = experiments_dir / "07_betterbetter_2_stage_processing_json_output"
    exp_08_dir = experiments_dir / "08_treatment_only_approaches"
    
    print("# Label Frequency by Question\n")
    
    if exp_07_dir.exists():
        label_counts_07 = process_experiment(exp_07_dir)
        print(format_table("Experiment 07", label_counts_07))
        print()
    
    if exp_08_dir.exists():
        label_counts_08 = process_experiment(exp_08_dir)
        print(format_table("Experiment 08", label_counts_08))
        print()


if __name__ == "__main__":
    main()