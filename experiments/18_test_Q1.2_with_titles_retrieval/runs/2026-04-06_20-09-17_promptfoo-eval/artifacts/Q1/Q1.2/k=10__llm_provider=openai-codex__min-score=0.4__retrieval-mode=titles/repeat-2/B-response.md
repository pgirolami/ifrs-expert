# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ifrs9`
   - `ifric16`

## Hypothèses
   - Le dividende intragroupe a généré une créance/dette monétaire intragroupe libellée en devise.
   - La question vise les comptes consolidés et la couverture du risque de change attaché à cette créance.
   - Le risque de change sur cette créance n’est pas totalement éliminé en consolidation uniquement si les entités concernées ont des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture peut viser la partie change d’une créance intragroupe seulement si cette créance monétaire crée un risque de change non totalement éliminé. Dans ce cas, la voie la plus cohérente est la couverture de juste valeur ; la couverture de flux de trésorerie peut aussi être envisagée ; la couverture d’investissement net ne convient pas au dividende lui-même.

## Points Opérationnels

   - En consolidation, le point décisif est de démontrer que la créance de dividende constitue bien un élément monétaire intragroupe dont le risque de change n’est pas totalement éliminé.
   - La documentation doit être formalisée à l’origine de la relation de couverture et identifier l’instrument de couverture, l’élément couvert, le risque de change couvert et le test d’efficacité.
   - Si l’objectif est de couvrir la réévaluation de la créance déjà comptabilisée, la couverture de juste valeur est en pratique la plus directement alignée avec le fait générateur décrit.
   - La couverture d’investissement net doit être réservée aux net assets d’une activité étrangère ; elle ne se substitue pas à une couverture de créance de dividende.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un élément monétaire exposé au change.<br>- Les écarts de change doivent affecter le résultat consolidé, c’est-à-dire ne pas être totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La documentation doit viser la variabilité des flux en monnaie fonctionnelle liée au change sur la créance reconnue.<br>- Les écarts de change sur la créance intragroupe doivent affecter le résultat consolidé. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un élément monétaire exposé au change.
   - Les écarts de change doivent affecter le résultat consolidé, c’est-à-dire ne pas être totalement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, la créance de dividende est un actif reconnu et la composante change peut être désignée comme risque couvert si elle affecte le résultat consolidé. IFRS 9 autorise un actif reconnu ou une composante de risque comme élément couvert, et prévoit expressément l’exception des éléments monétaires intragroupe en consolidation lorsque les écarts de change ne sont pas totalement éliminés.

**Implications pratiques**: La variation de valeur du dérivé irait en résultat et l’ajustement de couverture sur la créance couverte aussi en résultat.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.7
    >only changes in the cash flows or fair value of an item attributable to a specific risk
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.5.8
    >the hedging gain or loss on the hedged item shall adjust the carrying amount

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La documentation doit viser la variabilité des flux en monnaie fonctionnelle liée au change sur la créance reconnue.
   - Les écarts de change sur la créance intragroupe doivent affecter le résultat consolidé.

**Raisonnment**:
Cette approche peut s’envisager si l’on documente la variabilité des flux de trésorerie en monnaie fonctionnelle attachés à l’encaissement du dividende en devise. En consolidation, elle reste soumise à la même condition clé : l’élément intragroupe n’est éligible que si le risque de change sur l’élément monétaire n’est pas totalement éliminé.

**Implications pratiques**: La part efficace du dérivé serait comptabilisée en OCI puis recyclée en résultat quand le risque couvert affecte le résultat.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.5.11
    >the portion of the gain or loss on the hedging instrument that is determined to be an effective hedge ... shall be recognised in other comprehensive income

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, l’exposition décrite porte sur une créance de dividende intragroupe comptabilisée, et non sur un montant de net assets d’une activité étrangère. Le modèle de couverture d’investissement net vise la devise d’un investissement net dans une activité étrangère en consolidation, pas la partie change d’un dividende intragroupe pris isolément.

**Implications pratiques**: Cette documentation ne doit pas être retenue pour couvrir la créance de dividende elle-même.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 11
    >The hedged item can be an amount of net assets
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation