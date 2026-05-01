# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `53_initial_eval-retrieve_for_Q9.0`
- Run: `2026-05-01_15-51-27_promptfoo-eval-family-q9`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 2

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| revenue_recognised_at_a_point_in_time | no | 1/2 | 1 |
| revenue_recognised_over_time | no | 1/2 | 1 |
| right_to_access_intellectual_property | no | 2/2 | 1 |
| right_to_use_intellectual_property | no | 2/2 | 1 |
| sales_based_or_usage_based_royalty_recognition | no | 1/2 | 1 |
| sales_or_usage_based_royalty_recognition | no | 1/2 | 1 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q9.0 | 2 | 76.7 | 76.7 | 0 | 8 |

## Authority Categorization by Run

### Q9.0 / 0

- Question: Comment constater le revenu lié aux licences de propriété intellectuelle : à une date donnée ou de façon étalée sur la durée du droit ?
- Embedded question: Comment constater le revenu lié aux licences de propriété intellectuelle : à une date donnée ou de façon étalée sur la durée du droit ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 15 | g31-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g35-37 | 🔎 secondary | 0.56 | D:0 |
| IFRS 15 | g38-38 | 🔎 secondary | — | D:0 |
| IFRS 15 | g39-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g41-43 | 🔎 secondary | — | D:0 |
| IFRS 15 | g44-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g47-72 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g50-59 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g55-55 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g56-58 | 🔎 secondary | 0.56 | D:0 |
| IFRS 15 | g59-59 | 🔎 secondary | — | D:0 |
| IFRS 15 | g60-65 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 15 | g66-69 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g70-72 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | gB34-B38 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 15 | gB52-B63B | 🎯 authoritative | 0.55-0.56 | D:0 |
| IFRS 15 | gB57-B62 | 🎯 authoritative | 0.57-0.58 | D:0 |
| IFRS 15 | gB63-B63B | 🎯 authoritative | 0.60 | D:0 |

### Q9.0 / 1

- Question: Comment constater le revenu lié aux licences de propriété intellectuelle : à une date donnée ou de façon étalée sur la durée du droit ?
- Embedded question: Comment constater le revenu lié aux licences de propriété intellectuelle : à une date donnée ou de façon étalée sur la durée du droit ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 15 | g31-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g35-37 | 🔎 secondary | 0.56 | D:0 |
| IFRS 15 | g38-38 | 🔎 secondary | — | D:0 |
| IFRS 15 | g39-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g41-43 | 🔎 secondary | — | D:0 |
| IFRS 15 | g44-45 | 🔎 secondary | — | D:0 |
| IFRS 15 | g47-72 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g50-59 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g55-55 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g56-58 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 15 | g59-59 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g60-65 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 15 | g66-69 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | g70-72 | 🖼️ peripheral | — | D:0 |
| IFRS 15 | gB34-B38 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 15 | gB52-B63B | 🎯 authoritative | 0.55-0.56 | D:0 |
| IFRS 15 | gB57-B62 | 🎯 authoritative | 0.57-0.58 | D:0 |
| IFRS 15 | gB63-B63B | 🔎 secondary | 0.60 | D:0 |

