# 2026-03-24

## Context experiments to see NIH appear in the answer

### IFRS 9 + full IFRIC 16 (manual baseline that worked)
**Answer**
   - Ok to cover forex risk ✅
   - Not ok to for intragroup ✅
   - No to highly probable transaction because already accounted for ✅
   - Mentions NIH ✅

**Summary table**
| Approche                                               | Applicable             | Condition clé                                             |
| ------------------------------------------------------ | ---------------------- | --------------------------------------------------------- |
| Créance de dividende comme poste monétaire intragroupe | Oui sous conditions    | Écarts de change non totalement éliminés en consolidation |
| Dividende intragroupe comme transaction intragroupe    | Non                    | Exclusion des transactions intragroupe en consolidation   |
| Dividende futur comme transaction prévue               | Non dans le cas décrit | La créance est déjà comptabilisée                         |
| Couverture d’investissement net par analogie           | Non                    | IFRIC 16 ne s’applique pas à ce cas                       |

### top-k chunks from IFRS 9 & IFRIC 16 each
#### k=2, e=5, min-score=0.5
**Retrieved chunks**
- ifrs-9-financial-instruments 2025 required: 6.2.6, 6.3.1, 6.3.2, 6.3.3, 6.3.4, 6.3.5, 6.3.6, 6.3.7, 6.4.1, 6.5.1, 6.5.2, B6.2.6, B6.3.1, B6.3.2, B6.3.3, B6.3.4, B6.3.5, B6.3.6, B6.3.7, B6.3.8, B6.3.9, B6.3.10
- ifric-16-hedges-of-a-net-investment-in-a-foreign-operation: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18


**Sections mentioned in answer**
   - 6.3.5
   - 6.3.6
   - 6.3.1
   - 6.3.3
   - IFRIC 16: 8, 11

**Summary table**
| Approche                                             | Applicable          | Condition clé                                                                                                  |
| ---------------------------------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------- |
| Dividende intragroupe comme transaction couverte     | Non                 | L’élément couvert doit en principe être avec une partie externe (IFRS 9.6.3.5)                                 |
| Créance intragroupe reconnue comme élément monétaire | Oui sous conditions | Écarts de change non entièrement éliminés en consolidation entre entités à monnaies fonctionnelles différentes |
| Transaction intragroupe future hautement probable    | Non                 | Le cas porte sur une créance déjà reconnue, pas sur une transaction future                                     |
| Couverture d’investissement net                      | Non                 | Le risque couvert doit porter sur des net assets d’une foreign operation                                       |

**Answer**
   - Ok to cover forex risk ✅
   - Not ok to for intragroup ✅
   - Not ok for highly probable transaction because already accounted for ✅
   - Not ok for NIH ✅
