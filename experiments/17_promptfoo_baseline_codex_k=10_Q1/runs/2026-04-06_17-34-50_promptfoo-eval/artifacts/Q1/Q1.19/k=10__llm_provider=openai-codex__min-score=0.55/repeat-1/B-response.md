# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Dans un schéma où des dividendes intragroupe ont déjà été reconnus en créance à recevoir, la question se pose du traitement du risque de change associé en consolidation. Ce risque peut-il être formellement documenté dans une relation de couverture ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - Le dividende intragroupe a déjà été déclaré et comptabilisé en créance/dette intragroupe, donc comme élément monétaire.
   - L’analyse porte sur les états financiers consolidés et sur l’application d’IFRS 9.
   - Le risque visé est le risque de change sur cette créance/dette intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, le risque de change d’un élément monétaire intragroupe peut être documenté dans une relation de couverture si les écarts de change ne sont pas entièrement éliminés en consolidation. En pratique, cela peut être documenté surtout en couverture de juste valeur ; une couverture de flux de trésorerie n’est envisageable que si l’entité démontre une véritable variabilité des flux en monnaie fonctionnelle et respecte IFRS 9.

## Points Opérationnels

   - Le point décisif en consolidation est de vérifier si les écarts de change sur la créance/dette intragroupe sont ou non entièrement éliminés.
   - La documentation de couverture doit être formalisée dès l’origine de la relation et préciser l’instrument, l’élément couvert, le risque couvert et le test d’efficacité.
   - Dans ce schéma de dividende déjà déclaré et comptabilisé, la couverture de juste valeur est généralement l’angle le plus directement aligné avec l’existence d’une créance monétaire reconnue.
   - Une couverture d’investissement net ne convient pas au simple risque de change sur une créance de dividende intragroupe déjà née.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - Les écarts de change sur la créance/dette intragroupe ne sont pas entièrement éliminés en consolidation.<br>- La relation de couverture est formellement désignée et documentée dès l’origine conformément à IFRS 9.6.4.1.<br>- Les critères d’efficacité de la couverture sont satisfaits. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - Les écarts de change sur l’élément monétaire intragroupe affectent le résultat consolidé et ne sont pas entièrement éliminés.<br>- L’entité peut démontrer une variabilité des flux de trésorerie attribuable au risque de change sur l’élément reconnu.<br>- La documentation initiale et les critères d’efficacité d’IFRS 9.6.4.1 sont respectés. |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les écarts de change sur la créance/dette intragroupe ne sont pas entièrement éliminés en consolidation.
   - La relation de couverture est formellement désignée et documentée dès l’origine conformément à IFRS 9.6.4.1.
   - Les critères d’efficacité de la couverture sont satisfaits.

**Raisonnment**:
Ici, il existe déjà une créance intragroupe reconnue, donc un actif monétaire existant. IFRS 9 permet de désigner comme élément couvert un actif ou passif reconnu, et prévoit explicitement qu’en consolidation le risque de change d’un élément monétaire intragroupe peut être un élément couvert s’il génère des écarts non entièrement éliminés. Cette voie est cohérente avec un risque de change portant sur une créance déjà comptabilisée.

**Implications pratiques**: Possible en consolidation, mais seulement si l’élément monétaire intragroupe crée bien une exposition de change résiduelle au niveau consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.4.1
    >at the inception ... there is formal designation and documentation

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les écarts de change sur l’élément monétaire intragroupe affectent le résultat consolidé et ne sont pas entièrement éliminés.
   - L’entité peut démontrer une variabilité des flux de trésorerie attribuable au risque de change sur l’élément reconnu.
   - La documentation initiale et les critères d’efficacité d’IFRS 9.6.4.1 sont respectés.

**Raisonnment**:
IFRS 9 admet une couverture de flux de trésorerie sur un actif ou passif reconnu lorsqu’il existe une variabilité de flux pouvant affecter le résultat. Dans ce cas précis, l’exposition porte sur une créance intragroupe déjà reconnue ; cette approche n’est recevable que si l’entité démontre que le risque de change crée une variabilité pertinente des flux en monnaie fonctionnelle au niveau consolidé. À défaut, cette qualification serait moins naturelle que la couverture de juste valeur.

**Implications pratiques**: Juridiquement possible sous IFRS 9, mais plus exigeant à justifier dans ce schéma qu’une couverture de juste valeur.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.4.1
    >the hedging relationship meets all of the following hedge effectiveness requirements

### 3. Couverture d’un investissement net dans une activité à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait décrit est un dividende intragroupe déjà reconnu en créance à recevoir, donc une créance/dette monétaire distincte. Une couverture d’investissement net vise le risque de change sur les net assets d’une activité étrangère, non le risque de change sur un dividende déclaré et payable. Dans cette situation, ce modèle ne correspond pas à l’objet couvert.

**Implications pratiques**: Ce risque ne doit pas être documenté comme une couverture d’investissement net ; il faut analyser la créance monétaire elle-même.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 10
    >the hedged item can be an amount of net assets
 - ifric-16 7
    >applies only to hedges of net investments in foreign operations