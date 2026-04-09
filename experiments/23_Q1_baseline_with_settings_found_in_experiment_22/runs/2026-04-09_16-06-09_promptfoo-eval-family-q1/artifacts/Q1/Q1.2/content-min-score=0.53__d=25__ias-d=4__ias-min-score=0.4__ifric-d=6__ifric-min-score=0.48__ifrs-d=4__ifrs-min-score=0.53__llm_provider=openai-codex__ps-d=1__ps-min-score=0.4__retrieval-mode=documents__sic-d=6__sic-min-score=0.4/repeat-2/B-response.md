# Analyse d'une question comptable

**Date**: 2026-04-09

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
   - Le dividende intragroupe a donné lieu à une créance et à une dette monétaires entre deux entités du groupe ayant des monnaies fonctionnelles différentes.
   - La question vise les comptes consolidés IFRS et la seule composante de risque de change de cette créance de dividende.
   - Cette créance de dividende n'est pas présentée comme faisant partie d'un investissement net dans une activité à l'étranger.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture peut être appliquée sur le risque de change seulement si l'exposition intragroupe affecte le résultat consolidé. Dans les approches proposées, la couverture de juste valeur est la plus pertinente; la couverture de flux de trésorerie et la couverture d'investissement net ne conviennent pas à une créance de dividende déjà comptabilisée, sauf changement de faits non indiqué ici.

## Points Opérationnels

   - En consolidation, vérifier d'abord si la créance de dividende constitue bien un poste monétaire intragroupe dont l'effet de change subsiste en résultat consolidé.
   - La documentation de couverture doit être formalisée dès l'origine de la relation de couverture, avec identification de l'instrument, de l'élément couvert et du risque de change couvert.
   - Si les écarts de change sont totalement éliminés en consolidation, il n'y a pas d'exposition éligible à couvrir dans les comptes consolidés.
   - Une couverture sur un instrument intragroupe n'est pas le point de départ normal en consolidation; l'analyse doit viser l'exposition consolidée résiduelle.
   - La qualification en investissement net ne doit pas être utilisée pour un simple dividende déclaré et comptabilisé en créance, sauf faits différents non indiqués ici.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance intragroupe est un poste monétaire en devise<br>- les écarts de change sur cette créance affectent le résultat consolidé et ne sont pas totalement éliminés en consolidation<br>- la relation de couverture respecte la désignation et la documentation prévues par IFRS 9 |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance intragroupe est un poste monétaire en devise
   - les écarts de change sur cette créance affectent le résultat consolidé et ne sont pas totalement éliminés en consolidation
   - la relation de couverture respecte la désignation et la documentation prévues par IFRS 9

**Raisonnment**:
Ici, il existe une créance intragroupe déjà comptabilisée, donc un élément reconnu exposé au change. IFRS 9 admet la couverture d'un actif ou passif reconnu affectant le résultat, et précise qu'en consolidation un poste monétaire intragroupe peut être un élément couvert pour le risque de change si les écarts de change ne sont pas totalement éliminés. Cette logique correspond à une créance de dividende en devise.

**Implications pratiques**: Documenter la créance de dividende comme élément couvert du risque de change et un instrument de couverture externe au groupe.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.4.1
    >at the inception of the hedging relationship there is formal designation and documentation

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans les faits décrits, le dividende a déjà été comptabilisé en créance: l'exposition porte donc sur un poste monétaire reconnu, pas sur une transaction future hautement probable. Le modèle de cash flow hedge vise la variabilité de flux de trésorerie d'un élément reconnu ou d'une transaction future; ce n'est pas la qualification la plus adaptée à une créance fixe de dividende déjà constatée.

**Implications pratiques**: Cette approche ne doit pas être retenue pour la créance de dividende déjà enregistrée.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated

### 3. Couverture d'un investissement net dans une activité à l'étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite concerne une créance de dividende intragroupe, non un investissement net dans une activité à l'étranger. IFRIC 16 encadre cette couverture pour l'exposition de change sur les actifs nets d'une activité étrangère; une créance de dividende déclarée est d'une nature différente et n'entre pas, sur ces faits, dans ce modèle.

**Implications pratiques**: Ne pas documenter cette créance de dividende comme couverture d'investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation