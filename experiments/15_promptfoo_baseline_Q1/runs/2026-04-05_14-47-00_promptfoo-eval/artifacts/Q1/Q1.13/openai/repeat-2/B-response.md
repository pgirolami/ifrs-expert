# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Dans les comptes consolidés, des dividendes intragroupe ont été décidés et une créance à recevoir a été comptabilisée. Dans ce contexte, la composante de risque de change associée à cette créance peut-elle être intégrée dans une relation de couverture documentée ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La créance de dividende intragroupe est un poste monétaire reconnu.
   - Cette créance est libellée dans une devise qui crée un risque de change dans les comptes consolidés.
   - Le risque de change sur cette créance n’est pas totalement éliminé en consolidation, notamment parce que les entités concernées ont des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, la composante de risque de change d’une créance intragroupe reconnue peut entrer dans une relation de couverture documentée en comptes consolidés si elle relève de l’exception visant les postes monétaires intragroupe. Dans ce cas, un schéma de fair value hedge ou de cash flow hedge peut être envisageable selon le risque documenté ; en revanche, la couverture d’investissement net n’est pas adaptée à cette créance.

## Points Opérationnels

   - La qualification doit être appréciée au niveau des comptes consolidés, pas seulement dans les comptes individuels.
   - Le point décisif est de démontrer que la créance de dividende est un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation.
   - La documentation de couverture doit être formalisée dès l’origine de la relation et préciser l’instrument de couverture, l’élément couvert, le risque couvert et le test d’efficacité.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit être un poste monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.<br>- Le risque couvert doit pouvoir affecter le résultat consolidé. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La variabilité des flux de trésorerie en devise de la créance doit affecter le résultat consolidé.<br>- La créance doit relever de l’exception applicable aux postes monétaires intragroupe en devise. |
| 3. Couverture d’investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un poste monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.
   - Le risque couvert doit pouvoir affecter le résultat consolidé.

**Raisonnment**:
La créance de dividende déjà comptabilisée est un actif reconnu, ce qui correspond au périmètre d’une fair value hedge. En comptes consolidés, les éléments intragroupe sont en principe exclus, sauf l’exception visant le risque de change d’un poste monétaire intragroupe lorsqu’il génère des écarts non totalement éliminés en consolidation.

**Implications pratiques**: Il faut documenter la relation comme couverture du risque de change sur un actif reconnu dans les comptes consolidés.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La variabilité des flux de trésorerie en devise de la créance doit affecter le résultat consolidé.
   - La créance doit relever de l’exception applicable aux postes monétaires intragroupe en devise.

**Raisonnment**:
IFRS 9 permet une cash flow hedge d’un actif reconnu lorsque la variabilité des flux est attribuable à un risque particulier et affecte le résultat. Pour cette créance intragroupe, cela n’est possible en consolidé que si le risque de change du poste monétaire subsiste au niveau consolidé et entre dans l’exception prévue par IFRS 9.

**Implications pratiques**: La documentation doit viser la variabilité des flux en devise de la créance et son impact en résultat consolidé.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur une créance de dividende intragroupe reconnue, non sur un investissement net dans une activité étrangère. Le modèle de net investment hedge vise le risque de change attaché aux net assets d’une activité étrangère incluse dans les états financiers, pas une créance de dividende isolée.

**Implications pratiques**: Cette approche ne doit pas être retenue pour documenter la couverture de la créance de dividende.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16.2
    >The item being hedged ... may be an amount of net assets