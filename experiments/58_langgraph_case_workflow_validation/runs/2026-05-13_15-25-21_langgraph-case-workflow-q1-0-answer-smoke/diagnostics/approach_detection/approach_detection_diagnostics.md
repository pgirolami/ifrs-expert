# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `58_langgraph_case_workflow_validation`
- Run: `2026-05-13_15-25-21_langgraph-case-workflow-q1-0-answer-smoke`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 2

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| cash_flow_hedge | yes | 2/2 | 1 |
| fair_value_hedge | yes | 2/2 | 1 |
| hedge_of_a_net_investment | yes | 2/2 | 1 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q1.0 | 2 | 100.0 | 100.0 | 0 | 0 |

## Authority Categorization by Run

### Q1.0 / 0

- Question: Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?
- Embedded question: Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?
financial statements
hedge accounting
dividend
receivable
foreign currency
foreign exchange

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g5.2.1-5.2.3 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | g5.3.1-5.3.2 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.1.1-6.1.3 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g6.3.1-6.3.6 | 🎯 authoritative | 0.66-0.68 | D:0 |
| IFRS 9 | g6.4.1-6.4.1 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g6.5.1-6.5.16 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g6.5.15-6.5.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.16-6.5.16 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.2.1-B5.2.2A | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.3.1-B6.3.6 | 🗑️ dropped | 0.66-0.67 | D:0 |
| IFRS 9 | sgB5.2.3-B5.2.6 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | g1-6 | 🔎 secondary | 0.61-0.64 | D:0 |
| IFRIC 16 | g10-13 | 🔎 secondary | 0.62-0.65 | D:0 |
| IFRIC 16 | g14-15 | 🔎 secondary | 0.63 | D:0 |
| IFRIC 16 | g16-17 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | g7-8 | 🗑️ dropped | 0.63 | D:0 |
| IFRIC 16 | g9-9 | 🗑️ dropped | 0.62 | D:0 |
| IFRIC 16 | gAG10-AG12 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG13-AG15 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG2-AG2 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG3-AG6 | 🗑️ dropped | 0.61-0.61 | D:0 |
| IFRIC 16 | gAG7-AG7 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG9-AG15 | 🗑️ dropped | 0.61 | D:0 |
| IAS 21 | g15-15A | 🗑️ dropped | — | D:0 |
| IAS 21 | g17-19 | 🗑️ dropped | 0.61 | D:0 |
| IAS 21 | g20-22 | 🗑️ dropped | — | D:0 |
| IAS 21 | g23-26 | 🗑️ dropped | 0.63 | D:0 |
| IAS 21 | g27-34 | 🔎 secondary | 0.64-0.65 | D:0 |
| IAS 21 | g3-7 | 🔎 secondary | 0.61-0.65 | D:0 |
| IAS 21 | g38-43 | 🗑️ dropped | — | D:0 |
| IAS 21 | g44-47 | 🔎 secondary | 0.62-0.67 | D:0 |
| IAS 21 | g48-49 | 🗑️ dropped | — | D:0 |
| IAS 21 | g50-50 | 🗑️ dropped | — | D:0 |
| IAS 21 | g51-57 | 🗑️ dropped | — | D:0 |
| IAS 21 | g58-60K | 🗑️ dropped | 0.60 | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | 0.61 | D:1 |
| IAS 39 | g102A-102N | 🗑️ dropped | — | D:3 |
| IAS 39 | g102D-102D | 🗑️ dropped | — | D:1 |
| IAS 39 | g102E-102E | 🗑️ dropped | — | D:1 |
| IAS 39 | g102F-102G | 🗑️ dropped | — | D:2 |
| IAS 39 | g102H-102I | 🗑️ dropped | — | D:2 |
| IAS 39 | g102J-102O | 🗑️ dropped | — | D:6 |
| IAS 39 | g102P-102U | 🗑️ dropped | — | D:6 |
| IAS 39 | g102V-102V | 🗑️ dropped | — | D:1 |
| IAS 39 | g102W-102X | 🗑️ dropped | — | D:2 |
| IAS 39 | g102Y-102Z | 🗑️ dropped | — | D:2 |
| IAS 39 | g102Z1-102Z3 | 🗑️ dropped | — | D:3 |
| IAS 39 | g103-108F | 🗑️ dropped | 0.62 | D:21 |
| IAS 39 | g2-7 | 🗑️ dropped | 0.60 | D:1 |
| IAS 39 | g71-102 | 🗑️ dropped | — | D:1 |
| IAS 39 | g72-73 | 🗑️ dropped | 0.64 | D:2 |
| IAS 39 | g74-77 | 🗑️ dropped | 0.62 | D:8 |
| IAS 39 | g78-80 | 🗑️ dropped | 0.71 | D:2 |
| IAS 39 | g81-81A | 🗑️ dropped | — | D:2 |
| IAS 39 | g82-82 | 🗑️ dropped | — | D:2 |
| IAS 39 | g83-84 | 🗑️ dropped | — | D:2 |
| IAS 39 | g85-102 | 🗑️ dropped | 0.60 | D:8 |
| IAS 39 | g89-94 | 🗑️ dropped | — | D:7 |
| IAS 39 | g95-101 | 🗑️ dropped | — | D:7 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | — | D:13 |
| IAS 39 | gAG133-AG133_V2 | 🗑️ dropped | 0.61 | D:1 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.65-0.65 | D:5 |
| IFRS 7 | g13A-13F | 🗑️ dropped | — | D:0 |
| IFRS 7 | g21A-24G | 🖼️ peripheral | 0.62 | D:0 |
| IFRS 7 | g22-22C | 🗑️ dropped | — | D:0 |
| IFRS 7 | g23-23F | 🗑️ dropped | — | D:0 |
| IFRS 7 | g24-24F | 🖼️ peripheral | 0.59-0.63 | D:0 |
| IFRS 7 | g24G-24G | 🗑️ dropped | — | D:0 |
| IFRS 7 | g24H-24H | 🗑️ dropped | — | D:0 |
| IFRS 7 | g31-42 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g33-33 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g34-42 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35A-35E | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35A-38 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35F-35G | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35H-35L | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35M-35N | 🗑️ dropped | — | D:0 |
| IFRS 7 | g38-38 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g39-39 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g40-41 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42-42 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42A-42S | 🗑️ dropped | 0.60-0.60 | D:0 |
| IFRS 7 | g42D-42D | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42E-42G | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42H-42S | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB10A-B16 | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB17-B28 | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB22-B22 | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB23-B24 | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB25-B28 | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB29-B31 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 7 | gB33-B33 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 7 | gB51-B52 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 7 | gB6-B28 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 7 | gB7-B8 | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8A-B8C | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8D-B8E | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8F-B8G | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8H-B8J | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB9-B10 | 🗑️ dropped | — | D:0 |

Dropped chunks:

- IAS 39 / g102-102 / 102 / dropped
- IAS 39 / g102A-102N / 102A / dropped
- IAS 39 / g102A-102N / 102B / dropped
- IAS 39 / g102A-102N / 102C / dropped
- IAS 39 / g102D-102D / 102D / dropped
- IAS 39 / g102E-102E / 102E / dropped
- IAS 39 / g102F-102G / 102F / dropped
- IAS 39 / g102F-102G / 102G / dropped
- IAS 39 / g102H-102I / 102H / dropped
- IAS 39 / g102H-102I / 102I / dropped
- IAS 39 / g102J-102O / 102J / dropped
- IAS 39 / g102J-102O / 102K / dropped
- IAS 39 / g102J-102O / 102L / dropped
- IAS 39 / g102J-102O / 102M / dropped
- IAS 39 / g102J-102O / 102N / dropped
- IAS 39 / g102J-102O / 102O / dropped
- IAS 39 / g102P-102U / 102P / dropped
- IAS 39 / g102P-102U / 102Q / dropped
- IAS 39 / g102P-102U / 102R / dropped
- IAS 39 / g102P-102U / 102S / dropped
- IAS 39 / g102P-102U / 102T / dropped
- IAS 39 / g102P-102U / 102U / dropped
- IAS 39 / g102V-102V / 102V / dropped
- IAS 39 / g102W-102X / 102W / dropped
- IAS 39 / g102W-102X / 102X / dropped
- IAS 39 / g102Y-102Z / 102Y / dropped
- IAS 39 / g102Y-102Z / 102Z / dropped
- IAS 39 / g102Z1-102Z3 / 102Z1 / dropped
- IAS 39 / g102Z1-102Z3 / 102Z2 / dropped
- IAS 39 / g102Z1-102Z3 / 102Z3 / dropped
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
- IAS 39 / g2-7 / 2 / dropped
- IAS 39 / g71-102 / 71 / dropped
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
- IAS 39 / g81-81A / 81 / dropped
- IAS 39 / g81-81A / 81A / dropped
- IAS 39 / g82-82 / 82 / dropped
- IAS 39 / g82-82 / E5 / dropped
- IAS 39 / g83-84 / 83 / dropped
- IAS 39 / g83-84 / 84 / dropped
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
- IAS 39 / gAG133-AG133_V2 / AG133 / dropped
- IAS 39 / gAG98-AG99BA / AG98 / dropped
- IAS 39 / gAG98-AG99BA / AG99 / dropped
- IAS 39 / gAG98-AG99BA / AG99A / dropped
- IAS 39 / gAG98-AG99BA / AG99B / dropped
- IAS 39 / gAG98-AG99BA / AG99BA / dropped

### Q1.0 / 1

- Question: Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?
- Embedded question: Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?
financial statements
hedge accounting
dividend
receivable
foreign currency
foreign exchange

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IFRS 9 | g5.2.1-5.2.3 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | g5.3.1-5.3.2 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.1.1-6.1.3 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g6.3.1-6.3.6 | 🎯 authoritative | 0.66-0.68 | D:0 |
| IFRS 9 | g6.4.1-6.4.1 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g6.5.1-6.5.16 | 🎯 authoritative | — | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🗑️ dropped | 0.63 | D:0 |
| IFRS 9 | g6.5.15-6.5.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.16-6.5.16 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.2.1-B5.2.2A | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.3.1-B6.3.6 | 🗑️ dropped | 0.66-0.67 | D:0 |
| IFRS 9 | sgB5.2.3-B5.2.6 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | g1-6 | 🔎 secondary | 0.61-0.64 | D:0 |
| IFRIC 16 | g10-13 | 🔎 secondary | 0.62-0.65 | D:0 |
| IFRIC 16 | g14-15 | 🔎 secondary | 0.63 | D:0 |
| IFRIC 16 | g16-17 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | g7-8 | 🔎 secondary | 0.63 | D:0 |
| IFRIC 16 | g9-9 | 🗑️ dropped | 0.62 | D:0 |
| IFRIC 16 | gAG10-AG12 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG13-AG15 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG2-AG2 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG3-AG6 | 🗑️ dropped | 0.61-0.61 | D:0 |
| IFRIC 16 | gAG7-AG7 | 🗑️ dropped | — | D:0 |
| IFRIC 16 | gAG9-AG15 | 🗑️ dropped | 0.61 | D:0 |
| IAS 21 | g15-15A | 🗑️ dropped | — | D:0 |
| IAS 21 | g17-19 | 🗑️ dropped | 0.61 | D:0 |
| IAS 21 | g20-22 | 🗑️ dropped | — | D:0 |
| IAS 21 | g23-26 | 🗑️ dropped | 0.63 | D:0 |
| IAS 21 | g27-34 | 🔎 secondary | 0.64-0.65 | D:0 |
| IAS 21 | g3-7 | 🗑️ dropped | 0.61-0.65 | D:0 |
| IAS 21 | g38-43 | 🗑️ dropped | — | D:0 |
| IAS 21 | g44-47 | 🔎 secondary | 0.62-0.67 | D:0 |
| IAS 21 | g48-49 | 🗑️ dropped | — | D:0 |
| IAS 21 | g50-50 | 🗑️ dropped | — | D:0 |
| IAS 21 | g51-57 | 🗑️ dropped | — | D:0 |
| IAS 21 | g58-60K | 🗑️ dropped | 0.60 | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | 0.61 | D:1 |
| IAS 39 | g102A-102N | 🗑️ dropped | — | D:3 |
| IAS 39 | g102D-102D | 🗑️ dropped | — | D:1 |
| IAS 39 | g102E-102E | 🗑️ dropped | — | D:1 |
| IAS 39 | g102F-102G | 🗑️ dropped | — | D:2 |
| IAS 39 | g102H-102I | 🗑️ dropped | — | D:2 |
| IAS 39 | g102J-102O | 🗑️ dropped | — | D:6 |
| IAS 39 | g102P-102U | 🗑️ dropped | — | D:6 |
| IAS 39 | g102V-102V | 🗑️ dropped | — | D:1 |
| IAS 39 | g102W-102X | 🗑️ dropped | — | D:2 |
| IAS 39 | g102Y-102Z | 🗑️ dropped | — | D:2 |
| IAS 39 | g102Z1-102Z3 | 🗑️ dropped | — | D:3 |
| IAS 39 | g103-108F | 🗑️ dropped | 0.62 | D:21 |
| IAS 39 | g2-7 | 🗑️ dropped | 0.60 | D:1 |
| IAS 39 | g71-102 | 🗑️ dropped | — | D:1 |
| IAS 39 | g72-73 | 🗑️ dropped | 0.64 | D:2 |
| IAS 39 | g74-77 | 🗑️ dropped | 0.62 | D:8 |
| IAS 39 | g78-80 | 🗑️ dropped | 0.71 | D:2 |
| IAS 39 | g81-81A | 🗑️ dropped | — | D:2 |
| IAS 39 | g82-82 | 🗑️ dropped | — | D:2 |
| IAS 39 | g83-84 | 🗑️ dropped | — | D:2 |
| IAS 39 | g85-102 | 🗑️ dropped | 0.60 | D:8 |
| IAS 39 | g89-94 | 🗑️ dropped | — | D:7 |
| IAS 39 | g95-101 | 🗑️ dropped | — | D:7 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | — | D:13 |
| IAS 39 | gAG133-AG133_V2 | 🗑️ dropped | 0.61 | D:1 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | 0.65-0.65 | D:5 |
| IFRS 7 | g13A-13F | 🗑️ dropped | — | D:0 |
| IFRS 7 | g21A-24G | 🖼️ peripheral | 0.62 | D:0 |
| IFRS 7 | g22-22C | 🗑️ dropped | — | D:0 |
| IFRS 7 | g23-23F | 🗑️ dropped | — | D:0 |
| IFRS 7 | g24-24F | 🖼️ peripheral | 0.59-0.63 | D:0 |
| IFRS 7 | g24G-24G | 🗑️ dropped | — | D:0 |
| IFRS 7 | g24H-24H | 🗑️ dropped | — | D:0 |
| IFRS 7 | g31-42 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g33-33 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g34-42 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35A-35E | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35A-38 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35F-35G | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35H-35L | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35M-35N | 🗑️ dropped | — | D:0 |
| IFRS 7 | g38-38 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g39-39 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g40-41 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42-42 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42A-42S | 🗑️ dropped | 0.60-0.60 | D:0 |
| IFRS 7 | g42D-42D | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42E-42G | 🗑️ dropped | — | D:0 |
| IFRS 7 | g42H-42S | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB10A-B16 | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB17-B28 | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB22-B22 | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB23-B24 | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB25-B28 | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB29-B31 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 7 | gB33-B33 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 7 | gB51-B52 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 7 | gB6-B28 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 7 | gB7-B8 | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8A-B8C | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8D-B8E | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8F-B8G | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8H-B8J | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB9-B10 | 🗑️ dropped | — | D:0 |

Dropped chunks:

- IAS 39 / g102-102 / 102 / dropped
- IAS 39 / g102A-102N / 102A / dropped
- IAS 39 / g102A-102N / 102B / dropped
- IAS 39 / g102A-102N / 102C / dropped
- IAS 39 / g102D-102D / 102D / dropped
- IAS 39 / g102E-102E / 102E / dropped
- IAS 39 / g102F-102G / 102F / dropped
- IAS 39 / g102F-102G / 102G / dropped
- IAS 39 / g102H-102I / 102H / dropped
- IAS 39 / g102H-102I / 102I / dropped
- IAS 39 / g102J-102O / 102J / dropped
- IAS 39 / g102J-102O / 102K / dropped
- IAS 39 / g102J-102O / 102L / dropped
- IAS 39 / g102J-102O / 102M / dropped
- IAS 39 / g102J-102O / 102N / dropped
- IAS 39 / g102J-102O / 102O / dropped
- IAS 39 / g102P-102U / 102P / dropped
- IAS 39 / g102P-102U / 102Q / dropped
- IAS 39 / g102P-102U / 102R / dropped
- IAS 39 / g102P-102U / 102S / dropped
- IAS 39 / g102P-102U / 102T / dropped
- IAS 39 / g102P-102U / 102U / dropped
- IAS 39 / g102V-102V / 102V / dropped
- IAS 39 / g102W-102X / 102W / dropped
- IAS 39 / g102W-102X / 102X / dropped
- IAS 39 / g102Y-102Z / 102Y / dropped
- IAS 39 / g102Y-102Z / 102Z / dropped
- IAS 39 / g102Z1-102Z3 / 102Z1 / dropped
- IAS 39 / g102Z1-102Z3 / 102Z2 / dropped
- IAS 39 / g102Z1-102Z3 / 102Z3 / dropped
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
- IAS 39 / g2-7 / 2 / dropped
- IAS 39 / g71-102 / 71 / dropped
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
- IAS 39 / g81-81A / 81 / dropped
- IAS 39 / g81-81A / 81A / dropped
- IAS 39 / g82-82 / 82 / dropped
- IAS 39 / g82-82 / E5 / dropped
- IAS 39 / g83-84 / 83 / dropped
- IAS 39 / g83-84 / 84 / dropped
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
- IAS 39 / gAG133-AG133_V2 / AG133 / dropped
- IAS 39 / gAG98-AG99BA / AG98 / dropped
- IAS 39 / gAG98-AG99BA / AG99 / dropped
- IAS 39 / gAG98-AG99BA / AG99A / dropped
- IAS 39 / gAG98-AG99BA / AG99B / dropped
- IAS 39 / gAG98-AG99BA / AG99BA / dropped

