# Experiment 53
## Goal

Evaluate retrieval & answer on Q9 for the first time (= same as experiment 50 but for Q9)

- Diagnostic indexes:
  - [approach detection](./diagnostics/approach_detection_index.md)

## Results

### eval-retrieval run
- The evals all pass
- Diagnostics show that target document & chunk recall is 100% on Q9.0

### eval-answer

#### 1st run
A spurious approach was returned in both runs (but not the same label)
  ```    {
      "id": "approach_3",
      "label": "Sales-based or usage-based royalty recognition",
      "normalized_label": "sales_based_or_usage_based_royalty_recognition",
      "rationale_for_inclusion": "IFRS 15 provides a distinct recognition model for sales-based or usage-based royalties promised in exchange for a licence  intellectual property."
    }
  ```

This is not a top-level approach, it is an overlay to the existing approaches so it shouldn't be there. We changed the prompt to better exclude them.

#### 2nd run
After the change, neither of the two runs surfaced the spurious approach. However, the first run still produces overlapping approaches:
```
    {
      "id": "approach_1",
      "label": "Right to access intellectual property",
      "normalized_label": "right_to_access_intellectual_property",
      "rationale_for_inclusion": "IFRS 15 treats a licence as over time when the nature of the promise is to provide access to intellectual property throughout the licence period."
    },
    {
      "id": "approach_2",
      "label": "Right to use intellectual property",
      "normalized_label": "right_to_use_intellectual_property",
      "rationale_for_inclusion": "IFRS 15 treats a licence as at a point in time when the nature of the promise is to provide the right to use intellectual property as it exists when granted."
    },
    {
      "id": "approach_3",
      "label": "Revenue recognised over time",
      "normalized_label": "revenue_recognised_over_time",
      "rationale_for_inclusion": "If a licence is not distinct and is part of a broader performance obligation, IFRS 15 requires the combined obligation to be assessed under the general over-time model."
    },
    {
      "id": "approach_4",
      "label": "Revenue recognised at a point in time",
      "normalized_label": "revenue_recognised_at_a_point_in_time",
      "rationale_for_inclusion": "If a licence is not distinct and the combined performance obligation does not meet the over-time criteria, IFRS 15 requires point-in-time recognition."
    }
```

1. These are mapped from this treatment family:
   ```
    {
      "family": "Non-distinct licence combined with other goods or services and assessed under the general timing model",
      "authority_basis": [
        {
          "document": "ifrs15",
          "references": ["B54", "B55", "31", "32", "35", "38"]
        }
      ],
      "mapped_approaches": ["revenue_recognised_over_time", "revenue_recognised_at_a_point_in_time"]
    }
   ```
   but it shouldn't be a treatment family because we should assume the question is about a distinct license and the non-distinct case is a caveat.
  - the prompt was extended with lots of branching instructions to help it seperate these cases from approaches

2. The labeling difference (ex: "right to access intellectual property" vs "revenue recognised over time") looks like in one case the LLM chose the accounting model and in the other the recognition outcome.
  - the prompt was extended to tell the LLM not to emit an outcome label instead of a model label

#### 2nd run
The approach identification seems fixed, both runs only output 2 approaches now:
```
    {
      "id": "approach_1",
      "label": "Right to access intellectual property",
      "normalized_label": "right_to_access_intellectual_property",
      "rationale_for_inclusion": "IFRS 15 identifies this as a distinct licence model when the customer receives access to intellectual property as it exists throughout the licence period."
    },
    {
      "id": "approach_2",
      "label": "Right to use intellectual property",
      "normalized_label": "right_to_use_intellectual_property",
      "rationale_for_inclusion": "IFRS 15 identifies this as a distinct licence model when the customer receives a right to use the intellectual property as it exists when the licence is granted."
    }
```

One run still identified a specific treatment family for licenses combined with other goods or services but did not surface it as a top-level approach, as we wanted.

The answer to prompt B in both runs is correct.

## Non-regression
An `answer` eval was run on each of the worst performing questions of Q1, Q2, Q3:
- Q1 gave the correct answer even though the eval failed because the `net_investment_hedge` label became `hedge_of_a_net_investment_in_a_foreign_operation`
- Q2 also gave the correct answer. The family.yaml file was expanded to also check the approach labels now and their recommendation
- Q3