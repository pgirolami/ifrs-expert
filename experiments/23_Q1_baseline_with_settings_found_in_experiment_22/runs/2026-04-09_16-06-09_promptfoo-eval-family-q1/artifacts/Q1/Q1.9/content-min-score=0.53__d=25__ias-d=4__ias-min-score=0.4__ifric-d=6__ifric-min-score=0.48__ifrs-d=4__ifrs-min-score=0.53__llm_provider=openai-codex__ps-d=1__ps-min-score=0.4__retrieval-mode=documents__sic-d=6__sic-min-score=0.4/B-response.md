# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>La composante de risque de change liée à des dividendes intragroupe reconnus sous forme de créance peut-elle être désignée comme élément couvert dans les comptes consolidés ?

**Documentation consultée**
   - `ifrs9`
   - `ifrs19`
   - `ifric2`
   - `ifric16`
   - `ias32`
   - `ifric17`
   - `sic7`
   - `ias37`

## Hypothèses
   - Le dividende intragroupe a été comptabilisé en créance et génère une exposition de change dans les états financiers consolidés.
   - La question porte sur la possibilité de désigner cette exposition comme élément couvert au titre de la comptabilité de couverture selon IFRS 9 dans les comptes consolidés.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en principe via une couverture de juste valeur, si la créance de dividende intragroupe est un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation. En revanche, ce n’est pas une couverture d’investissement net, et l’approche de couverture de flux de trésorerie n’est pas celle qui correspond le mieux à ce fait générateur.

## Points Opérationnels

   - Vérifier au moment de la désignation que la créance de dividende est bien un poste monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.
   - Documenter formellement dès l’origine l’instrument de couverture, l’élément couvert, le risque de change couvert et l’évaluation de l’efficacité.
   - Ne pas utiliser le modèle de couverture d’investissement net pour une créance de dividende reconnue ; ce modèle vise les actifs nets d’une opération étrangère.
   - L’analyse dépend du fait que l’exposition de change subsiste réellement dans les comptes consolidés, malgré l’élimination intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende constitue un poste monétaire intragroupe.<br>- Les gains ou pertes de change correspondants ne sont pas totalement éliminés en consolidation.<br>- La relation de couverture satisfait aux critères de désignation, documentation et efficacité d’IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende constitue un poste monétaire intragroupe.
   - Les gains ou pertes de change correspondants ne sont pas totalement éliminés en consolidation.
   - La relation de couverture satisfait aux critères de désignation, documentation et efficacité d’IFRS 9.

**Raisonnment**:
Dans cette situation, la créance de dividende déjà reconnue est un actif comptabilisé. IFRS 9 permet en principe de couvrir un actif reconnu pour un risque particulier, mais en consolidation seuls les éléments avec des tiers externes sont éligibles, sauf exception pour le risque de change d’un poste monétaire intragroupe non totalement éliminé. Sous l’hypothèse donnée, cette exception peut s’appliquer.

**Implications pratiques**: La désignation est envisageable en comptes consolidés comme couverture de juste valeur du risque de change de la créance reconnue.

**Référence**:
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.4.1
    >there is formal designation and documentation of the hedging relationship

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, le dividende intragroupe est déjà reconnu sous forme de créance. Le sujet porte donc sur le risque de change d’un actif comptabilisé existant, non sur une transaction future hautement probable ni sur une variabilité de flux de trésorerie du type visé par IFRS 9 pour ce modèle. Le fait générateur décrit correspond davantage à une exposition de juste valeur qu’à une couverture de flux.

**Implications pratiques**: Cette approche ne devrait pas être retenue pour une créance de dividende intragroupe déjà comptabilisée.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividende intragroupe reconnue, et non l’exposition de change sur un investissement net dans une activité à l’étranger. IFRS 9 et IFRIC 16 réservent ce modèle au risque de change lié aux actifs nets d’une opération étrangère inclus dans les comptes consolidés. Une créance de dividende ne constitue pas cet élément couvert.

**Implications pratiques**: La créance de dividende ne doit pas être désignée comme élément couvert au titre d’une couverture d’investissement net.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - 7
    >This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation