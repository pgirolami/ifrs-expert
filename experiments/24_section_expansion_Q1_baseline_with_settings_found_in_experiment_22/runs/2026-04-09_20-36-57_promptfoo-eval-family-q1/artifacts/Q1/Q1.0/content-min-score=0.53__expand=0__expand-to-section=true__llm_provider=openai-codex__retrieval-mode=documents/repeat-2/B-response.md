# Analyse d'une question comptable

**Date**: 2026-04-09

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
   - La question vise des états financiers consolidés établis selon les IFRS.
   - L’exposition de change concerne un dividende intragroupe déclaré, pour lequel une créance à recevoir a déjà été comptabilisée.
   - Un instrument de couverture de change existe ou est envisagé pour couvrir cette exposition.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, une documentation de couverture peut être appliquée en consolidé sur cette créance de dividende intragroupe si l’exposition est celle d’un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. En revanche, ce n’est pas un hedge de net investment ; à défaut de ces conditions, le dérivé reste non désigné et va en résultat.

## Points Opérationnels

   - Vérifier au niveau consolidé si la créance de dividende intragroupe est bien un poste monétaire et si ses écarts de change restent en résultat consolidé.
   - Ne pas traiter cette situation comme une couverture d’investissement net : l’objet couvert est ici la créance de dividende, pas les actifs nets de la filiale.
   - Si la documentation de couverture n’est pas admissible, comptabiliser le dérivé de change comme dérivé non désigné avec variations de juste valeur en résultat.
   - La désignation et la documentation doivent être établies sur l’exposition pertinente en comptes consolidés, pas seulement dans les comptes sociaux.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilité de couverture | OUI SOUS CONDITIONS | - La créance de dividende constitue un poste monétaire intragroupe.<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.<br>- La relation de couverture est documentée et désignée au niveau consolidé sur cette exposition de change. |
| 2. Couverture d’investissement net | NON | - (non spécifiées) |
| 3. Dérivé non désigné | OUI | - (non spécifiées) |

### 1. Comptabilité de couverture
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende constitue un poste monétaire intragroupe.
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.
   - La relation de couverture est documentée et désignée au niveau consolidé sur cette exposition de change.

**Raisonnment**:
En consolidé, IFRS 9 limite en principe les éléments couverts à des positions avec des tiers externes. Toutefois, une exception existe pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Dans votre situation, cela peut viser la créance de dividende intragroupe déjà comptabilisée, si elle génère bien une telle exposition résiduelle en résultat consolidé.

**Implications pratiques**: Possible en consolidé, mais seulement sur l’exposition de change résiduelle admissible ; sinon pas de hedge accounting.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le hedge de net investment vise l’exposition de change sur les actifs nets d’une activité étrangère en consolidation. Ici, le risque décrit porte sur un dividende intragroupe déjà déclaré et comptabilisé en créance à recevoir, donc sur un flux/poste intragroupe spécifique, pas sur l’investissement net dans la filiale. Cette situation ne correspond pas au modèle de couverture d’investissement net.

**Implications pratiques**: Ne pas documenter cette couverture comme un hedge de net investment.

**Référence**:
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 13
    >An exposure to foreign currency risk arising from a net investment in a foreign operation may qualify for hedge accounting only once

### 3. Dérivé non désigné
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Si les conditions ci-dessus ne sont pas remplies, le dérivé de change peut toujours être comptabilisé sans désignation de couverture. Dans ce cas, les gains et pertes sont reconnus en résultat selon IFRS 9, puis classés selon IFRS 18. C’est donc une alternative applicable dans votre situation si la documentation de couverture en consolidé n’est pas recevable.

**Implications pratiques**: Le dérivé est comptabilisé au résultat, sans effets de hedge accounting.

**Référence**:
 - 5.7.1
    >A gain or loss on a financial asset or financial liability that is measured at fair value shall be recognised in profit or loss unless
 - B72
    >a derivative that is not designated as a hedging instrument applying IFRS 9