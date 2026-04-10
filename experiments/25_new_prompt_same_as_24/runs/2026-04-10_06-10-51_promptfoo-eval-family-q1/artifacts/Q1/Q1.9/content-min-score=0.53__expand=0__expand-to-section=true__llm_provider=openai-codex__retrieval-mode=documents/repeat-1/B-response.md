# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>La composante de risque de change liée à des dividendes intragroupe reconnus sous forme de créance peut-elle être désignée comme élément couvert dans les comptes consolidés ?

**Documentation consultée**
   - `ifrs9`
   - `ifrs19`
   - `ifric2`
   - `ifric16`
   - `ias32`
   - `ifric17`
   - `sic7`
   - `ias37`

## Hypothèses
   - La question porte sur la comptabilité de couverture en comptes consolidés selon IFRS 9 pour un risque de change.
   - Le dividende intragroupe a déjà été comptabilisé en créance intercompagnie, donc comme un élément monétaire.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via l’exception IFRS 9 applicable aux éléments monétaires intragroupe en comptes consolidés. Il faut que la créance de dividende génère des écarts de change qui ne sont pas intégralement éliminés en consolidation, notamment entre entités de devises fonctionnelles différentes.

## Points Opérationnels

   - Vérifier en premier lieu si la créance de dividende est bien un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes.
   - Confirmer que les écarts de change sur cette créance ne sont pas entièrement éliminés en consolidation ; c’est la condition décisive de l’exception IFRS 9.
   - En pratique, si les conditions sont remplies, la désignation relève de la logique d’une couverture de juste valeur d’un actif reconnu, pas d’une couverture de flux futurs ni d’un investissement net.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe<br>- Les entités concernées ont des monnaies fonctionnelles différentes<br>- Les écarts de change correspondants ne sont pas intégralement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe
   - Les entités concernées ont des monnaies fonctionnelles différentes
   - Les écarts de change correspondants ne sont pas intégralement éliminés en consolidation

**Raisonnment**:
La créance de dividende reconnue est, selon l’hypothèse retenue, un actif monétaire intragroupe. En comptes consolidés, IFRS 9 n’autorise en principe que des éléments avec des tiers, mais prévoit une exception pour le risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas entièrement éliminés en consolidation. Dans ce cas précis, la désignation comme élément couvert est possible.

**Implications pratiques**: La documentation de couverture doit viser spécifiquement le risque de change de la créance intragroupe reconnue en consolidation.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans la situation décrite, le dividende intragroupe est déjà reconnu sous forme de créance. On n’est donc pas face à une transaction future hautement probable, mais à un actif monétaire existant. L’approche de couverture de flux de trésorerie ne correspond pas au fait générateur décrit.

**Implications pratiques**: Cette voie n’est pas adaptée une fois le dividende déjà comptabilisé en créance intragroupe.

**Référence**:
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions

### 3. Couverture d’un investissement net dans une activité à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé ici porte sur une créance de dividende intragroupe reconnue, non sur l’investissement net dans l’activité étrangère. IFRIC 16 réserve cette forme de couverture au risque de change sur les actifs nets de l’activité étrangère inclus dans les états financiers. Le fait décrit ne correspond donc pas à cet objet de couverture.

**Implications pratiques**: Il ne faut pas assimiler une créance de dividende intragroupe à un investissement net couvert.

**Référence**:
 - 2
    >the item being hedged ... may be an amount of net assets
 - 7
    >applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations
 - 8
    >applies only to hedges of net investments in foreign operations