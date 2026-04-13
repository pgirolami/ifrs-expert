# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Reformulation**:
>Eligibility of intra-group dividend receivables for hedge accounting designation on foreign exchange risk in consolidated financial statements

## Documentation
**Consultée**
   - IAS (`ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric16`, `ifric19`)
   - IFRS (`ifrs19`, `ifrs9`, `ifrs18`, `ifrs12`)
   - SIC (`sic25`, `sic29`)

**Retenue pour l'analyse**
   - IAS (`ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric16`, `ifric19`)
   - IFRS (`ifrs19`, `ifrs9`, `ifrs18`, `ifrs12`)
   - SIC (`sic25`, `sic29`)

## Hypothèses
   - Il s'agit des comptes consolidés du groupe (et non de comptes individuels).
   - La créance dividendes intragroupe est libellée dans une devise différente de la devise fonctionnelle de l'entité qui la comptabilise.
   - Aucun traité de change spécifique n'a été mis en place pour qualifier l'exposition comme un élément monétaire éligible.

## Recommandation

**NON**

En application d'IFRS 9 §6.3.5, une créance dividendes intragroupe ne peut pas être désignée comme élément couvert dans les comptes consolidés car elle constitue une transaction avec une partie interne au groupe. L'exception prévue par IFRS 9 §6.3.6 ne s'applique qu'aux éléments monétaires intragroupe dont le risque de change affecte le résultat consolidé, ce qui n'est pas le cas ici.

## Points Opérationnels

   - Dans les comptes individuels de la fille distributrice, le dividende est exigible et peut être considéré comme un élément monétaire ; dans ces comptes, une documentation de couverture pourrait être envisagée si le risque affecte le résultat individuel.
   - Dans les comptes consolidés, la créance dividendes intragroupe est éliminée et ne constitue pas une exposition externe au groupe.
   - Le groupe peut cependant chercher à couvrir le risque de change au niveau de la transaction finale (par exemple, sur le dividende effectivement versé à des actionnaires externes) en utilisant des instruments dérivés externes.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Impossibilité d'applique la comptabilité de couverture sur des créances dividendes intragroupe | OUI | - La créance dividendes intragroupe doit être éliminée en consolidation.<br>- Le risque de change doit concerner une partie externe au groupe. |
| 2. Exception pour les éléments monétaires intragroupe | NON | - L'élément doit être monétaire au sens d'IAS 21.<br>- Le risque de change doit affecter le résultat consolidé après élimination.<br>- L'exposition doit être avec une partie interne mais résulter en un impact consolidé réel. |

### 1. Impossibilité d'applique la comptabilité de couverture sur des créances dividendes intragroupe

**Applicabilité**: OUI

**Conditions**:
   - La créance dividendes intragroupe doit être éliminée en consolidation.
   - Le risque de change doit concerner une partie externe au groupe.

**Raisonnement**:
La créance de dividende intragroupe est une exposition avec une partie interne au groupe. En consolidated statements, les dividendes intragroupe sont éliminés à la consolidation ; ils ne génèrent pas d'exposition au risque de change avec une partie externe. IFRS 9 §6.3.5 exclut expressément les transactions intragroupe de l'éligibilité à la comptabilité de couverture.

**Implications pratiques**: Aucune documentation de couverture ne peut être établie sur cette créance dans les comptes consolidés.

**Référence**:
 - IFRS 9 6.3.5

    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - IFRIC 16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity's functional currency

### 2. Exception pour les éléments monétaires intragroupe

**Applicabilité**: NON

**Conditions**:
   - L'élément doit être monétaire au sens d'IAS 21.
   - Le risque de change doit affecter le résultat consolidé après élimination.
   - L'exposition doit être avec une partie interne mais résulter en un impact consolidé réel.

**Raisonnement**:
L'exception d'IFRS 9 §6.3.6 ne s'applique qu'aux éléments monétaires intragroupe (tels que des prête/receive entre deux filles). Une créance de dividende, avant sa constatation comme élément financier, n'est pas automatiquement un élément monétaire au sens d'IAS 21. De plus, le dividende intragroupe est éliminé en consolidation et son risque de change ne se traduit pas par un impact sur le résultat consolidé.

**Implications pratiques**: Cette exception ne permet pas de couvrir la créance dividendes intragroupe.

**Référence**:
 - IFRS 9 6.3.6

    >as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation