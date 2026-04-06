# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>La distribution de dividendes intragroupe a été reconnue sous la forme d’une créance dans les états financiers consolidés. Cette exposition de change peut-elle, en IFRS, être désignée comme élément couvert dans une relation de couverture ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question est analysée du point de vue des états financiers consolidés.
   - L’exposition visée est un risque de change sur une créance intragroupe résultant d’une distribution de dividendes.
   - La créance est un poste monétaire intragroupe et la question porte sur sa désignation comme élément couvert au titre d’IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, un poste intragroupe ne peut être désigné comme élément couvert que dans l’exception IFRS 9 relative au risque de change d’un poste monétaire intragroupe. Donc la créance de dividende intragroupe n’est éligible que si ses écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.

## Points Opérationnels

   - Le point décisif n’est pas le caractère intragroupe de la créance en soi, mais le fait que les écarts de change subsistent ou non dans le résultat consolidé.
   - Si les écarts de change sont totalement éliminés en consolidation, la créance ne peut pas être désignée comme élément couvert.
   - La relation de couverture doit être formellement désignée et documentée dès l’origine, avec identification du risque de change couvert et du test d’efficacité.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende constitue un poste monétaire intragroupe.<br>- Les gains ou pertes de change qui en résultent ne sont pas totalement éliminés en consolidation.<br>- Le risque de change affecte le résultat consolidé. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance de dividende est libellée dans une devise générant une variabilité des flux en monnaie fonctionnelle.<br>- Il s’agit d’un poste monétaire intragroupe relevant de l’exception IFRS 9.<br>- Le risque de change affecte le résultat consolidé parce qu’il n’est pas totalement éliminé en consolidation. |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende constitue un poste monétaire intragroupe.
   - Les gains ou pertes de change qui en résultent ne sont pas totalement éliminés en consolidation.
   - Le risque de change affecte le résultat consolidé.

**Raisonnment**:
La créance est, dans les faits décrits, un actif reconnu. IFRS 9 permet en principe une couverture de juste valeur d’un actif reconnu exposé à un risque particulier. Toutefois, en consolidation, les éléments intragroupe sont en principe exclus; seule l’exception visant le risque de change d’un poste monétaire intragroupe s’applique si les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé.

**Implications pratiques**: Possible seulement si l’entité documente la relation de couverture sur le risque de change résiduel au niveau consolidé.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est libellée dans une devise générant une variabilité des flux en monnaie fonctionnelle.
   - Il s’agit d’un poste monétaire intragroupe relevant de l’exception IFRS 9.
   - Le risque de change affecte le résultat consolidé parce qu’il n’est pas totalement éliminé en consolidation.

**Raisonnment**:
IFRS 9 admet une couverture de flux de trésorerie pour la variabilité des flux d’un actif reconnu due à un risque particulier. Pour une créance intragroupe en devise, cela n’est recevable en consolidation que via l’exception sur les postes monétaires intragroupe. Dans cette situation, l’éligibilité dépend donc du fait que le risque de change subsiste au niveau consolidé et affecte le résultat consolidé.

**Implications pratiques**: Si ces conditions sont remplies, la couverture peut être structurée comme une couverture de flux de trésorerie du risque de change.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’un investissement net dans une activité à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite concerne une créance de dividende intragroupe, non un montant de net assets d’une activité étrangère. IFRS 9 et IFRIC 16 réservent ce modèle à la couverture du risque de change sur un investissement net dans une activité à l’étranger. Une créance de dividende reconnue ne correspond pas à cet objet de couverture.

**Implications pratiques**: Ce modèle ne doit pas être retenu pour couvrir le risque de change de la créance de dividende intragroupe.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >applies only to hedges of net investments in foreign operations
 - ifric-16 10
    >the hedged item can be an amount of net assets