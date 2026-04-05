# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Des dividendes intragroupe ont été comptabilisés à recevoir, ce qui fait naître une variation potentielle liée au change dans les comptes consolidés. Est-il alors possible de mettre en place une relation de couverture sur cette seule composante de change ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - Les dividendes intragroupe à recevoir sont analysés dans les comptes consolidés.
   - Le dividende a déjà été comptabilisé en créance/dette intragroupe, donc il s'agit du risque de change sur un poste monétaire intragroupe reconnu.
   - La question vise la possibilité de désigner uniquement la composante de change comme élément couvert.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance/dette de dividende constitue un poste monétaire intragroupe dont les écarts de change ne sont pas entièrement éliminés en consolidation. Dans ce cas, la seule composante de change peut être désignée; sinon, la couverture n'est pas admissible en consolidation.

## Points Opérationnels

   - La documentation de couverture doit identifier l'instrument de couverture, l'élément couvert, le risque de change couvert et la manière d'évaluer l'efficacité.
   - Le point décisif est de démontrer que les écarts de change sur la créance/dette de dividende ne sont pas entièrement éliminés en consolidation.
   - La désignation doit porter sur la seule composante de change, pas sur l'élément intragroupe dans son ensemble si seule cette composante est gérée.
   - Si cette condition d'exception n'est pas satisfaite, la réponse en consolidation devient non.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende est un poste monétaire intragroupe.<br>- Les écarts de change correspondants ne sont pas entièrement éliminés en consolidation.<br>- La seule composante de change est séparément identifiable et mesurable de façon fiable. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende est un poste monétaire intragroupe.
   - Les écarts de change correspondants ne sont pas entièrement éliminés en consolidation.
   - La seule composante de change est séparément identifiable et mesurable de façon fiable.

**Raisonnment**:
Dans cette situation, le dividende à recevoir est un actif reconnu. En consolidation, un élément intragroupe n'est en principe pas éligible, sauf exception pour le risque de change d'un poste monétaire intragroupe lorsque les gains/pertes de change ne sont pas entièrement éliminés. IFRS 9 permet aussi de désigner une composante de risque spécifique, telle que la composante de change.

**Implications pratiques**: Si ces conditions sont remplies, la désignation doit viser uniquement le risque de change sur la créance/dette de dividende reconnue.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.3.7
    >only changes in the cash flows or fair value ... attributable to a specific risk or risks
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les faits décrits portent sur des dividendes déjà comptabilisés à recevoir, donc sur une créance intragroupe reconnue et non sur une transaction future hautement probable. La logique IFRS fournie pour les transactions intragroupe en cash flow hedge vise surtout des flux futurs affectant le résultat consolidé; ce n'est pas le cas typique d'un dividende intragroupe déjà comptabilisé.

**Implications pratiques**: Cette voie ne paraît pas adaptée au cas présenté; l'analyse doit se concentrer sur une éventuelle couverture de juste valeur.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.5
    >This is usually the case for royalty payments, interest payments or management charges

### 3. Couverture d'un investissement net dans une activité à l'étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le cas décrit concerne une créance de dividende intragroupe comptabilisée, non un investissement net dans une activité étrangère. La couverture d'investissement net vise le risque de change lié aux net assets d'une activité étrangère, pas celui d'un dividende intragroupe à recevoir isolé.

**Implications pratiques**: Le modèle de couverture d'investissement net n'est pas le bon traitement pour cette créance de dividende.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity