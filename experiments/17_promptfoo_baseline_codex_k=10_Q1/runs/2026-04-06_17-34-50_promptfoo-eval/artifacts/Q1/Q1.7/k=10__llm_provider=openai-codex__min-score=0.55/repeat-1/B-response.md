# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Est-il recevable, au regard des IFRS, de documenter une couverture du risque de change sur des dividendes intragroupe ayant donné lieu à la reconnaissance d’une créance dans les comptes consolidés ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise les comptes consolidés établis selon les IFRS.
   - Le dividende intragroupe a été déclaré et a donné lieu à la comptabilisation d'une créance et d'une dette intragroupe monétaires.
   - La créance et la dette sont libellées dans une devise créant un risque de change entre deux entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que l'effet de change n'est pas intégralement éliminé en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une position monétaire intragroupe peut être un élément couvert pour le seul risque de change si les écarts de change ne sont pas totalement éliminés. Dans cette situation, la documentation est recevable principalement en couverture de juste valeur, mais pas comme couverture d'investissement net sur le dividende lui-même.

## Points Opérationnels

   - La documentation doit être mise en place au titre des comptes consolidés et viser explicitement le risque de change sur l'élément monétaire intragroupe reconnu.
   - Le point décisif est de démontrer que les écarts de change sur la créance/dette de dividende ne sont pas totalement éliminés en consolidation du fait de monnaies fonctionnelles différentes.
   - Si le dividende n'était encore qu'une transaction future intragroupe, l'analyse relèverait d'abord des règles sur les transactions intragroupe hautement probables, et non d'une créance déjà comptabilisée.
   - Il faut conserver la documentation formelle de la relation de couverture et de l'évaluation de son efficacité conformément à IFRS 9 6.4.1.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un élément monétaire reconnu.<br>- Le risque de change doit donner lieu à des gains ou pertes non totalement éliminés en consolidation.<br>- La relation de couverture doit satisfaire aux critères de documentation et d'efficacité d'IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un élément monétaire reconnu.
   - Le risque de change doit donner lieu à des gains ou pertes non totalement éliminés en consolidation.
   - La relation de couverture doit satisfaire aux critères de documentation et d'efficacité d'IFRS 9.

**Raisonnment**:
Ici, le dividende déclaré a généré une créance intragroupe reconnue, donc un élément monétaire existant. IFRS 9 admet, par exception en consolidation, que le risque de change d'un élément monétaire intragroupe soit désigné comme élément couvert lorsqu'il génère des écarts de change non totalement éliminés ; ce schéma correspond à une exposition sur un actif reconnu affectant le résultat.

**Implications pratiques**: La documentation peut viser le risque de change de la créance de dividende dans les comptes consolidés si l'exposition impacte bien le résultat consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.3.1
    >a recognised asset or liability
 - 6.5.1
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, le dividende a déjà donné lieu à une créance reconnue : il ne s'agit plus d'une transaction future hautement probable mais d'un montant dû. Le fait générateur décrit correspond donc à une exposition de change sur une position monétaire existante, et non à une variabilité de flux futurs au sens présenté pour les transactions intragroupe de type prévisionnel.

**Implications pratiques**: Le modèle de cash flow hedge n'est pas le plus approprié pour une créance de dividende déjà comptabilisée en consolidation.

**Référence**:
 - 6.5.1
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.5
    >This is usually the case for royalty payments, interest payments or management charges ... unless there is a related external transaction.

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur des dividendes intragroupe ayant donné lieu à une créance, non sur la couverture du risque de change attaché au montant net d'investissement dans une activité étrangère. IFRIC 16 traite la couverture du risque de change d'un investissement net dans une entité étrangère ; une créance de dividende reconnue est une exposition distincte de cet investissement net.

**Implications pratiques**: Le dividende intragroupe ne doit pas être documenté comme un hedge de net investment du seul fait qu'il provient d'une filiale étrangère.

**Référence**:
 - 6.5.1
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >applies only to hedges of net investments in foreign operations
 - ifric-16 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation