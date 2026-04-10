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
   - Le dividende intragroupe a été déclaré et un receivable/payable intragroupe a déjà été comptabilisé.
   - La créance de dividende est libellée dans une devise autre que la devise fonctionnelle d'au moins une des entités concernées.
   - La question porte sur les comptes consolidés et sur l'éligibilité de la variation de change comme élément couvert, non sur la désignation effective de l'instrument de couverture.

## Recommandation

**OUI SOUS CONDITIONS**

Dans les comptes consolidés, l'éligibilité existe en principe via un fair value hedge si la créance de dividende intragroupe est un élément monétaire exposé à un risque de change non totalement éliminé en consolidation. Le cash flow hedge n'est pas adapté une fois la créance reconnue, et le net investment hedge n'est pas le modèle pertinent sauf cas très particulier où l'élément ferait partie de l'investissement net.

## Points Opérationnels

   - Le point déterminant est le niveau consolidé : les positions intragroupe sont en principe exclues, sauf exception limitée au risque de change d'un élément monétaire intragroupe.
   - Le timing compte : dès lors que le dividende a donné lieu à une créance reconnue, l'analyse bascule vers un élément monétaire existant et non vers une transaction future hautement probable.
   - Il faut documenter que l'écart de change sur la créance/payable intragroupe n'est pas totalement éliminé en consolidation, ce qui suppose généralement des devises fonctionnelles différentes.
   - Si les faits montraient au contraire un élément faisant partie de l'investissement net dans une activité étrangère, l'analyse pourrait relever d'un autre cadre; ce n'est pas le cas décrit ici.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende constitue un élément monétaire intragroupe<br>- le risque de change génère des écarts non totalement éliminés en consolidation<br>- les entités concernées ont des devises fonctionnelles différentes |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende constitue un élément monétaire intragroupe
   - le risque de change génère des écarts non totalement éliminés en consolidation
   - les entités concernées ont des devises fonctionnelles différentes

**Raisonnment**:
Dans cette situation, la créance de dividende déjà reconnue est un actif comptabilisé, donc elle entre conceptuellement dans le champ des éléments pouvant être couverts. En comptes consolidés, IFRS 9 exclut en principe les positions intragroupe, mais admet une exception pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. IAS 21 confirme qu'un tel écart de change subsiste en résultat consolidé pour un élément monétaire entre entités de devises fonctionnelles différentes.

**Implications pratiques**: La désignation est envisageable sur le seul risque de change de la créance de dividende reconnue en consolidation.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 45
    >cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le modèle de cash flow hedge vise notamment une transaction prévue hautement probable. Or, dans les faits posés, un receivable a déjà été constaté : l'exposition n'est plus celle d'un flux futur non reconnu, mais celle d'un élément monétaire existant dont la variation de change est déjà constatée. La question telle que formulée renvoie donc à une exposition sur créance reconnue, pas à une transaction future.

**Implications pratiques**: Ce modèle n'est pas le bon véhicule de désignation pour la variation de change d'un dividende déjà comptabilisé en créance.

**Référence**:
 - 6.3.1
    >The hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d'investissement net vise les expositions de change rattachées à un investissement net dans une activité étrangère. Ici, il s'agit d'un dividende intragroupe pour lequel une créance a été reconnue, donc d'un poste de règlement intragroupe et non, d'après les faits fournis, d'un élément formant partie de l'investissement net. Le cas décrit ne correspond donc pas au modèle de net investment hedge.

**Implications pratiques**: La variation de change sur la créance de dividende ne se traite pas, dans ce cas, comme une couverture d'investissement net.

**Référence**:
 - 32
    >a monetary item that forms part of a reporting entity’s net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation