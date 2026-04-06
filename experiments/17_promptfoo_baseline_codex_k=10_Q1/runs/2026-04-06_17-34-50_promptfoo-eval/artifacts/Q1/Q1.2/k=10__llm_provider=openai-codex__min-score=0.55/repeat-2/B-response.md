# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ifrs-9`

## Hypothèses
   - La question porte uniquement sur les modèles de comptabilité de couverture d’IFRS 9 envisageables dans les comptes consolidés.
   - Le dividende intragroupe a généré une créance monétaire libellée en devise étrangère, donc une exposition de change existe au niveau consolidé.
   - Le dividende est déjà comptabilisé en créance à la date d’analyse ; il ne s’agit donc plus seulement d’un flux futur non encore reconnu.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie la plus cohérente est soit l’absence de comptabilité de couverture, soit éventuellement une couverture de juste valeur de la créance en devise. La couverture de flux de trésorerie ne convient en principe pas une fois la créance reconnue, et la couverture d’investissement net ne vise pas ce dividende.

## Points Opérationnels

   - Comme la créance de dividende est déjà reconnue, le point de départ de l’analyse est un poste monétaire existant, pas un flux futur.
   - En pratique, l’absence de comptabilité de couverture est souvent la voie la plus simple si le dérivé et l’effet de change de la créance passent tous deux en résultat.
   - Si une documentation de couverture est néanmoins souhaitée, la piste à examiner est la couverture de juste valeur de la créance en devise.
   - La couverture d’investissement net doit être réservée aux expositions liées à un investissement net dans une activité étrangère, ce qui ne correspond pas au dividende décrit.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance en dividende est bien exposée à un risque de change au niveau consolidé<br>- Une désignation formelle de la relation de couverture est mise en place<br>- L’entité choisit d’appliquer la comptabilité de couverture plutôt qu’un simple dérivé à la JV par résultat |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Sans comptabilité de couverture | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance en dividende est bien exposée à un risque de change au niveau consolidé
   - Une désignation formelle de la relation de couverture est mise en place
   - L’entité choisit d’appliquer la comptabilité de couverture plutôt qu’un simple dérivé à la JV par résultat

**Raisonnment**:
Ici, le dividende a déjà été comptabilisé en créance : l’exposition porte donc sur un poste monétaire existant en devise. Une documentation de couverture de juste valeur peut être envisagée sur le risque de change de cette créance dans les comptes consolidés, mais seulement si une relation de couverture est formellement désignée et suivie comme telle.

**Implications pratiques**: Solution potentiellement documentable pour la créance reconnue, mais plus lourde opérationnellement que l’absence de hedge accounting.

**Référence**:
 - 5.7.3
    >A gain or loss on financial assets or financial liabilities that are hedged items in a hedging relationship shall be recognised
 - B5.7.2
    >If there is a hedging relationship between a non-derivative monetary asset and a non-derivative monetary liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans les faits donnés, le dividende est déjà comptabilisé en créance. L’exposition n’est donc plus celle d’un flux futur non encore reconnu, mais celle d’un actif monétaire déjà inscrit ; la couverture de flux de trésorerie n’est pas la forme la plus adaptée à ce cas tel que posé.

**Implications pratiques**: Cette approche ne paraît pas appropriée pour documenter la partie change d’une créance déjà reconnue.

**Référence**:
 - B6.6.14
    >the gain or loss on the forward exchange contract that is reclassified from the cash flow hedge reserve to profit or loss
 - B6.6.15
    >when the net position affects profit or loss

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé ici porte sur la créance née d’un dividende intragroupe, non sur un investissement net dans une activité à l’étranger. Sur les faits décrits, ce traitement ne cible pas l’objet économique à couvrir dans les comptes consolidés.

**Implications pratiques**: À écarter pour la partie change de ce dividende comptabilisé en créance.

**Référence**:
 - 5.7.1
    >a hedge of a net investment
 - B5.7.2
    >a hedge of a net investment

### 4. Sans comptabilité de couverture
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, c’est l’option la plus directe. Le dérivé serait comptabilisé à la juste valeur par résultat, tandis que la créance monétaire en devise porte aussi un effet de change en résultat ; sur les faits donnés, cela permet de couvrir économiquement le risque sans documentation IFRS 9 de couverture.

**Implications pratiques**: Approche la plus simple en consolidation si l’objectif est de neutraliser économiquement le change sans formalisme de hedge accounting.

**Référence**:
 - 5.7.1
    >A gain or loss on a financial asset or financial liability that is measured at fair value shall be recognised in profit or loss unless
 - 5.7.2
    >A gain or loss on a financial asset that is measured at amortised cost ... shall be recognised in profit or loss