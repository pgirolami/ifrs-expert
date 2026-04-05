# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - L’analyse est faite sous IFRS 9 pour une relation de couverture du risque de change en comptes consolidés.
   - Le dividende intragroupe a déjà donné lieu à une créance à recevoir comptabilisée ; la question porte donc sur un poste reconnu.
   - L’existence d’un instrument de couverture éligible n’est pas en cause ; la question porte sur l’éligibilité de l’élément couvert en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance de dividende intragroupe est un poste monétaire dont les écarts de change affectent encore le résultat consolidé parce qu’ils ne sont pas totalement éliminés. Dans ce cas, la documentation pertinente est une couverture de juste valeur du risque de change ; les modèles de cash flow hedge et de net investment hedge ne correspondent pas aux faits tels que posés.

## Points Opérationnels

   - Le point clé se juge au niveau consolidé : il faut démontrer un impact résiduel en résultat consolidé des écarts de change sur la créance/payable de dividende.
   - Si les écarts de change sont totalement éliminés en consolidation, aucun élément couvert éligible n’existe dans les comptes consolidés.
   - Si l’exception intragroupe s’applique, la désignation et la documentation doivent être formalisées à l’inception de la relation de couverture en consolidation.
   - La documentation doit identifier le poste couvert comme le risque de change de la créance monétaire intragroupe reconnue, et non comme un investissement net dans l’opération étrangère.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende intragroupe est libellée dans une devise créant une exposition de change au niveau du groupe<br>- les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation<br>- la documentation vise le risque de change du poste monétaire reconnu, et non le dividende intragroupe comme flux éliminé |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende intragroupe est libellée dans une devise créant une exposition de change au niveau du groupe
   - les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation
   - la documentation vise le risque de change du poste monétaire reconnu, et non le dividende intragroupe comme flux éliminé

**Raisonnment**:
Le dividende intragroupe a déjà donné lieu à une créance reconnue ; l’exposition visée porte donc sur un actif comptabilisé. En consolidation, les éléments intragroupe sont en principe exclus, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Dans cette situation, le modèle pertinent est la couverture de juste valeur.

**Implications pratiques**: Documenter en consolidation une couverture de juste valeur du risque de change sur la créance/payable de dividende intragroupe.

**Référence**:
 - IFRS 9 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items.
 - IFRS 9 6.3.6
    >the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item
 - IFRS 9 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - IFRS 9 6.4.1
    >at the inception of the hedging relationship there is formal designation and documentation

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans les faits décrits, le dividende n’est plus une transaction future hautement probable mais une créance déjà comptabilisée. Le risque que vous cherchez à couvrir est la réévaluation de change d’un poste monétaire reconnu, alors que le cash flow hedge vise une exposition à la variabilité de flux de trésorerie. Ce n’est donc pas le bon modèle ici.

**Implications pratiques**: Ne documentez pas ce solde déjà reconnu comme une couverture de flux de trésorerie.

**Référence**:
 - IFRS 9 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - IFRS 9 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements

### 3. Couverture d’un investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d’un investissement net vise le risque de change lié aux actifs nets d’une opération étrangère. Une créance de dividende intragroupe déjà comptabilisée est un poste monétaire intragroupe distinct, et non un montant d’actifs nets couvert. Ce traitement n’est donc pas applicable à votre cas.

**Implications pratiques**: Ne rattachez pas cette créance de dividende à une relation de couverture d’investissement net.

**Référence**:
 - IFRIC 16 7
    >This Interpretation applies only to hedges of net investments in foreign operations
 - IFRIC 16 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation