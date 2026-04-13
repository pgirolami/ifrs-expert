# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Des dividendes intragroupe ont été comptabilisés à recevoir, ce qui fait naître une variation potentielle liée au change dans les comptes consolidés. Est-il alors possible de mettre en place une relation de couverture sur cette seule composante de change ?

**Reformulation**:
>Whether a foreign currency risk component of an intragroup dividend receivable can be designated as a hedged item in a hedge accounting relationship in consolidated financial statements, given the prohibition on hedging transactions between entities in the same group.

## Documentation
**Consultée**
   - IAS (`ias21`, `ias24`, `ias37`, `ias26`)
   - IFRIC (`ifric17`, `ifric16`, `ifric1`, `ifric23`, `ifric22`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs2`, `ifrs12`)
   - SIC (`sic25`, `sic7`, `sic29`)

**Retenue pour l'analyse**
   - IAS (`ias21`, `ias24`, `ias37`, `ias26`)
   - IFRIC (`ifric17`, `ifric16`, `ifric1`, `ifric23`, `ifric22`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs2`, `ifrs12`)
   - SIC (`sic25`, `sic7`, `sic29`)

## Hypothèses
   - Les deux entités du groupe ont des devises fonctionnelles différentes.
   - La variation de change sur la créance dividendes intragroupe n'est pas éliminée à la consolidation.
   - L'entité qui reçoit le dividende intragroupe prépare des états financiers consolidés.

## Recommandation

**OUI**

L'approche 1 est applicable en virtud de l'exception prévue au paragraphe 6.3.6 d'IFRS 9, qui permet spécifiquement de couvrir le risque de change d'un élément monétaire intragroupe dans les états financiers consolidés lorsque les différences de change ne sont pas entièrement éliminées à la consolidation. Les dividendes intragroupe créent une exposition en devise et relèvent de cette exception.

## Points Opérationnels

   - Documenter clairement que seule la composante risque de change est désignée comme élément couvert.
   - Satisfaire les conditions de désignation et d'efficacité selon IFRS 9 paragraphe 6.4.1.
   - Vérifier que les différences de change ne sont pas éliminées à la consolidation (IAS 21 paragraphe 45).


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilisation de couverture sur l'élément monétaire intragroupe | OUI | - Les devises fonctionnelles des deux entités du groupe doivent être différentes.<br>- Les différences de change ne doivent pas être éliminées à la consolidation.<br>- Les exigences de documentation et d'efficacité d'IFRS 9 paragraphe 6.4.1 doivent être satisfaites. |
| 2. Absence de comptabilité de couverture sur la créance dividendes intragroupe | NON | - (non spécifiées) |

### 1. Comptabilisation de couverture sur l'élément monétaire intragroupe

**Applicabilité**: OUI

**Conditions**:
   - Les devises fonctionnelles des deux entités du groupe doivent être différentes.
   - Les différences de change ne doivent pas être éliminées à la consolidation.
   - Les exigences de documentation et d'efficacité d'IFRS 9 paragraphe 6.4.1 doivent être satisfaites.

**Raisonnement**:
Le paragraphe 6.3.6 d'IFRS 9 crée une exception explicite pour le risque de change des éléments monétaires intragroupe dans les comptes consolidés. Une créance dividendes intragroupe en devise étrangère constitue un élément monétaire dont les différences de change ne sont pas éliminées à la consolidation selon IAS 21. De plus, le paragraphe 6.3.1 permet de désigner un composant d'un élément comme élément couvert.

**Implications pratiques**: L'entreprise peut désigner le risque de change de la créance dividendes intragroupe comme risque couvert et appliquer la comptabilité de couverture dans ses états financiers consolidés.

**Référence**:
 - IFRS 9 6.3.6

    >The foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation.
 - IFRS 9 6.3.1

    >A hedged item can be a recognised asset or liability [...] A hedged item can also be a component of such an item or group of items.

### 2. Absence de comptabilité de couverture sur la créance dividendes intragroupe

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La règle générale du paragraphe 6.3.5 interdisant la couverture des transactions intragroupe dans les comptes consolidés ne s'applique pas ici car elle est supplantée par l'exception spécifique du paragraphe 6.3.6. Celle-ci autorise explicitement la couverture du risque de change des éléments monétaires intragroupe lorsque les différences de change ne sont pas éliminées à la consolidation.

**Implications pratiques**: Non applicable car l'exception de 6.3.6 permet la désignation.

**Référence**:
 - IFRS 9 6.3.5

    >Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group.