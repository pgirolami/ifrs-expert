"""Run stability scoring on experiment outputs."""

import json
import sys
from pathlib import Path
from dataclasses import dataclass

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from stability_scorer import compute_stability_score


@dataclass
class QuestionScore:
    question_id: str
    runs: int
    stability_score: float
    stability_score_loose: float
    approach_stability: float
    approach_stability_canonical: float
    applicability_stability: float
    applicability_stability_loose: float
    recommendation_stability: float
    recommendation_stability_loose: float
    structural_valid: bool
    rec_dist: dict


def load_b_response(run_dir: Path) -> dict | None:
    """Load B-response.md file, parsing JSON from markdown."""
    b_response_path = run_dir / "B-response.md"
    if not b_response_path.exists():
        return None
    
    content = b_response_path.read_text()
    content = content.strip()
    if content.startswith("```json"):
        content = content[7:]
    if content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    content = content.strip()
    
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return None


def main():
    exp_dir = Path("experiments")
    exp_07_dirs = sorted([d for d in exp_dir.iterdir() if d.is_dir() and d.name.startswith("07")])
    
    if not exp_07_dirs:
        print("No experiment directories found starting with '07'")
        return
    
    all_results: list[QuestionScore] = []
    
    for exp_dir_item in exp_07_dirs:
        print(f"\n{'='*80}")
        print(f"EXPERIMENT: {exp_dir_item.name}")
        print(f"{'='*80}\n")
        
        run_dirs = sorted([d for d in exp_dir_item.iterdir() if d.is_dir() and "__run" in d.name])
        
        runs_by_question: dict[str, list[Path]] = {}
        for run_dir in run_dirs:
            parts = run_dir.name.split("__run")
            if len(parts) >= 2:
                question_id = parts[0]
                if question_id not in runs_by_question:
                    runs_by_question[question_id] = []
                runs_by_question[question_id].append(run_dir)
        
        for question_id, run_paths in sorted(runs_by_question.items()):
            runs = []
            for run_path in sorted(run_paths):
                b_response = load_b_response(run_path)
                if b_response:
                    runs.append(b_response)
            
            if len(runs) < 2:
                print(f"  [SKIP] {question_id}: only {len(runs)} run(s)")
                continue
            
            result = compute_stability_score(runs)
            
            all_results.append(QuestionScore(
                question_id=question_id,
                runs=len(runs),
                stability_score=result.stability_score,
                stability_score_loose=result.stability_score_loose,
                approach_stability=result.approach_set_stability,
                applicability_stability=result.applicability_stability,
                applicability_stability_loose=result.applicability_stability_loose,
                recommendation_stability=result.recommendation_stability,
                recommendation_stability_loose=result.recommendation_stability_loose,
                structural_valid=result.diagnostics.structural_validity_flag,
                rec_dist=result.diagnostics.recommendation_distribution,
            ))
            
            print(f"  {question_id}: Score={result.stability_score:.1f}, Score(loose)={result.stability_score_loose:.1f}  (runs={len(runs)}, valid={result.diagnostics.structural_validity_flag})")
            print(f"    Approach={result.approach_set_stability:.2f}, Applicability={result.applicability_stability:.2f}, Rec={result.recommendation_stability:.2f}")
    
    # Summary table
    print(f"\n{'='*80}")
    print("SUMMARY TABLE")
    print(f"{'='*80}")
    print(f"{'Question':<35} {'Runs':>5} {'Score':>7} {'Score(loose)':>12} {'Valid':>5}")
    print(f"{'-'*35} {'-'*5} {'-'*7} {'-'*12} {'-'*5}")
    
    total_score = 0
    total_score_loose = 0
    count = 0
    for r in sorted(all_results, key=lambda x: x.stability_score, reverse=True):
        print(f"{r.question_id:<35} {r.runs:>5} {r.stability_score:>7.1f} {r.stability_score_loose:>12.1f} {str(r.structural_valid):>5}")
        total_score += r.stability_score
        total_score_loose += r.stability_score_loose
        count += 1
    
    if count > 0:
        print(f"{'-'*35} {'-'*5} {'-'*7} {'-'*12} {'-'*5}")
        print(f"{'AVERAGE':<35} {'':>5} {total_score/count:>7.1f} {total_score_loose/count:>12.1f} {'':>5}")


if __name__ == "__main__":
    main()