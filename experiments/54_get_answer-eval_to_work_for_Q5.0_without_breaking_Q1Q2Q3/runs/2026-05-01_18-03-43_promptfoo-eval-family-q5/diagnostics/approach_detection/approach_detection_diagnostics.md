# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `54_get_answer-eval_to_work_for_Q5.0_without_breaking_Q1Q2Q3`
- Run: `2026-05-01_18-03-43_promptfoo-eval-family-q5`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 2

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| fair_value_measurement_of_a_liability | yes | 0/2 | 0 |
| fair_value_measurement_of_an_asset | yes | 0/2 | 0 |
| fair_value_measurement_of_assets | no | 1/2 | 1 |
| fair_value_measurement_of_liabilities | no | 1/2 | 1 |
| fair_value_of_a_liability | no | 1/2 | 1 |
| fair_value_of_an_asset | no | 1/2 | 1 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q5.0 | 2 | 35.0 | 35.0 | 4 | 4 |

## Authority Categorization by Run

### Q5.0 / 0

- Question: Le risque de défaut de la contrepartie doit-il être pris en compte dans l'évaluation de la juste valeur d'un actif ou d'un passif ?
- Embedded question: Le risque de défaut de la contrepartie doit-il être pris en compte dans l'évaluation de la juste valeur d'un actif ou d'un passif ?
fair value

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 13 | g1-4 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g11-14 | 🖼️ peripheral | 0.68 | D:0 |
| IFRS 13 | g15-21 | 🖼️ peripheral | 0.66 | D:0 |
| IFRS 13 | g22-23 | 🎯 authoritative | — | D:0 |
| IFRS 13 | g24-26 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 13 | g27-30 | 🖼️ peripheral | — | D:0 |
| IFRS 13 | g31-33 | 🖼️ peripheral | — | D:0 |
| IFRS 13 | g34-41 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 13 | g37-39 | 🔎 secondary | — | D:0 |
| IFRS 13 | g40-41 | 🔎 secondary | — | D:0 |
| IFRS 13 | g42-44 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 13 | g56-56 | 🔎 secondary | 0.74 | D:0 |
| IFRS 13 | g61-66 | 🔎 secondary | — | D:0 |
| IFRS 13 | g67-69 | 🔎 secondary | — | D:0 |
| IFRS 13 | g72-90 | 🖼️ peripheral | — | D:0 |
| IFRS 13 | g76-80 | 🖼️ peripheral | — | D:0 |
| IFRS 13 | g81-85 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g86-90 | 🔎 secondary | — | D:0 |
| IFRS 13 | g9-10 | 🖼️ peripheral | — | D:0 |
| IFRS 13 | gB15-B17 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | gB2-B2 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | gB31-B33 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB34-B34 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB37-B47 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | gB4-B4 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 13 | gB43-B44 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB45-B47 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102-102 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g81-81A | 🖼️ peripheral | 0.64 | D:0 |
| IAS 39 | g83-84 | 🖼️ peripheral | 0.59 | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | 0.63 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | 0.60-0.62 | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.62 | D:0 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | 0.64 | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | 0.59-0.61 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:0 |
| IAS 41 | g10-33 | 🖼️ peripheral | 0.54-0.55 | D:0 |
| IAS 41 | g26-29 | 🗑️ dropped | 0.55 | D:0 |
| IAS 41 | g30-33 | 🖼️ peripheral | 0.54-0.58 | D:0 |
| IAS 41 | g40-53 | 🗑️ dropped | 0.54 | D:0 |
| IAS 41 | g54-56 | 🗑️ dropped | 0.54 | D:0 |
| IAS 41 | g8-9 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.1.1-5.1.3 | 🖼️ peripheral | 0.64 | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🖼️ peripheral | — | D:0 |
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
| IFRS 9 | gB5.1.1-B5.1.2A | 🖼️ peripheral | 0.63-0.64 | D:0 |
| IFRS 9 | gB5.2.1-B5.2.2A | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.4.8-B5.4.8 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🔎 secondary | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 9 | gB6.5.1-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.22-B6.5.28 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.29-B6.5.33 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.34-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.4-B6.5.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.7-B6.5.21 | 🗑️ dropped | — | D:0 |
| IFRS 9 | sgB5.2.3-B5.2.6 | 🗑️ dropped | 0.64 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N115305FB4F52CB-EFL | 🗑️ dropped | 0.64 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N145305FB4F52CB-EFL | 🗑️ dropped | 0.66 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N2A5305FB4F52CB-EFL | 🗑️ dropped | 0.63 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N245305FB4F52CB-EFL | 🗑️ dropped | 0.65 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N355305FB4F52CB-EFL | 🗑️ dropped | 0.62 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N525305FB4F52CB-EFL | 🗑️ dropped | 0.62 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N815305FB4F52CB-EFL | 🔎 secondary | 0.81 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N9C5305FB4F52CB-EFL | 🔎 secondary | 0.67 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | NA75305FB4F52CB-EFL | 🔎 secondary | 0.66 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | NDD5305FB4F52CB-EFL | 🗑️ dropped | 0.63 | D:0 |

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
| IFRS 13 | g24-26 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 13 | g27-30 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g31-33 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g34-41 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 13 | g37-39 | 🔎 secondary | — | D:0 |
| IFRS 13 | g40-41 | 🔎 secondary | — | D:0 |
| IFRS 13 | g42-44 | 🎯 authoritative | 0.68 | D:0 |
| IFRS 13 | g56-56 | 🗑️ dropped | 0.74 | D:0 |
| IFRS 13 | g61-66 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g67-69 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g72-90 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g76-80 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g81-85 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g86-90 | 🗑️ dropped | — | D:0 |
| IFRS 13 | g9-10 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB15-B17 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | gB2-B2 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | gB31-B33 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB34-B34 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB37-B47 | 🗑️ dropped | 0.66 | D:0 |
| IFRS 13 | gB4-B4 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 13 | gB43-B44 | 🗑️ dropped | — | D:0 |
| IFRS 13 | gB45-B47 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g81-81A | 🗑️ dropped | 0.64 | D:0 |
| IAS 39 | g83-84 | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | g85-102 | 🗑️ dropped | 0.63 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | 0.60-0.62 | D:0 |
| IAS 39 | g95-101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.62 | D:0 |
| IAS 39 | gAG105-AG113A | 🖼️ peripheral | 0.64 | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | 0.59-0.61 | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:0 |
| IAS 41 | g10-33 | 🖼️ peripheral | 0.54-0.55 | D:0 |
| IAS 41 | g26-29 | 🗑️ dropped | 0.55 | D:0 |
| IAS 41 | g30-33 | 🗑️ dropped | 0.54-0.58 | D:0 |
| IAS 41 | g40-53 | 🗑️ dropped | 0.54 | D:0 |
| IAS 41 | g54-56 | 🗑️ dropped | 0.54 | D:0 |
| IAS 41 | g8-9 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.1.1-5.1.3 | 🗑️ dropped | 0.64 | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | 0.67 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🖼️ peripheral | — | D:0 |
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
| IFRS 9 | gB5.7.13-B5.7.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | 0.65 | D:0 |
| IFRS 9 | gB6.5.1-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.22-B6.5.28 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.29-B6.5.33 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.34-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.4-B6.5.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.7-B6.5.21 | 🗑️ dropped | — | D:0 |
| IFRS 9 | sgB5.2.3-B5.2.6 | 🗑️ dropped | 0.64 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N115305FB4F52CB-EFL | 🗑️ dropped | 0.64 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N145305FB4F52CB-EFL | 🗑️ dropped | 0.66 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N2A5305FB4F52CB-EFL | 🗑️ dropped | 0.63 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N245305FB4F52CB-EFL | 🗑️ dropped | 0.65 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N355305FB4F52CB-EFL | 🗑️ dropped | 0.62 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N525305FB4F52CB-EFL | 🗑️ dropped | 0.62 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N815305FB4F52CB-EFL | 🔎 secondary | 0.81 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | N9C5305FB4F52CB-EFL | 🔎 secondary | 0.67 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | NA75305FB4F52CB-EFL | 🔎 secondary | 0.66 | D:0 |
| NAVIS QRIFRS C 25305FB 4F 52CB EFL | NDD5305FB4F52CB-EFL | 🗑️ dropped | 0.63 | D:0 |

