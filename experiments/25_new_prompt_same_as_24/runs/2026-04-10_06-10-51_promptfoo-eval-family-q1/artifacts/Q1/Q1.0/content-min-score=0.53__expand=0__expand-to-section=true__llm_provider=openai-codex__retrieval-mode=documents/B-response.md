# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ias32`
   - `ifrs19`
   - `ifric17`
   - `ifrs9`
   - `ifrs18`
   - `ifrs12`
   - `ias7`
   - `ias37`
   - `sic25`
   - `ifric16`
   - `sic29`
   - `ifric19`

## Hypothèses
   - La question vise des comptes consolidés IFRS.
   - Le dividende intragroupe a déjà donné lieu à la comptabilisation d’une créance à recevoir.
   - Le risque visé est le risque de change sur cette créance intragroupe ou sur le flux correspondant.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidé, une documentation de couverture peut être envisagée sur le risque de change d’une créance intragroupe déjà comptabilisée si cette créance est un élément monétaire entre entités à monnaies fonctionnelles différentes et si les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas, l’approche pertinente est la couverture de juste valeur, pas la couverture de flux de trésorerie ni la couverture d’investissement net.

## Points Opérationnels

   - Le point clé en consolidé est de vérifier si la créance de dividende est bien un élément monétaire entre entités à monnaies fonctionnelles différentes.
   - Si les écarts de change sur cette créance sont totalement éliminés en consolidation, l’exception IFRS 9 sur les éléments intragroupe ne permet pas la désignation.
   - Comme la créance est déjà reconnue, la documentation doit viser un poste existant et non une transaction future de dividende.
   - La conclusion doit être arrêtée au niveau des comptes consolidés, pas seulement dans les comptes individuels des entités du groupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit constituer un élément monétaire intragroupe.<br>- Les entités concernées doivent avoir des monnaies fonctionnelles différentes.<br>- Le risque de change doit générer des écarts de change non totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit constituer un élément monétaire intragroupe.
   - Les entités concernées doivent avoir des monnaies fonctionnelles différentes.
   - Le risque de change doit générer des écarts de change non totalement éliminés en consolidation.

**Raisonnment**:
Dans votre situation, la créance de dividende est déjà comptabilisée : on n’est donc plus sur une transaction future mais sur un actif reconnu. En consolidé, les éléments intragroupe ne sont en principe pas éligibles, sauf l’exception IFRS 9 pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation.

**Implications pratiques**: La relation de couverture peut être documentée en consolidé sur le seul risque de change de la créance reconnue, si l’exception intragroupe est satisfaite.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise une transaction future prévue et hautement probable. Or, dans votre cas, une créance de dividende a déjà été comptabilisée : le sujet n’est donc plus un flux futur non reconnu mais un poste monétaire existant. L’analyse doit alors se faire sur le poste reconnu, pas comme cash flow hedge.

**Implications pratiques**: Une documentation de couverture de flux de trésorerie ne correspond pas aux faits décrits dès lors que le dividende est déjà comptabilisé en créance.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d’investissement net vise l’exposition de change sur les actifs nets d’une activité à l’étranger, pas une créance de dividende intragroupe déjà constatée. Les extraits fournis d’IFRIC 16 traitent du hedge d’un net investment et non du change sur un dividende à recevoir.

**Implications pratiques**: Cette documentation n’est pas adaptée à une créance de dividende intragroupe reconnue.

**Référence**:
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity
 - 13
    >An exposure to foreign currency risk arising from a net investment in a foreign operation may qualify for hedge accounting only once