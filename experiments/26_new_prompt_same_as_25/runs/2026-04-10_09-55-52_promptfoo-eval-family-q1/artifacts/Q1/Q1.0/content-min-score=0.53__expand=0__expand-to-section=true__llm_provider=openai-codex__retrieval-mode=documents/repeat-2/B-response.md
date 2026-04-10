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
   - La question vise les comptes consolidés IFRS.
   - Le dividende intragroupe a donné lieu à une créance et une dette intragroupe déjà comptabilisées.
   - La créance à recevoir est exposée à un risque de change entre des entités du groupe ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la documentation de couverture n’est envisageable que de façon limitée. Elle peut être possible sur le risque de change d’une créance intragroupe comptabilisée seulement si ce risque n’est pas entièrement éliminé en consolidation; sinon, non. Les modèles cash flow hedge et net investment hedge ne correspondent pas à ce fait précis.

## Points Opérationnels

   - Le test se fait au niveau des comptes consolidés, pas seulement dans les comptes individuels des entités du groupe.
   - Le point décisif est de savoir si les écarts de change sur la créance/dette de dividende intragroupe sont ou non entièrement éliminés à la consolidation.
   - Si la créance est déjà comptabilisée, l’analyse pertinente est celle d’un poste reconnu, pas celle d’une transaction future.
   - La documentation doit être cohérente avec le risque effectivement conservé en consolidation et avec l’exception étroite prévue pour les éléments monétaires intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un élément monétaire exposé au change.<br>- Les gains ou pertes de change correspondants ne doivent pas être entièrement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un élément monétaire exposé au change.
   - Les gains ou pertes de change correspondants ne doivent pas être entièrement éliminés en consolidation.

**Raisonnment**:
Une créance comptabilisée est, en principe, un type d’élément pouvant être couvert. Mais en comptes consolidés, seuls des actifs, passifs, engagements fermes ou transactions prévues avec une partie externe peuvent être désignés, sauf exception pour le risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés en consolidation. Donc votre cas n’est possible que dans cette exception étroite.

**Implications pratiques**: Documenter la couverture au niveau consolidé n’est défendable que sur le risque de change résiduel conservé en consolidation.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans votre situation, il existe déjà une créance comptabilisée au titre d’un dividende déclaré. Ce n’est donc plus une transaction future hautement probable à couvrir en flux de trésorerie, mais une exposition sur un poste reconnu. En outre, en consolidation, les éléments intragroupe ne sont en principe pas éligibles sauf exceptions ciblées sur le change d’éléments monétaires, ce qui renvoie plutôt au modèle de couverture d’un poste reconnu.

**Implications pratiques**: Le modèle cash flow hedge ne correspond pas à un dividende intragroupe déjà constaté en créance.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur le risque de change d’un dividende intragroupe ayant déjà donné lieu à une créance à recevoir, non sur l’exposition de conversion liée à un investissement net dans une activité à l’étranger. IFRIC 16 vise la couverture du risque de change de l’investissement net lui-même. Ce modèle n’est donc pas le bon pour une créance de dividende intragroupe comptabilisée.

**Implications pratiques**: Ne pas utiliser la documentation de couverture d’investissement net pour une créance de dividende intragroupe.

**Référence**:
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity
 - 13
    >An exposure to foreign currency risk arising from a net investment in a foreign operation may qualify for hedge accounting only once