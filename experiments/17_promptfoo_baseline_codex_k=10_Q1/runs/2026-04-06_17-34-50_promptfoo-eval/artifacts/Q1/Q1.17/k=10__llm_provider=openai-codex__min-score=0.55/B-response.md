# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Des dividendes intragroupe ont été comptabilisés à recevoir, ce qui fait naître une variation potentielle liée au change dans les comptes consolidés. Est-il alors possible de mettre en place une relation de couverture sur cette seule composante de change ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question vise les comptes consolidés et un dividende intragroupe déjà comptabilisé en créance/dette, libellé dans une devise différente au moins pour l’une des entités du groupe.
   - La relation envisagée porte uniquement sur le risque de change de cet élément intragroupe, et non sur une couverture d’investissement net dans une activité à l’étranger.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si le dividende intragroupe comptabilisé à recevoir/payé constitue un poste monétaire intragroupe dont le risque de change n’est pas entièrement éliminé en consolidation et affecte le résultat consolidé. Dans ce cas, seule la composante de change peut être désignée; sinon, non.

## Points Opérationnels

   - Le point décisif est l’effet en résultat consolidé: si le change sur le dividende intragroupe est totalement éliminé en consolidation, la désignation échoue.
   - La documentation de couverture doit identifier explicitement la seule composante de change comme risque couvert.
   - L’analyse doit être faite au niveau consolidé, pas seulement dans les comptes individuels des entités du groupe.
   - Si la relation est retenue, il faut démontrer que la composante de change est séparément identifiable et fiable à mesurer.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - Le dividende à recevoir/à payer doit être un poste monétaire intragroupe<br>- Le risque de change doit ne pas être entièrement éliminé en consolidation<br>- Le risque de change doit affecter le résultat consolidé |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - Le dividende à recevoir/à payer doit être un poste monétaire intragroupe reconnu<br>- Le risque de change doit ne pas être entièrement éliminé en consolidation<br>- Le risque de change doit affecter le résultat consolidé |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende à recevoir/à payer doit être un poste monétaire intragroupe
   - Le risque de change doit ne pas être entièrement éliminé en consolidation
   - Le risque de change doit affecter le résultat consolidé

**Raisonnment**:
Dans cette situation, l’élément est déjà comptabilisé et le risque visé est le change sur un poste intragroupe. IFRS 9 admet en consolidation certains risques de change sur éléments intragroupe, mais seulement s’ils affectent le résultat consolidé; sinon l’intragroupe ne peut pas être désigné. La composante de change peut être désignée si elle est séparément identifiable et mesurable.

**Implications pratiques**: Sans impact en résultat consolidé, une couverture de flux de trésorerie ne tient pas en consolidation.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.3.7
    >only changes in the cash flows or fair value ... attributable to a specific risk or risks
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende à recevoir/à payer doit être un poste monétaire intragroupe reconnu
   - Le risque de change doit ne pas être entièrement éliminé en consolidation
   - Le risque de change doit affecter le résultat consolidé

**Raisonnment**:
Le dividende intragroupe comptabilisé à recevoir/payé est un actif ou passif reconnu; une couverture de juste valeur vise précisément un actif/passif reconnu exposé à un risque particulier. En consolidation, cela n’est recevable ici que si l’exception pour poste monétaire intragroupe s’applique et si la variation de change affecte le résultat consolidé. La seule composante de change peut être désignée.

**Implications pratiques**: Si ces conditions sont remplies, la désignation de la seule composante change est conceptuellement compatible avec une couverture de juste valeur.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.3.7
    >only changes in the cash flows or fair value of an item attributable to a specific risk or risks
 - 6.4.1
    >there is formal designation and documentation of the hedging relationship

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait décrit est un dividende intragroupe comptabilisé à recevoir, donc un poste de créance/dette intragroupe, et non une exposition de change sur un investissement net dans une activité étrangère. Le modèle IFRS 9 / IFRIC 16 vise les net assets d’une activité étrangère, pas un dividende intragroupe isolé.

**Implications pratiques**: Cette voie n’est pas la bonne qualification pour couvrir le change sur un dividende intragroupe à recevoir.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16.7
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16.10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets