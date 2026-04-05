# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Au niveau consolidé, l’entité constate une créance liée à des dividendes intragroupe et supporte, de ce fait, une exposition au risque de change. Cette exposition peut-elle faire l’objet d’une documentation de couverture conforme aux IFRS ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La créance de dividendes intragroupe est un élément monétaire comptabilisé qui génère une exposition de change dans les comptes consolidés.
   - La question porte sur l’éligibilité de cette exposition au hedge accounting selon IFRS 9 en comptes consolidés.

## Recommandation

**OUI**

Oui, dans cette situation, l’exposition de change sur une créance intragroupe monétaire peut faire l’objet d’une documentation de couverture IFRS au niveau consolidé. Le modèle le plus adapté ici est la couverture de juste valeur, sous réserve que le risque de change ne soit pas intégralement éliminé en consolidation.

## Points Opérationnels

   - Au niveau consolidé, vérifier et documenter que l’écart de change sur la créance intragroupe n’est pas entièrement éliminé en consolidation.
   - La documentation doit être établie à l’origine de la relation de couverture, avec identification de l’instrument de couverture, de la créance couverte et du risque de change couvert.
   - L’analyse d’efficacité doit être formalisée conformément à IFRS 9, y compris le lien économique et le hedge ratio.
   - Le choix pratique à privilégier sur les faits décrits est la couverture de juste valeur, pas la couverture d’investissement net.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI | - Le risque de change sur la créance intragroupe ne doit pas être totalement éliminé en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI

**Conditions**:
   - Le risque de change sur la créance intragroupe ne doit pas être totalement éliminé en consolidation.

**Raisonnment**:
La créance de dividendes est, selon les hypothèses, un actif monétaire déjà comptabilisé exposé au risque de change. IFRS 9 permet qu’un élément monétaire intragroupe soit désigné comme élément couvert en consolidation pour son risque de change lorsqu’il crée une exposition non totalement éliminée en consolidation. Ce risque affecte le résultat, ce qui correspond à une couverture de juste valeur d’un actif comptabilisé au titre d’un risque particulier.

**Implications pratiques**: Documenter la relation de couverture sur le risque de change de la créance intragroupe et comptabiliser l’inefficacité en résultat.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les faits décrits portent sur une créance déjà comptabilisée en tant qu’élément monétaire intragroupe, avec une exposition de change sur sa valeur en consolidation. Dans cette situation, le risque décrit est celui de réévaluation d’un poste existant, et non une variabilité de flux de trésorerie d’une transaction future ou d’un poste à flux variables. Le cas s’aligne donc sur une couverture de juste valeur plutôt que sur une couverture de flux.

**Implications pratiques**: Ne pas retenir ce modèle sur la seule base des faits décrits pour la créance de dividendes déjà reconnue.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La créance de dividendes intragroupe n’est pas un investissement net dans une activité à l’étranger mais un poste monétaire intragroupe distinct. IFRIC 16 limite ce modèle aux couvertures du risque de change lié aux net assets d’une activité étrangère inclus dans les états financiers. Ce n’est pas la situation décrite ici.

**Implications pratiques**: Ne pas documenter cette exposition comme couverture d’investissement net.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16 7
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16 10
    >the hedged item can be an amount of net assets