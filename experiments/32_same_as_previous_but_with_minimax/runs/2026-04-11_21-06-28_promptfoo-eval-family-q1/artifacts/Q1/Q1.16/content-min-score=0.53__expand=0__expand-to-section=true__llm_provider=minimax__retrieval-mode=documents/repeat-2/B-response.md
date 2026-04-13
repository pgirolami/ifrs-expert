# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Au niveau consolidé, l’entité constate une créance liée à des dividendes intragroupe et supporte, de ce fait, une exposition au risque de change. Cette exposition peut-elle faire l’objet d’une documentation de couverture conforme aux IFRS ?

**Reformulation**:
>Eligibility of intragroup dividend receivable for IFRS hedge accounting for foreign currency risk

## Documentation
**Consultée**
   - IAS (`ias32`, `ias21`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric16`, `ifric19`, `ifric21`, `ifric23`, `ifric1`)
   - IFRS (`ifrs19`, `ifrs7`, `ifrs9`, `ifrs12`)
   - PS (`ps1`)
   - SIC (`sic25`, `sic29`, `sic7`)

**Retenue pour l'analyse**
   - IAS (`ias32`, `ias21`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric16`, `ifric19`, `ifric21`, `ifric23`, `ifric1`)
   - IFRS (`ifrs19`, `ifrs7`, `ifrs9`, `ifrs12`)
   - PS (`ps1`)
   - SIC (`sic25`, `sic29`, `sic7`)

## Hypothèses
   - L'entité est en contexte consolidé (pas en IFRS individuelle/séparée)
   - La créance dividendes intragroupe est libellée en monnaie étrangère
   - Les deux parties ont des devises fonctionnelles différentes
   - L'exposition au risque de change n'est pas totalement éliminée à la consolidation

## Recommandation

**OUI SOUS CONDITIONS**

L'exception de l'IFRS 9 §6.3.6 autorise la désignation du risque de change d'un poste monétaire intragroupe en élément couvert dans les états financiers consolidés, à condition que les différences de change ne soient pas totalement éliminées à la consolidation (IAS 21 §45).

## Points Opérationnels

   - Vérifier que la créance dividendes intragroupe n'est pas éliminée à la consolidation du fait de devises fonctionnelles différentes entre les entités du groupe (condition clé de l'exception §6.3.6)
   - Documenter formalement la relation de couverture dès l'origine et démontrer l'efficacité prospectif et retrospectif
   - Choisir entre couverture en juste valeur (approche 1) ou couverture de flux de trésorerie (approche 2) selon la nature de l'exposition que l'entité souhaite gérer
   - Si aucune couverture n'est souhaitée, appliquer le traitement par défaut IAS 21 §45


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture en juste valeur du risque de change sur créance dividendes intragroupe | OUI SOUS CONDITIONS | - Le poste monétaire intragroupe génère une exposition aux gains ou pertes de change non éliminée à la consolidation (IAS 21 §45)<br>- La documentation de couverture est正式isée et l'efficacité est démontrée (IFRS 9 §6.4.1)<br>- L'exposition désigne le risque de change entre la devise fonctionnelle de l'entité détentrice et la devise de règlement du dividende |
| 2. Couverture de flux de trésorerie pour le risque de change sur créance dividendes intragroupe | OUI SOUS CONDITIONS | - Même condition de non-élimination à la consolidation (IAS 21 §45)<br>- Documentation conforme et efficacité démontrée (IFRS 9 §6.4.1)<br>- Le risque désigné est la variabilité des flux de trésorerie futurs en devise fonctionnelle liés au dividende à recevoir |
| 3. Constatation des différences de change en résultat (ou OCI) sans désignation de couverture | OUI | - Aucune désignation de relation de couverture n'est effectuée |

### 1. Couverture en juste valeur du risque de change sur créance dividendes intragroupe

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le poste monétaire intragroupe génère une exposition aux gains ou pertes de change non éliminée à la consolidation (IAS 21 §45)
   - La documentation de couverture est正式isée et l'efficacité est démontrée (IFRS 9 §6.4.1)
   - L'exposition désigne le risque de change entre la devise fonctionnelle de l'entité détentrice et la devise de règlement du dividende

**Raisonnement**:
En vertu de l'exception IFRS 9 §6.3.6, une créance intragroupe libellée en devise étrangère constitue un élément éligible à la couverture dans les comptes consolidés, dès lors que le risque de change n'est pas éliminé à la consolidation.

**Implications pratiques**: Les variations de juste valeur attribuables au risque de change sont reconnues en résultat, avec un ajustement symétrique sur l'élément couvert.

**Référence**:
 - IFRS 9 6.3.6

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation
 - IAS 21 45

    >an intragroup monetary asset cannot be eliminated without showing the results of currency fluctuations in the consolidated financial statements

### 2. Couverture de flux de trésorerie pour le risque de change sur créance dividendes intragroupe

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Même condition de non-élimination à la consolidation (IAS 21 §45)
   - Documentation conforme et efficacité démontrée (IFRS 9 §6.4.1)
   - Le risque désigné est la variabilité des flux de trésorerie futurs en devise fonctionnelle liés au dividende à recevoir

**Raisonnement**:
L'IFRS 9 autorise également la désignation en couverture de flux de trésorerie pour un poste monétaire libellé en devise étrangère. Les conditions et l'exception du §6.3.6 s'appliquent de la même manière.

**Implications pratiques**: La partie efficace de la couverture est présentée enOCI jusqu'à réalisation du dividende ; la partie inefficace est reconnue en résultat.

**Référence**:
 - IFRS 9 6.3.6

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements
 - IFRS 9 6.6.1–6.6.6

    >Specifies accounting for cash flow hedges

### 3. Constatation des différences de change en résultat (ou OCI) sans désignation de couverture

**Applicabilité**: OUI

**Conditions**:
   - Aucune désignation de relation de couverture n'est effectuée

**Raisonnement**:
À défaut de désignation en couverture, les différences de change sur la créance intragroupe sont reconnues en résultat (ou en OCI en cas de参​照 IAS 21 §32) conformément à IAS 21 §45. C'est le traitement par défaut.

**Implications pratiques**: Les écarts de change sont comptabilisés immédiatement en résultat, sans adjustment symétrique.

**Référence**:
 - IAS 21 45

    >in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or in other comprehensive income