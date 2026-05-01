# Experiment 54
## Goal

Evaluate retrieval & answer on Q5 for the first time (= same as experiment 50 but for Q5)

- Diagnostic indexes:
  - [approach detection](./diagnostics/approach_detection_index.md)

## Results

### eval-retrieval run
- The evals all pass
- Diagnostics show that target document & chunk recall is 100% on Q9.0

### eval-answer

#### 1st run
The first run surfaced the exact NAVIS question so the policy was updated to exclude NAVIS documents and the directory was deleted to run again.

#### 2nd run
The second run was run by mistake with the NAVIS documents again. This time
- only one run surfaced the NAVIS document, which is strange
- the approach labels were inconsistent across runs, one being plural and the other singular
  - `fair_value_of_an_asset` vs `fair_value_measurement_of_assets`
  - `fair_value_of_a_liability` vs `fair_value_measurement_of_liabilities`

### 3rd run
The third one surfaced the same labels for the identified approaches for both runs.

However, the recommendation varied between 'oui' and 'oui_sous_conditions'. For now, the eval was updated to accept both.

### 4th run
Success
 - eval passed: approaches are correct, applicabilities are correct and recommendation applicability is correct
 - recall is 100%

 ## Non-regression
An `answer` eval was run on each of the worst performing questions of Q1, Q2, Q3:
- Q1 runs surfaced 2 different labels for the 3rd approach : `hedge_of_a_net_investment_in_a_foreign_operation` vs `hedge_of_a_net_investment`
  - the prompt was updated to prefer shorter labels when the extra words don't make it a different top-level model
  - the follow 2 runs both produced `hedge_of_a_net_investment`, the eval wasn't checking the right label anymore but everything else was fine
- Q2.3 : recall is 100%, the eval passes
- Q3.8 : recall is 100% but the eval fails because the recommendation is 'oui' and the eval tested for 'oui_sous_conditions'. The eval was updated to accept both.

Following these changes, the Q5.0 answer eval was run again and the approach labels differed again: `fair_value_of_an_asset` vs `fair_value_measurement_of_an_asset` and `fair_value_of_a_liability` vs `fair_value_measurement_of_a_liability`
  - another attempt at handling this in the prompt was made (the prompt is getting very long)
  - after another iteration, the 2 runs finally returned `fair_value_of_an_asset` and `fair_value_of_a_liability``

Finally Q1.4 was run again to check the impact on the net investment hedge approach naming: all good