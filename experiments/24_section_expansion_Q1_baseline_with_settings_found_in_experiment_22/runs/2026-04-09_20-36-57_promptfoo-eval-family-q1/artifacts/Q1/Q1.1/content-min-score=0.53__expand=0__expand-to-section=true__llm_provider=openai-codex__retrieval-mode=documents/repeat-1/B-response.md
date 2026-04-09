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
   - La créance de dividende intragroupe crée une exposition de change entre des entités du groupe ayant des monnaies fonctionnelles différentes.
   - La question porte sur les possibilités de comptabilité de couverture dans les comptes consolidés pour la seule composante de change.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie pertinente est la couverture de juste valeur sur le risque de change de la créance intragroupe reconnue, si l’élément monétaire intragroupe génère un écart de change non totalement éliminé en consolidation. La couverture de flux de trésorerie et la couverture d’investissement net ne correspondent pas aux faits décrits.

## Points Opérationnels

   - Le point clé est la nature du poste : une créance de dividende déjà reconnue oriente vers une couverture d’un élément reconnu, pas d’un flux futur.
   - En consolidation, l’exception IFRS 9 pour les éléments monétaires intragroupe en devise n’est utilisable que si les écarts de change ne sont pas totalement éliminés.
   - Si aucune relation de couverture éligible n’est formalisée, la dérivée éventuelle reste hors hedge accounting et ses variations suivent le régime général IFRS 9.
   - La documentation doit être mise en place au niveau consolidé avec une désignation explicite du risque de change couvert.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un élément monétaire intragroupe exposé au change.<br>- Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation.<br>- Une désignation et une documentation de couverture conformes à IFRS 9 doivent être mises en place. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Sans comptabilité de couverture | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un élément monétaire intragroupe exposé au change.
   - Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation.
   - Une désignation et une documentation de couverture conformes à IFRS 9 doivent être mises en place.

**Raisonnment**:
Ici, le dividende intragroupe a déjà été comptabilisé en créance : il s’agit donc d’un élément reconnu, et non d’un flux futur. En comptes consolidés, IFRS 9 admet la couverture du risque de change d’un élément monétaire intragroupe si ce risque donne lieu à des écarts de change qui ne sont pas totalement éliminés à la consolidation.

**Implications pratiques**: Cette approche permet de documenter en consolidation la couverture de la partie change de la créance déjà reconnue.

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
Cette modalité vise une transaction future prévue et hautement probable. Or, dans les faits décrits, le dividende intragroupe a déjà été comptabilisé en créance ; l’exposition de change porte donc sur un poste reconnu et non sur un flux futur à venir.

**Implications pratiques**: Cette documentation n’est pas adaptée à la créance de dividende déjà comptabilisée.

**Référence**:
 - 6.3.1
    >A hedged item can be a ... forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les extraits fournis traitent cette couverture comme un modèle distinct visant un investissement net dans une activité à l’étranger. Les faits décrits concernent une créance de dividende intragroupe comptabilisée, pas la couverture d’un investissement net ; rien n’indique ici une telle désignation.

**Implications pratiques**: Cette approche ne correspond pas à la partie change de la créance de dividende telle que décrite.

**Référence**:
 - 6.3.1
    >a net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation

### 4. Sans comptabilité de couverture
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut de désignation éligible en couverture, l’instrument de change reste comptabilisé selon les règles générales d’IFRS 9, avec les gains et pertes reconnus selon son classement. Cette solution est toujours disponible, mais elle ne donne pas l’effet de présentation d’une relation de couverture documentée.

**Implications pratiques**: L’exposition de change est suivie sans relation de couverture comptable en consolidation.

**Référence**:
 - 5.7.1
    >A gain or loss on a financial asset or financial liability that is measured at fair value shall be recognised in profit or loss unless:
 - B72
    >a derivative that is not designated as a hedging instrument