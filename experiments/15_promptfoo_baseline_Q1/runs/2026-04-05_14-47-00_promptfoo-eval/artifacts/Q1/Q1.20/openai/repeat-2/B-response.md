# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Une créance relative à des dividendes intragroupe figure désormais dans les états financiers consolidés, avec une sensibilité corrélative aux fluctuations de change. Peut-on couvrir cette exposition dans le cadre d’une documentation de hedge accounting ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise le risque de change porté par une créance de dividendes intragroupe dans des états financiers consolidés.
   - La créance est déjà comptabilisée à la date de la documentation de couverture et l'exposition recherchée est l'effet de change en résultat consolidé.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en pratique via une relation de fair value hedge sur le risque de change, mais seulement si cette créance intragroupe génère des écarts de change qui ne sont pas totalement éliminés en consolidation. Le net investment hedge n'est pas adapté à cette créance, et le cash flow hedge ne correspond pas aux faits décrits.

## Points Opérationnels

   - Vérifier et conserver la démonstration que l'écart de change sur la créance n'est pas totalement éliminé lors de la consolidation.
   - La documentation initiale doit identifier l'instrument de couverture, la créance de dividendes couverte, le risque de change couvert et la manière d'apprécier l'efficacité.
   - Si l'exposition de change ne passe pas en résultat consolidé, l'éligibilité comme hedged item en consolidation tombe.
   - Le traitement doit rester centré sur le risque de change de la créance intragroupe, et non être présenté comme une couverture de l'investissement net dans la filiale.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit produire des gains ou pertes de change non totalement éliminés en consolidation.<br>- Le risque couvert doit être limité au risque de change de cette créance reconnue. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit produire des gains ou pertes de change non totalement éliminés en consolidation.
   - Le risque couvert doit être limité au risque de change de cette créance reconnue.

**Raisonnment**:
La créance de dividendes est ici un actif reconnu ; le modèle de fair value hedge vise précisément une exposition aux variations de valeur d'un actif reconnu attribuables à un risque particulier affectant le résultat. En consolidation, un élément intragroupe n'est éligible que si son risque de change donne lieu à des gains ou pertes non totalement éliminés ; c'est la condition décisive dans cette situation.

**Implications pratiques**: Documenter la créance de dividendes comme hedged item reconnu et le risque couvert comme le seul risque de change affectant le résultat consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.1
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les faits décrits portent sur une créance déjà reconnue en consolidation, avec une sensibilité de change constatée désormais. Le contexte IFRS 9 fourni rattache surtout le cash flow hedge aux flux variables d'éléments reconnus ou aux transactions intragroupe hautement probables ; ici, l'exposition décrite n'est pas celle d'une transaction future mais d'une créance existante.

**Implications pratiques**: Ne pas privilégier ce modèle pour documenter la couverture d'une créance de dividendes déjà comptabilisée.

**Référence**:
 - 6.5.1
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividendes intragroupe, non un montant de net assets d'une activité étrangère. Le net investment hedge est réservé au risque de change sur un investissement net dans une opération étrangère ; il ne sert pas à couvrir une créance intragroupe isolée, même si celle-ci apparaît en consolidation.

**Implications pratiques**: Ne pas qualifier cette créance de dividendes comme élément couvert au titre d'un net investment hedge.

**Référence**:
 - 6.5.1
    >hedge of a net investment in a foreign operation
 - ifric-16 2
    >The item being hedged ... may be an amount of net assets