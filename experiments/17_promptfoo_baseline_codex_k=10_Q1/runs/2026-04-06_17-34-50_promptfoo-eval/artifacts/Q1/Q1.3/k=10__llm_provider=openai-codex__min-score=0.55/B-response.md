# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Peut-on désigner, dans les comptes consolidés, le risque de change afférent à des dividendes intragroupe donnant lieu à la comptabilisation d’une créance à recevoir dans une relation de couverture documentée ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise les comptes consolidés et l’application de la comptabilité de couverture selon IFRS 9.
   - Les dividendes intragroupe sont envisagés soit après leur mise en paiement avec comptabilisation d’une créance/dette intragroupe, soit avant cette comptabilisation comme flux intragroupe prévu.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si le dividende intragroupe a donné lieu à une créance/dette monétaire entre entités de groupe ayant des monnaies fonctionnelles différentes, de sorte que le risque de change n’est pas totalement éliminé en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur ; les autres modèles ne conviennent pas à cette situation.

## Points Opérationnels

   - Le point clé est le moment : avant déclaration/paiement, on est sur un flux intragroupe ; après comptabilisation de la créance, on est sur un poste monétaire reconnu.
   - En consolidation, il faut démontrer que les écarts de change sur la créance/dette intragroupe ne sont pas totalement éliminés parce que les entités ont des monnaies fonctionnelles différentes.
   - La documentation de couverture doit identifier précisément le poste monétaire intragroupe, le risque de change couvert et la manière d’évaluer l’efficacité de la relation.
   - Si l’exposition ne relève pas d’un poste monétaire intragroupe affectant le résultat consolidé, la réponse est non en comptes consolidés.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - le dividende a déjà donné lieu à la comptabilisation d’une créance/dette intragroupe<br>- la créance/dette est libellée dans une monnaie différente de la monnaie fonctionnelle de l’une des entités concernées<br>- les écarts de change correspondants affectent le résultat consolidé et ne sont pas totalement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - le dividende a déjà donné lieu à la comptabilisation d’une créance/dette intragroupe
   - la créance/dette est libellée dans une monnaie différente de la monnaie fonctionnelle de l’une des entités concernées
   - les écarts de change correspondants affectent le résultat consolidé et ne sont pas totalement éliminés en consolidation

**Raisonnment**:
Dans cette situation, une créance à recevoir sur dividende déjà comptabilisée est un poste reconnu. IFRS 9 admet en consolidation, par exception, qu’un poste monétaire intragroupe exposé au change soit un élément couvert si les écarts de change ne sont pas totalement éliminés. La désignation n’est donc possible que dans ce cas précis.

**Implications pratiques**: La documentation de couverture doit viser le risque de change du poste monétaire intragroupe reconnu, et non un simple flux de dividende interne abstrait.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise un dividende intragroupe ayant déjà donné lieu à une créance à recevoir ; il ne s’agit donc plus d’une transaction future hautement probable à couvrir en flux. En outre, IFRS 9 ne permet, en consolidation, les transactions intragroupe prévues qu’à titre limité pour le risque de change lorsqu’elles affectent le résultat consolidé ; les exemples fournis excluent en pratique les paiements internes de type dividende.

**Implications pratiques**: Une documentation en cash flow hedge ne serait pas la base adaptée pour un dividende déjà déclaré et comptabilisé en créance intragroupe.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.5
    >This is usually the case for royalty payments, interest payments or management charges

### 3. Couverture d’un investissement net dans une activité à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé ici porte sur une créance de dividende intragroupe, non sur l’investissement net dans une activité à l’étranger. IFRIC 16 limite ce modèle au risque de change afférent aux net assets de l’activité étrangère inclus dans les états financiers ; un dividende à recevoir est d’une nature différente.

**Implications pratiques**: Ce modèle ne doit pas être utilisé pour couvrir un dividende intragroupe à recevoir.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 2
    >will apply only when the net assets of that foreign operation are included
 - ifric-16 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount