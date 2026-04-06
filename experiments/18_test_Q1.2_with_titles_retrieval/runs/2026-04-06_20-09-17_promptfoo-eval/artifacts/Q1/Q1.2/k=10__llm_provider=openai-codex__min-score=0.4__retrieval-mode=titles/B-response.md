# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ifrs9`
   - `ifric16`

## Hypothèses
   - La question vise uniquement la possibilité de documenter une relation de couverture dans les comptes consolidés sur le risque de change d’une créance de dividende intragroupe déjà comptabilisée.
   - La créance de dividende est un élément monétaire intragroupe libellé dans une devise créant un risque de change en consolidation.
   - L’analyse est limitée aux trois modèles de couverture déjà identifiés.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la voie la plus pertinente est la couverture de juste valeur du risque de change de la créance intragroupe, à condition que ce risque de change ne soit pas totalement éliminé en consolidation. La couverture de flux de trésorerie n’est pas adaptée aux faits décrits, et la couverture d’investissement net ne vise pas une créance de dividende.

## Points Opérationnels

   - La documentation doit être mise en place à l’origine de la relation de couverture, avec identification de l’instrument, de l’élément couvert, du risque de change couvert et du test d’efficacité.
   - En consolidation, il faut démontrer que le risque de change sur la créance intragroupe n’est pas entièrement éliminé lors de la consolidation.
   - Si la couverture est qualifiée en juste valeur, les variations de l’instrument de couverture et de l’élément couvert au titre du risque couvert passent de manière cohérente en résultat.
   - Le modèle d’investissement net ne doit pas être utilisé pour remplacer une couverture de créance de dividende ; il répond à une logique différente de couverture des net assets d’une activité étrangère.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un élément monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.<br>- La relation de couverture doit être formellement désignée et documentée dès l’origine avec les critères d’efficacité IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un élément monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.
   - La relation de couverture doit être formellement désignée et documentée dès l’origine avec les critères d’efficacité IFRS 9.

**Raisonnment**:
Ici, la créance de dividende est déjà comptabilisée : il s’agit donc d’un actif reconnu, ce qui correspond au modèle de juste valeur. En consolidation, un élément intragroupe n’est éligible que si son risque de change n’est pas totalement éliminé ; IFRS 9 prévoit précisément cette exception pour un élément monétaire intragroupe.

**Implications pratiques**: Le gain ou la perte sur l’instrument de couverture va en résultat, et l’ajustement de couverture sur la créance couverte va aussi en résultat.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.5.8
    >the hedging gain or loss on the hedged item shall adjust the carrying amount

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans les faits décrits, le dividende a déjà été comptabilisé en créance ; l’exposition porte donc sur la réévaluation de cette créance en devise, pas sur une transaction future hautement probable. Le modèle cash flow hedge vise surtout la variabilité de flux futurs, alors qu’ici le sujet est un actif monétaire déjà reconnu.

**Implications pratiques**: Ce modèle n’est pas le bon véhicule de documentation pour la partie change d’une créance de dividende déjà comptabilisée.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur une créance de dividende intragroupe, pas sur une exposition de conversion liée à un investissement net dans une activité à l’étranger. IFRIC 16 encadre ce modèle pour les écarts de change entre la devise fonctionnelle de l’opération étrangère et celle de la société mère, ce qui est différent d’un dividende à recevoir.

**Implications pratiques**: La documentation de couverture d’investissement net ne convient pas pour couvrir la partie change d’une créance de dividende intragroupe.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric16-10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - ifric16-11
    >The hedged item can be an amount of net assets