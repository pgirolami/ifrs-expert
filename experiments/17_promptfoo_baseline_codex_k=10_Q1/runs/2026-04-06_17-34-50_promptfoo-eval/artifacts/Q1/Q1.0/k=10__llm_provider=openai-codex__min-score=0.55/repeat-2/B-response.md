# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question vise les comptes consolidés et une créance de dividende intragroupe déjà comptabilisée entre entités du groupe.
   - La couverture recherchée porte uniquement sur le risque de change attaché à cette créance/dividende intragroupe.
   - On suppose que la créance de dividende est un poste monétaire intragroupe pouvant générer des écarts de change qui ne sont pas totalement éliminés en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via une couverture de juste valeur si la créance intragroupe crée bien une exposition de change non totalement éliminée en consolidation. La couverture de flux de trésorerie et la couverture d’investissement net ne correspondent pas, en principe, à cette situation.

## Points Opérationnels

   - Le point décisif en consolidation est de démontrer que la créance de dividende intragroupe génère bien un écart de change non totalement éliminé.
   - Si cette condition n’est pas satisfaite, la réponse pratique devient non en comptes consolidés malgré l’existence d’une créance dans les comptes individuels.
   - La documentation doit être mise en place dès l’origine de la relation de couverture et identifier clairement l’instrument de couverture, l’élément couvert et le risque de change couvert.
   - La couverture d’investissement net n’est pas adaptée à un dividende intragroupe déclaré ; il faut éviter une documentation sur une base conceptuelle erronée.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende constitue un poste monétaire intragroupe<br>- Le risque de change sur cette créance affecte le résultat consolidé car il n’est pas totalement éliminé en consolidation<br>- La relation de couverture respecte la désignation et la documentation exigées par IFRS 9 |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende constitue un poste monétaire intragroupe
   - Le risque de change sur cette créance affecte le résultat consolidé car il n’est pas totalement éliminé en consolidation
   - La relation de couverture respecte la désignation et la documentation exigées par IFRS 9

**Raisonnment**:
Ici, la créance de dividende est déjà comptabilisée : on est donc face à un actif reconnu, ce qui cadre avec le modèle de juste valeur. En consolidation, un élément intragroupe n’est normalement pas éligible, sauf exception pour le risque de change d’un poste monétaire intragroupe lorsqu’il crée des écarts non totalement éliminés ; dans ce cas, la documentation de couverture peut être envisagée.

**Implications pratiques**: La documentation doit viser spécifiquement le risque de change de la créance reconnue dans les comptes consolidés.

**Référence**:
 - 6.5.1
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite porte sur un dividende intragroupe déjà constaté en créance à recevoir, donc sur un actif reconnu et non sur une variabilité de flux de trésorerie d’une transaction future hautement probable. En outre, pour les opérations intragroupe en consolidation, IFRS 9 ne retient qu’une exception ciblée, formulée pour certains postes monétaires intragroupe et certaines transactions futures de change, ce qui ne correspond pas naturellement à cette créance de dividende reconnue.

**Implications pratiques**: Ce modèle n’est pas le bon véhicule de documentation pour une créance de dividende déjà enregistrée.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - B6.3.5
    >This is usually the case for royalty payments, interest payments or management charges between members of the same group

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait générateur décrit n’est pas le risque de change sur un investissement net dans une activité étrangère, mais le risque de change sur un dividende intragroupe à recevoir. IFRIC 16 traite la couverture de la position nette d’investissement dans une entité étrangère ; cela est différent d’une créance de dividende intragroupe isolée.

**Implications pratiques**: Il ne faut pas documenter ce risque de dividende comme une couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16 2
    >the item being hedged ... may be an amount of net assets