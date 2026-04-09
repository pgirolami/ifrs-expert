# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ias32`
   - `ifrs19`
   - `ifric17`
   - `ifrs9`
   - `ifrs18`
   - `ifrs12`
   - `ias7`
   - `ias37`
   - `sic25`
   - `ifric16`
   - `sic29`
   - `ifric19`

## Hypothèses
   - La question vise les comptes consolidés IFRS et un dividende intragroupe libellé dans une devise différente de la monnaie fonctionnelle d’au moins une des entités concernées.
   - Une créance de dividende a déjà été comptabilisée avant l’analyse des éliminations de consolidation.
   - La couverture envisagée porte uniquement sur le risque de change attaché à cette créance intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, seulement si la créance intragroupe de dividende est un élément monétaire exposant le groupe à des écarts de change qui ne sont pas totalement éliminés en consolidation. Dans ce cas, une relation de couverture peut être documentée; sinon, non, et le dérivé reste comptabilisé à la juste valeur par résultat.

## Points Opérationnels

   - Le point décisif en consolidation est de démontrer que les écarts de change sur la créance de dividende intragroupe ne sont pas totalement éliminés.
   - La documentation de couverture doit être en place dès l’origine de la relation de couverture et respecter IFRS 9 sur la désignation et l’efficacité.
   - Si l’exposition consolidée n’existe pas, la documentation de couverture ne peut pas être soutenue pour cet élément précis.
   - À défaut de relation qualifiante, le dérivé sera suivi à la juste valeur par résultat, ce qui peut créer de la volatilité en résultat consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe<br>- Les écarts de change sur cette créance affectent le résultat consolidé et ne sont pas totalement éliminés en consolidation<br>- La relation de couverture satisfait aux critères de désignation et de documentation d’IFRS 9 |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Dérivé à la juste valeur par résultat | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe
   - Les écarts de change sur cette créance affectent le résultat consolidé et ne sont pas totalement éliminés en consolidation
   - La relation de couverture satisfait aux critères de désignation et de documentation d’IFRS 9

**Raisonnment**:
Dans vos comptes consolidés, un élément couvert doit en principe être avec une partie externe. L’exception vise toutefois un élément monétaire intragroupe lorsque son risque de change génère des gains ou pertes non totalement éliminés en consolidation. Si la créance de dividende remplit ce critère, une documentation de couverture de juste valeur peut être envisagée sur ce risque de change.

**Implications pratiques**: Vérifier d’abord si l’exposition de change subsiste réellement au niveau consolidé avant de formaliser la documentation.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans votre situation, le dividende n’est plus une transaction future intragroupe hautement probable: une créance a déjà été comptabilisée. La question ne porte donc plus sur un flux futur prévu, mais sur un actif monétaire déjà reconnu. Sur ces faits précis, ce modèle n’est pas le plus adapté.

**Implications pratiques**: Une fois la créance de dividende constatée, l’analyse doit se faire sur l’élément monétaire reconnu, pas comme flux futur prévu.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Un dividende intragroupe à recevoir correspond ici à une créance destinée à être réglée, non à un investissement net dans une activité étrangère. Le modèle de couverture d’investissement net vise l’exposition sur les actifs nets d’une opération étrangère, pas le risque de change d’un dividende intragroupe comptabilisé en créance.

**Implications pratiques**: Ne pas documenter cette couverture comme couverture d’investissement net pour une simple créance de dividende intragroupe.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets
 - 10
    >applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency

### 4. Dérivé à la juste valeur par résultat
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Si la créance de dividende intragroupe n’est pas éligible comme élément couvert en consolidation, ou si vous ne documentez pas une relation de couverture qualifiante, le dérivé reste comptabilisé selon le modèle général IFRS 9. Ses variations de juste valeur iront alors en résultat.

**Implications pratiques**: C’est le traitement par défaut si la couverture comptable ne peut pas être appliquée au niveau consolidé.

**Référence**:
 - 5.7.1
    >A gain or loss on a financial asset or financial liability that is measured at fair value shall be recognised in profit or loss
 - 4.2.1(a)
    >financial liabilities at fair value through profit or loss ... including derivatives that are liabilities