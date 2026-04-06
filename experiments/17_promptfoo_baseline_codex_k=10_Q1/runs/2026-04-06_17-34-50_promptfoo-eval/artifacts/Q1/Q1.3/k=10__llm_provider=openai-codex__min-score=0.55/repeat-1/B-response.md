# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Peut-on désigner, dans les comptes consolidés, le risque de change afférent à des dividendes intragroupe donnant lieu à la comptabilisation d’une créance à recevoir dans une relation de couverture documentée ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question est analysée dans le cadre des comptes consolidés et de la comptabilité de couverture selon IFRS 9.
   - Le dividende intragroupe donne soit lieu à une créance monétaire intragroupe comptabilisée, soit à un flux intragroupe prévu avant comptabilisation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si le dividende intragroupe a déjà donné lieu à une créance monétaire intragroupe comptabilisée exposée à un risque de change non totalement éliminé en consolidation. En revanche, une couverture de flux de trésorerie d’un dividende intragroupe prévu n’est pas recevable dans cette situation.

## Points Opérationnels

   - Le point décisif est le moment: avant comptabilisation de la créance de dividende, la désignation en consolidation n’est pas recevable ici; après comptabilisation, elle peut l’être sous l’exception des postes monétaires intragroupe.
   - Il faut vérifier que les entités concernées ont des monnaies fonctionnelles différentes, faute de quoi il n’existe pas de risque de change éligible.
   - La documentation de couverture doit identifier précisément la créance intragroupe reconnue et démontrer que les écarts de change affectent encore le résultat consolidé.
   - Si la relation vise un dividende simplement déclaré ou anticipé sans créance monétaire reconnue, la réponse est non en comptes consolidés.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - le dividende a donné lieu à une créance monétaire intragroupe comptabilisée<br>- la créance et la dette correspondante sont entre entités ayant des monnaies fonctionnelles différentes<br>- les écarts de change correspondants ne sont pas totalement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - le dividende a donné lieu à une créance monétaire intragroupe comptabilisée
   - la créance et la dette correspondante sont entre entités ayant des monnaies fonctionnelles différentes
   - les écarts de change correspondants ne sont pas totalement éliminés en consolidation

**Raisonnment**:
Dans les comptes consolidés, un élément couvert doit en principe être externe au groupe. Toutefois, IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe s’il génère des écarts de change non totalement éliminés en consolidation. Une créance de dividende intragroupe déjà comptabilisée peut donc être désignée seulement dans ce cas.

**Implications pratiques**: Documenter la relation comme couverture d’un poste monétaire intragroupe existant, et non comme simple flux intragroupe futur.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Pour un flux intragroupe prévu, IFRS 9 n’admet en consolidation que certains risques de change qui affecteront le résultat consolidé. Le contexte précise que des flux intragroupe tels que redevances, intérêts ou management fees ne qualifient généralement pas faute d’effet sur le résultat consolidé; un dividende intragroupe est encore moins apte à affecter ce résultat. Il ne peut donc pas être désigné ici comme élément couvert en cash flow hedge.

**Implications pratiques**: Un dividende intragroupe prévu ne doit pas être documenté comme élément couvert de cash flow hedge dans les comptes consolidés.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.5
    >This is usually the case for royalty payments, interest payments or management charges between members of the same group