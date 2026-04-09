# Analyse d'une question comptable

**Date**: 2026-04-09

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
   - La question vise les comptes consolidés IFRS et la partie change d’un dividende intragroupe déjà comptabilisé en créance.
   - La créance de dividende est supposée être un élément monétaire libellé dans une devise différente de la monnaie fonctionnelle d’au moins une des entités concernées.
   - L’objectif est d’identifier quel modèle de comptabilité de couverture IFRS peut s’appliquer à cette exposition de change dans cette situation précise.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie IFRS pertinente est la couverture de juste valeur, à condition que la créance intragroupe soit un élément monétaire dont le risque de change affecte le résultat consolidé et n’est pas entièrement éliminé en consolidation. Les modèles de couverture de flux de trésorerie et de couverture d’investissement net ne sont pas adaptés ici au fait générateur décrit.

## Points Opérationnels

   - Le point clé en consolidation est de démontrer que le risque de change sur la créance intragroupe affecte bien le résultat consolidé malgré l’élimination intragroupe.
   - Si le dividende était encore seulement prévu et non comptabilisé, la logique de couverture de flux de trésorerie pourrait être examinée, mais ce n’est pas le cas ici.
   - La documentation doit être alignée sur le fait générateur réel : exposition de change sur une créance reconnue, et non sur l’investissement net ni sur un flux futur.
   - La qualification comme élément monétaire intragroupe est déterminante pour retenir ou non la couverture de juste valeur en comptes consolidés.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Le dividende est libellé dans une devise créant un risque de change.<br>- Les écarts de change sur cette créance affectent le résultat consolidé et ne sont pas entièrement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Le dividende est libellé dans une devise créant un risque de change.
   - Les écarts de change sur cette créance affectent le résultat consolidé et ne sont pas entièrement éliminés en consolidation.

**Raisonnment**:
La créance de dividende déjà comptabilisée est un actif reconnu, donc elle entre dans les types d’éléments pouvant être désignés comme éléments couverts. En consolidation, un élément intragroupe n’est en principe pas éligible, sauf pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés et affectent le résultat consolidé. C’est le cas IFRS qui peut permettre une documentation de couverture ici.

**Implications pratiques**: La documentation de couverture peut viser le risque de change de la créance reconnue, si l’exposition subsiste au niveau consolidé.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ce modèle vise une transaction future prévue ou hautement probable. Or, dans les faits donnés, le dividende intragroupe n’est plus une transaction future : il a déjà été comptabilisé en créance. La question porte donc sur une exposition de change attachée à un actif reconnu, pas sur un flux futur à venir.

**Implications pratiques**: Ce modèle n’est pas adapté une fois le dividende déjà déclaré et enregistré en créance.

**Référence**:
 - 6.3.1
    >A hedged item can be a ... forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ce modèle concerne la couverture d’un investissement net dans une activité à l’étranger. Dans la situation décrite, l’élément visé est une créance de dividende intragroupe déjà comptabilisée, et non l’investissement net lui-même. Sur les faits fournis, la documentation de couverture ne peut donc pas être rattachée à ce modèle.

**Implications pratiques**: La créance de dividende ne doit pas être traitée comme une couverture d’investissement net dans cette situation.

**Référence**:
 - 6.3.1
    >A hedged item can be a ... net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation