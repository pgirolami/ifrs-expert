# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `55_get_answer-eval_to_work_for_Q16.0_without_breaking_Q1Q2Q3`
- Run: `2026-05-01_20-44-53_promptfoo-eval-family-q16`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 2

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| contingent_liability | yes | 2/2 | 1 |
| provision | yes | 2/2 | 1 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q16.0 | 2 | 100.0 | 100.0 | 0 | 0 |

## Authority Categorization by Run

### Q16.0 / 0

- Question: Une entité ayant pris un engagement volontaire de contribution à la neutralité carbone à un horizon défini doit-elle constituer une provision ?
Doit-elle constituer une provision pour les crédits carbone qui seront utilisés pour compenser les émissions excédentaires de l'entité ?
- Embedded question: Une entité ayant pris un engagement volontaire de contribution à la neutralité carbone à un horizon défini doit-elle constituer une provision ?
Doit-elle constituer une provision pour les crédits carbone qui seront utilisés pour compenser les émissions excédentaires de l'entité ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IAS 37 | g1-9 | 🎯 authoritative | 0.59 | D:0 |
| IAS 37 | g10-13 | 🎯 authoritative | 0.62 | D:0 |
| IAS 37 | g11-11 | 🗑️ dropped | — | D:0 |
| IAS 37 | g12-13 | 🔎 secondary | — | D:0 |
| IAS 37 | g14-26 | 🎯 authoritative | 0.63 | D:0 |
| IAS 37 | g15-16 | 🔎 secondary | — | D:0 |
| IAS 37 | g17-22 | 🎯 authoritative | 0.59-0.66 | D:0 |
| IAS 37 | g23-24 | 🎯 authoritative | — | D:0 |
| IAS 37 | g25-26 | 🗑️ dropped | 0.59 | D:0 |
| IAS 37 | g48-50 | 🔎 secondary | — | D:0 |
| IAS 37 | g53-58 | 🗑️ dropped | — | D:0 |
| IAS 37 | g59-60 | 🗑️ dropped | — | D:0 |
| IAS 37 | g61-62 | 🗑️ dropped | — | D:0 |
| IAS 37 | g84-92 | 🗑️ dropped | 0.58-0.59 | D:0 |
| IFRS 19 | g203-203 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 19 | g211-211 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g257-262 | 🖼️ peripheral | 0.58-0.59 | D:0 |
| IFRS 19 | g65-67 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 19 | g76-81 | 🗑️ dropped | 0.57-0.58 | D:0 |
| IFRS 19 | g84-87 | 🗑️ dropped | 0.56-0.58 | D:0 |
| IFRS 19 | g92-94 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 7 | g13A-13F | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35A-35E | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35A-38 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35F-35G | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | g35H-35L | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35M-35N | 🗑️ dropped | — | D:0 |
| IFRS 7 | g38-38 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g39-39 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 7 | g43-44DD | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB10A-B16 | 🗑️ dropped | 0.55-0.59 | D:0 |
| IFRS 7 | gB50-B50 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | gB8A-B8C | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8D-B8E | 🗑️ dropped | 0.61 | D:0 |
| IFRS 7 | gB8H-B8J | 🗑️ dropped | 0.57 | D:0 |
| IFRS 7 | gB9-B10 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | sg20-20A | 🖼️ peripheral | 0.61 | D:0 |

### Q16.0 / 1

- Question: Une entité ayant pris un engagement volontaire de contribution à la neutralité carbone à un horizon défini doit-elle constituer une provision ?
Doit-elle constituer une provision pour les crédits carbone qui seront utilisés pour compenser les émissions excédentaires de l'entité ?
- Embedded question: Une entité ayant pris un engagement volontaire de contribution à la neutralité carbone à un horizon défini doit-elle constituer une provision ?
Doit-elle constituer une provision pour les crédits carbone qui seront utilisés pour compenser les émissions excédentaires de l'entité ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IAS 37 | g1-9 | 🗑️ dropped | 0.59 | D:0 |
| IAS 37 | g10-13 | 🎯 authoritative | 0.62 | D:0 |
| IAS 37 | g11-11 | 🗑️ dropped | — | D:0 |
| IAS 37 | g12-13 | 🗑️ dropped | — | D:0 |
| IAS 37 | g14-26 | 🎯 authoritative | 0.63 | D:0 |
| IAS 37 | g15-16 | 🔎 secondary | — | D:0 |
| IAS 37 | g17-22 | 🎯 authoritative | 0.59-0.66 | D:0 |
| IAS 37 | g23-24 | 🔎 secondary | — | D:0 |
| IAS 37 | g25-26 | 🔎 secondary | 0.59 | D:0 |
| IAS 37 | g48-50 | 🗑️ dropped | — | D:0 |
| IAS 37 | g53-58 | 🗑️ dropped | — | D:0 |
| IAS 37 | g59-60 | 🗑️ dropped | — | D:0 |
| IAS 37 | g61-62 | 🗑️ dropped | — | D:0 |
| IAS 37 | g84-92 | 🗑️ dropped | 0.58-0.59 | D:0 |
| IFRS 19 | g203-203 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 19 | g211-211 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g257-262 | 🖼️ peripheral | 0.58-0.59 | D:0 |
| IFRS 19 | g65-67 | 🖼️ peripheral | 0.61 | D:0 |
| IFRS 19 | g76-81 | 🗑️ dropped | 0.57-0.58 | D:0 |
| IFRS 19 | g84-87 | 🗑️ dropped | 0.56-0.58 | D:0 |
| IFRS 19 | g92-94 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 7 | g13A-13F | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35A-35E | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35A-38 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35F-35G | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | g35H-35L | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35M-35N | 🗑️ dropped | — | D:0 |
| IFRS 7 | g38-38 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g39-39 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 7 | g43-44DD | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB10A-B16 | 🗑️ dropped | 0.55-0.59 | D:0 |
| IFRS 7 | gB50-B50 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | gB8A-B8C | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8D-B8E | 🗑️ dropped | 0.61 | D:0 |
| IFRS 7 | gB8H-B8J | 🗑️ dropped | 0.57 | D:0 |
| IFRS 7 | gB9-B10 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | sg20-20A | 🖼️ peripheral | 0.61 | D:0 |

