# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Des dividendes intragroupe ont été comptabilisés à recevoir, ce qui fait naître une variation potentielle liée au change dans les comptes consolidés. Est-il alors possible de mettre en place une relation de couverture sur cette seule composante de change ?

**Documentation consultée**
   - `ifrs9`
   - `ias21`
   - `ifric17`
   - `ifrs19`
   - `ifrs2`
   - `ias24`
   - `sic25`
   - `ifric16`
   - `ifrs12`
   - `ifric1`
   - `ias37`
   - `sic7`
   - `ifric23`
   - `sic29`
   - `ias26`
   - `ifric22`

## Hypothèses
   - La créance de dividende intragroupe est libellée en devise étrangère.
   - Cette créance génère effectivement des écarts de change dans les comptes consolidés, donc l’exposition n’est pas totalement éliminée en consolidation.
   - La question porte sur les états financiers consolidés établis selon les IFRS.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en principe, la seule composante de change peut être désignée comme élément couvert si la créance intragroupe crée bien une exposition de change non totalement éliminée en consolidation. Dans ce cas, la voie la plus pertinente est une couverture de juste valeur; les autres modèles ne conviennent pas à ces faits sauf cas particulier de net investment.

## Points Opérationnels

   - Le point déterminant est factuel : il faut démontrer que la créance de dividende intragroupe produit bien une exposition de change non totalement éliminée en consolidation.
   - Si cette exposition existe, la désignation doit viser le risque de change du poste monétaire reconnu, non le dividende en tant que simple distribution intragroupe.
   - La couverture de juste valeur est le modèle le plus cohérent pour un dividende déjà comptabilisé à recevoir; la couverture de flux de trésorerie viserait plutôt un dividende encore futur et hautement probable.
   - Si le poste relève en réalité d’un investissement net dans une activité à l’étranger, le traitement doit être analysé sous l’angle spécifique de la couverture d’investissement net.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende intragroupe doit générer des gains ou pertes de change non totalement éliminés en consolidation<br>- la relation de couverture doit porter sur le risque de change de cet élément reconnu |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | OUI SOUS CONDITIONS | - la créance ou le poste monétaire concerné doit faire partie de l’investissement net dans une activité à l’étranger |
| 4. Comptabilisation du change selon IAS 21 | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende intragroupe doit générer des gains ou pertes de change non totalement éliminés en consolidation
   - la relation de couverture doit porter sur le risque de change de cet élément reconnu

**Raisonnment**:
Ici, la créance de dividende est un actif monétaire déjà comptabilisé. IFRS 9 permet qu’un élément couvert soit un actif reconnu, y compris un composant, et prévoit une exception pour le risque de change d’un élément monétaire intragroupe en consolidation s’il n’est pas totalement éliminé. Dans cette situation, couvrir la seule composante de change est donc envisageable.

**Implications pratiques**: La variation de change de l’élément couvert et celle de l’instrument de couverture seraient comptabilisées selon les règles de la couverture de juste valeur.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.1
    >A hedged item can also be a component of such an item
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite vise une créance de dividende déjà comptabilisée à recevoir, donc un poste monétaire existant. Le modèle de cash flow hedge visé dans le contexte concerne surtout des transactions prévues hautement probables, y compris certains flux intragroupe futurs en devise. Ce n’est pas le fait décrit ici.

**Implications pratiques**: Ce modèle n’est pas adapté à une créance de dividende déjà reconnue.

**Référence**:
 - 6.3.1
    >The hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance ou le poste monétaire concerné doit faire partie de l’investissement net dans une activité à l’étranger

**Raisonnment**:
Ce modèle ne s’applique pas au simple fait qu’un dividende intragroupe soit à recevoir. Il ne devient pertinent que si le poste monétaire concerné fait partie de l’investissement net dans une activité à l’étranger, auquel cas les écarts de change sont traités en OCI en consolidation. À défaut de ce lien, ce n’est pas la bonne qualification.

**Implications pratiques**: À défaut d’un lien avec un investissement net, cette voie ne doit pas être retenue pour un dividende intragroupe à recevoir.

**Référence**:
 - 32
    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation
 - 7
    >This Interpretation applies only to hedges of net investments in foreign operations
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation

### 4. Comptabilisation du change selon IAS 21
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
En l’absence d’une relation de couverture qualifiante, IAS 21 constitue le traitement de base. Les écarts de change sur les éléments monétaires sont reconnus en résultat, sauf cas particulier d’un poste faisant partie d’un investissement net. Cette base confirme qu’il existe bien une exposition à couvrir si elle subsiste en consolidation.

**Implications pratiques**: Sans couverture qualifiante, la variation de change sur la créance sera comptabilisée selon IAS 21, en principe en résultat.

**Référence**:
 - 28
    >Exchange differences ... on translating monetary items ... shall be recognised in profit or loss
 - 32
    >shall be recognised initially in other comprehensive income
 - 5.7.2
    >A gain or loss on a financial asset that is measured at amortised cost ... shall be recognised in profit or loss