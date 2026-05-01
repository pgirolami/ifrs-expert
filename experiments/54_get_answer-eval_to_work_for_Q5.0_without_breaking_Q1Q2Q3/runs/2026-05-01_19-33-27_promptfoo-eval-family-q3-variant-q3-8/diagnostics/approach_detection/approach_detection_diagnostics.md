# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `54_get_answer-eval_to_work_for_Q5.0_without_breaking_Q1Q2Q3`
- Run: `2026-05-01_19-33-27_promptfoo-eval-family-q3-variant-q3-8`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 2

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| amortised_cost | yes | 2/2 | 1 |
| fair_value_through_other_comprehensive_income | yes | 2/2 | 1 |
| fair_value_through_profit_or_loss | yes | 2/2 | 1 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q3.8 | 2 | 80.0 | 100.0 | 0 | 0 |

## Authority Categorization by Run

### Q3.8 / 0

- Question: Qu’entend-on par un actif financier générant exclusivement des paiements de principal et d’intérêts selon ses clauses contractuelles ?
- Embedded question: Qu’entend-on par un actif financier générant exclusivement des paiements de principal et d’intérêts selon ses clauses contractuelles ?
financial asset

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g3.2.1-3.2.23 | 🗑️ dropped | 0.62-0.62 | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.15-3.2.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.16-3.2.21 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.22-3.2.23 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.1-B3.2.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.16-B3.2.17 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.2-B3.2.3 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.1-B4.1.2B | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.63-0.66 | D:0 |
| IFRS 9 | gB4.1.2C-B4.1.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.27-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.4A-B4.1.4C | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.5-B4.1.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.63-0.65 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
| IAS 19 | g102-108 | 🗑️ dropped | — | D:0 |
| IAS 19 | g109-112 | 🗑️ dropped | — | D:0 |
| IAS 19 | g113-115 | 🖼️ peripheral | 0.63 | D:0 |
| IAS 19 | g116-119 | 🗑️ dropped | — | D:0 |
| IAS 19 | g120-130 | 🗑️ dropped | — | D:0 |
| IAS 19 | g122A-122A_V1 | 🗑️ dropped | — | D:0 |
| IAS 19 | g123-126 | 🗑️ dropped | 0.58-0.60 | D:0 |
| IAS 19 | g127-130 | 🗑️ dropped | 0.55 | D:0 |
| IAS 19 | g131-132 | 🖼️ peripheral | — | D:0 |
| IAS 19 | g133-133 | 🗑️ dropped | — | D:0 |
| IAS 19 | g134-134 | 🗑️ dropped | 0.55 | D:0 |
| IAS 19 | g135-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g139-139 | 🗑️ dropped | — | D:0 |
| IAS 19 | g140-144 | 🗑️ dropped | 0.56-0.57 | D:0 |
| IAS 19 | g145-147 | 🗑️ dropped | — | D:0 |
| IAS 19 | g148-148 | 🗑️ dropped | — | D:0 |
| IAS 19 | g149-150 | 🗑️ dropped | — | D:0 |
| IAS 19 | g151-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g155-157 | 🗑️ dropped | 0.56 | D:0 |
| IAS 19 | g55-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g56-60 | 🗑️ dropped | — | D:0 |
| IAS 19 | g61-62 | 🗑️ dropped | — | D:0 |
| IAS 19 | g63-65 | 🗑️ dropped | 0.57-0.59 | D:0 |
| IAS 19 | g66-70 | 🗑️ dropped | — | D:0 |
| IAS 19 | g67-69 | 🗑️ dropped | — | D:0 |
| IAS 19 | g70-70 | 🗑️ dropped | — | D:0 |
| IAS 19 | g75-80 | 🗑️ dropped | — | D:0 |
| IAS 19 | g81-82 | 🗑️ dropped | — | D:0 |
| IAS 19 | g83-86 | 🗑️ dropped | — | D:0 |
| IAS 19 | g87-98 | 🗑️ dropped | — | D:0 |
| IAS 19 | g99-112 | 🗑️ dropped | — | D:0 |
| IAS 32 | g11-14 | 🖼️ peripheral | 0.68 | D:0 |
| IAS 32 | g15-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🗑️ dropped | 0.64 | D:0 |
| IAS 32 | g21-24 | 🗑️ dropped | 0.64-0.66 | D:0 |
| IAS 32 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 32 | g26-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG15-AG19 | 🖼️ peripheral | 0.64-0.67 | D:0 |
| IAS 32 | gAG20-AG24 | 🗑️ dropped | 0.69 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🗑️ dropped | 0.66-0.66 | D:0 |
| IFRS 3 | g15-17 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 3 | g3-3 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g39-40 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | g43-44 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 3 | g54-58 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 3 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g56-56 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g57-57 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g58-58 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | gB12-B12D | 🗑️ dropped | 0.53 | D:0 |
| IFRS 3 | gB13-B18 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | 0.53 | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB63-B63 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB7A-B7C | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | sg22-23 | 🗑️ dropped | 0.57 | D:0 |
| IFRIC 12 | g1-3 | 🗑️ dropped | — | D:0 |
| IFRIC 12 | g12-13 | 🗑️ dropped | 0.53 | D:0 |
| IFRIC 12 | g15-19 | 🖼️ peripheral | 0.55-0.63 | D:0 |
| IFRIC 12 | g23-25 | 🖼️ peripheral | 0.56 | D:0 |
| IFRIC 12 | g26-26 | 🗑️ dropped | — | D:0 |
| IFRIC 12 | g4-9 | 🗑️ dropped | — | D:0 |

### Q3.8 / 1

- Question: Qu’entend-on par un actif financier générant exclusivement des paiements de principal et d’intérêts selon ses clauses contractuelles ?
- Embedded question: Qu’entend-on par un actif financier générant exclusivement des paiements de principal et d’intérêts selon ses clauses contractuelles ?
financial asset

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g3.2.1-3.2.23 | 🗑️ dropped | 0.62-0.62 | D:0 |
| IFRS 9 | g3.2.10-3.2.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.15-3.2.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.16-3.2.21 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g3.2.22-3.2.23 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🎯 authoritative | 0.67 | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.1-B3.2.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.16-B3.2.17 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB3.2.2-B3.2.3 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.1-B4.1.2B | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.10-B4.1.19 | 🎯 authoritative | 0.63-0.66 | D:0 |
| IFRS 9 | gB4.1.2C-B4.1.4 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.20-B4.1.26 | 🎯 authoritative | — | D:0 |
| IFRS 9 | gB4.1.27-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.33-B4.1.36 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.4A-B4.1.4C | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.5-B4.1.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB4.1.7-B4.1.26 | 🎯 authoritative | 0.63-0.65 | D:0 |
| IFRS 9 | gB4.1.9A-B4.1.9E | 🗑️ dropped | — | D:0 |
| IAS 19 | g102-108 | 🗑️ dropped | — | D:0 |
| IAS 19 | g109-112 | 🗑️ dropped | — | D:0 |
| IAS 19 | g113-115 | 🖼️ peripheral | 0.63 | D:0 |
| IAS 19 | g116-119 | 🗑️ dropped | — | D:0 |
| IAS 19 | g120-130 | 🗑️ dropped | — | D:0 |
| IAS 19 | g122A-122A_V1 | 🗑️ dropped | — | D:0 |
| IAS 19 | g123-126 | 🗑️ dropped | 0.58-0.60 | D:0 |
| IAS 19 | g127-130 | 🗑️ dropped | 0.55 | D:0 |
| IAS 19 | g131-132 | 🖼️ peripheral | — | D:0 |
| IAS 19 | g133-133 | 🗑️ dropped | — | D:0 |
| IAS 19 | g134-134 | 🗑️ dropped | 0.55 | D:0 |
| IAS 19 | g135-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g139-139 | 🗑️ dropped | — | D:0 |
| IAS 19 | g140-144 | 🗑️ dropped | 0.56-0.57 | D:0 |
| IAS 19 | g145-147 | 🗑️ dropped | — | D:0 |
| IAS 19 | g148-148 | 🗑️ dropped | — | D:0 |
| IAS 19 | g149-150 | 🗑️ dropped | — | D:0 |
| IAS 19 | g151-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g155-157 | 🗑️ dropped | 0.56 | D:0 |
| IAS 19 | g55-152 | 🗑️ dropped | — | D:0 |
| IAS 19 | g56-60 | 🗑️ dropped | — | D:0 |
| IAS 19 | g61-62 | 🗑️ dropped | — | D:0 |
| IAS 19 | g63-65 | 🗑️ dropped | 0.57-0.59 | D:0 |
| IAS 19 | g66-70 | 🗑️ dropped | — | D:0 |
| IAS 19 | g67-69 | 🗑️ dropped | — | D:0 |
| IAS 19 | g70-70 | 🗑️ dropped | — | D:0 |
| IAS 19 | g75-80 | 🗑️ dropped | — | D:0 |
| IAS 19 | g81-82 | 🗑️ dropped | — | D:0 |
| IAS 19 | g83-86 | 🗑️ dropped | — | D:0 |
| IAS 19 | g87-98 | 🗑️ dropped | — | D:0 |
| IAS 19 | g99-112 | 🗑️ dropped | — | D:0 |
| IAS 32 | g11-14 | 🔎 secondary | 0.68 | D:0 |
| IAS 32 | g15-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g16A-16B | 🗑️ dropped | — | D:0 |
| IAS 32 | g16C-16D | 🗑️ dropped | — | D:0 |
| IAS 32 | g16E-16F | 🗑️ dropped | — | D:0 |
| IAS 32 | g17-20 | 🗑️ dropped | 0.64 | D:0 |
| IAS 32 | g21-24 | 🗑️ dropped | 0.64-0.66 | D:0 |
| IAS 32 | g25-25 | 🗑️ dropped | — | D:0 |
| IAS 32 | g26-27 | 🗑️ dropped | — | D:0 |
| IAS 32 | g4-10 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG13-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14A-AG14D | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14E-AG14E | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14F-AG14I | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG14J-AG14J | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG15-AG19 | 🔎 secondary | 0.64-0.67 | D:0 |
| IAS 32 | gAG20-AG24 | 🗑️ dropped | 0.69 | D:0 |
| IAS 32 | gAG25-AG26 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG27-AG27 | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG29-AG29A | 🗑️ dropped | — | D:0 |
| IAS 32 | gAG3-AG12 | 🔎 secondary | 0.66-0.66 | D:0 |
| IFRS 3 | g15-17 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 3 | g3-3 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g39-40 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 3 | g43-44 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 3 | g54-58 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | g55-55 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g56-56 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g57-57 | 🗑️ dropped | — | D:0 |
| IFRS 3 | g58-58 | 🖼️ peripheral | — | D:0 |
| IFRS 3 | gB12-B12D | 🗑️ dropped | 0.53 | D:0 |
| IFRS 3 | gB13-B18 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | gB31-B40 | 🗑️ dropped | 0.53 | D:0 |
| IFRS 3 | gB35-B36 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB37-B40 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB63-B63 | 🗑️ dropped | — | D:0 |
| IFRS 3 | gB7A-B7C | 🗑️ dropped | 0.54 | D:0 |
| IFRS 3 | sg22-23 | 🗑️ dropped | 0.57 | D:0 |
| IFRIC 12 | g1-3 | 🗑️ dropped | — | D:0 |
| IFRIC 12 | g12-13 | 🗑️ dropped | 0.53 | D:0 |
| IFRIC 12 | g15-19 | 🖼️ peripheral | 0.55-0.63 | D:0 |
| IFRIC 12 | g23-25 | 🖼️ peripheral | 0.56 | D:0 |
| IFRIC 12 | g26-26 | 🗑️ dropped | — | D:0 |
| IFRIC 12 | g4-9 | 🗑️ dropped | — | D:0 |

