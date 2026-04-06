# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Une créance relative à des dividendes intragroupe figure désormais dans les états financiers consolidés, avec une sensibilité corrélative aux fluctuations de change. Peut-on couvrir cette exposition dans le cadre d’une documentation de hedge accounting ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise les états financiers consolidés et une créance de dividendes intragroupe générant un risque de change.
   - La créance de dividendes est traitée comme un poste intragroupe ; son éligibilité dépend donc des règles spécifiques IFRS 9 applicables en consolidation aux éléments intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, un élément intragroupe n’est en principe pas éligible, sauf exception pour le risque de change d’un poste monétaire intragroupe non totalement éliminé. Dans cette situation, la voie pertinente est la fair value hedge ; les modèles cash flow hedge et net investment hedge ne sont pas adaptés aux faits décrits.

## Points Opérationnels

   - Le point décisif est de vérifier si la créance de dividendes est bien un poste monétaire intragroupe dont le risque de change subsiste en résultat consolidé.
   - Si cette condition n’est pas remplie, aucun hedge accounting ne peut être documenté en consolidation sur cette créance intragroupe.
   - Si elle est remplie, la documentation doit identifier le risque de change couvert, l’instrument de couverture, le hedge ratio et démontrer l’effet en résultat consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividendes doit constituer un poste monétaire intragroupe.<br>- Les gains/pertes de change sur cette créance ne doivent pas être totalement éliminés en consolidation.<br>- Le risque couvert doit être le risque de change affectant le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividendes doit constituer un poste monétaire intragroupe.
   - Les gains/pertes de change sur cette créance ne doivent pas être totalement éliminés en consolidation.
   - Le risque couvert doit être le risque de change affectant le résultat consolidé.

**Raisonnment**:
La créance est un actif reconnu ; une fair value hedge peut viser un risque particulier affectant le résultat. Toutefois, en consolidation, un élément intragroupe n’est éligible que s’il s’agit du risque de change d’un poste monétaire intragroupe dont les écarts ne sont pas totalement éliminés, typiquement entre entités de monnaies fonctionnelles différentes.

**Implications pratiques**: Documenter la relation comme une couverture de juste valeur du risque de change de la créance si l’exception intragroupe en consolidation est satisfaite.

**Référence**:
 - 6.5.2(a)
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
Les faits décrits portent sur une créance déjà comptabilisée, avec une sensibilité de change sur sa valeur, et non sur une variabilité de flux d’une transaction future hautement probable. L’exception intragroupe en consolidation vise aussi certaines transactions intragroupe futures, mais ce n’est pas la situation décrite ici.

**Implications pratiques**: Ne pas documenter cette exposition comme cash flow hedge sur la seule base d’une créance de dividendes déjà reconnue.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait générateur décrit est une créance de dividendes intragroupe, non un investissement net dans une activité à l’étranger. IFRS 9 et IFRIC 16 réservent ce modèle au risque de change sur les net assets d’une foreign operation ; il ne vise pas un compte de dividendes à recevoir intragroupe.

**Implications pratiques**: Écarter la documentation en net investment hedge pour cette créance de dividendes.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16 section 2
    >The item being hedged ... may be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation