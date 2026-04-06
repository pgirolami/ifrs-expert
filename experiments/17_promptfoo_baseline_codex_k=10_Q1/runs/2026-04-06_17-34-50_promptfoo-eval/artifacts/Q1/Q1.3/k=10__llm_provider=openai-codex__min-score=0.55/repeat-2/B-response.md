# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Peut-on désigner, dans les comptes consolidés, le risque de change afférent à des dividendes intragroupe donnant lieu à la comptabilisation d’une créance à recevoir dans une relation de couverture documentée ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question vise les comptes consolidés établis en IFRS.
   - La mise en paiement ou la décision de dividende a conduit à comptabiliser une créance intragroupe libellée en devise.
   - La créance et la dette intragroupe correspondante sont monétaires et concernent des entités du groupe ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si le risque de change sur la créance monétaire intragroupe n’est pas entièrement éliminé en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur ; les modèles de cash flow hedge et de net investment hedge ne correspondent pas à cette situation.

## Points Opérationnels

   - Le point clé en consolidation est de vérifier si les écarts de change sur la créance/dette intragroupe monétaire subsistent au résultat consolidé.
   - Si le dividende n’est qu’une transaction intragroupe éliminée sans exposition résiduelle au résultat consolidé, la désignation échoue.
   - La qualification doit être appréciée à la date où la créance est reconnue ; avant cette date, on ne se situe pas dans le même schéma.
   - La documentation de couverture doit identifier précisément l’élément monétaire intragroupe, le risque de change couvert et l’effet attendu sur le résultat consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un élément monétaire exposé à un risque de change non entièrement éliminé en consolidation.<br>- Le risque couvert doit pouvoir affecter le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un élément monétaire exposé à un risque de change non entièrement éliminé en consolidation.
   - Le risque couvert doit pouvoir affecter le résultat consolidé.

**Raisonnment**:
La créance à recevoir sur dividende, une fois comptabilisée, est un actif reconnu. En consolidation, IFRS 9 autorise exceptionnellement la désignation du risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas entièrement éliminés. Dans ce cas précis, une relation de couverture documentée peut viser ce risque sur la créance reconnue.

**Implications pratiques**: Si ces conditions sont remplies, la désignation doit être structurée comme une couverture de juste valeur du risque de change de la créance reconnue.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les faits décrits portent sur une créance déjà comptabilisée au titre d’un dividende intragroupe, et non sur une transaction future hautement probable. L’exception IFRS 9 pour les transactions intragroupe en consolidation vise des opérations futures dont le risque de change affectera le résultat consolidé ; les dividendes intragroupe sont cités comme cas habituellement non éligibles.

**Implications pratiques**: La documentation ne doit pas être construite comme une couverture de flux de trésorerie de dividendes intragroupe déjà déclarés.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.5
    >This is usually the case for royalty payments, interest payments or management charges between members of the same group

### 3. Couverture d’un investissement net dans une activité à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise le risque de change sur une créance intragroupe de dividende, pas le risque de change sur des actifs nets d’une activité à l’étranger. Le modèle de net investment hedge concerne l’exposition liée à l’investissement net dans l’opération étrangère, non un dividende à recevoir entre entités du groupe.

**Implications pratiques**: Cette situation ne doit pas être documentée comme une couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation as defined in IAS 21
 - ifric-16 2
    >The item being hedged ... may be an amount of net assets
 - ifric-16 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation