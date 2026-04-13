# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>L’exposition au change générée par des dividendes intragroupe, une fois la créance correspondante enregistrée, peut-elle être couverte et documentée en hedge accounting dans les comptes consolidés ?

**Reformulation**:
>Whether foreign exchange exposure from intragroup dividend receivables can qualify as a hedged item in consolidated financial statements under hedge accounting rules

## Documentation
**Consultée**
   - IAS (`ias39`, `ias21`, `ias29`)
   - IFRIC (`ifric16`, `ifric17`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs18`, `ifrs12`)
   - SIC (`sic7`)

**Retenue pour l'analyse**
   - IAS (`ias39`, `ias21`, `ias29`)
   - IFRIC (`ifric16`, `ifric17`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs18`, `ifrs12`)
   - SIC (`sic7`)

## Hypothèses
   - La créance dividendes intragroupe est un instrument monétaire libellé dans une devise étrangère
   - Les deux entités intragroupe ont des devises fonctionnelles différentes
   - L'exposition au change générée affectera le résultat consolidé

## Recommandation

**OUI SOUS CONDITIONS**

L'approche 1 (exception pour les éléments monétaires intragroupe) s'applique sous réserve que les conditions spécifiques de IFRS 9 §6.3.6 soient remplies. L'approche 2 (règle générale) exclut les transactions intragroupe de la comptabilité de couverture consolidée sauf exception. L'approche 3 (comptes séparés) constitue une alternative si les conditions de l'approche 1 ne sont pas satisfaites.

## Points Opérationnels

   - Vérifier que les devises fonctionnelles des entités impliquées sont effectivement différentes pour déterminer l'applicabilité de l'approche 1
   - Documenter la relation de couverture conformément à IFRS 9 §6.4.1 dès l'origine avec identification de l'instrument de couverture, de l'élément couvert et du risque
   - Si les devises fonctionnelles sont identiques, la couverture n'est pas disponible dans les comptes consolidés mais peut l'être dans les comptes individuels de chaque entité
   - En cas de désignation dans les comptes consolidés, l'inefficacité doit être comptabilisée en résultat et la关系 doit être évaluée régulièrement


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Exception pour élément monétaire intragroupe | OUI SOUS CONDITIONS | - La créance doit être libellée dans une devise différente de la devise fonctionnelle de l'entité qui la comptabilise<br>- Les écarts de change doivent affecter le résultat consolidé (IAS 21 §32)<br>- Documentation conforme à IFRS 9 §6.4.1 requise à l'origine |
| 2. Aucune comptabilité de couverture dans les comptes consolidés | NON | - (non spécifiées) |
| 3. Comptabilité de couverture dans les comptes individuels/séparés | OUI | - La désignation est faite dans les états financiers de l'entité qui est partie à la créance<br>- Les instruments et éléments couverts impliquent une partie externe à cette entité |

### 1. Exception pour élément monétaire intragroupe

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être libellée dans une devise différente de la devise fonctionnelle de l'entité qui la comptabilise
   - Les écarts de change doivent affecter le résultat consolidé (IAS 21 §32)
   - Documentation conforme à IFRS 9 §6.4.1 requise à l'origine

**Raisonnement**:
La créance dividendes intragroupe est un élément monétaire. Selon IFRS 9 §6.3.6, son risque de change peut être éligible si les écarts de change ne sont pas entièrement éliminés lors de la consolidation, ce qui se produit lorsque les entités ont des devises fonctionnelles différentes.

**Implications pratiques**: La couverture est possible dans les comptes consolidés uniquement si les devises fonctionnelles diffèrent.

**Référence**:
 - IFRS 9 6.3.6

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation
 - IAS 21 32

    >Exchange differences arising on a monetary item that forms part of a reporting entity's net investment in a foreign operation shall be recognised in profit or loss... in the separate financial statements... in the financial statements that include the foreign operation... such exchange differences shall be recognised initially in other comprehensive income

### 2. Aucune comptabilité de couverture dans les comptes consolidés

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La règle générale de IFRS 9 §6.3.5 exclut les transactions intragroupe de la comptabilité de couverture consolidée. Cependant, cette exclusion ne s'applique pas si l'exception de l'approche 1 est satisfaite, car cette exception constitue un cas spécifique qui prévaut sur la règle générale.

**Implications pratiques**: Cette approche est supplantée par l'exception de l'approche 1.

**Référence**:
 - IFRS 9 6.3.5

    >Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group

### 3. Comptabilité de couverture dans les comptes individuels/séparés

**Applicabilité**: OUI

**Conditions**:
   - La désignation est faite dans les états financiers de l'entité qui est partie à la créance
   - Les instruments et éléments couverts impliquent une partie externe à cette entité

**Raisonnement**:
Si les conditions de l'approche 1 ne sont pas satisfaites (ou comme alternative), la comptabilité de couverture est permise dans les comptes individuels de chaque entité car le critère de partie externe est respecté à ce niveau de reporting.

**Implications pratiques**: Les entités peuvent appliquer la comptabilité de couverture individuellement si la consolidation ne le permet pas.

**Référence**:
 - IFRS 9 6.3.5

    >Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities
 - IAS 39 80

    >they may qualify for hedge accounting in the individual or separate financial statements of individual entities within the group provided that they are external to the individual entity that is being reported on