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

#### k=2, e=5, min-score=0.5, Q1.2
**Retrieved chunks**
- ifrs-9-financial-instruments 2025 required: B3.2.12, B3.2.13, B3.2.14, B3.2.15, B3.2.16, B3.2.17, B3.3.1, B3.3.2, B3.3.3, B3.3.4, B3.3.5, B5.7.4, B5.7.5, B5.7.6, B5.7.7, B5.7.8, B5.7.9, B5.7.10, B5.7.11, B5.7.12, B5.7.13, B5.7.14
- ifric-16-hedges-of-a-net-investment-in-a-foreign-operation: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18A


**Sections mentioned in answer**
   - IFRIC 16: 2, 11, 10, 12, 5, 14, 8

**Summary table**
| Approche                                                                                    | Applicable          | Condition clé                                                              |
| ------------------------------------------------------------------------------------------- | ------------------- | -------------------------------------------------------------------------- |
| 1. Couvrir la créance de dividende comme investissement net                                 | Non                 | Le texte vise un **amount of net assets**, pas une créance de dividende    |
| 2. Couvrir l’investissement net sous-jacent, pas le dividende                               | Oui sous conditions | L’élément couvert doit être l’**investissement net** en activité étrangère |
| 3. Utiliser un dérivé ou non-dérivé dans le groupe pour une couverture d’investissement net | Oui sous conditions | Documentation, désignation et efficacité IFRS 9 / IFRIC 16                 |
| 4. Appliquer IFRIC 16 par analogie au dividende intragroupe                                 | Non                 | IFRIC 16.8 interdit l’application par analogie                             |

**Answer**
   - No to cover forex risk on dividends because IFRIC 16 says not to extend analogy ❌
   - intragroup is missing ❌
   - highly probable transaction is missing ❌
   - No for NIH ✅


=> answer hardly mentions IFRS 9

#### k=5, e=5, min-score=0.5
**Retrieved chunks**
- ifrs-9-financial-instruments 2025 required: B3.2.12, B3.2.13, B3.2.14, B3.2.15, B3.2.16, B3.2.17, B3.3.1, B3.3.2, B3.3.3, B3.3.4, B3.3.5, B5.7.4, B5.7.5, B5.7.6, B5.7.7, B5.7.8, B5.7.9, B5.7.10, B5.7.11, B5.7.12, B5.7.13, B5.7.14
- ifric-16-hedges-of-a-net-investment-in-a-foreign-operation: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18A


**Sections mentioned in answer**
   - IFRIC 16: 2, 11, 10, 12, 5, 14, 8

**Summary table**
| Approche                                                                                    | Applicable          | Condition clé                                                              |
| ------------------------------------------------------------------------------------------- | ------------------- | -------------------------------------------------------------------------- |
| 1. Couvrir la créance de dividende comme investissement net                                 | Non                 | Le texte vise un **amount of net assets**, pas une créance de dividende    |
| 2. Couvrir l’investissement net sous-jacent, pas le dividende                               | Oui sous conditions | L’élément couvert doit être l’**investissement net** en activité étrangère |
| 3. Utiliser un dérivé ou non-dérivé dans le groupe pour une couverture d’investissement net | Oui sous conditions | Documentation, désignation et efficacité IFRS 9 / IFRIC 16                 |
| 4. Appliquer IFRIC 16 par analogie au dividende intragroupe                                 | Non                 | IFRIC 16.8 interdit l’application par analogie                             |

**Answer**
   - No to cover forex risk on dividends because IFRIC 16 says not to extend analogy ❌
   - intragroup is missing ✅
   - highly probable transaction is missing ❌
   - No for NIH ✅


#### k=5, e=5, min-score=0.5, Q1.1
**Retrieved chunks**
- ifrs-9-financial-instruments 2025 required: 5.7.2, 5.7.3, 5.7.4, 5.7.5, 5.7.6, 5.7.7, 5.7.8, 5.7.9, 5.7.10, 5.7.11, 6.1.1, 6.2.6, 6.3.1, 6.3.2, 6.3.3, 6.3.4, 6.3.5, 6.3.6, 6.3.7, 6.4.1, 6.5.1, 6.5.2, B2.1, B2.2, B2.3, B2.4, B2.5, B2.6, B3.1.1, B3.1.2, B3.1.2A, B3.1.3, B3.1.4, B3.2.12, B3.2.13, B3.2.14, B3.2.15, B3.2.16, B3.2.17, B3.3.1, B3.3.2, B3.3.3, B3.3.4, B3.3.5, B5.7.4, B5.7.5, B5.7.6, B5.7.7, B5.7.8, B5.7.9, B5.7.10, B5.7.11, B5.7.12, B5.7.13, B5.7.14
- ifric-16-hedges-of-a-net-investment-in-a-foreign-operation: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18A, 19, AG1, AG2, AG3, AG4, AG5, AG6, AG7, AG8, AG9, AG10, AG11, AG12


**Sections mentioned in answer**
   - IFRS 9: 6.3.5, 6.3.6, 
   - IFRIC 16: 10, 11

**Summary table**
| Approche                                                      | Applicable          | Condition clé                                                                 |
| ------------------------------------------------------------- | ------------------- | ----------------------------------------------------------------------------- |
| Couverture de la créance intragroupe comptabilisée            | Oui sous conditions | Créance monétaire + écarts de change non totalement éliminés en consolidation |
| Couverture du dividende intragroupe futur                     | Non                 | Le risque doit affecter le résultat consolidé                                 |
| Couverture de net investment                                  | Non                 | L’élément couvert doit être un montant de net assets d’une activité étrangère |
| Documentation en comptes individuels reprise en consolidation | Non                 | Les critères spécifiques de 6.3.6 doivent être remplis au niveau consolidé    |

**Answer**
   - Yes to cover forex risk on dividends ✅ 
   - No to highly probable transaction ✅
   - No for NIH ✅
   - Missing on covering intragroup transaction ❌
   - No to individuels/séparés 🟠



#### k=5, e=5, min-score=0.5, Q1.2
**Retrieved chunks**
- ifrs-9-financial-instruments 2025 required: 5.7.2, 5.7.3, 5.7.4, 5.7.5, 5.7.6, 5.7.7, 5.7.8, 5.7.9, 5.7.10, 5.7.11, 6.1.1, B2.1, B2.2, B2.3, B2.4, B2.5, B2.6, B3.1.1, B3.1.2, B3.1.2A, B3.1.3, B3.1.4, B3.2.12, B3.2.13, B3.2.14, B3.2.15, B3.2.16, B3.2.17, B3.3.1, B3.3.2, B3.3.3, B3.3.4, B3.3.5, B5.5.53, B5.5.54, B5.5.55, B5.6.1, B5.6.2, B5.7.1, B5.7.1A, B5.7.2, B5.7.2A, B5.7.3, B5.7.4, B5.7.5, B5.7.6, B5.7.7, B5.7.8, B5.7.9, B5.7.10, B5.7.11, B5.7.12, B5.7.13, B5.7.14
- ifric-16-hedges-of-a-net-investment-in-a-foreign-operation: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18A, 18B, 19, AG1, AG2, AG3, AG4, AG5, AG6, AG7, AG8, AG9, AG10, AG11, AG12


**Sections mentioned in answer**
   - IFRS 9: B3.1.2(a), 5.7.3, B5.7.2, 6.1.1
   - IFRIC 16: 2, 10, 11

**Summary table**
| Approche                                               | Applicable          | Condition clé                                                  |
| ------------------------------------------------------ | ------------------- | -------------------------------------------------------------- |
| Couverture de juste valeur de la créance comptabilisée | Oui sous conditions | L’exposition de change doit rester pertinente en consolidation |
| Couverture d’investissement net sur le dividende       | Non                 | IFRIC 16 vise des **net assets**, pas une créance de dividende |
| Offset économique sans hedge accounting                | Non                 | Absence de désignation/documentation IFRS 9                    |
| Double désignation de la même exposition               | Non                 | Une même exposition ne doit pas être qualifiée deux fois       |

**Answer**
   - Yes to fair value hedge on receivable ❌
   - No for NIH ✅

   - Cover forex risk on dividends missing even though it mentions doing it without recognition ! ❌
   - No to highly probable transaction ✅
   - Missing on covering intragroup transaction ❌
   - No to individuels/séparés 🟠
