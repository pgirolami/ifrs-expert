# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `54_get_answer-eval_to_work_for_Q5.0_without_breaking_Q1Q2Q3`
- Run: `2026-05-01_19-08-15_promptfoo-eval-family-q1-variant-q1-4`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 2

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| cash_flow_hedge | yes | 2/2 | 1 |
| fair_value_hedge | yes | 2/2 | 1 |
| hedge_of_a_net_investment | no | 1/2 | 1 |
| hedge_of_a_net_investment_in_a_foreign_operation | yes | 1/2 | 1 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q1.4 | 2 | 82.5 | 82.5 | 1 | 1 |

## Authority Categorization by Run

### Q1.4 / 0

- Question: En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?
- Embedded question: En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?
hedge accounting
dividend
receivable
foreign currency
foreign exchange

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.1.1-6.1.3 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | g6.3.1-6.3.6 | 🎯 authoritative | 0.66-0.70 | D:0 |
| IFRS 9 | g6.3.7-6.3.7 | 🎯 authoritative | 0.62 | D:0 |
| IFRS 9 | g6.4.1-6.4.1 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g6.5.1-6.5.16 | 🎯 authoritative | 0.63 | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g6.5.15-6.5.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.16-6.5.16 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🎯 authoritative | — | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.3.1-B6.3.6 | 🗑️ dropped | 0.63-0.69 | D:0 |
| IFRS 9 | gB6.4.13-B6.4.19 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | gB6.5.1-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.22-B6.5.28 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.29-B6.5.33 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.34-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.4-B6.5.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.7-B6.5.21 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | g1-6 | 🗑️ dropped | 0.63-0.67 | D:0 |
| IFRIC 16 | g10-13 | 🔎 secondary | 0.64-0.68 | D:0 |
| IFRIC 16 | g14-15 | 🔎 secondary | 0.67 | D:0 |
| IFRIC 16 | g16-17 | 🔎 secondary | — | D:0 |
| IFRIC 16 | g7-8 | 🗑️ dropped | 0.65 | D:0 |
| IFRIC 16 | g9-9 | 🗑️ dropped | 0.66 | D:0 |
| IFRIC 16 | gAG10-AG12 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG13-AG15 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG2-AG2 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG3-AG6 | 🗑️ dropped | 0.63 | D:0 |
| IFRIC 16 | gAG7-AG7 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG9-AG15 | 🗑️ dropped | 0.62 | D:0 |
| IAS 21 | g15-15A | 🗑️ dropped | — | D:0 |
| IAS 21 | g17-19 | 🗑️ dropped | 0.59 | D:0 |
| IAS 21 | g20-22 | 🗑️ dropped | — | D:0 |
| IAS 21 | g23-26 | 🗑️ dropped | 0.61 | D:0 |
| IAS 21 | g27-34 | 🔎 secondary | 0.59-0.65 | D:0 |
| IAS 21 | g3-7 | 🗑️ dropped | 0.60 | D:0 |
| IAS 21 | g38-43 | 🗑️ dropped | 0.60 | D:0 |
| IAS 21 | g44-47 | 🔎 secondary | 0.63-0.71 | D:0 |
| IAS 21 | g48-49 | 🔎 secondary | 0.59 | D:0 |
| IAS 21 | g50-50 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | 0.61 | D:1 |
| IAS 39 | g103-108F | 🗑️ dropped | 0.62 | D:21 |
| IAS 39 | g72-73 | 🗑️ dropped | 0.66 | D:2 |
| IAS 39 | g74-77 | 🗑️ dropped | 0.62 | D:8 |
| IAS 39 | g78-80 | 🗑️ dropped | 0.72 | D:2 |
| IAS 39 | g85-102 | 🗑️ dropped | 0.62-0.63 | D:8 |
| IAS 39 | g89-94 | 🗑️ dropped | — | D:7 |
| IAS 39 | g95-101 | 🗑️ dropped | — | D:7 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | — | D:3 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | — | D:13 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | — | D:19 |
| IAS 39 | gAG133-AG133_V2 | 🗑️ dropped | 0.61 | D:1 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.67-0.68 | D:5 |
| IFRS 7 | g13A-13F | 🗑️ dropped | — | D:0 |
| IFRS 7 | g17-17 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 7 | g21A-24G | 🖼️ peripheral | 0.63 | D:0 |
| IFRS 7 | g22-22C | 🖼️ peripheral | — | D:0 |
| IFRS 7 | g23-23F | 🗑️ dropped | — | D:0 |
| IFRS 7 | g24-24F | 🖼️ peripheral | 0.60-0.63 | D:0 |
| IFRS 7 | g24G-24G | 🗑️ dropped | — | D:0 |
| IFRS 7 | g24H-24H | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42A-42S | 🗑️ dropped | 0.58 | D:0 |
| IFRS 7 | g42D-42D | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42E-42G | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42H-42S | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB29-B31 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 7 | gB33-B33 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 7 | gB51-B52 | 🗑️ dropped | 0.58 | D:0 |

Dropped chunks:

- IAS 39 / g102-102 / 102 / dropped
- IAS 39 / g103-108F / 103 / dropped
- IAS 39 / g103-108F / 103C / dropped
- IAS 39 / g103-108F / 103E / dropped
- IAS 39 / g103-108F / 103G / dropped
- IAS 39 / g103-108F / 103K / dropped
- IAS 39 / g103-108F / 103Q / dropped
- IAS 39 / g103-108F / 103R / dropped
- IAS 39 / g103-108F / 103T / dropped
- IAS 39 / g103-108F / 103U / dropped
- IAS 39 / g103-108F / 103V / dropped
- IAS 39 / g103-108F / 104 / dropped
- IAS 39 / g103-108F / 108 / dropped
- IAS 39 / g103-108F / 108A / dropped
- IAS 39 / g103-108F / 108B / dropped
- IAS 39 / g103-108F / 108C / dropped
- IAS 39 / g103-108F / 108D / dropped
- IAS 39 / g103-108F / 108G / dropped
- IAS 39 / g103-108F / 108H / dropped
- IAS 39 / g103-108F / 108I / dropped
- IAS 39 / g103-108F / 108J / dropped
- IAS 39 / g103-108F / 108K / dropped
- IAS 39 / g72-73 / 72 / dropped
- IAS 39 / g72-73 / 73 / dropped
- IAS 39 / g74-77 / 74 / dropped
- IAS 39 / g74-77 / 75 / dropped
- IAS 39 / g74-77 / 76 / dropped
- IAS 39 / g74-77 / 77 / dropped
- IAS 39 / g74-77 / E1 / dropped
- IAS 39 / g74-77 / E2 / dropped
- IAS 39 / g74-77 / E3 / dropped
- IAS 39 / g74-77 / E4 / dropped
- IAS 39 / g78-80 / 78 / dropped
- IAS 39 / g78-80 / 80 / dropped
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
- IAS 39 / gAG133-AG133_V2 / AG133 / dropped
- IAS 39 / gAG98-AG99BA / AG98 / dropped
- IAS 39 / gAG98-AG99BA / AG99 / dropped
- IAS 39 / gAG98-AG99BA / AG99A / dropped
- IAS 39 / gAG98-AG99BA / AG99B / dropped
- IAS 39 / gAG98-AG99BA / AG99BA / dropped

### Q1.4 / 1

- Question: En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?
- Embedded question: En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?
hedge accounting
dividend
receivable
foreign currency
foreign exchange

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.1.1-6.1.3 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | g6.3.1-6.3.6 | 🎯 authoritative | 0.66-0.70 | D:0 |
| IFRS 9 | g6.3.7-6.3.7 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | g6.4.1-6.4.1 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g6.5.1-6.5.16 | 🎯 authoritative | 0.63 | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.15-6.5.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.16-6.5.16 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.3.1-B6.3.6 | 🗑️ dropped | 0.63-0.69 | D:0 |
| IFRS 9 | gB6.4.13-B6.4.19 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | gB6.5.1-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.22-B6.5.28 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.29-B6.5.33 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.34-B6.5.39 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.4-B6.5.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.5.7-B6.5.21 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | g1-6 | 🗑️ dropped | 0.63-0.67 | D:0 |
| IFRIC 16 | g10-13 | 🔎 secondary | 0.64-0.68 | D:0 |
| IFRIC 16 | g14-15 | 🔎 secondary | 0.67 | D:0 |
| IFRIC 16 | g16-17 | 🔎 secondary | — | D:0 |
| IFRIC 16 | g7-8 | 🗑️ dropped | 0.65 | D:0 |
| IFRIC 16 | g9-9 | 🗑️ dropped | 0.66 | D:0 |
| IFRIC 16 | gAG10-AG12 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG13-AG15 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG2-AG2 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG3-AG6 | 🗑️ dropped | 0.63 | D:0 |
| IFRIC 16 | gAG7-AG7 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG9-AG15 | 🗑️ dropped | 0.62 | D:0 |
| IAS 21 | g15-15A | 🗑️ dropped | — | D:0 |
| IAS 21 | g17-19 | 🗑️ dropped | 0.59 | D:0 |
| IAS 21 | g20-22 | 🗑️ dropped | — | D:0 |
| IAS 21 | g23-26 | 🗑️ dropped | 0.61 | D:0 |
| IAS 21 | g27-34 | 🔎 secondary | 0.59-0.65 | D:0 |
| IAS 21 | g3-7 | 🗑️ dropped | 0.60 | D:0 |
| IAS 21 | g38-43 | 🗑️ dropped | 0.60 | D:0 |
| IAS 21 | g44-47 | 🔎 secondary | 0.63-0.71 | D:0 |
| IAS 21 | g48-49 | 🔎 secondary | 0.59 | D:0 |
| IAS 21 | g50-50 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | 0.61 | D:1 |
| IAS 39 | g103-108F | 🗑️ dropped | 0.62 | D:21 |
| IAS 39 | g72-73 | 🗑️ dropped | 0.66 | D:2 |
| IAS 39 | g74-77 | 🗑️ dropped | 0.62 | D:8 |
| IAS 39 | g78-80 | 🗑️ dropped | 0.72 | D:2 |
| IAS 39 | g85-102 | 🗑️ dropped | 0.62-0.63 | D:8 |
| IAS 39 | g89-94 | 🗑️ dropped | — | D:7 |
| IAS 39 | g95-101 | 🗑️ dropped | — | D:7 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | — | D:3 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | — | D:13 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | — | D:19 |
| IAS 39 | gAG133-AG133_V2 | 🗑️ dropped | 0.61 | D:1 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.67-0.68 | D:5 |
| IFRS 7 | g13A-13F | 🗑️ dropped | — | D:0 |
| IFRS 7 | g17-17 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 7 | g21A-24G | 🖼️ peripheral | 0.63 | D:0 |
| IFRS 7 | g22-22C | 🖼️ peripheral | — | D:0 |
| IFRS 7 | g23-23F | 🗑️ dropped | — | D:0 |
| IFRS 7 | g24-24F | 🖼️ peripheral | 0.60-0.63 | D:0 |
| IFRS 7 | g24G-24G | 🗑️ dropped | — | D:0 |
| IFRS 7 | g24H-24H | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42A-42S | 🗑️ dropped | 0.58 | D:0 |
| IFRS 7 | g42D-42D | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42E-42G | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42H-42S | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB29-B31 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 7 | gB33-B33 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 7 | gB51-B52 | 🗑️ dropped | 0.58 | D:0 |

Dropped chunks:

- IAS 39 / g102-102 / 102 / dropped
- IAS 39 / g103-108F / 103 / dropped
- IAS 39 / g103-108F / 103C / dropped
- IAS 39 / g103-108F / 103E / dropped
- IAS 39 / g103-108F / 103G / dropped
- IAS 39 / g103-108F / 103K / dropped
- IAS 39 / g103-108F / 103Q / dropped
- IAS 39 / g103-108F / 103R / dropped
- IAS 39 / g103-108F / 103T / dropped
- IAS 39 / g103-108F / 103U / dropped
- IAS 39 / g103-108F / 103V / dropped
- IAS 39 / g103-108F / 104 / dropped
- IAS 39 / g103-108F / 108 / dropped
- IAS 39 / g103-108F / 108A / dropped
- IAS 39 / g103-108F / 108B / dropped
- IAS 39 / g103-108F / 108C / dropped
- IAS 39 / g103-108F / 108D / dropped
- IAS 39 / g103-108F / 108G / dropped
- IAS 39 / g103-108F / 108H / dropped
- IAS 39 / g103-108F / 108I / dropped
- IAS 39 / g103-108F / 108J / dropped
- IAS 39 / g103-108F / 108K / dropped
- IAS 39 / g72-73 / 72 / dropped
- IAS 39 / g72-73 / 73 / dropped
- IAS 39 / g74-77 / 74 / dropped
- IAS 39 / g74-77 / 75 / dropped
- IAS 39 / g74-77 / 76 / dropped
- IAS 39 / g74-77 / 77 / dropped
- IAS 39 / g74-77 / E1 / dropped
- IAS 39 / g74-77 / E2 / dropped
- IAS 39 / g74-77 / E3 / dropped
- IAS 39 / g74-77 / E4 / dropped
- IAS 39 / g78-80 / 78 / dropped
- IAS 39 / g78-80 / 80 / dropped
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
- IAS 39 / gAG133-AG133_V2 / AG133 / dropped
- IAS 39 / gAG98-AG99BA / AG98 / dropped
- IAS 39 / gAG98-AG99BA / AG99 / dropped
- IAS 39 / gAG98-AG99BA / AG99A / dropped
- IAS 39 / gAG98-AG99BA / AG99B / dropped
- IAS 39 / gAG98-AG99BA / AG99BA / dropped

