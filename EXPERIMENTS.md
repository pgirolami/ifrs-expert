# 2026-03-24

## Minimum context to see NIH appear

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

### top-k chunks from IFRS 9 + IFRIC 16
#### k=5
**Retrieved chunks**
   - 6.3.5, B6.3.5, 6.3.6, B2.6, 2.1

**Answer**
   - Ok to cover forex risk ✅
   - Not ok to for intragroup ✅
   - No to highly probable transaction because already accounted for ✅
   - Doesn't mention NIH which is not surprising since retrieval didn't include any IFRIC 16 sections ❌

**Sections mentioned in answer**
TODO

**Summary table**
| Approche                                                                     | Applicable          | Condition clé                                                |
| ---------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------ |
| Créance de dividendes intragroupe déjà comptabilisée comme élément monétaire | Oui sous conditions | Écarts de change non entièrement éliminés en consolidation   |
| Application de la règle générale aux éléments intragroupe                    | Non                 | Les hedged items doivent en principe être externes au groupe |
| Transaction intragroupe future hautement probable                            | Non dans ce cas     | La créance est déjà comptabilisée                            |
| Couverture d’un risque de change sans effet sur le résultat consolidé        | Non                 | Le risque doit affecter le résultat consolidé                |

#### k=20
**Retrieved chunks**
   - ifrs9_6.3.5, ifrs9_B6.3.5, ifrs9_6.3.6, ifrs9_B2.6, ifrs9_2.1
   - ifrs9_5, ifrs9_B6.3.6, ifrs9_4.3.4, ifrs9_B5.7.9, ifrs9_B4.3.4
   - ifrs9_2.3, ifrs9_7.2.26, ifrs9_5.7.1, ifrs9_B4.3.12, ifrs9_6.9.6
   - ifrs9_B2.5, ifrs9_3, ifrs9_6.6.3, ifrs9_13, ifrs9_4.2.2
   - ifrs9_5.2.3, ifrs9_3.3.5, ifric16_14, ifrs9_5.7.1A, ifrs9_5.7.3
   - ifrs9_5.7.7, ifrs9_B3.2.17, ifrs9_B5.7.1, ifrs9_B5.7.2, ifric16_AG6
   - ifrs9_B4.3.11, ifrs9_B4.1.36, ifrs9_6.1.3, ifrs9_B4.1.30, ifrs9_7.2.34
   - ifrs9_5.7.8, ifrs9_B3.2.10, ifric16_17, ifrs9_4.3.5

**Answer**
TODO

**Sections mentioned in answer**
   - 6.3.6
   - 6.3.5
   - B6.3.6


**Summary table**
TODO

#### k=40
**Retrieved chunks**
   - 6.3.5, B6.3.5, 6.3.6, B2.6, 2.1
   - 5, B6.3.6, 4.3.4, B5.7.9, B4.3.4
   - 2.3, 7.2.26, 5.7.1, B4.3.12, 6.9.6
   - B2.5, 3, 6.6.3, 13, 4.2.2

**Summary table**
| Approche                                                                    | Applicable          | Condition clé                                                |
| --------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------ |
| Créance de dividende intragroupe déjà comptabilisée comme élément monétaire | Oui sous conditions | Écarts de change non totalement éliminés en consolidation    |
| Dividende intragroupe comme transaction future                              | Non                 | N’affecte pas le résultat consolidé                          |
| Créance intragroupe mais exposition totalement éliminée                     | Non                 | Absence d’exposition résiduelle en consolidation             |
| Documentation dans les comptes individuels/séparés                          | Oui                 | Documentation au niveau de l’entité, pas au niveau consolidé |

**Review**
   - NIH coverage is still not mentioned even though some IFRIC 16 chunks were reported
   - doesn't mention highly-probable transactions to eliminate it but does mention "couverture de flux" and reject it


### top-k chunks + expand to p nearby chunks
#### k=5
##### p=5