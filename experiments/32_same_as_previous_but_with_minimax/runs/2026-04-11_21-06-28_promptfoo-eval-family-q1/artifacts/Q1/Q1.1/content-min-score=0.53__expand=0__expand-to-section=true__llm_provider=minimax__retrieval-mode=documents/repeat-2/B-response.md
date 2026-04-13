# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Reformulation**:
>Accounting for foreign exchange risk on intragroup dividend receivables using hedge accounting in consolidated financial statements

## Documentation
**Consultée**
   - IAS (`ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric2`, `ifric19`, `ifric16`)
   - IFRS (`ifrs19`, `ifrs18`, `ifrs9`, `ifrs12`)
   - SIC (`sic25`)

**Retenue pour l'analyse**
   - IAS (`ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric2`, `ifric19`, `ifric16`)
   - IFRS (`ifrs19`, `ifrs18`, `ifrs9`, `ifrs12`)
   - SIC (`sic25`)

## Hypothèses
   - Le dividende intragroupe est comptabilisé comme une créance financière (actif monétaire) dans les comptes consolidés
   - La question porte sur la couverture du risque de change dans les états financiers consolidés du groupe
   - L'exposition au change du dividende intragroupe affecte effectivement le résultat consolidé (n'est pas éliminée par consolidation)

## Recommandation

**OUI SOUS CONDITIONS**

L'approche IFRS 9 (exception intragroupe) est applicable sous condition que le dividende crée une exposition au risque de change non éliminée à la consolidation. Les approches 2 et 3 constituent des alternatives ou des limites selon le contexte spécifique.

## Points Opérationnels

   - Identifier la devise fonctionnelle de chaque entité pour déterminer si le dividende crée une exposition au change dans les comptes consolidés
   - Documenter la relation de couverture dès l'origine avec désignation formelle de l'élément couvert, de l'instrument de couverture et de la nature du risque couvert
   - Tester l'efficacité de la relation de couverture de manière prospective et rétrospective selon IFRS 9 §6.4.1
   - Si plusieurs entités du groupe détiennent des instruments de couverture, assurer que la stratégie de couverture est cohérente et documentée au niveau du groupe
   - Considérer les exigences de présentation selon IFRS 18 pour la classification des produits et charges de couverture


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture IFRS 9 avec exception pour les postes monétaires intragroupe | OUI SOUS CONDITIONS | - Les entités émettrice et réceptrice du dividende ont des devises fonctionnelles différentes<br>- Les écarts de change ne sont pas entièrement éliminés à la consolidation selon IAS 21<br>- La relation de couverture est documentée conformément aux exigences de IFRS 9 §6.4.1 |
| 2. Exposition de change non couverte selon IAS 21 | OUI SOUS CONDITIONS | - Les écarts de change sur la créance de dividende sont entièrement éliminés à la consolidation<br>- Aucune exposition au risque de change n'affecte le résultat consolidé |
| 3. Couverture d'investissement net dans une opération étrangère | OUI SOUS CONDITIONS | - La créance de dividende concerne une filiale étrangère (opération étrangère)<br>- L'objectif de couverture est de protéger l'investissement net dans la filiale étrangère<br>- Les instruments de couverture peuvent être détenus par n'importe quelle entité du groupe |

### 1. Couverture IFRS 9 avec exception pour les postes monétaires intragroupe

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les entités émettrice et réceptrice du dividende ont des devises fonctionnelles différentes
   - Les écarts de change ne sont pas entièrement éliminés à la consolidation selon IAS 21
   - La relation de couverture est documentée conformément aux exigences de IFRS 9 §6.4.1

**Raisonnement**:
Le dividende intragroupe comptabilisé en créance constitue un poste monétaire intragroupe. Selon IFRS 9 §6.3.6, ce poste peut être désigné comme élément couvert dans les comptes consolidés si le risque de change affecte le résultat consolidé (non éliminé par consolidation). Cette exception s'applique spécifiquement aux dividendes intragroupe en créance lorsque les entités ont des devises fonctionnelles différentes.

**Implications pratiques**: Le groupe peut désigner le risque de change sur la créance de dividende comme élément couvert et utiliser un instrument dérivé (par exemple, contrat à terme) comme instrument de couverture avec traitement comptable de couverture.

**Référence**:
 - IFRS 9 6.3.6

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation
 - IAS 32 35

    >Interest, dividends, losses and gains relating to a financial instrument or a component that is a financial liability shall be recognised as income or expense in profit or loss

### 2. Exposition de change non couverte selon IAS 21

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les écarts de change sur la créance de dividende sont entièrement éliminés à la consolidation
   - Aucune exposition au risque de change n'affecte le résultat consolidé

**Raisonnement**:
Si l'écart de change sur la créance de dividende intragroupe est entièrement éliminé à la consolidation (par exemple, parce que les deux entités ont la même devise fonctionnelle ou que l'élimination intragroupe neutralise l'effet), aucune couverture n'est disponible selon IFRS 9 §6.3.5. Dans ce cas, les écarts de change sont traités selon IAS 21 et peuvent être reconnus en résultat ou en autres éléments du résultat global selon la situation.

**Implications pratiques**: En l'absence de couverture, les écarts de change sur la créance de dividende sont comptabilisés selon IAS 21, sans possibilité d'appliquer les règles de comptabilité de couverture.

**Référence**:
 - IFRS 9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items

### 3. Couverture d'investissement net dans une opération étrangère

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende concerne une filiale étrangère (opération étrangère)
   - L'objectif de couverture est de protéger l'investissement net dans la filiale étrangère
   - Les instruments de couverture peuvent être détenus par n'importe quelle entité du groupe

**Raisonnement**:
IFRIC 16 permet de désigner des instruments de couverture pour couvrir le risque de change d'un investissement net dans une opération étrangère. Si la créance de dividende provient d'une filiale étrangère et que le groupe souhaite protéger la valeur de cet investissement, une couverture d'investissement net peut être mise en place. Cependant, cette approche cible l'investissement net plutôt que directement la créance de dividende.

**Implications pratiques**: L'instrument de couverture (dérivé ou non dérivé) est désigné comme couverture d'investissement net, et la portion efficace de la variation de valeur est reconnue en autres éléments du résultat global.

**Référence**:
 - IFRIC 16 14

    >A derivative or a non-derivative instrument may be designated as a hedging instrument in a hedge of a net investment in a foreign operation
 - IFRIC 16 15

    >the change in value of the hedging instrument in respect of foreign exchange risk is computed by reference to the functional currency of the parent entity