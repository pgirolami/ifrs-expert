# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `57_answer-evals_on_variants_for_Q5_Q6_Q9_Q12_Q16`
- Run: `2026-05-02_12-49-24_promptfoo-eval-family-q6`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 10

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| contractual_decision_making_power | no | 1/10 | 1 |
| contractual_decision_making_rights | no | 2/10 | 2 |
| contractual_power | no | 1/10 | 1 |
| contractual_power_over_relevant_activities | no | 1/10 | 1 |
| contractual_rights | no | 1/10 | 1 |
| control | no | 2/10 | 1 |
| control_of_a_deemed_separate_entity | no | 1/10 | 1 |
| de_facto_control_through_voting_rights | no | 1/10 | 1 |
| de_facto_power | no | 2/10 | 2 |
| de_facto_power_through_voting_rights | no | 2/10 | 2 |
| deemed_separate_entity | no | 1/10 | 1 |
| joint_control | no | 2/10 | 1 |
| majority_voting_rights | no | 2/10 | 2 |
| potential_voting_rights_power | no | 1/10 | 1 |
| power_through_contractual_rights | no | 2/10 | 2 |
| power_through_delegated_decision_making_rights | no | 1/10 | 1 |
| power_through_potential_voting_rights | no | 1/10 | 1 |
| power_through_relevant_activities_upon_contingent_events | no | 1/10 | 1 |
| power_through_voting_rights | no | 1/10 | 1 |
| practical_ability_and_de_facto_agency | no | 1/10 | 1 |
| principal_agent_assessment | no | 1/10 | 1 |
| principal_decision_maker | no | 2/10 | 2 |
| principal_decision_maker_power | no | 1/10 | 1 |
| principal_power | no | 1/10 | 1 |
| principal_versus_agent | no | 1/10 | 1 |
| protective_rights | no | 1/10 | 1 |
| significant_influence | no | 2/10 | 1 |
| substantive_majority_voting_rights | no | 1/10 | 1 |
| substantive_potential_voting_rights | no | 3/10 | 3 |
| voting_rights | no | 2/10 | 2 |
| voting_rights_power | no | 2/10 | 2 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q6.0 | 2 | 15.0 | 35.0 | 0 | 11 |
| Q6.1 | 2 | 35.0 | 35.0 | 0 | 11 |
| Q6.2 | 2 | 35.0 | 35.0 | 0 | 6 |
| Q6.3 | 2 | 35.0 | 35.0 | 0 | 10 |
| Q6.4 | 2 | 70.0 | 100.0 | 0 | 6 |

## Authority Categorization by Run

### Q6.0 / 0

- Question: Comment déterminer si un investisseur détient le pouvoir sur une entité ?
- Embedded question: Comment déterminer si un investisseur détient le pouvoir sur une entité ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 10 | g10-14 | 🎯 authoritative | 0.69 | D:0 |
| IFRS 10 | g15-16 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g17-18 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g5-18 | 🎯 authoritative | 0.69-0.69 | D:0 |
| IFRS 10 | gB11-B13 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB14-B28 | 🎯 authoritative | 0.69-0.70 | D:0 |
| IFRS 10 | gB2-B85 | 🎯 authoritative | 0.73 | D:0 |
| IFRS 10 | gB22-B25 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB26-B28 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB29-B33 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB34-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB35-B35 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB36-B37 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB38-B38 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB39-B39 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB40-B40 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB41-B46 | 🎯 authoritative | 0.70 | D:0 |
| IFRS 10 | gB47-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB5-B8 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB51-B54 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB55-B57 | 🗑️ dropped | 0.69 | D:0 |
| IFRS 10 | gB62-B63 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB64-B67 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB68-B70 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB71-B72 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB73-B75 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB76-B79 | 🗑️ dropped | 0.69 | D:0 |
| IFRS 10 | gB80-B85 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB9-B54 | 🎯 authoritative | 0.72 | D:0 |
| IFRS 10 | sgB58-B72 | 🎯 authoritative | — | D:0 |
| IAS 28 | g10-15 | 🗑️ dropped | 0.59 | D:9 |
| IAS 28 | g16-43 | 🗑️ dropped | 0.58 | D:2 |
| IAS 28 | g17-19 | 🗑️ dropped | 0.62-0.64 | D:3 |
| IAS 28 | g20-21 | 🗑️ dropped | — | D:2 |
| IAS 28 | g22-24 | 🗑️ dropped | — | D:3 |
| IAS 28 | g25-25 | 🗑️ dropped | — | D:2 |
| IAS 28 | g26-39 | 🗑️ dropped | 0.59 | D:20 |
| IAS 28 | g40-43 | 🗑️ dropped | — | D:8 |
| IAS 28 | g5-9 | 🗑️ dropped | 0.58-0.64 | D:6 |
| IFRS 3 | g18-20 | 🗑️ dropped | 0.55 | D:3 |
| IFRS 3 | g3-3 | 🗑️ dropped | — | D:1 |
| IFRS 3 | g41-42A | 🗑️ dropped | 0.54 | D:3 |
| IFRS 3 | g43-44 | 🗑️ dropped | 0.53 | D:2 |
| IFRS 3 | g6-7 | 🗑️ dropped | 0.55 | D:3 |
| IFRS 3 | gB1-B4 | 🗑️ dropped | 0.56 | D:5 |
| IFRS 3 | gB13-B18 | 🗑️ dropped | 0.54-0.61 | D:8 |
| IFRS 3 | gB19-B27 | 🗑️ dropped | — | D:3 |
| IFRS 3 | gB20-B20 | 🗑️ dropped | — | D:1 |
| IFRS 3 | gB21-B22 | 🗑️ dropped | — | D:2 |
| IFRS 3 | gB23-B24 | 🗑️ dropped | — | D:2 |
| IFRS 3 | gB25-B27 | 🗑️ dropped | — | D:3 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | 0.55 | D:5 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | — | D:2 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:4 |
| IFRS 3 | gB44-B45 | 🗑️ dropped | 0.57 | D:2 |
| IFRS 3 | gB7A-B7C | 🗑️ dropped | 0.54 | D:3 |

Dropped chunks:

- IAS 28 / g10-15 / 10 / dropped
- IAS 28 / g10-15 / 11 / dropped
- IAS 28 / g10-15 / 12 / dropped
- IAS 28 / g10-15 / 13 / dropped
- IAS 28 / g10-15 / 14 / dropped
- IAS 28 / g10-15 / 14A / dropped
- IAS 28 / g10-15 / 15 / dropped
- IAS 28 / g10-15 / E2 / dropped
- IAS 28 / g10-15 / E3 / dropped
- IAS 28 / g16-43 / 16 / dropped
- IAS 28 / g16-43 / E4 / dropped
- IAS 28 / g17-19 / 17 / dropped
- IAS 28 / g17-19 / 18 / dropped
- IAS 28 / g17-19 / 19 / dropped
- IAS 28 / g20-21 / 20 / dropped
- IAS 28 / g20-21 / 21 / dropped
- IAS 28 / g22-24 / 22 / dropped
- IAS 28 / g22-24 / 23 / dropped
- IAS 28 / g22-24 / 24 / dropped
- IAS 28 / g25-25 / 25 / dropped
- IAS 28 / g25-25 / E5 / dropped
- IAS 28 / g26-39 / 26 / dropped
- IAS 28 / g26-39 / 27 / dropped
- IAS 28 / g26-39 / 28 / dropped
- IAS 28 / g26-39 / 29 / dropped
- IAS 28 / g26-39 / 30 / dropped
- IAS 28 / g26-39 / 31 / dropped
- IAS 28 / g26-39 / 31A / dropped
- IAS 28 / g26-39 / 31B / dropped
- IAS 28 / g26-39 / 32 / dropped
- IAS 28 / g26-39 / 33 / dropped
- IAS 28 / g26-39 / 34 / dropped
- IAS 28 / g26-39 / 35 / dropped
- IAS 28 / g26-39 / 36 / dropped
- IAS 28 / g26-39 / 36A / dropped
- IAS 28 / g26-39 / 37 / dropped
- IAS 28 / g26-39 / 38 / dropped
- IAS 28 / g26-39 / 39 / dropped
- IAS 28 / g26-39 / E6 / dropped
- IAS 28 / g26-39 / E7 / dropped
- IAS 28 / g26-39 / E8 / dropped
- IAS 28 / g40-43 / 40 / dropped
- IAS 28 / g40-43 / 41A / dropped
- IAS 28 / g40-43 / 41B / dropped
- IAS 28 / g40-43 / 41C / dropped
- IAS 28 / g40-43 / 42 / dropped
- IAS 28 / g40-43 / 43 / dropped
- IAS 28 / g40-43 / E9 / dropped
- IAS 28 / g40-43 / E10 / dropped
- IAS 28 / g5-9 / 5 / dropped
- IAS 28 / g5-9 / 6 / dropped
- IAS 28 / g5-9 / 7 / dropped
- IAS 28 / g5-9 / 8 / dropped
- IAS 28 / g5-9 / 9 / dropped
- IAS 28 / g5-9 / E1 / dropped
- IFRS 3 / g18-20 / 18 / dropped
- IFRS 3 / g18-20 / 19 / dropped
- IFRS 3 / g18-20 / 20 / dropped
- IFRS 3 / g3-3 / 3 / dropped
- IFRS 3 / g41-42A / 41 / dropped
- IFRS 3 / g41-42A / 42 / dropped
- IFRS 3 / g41-42A / 42A / dropped
- IFRS 3 / g43-44 / 43 / dropped
- IFRS 3 / g43-44 / 44 / dropped
- IFRS 3 / g6-7 / 6 / dropped
- IFRS 3 / g6-7 / 7 / dropped
- IFRS 3 / g6-7 / E7 / dropped
- IFRS 3 / gB1-B4 / B1 / dropped
- IFRS 3 / gB1-B4 / B2 / dropped
- IFRS 3 / gB1-B4 / B3 / dropped
- IFRS 3 / gB1-B4 / B4 / dropped
- IFRS 3 / gB1-B4 / E11 / dropped
- IFRS 3 / gB13-B18 / B13 / dropped
- IFRS 3 / gB13-B18 / B14 / dropped
- IFRS 3 / gB13-B18 / B15 / dropped
- IFRS 3 / gB13-B18 / B16 / dropped
- IFRS 3 / gB13-B18 / B17 / dropped
- IFRS 3 / gB13-B18 / B18 / dropped
- IFRS 3 / gB13-B18 / E12 / dropped
- IFRS 3 / gB13-B18 / E13 / dropped
- IFRS 3 / gB19-B27 / B19 / dropped
- IFRS 3 / gB19-B27 / E14 / dropped
- IFRS 3 / gB19-B27 / E15 / dropped
- IFRS 3 / gB20-B20 / B20 / dropped
- IFRS 3 / gB21-B22 / B21 / dropped
- IFRS 3 / gB21-B22 / B22 / dropped
- IFRS 3 / gB23-B24 / B23 / dropped
- IFRS 3 / gB23-B24 / B24 / dropped
- IFRS 3 / gB25-B27 / B25 / dropped
- IFRS 3 / gB25-B27 / B26 / dropped
- IFRS 3 / gB25-B27 / B27 / dropped
- IFRS 3 / gB31-B40 / B31 / dropped
- IFRS 3 / gB31-B40 / B32 / dropped
- IFRS 3 / gB31-B40 / B33 / dropped
- IFRS 3 / gB31-B40 / B34 / dropped
- IFRS 3 / gB31-B40 / E16 / dropped
- IFRS 3 / gB35-B36 / B35 / dropped
- IFRS 3 / gB35-B36 / B36 / dropped
- IFRS 3 / gB37-B40 / B37 / dropped
- IFRS 3 / gB37-B40 / B38 / dropped
- IFRS 3 / gB37-B40 / B39 / dropped
- IFRS 3 / gB37-B40 / B40 / dropped
- IFRS 3 / gB44-B45 / B44 / dropped
- IFRS 3 / gB44-B45 / B45 / dropped
- IFRS 3 / gB7A-B7C / B7A / dropped
- IFRS 3 / gB7A-B7C / B7B / dropped
- IFRS 3 / gB7A-B7C / B7C / dropped

### Q6.0 / 1

- Question: Comment déterminer si un investisseur détient le pouvoir sur une entité ?
- Embedded question: Comment déterminer si un investisseur détient le pouvoir sur une entité ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 10 | g10-14 | 🎯 authoritative | 0.69 | D:0 |
| IFRS 10 | g15-16 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g17-18 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g5-18 | 🎯 authoritative | 0.69-0.69 | D:0 |
| IFRS 10 | gB11-B13 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB14-B28 | 🎯 authoritative | 0.69-0.70 | D:0 |
| IFRS 10 | gB2-B85 | 🎯 authoritative | 0.73 | D:0 |
| IFRS 10 | gB22-B25 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB26-B28 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB29-B33 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB34-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB35-B35 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB36-B37 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB38-B38 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB39-B39 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB40-B40 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB41-B46 | 🎯 authoritative | 0.70 | D:0 |
| IFRS 10 | gB47-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB5-B8 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB51-B54 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB55-B57 | 🗑️ dropped | 0.69 | D:0 |
| IFRS 10 | gB62-B63 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB64-B67 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB68-B70 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB71-B72 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB73-B75 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB76-B79 | 🎯 authoritative | 0.69 | D:0 |
| IFRS 10 | gB80-B85 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB9-B54 | 🎯 authoritative | 0.72 | D:0 |
| IFRS 10 | sgB58-B72 | 🎯 authoritative | — | D:0 |
| IAS 28 | g10-15 | 🗑️ dropped | 0.59 | D:0 |
| IAS 28 | g16-43 | 🖼️ peripheral | 0.58 | D:0 |
| IAS 28 | g17-19 | 🖼️ peripheral | 0.62-0.64 | D:0 |
| IAS 28 | g20-21 | 🗑️ dropped | — | D:0 |
| IAS 28 | g22-24 | 🖼️ peripheral | — | D:0 |
| IAS 28 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 28 | g26-39 | 🖼️ peripheral | 0.59 | D:0 |
| IAS 28 | g40-43 | 🗑️ dropped | — | D:0 |
| IAS 28 | g5-9 | 🖼️ peripheral | 0.58-0.64 | D:0 |
| IFRS 3 | g18-20 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 3 | g3-3 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g41-42A | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | g43-44 | 🔎 secondary | 0.53 | D:0 |
| IFRS 3 | g6-7 | 🔎 secondary | 0.55 | D:0 |
| IFRS 3 | gB1-B4 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 3 | gB13-B18 | 🔎 secondary | 0.54-0.61 | D:0 |
| IFRS 3 | gB19-B27 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB20-B20 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB21-B22 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB23-B24 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB25-B27 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB44-B45 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 3 | gB7A-B7C | 🗑️ dropped | 0.54 | D:0 |

### Q6.1 / 0

- Question: Quels éléments permettent d’établir qu’un investisseur détient le pouvoir sur une entité au sens d’IFRS 10 ?
- Embedded question: Quels éléments permettent d’établir qu’un investisseur détient le pouvoir sur une entité au sens d’IFRS 10 ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 10 | g10-14 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 10 | g15-16 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g17-18 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g5-18 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 10 | gB11-B13 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB14-B28 | 🎯 authoritative | 0.64-0.65 | D:0 |
| IFRS 10 | gB2-B85 | 🎯 authoritative | 0.64 | D:0 |
| IFRS 10 | gB22-B25 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB26-B28 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB29-B33 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB34-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB35-B35 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB36-B37 | 🎯 authoritative | 0.64 | D:0 |
| IFRS 10 | gB38-B38 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB39-B39 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB40-B40 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB41-B46 | 🎯 authoritative | 0.64-0.64 | D:0 |
| IFRS 10 | gB47-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB5-B8 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB51-B54 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB55-B57 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB62-B63 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB64-B67 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB68-B70 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB71-B72 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB73-B75 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB76-B79 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB80-B85 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB9-B54 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 10 | sgB58-B72 | 🎯 authoritative | — | D:0 |
| IAS 28 | g10-15 | 🗑️ dropped | 0.57 | D:0 |
| IAS 28 | g16-43 | 🖼️ peripheral | 0.56 | D:0 |
| IAS 28 | g17-19 | 🖼️ peripheral | 0.59-0.60 | D:0 |
| IAS 28 | g20-21 | 🗑️ dropped | 0.57 | D:0 |
| IAS 28 | g22-24 | 🖼️ peripheral | — | D:0 |
| IAS 28 | g25-25 | 🖼️ peripheral | — | D:0 |
| IAS 28 | g26-39 | 🗑️ dropped | 0.57 | D:0 |
| IAS 28 | g40-43 | 🗑️ dropped | — | D:0 |
| IAS 28 | g5-9 | 🖼️ peripheral | 0.56-0.63 | D:0 |
| IAS 24 | g2-4 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 12 | g1-4 | 🗑️ dropped | — | D:0 |
| IFRS 12 | g10-19 | 🖼️ peripheral | — | D:0 |
| IFRS 12 | g12-12 | 🖼️ peripheral | — | D:0 |
| IFRS 12 | g13-13 | 🖼️ peripheral | — | D:0 |
| IFRS 12 | g14-17 | 🗑️ dropped | — | D:0 |
| IFRS 12 | g18-18 | 🗑️ dropped | — | D:0 |
| IFRS 12 | g19-19 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 12 | g19A-19G_V1 | 🗑️ dropped | 0.54-0.59 | D:0 |
| IFRS 12 | g2-4 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 12 | g20-23 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 12 | g21-22 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 12 | g23-23 | 🗑️ dropped | — | D:0 |
| IFRS 12 | g24-31 | 🖼️ peripheral | — | D:0 |
| IFRS 12 | g26-28 | 🗑️ dropped | — | D:0 |
| IFRS 12 | g29-31 | 🖼️ peripheral | — | D:0 |
| IFRS 12 | g5-6 | 🗑️ dropped | — | D:0 |
| IFRS 12 | g7-9B | 🔎 secondary | 0.57-0.61 | D:0 |
| IFRS 12 | g9A-9B | 🗑️ dropped | 0.56-0.63 | D:0 |
| IFRS 12 | gB10-B17 | 🗑️ dropped | — | D:0 |

### Q6.1 / 1

- Question: Quels éléments permettent d’établir qu’un investisseur détient le pouvoir sur une entité au sens d’IFRS 10 ?
- Embedded question: Quels éléments permettent d’établir qu’un investisseur détient le pouvoir sur une entité au sens d’IFRS 10 ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 10 | g10-14 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 10 | g15-16 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g17-18 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g5-18 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 10 | gB11-B13 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB14-B28 | 🎯 authoritative | 0.64-0.65 | D:0 |
| IFRS 10 | gB2-B85 | 🎯 authoritative | 0.64 | D:0 |
| IFRS 10 | gB22-B25 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB26-B28 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB29-B33 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB34-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB35-B35 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB36-B37 | 🎯 authoritative | 0.64 | D:0 |
| IFRS 10 | gB38-B38 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB39-B39 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB40-B40 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB41-B46 | 🎯 authoritative | 0.64-0.64 | D:0 |
| IFRS 10 | gB47-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB5-B8 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB51-B54 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB55-B57 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB62-B63 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB64-B67 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB68-B70 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB71-B72 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB73-B75 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB76-B79 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB80-B85 | 🔎 secondary | — | D:0 |
| IFRS 10 | gB9-B54 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 10 | sgB58-B72 | 🎯 authoritative | — | D:0 |
| IAS 28 | g10-15 | 🗑️ dropped | 0.57 | D:0 |
| IAS 28 | g16-43 | 🖼️ peripheral | 0.56 | D:0 |
| IAS 28 | g17-19 | 🗑️ dropped | 0.59-0.60 | D:0 |
| IAS 28 | g20-21 | 🗑️ dropped | 0.57 | D:0 |
| IAS 28 | g22-24 | 🗑️ dropped | — | D:0 |
| IAS 28 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 28 | g26-39 | 🗑️ dropped | 0.57 | D:0 |
| IAS 28 | g40-43 | 🗑️ dropped | — | D:0 |
| IAS 28 | g5-9 | 🖼️ peripheral | 0.56-0.63 | D:0 |
| IAS 24 | g2-4 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 12 | g1-4 | 🗑️ dropped | — | D:0 |
| IFRS 12 | g10-19 | 🖼️ peripheral | — | D:0 |
| IFRS 12 | g12-12 | 🖼️ peripheral | — | D:0 |
| IFRS 12 | g13-13 | 🖼️ peripheral | — | D:0 |
| IFRS 12 | g14-17 | 🗑️ dropped | — | D:0 |
| IFRS 12 | g18-18 | 🗑️ dropped | — | D:0 |
| IFRS 12 | g19-19 | 🖼️ peripheral | 0.56 | D:0 |
| IFRS 12 | g19A-19G_V1 | 🗑️ dropped | 0.54-0.59 | D:0 |
| IFRS 12 | g2-4 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 12 | g20-23 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 12 | g21-22 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 12 | g23-23 | 🗑️ dropped | — | D:0 |
| IFRS 12 | g24-31 | 🖼️ peripheral | — | D:0 |
| IFRS 12 | g26-28 | 🗑️ dropped | — | D:0 |
| IFRS 12 | g29-31 | 🖼️ peripheral | — | D:0 |
| IFRS 12 | g5-6 | 🗑️ dropped | — | D:0 |
| IFRS 12 | g7-9B | 🔎 secondary | 0.57-0.61 | D:0 |
| IFRS 12 | g9A-9B | 🗑️ dropped | 0.56-0.63 | D:0 |
| IFRS 12 | gB10-B17 | 🗑️ dropped | — | D:0 |

### Q6.2 / 0

- Question: Un investisseur exerce des droits sur une entité mais leur portée doit être analysée. Comment déterminer si ces droits lui confèrent le pouvoir pertinent pour conclure à un contrôle ?
- Embedded question: Un investisseur exerce des droits sur une entité mais leur portée doit être analysée. Comment déterminer si ces droits lui confèrent le pouvoir pertinent pour conclure à un contrôle ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 10 | g10-14 | 🎯 authoritative | — | D:0 |
| IFRS 10 | g15-16 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g17-18 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g5-18 | 🎯 authoritative | 0.74 | D:0 |
| IFRS 10 | gB11-B13 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB14-B28 | 🎯 authoritative | 0.74-0.75 | D:0 |
| IFRS 10 | gB2-B85 | 🎯 authoritative | 0.77 | D:0 |
| IFRS 10 | gB22-B25 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB26-B28 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB29-B33 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB34-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB35-B35 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB36-B37 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB38-B38 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB39-B39 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB40-B40 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB41-B46 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB47-B50 | 🎯 authoritative | 0.73-0.74 | D:0 |
| IFRS 10 | gB5-B8 | 🎯 authoritative | 0.76 | D:0 |
| IFRS 10 | gB51-B54 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB55-B57 | 🗑️ dropped | 0.77 | D:0 |
| IFRS 10 | gB62-B63 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB64-B67 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB68-B70 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB71-B72 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB73-B75 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB76-B79 | 🗑️ dropped | 0.74 | D:0 |
| IFRS 10 | gB80-B85 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB9-B54 | 🎯 authoritative | 0.76 | D:0 |
| IFRS 10 | sgB58-B72 | 🎯 authoritative | — | D:0 |
| IAS 28 | g10-15 | 🗑️ dropped | 0.62-0.64 | D:0 |
| IAS 28 | g16-43 | 🖼️ peripheral | 0.62 | D:0 |
| IAS 28 | g17-19 | 🗑️ dropped | 0.60-0.61 | D:0 |
| IAS 28 | g20-21 | 🗑️ dropped | — | D:0 |
| IAS 28 | g22-24 | 🗑️ dropped | — | D:0 |
| IAS 28 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 28 | g26-39 | 🗑️ dropped | — | D:0 |
| IAS 28 | g40-43 | 🗑️ dropped | — | D:0 |
| IAS 28 | g5-9 | 🖼️ peripheral | 0.59-0.66 | D:0 |
| IAS 24 | g5-8 | 🖼️ peripheral | 0.55-0.55 | D:0 |
| IAS 24 | sg13-24 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 16 | g1-2 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g100-102 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g103-103 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g12-17 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g13-16 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g17-17 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g3-4 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g36-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g39-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g5-8 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g9-17 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 16 | g99-103 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 16 | gB13-B20 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB14-B19 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB20-B20 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB21-B23 | 🗑️ dropped | 0.55-0.56 | D:0 |
| IFRS 16 | gB24-B31 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 16 | gB25-B31 | 🖼️ peripheral | 0.59-0.63 | D:0 |
| IFRS 16 | gB28-B29 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 16 | gB30-B31 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB34-B41 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 16 | gB9-B31 | 🖼️ peripheral | 0.67 | D:0 |

### Q6.2 / 1

- Question: Un investisseur exerce des droits sur une entité mais leur portée doit être analysée. Comment déterminer si ces droits lui confèrent le pouvoir pertinent pour conclure à un contrôle ?
- Embedded question: Un investisseur exerce des droits sur une entité mais leur portée doit être analysée. Comment déterminer si ces droits lui confèrent le pouvoir pertinent pour conclure à un contrôle ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 10 | g10-14 | 🎯 authoritative | — | D:0 |
| IFRS 10 | g15-16 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g17-18 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g5-18 | 🎯 authoritative | 0.74 | D:0 |
| IFRS 10 | gB11-B13 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB14-B28 | 🎯 authoritative | 0.74-0.75 | D:0 |
| IFRS 10 | gB2-B85 | 🎯 authoritative | 0.77 | D:0 |
| IFRS 10 | gB22-B25 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB26-B28 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB29-B33 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB34-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB35-B35 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB36-B37 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB38-B38 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB39-B39 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB40-B40 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB41-B46 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB47-B50 | 🎯 authoritative | 0.73-0.74 | D:0 |
| IFRS 10 | gB5-B8 | 🎯 authoritative | 0.76 | D:0 |
| IFRS 10 | gB51-B54 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB55-B57 | 🗑️ dropped | 0.77 | D:0 |
| IFRS 10 | gB62-B63 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB64-B67 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB68-B70 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB71-B72 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB73-B75 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB76-B79 | 🗑️ dropped | 0.74 | D:0 |
| IFRS 10 | gB80-B85 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB9-B54 | 🎯 authoritative | 0.76 | D:0 |
| IFRS 10 | sgB58-B72 | 🎯 authoritative | — | D:0 |
| IAS 28 | g10-15 | 🗑️ dropped | 0.62-0.64 | D:0 |
| IAS 28 | g16-43 | 🖼️ peripheral | 0.62 | D:0 |
| IAS 28 | g17-19 | 🗑️ dropped | 0.60-0.61 | D:0 |
| IAS 28 | g20-21 | 🗑️ dropped | — | D:0 |
| IAS 28 | g22-24 | 🗑️ dropped | — | D:0 |
| IAS 28 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 28 | g26-39 | 🗑️ dropped | — | D:0 |
| IAS 28 | g40-43 | 🗑️ dropped | — | D:0 |
| IAS 28 | g5-9 | 🖼️ peripheral | 0.59-0.66 | D:0 |
| IAS 24 | g5-8 | 🖼️ peripheral | 0.55-0.55 | D:0 |
| IAS 24 | sg13-24 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 16 | g1-2 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g100-102 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g103-103 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g12-17 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g13-16 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g17-17 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g3-4 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g36-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g39-43 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g5-8 | 🗑️ dropped | — | D:0 |
| IFRS 16 | g9-17 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 16 | g99-103 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 16 | gB13-B20 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB14-B19 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB20-B20 | 🗑️ dropped | — | D:0 |
| IFRS 16 | gB21-B23 | 🗑️ dropped | 0.55-0.56 | D:0 |
| IFRS 16 | gB24-B31 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 16 | gB25-B31 | 🖼️ peripheral | 0.59-0.63 | D:0 |
| IFRS 16 | gB28-B29 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 16 | gB30-B31 | 🖼️ peripheral | — | D:0 |
| IFRS 16 | gB34-B41 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 16 | gB9-B31 | 🖼️ peripheral | 0.67 | D:0 |

### Q6.3 / 0

- Question: Dans l’analyse du contrôle, comment apprécier si les droits détenus par un investisseur sont suffisants pour diriger les activités pertinentes de l’entité ?
- Embedded question: Dans l’analyse du contrôle, comment apprécier si les droits détenus par un investisseur sont suffisants pour diriger les activités pertinentes de l’entité ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 10 | g10-14 | 🎯 authoritative | — | D:0 |
| IFRS 10 | g15-16 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g17-18 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g5-18 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 10 | gB11-B13 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB14-B28 | 🎯 authoritative | 0.67-0.71 | D:0 |
| IFRS 10 | gB2-B85 | 🎯 authoritative | 0.71 | D:0 |
| IFRS 10 | gB22-B25 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB26-B28 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB29-B33 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB34-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB35-B35 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB36-B37 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB38-B38 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB39-B39 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB40-B40 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB41-B46 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB47-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB5-B8 | 🎯 authoritative | 0.69-0.71 | D:0 |
| IFRS 10 | gB51-B54 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB55-B57 | 🗑️ dropped | 0.69 | D:0 |
| IFRS 10 | gB62-B63 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB64-B67 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB68-B70 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB71-B72 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB73-B75 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB76-B79 | 🗑️ dropped | 0.68-0.71 | D:0 |
| IFRS 10 | gB80-B85 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB9-B54 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 10 | sgB58-B72 | 🎯 authoritative | — | D:0 |
| IAS 28 | g10-15 | 🗑️ dropped | 0.57-0.61 | D:0 |
| IAS 28 | g16-43 | 🖼️ peripheral | 0.59 | D:0 |
| IAS 28 | g17-19 | 🗑️ dropped | 0.55-0.57 | D:0 |
| IAS 28 | g20-21 | 🗑️ dropped | — | D:0 |
| IAS 28 | g22-24 | 🗑️ dropped | — | D:0 |
| IAS 28 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 28 | g26-39 | 🗑️ dropped | — | D:0 |
| IAS 28 | g40-43 | 🗑️ dropped | — | D:0 |
| IAS 28 | g5-9 | 🖼️ peripheral | 0.56-0.59 | D:0 |
| IAS 24 | sg13-24 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 15 | g18-21 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g31-45 | 🖼️ peripheral | 0.54-0.57 | D:0 |
| IFRS 15 | g35-37 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 15 | g38-38 | 🖼️ peripheral | 0.64 | D:0 |
| IFRS 15 | g39-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g41-43 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g44-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g47-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g50-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g56-58 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g59-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g60-65 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g66-69 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 15 | g70-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB3-B4 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB34-B38 | 🖼️ peripheral | 0.54-0.56 | D:0 |
| IFRS 15 | gB5-B5 | 🖼️ peripheral | 0.60 | D:0 |
| IFRS 15 | gB6-B8 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 15 | gB64-B76 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB66-B69 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB70-B76 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB77-B78 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB79-B82 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 15 | gB83-B86 | 🗑️ dropped | — | D:0 |

### Q6.3 / 1

- Question: Dans l’analyse du contrôle, comment apprécier si les droits détenus par un investisseur sont suffisants pour diriger les activités pertinentes de l’entité ?
- Embedded question: Dans l’analyse du contrôle, comment apprécier si les droits détenus par un investisseur sont suffisants pour diriger les activités pertinentes de l’entité ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 10 | g10-14 | 🎯 authoritative | — | D:0 |
| IFRS 10 | g15-16 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g17-18 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g5-18 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 10 | gB11-B13 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB14-B28 | 🎯 authoritative | 0.67-0.71 | D:0 |
| IFRS 10 | gB2-B85 | 🎯 authoritative | 0.71 | D:0 |
| IFRS 10 | gB22-B25 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB26-B28 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB29-B33 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB34-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB35-B35 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB36-B37 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB38-B38 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB39-B39 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB40-B40 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB41-B46 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB47-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB5-B8 | 🎯 authoritative | 0.69-0.71 | D:0 |
| IFRS 10 | gB51-B54 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB55-B57 | 🗑️ dropped | 0.69 | D:0 |
| IFRS 10 | gB62-B63 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB64-B67 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB68-B70 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB71-B72 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB73-B75 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB76-B79 | 🗑️ dropped | 0.68-0.71 | D:0 |
| IFRS 10 | gB80-B85 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB9-B54 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 10 | sgB58-B72 | 🗑️ dropped | — | D:0 |
| IAS 28 | g10-15 | 🗑️ dropped | 0.57-0.61 | D:0 |
| IAS 28 | g16-43 | 🖼️ peripheral | 0.59 | D:0 |
| IAS 28 | g17-19 | 🗑️ dropped | 0.55-0.57 | D:0 |
| IAS 28 | g20-21 | 🗑️ dropped | — | D:0 |
| IAS 28 | g22-24 | 🗑️ dropped | — | D:0 |
| IAS 28 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 28 | g26-39 | 🗑️ dropped | — | D:0 |
| IAS 28 | g40-43 | 🗑️ dropped | — | D:0 |
| IAS 28 | g5-9 | 🖼️ peripheral | 0.56-0.59 | D:0 |
| IAS 24 | sg13-24 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 15 | g18-21 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g31-45 | 🖼️ peripheral | 0.54-0.57 | D:0 |
| IFRS 15 | g35-37 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 15 | g38-38 | 🖼️ peripheral | 0.64 | D:0 |
| IFRS 15 | g39-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g41-43 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g44-45 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g47-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g50-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g56-58 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g59-59 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g60-65 | 🗑️ dropped | — | D:0 |
| IFRS 15 | g66-69 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 15 | g70-72 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB3-B4 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB34-B38 | 🖼️ peripheral | 0.54-0.56 | D:0 |
| IFRS 15 | gB5-B5 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 15 | gB6-B8 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 15 | gB64-B76 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB66-B69 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB70-B76 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB77-B78 | 🗑️ dropped | — | D:0 |
| IFRS 15 | gB79-B82 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 15 | gB83-B86 | 🗑️ dropped | — | D:0 |

### Q6.4 / 0

- Question: Une entité est détenue ou influencée par plusieurs parties. Sur quelle base IFRS faut-il conclure qu’un investisseur, plutôt qu’un autre, détient le pouvoir sur cette entité ?
- Embedded question: Une entité est détenue ou influencée par plusieurs parties. Sur quelle base IFRS faut-il conclure qu’un investisseur, plutôt qu’un autre, détient le pouvoir sur cette entité ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 10 | g10-14 | 🎯 authoritative | 0.67-0.67 | D:0 |
| IFRS 10 | g15-16 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g17-18 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g5-18 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 10 | gB11-B13 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB14-B28 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB2-B85 | 🎯 authoritative | 0.66 | D:0 |
| IFRS 10 | gB22-B25 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB26-B28 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB29-B33 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB34-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB35-B35 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB36-B37 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 10 | gB38-B38 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB39-B39 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB40-B40 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB41-B46 | 🎯 authoritative | 0.66-0.68 | D:0 |
| IFRS 10 | gB47-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB5-B8 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB51-B54 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB55-B57 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB62-B63 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB64-B67 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB68-B70 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB71-B72 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB73-B75 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB76-B79 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 10 | gB80-B85 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB9-B54 | 🎯 authoritative | 0.66-0.67 | D:0 |
| IFRS 10 | sgB58-B72 | 🎯 authoritative | — | D:0 |
| IAS 28 | g10-15 | 🗑️ dropped | 0.62-0.62 | D:0 |
| IAS 28 | g16-43 | 🔎 secondary | 0.61 | D:0 |
| IAS 28 | g17-19 | 🗑️ dropped | 0.63-0.65 | D:0 |
| IAS 28 | g20-21 | 🗑️ dropped | 0.61 | D:0 |
| IAS 28 | g22-24 | 🗑️ dropped | — | D:0 |
| IAS 28 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 28 | g26-39 | 🗑️ dropped | — | D:0 |
| IAS 28 | g40-43 | 🗑️ dropped | — | D:0 |
| IAS 28 | g5-9 | 🔎 secondary | 0.60-0.65 | D:0 |
| IAS 24 | g5-8 | 🖼️ peripheral | 0.53-0.56 | D:0 |
| IAS 24 | g9-12 | 🖼️ peripheral | 0.54 | D:0 |
| IAS 24 | sg13-24 | 🖼️ peripheral | 0.55 | D:0 |
| IAS 24 | sg25-27 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 11 | g1-2 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 11 | g14-19 | 🗑️ dropped | — | D:0 |
| IFRS 11 | g2-2 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 11 | g20-23 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 11 | g24-25 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 11 | g26-27 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 11 | g7-13 | 🔎 secondary | 0.57-0.61 | D:0 |
| IFRS 11 | gB12-B32 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB15-B32 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB16-B18 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB19-B21 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB2-B4 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB22-B24 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB25-B28 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB29-B32 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB33A-B33D_V2 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 11 | gB34-B35 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB36-B37 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB5-B11 | 🔎 secondary | 0.67 | D:0 |

### Q6.4 / 1

- Question: Une entité est détenue ou influencée par plusieurs parties. Sur quelle base IFRS faut-il conclure qu’un investisseur, plutôt qu’un autre, détient le pouvoir sur cette entité ?
- Embedded question: Une entité est détenue ou influencée par plusieurs parties. Sur quelle base IFRS faut-il conclure qu’un investisseur, plutôt qu’un autre, détient le pouvoir sur cette entité ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 10 | g10-14 | 🎯 authoritative | 0.67-0.67 | D:0 |
| IFRS 10 | g15-16 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g17-18 | 🗑️ dropped | — | D:0 |
| IFRS 10 | g5-18 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 10 | gB11-B13 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB14-B28 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB2-B85 | 🎯 authoritative | 0.66 | D:0 |
| IFRS 10 | gB22-B25 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB26-B28 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB29-B33 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB34-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB35-B35 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB36-B37 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 10 | gB38-B38 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB39-B39 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB40-B40 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB41-B46 | 🎯 authoritative | 0.66-0.68 | D:0 |
| IFRS 10 | gB47-B50 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB5-B8 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB51-B54 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB55-B57 | 🗑️ dropped | — | D:0 |
| IFRS 10 | gB62-B63 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB64-B67 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB68-B70 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB71-B72 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB73-B75 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB76-B79 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 10 | gB80-B85 | 🎯 authoritative | — | D:0 |
| IFRS 10 | gB9-B54 | 🎯 authoritative | 0.66-0.67 | D:0 |
| IFRS 10 | sgB58-B72 | 🎯 authoritative | — | D:0 |
| IAS 28 | g10-15 | 🗑️ dropped | 0.62-0.62 | D:0 |
| IAS 28 | g16-43 | 🔎 secondary | 0.61 | D:0 |
| IAS 28 | g17-19 | 🗑️ dropped | 0.63-0.65 | D:0 |
| IAS 28 | g20-21 | 🗑️ dropped | 0.61 | D:0 |
| IAS 28 | g22-24 | 🗑️ dropped | — | D:0 |
| IAS 28 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 28 | g26-39 | 🗑️ dropped | — | D:0 |
| IAS 28 | g40-43 | 🗑️ dropped | — | D:0 |
| IAS 28 | g5-9 | 🔎 secondary | 0.60-0.65 | D:0 |
| IAS 24 | g5-8 | 🖼️ peripheral | 0.53-0.56 | D:0 |
| IAS 24 | g9-12 | 🖼️ peripheral | 0.54 | D:0 |
| IAS 24 | sg13-24 | 🖼️ peripheral | 0.55 | D:0 |
| IAS 24 | sg25-27 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 11 | g1-2 | 🔎 secondary | 0.58 | D:0 |
| IFRS 11 | g14-19 | 🗑️ dropped | — | D:0 |
| IFRS 11 | g2-2 | 🔎 secondary | 0.58 | D:0 |
| IFRS 11 | g20-23 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 11 | g24-25 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 11 | g26-27 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 11 | g7-13 | 🔎 secondary | 0.57-0.61 | D:0 |
| IFRS 11 | gB12-B32 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB15-B32 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB16-B18 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB19-B21 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB2-B4 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB22-B24 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB25-B28 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB29-B32 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB33A-B33D_V2 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 11 | gB34-B35 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB36-B37 | 🗑️ dropped | — | D:0 |
| IFRS 11 | gB5-B11 | 🔎 secondary | 0.67 | D:0 |

