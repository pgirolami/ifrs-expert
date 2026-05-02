# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `57_answer-evals_on_variants_for_Q5_Q6_Q9_Q12_Q16`
- Run: `2026-05-02_12-39-53_promptfoo-eval-family-q5`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 10

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| exit_price_for_an_asset | no | 1/10 | 1 |
| fair_value_of_a_group_position | no | 1/10 | 1 |
| fair_value_of_a_liability | yes | 6/10 | 4 |
| fair_value_of_an_asset | yes | 6/10 | 4 |
| individual_fair_value_measurement | no | 1/10 | 1 |
| net_exposure_portfolio_fair_value | no | 1/10 | 1 |
| net_exposure_to_credit_risk | no | 1/10 | 1 |
| portfolio_exception | no | 1/10 | 1 |
| risk_adjusted_cash_flows | no | 1/10 | 1 |
| risk_adjusted_discount_rate | no | 1/10 | 1 |
| stand_alone_asset_fair_value | no | 1/10 | 1 |
| stand_alone_liability_fair_value | no | 1/10 | 1 |
| transfer_price_for_a_liability | no | 1/10 | 1 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q5.0 | 2 | 73.3 | 88.3 | 0 | 1 |
| Q5.1 | 2 | 35.0 | 35.0 | 2 | 3 |
| Q5.2 | 2 | 100.0 | 100.0 | 0 | 0 |
| Q5.3 | 2 | 35.0 | 35.0 | 4 | 5 |
| Q5.4 | 2 | 15.0 | 35.0 | 2 | 2 |

## Authority Categorization by Run

### Q5.0 / 0

- Question: Le risque de défaut de la contrepartie doit-il être pris en compte dans l'évaluation de la juste valeur d'un actif ou d'un passif ?
- Embedded question: Le risque de défaut de la contrepartie doit-il être pris en compte dans l'évaluation de la juste valeur d'un actif ou d'un passif ?
fair value

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 13 | g1-4 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g11-14 | 🗑️ dropped | 0.68 | D:0 |
| IFRS 13 | g15-21 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | g22-23 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g24-26 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 13 | g27-30 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g31-33 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g34-41 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 13 | g37-39 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g40-41 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g42-44 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 13 | g56-56 | 🗑️ dropped | 0.74 | D:0 |
| IFRS 13 | g61-66 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g67-69 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g72-90 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g76-80 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g81-85 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g86-90 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g9-10 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB15-B17 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | gB2-B2 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | gB31-B33 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB34-B34 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB37-B47 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | gB4-B4 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 13 | gB43-B44 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB45-B47 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.1.1-5.1.3 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🔎 secondary | — | D:0 |
| IFRS 9 | g6.4.1-6.4.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.1-6.5.16 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.15-6.5.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.16-6.5.16 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 9 | gB5.1.1-B5.1.2A | 🗑️ dropped | 0.63-0.64 | D:0 |
| IFRS 9 | gB5.2.1-B5.2.2A | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.4.8-B5.4.8 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 9 | gB6.5.1-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.22-B6.5.28 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.29-B6.5.33 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.34-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.4-B6.5.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.7-B6.5.21 | 🗑️ dropped | — | D:0 |
| IFRS 9 | sgB5.2.3-B5.2.6 | 🗑️ dropped | 0.64 | D:0 |
| IAS 39 | g102-102 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g81-81A | 🗑️ dropped | 0.64 | D:0 |
| IAS 39 | g83-84 | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | g85-102 | 🗑️ dropped | 0.63 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | 0.60-0.62 | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.62 | D:0 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | 0.64 | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | 0.59-0.61 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:0 |
| IAS 41 | g10-33 | 🖼️ peripheral | 0.54-0.55 | D:0 |
| IAS 41 | g26-29 | 🖼️ peripheral | 0.55 | D:0 |
| IAS 41 | g30-33 | 🗑️ dropped | 0.54-0.58 | D:0 |
| IAS 41 | g40-53 | 🗑️ dropped | 0.54 | D:0 |
| IAS 41 | g54-56 | 🗑️ dropped | 0.54 | D:0 |
| IAS 41 | g8-9 | 🖼️ peripheral | 0.55 | D:0 |

### Q5.0 / 1

- Question: Le risque de défaut de la contrepartie doit-il être pris en compte dans l'évaluation de la juste valeur d'un actif ou d'un passif ?
- Embedded question: Le risque de défaut de la contrepartie doit-il être pris en compte dans l'évaluation de la juste valeur d'un actif ou d'un passif ?
fair value

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 13 | g1-4 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g11-14 | 🗑️ dropped | 0.68 | D:0 |
| IFRS 13 | g15-21 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | g22-23 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g24-26 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 13 | g27-30 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g31-33 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g34-41 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 13 | g37-39 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g40-41 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g42-44 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 13 | g56-56 | 🎯 authoritative | 0.74 | D:0 |
| IFRS 13 | g61-66 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g67-69 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g72-90 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g76-80 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g81-85 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g86-90 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g9-10 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB15-B17 | 🎯 authoritative | 0.66 | D:0 |
| IFRS 13 | gB2-B2 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | gB31-B33 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB34-B34 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB37-B47 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | gB4-B4 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 13 | gB43-B44 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB45-B47 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.1.1-5.1.3 | 🔎 secondary | 0.64 | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🔎 secondary | — | D:0 |
| IFRS 9 | g6.4.1-6.4.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.1-6.5.16 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.15-6.5.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.16-6.5.16 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 9 | gB5.1.1-B5.1.2A | 🔎 secondary | 0.63-0.64 | D:0 |
| IFRS 9 | gB5.2.1-B5.2.2A | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.4.8-B5.4.8 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 9 | gB6.5.1-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.22-B6.5.28 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.29-B6.5.33 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.34-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.4-B6.5.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.7-B6.5.21 | 🗑️ dropped | — | D:0 |
| IFRS 9 | sgB5.2.3-B5.2.6 | 🗑️ dropped | 0.64 | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | 0.64 | D:0 |
| IAS 39 | g83-84 | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | g85-102 | 🗑️ dropped | 0.63 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | 0.60-0.62 | D:0 |
| IAS 39 | g95-101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.62 | D:0 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | 0.64 | D:0 |
| IAS 39 | gAG114-AG132 | 🖼️ peripheral | 0.59-0.61 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:0 |
| IAS 41 | g10-33 | 🖼️ peripheral | 0.54-0.55 | D:0 |
| IAS 41 | g26-29 | 🗑️ dropped | 0.55 | D:0 |
| IAS 41 | g30-33 | 🖼️ peripheral | 0.54-0.58 | D:0 |
| IAS 41 | g40-53 | 🗑️ dropped | 0.54 | D:0 |
| IAS 41 | g54-56 | 🗑️ dropped | 0.54 | D:0 |
| IAS 41 | g8-9 | 🖼️ peripheral | 0.55 | D:0 |

### Q5.1 / 0

- Question: Lorsqu’une entité évalue un actif ou un passif à la juste valeur, doit-elle intégrer le risque de défaut de la contrepartie dans cette évaluation ?
- Embedded question: Lorsqu’une entité évalue un actif ou un passif à la juste valeur, doit-elle intégrer le risque de défaut de la contrepartie dans cette évaluation ?
fair value

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 13 | g1-4 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g11-14 | 🗑️ dropped | 0.71 | D:0 |
| IFRS 13 | g15-21 | 🗑️ dropped | 0.69 | D:0 |
| IFRS 13 | g22-23 | 🎯 authoritative | 0.70 | D:0 |
| IFRS 13 | g24-26 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 13 | g27-30 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g31-33 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g34-41 | 🔎 secondary | 0.68 | D:0 |
| IFRS 13 | g37-39 | 🔎 secondary | — | D:0 |
| IFRS 13 | g40-41 | 🔎 secondary | — | D:0 |
| IFRS 13 | g42-44 | 🎯 authoritative | 0.70 | D:0 |
| IFRS 13 | g48-56 | 🔎 secondary | 0.69 | D:0 |
| IFRS 13 | g53-55 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g56-56 | 🔎 secondary | 0.75 | D:0 |
| IFRS 13 | g61-66 | 🔎 secondary | — | D:0 |
| IFRS 13 | g67-69 | 🔎 secondary | — | D:0 |
| IFRS 13 | g72-90 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g76-80 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g81-85 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g86-90 | 🔎 secondary | 0.69 | D:0 |
| IFRS 13 | g9-10 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB2-B2 | 🗑️ dropped | 0.68 | D:0 |
| IFRS 13 | gB37-B47 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB43-B44 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB45-B47 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.1.1-5.1.3 | 🖼️ peripheral | 0.69 | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | 0.68 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g6.4.1-6.4.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | 0.66-0.67 | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | 0.70 | D:0 |
| IFRS 9 | gB5.1.1-B5.1.2A | 🖼️ peripheral | 0.66 | D:0 |
| IFRS 9 | gB5.4.8-B5.4.8 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | 0.66-0.67 | D:0 |
| IFRS 9 | sgB5.2.3-B5.2.6 | 🗑️ dropped | 0.66-0.66 | D:0 |
| IAS 8 | g31A-31I | 🖼️ peripheral | 0.56-0.60 | D:0 |
| IAS 8 | g32-40 | 🖼️ peripheral | 0.55 | D:0 |
| IAS 8 | g34-40 | 🖼️ peripheral | — | D:0 |
| IAS 8 | g36-38 | 🗑️ dropped | 0.58 | D:0 |
| IAS 8 | g39-40-L3 | 🗑️ dropped | — | D:0 |
| IAS 8 | g41-49 | 🗑️ dropped | 0.55 | D:0 |
| IAS 8 | g43-48 | 🗑️ dropped | — | D:0 |
| IAS 8 | g49-49 | 🗑️ dropped | — | D:0 |
| IAS 8 | g50-53 | 🗑️ dropped | — | D:0 |
| IAS 8 | g54-54G | 🗑️ dropped | 0.56 | D:0 |
| IAS 8 | g6A-6J | 🗑️ dropped | 0.57-0.58 | D:0 |
| IAS 40 | g16-19A | 🗑️ dropped | — | D:0 |
| IAS 40 | g20-29A | 🗑️ dropped | 0.65 | D:0 |
| IAS 40 | g30-32C | 🖼️ peripheral | 0.65-0.66 | D:0 |
| IAS 40 | g33-55 | 🖼️ peripheral | 0.64-0.67 | D:0 |
| IAS 40 | g53-55 | 🖼️ peripheral | 0.64 | D:0 |
| IAS 40 | g56-56 | 🗑️ dropped | — | D:0 |
| IAS 40 | g57-65 | 🗑️ dropped | 0.64 | D:0 |
| IAS 40 | g66-73 | 🗑️ dropped | 0.64 | D:0 |
| IAS 40 | g76-78 | 🗑️ dropped | 0.64 | D:0 |
| IAS 40 | g79-79 | 🗑️ dropped | — | D:0 |

### Q5.1 / 1

- Question: Lorsqu’une entité évalue un actif ou un passif à la juste valeur, doit-elle intégrer le risque de défaut de la contrepartie dans cette évaluation ?
- Embedded question: Lorsqu’une entité évalue un actif ou un passif à la juste valeur, doit-elle intégrer le risque de défaut de la contrepartie dans cette évaluation ?
fair value

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 13 | g1-4 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g11-14 | 🗑️ dropped | 0.71 | D:0 |
| IFRS 13 | g15-21 | 🗑️ dropped | 0.69 | D:0 |
| IFRS 13 | g22-23 | 🎯 authoritative | 0.70 | D:0 |
| IFRS 13 | g24-26 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 13 | g27-30 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g31-33 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g34-41 | 🗑️ dropped | 0.68 | D:0 |
| IFRS 13 | g37-39 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g40-41 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g42-44 | 🎯 authoritative | 0.70 | D:0 |
| IFRS 13 | g48-56 | 🗑️ dropped | 0.69 | D:0 |
| IFRS 13 | g53-55 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g56-56 | 🗑️ dropped | 0.75 | D:0 |
| IFRS 13 | g61-66 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g67-69 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g72-90 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g76-80 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g81-85 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g86-90 | 🗑️ dropped | 0.69 | D:0 |
| IFRS 13 | g9-10 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB2-B2 | 🗑️ dropped | 0.68 | D:0 |
| IFRS 13 | gB37-B47 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB43-B44 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB45-B47 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.1.1-5.1.3 | 🔎 secondary | 0.69 | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | 0.68 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🔎 secondary | — | D:0 |
| IFRS 9 | g6.4.1-6.4.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | 0.66-0.67 | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | 0.70 | D:0 |
| IFRS 9 | gB5.1.1-B5.1.2A | 🔎 secondary | 0.66 | D:0 |
| IFRS 9 | gB5.4.8-B5.4.8 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | 0.66-0.67 | D:0 |
| IFRS 9 | sgB5.2.3-B5.2.6 | 🗑️ dropped | 0.66-0.66 | D:0 |
| IAS 8 | g31A-31I | 🖼️ peripheral | 0.56-0.60 | D:0 |
| IAS 8 | g32-40 | 🖼️ peripheral | 0.55 | D:0 |
| IAS 8 | g34-40 | 🖼️ peripheral | — | D:0 |
| IAS 8 | g36-38 | 🗑️ dropped | 0.58 | D:0 |
| IAS 8 | g39-40-L3 | 🗑️ dropped | — | D:0 |
| IAS 8 | g41-49 | 🗑️ dropped | 0.55 | D:0 |
| IAS 8 | g43-48 | 🗑️ dropped | — | D:0 |
| IAS 8 | g49-49 | 🗑️ dropped | — | D:0 |
| IAS 8 | g50-53 | 🗑️ dropped | — | D:0 |
| IAS 8 | g54-54G | 🗑️ dropped | 0.56 | D:0 |
| IAS 8 | g6A-6J | 🗑️ dropped | 0.57-0.58 | D:0 |
| IAS 40 | g16-19A | 🗑️ dropped | — | D:0 |
| IAS 40 | g20-29A | 🗑️ dropped | 0.65 | D:0 |
| IAS 40 | g30-32C | 🖼️ peripheral | 0.65-0.66 | D:0 |
| IAS 40 | g33-55 | 🖼️ peripheral | 0.64-0.67 | D:0 |
| IAS 40 | g53-55 | 🗑️ dropped | 0.64 | D:0 |
| IAS 40 | g56-56 | 🗑️ dropped | — | D:0 |
| IAS 40 | g57-65 | 🗑️ dropped | 0.64 | D:0 |
| IAS 40 | g66-73 | 🗑️ dropped | 0.64 | D:0 |
| IAS 40 | g76-78 | 🗑️ dropped | 0.64 | D:0 |
| IAS 40 | g79-79 | 🗑️ dropped | — | D:0 |

### Q5.2 / 0

- Question: La juste valeur d’un instrument est déterminée dans une perspective de marché. Dans ce cadre, le risque de non-exécution ou de défaut de la contrepartie doit-il être reflété pour un actif comme pour un passif ?
- Embedded question: La juste valeur d’un instrument est déterminée dans une perspective de marché. Dans ce cadre, le risque de non-exécution ou de défaut de la contrepartie doit-il être reflété pour un actif comme pour un passif ?
fair value

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 13 | g1-4 | 🎯 authoritative | 0.73-0.74 | D:0 |
| IFRS 13 | g11-14 | 🗑️ dropped | 0.73 | D:0 |
| IFRS 13 | g15-21 | 🎯 authoritative | 0.73-0.74 | D:0 |
| IFRS 13 | g22-23 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g24-26 | 🎯 authoritative | 0.73 | D:0 |
| IFRS 13 | g27-30 | 🗑️ dropped | 0.74 | D:0 |
| IFRS 13 | g31-33 | 🗑️ dropped | 0.72 | D:0 |
| IFRS 13 | g61-66 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g67-69 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g72-90 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g76-80 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g81-85 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g86-90 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g9-10 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB15-B17 | 🎯 authoritative | 0.73 | D:0 |
| IFRS 13 | gB2-B2 | 🎯 authoritative | 0.73 | D:0 |
| IFRS 13 | gB3-B3 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB31-B33 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.1.1-5.1.3 | 🔎 secondary | — | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🔎 secondary | — | D:0 |
| IFRS 9 | g6.2.1-6.2.3 | 🗑️ dropped | 0.68 | D:0 |
| IFRS 9 | g6.4.1-6.4.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.1-6.5.16 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.15-6.5.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.16-6.5.16 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 9 | gB5.1.1-B5.1.2A | 🔎 secondary | 0.67-0.71 | D:0 |
| IFRS 9 | gB5.2.1-B5.2.2A | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 9 | gB6.2.1-B6.2.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.2.4-B6.2.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.1-B6.5.39 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 9 | gB6.5.22-B6.5.28 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.29-B6.5.33 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.34-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.4-B6.5.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.7-B6.5.21 | 🗑️ dropped | — | D:0 |
| IFRS 9 | sgB5.2.3-B5.2.6 | 🗑️ dropped | 0.72 | D:0 |
| IAS 8 | g31A-31I | 🖼️ peripheral | 0.56-0.59 | D:0 |
| IAS 8 | g32-40 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 8 | g34-40 | 🖼️ peripheral | — | D:0 |
| IAS 8 | g36-38 | 🖼️ peripheral | 0.55 | D:0 |
| IAS 8 | g39-40-L3 | 🗑️ dropped | — | D:0 |
| IAS 8 | g50-53 | 🗑️ dropped | 0.53 | D:0 |
| IAS 8 | g6A-6J | 🗑️ dropped | 0.58-0.60 | D:0 |
| IAS 8 | g7-12 | 🖼️ peripheral | 0.53-0.54 | D:0 |
| IAS 26 | g17-31 | 🗑️ dropped | 0.53-0.54 | D:0 |
| IAS 26 | g23-26 | 🗑️ dropped | 0.53-0.55 | D:0 |
| IAS 26 | g27-27 | 🗑️ dropped | — | D:0 |
| IAS 26 | g28-31 | 🗑️ dropped | 0.54 | D:0 |
| IAS 26 | g32-33 | 🖼️ peripheral | 0.54-0.72 | D:0 |
| IFRIC 17 | g11-13 | 🖼️ peripheral | 0.59-0.59 | D:0 |
| IFRIC 17 | g14-14 | 🖼️ peripheral | 0.55 | D:0 |

### Q5.2 / 1

- Question: La juste valeur d’un instrument est déterminée dans une perspective de marché. Dans ce cadre, le risque de non-exécution ou de défaut de la contrepartie doit-il être reflété pour un actif comme pour un passif ?
- Embedded question: La juste valeur d’un instrument est déterminée dans une perspective de marché. Dans ce cadre, le risque de non-exécution ou de défaut de la contrepartie doit-il être reflété pour un actif comme pour un passif ?
fair value

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 13 | g1-4 | 🎯 authoritative | 0.73-0.74 | D:0 |
| IFRS 13 | g11-14 | 🗑️ dropped | 0.73 | D:0 |
| IFRS 13 | g15-21 | 🎯 authoritative | 0.73-0.74 | D:0 |
| IFRS 13 | g22-23 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g24-26 | 🎯 authoritative | 0.73 | D:0 |
| IFRS 13 | g27-30 | 🗑️ dropped | 0.74 | D:0 |
| IFRS 13 | g31-33 | 🗑️ dropped | 0.72 | D:0 |
| IFRS 13 | g61-66 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g67-69 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g72-90 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g76-80 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g81-85 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g86-90 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g9-10 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB15-B17 | 🎯 authoritative | 0.73 | D:0 |
| IFRS 13 | gB2-B2 | 🗑️ dropped | 0.73 | D:0 |
| IFRS 13 | gB3-B3 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB31-B33 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.1.1-5.1.3 | 🔎 secondary | — | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.2.1-6.2.3 | 🗑️ dropped | 0.68 | D:0 |
| IFRS 9 | g6.4.1-6.4.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.1-6.5.16 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.15-6.5.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.16-6.5.16 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 9 | gB5.1.1-B5.1.2A | 🔎 secondary | 0.67-0.71 | D:0 |
| IFRS 9 | gB5.2.1-B5.2.2A | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 9 | gB6.2.1-B6.2.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.2.4-B6.2.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.1-B6.5.39 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 9 | gB6.5.22-B6.5.28 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.29-B6.5.33 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.34-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.4-B6.5.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.7-B6.5.21 | 🗑️ dropped | — | D:0 |
| IFRS 9 | sgB5.2.3-B5.2.6 | 🗑️ dropped | 0.72 | D:0 |
| IAS 8 | g31A-31I | 🖼️ peripheral | 0.56-0.59 | D:0 |
| IAS 8 | g32-40 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 8 | g34-40 | 🖼️ peripheral | — | D:0 |
| IAS 8 | g36-38 | 🖼️ peripheral | 0.55 | D:0 |
| IAS 8 | g39-40-L3 | 🗑️ dropped | — | D:0 |
| IAS 8 | g50-53 | 🗑️ dropped | 0.53 | D:0 |
| IAS 8 | g6A-6J | 🗑️ dropped | 0.58-0.60 | D:0 |
| IAS 8 | g7-12 | 🖼️ peripheral | 0.53-0.54 | D:0 |
| IAS 26 | g17-31 | 🗑️ dropped | 0.53-0.54 | D:0 |
| IAS 26 | g23-26 | 🗑️ dropped | 0.53-0.55 | D:0 |
| IAS 26 | g27-27 | 🗑️ dropped | — | D:0 |
| IAS 26 | g28-31 | 🗑️ dropped | 0.54 | D:0 |
| IAS 26 | g32-33 | 🖼️ peripheral | 0.54-0.72 | D:0 |
| IFRIC 17 | g11-13 | 🖼️ peripheral | 0.59-0.59 | D:0 |
| IFRIC 17 | g14-14 | 🖼️ peripheral | 0.55 | D:0 |

### Q5.3 / 0

- Question: Comment le risque de crédit de la contrepartie intervient-il dans la mesure de la juste valeur d’un actif ou d’un passif selon les IFRS ?
- Embedded question: Comment le risque de crédit de la contrepartie intervient-il dans la mesure de la juste valeur d’un actif ou d’un passif selon les IFRS ?
fair value

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 13 | g1-4 | 🎯 authoritative | 0.64 | D:0 |
| IFRS 13 | g11-14 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g15-21 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 13 | g22-23 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g24-26 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 13 | g37-39 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g42-44 | 🎯 authoritative | 0.67-0.68 | D:0 |
| IFRS 13 | g48-56 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 13 | g53-55 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g56-56 | 🎯 authoritative | 0.72 | D:0 |
| IFRS 13 | g61-66 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g86-90 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g9-10 | 🎯 authoritative | 0.70 | D:0 |
| IFRS 13 | gB13-B30 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 13 | gB14-B14 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB15-B17 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB18-B22 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB23-B30 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB31-B33 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB43-B44 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.3.3-4.3.7 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🔎 secondary | 0.63 | D:0 |
| IFRS 9 | g6.5.1-6.5.16 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.15-6.5.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.16-6.5.16 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 9 | gB5.1.1-B5.1.2A | 🗑️ dropped | 0.66 | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🔎 secondary | 0.62 | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🔎 secondary | 0.62-0.63 | D:0 |
| IFRS 9 | gB6.5.1-B6.5.39 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 9 | gB6.5.22-B6.5.28 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.29-B6.5.33 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.34-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.4-B6.5.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.7-B6.5.21 | 🗑️ dropped | — | D:0 |
| IAS 36 | g117-121 | 🗑️ dropped | 0.55-0.59 | D:0 |
| IAS 36 | g18-57 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 36 | g2-5 | 🗑️ dropped | 0.56 | D:0 |
| IAS 36 | g24-24 | 🗑️ dropped | — | D:0 |
| IAS 36 | g25-29 | 🗑️ dropped | — | D:0 |
| IAS 36 | g30-57 | 🖼️ peripheral | — | D:0 |
| IAS 36 | g33-38 | 🗑️ dropped | — | D:0 |
| IAS 36 | g39-53A | 🖼️ peripheral | 0.61 | D:0 |
| IAS 36 | g54-54 | 🗑️ dropped | — | D:0 |
| IAS 36 | g55-57 | 🖼️ peripheral | 0.60 | D:0 |
| IAS 36 | g58-64 | 🗑️ dropped | — | D:0 |
| IAS 36 | gA15-A21 | 🗑️ dropped | 0.55-0.56 | D:0 |
| IAS 36 | gA4-A6 | 🗑️ dropped | 0.55 | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | 0.60-0.64 | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | 0.63 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | 0.61-0.61 | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🖼️ peripheral | 0.66 | D:0 |
| IAS 39 | gAG105-AG113A | 🖼️ peripheral | 0.63 | D:0 |
| IAS 39 | gAG114-AG132 | 🖼️ peripheral | 0.60-0.64 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:0 |

### Q5.3 / 1

- Question: Comment le risque de crédit de la contrepartie intervient-il dans la mesure de la juste valeur d’un actif ou d’un passif selon les IFRS ?
- Embedded question: Comment le risque de crédit de la contrepartie intervient-il dans la mesure de la juste valeur d’un actif ou d’un passif selon les IFRS ?
fair value

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 13 | g1-4 | 🎯 authoritative | 0.64 | D:0 |
| IFRS 13 | g11-14 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g15-21 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 13 | g22-23 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g24-26 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 13 | g37-39 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g42-44 | 🎯 authoritative | 0.67-0.68 | D:0 |
| IFRS 13 | g48-56 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 13 | g53-55 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g56-56 | 🎯 authoritative | 0.72 | D:0 |
| IFRS 13 | g61-66 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g86-90 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g9-10 | 🎯 authoritative | 0.70 | D:0 |
| IFRS 13 | gB13-B30 | 🎯 authoritative | 0.65 | D:0 |
| IFRS 13 | gB14-B14 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB15-B17 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB18-B22 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB23-B30 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB31-B33 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB43-B44 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.3.3-4.3.7 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🔎 secondary | 0.63 | D:0 |
| IFRS 9 | g6.5.1-6.5.16 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.15-6.5.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.16-6.5.16 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 9 | gB5.1.1-B5.1.2A | 🗑️ dropped | 0.66 | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🔎 secondary | 0.62 | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🔎 secondary | 0.62-0.63 | D:0 |
| IFRS 9 | gB6.5.1-B6.5.39 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 9 | gB6.5.22-B6.5.28 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.29-B6.5.33 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.34-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.4-B6.5.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.7-B6.5.21 | 🗑️ dropped | — | D:0 |
| IAS 36 | g117-121 | 🗑️ dropped | 0.55-0.59 | D:0 |
| IAS 36 | g18-57 | 🖼️ peripheral | 0.57 | D:0 |
| IAS 36 | g2-5 | 🗑️ dropped | 0.56 | D:0 |
| IAS 36 | g24-24 | 🗑️ dropped | — | D:0 |
| IAS 36 | g25-29 | 🗑️ dropped | — | D:0 |
| IAS 36 | g30-57 | 🖼️ peripheral | — | D:0 |
| IAS 36 | g33-38 | 🗑️ dropped | — | D:0 |
| IAS 36 | g39-53A | 🖼️ peripheral | 0.61 | D:0 |
| IAS 36 | g54-54 | 🗑️ dropped | — | D:0 |
| IAS 36 | g55-57 | 🖼️ peripheral | 0.60 | D:0 |
| IAS 36 | g58-64 | 🗑️ dropped | — | D:0 |
| IAS 36 | gA15-A21 | 🗑️ dropped | 0.55-0.56 | D:0 |
| IAS 36 | gA4-A6 | 🗑️ dropped | 0.55 | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:1 |
| IAS 39 | g81-81A | 🗑️ dropped | 0.60-0.64 | D:2 |
| IAS 39 | g85-102 | 🗑️ dropped | 0.63 | D:8 |
| IAS 39 | g89-94 | 🗑️ dropped | 0.61-0.61 | D:7 |
| IAS 39 | g95-101 | 🗑️ dropped | — | D:7 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:1 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.66 | D:3 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | 0.63 | D:13 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | 0.60-0.64 | D:19 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:2 |

Dropped chunks:

- IAS 39 / g102-102 / 102 / dropped
- IAS 39 / g81-81A / 81 / dropped
- IAS 39 / g81-81A / 81A / dropped
- IAS 39 / g85-102 / 85 / dropped
- IAS 39 / g85-102 / 86 / dropped
- IAS 39 / g85-102 / 87 / dropped
- IAS 39 / g85-102 / 88 / dropped
- IAS 39 / g85-102 / E6 / dropped
- IAS 39 / g85-102 / E7 / dropped
- IAS 39 / g85-102 / E8 / dropped
- IAS 39 / g85-102 / E9 / dropped
- IAS 39 / g89-94 / 89 / dropped
- IAS 39 / g89-94 / 89A / dropped
- IAS 39 / g89-94 / 90 / dropped
- IAS 39 / g89-94 / 91 / dropped
- IAS 39 / g89-94 / 92 / dropped
- IAS 39 / g89-94 / 93 / dropped
- IAS 39 / g89-94 / 94 / dropped
- IAS 39 / g95-101 / 95 / dropped
- IAS 39 / g95-101 / 96 / dropped
- IAS 39 / g95-101 / 97 / dropped
- IAS 39 / g95-101 / 98 / dropped
- IAS 39 / g95-101 / 99 / dropped
- IAS 39 / g95-101 / 100 / dropped
- IAS 39 / g95-101 / 101 / dropped
- IAS 39 / gAG101-AG101 / AG101 / dropped
- IAS 39 / gAG102-AG132 / AG102 / dropped
- IAS 39 / gAG102-AG132 / AG103 / dropped
- IAS 39 / gAG102-AG132 / AG104 / dropped
- IAS 39 / gAG105-AG113A / AG105 / dropped
- IAS 39 / gAG105-AG113A / AG106 / dropped
- IAS 39 / gAG105-AG113A / AG107 / dropped
- IAS 39 / gAG105-AG113A / AG107A / dropped
- IAS 39 / gAG105-AG113A / AG108 / dropped
- IAS 39 / gAG105-AG113A / AG109 / dropped
- IAS 39 / gAG105-AG113A / AG110 / dropped
- IAS 39 / gAG105-AG113A / AG110A / dropped
- IAS 39 / gAG105-AG113A / AG110B / dropped
- IAS 39 / gAG105-AG113A / AG111 / dropped
- IAS 39 / gAG105-AG113A / AG112 / dropped
- IAS 39 / gAG105-AG113A / AG113 / dropped
- IAS 39 / gAG105-AG113A / AG113A / dropped
- IAS 39 / gAG114-AG132 / AG114 / dropped
- IAS 39 / gAG114-AG132 / AG115 / dropped
- IAS 39 / gAG114-AG132 / AG116 / dropped
- IAS 39 / gAG114-AG132 / AG117 / dropped
- IAS 39 / gAG114-AG132 / AG118 / dropped
- IAS 39 / gAG114-AG132 / AG119 / dropped
- IAS 39 / gAG114-AG132 / AG120 / dropped
- IAS 39 / gAG114-AG132 / AG121 / dropped
- IAS 39 / gAG114-AG132 / AG122 / dropped
- IAS 39 / gAG114-AG132 / AG123 / dropped
- IAS 39 / gAG114-AG132 / AG124 / dropped
- IAS 39 / gAG114-AG132 / AG125 / dropped
- IAS 39 / gAG114-AG132 / AG126 / dropped
- IAS 39 / gAG114-AG132 / AG127 / dropped
- IAS 39 / gAG114-AG132 / AG128 / dropped
- IAS 39 / gAG114-AG132 / AG129 / dropped
- IAS 39 / gAG114-AG132 / AG130 / dropped
- IAS 39 / gAG114-AG132 / AG131 / dropped
- IAS 39 / gAG114-AG132 / AG132 / dropped
- IAS 39 / gAG99C-AG99D / AG99C / dropped
- IAS 39 / gAG99C-AG99D / AG99D / dropped

### Q5.4 / 0

- Question: Pour mesurer la juste valeur, faut-il ajuster l’évaluation afin de tenir compte de la possibilité que la contrepartie ne remplisse pas ses obligations ?
- Embedded question: Pour mesurer la juste valeur, faut-il ajuster l’évaluation afin de tenir compte de la possibilité que la contrepartie ne remplisse pas ses obligations ?
fair value

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 13 | g1-4 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 13 | g11-14 | 🗑️ dropped | 0.70 | D:0 |
| IFRS 13 | g15-21 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 13 | g22-23 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g24-26 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g27-30 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g31-33 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g34-41 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 13 | g37-39 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g40-41 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g42-44 | 🎯 authoritative | 0.69-0.73 | D:0 |
| IFRS 13 | g56-56 | 🎯 authoritative | 0.70 | D:0 |
| IFRS 13 | g61-66 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g67-69 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g72-90 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g76-80 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g81-85 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g86-90 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g9-10 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB15-B17 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 13 | gB2-B2 | 🎯 authoritative | 0.69 | D:0 |
| IFRS 13 | gB31-B33 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB37-B47 | 🗑️ dropped | 0.70 | D:0 |
| IFRS 13 | gB43-B44 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB45-B47 | 🗑️ dropped | — | D:0 |
| IAS 8 | g31A-31I | 🖼️ peripheral | 0.56-0.59 | D:0 |
| IAS 8 | g32-40 | 🖼️ peripheral | 0.56 | D:0 |
| IAS 8 | g34-40 | 🖼️ peripheral | — | D:0 |
| IAS 8 | g36-38 | 🗑️ dropped | 0.54 | D:0 |
| IAS 8 | g39-40-L3 | 🗑️ dropped | — | D:0 |
| IAS 8 | g50-53 | 🗑️ dropped | 0.53-0.55 | D:0 |
| IAS 8 | g54-54G | 🗑️ dropped | 0.56 | D:0 |
| IAS 8 | g6A-6J | 🗑️ dropped | 0.53-0.55 | D:0 |
| IAS 36 | g109-125 | 🗑️ dropped | 0.59 | D:0 |
| IAS 36 | g117-121 | 🗑️ dropped | — | D:0 |
| IAS 36 | g122-123 | 🗑️ dropped | — | D:0 |
| IAS 36 | g124-125 | 🗑️ dropped | — | D:0 |
| IAS 36 | g18-57 | 🖼️ peripheral | 0.58-0.65 | D:0 |
| IAS 36 | g24-24 | 🗑️ dropped | — | D:0 |
| IAS 36 | g25-29 | 🗑️ dropped | — | D:0 |
| IAS 36 | g30-57 | 🖼️ peripheral | — | D:0 |
| IAS 36 | g33-38 | 🗑️ dropped | — | D:0 |
| IAS 36 | g39-53A | 🖼️ peripheral | 0.62 | D:0 |
| IAS 36 | g54-54 | 🗑️ dropped | — | D:0 |
| IAS 36 | g55-57 | 🖼️ peripheral | — | D:0 |
| IAS 36 | g58-64 | 🗑️ dropped | — | D:0 |
| IAS 36 | g7-17 | 🗑️ dropped | 0.56-0.57 | D:0 |
| IAS 36 | g80-87 | 🗑️ dropped | 0.60 | D:0 |
| IAS 36 | g88-95 | 🗑️ dropped | — | D:0 |
| IAS 36 | g96-99 | 🗑️ dropped | — | D:0 |
| IAS 36 | gA15-A21 | 🗑️ dropped | 0.56-0.58 | D:0 |
| IAS 36 | gA4-A6 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 2 | g10-13A | 🖼️ peripheral | 0.64-0.66 | D:0 |
| IFRS 2 | g14-15 | 🗑️ dropped | — | D:0 |
| IFRS 2 | g16-18 | 🖼️ peripheral | 0.65 | D:0 |
| IFRS 2 | g19-21 | 🗑️ dropped | — | D:0 |
| IFRS 2 | g22-22 | 🗑️ dropped | — | D:0 |
| IFRS 2 | g23-23 | 🗑️ dropped | — | D:0 |
| IFRS 2 | g24-25 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 2 | g30-33D | 🖼️ peripheral | 0.63 | D:0 |
| IFRS 2 | g33A-33D | 🗑️ dropped | 0.66 | D:0 |
| IFRS 2 | g35-40 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 2 | gB1-B41 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB11-B15 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB16-B21 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB2-B3 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB22-B30 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB26-B26 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB27-B30 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB31-B36 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 2 | gB37-B37 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB38-B41 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB4-B10 | 🗑️ dropped | 0.64 | D:0 |

### Q5.4 / 1

- Question: Pour mesurer la juste valeur, faut-il ajuster l’évaluation afin de tenir compte de la possibilité que la contrepartie ne remplisse pas ses obligations ?
- Embedded question: Pour mesurer la juste valeur, faut-il ajuster l’évaluation afin de tenir compte de la possibilité que la contrepartie ne remplisse pas ses obligations ?
fair value

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 13 | g1-4 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 13 | g11-14 | 🗑️ dropped | 0.70 | D:0 |
| IFRS 13 | g15-21 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 13 | g22-23 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g24-26 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g27-30 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g31-33 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g34-41 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 13 | g37-39 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g40-41 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g42-44 | 🎯 authoritative | 0.69-0.73 | D:0 |
| IFRS 13 | g56-56 | 🗑️ dropped | 0.70 | D:0 |
| IFRS 13 | g61-66 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g67-69 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g72-90 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g76-80 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g81-85 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g86-90 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g9-10 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB15-B17 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 13 | gB2-B2 | 🗑️ dropped | 0.69 | D:0 |
| IFRS 13 | gB31-B33 | 🎯 authoritative | — | D:0 |
| IFRS 13 | gB37-B47 | 🗑️ dropped | 0.70 | D:0 |
| IFRS 13 | gB43-B44 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB45-B47 | 🗑️ dropped | — | D:0 |
| IAS 8 | g31A-31I | 🖼️ peripheral | 0.56-0.59 | D:0 |
| IAS 8 | g32-40 | 🖼️ peripheral | 0.56 | D:0 |
| IAS 8 | g34-40 | 🖼️ peripheral | — | D:0 |
| IAS 8 | g36-38 | 🖼️ peripheral | 0.54 | D:0 |
| IAS 8 | g39-40-L3 | 🗑️ dropped | — | D:0 |
| IAS 8 | g50-53 | 🗑️ dropped | 0.53-0.55 | D:0 |
| IAS 8 | g54-54G | 🗑️ dropped | 0.56 | D:0 |
| IAS 8 | g6A-6J | 🗑️ dropped | 0.53-0.55 | D:0 |
| IAS 36 | g109-125 | 🗑️ dropped | 0.59 | D:0 |
| IAS 36 | g117-121 | 🗑️ dropped | — | D:0 |
| IAS 36 | g122-123 | 🗑️ dropped | — | D:0 |
| IAS 36 | g124-125 | 🗑️ dropped | — | D:0 |
| IAS 36 | g18-57 | 🖼️ peripheral | 0.58-0.65 | D:0 |
| IAS 36 | g24-24 | 🗑️ dropped | — | D:0 |
| IAS 36 | g25-29 | 🗑️ dropped | — | D:0 |
| IAS 36 | g30-57 | 🖼️ peripheral | — | D:0 |
| IAS 36 | g33-38 | 🗑️ dropped | — | D:0 |
| IAS 36 | g39-53A | 🖼️ peripheral | 0.62 | D:0 |
| IAS 36 | g54-54 | 🗑️ dropped | — | D:0 |
| IAS 36 | g55-57 | 🖼️ peripheral | — | D:0 |
| IAS 36 | g58-64 | 🗑️ dropped | — | D:0 |
| IAS 36 | g7-17 | 🗑️ dropped | 0.56-0.57 | D:0 |
| IAS 36 | g80-87 | 🗑️ dropped | 0.60 | D:0 |
| IAS 36 | g88-95 | 🗑️ dropped | — | D:0 |
| IAS 36 | g96-99 | 🗑️ dropped | — | D:0 |
| IAS 36 | gA15-A21 | 🖼️ peripheral | 0.56-0.58 | D:0 |
| IAS 36 | gA4-A6 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 2 | g10-13A | 🖼️ peripheral | 0.64-0.66 | D:0 |
| IFRS 2 | g14-15 | 🗑️ dropped | — | D:0 |
| IFRS 2 | g16-18 | 🖼️ peripheral | 0.65 | D:0 |
| IFRS 2 | g19-21 | 🗑️ dropped | — | D:0 |
| IFRS 2 | g22-22 | 🗑️ dropped | — | D:0 |
| IFRS 2 | g23-23 | 🗑️ dropped | — | D:0 |
| IFRS 2 | g24-25 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 2 | g30-33D | 🖼️ peripheral | 0.63 | D:0 |
| IFRS 2 | g33A-33D | 🗑️ dropped | 0.66 | D:0 |
| IFRS 2 | g35-40 | 🖼️ peripheral | 0.67 | D:0 |
| IFRS 2 | gB1-B41 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB11-B15 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB16-B21 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB2-B3 | 🖼️ peripheral | — | D:0 |
| IFRS 2 | gB22-B30 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB26-B26 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB27-B30 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB31-B36 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 2 | gB37-B37 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB38-B41 | 🗑️ dropped | — | D:0 |
| IFRS 2 | gB4-B10 | 🖼️ peripheral | 0.64 | D:0 |

