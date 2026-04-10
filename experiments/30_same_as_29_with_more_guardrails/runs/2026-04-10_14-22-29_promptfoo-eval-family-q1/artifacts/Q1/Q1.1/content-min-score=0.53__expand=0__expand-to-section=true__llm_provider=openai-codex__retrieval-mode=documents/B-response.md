# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Documentation consultée**
   - `ias32`
   - `ifrs19`
   - `ifrs18`
   - `ifric17`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ifrs9`
   - `ifrs12`
   - `ias37`
   - `ifric19`
   - `ifric16`

## Hypothèses
   - Le dividende intragroupe a été formellement décidé et comptabilisé en créance dans les comptes individuels avant consolidation.
   - La question vise les comptes consolidés IFRS et uniquement la composante de change liée à cette créance intragroupe.
   - La créance et la dette de dividende correspondante sont libellées dans une devise créant un risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie IFRS la plus défendable est la couverture de juste valeur sur le risque de change de la créance reconnue, mais seulement si l'exposition de change sur l'élément monétaire intragroupe n'est pas totalement éliminée en consolidation. La couverture de flux de trésorerie n'est pas adaptée à une créance déjà comptabilisée, et la couverture d'investissement net vise un autre objet de couverture.

## Points Opérationnels

   - En consolidation, la règle de base exclut les transactions intragroupe comme éléments couverts ; il faut donc démontrer que l'on se situe dans l'exception du poste monétaire intragroupe exposé au change.
   - Le point décisif est le timing : une fois le dividende comptabilisé en créance, l'analyse bascule d'une transaction future vers un actif reconnu.
   - La documentation de couverture doit être préparée au niveau consolidé et cibler explicitement le risque de change de la créance, pas le dividende intragroupe en général.
   - Si la créance est soldée rapidement ou si les effets de change sont totalement éliminés en consolidation, l'intérêt et la recevabilité de la couverture deviennent très limités.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire exposé au risque de change.<br>- Les gains ou pertes de change correspondants ne doivent pas être totalement éliminés en consolidation.<br>- La relation de couverture doit être documentée en comptes consolidés sur ce risque de change spécifique. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire exposé au risque de change.
   - Les gains ou pertes de change correspondants ne doivent pas être totalement éliminés en consolidation.
   - La relation de couverture doit être documentée en comptes consolidés sur ce risque de change spécifique.

**Raisonnment**:
Ici, la créance de dividende est déjà reconnue ; on n'est donc pas sur un flux futur mais sur un poste existant. En consolidation, un poste intragroupe ne peut être couvert que s'il s'agit d'un élément monétaire exposé au change dont les écarts ne sont pas totalement éliminés, ce que vise l'exception IFRS 9 pour le risque de change des postes monétaires intragroupe.

**Implications pratiques**: C'est l'approche pertinente si vous voulez couvrir en consolidation la variation de change d'une créance de dividende déjà comptabilisée.

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
Le fait décrit n'est pas une transaction future hautement probable : le dividende est déjà comptabilisé en créance. Or le modèle cash flow hedge vise des transactions futures, y compris certaines transactions intragroupe futures en devise, pas une créance déjà reconnue au bilan.

**Implications pratiques**: Cette documentation ne convient pas à la partie change d'un dividende déjà enregistré en créance.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche couvre le risque de change d'un investissement net dans une activité à l'étranger, non la variation de change d'une créance de dividende intragroupe prise isolément. Dans les faits décrits, l'objet comptabilisé est la créance de dividende ; ce n'est pas, en tant que tel, l'investissement net dans la filiale étrangère.

**Implications pratiques**: À écarter pour couvrir la créance de dividende elle-même ; cette relation de couverture vise un autre niveau de risque.

**Référence**:
 - 6.3.1
    >A hedged item can be ... a net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation