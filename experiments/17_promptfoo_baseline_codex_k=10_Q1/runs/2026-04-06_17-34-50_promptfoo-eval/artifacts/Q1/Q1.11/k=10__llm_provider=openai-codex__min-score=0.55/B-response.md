# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>L’exposition au change générée par des dividendes intragroupe, une fois la créance correspondante enregistrée, peut-elle être couverte et documentée en hedge accounting dans les comptes consolidés ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question vise l'application de la comptabilité de couverture selon IFRS 9 dans des comptes consolidés.
   - Le dividende intragroupe a déjà été comptabilisé en créance/dette, de sorte qu'il s'agit d'un poste monétaire intragroupe exposé au risque de change.
   - L'exposition de change sur cette créance/dette affecte le résultat consolidé parce qu'elle n'est pas totalement éliminée en consolidation lorsque les entités ont des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en comptes consolidés, si le dividende intragroupe comptabilisé constitue un poste monétaire intragroupe dont le risque de change n'est pas totalement éliminé en consolidation. Dans ce cas, la voie pertinente est la fair value hedge; les modèles cash flow hedge et net investment hedge ne correspondent pas aux faits décrits.

## Points Opérationnels

   - Le point clé est le moment: une fois le dividende enregistré, l'analyse porte sur un poste monétaire intragroupe existant, non sur une transaction future.
   - En consolidé, il faut démontrer que le risque de change sur la créance/dette de dividende affecte bien le résultat consolidé et n'est pas totalement éliminé.
   - La documentation doit identifier précisément l'instrument de couverture, le poste monétaire de dividende couvert, le risque de change couvert et l'évaluation de l'efficacité selon IFRS 9 6.4.1.
   - Si l'exposition de change n'affecte pas le résultat consolidé, la couverture ne peut pas être qualifiée en hedge accounting dans les comptes consolidés.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende est un poste monétaire intragroupe.<br>- Les entités concernées ont des monnaies fonctionnelles différentes.<br>- Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende est un poste monétaire intragroupe.
   - Les entités concernées ont des monnaies fonctionnelles différentes.
   - Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.

**Raisonnment**:
Ici, le dividende intragroupe est déjà enregistré en créance/dette: il s'agit d'un poste monétaire intragroupe reconnu. IFRS 9 permet, par exception, de désigner en consolidé le risque de change d'un poste monétaire intragroupe s'il génère des écarts de change non totalement éliminés; cela correspond à une exposition sur un élément reconnu pouvant affecter le résultat.

**Implications pratiques**: La documentation de couverture en consolidé doit viser le risque de change du poste monétaire intragroupe déjà reconnu, dans un schéma de fair value hedge.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.5.8
    >the hedging gain or loss on the hedged item shall adjust the carrying amount of the hedged item ... and be recognised in profit or loss

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur un dividende intragroupe déjà comptabilisé en créance/dette, donc sur une exposition existante et non sur une transaction future hautement probable. Dans les extraits fournis, l'exception intragroupe en consolidé pour les cash flow hedges vise surtout des transactions intragroupe futures hautement probables en devise, pas une créance de dividende déjà constatée.

**Implications pratiques**: Ce modèle n'est pas le bon véhicule comptable pour couvrir la créance de dividende déjà enregistrée en consolidé.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item
 - B6.3.5
    >the foreign currency risk of a forecast intragroup transaction will affect consolidated profit or loss

### 3. Couverture d'un investissement net dans une activité à l'étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Un dividende intragroupe comptabilisé en créance/dette n'est pas un investissement net dans une activité à l'étranger mais un poste monétaire intragroupe distinct. Le modèle de net investment hedge vise le risque de change sur les net assets d'une activité étrangère inclus dans les états financiers, ce qui ne correspond pas au fait décrit.

**Implications pratiques**: Il ne faut pas documenter cette couverture comme hedge d'investissement net, sauf si l'élément couvert était réellement une exposition de net investment, ce qui n'est pas le cas ici.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16 2
    >The item being hedged ... may be an amount of net assets
 - ifric-16 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation