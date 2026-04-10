# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Documentation consultée**
   - `ifrs10`
   - `ifrs12`
   - `ifrs19`
   - `ias24`
   - `ifrs9`
   - `ias7`
   - `ifric17`
   - `ias27`
   - `ifric16`
   - `ias32`
   - `sic25`
   - `ifric2`

## Hypothèses
   - La question vise des états financiers consolidés, et non des états financiers séparés.
   - Le dividende intragroupe est libellé dans une devise différente de la monnaie fonctionnelle d’au moins l’une des entités concernées.
   - La créance de dividende reconnue constitue un poste monétaire intragroupe générant un risque de change dont les écarts ne sont pas intégralement éliminés en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture peut être mise en place sur la composante change d’une créance de dividende intragroupe reconnue si cette créance est un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation. Dans ce cas, le modèle pertinent est la fair value hedge, pas la cash flow hedge.

## Points Opérationnels

   - Le point clé est le niveau de reporting : l’analyse doit être faite en consolidation, où la créance intragroupe est éliminée mais où certains écarts de change peuvent subsister.
   - Le moment est déterminant : avant reconnaissance du dividende, la logique peut relever d’une transaction future; après reconnaissance de la créance, la question se traite comme un poste monétaire reconnu.
   - La documentation doit viser strictement la composante change résiduelle en consolidation, et non le dividende intragroupe en tant que tel.
   - Il faut vérifier concrètement que les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation, notamment en présence de monnaies fonctionnelles différentes.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende reconnue est un poste monétaire intragroupe.<br>- Les écarts de change correspondants ne sont pas intégralement éliminés en consolidation.<br>- La désignation porte sur la composante change de la créance reconnue, après sa comptabilisation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende reconnue est un poste monétaire intragroupe.
   - Les écarts de change correspondants ne sont pas intégralement éliminés en consolidation.
   - La désignation porte sur la composante change de la créance reconnue, après sa comptabilisation.

**Raisonnment**:
En consolidation, les éléments intragroupe sont en principe exclus comme éléments couverts, car seuls les éléments avec une partie externe peuvent être désignés. Toutefois, IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés en consolidation. Si la créance de dividende reconnue entre dans ce cas, une documentation de couverture est possible sur cette composante change.

**Implications pratiques**: La couverture peut être documentée au niveau consolidé sur la créance reconnue, mais seulement pour le risque de change qui subsiste en consolidation.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - B86
    >eliminate in full intragroup assets and liabilities

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans la situation décrite, une créance de dividende a déjà été reconnue. Le modèle de cash flow hedge vise plutôt une transaction future hautement probable; IFRS 9 admet, par exception, certaines transactions intragroupe futures en devise en consolidation. Une fois la créance comptabilisée, on n’est plus dans le cas d’une transaction future à documenter en cash flow hedge.

**Implications pratiques**: Le modèle de cash flow hedge n’est pas le bon véhicule si le dividende intragroupe a déjà donné lieu à la reconnaissance d’une créance.

**Référence**:
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item
 - 12
    >Dividends from a subsidiary... are recognised ... when the entity’s right to receive the dividend is established