# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ifrs19`
   - `ias32`
   - `ifric17`
   - `ifrs17`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ifrs12`
   - `ifrs9`
   - `ifric19`
   - `ias37`
   - `ifric16`

## Hypothèses
   - La question vise les comptes consolidés IFRS du groupe.
   - Le dividende intragroupe a déjà été déclaré et comptabilisé en créance, donc il s'agit d'un poste monétaire intragroupe reconnu.
   - La créance de dividende est libellée dans une devise différente de la monnaie fonctionnelle d'au moins une des entités concernées, de sorte qu'un risque de change existe.
   - Aucune autre relation de couverture n'est visée que la couverture de la composante change de cette créance de dividende intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie pertinente est la couverture de juste valeur, mais seulement si la créance intragroupe crée un écart de change qui n'est pas entièrement éliminé en consolidation. La couverture de flux de trésorerie ne convient pas car le dividende est déjà comptabilisé en créance, et la couverture d'investissement net ne couvre pas, en tant que telle, cette créance de dividende.

## Points Opérationnels

   - Le point clé en consolidation est de démontrer que l'écart de change sur la créance intragroupe n'est pas totalement éliminé.
   - Si le dividende était encore au stade de flux futur non reconnu, la logique cash flow hedge pourrait être examinée ; après comptabilisation en créance, ce n'est plus le cas ici.
   - La documentation doit être alignée sur l'objet réellement couvert : ici la créance de dividende reconnue, et non l'investissement net dans la filiale.
   - En pratique, l'effort principal porte sur l'analyse de la nature monétaire de la créance et du traitement de ses écarts de change en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire reconnu.<br>- Le risque de change sur cette créance produit des gains ou pertes de change non intégralement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire reconnu.
   - Le risque de change sur cette créance produit des gains ou pertes de change non intégralement éliminés en consolidation.

**Raisonnment**:
Ici, le dividende est déjà comptabilisé en créance : il s'agit donc d'un actif reconnu, ce qui correspond au type d'élément couvert admis par IFRS 9. En consolidation, un poste monétaire intragroupe peut être désigné uniquement si son risque de change génère des écarts qui ne sont pas totalement éliminés ; c'est cette condition qui est décisive dans votre cas.

**Implications pratiques**: Possible si la documentation vise la composante change de la créance reconnue et si l'effet de change subsiste en consolidation.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise une transaction future prévue et hautement probable. Or, dans votre situation, le dividende intragroupe n'est plus une transaction future : il a déjà été comptabilisé en créance. Le fait générateur n'est donc plus au stade d'un flux futur à documenter comme élément couvert.

**Implications pratiques**: À ce stade, cette documentation n'est pas adaptée à la créance de dividende déjà reconnue.

**Référence**:
 - 6.3.1
    >A hedged item can be ... a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d'investissement net porte sur le risque de change de l'investissement net dans une activité à l'étranger, pas sur une créance de dividende intragroupe déjà comptabilisée. Dans les faits décrits, l'exposition visée est celle du dividende en créance ; ce n'est donc pas cette relation de couverture qui correspond directement à l'objet à couvrir.

**Implications pratiques**: Cette piste ne répond pas directement à la couverture change de la créance de dividende elle-même.

**Référence**:
 - 6.3.1
    >The hedged item can be ... a net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation