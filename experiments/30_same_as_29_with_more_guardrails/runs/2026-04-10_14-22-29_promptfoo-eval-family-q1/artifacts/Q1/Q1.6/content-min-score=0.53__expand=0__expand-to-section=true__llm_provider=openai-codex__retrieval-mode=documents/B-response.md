# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Dans les comptes consolidés, la variation de change relative à des dividendes intragroupe pour lesquels un receivable a été constaté est-elle éligible à une désignation en comptabilité de couverture ?

**Documentation consultée**
   - `ifric17`
   - `ifrs9`
   - `ifrs19`
   - `ias21`
   - `ias7`
   - `sic25`
   - `ifric16`
   - `ias37`

## Hypothèses
   - Le dividende intragroupe a été déclaré et a donné lieu à la comptabilisation d'une créance/dividende à recevoir entre deux entités du groupe.
   - La créance est un élément monétaire libellé dans une devise et concerne les comptes consolidés.
   - Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que l'écart de change sur cet élément monétaire n'est pas entièrement éliminé en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Dans les comptes consolidés, le risque de change d'un dividende intragroupe déjà comptabilisé en créance peut être éligible à une désignation de couverture seulement s'il s'agit d'un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur ; la couverture de flux de trésorerie et la couverture d'investissement net ne conviennent pas, sauf faits additionnels très spécifiques.

## Points Opérationnels

   - Le point clé est le niveau de reporting : l'exception IFRS 9 vise les comptes consolidés, pas seulement les comptes individuels.
   - Il faut démontrer que l'écart de change sur la créance de dividende intragroupe affecte bien le résultat consolidé parce qu'il n'est pas totalement éliminé.
   - Si la créance est déjà reconnue, la documentation de couverture doit viser le risque de change de cet actif monétaire reconnu.
   - En l'absence de monnaies fonctionnelles différentes ou si l'écart de change est totalement éliminé en consolidation, l'éligibilité disparaît.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende est un élément monétaire intragroupe<br>- le risque de change affecte le résultat consolidé car les écarts ne sont pas totalement éliminés<br>- la désignation porte sur le risque de change de la créance reconnue |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende est un élément monétaire intragroupe
   - le risque de change affecte le résultat consolidé car les écarts ne sont pas totalement éliminés
   - la désignation porte sur le risque de change de la créance reconnue

**Raisonnment**:
Ici, la créance de dividende déjà constatée est un actif reconnu. En consolidation, IFRS 9 autorise par exception la désignation du risque de change d'un élément monétaire intragroupe comme élément couvert si ce risque génère des écarts de change non totalement éliminés. C'est précisément le cas visé pour une créance/dividende intragroupe en devise entre entités à monnaies fonctionnelles différentes.

**Implications pratiques**: La désignation est envisageable en consolidation comme couverture du risque de change de la créance de dividende reconnue.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 45
    >cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise un dividende intragroupe pour lequel une créance a déjà été comptabilisée. On n'est donc plus face à une transaction future hautement probable, mais à un actif monétaire reconnu. Dans ces faits, le modèle de cash flow hedge n'est pas le plus adapté à la variation de change d'une créance déjà existante.

**Implications pratiques**: La variation de change de la créance reconnue ne serait pas désignée en couverture de flux de trésorerie dans cette situation.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Une créance de dividende intragroupe déclarée correspond normalement à un montant à régler, pas à un élément faisant partie de l'investissement net dans une activité à l'étranger. Le modèle de couverture d'investissement net vise les expositions de conversion liées à un investissement net, non un dividende à recevoir déjà détaché et exigible.

**Implications pratiques**: Sauf fait très particulier montrant que l'élément fait partie de l'investissement net, cette désignation n'est pas appropriée.

**Référence**:
 - 32
    >a monetary item that forms part of a reporting entity’s net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation