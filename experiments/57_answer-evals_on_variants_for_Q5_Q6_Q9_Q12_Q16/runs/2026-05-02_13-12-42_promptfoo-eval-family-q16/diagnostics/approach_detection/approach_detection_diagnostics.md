# approach_detection_diagnostics

This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.

- Experiment: `57_answer-evals_on_variants_for_Q5_Q6_Q9_Q12_Q16`
- Run: `2026-05-02_13-12-42_promptfoo-eval-family-q16`
- Provider: `OpenAI GPT 5.4 through Codex current answer defaults`
- Answer attempts: 9

## Label Frequency

| Label | Expected | Present | Questions |
| --- | ---: | ---: | ---: |
| contingent_liability | yes | 9/9 | 5 |
| provision | yes | 9/9 | 5 |

## Question Stability

| Question | Runs | Strict | Loose | Missing expected | Spurious |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q16.0 | 2 | 100.0 | 100.0 | 0 | 0 |
| Q16.1 | 2 | 100.0 | 100.0 | 0 | 0 |
| Q16.2 | 2 | 100.0 | 100.0 | 0 | 0 |
| Q16.3 | 2 | 35.0 | 35.0 | 0 | 0 |
| Q16.4 | 1 | 100.0 | 100.0 | 0 | 0 |

## Authority Categorization by Run

### Q16.0 / 0

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
| IAS 37 | g48-50 | 🔎 secondary | — | D:0 |
| IAS 37 | g53-58 | 🔎 secondary | — | D:0 |
| IAS 37 | g59-60 | 🔎 secondary | — | D:0 |
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
| IFRS 7 | g35A-35E | 🖼️ peripheral | — | D:0 |
| IFRS 7 | g35A-38 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35F-35G | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 7 | g35H-35L | 🖼️ peripheral | — | D:0 |
| IFRS 7 | g35M-35N | 🖼️ peripheral | — | D:0 |
| IFRS 7 | g38-38 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g39-39 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 7 | g43-44DD | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB10A-B16 | 🗑️ dropped | 0.55-0.59 | D:0 |
| IFRS 7 | gB50-B50 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | gB8A-B8C | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8D-B8E | 🖼️ peripheral | 0.61 | D:0 |
| IFRS 7 | gB8H-B8J | 🗑️ dropped | 0.57 | D:0 |
| IFRS 7 | gB9-B10 | 🖼️ peripheral | 0.55 | D:0 |
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
| IAS 37 | g23-24 | 🎯 authoritative | — | D:0 |
| IAS 37 | g25-26 | 🎯 authoritative | 0.59 | D:0 |
| IAS 37 | g48-50 | 🔎 secondary | — | D:0 |
| IAS 37 | g53-58 | 🔎 secondary | — | D:0 |
| IAS 37 | g59-60 | 🔎 secondary | — | D:0 |
| IAS 37 | g61-62 | 🔎 secondary | — | D:0 |
| IAS 37 | g84-92 | 🔎 secondary | 0.58-0.59 | D:0 |
| IFRS 19 | g203-203 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 19 | g211-211 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g257-262 | 🖼️ peripheral | 0.58-0.59 | D:0 |
| IFRS 19 | g65-67 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 19 | g76-81 | 🗑️ dropped | 0.57-0.58 | D:0 |
| IFRS 19 | g84-87 | 🗑️ dropped | 0.56-0.58 | D:0 |
| IFRS 19 | g92-94 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 7 | g13A-13F | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35A-35E | 🖼️ peripheral | — | D:0 |
| IFRS 7 | g35A-38 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35F-35G | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 7 | g35H-35L | 🖼️ peripheral | — | D:0 |
| IFRS 7 | g35M-35N | 🖼️ peripheral | — | D:0 |
| IFRS 7 | g38-38 | 🗑️ dropped | — | D:0 |
| IFRS 7 | g39-39 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 7 | g43-44DD | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB10A-B16 | 🖼️ peripheral | 0.55-0.59 | D:0 |
| IFRS 7 | gB50-B50 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | gB8A-B8C | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8D-B8E | 🖼️ peripheral | 0.61 | D:0 |
| IFRS 7 | gB8H-B8J | 🗑️ dropped | 0.57 | D:0 |
| IFRS 7 | gB9-B10 | 🖼️ peripheral | 0.55 | D:0 |
| IFRS 7 | sg20-20A | 🖼️ peripheral | 0.61 | D:0 |

### Q16.1 / 0

- Question: Une entité s’est engagée volontairement à contribuer à la neutralité carbone à une échéance déterminée. Dans ce contexte, doit-elle comptabiliser une provision, notamment au titre des crédits carbone nécessaires pour compenser ses émissions excédentaires ?
- Embedded question: Une entité s’est engagée volontairement à contribuer à la neutralité carbone à une échéance déterminée. Dans ce contexte, doit-elle comptabiliser une provision, notamment au titre des crédits carbone nécessaires pour compenser ses émissions excédentaires ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IAS 37 | g1-9 | 🗑️ dropped | 0.57 | D:0 |
| IAS 37 | g10-13 | 🎯 authoritative | 0.58 | D:0 |
| IAS 37 | g11-11 | 🗑️ dropped | — | D:0 |
| IAS 37 | g12-13 | 🗑️ dropped | — | D:0 |
| IAS 37 | g14-26 | 🎯 authoritative | 0.59 | D:0 |
| IAS 37 | g15-16 | 🗑️ dropped | — | D:0 |
| IAS 37 | g17-22 | 🎯 authoritative | 0.61-0.65 | D:0 |
| IAS 37 | g23-24 | 🔎 secondary | — | D:0 |
| IAS 37 | g25-26 | 🔎 secondary | 0.57 | D:0 |
| IAS 37 | g27-30 | 🗑️ dropped | 0.57 | D:0 |
| IAS 37 | g36-41 | 🔎 secondary | 0.58 | D:0 |
| IAS 37 | g48-50 | 🔎 secondary | 0.57 | D:0 |
| IFRS 19 | g176-177 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g178-181 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g196-199 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g203-203 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 19 | g257-262 | 🖼️ peripheral | 0.56-0.57 | D:0 |
| IFRS 19 | g45-46 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | g65-67 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 19 | g76-81 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | gB13-B14 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 7 | g22-22C | 🗑️ dropped | — | D:0 |
| IFRS 7 | g24I-24J | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | g35A-35E | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35F-35G | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | g35M-35N | 🗑️ dropped | — | D:0 |
| IFRS 7 | g39-39 | 🖼️ peripheral | — | D:0 |
| IFRS 7 | g43-44DD | 🗑️ dropped | — | D:0 |
| IFRS 7 | g9-11 | 🗑️ dropped | 0.55-0.55 | D:0 |
| IFRS 7 | gB10A-B16 | 🗑️ dropped | 0.57-0.59 | D:0 |
| IFRS 7 | gB8A-B8C | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8D-B8E | 🗑️ dropped | 0.59 | D:0 |
| IFRS 7 | gB8H-B8J | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | sg20-20A | 🖼️ peripheral | 0.64 | D:0 |
| IAS 19 | g102-108 | 🖼️ peripheral | — | D:0 |
| IAS 19 | g109-112 | 🗑️ dropped | — | D:0 |
| IAS 19 | g19-24 | 🖼️ peripheral | 0.57-0.58 | D:0 |
| IAS 19 | g26-49 | 🗑️ dropped | 0.57-0.59 | D:0 |
| IAS 19 | g32-39 | 🗑️ dropped | — | D:0 |
| IAS 19 | g40-42 | 🗑️ dropped | — | D:0 |
| IAS 19 | g43-45 | 🗑️ dropped | — | D:0 |
| IAS 19 | g46-49 | 🖼️ peripheral | 0.59 | D:0 |
| IAS 19 | g51-52 | 🗑️ dropped | 0.57-0.59 | D:0 |
| IAS 19 | g53-54 | 🗑️ dropped | 0.61 | D:0 |
| IAS 19 | g63-65 | 🗑️ dropped | 0.57 | D:0 |
| IAS 19 | g75-80 | 🗑️ dropped | — | D:0 |
| IAS 19 | g87-98 | 🗑️ dropped | 0.56 | D:0 |

### Q16.1 / 1

- Question: Une entité s’est engagée volontairement à contribuer à la neutralité carbone à une échéance déterminée. Dans ce contexte, doit-elle comptabiliser une provision, notamment au titre des crédits carbone nécessaires pour compenser ses émissions excédentaires ?
- Embedded question: Une entité s’est engagée volontairement à contribuer à la neutralité carbone à une échéance déterminée. Dans ce contexte, doit-elle comptabiliser une provision, notamment au titre des crédits carbone nécessaires pour compenser ses émissions excédentaires ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IAS 37 | g1-9 | 🗑️ dropped | 0.57 | D:0 |
| IAS 37 | g10-13 | 🎯 authoritative | 0.58 | D:0 |
| IAS 37 | g11-11 | 🗑️ dropped | — | D:0 |
| IAS 37 | g12-13 | 🗑️ dropped | — | D:0 |
| IAS 37 | g14-26 | 🎯 authoritative | 0.59 | D:0 |
| IAS 37 | g15-16 | 🗑️ dropped | — | D:0 |
| IAS 37 | g17-22 | 🎯 authoritative | 0.61-0.65 | D:0 |
| IAS 37 | g23-24 | 🎯 authoritative | — | D:0 |
| IAS 37 | g25-26 | 🗑️ dropped | 0.57 | D:0 |
| IAS 37 | g27-30 | 🎯 authoritative | 0.57 | D:0 |
| IAS 37 | g36-41 | 🎯 authoritative | 0.58 | D:0 |
| IAS 37 | g48-50 | 🎯 authoritative | 0.57 | D:0 |
| IFRS 19 | g176-177 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g178-181 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g196-199 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 19 | g203-203 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 19 | g257-262 | 🖼️ peripheral | 0.56-0.57 | D:0 |
| IFRS 19 | g45-46 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | g65-67 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 19 | g76-81 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | gB13-B14 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 7 | g22-22C | 🗑️ dropped | — | D:0 |
| IFRS 7 | g24I-24J | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | g35A-35E | 🗑️ dropped | — | D:0 |
| IFRS 7 | g35F-35G | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | g35M-35N | 🗑️ dropped | — | D:0 |
| IFRS 7 | g39-39 | 🖼️ peripheral | — | D:0 |
| IFRS 7 | g43-44DD | 🗑️ dropped | — | D:0 |
| IFRS 7 | g9-11 | 🗑️ dropped | 0.55-0.55 | D:0 |
| IFRS 7 | gB10A-B16 | 🗑️ dropped | 0.57-0.59 | D:0 |
| IFRS 7 | gB8A-B8C | 🗑️ dropped | — | D:0 |
| IFRS 7 | gB8D-B8E | 🗑️ dropped | 0.59 | D:0 |
| IFRS 7 | gB8H-B8J | 🗑️ dropped | 0.55 | D:0 |
| IFRS 7 | sg20-20A | 🖼️ peripheral | 0.64 | D:0 |
| IAS 19 | g102-108 | 🗑️ dropped | — | D:0 |
| IAS 19 | g109-112 | 🗑️ dropped | — | D:0 |
| IAS 19 | g19-24 | 🔎 secondary | 0.57-0.58 | D:0 |
| IAS 19 | g26-49 | 🗑️ dropped | 0.57-0.59 | D:0 |
| IAS 19 | g32-39 | 🗑️ dropped | — | D:0 |
| IAS 19 | g40-42 | 🗑️ dropped | — | D:0 |
| IAS 19 | g43-45 | 🗑️ dropped | — | D:0 |
| IAS 19 | g46-49 | 🗑️ dropped | 0.59 | D:0 |
| IAS 19 | g51-52 | 🗑️ dropped | 0.57-0.59 | D:0 |
| IAS 19 | g53-54 | 🗑️ dropped | 0.61 | D:0 |
| IAS 19 | g63-65 | 🗑️ dropped | 0.57 | D:0 |
| IAS 19 | g75-80 | 🗑️ dropped | — | D:0 |
| IAS 19 | g87-98 | 🗑️ dropped | 0.56 | D:0 |

### Q16.2 / 0

- Question: Un engagement public et volontaire de neutralité carbone a été pris pour un horizon défini. Faut-il reconnaître une provision pour cet engagement ou pour l’achat futur de crédits carbone destinés à compenser les dépassements d’émissions ?
- Embedded question: Un engagement public et volontaire de neutralité carbone a été pris pour un horizon défini. Faut-il reconnaître une provision pour cet engagement ou pour l’achat futur de crédits carbone destinés à compenser les dépassements d’émissions ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IAS 37 | g1-9 | 🗑️ dropped | — | D:0 |
| IAS 37 | g10-13 | 🎯 authoritative | — | D:0 |
| IAS 37 | g11-11 | 🗑️ dropped | — | D:0 |
| IAS 37 | g12-13 | 🗑️ dropped | 0.55 | D:0 |
| IAS 37 | g14-26 | 🎯 authoritative | 0.58 | D:0 |
| IAS 37 | g15-16 | 🗑️ dropped | — | D:0 |
| IAS 37 | g17-22 | 🎯 authoritative | 0.55-0.64 | D:0 |
| IAS 37 | g23-24 | 🗑️ dropped | 0.56 | D:0 |
| IAS 37 | g25-26 | 🗑️ dropped | — | D:0 |
| IAS 37 | g36-41 | 🗑️ dropped | — | D:0 |
| IAS 37 | g48-50 | 🗑️ dropped | 0.55-0.56 | D:0 |
| IAS 37 | g53-58 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | g178-181 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | g200-202 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | g203-203 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | g257-262 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 19 | g65-67 | 🗑️ dropped | 0.54-0.61 | D:0 |
| IFRS 19 | g68-71 | 🗑️ dropped | 0.54-0.55 | D:0 |
| IFRS 19 | g7-12 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 19 | g88-91 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 9 | g2.1-2.7 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 9 | g2.4-2.8 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g4.2.1-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.5.1-5.5.8 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.5.17-5.5.20 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 9 | g5.5.9-5.5.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.7.1-6.7.1 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 9 | gB2.1-B2.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.5.1-B5.5.6 | 🗑️ dropped | 0.57-0.57 | D:0 |
| IFRS 9 | gB5.5.28-B5.5.35 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 9 | gB5.5.38-B5.5.40 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 9 | gB5.5.44-B5.5.48 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 9 | gB5.5.49-B5.5.54 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 9 | gB5.5.55-B5.5.55 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.5.7-B5.5.14 | 🗑️ dropped | 0.57 | D:0 |
| IAS 38 | g11-12 | 🗑️ dropped | — | D:0 |
| IAS 38 | g13-16 | 🗑️ dropped | — | D:0 |
| IAS 38 | g17-17 | 🗑️ dropped | — | D:0 |
| IAS 38 | g18-67 | 🗑️ dropped | — | D:0 |
| IAS 38 | g25-32 | 🗑️ dropped | 0.53-0.53 | D:0 |
| IAS 38 | g33-43 | 🗑️ dropped | — | D:0 |
| IAS 38 | g35-38-41 | 🗑️ dropped | — | D:0 |
| IAS 38 | g42-43 | 🗑️ dropped | — | D:0 |
| IAS 38 | g44-44 | 🗑️ dropped | — | D:0 |
| IAS 38 | g45-47 | 🗑️ dropped | — | D:0 |
| IAS 38 | g48-50 | 🗑️ dropped | — | D:0 |
| IAS 38 | g51-67 | 🗑️ dropped | — | D:0 |
| IAS 38 | g54-56 | 🗑️ dropped | — | D:0 |
| IAS 38 | g57-64 | 🗑️ dropped | — | D:0 |
| IAS 38 | g65-67 | 🗑️ dropped | — | D:0 |
| IAS 38 | g9-17 | 🔎 secondary | 0.61 | D:0 |

### Q16.2 / 1

- Question: Un engagement public et volontaire de neutralité carbone a été pris pour un horizon défini. Faut-il reconnaître une provision pour cet engagement ou pour l’achat futur de crédits carbone destinés à compenser les dépassements d’émissions ?
- Embedded question: Un engagement public et volontaire de neutralité carbone a été pris pour un horizon défini. Faut-il reconnaître une provision pour cet engagement ou pour l’achat futur de crédits carbone destinés à compenser les dépassements d’émissions ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IAS 37 | g1-9 | 🗑️ dropped | — | D:0 |
| IAS 37 | g10-13 | 🎯 authoritative | — | D:0 |
| IAS 37 | g11-11 | 🗑️ dropped | — | D:0 |
| IAS 37 | g12-13 | 🎯 authoritative | 0.55 | D:0 |
| IAS 37 | g14-26 | 🎯 authoritative | 0.58 | D:0 |
| IAS 37 | g15-16 | 🔎 secondary | — | D:0 |
| IAS 37 | g17-22 | 🎯 authoritative | 0.55-0.64 | D:0 |
| IAS 37 | g23-24 | 🎯 authoritative | 0.56 | D:0 |
| IAS 37 | g25-26 | 🎯 authoritative | — | D:0 |
| IAS 37 | g36-41 | 🎯 authoritative | — | D:0 |
| IAS 37 | g48-50 | 🎯 authoritative | 0.55-0.56 | D:0 |
| IAS 37 | g53-58 | 🔎 secondary | 0.55 | D:0 |
| IFRS 19 | g178-181 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | g200-202 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | g203-203 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 19 | g257-262 | 🖼️ peripheral | 0.54 | D:0 |
| IFRS 19 | g65-67 | 🗑️ dropped | 0.54-0.61 | D:0 |
| IFRS 19 | g68-71 | 🗑️ dropped | 0.54-0.55 | D:0 |
| IFRS 19 | g7-12 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 19 | g88-91 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 9 | g2.1-2.7 | 🖼️ peripheral | 0.61 | D:0 |
| IFRS 9 | g2.4-2.8 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g4.2.1-4.2.2 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.5.1-5.5.8 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g5.5.17-5.5.20 | 🖼️ peripheral | 0.59 | D:0 |
| IFRS 9 | g5.5.9-5.5.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.7.1-6.7.1 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 9 | gB2.1-B2.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.5.1-B5.5.6 | 🗑️ dropped | 0.57-0.57 | D:0 |
| IFRS 9 | gB5.5.28-B5.5.35 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 9 | gB5.5.38-B5.5.40 | 🗑️ dropped | 0.57 | D:0 |
| IFRS 9 | gB5.5.44-B5.5.48 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 9 | gB5.5.49-B5.5.54 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 9 | gB5.5.55-B5.5.55 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.5.7-B5.5.14 | 🗑️ dropped | 0.57 | D:0 |
| IAS 38 | g11-12 | 🗑️ dropped | — | D:0 |
| IAS 38 | g13-16 | 🖼️ peripheral | — | D:0 |
| IAS 38 | g17-17 | 🗑️ dropped | — | D:0 |
| IAS 38 | g18-67 | 🖼️ peripheral | — | D:0 |
| IAS 38 | g25-32 | 🖼️ peripheral | 0.53-0.53 | D:0 |
| IAS 38 | g33-43 | 🗑️ dropped | — | D:0 |
| IAS 38 | g35-38-41 | 🗑️ dropped | — | D:0 |
| IAS 38 | g42-43 | 🗑️ dropped | — | D:0 |
| IAS 38 | g44-44 | 🗑️ dropped | — | D:0 |
| IAS 38 | g45-47 | 🗑️ dropped | — | D:0 |
| IAS 38 | g48-50 | 🗑️ dropped | — | D:0 |
| IAS 38 | g51-67 | 🗑️ dropped | — | D:0 |
| IAS 38 | g54-56 | 🗑️ dropped | — | D:0 |
| IAS 38 | g57-64 | 🗑️ dropped | — | D:0 |
| IAS 38 | g65-67 | 🗑️ dropped | — | D:0 |
| IAS 38 | g9-17 | 🖼️ peripheral | 0.61 | D:0 |

### Q16.3 / 0

- Question: Dans quelle mesure un engagement volontaire de contribution à la neutralité carbone crée-t-il une obligation actuelle imposant la comptabilisation d’une provision pour les crédits carbone à utiliser ultérieurement ?
- Embedded question: Dans quelle mesure un engagement volontaire de contribution à la neutralité carbone crée-t-il une obligation actuelle imposant la comptabilisation d’une provision pour les crédits carbone à utiliser ultérieurement ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IAS 37 | g10-13 | 🎯 authoritative | 0.54 | D:0 |
| IAS 37 | g11-11 | 🗑️ dropped | — | D:0 |
| IAS 37 | g12-13 | 🗑️ dropped | — | D:0 |
| IAS 37 | g15-16 | 🎯 authoritative | — | D:0 |
| IAS 37 | g17-22 | 🎯 authoritative | 0.55-0.61 | D:0 |
| IAS 37 | g23-24 | 🎯 authoritative | — | D:0 |
| IAS 37 | g25-26 | 🎯 authoritative | — | D:0 |

### Q16.3 / 1

- Question: Dans quelle mesure un engagement volontaire de contribution à la neutralité carbone crée-t-il une obligation actuelle imposant la comptabilisation d’une provision pour les crédits carbone à utiliser ultérieurement ?
- Embedded question: Dans quelle mesure un engagement volontaire de contribution à la neutralité carbone crée-t-il une obligation actuelle imposant la comptabilisation d’une provision pour les crédits carbone à utiliser ultérieurement ?

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IAS 37 | g10-13 | 🎯 authoritative | 0.54 | D:0 |
| IAS 37 | g11-11 | 🖼️ peripheral | — | D:0 |
| IAS 37 | g12-13 | 🎯 authoritative | — | D:0 |
| IAS 37 | g15-16 | 🎯 authoritative | — | D:0 |
| IAS 37 | g17-22 | 🎯 authoritative | 0.55-0.61 | D:0 |
| IAS 37 | g23-24 | 🎯 authoritative | — | D:0 |
| IAS 37 | g25-26 | 🎯 authoritative | — | D:0 |

### Q16.4 / 0

- Question: Une société annonce un objectif volontaire de neutralité carbone et prévoit de recourir à des crédits carbone pour couvrir ses émissions excédentaires. Cette situation entraîne-t-elle la reconnaissance d’une provision selon les IFRS ?
- Embedded question: Une société annonce un objectif volontaire de neutralité carbone et prévoit de recourir à des crédits carbone pour couvrir ses émissions excédentaires. Cette situation entraîne-t-elle la reconnaissance d’une provision selon les IFRS ?
hedge accounting

| Document | Section range | Category | Retrieved score | Dropped |
| --- | --- | --- | --- | --- |
| IAS 37 | g1-9 | 🗑️ dropped | 0.56-0.60 | D:0 |
| IAS 37 | g10-13 | 🎯 authoritative | — | D:0 |
| IAS 37 | g11-11 | 🗑️ dropped | — | D:0 |
| IAS 37 | g12-13 | 🗑️ dropped | — | D:0 |
| IAS 37 | g14-26 | 🎯 authoritative | 0.59 | D:0 |
| IAS 37 | g15-16 | 🔎 secondary | — | D:0 |
| IAS 37 | g17-22 | 🎯 authoritative | 0.59-0.63 | D:0 |
| IAS 37 | g23-24 | 🎯 authoritative | 0.56 | D:0 |
| IAS 37 | g25-26 | 🔎 secondary | 0.56 | D:0 |
| IAS 37 | g27-30 | 🎯 authoritative | 0.56 | D:0 |
| IAS 37 | g36-41 | 🔎 secondary | — | D:0 |
| IFRS 9 | g4.1.1-4.1.5 | 🖼️ peripheral | — | D:0 |
| IFRS 9 | g4.1.5-4.1.5 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g4.2.2-4.2.2 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.1-5.7.11 | 🖼️ peripheral | 0.61 | D:0 |
| IFRS 9 | g5.7.10-5.7.11 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.5-5.7.6 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g5.7.7-5.7.9 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.1.1-6.1.3 | 🖼️ peripheral | 0.61-0.62 | D:0 |
| IFRS 9 | g6.3.7-6.3.7 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 9 | g6.4.1-6.4.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.11-6.5.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.13-6.5.14 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.5.8-6.5.10 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.6.1-6.6.1 | 🗑️ dropped | — | D:0 |
| IFRS 9 | g6.6.2-6.6.3 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 9 | gB4.1.29-B4.1.32 | 🗑️ dropped | 0.62 | D:0 |
| IFRS 9 | gB5.7.1-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.13-B5.7.15 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.16-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB5.7.5-B5.7.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.3.16-B6.3.20 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.3.8-B6.3.15 | 🗑️ dropped | 0.59 | D:0 |
| IFRS 9 | gB6.6.1-B6.6.4 | 🗑️ dropped | 0.60 | D:0 |
| IFRS 9 | gB6.6.11-B6.6.12 | 🗑️ dropped | — | D:0 |
| IFRS 9 | gB6.6.13-B6.6.16 | 🗑️ dropped | 0.61 | D:0 |
| IFRS 9 | gB6.6.7-B6.6.10 | 🗑️ dropped | 0.60 | D:0 |
| IAS 39 | g102-102 | 🗑️ dropped | — | D:0 |
| IAS 39 | g102A-102N | 🗑️ dropped | — | D:0 |
| IAS 39 | g102D-102D | 🗑️ dropped | — | D:0 |
| IAS 39 | g102E-102E | 🗑️ dropped | — | D:0 |
| IAS 39 | g102F-102G | 🗑️ dropped | — | D:0 |
| IAS 39 | g102H-102I | 🗑️ dropped | — | D:0 |
| IAS 39 | g102J-102O | 🗑️ dropped | — | D:0 |
| IAS 39 | g102P-102U | 🗑️ dropped | 0.58-0.61 | D:0 |
| IAS 39 | g102V-102V | 🗑️ dropped | — | D:0 |
| IAS 39 | g102W-102X | 🗑️ dropped | — | D:0 |
| IAS 39 | g102Y-102Z | 🗑️ dropped | — | D:0 |
| IAS 39 | g102Z1-102Z3 | 🗑️ dropped | — | D:0 |
| IAS 39 | g103-108F | 🗑️ dropped | — | D:0 |
| IAS 39 | g71-102 | 🖼️ peripheral | 0.61 | D:0 |
| IAS 39 | g72-73 | 🗑️ dropped | — | D:0 |
| IAS 39 | g74-77 | 🗑️ dropped | — | D:0 |
| IAS 39 | g78-80 | 🗑️ dropped | 0.58 | D:0 |
| IAS 39 | g81-81A | 🗑️ dropped | — | D:0 |
| IAS 39 | g82-82 | 🗑️ dropped | — | D:0 |
| IAS 39 | g83-84 | 🗑️ dropped | — | D:0 |
| IAS 39 | g85-102 | 🖼️ peripheral | 0.58 | D:0 |
| IAS 39 | g89-94 | 🖼️ peripheral | — | D:0 |
| IAS 39 | g95-101 | 🖼️ peripheral | 0.61 | D:0 |
| IAS 39 | gAG100-AG100 | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG101-AG101 | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG102-AG132 | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG105-AG113A | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG114-AG132 | 🗑️ dropped | 0.59 | D:0 |
| IAS 39 | gAG98-AG101 | 🗑️ dropped | 0.60 | D:0 |
| IAS 39 | gAG98-AG99BA | 🗑️ dropped | — | D:0 |
| IAS 39 | gAG99C-AG99D | 🗑️ dropped | — | D:0 |
| IFRS 17 | g10-13 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g110-113 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g114-116 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 17 | g117-120 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g121-132 | 🗑️ dropped | 0.55 | D:0 |
| IFRS 17 | g127-127 | 🗑️ dropped | 0.58 | D:0 |
| IFRS 17 | g128-129 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 17 | g130-130 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g131-131 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 17 | g132-132 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g3-13 | 🖼️ peripheral | 0.57 | D:0 |
| IFRS 17 | g38-39 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g47-52 | 🖼️ peripheral | — | D:0 |
| IFRS 17 | g9-9 | 🗑️ dropped | — | D:0 |
| IFRS 17 | g93-132 | 🖼️ peripheral | 0.58 | D:0 |
| IFRS 17 | g97-116 | 🗑️ dropped | — | D:0 |
| IFRS 17 | gB120-B127 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 17 | gB137-B137 | 🗑️ dropped | 0.56 | D:0 |
| IFRS 17 | gB61-B71 | 🗑️ dropped | 0.54 | D:0 |
| IFRS 17 | gB67-B71 | 🗑️ dropped | — | D:0 |

