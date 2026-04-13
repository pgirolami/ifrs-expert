# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Peut-on appliquer la comptabilité de couverture en consolidation à l’exposition de change résultant de dividendes intragroupe dès lors que ceux-ci ont été comptabilisés en créance à recevoir ?

**Reformulation**:
>Eligibility of intragroup monetary items (dividend receivables) as hedged items for foreign exchange risk in consolidated financial statements

## Documentation
**Consultée**
   - IAS (`ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric2`, `ifric16`)
   - IFRS (`ifrs9`, `ifrs18`, `ifrs19`, `ifrs7`)
   - SIC (`sic25`)

**Retenue pour l'analyse**
   - IAS (`ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric2`, `ifric16`)
   - IFRS (`ifrs9`, `ifrs18`, `ifrs19`, `ifrs7`)
   - SIC (`sic25`)

## Hypothèses
   - Les dividendes intragroupe ont été comptabilisés en créance à recevoir et constituent donc un élément monétaire intragroupe
   - La question porte sur les états financiers consolidés du groupe
   - L'exposition au risque de change_foreign currency risk_ concernée est le risque de fluctuation du cours de change entre la devise de la créance de dividende et la devise fonctionnelle de l'entité qui la constate
   - Aucune information n'est fournie sur les devises fonctionnelles respectives des entités du groupe impliquées

## Recommandation

**OUI SOUS CONDITIONS**

La créance de dividende intragroupe est un élément monétaire. Selon IFRS 9 §6.3.6, le risque de change des éléments monétaires intragroupe peut être désigné comme élément couvert en consolidation, à condition que les gains ou pertes de change ne soient pas éliminés lors de la consolidation conformément à IAS 21. Cette condition est remplie uniquement lorsque les filiales ont des devises fonctionnelles différentes. En l'absence d'information sur les devises fonctionnelles, la réponse est conditionnelle.

## Points Opérationnels

   - Identifier la devise fonctionnelle de chaque entité du groupe concernée par le dividende intragroupe pour déterminer si l'écart de change sera éliminé ou non en consolidation
   - Si les devises fonctionnelles diffèrent : documenter la relation de couverture conformément à IFRS 9 §6.4.1 et désigner le risque de change de la créance de dividende comme élément couvert
   - Le cas échéant, appliquer IFRIC 16 §§9-16 pour la désignation du risque couvert et la réévaluation du montant reclassé lors de la sortie de l'investissement


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilité de couverture pour les éléments monétaires intragroupe | OUI SOUS CONDITIONS | - Les filiales impliquées ont des devises fonctionnelles différentes (le dividende est libellé dans une devise autre que la devise fonctionnelle de la filiale créditrice)<br>- Le risque de change affecte le résultat consolidé (n'est pas éliminé par la consolidation)<br>- La relation de couverture satisfait aux exigences de documentation et d'efficacité de l'IFRS 9 |
| 2. Absence de comptabilité de couverture pour les éléments intragroupe | OUI SOUS CONDITIONS | - Les filiales impliquées ont la même devise fonctionnelle (ou le dividende est libellé dans la devise fonctionnelle de la filiale créditrice)<br>- Les gains/pertes de change sont entièrement éliminés lors de la consolidation |

### 1. Comptabilité de couverture pour les éléments monétaires intragroupe

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les filiales impliquées ont des devises fonctionnelles différentes (le dividende est libellé dans une devise autre que la devise fonctionnelle de la filiale créditrice)
   - Le risque de change affecte le résultat consolidé (n'est pas éliminé par la consolidation)
   - La relation de couverture satisfait aux exigences de documentation et d'efficacité de l'IFRS 9

**Raisonnement**:
La créance de dividende intragroupe est un élément monétaire (§6.3.6 IFRS 9). Elle peut être désignée comme élément couvert pour le risque de change si les gains/pertes de change ne sont pas éliminés en consolidation, ce qui se produit quand les filiales ont des devises fonctionnelles différentes (IAS 21). Dans ce cas, l'exposition au risque de change affecte le résultat consolidé et la comptabilité de couverture est permissible.

**Implications pratiques**: Désignation possible du risque de change sur la créance de dividende comme élément couvert dans les comptes consolidés avec documentation conforme à IFRS 9 §6.4.1.

**Référence**:
 - IFRS 9 6.3.5-6.3.6

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation
 - IAS 21 48

    >foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies

### 2. Absence de comptabilité de couverture pour les éléments intragroupe

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les filiales impliquées ont la même devise fonctionnelle (ou le dividende est libellé dans la devise fonctionnelle de la filiale créditrice)
   - Les gains/pertes de change sont entièrement éliminés lors de la consolidation

**Raisonnement**:
En vertu d'IFRS 9 §6.3.5, la comptabilité de couverture en consolidation ne s'applique qu'aux transactions avec des parties externes. L'exception de l §6.3.6 n'est pas disponible si les gains/pertes de change sur la créance de dividende intragroupe sont entièrement éliminés en consolidation. Cette élimination se produit lorsque les filiales ont la même devise fonctionnelle : les écarts de change sont annulés lors de la consolidation et aucun risque de change résiduel n'affecte le résultat consolidé.

**Implications pratiques**: Aucun risque de change résiduel en consolidation ; la comptabilité de couverture n'est pas applicable aux états financiers consolidés.

**Référence**:
 - IFRS 9 6.3.5

    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - IFRS 9 6.3.6

    >foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies