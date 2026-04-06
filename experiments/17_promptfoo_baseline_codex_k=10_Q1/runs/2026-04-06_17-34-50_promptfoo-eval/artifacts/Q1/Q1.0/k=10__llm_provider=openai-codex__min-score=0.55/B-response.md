# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - Le dividende intragroupe a donné lieu à la comptabilisation d’une créance intragroupe avant élimination de consolidation.
   - La question porte sur les comptes consolidés et sur la couverture du risque de change attaché à cette créance.
   - La créance de dividende est traitée comme un poste monétaire intragroupe dans le contexte décrit.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidé, un poste intragroupe n’est en principe pas éligible, sauf exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas, la documentation de couverture peut être envisagée, mais pas au titre d’une couverture de flux de trésorerie ni d’une couverture d’investissement net sur ces faits.

## Points Opérationnels

   - En premier lieu, qualifier la créance de dividende comme poste monétaire intragroupe et vérifier si ses écarts de change subsistent en résultat consolidé après éliminations.
   - Si ces écarts de change sont totalement éliminés en consolidation, la réponse est non en pratique.
   - Si un risque de change résiduel existe en consolidé, la documentation doit être mise en place à l’origine de la relation de couverture avec désignation formelle et test d’efficacité selon IFRS 9 6.4.1.
   - La démonstration clé est l’impact sur le résultat consolidé ; sans cet impact, l’éligibilité du poste couvert échoue.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire intragroupe.<br>- Les écarts de change sur cette créance ne doivent pas être totalement éliminés en consolidation.<br>- Le risque couvert doit affecter le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire intragroupe.
   - Les écarts de change sur cette créance ne doivent pas être totalement éliminés en consolidation.
   - Le risque couvert doit affecter le résultat consolidé.

**Raisonnment**:
La créance à recevoir est un actif reconnu, ce qui correspond au modèle de couverture de juste valeur d’un actif reconnu exposé à un risque particulier. En consolidé, cela n’est possible ici que si la créance de dividende constitue un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés à la consolidation et affectent le résultat consolidé.

**Implications pratiques**: La documentation n’est défendable en consolidé que si vous démontrez l’existence d’un risque de change résiduel au niveau du résultat consolidé.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans votre situation, le dividende a déjà donné lieu à la comptabilisation d’une créance à recevoir. Le sujet n’est donc plus un flux futur hautement probable, mais un poste reconnu. En outre, les indications IFRS visent les transactions intragroupe futures affectant le résultat consolidé, pas une créance intragroupe déjà comptabilisée sur dividende.

**Implications pratiques**: Ce modèle n’est pas le bon véhicule pour couvrir le change d’une créance de dividende déjà reconnue.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.
 - B6.3.5
    >This is usually the case for royalty payments, interest payments or management charges between members of the same group

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise le risque de change sur un dividende intragroupe à recevoir, donc sur une créance spécifique, et non sur le risque de change lié à un investissement net dans une activité à l’étranger. Le modèle de couverture d’investissement net ne correspond pas à ce fait générateur.

**Implications pratiques**: Il ne faut pas documenter cette créance de dividende comme une couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16 2
    >the item being hedged ... may be an amount of net assets