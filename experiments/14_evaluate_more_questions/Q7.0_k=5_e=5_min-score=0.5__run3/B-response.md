# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>I would appreciate your help with the accounting for a forward foreign exchange contract under IFRS 9.

Background:

We have a forward FX contract (not designated as a hedge) that is correctly classified at Fair Value Through Profit or Loss (FVTPL).

The contract started in June 2025.

We have been remeasuring it to fair value at each period-end, posting entries like the one below for June 2025:

30 June 2025:

Dr. Financial Asset - Derivative

Cr. Derivative Fair Value Gain (in P&L)

Situation:
The contract is scheduled to mature and be settled on 20 December 2025. I need to confirm the correct final journal entries on the settlement date.

My Question:
What are the specific journal entries to record the final fair value remeasurement and the physical settlement of the contract? Specifically, how do we derecognize the derivative asset and record the actual currency exchange?

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`

## Hypothèses
   - Le contrat à terme de change est un dérivé relevant d’IFRS 9 et n’a été désigné dans aucune relation de couverture à aucun moment.
   - Le règlement du 20 décembre 2025 est un règlement physique avec échange des deux devises, et non un règlement net en trésorerie.
   - La juste valeur du dérivé est mise à jour à la date de règlement avant sa sortie de bilan ; si la position finale est un passif plutôt qu’un actif, les sens débit/crédit s’inversent.

## Recommandation

**OUI**

Dans cette situation, seul le traitement à la juste valeur par résultat s’applique. Il faut enregistrer une dernière variation de juste valeur en résultat jusqu’au 20 décembre 2025, puis solder le dérivé lors du règlement physique, sans OCI ni réserve de couverture.

## Points Opérationnels

   - Au 20/12/2025, comptabiliser d’abord la dernière variation de juste valeur depuis la dernière clôture : si la juste valeur augmente, Dr actif dérivé / Cr gain de juste valeur en résultat ; si elle baisse, l’écriture est inverse.
   - Après cette réévaluation finale, le règlement physique sert à solder le dérivé : pour un dérivé actif, Dr compte de la devise reçue, Cr compte de la devise livrée, Cr actif dérivé ; pour un dérivé passif, débiter le passif dérivé à la place.
   - Si la juste valeur a bien été mise à jour à la date de règlement, il n’y a normalement pas de gain ou perte supplémentaire sur le dérivé au moment du règlement lui-même ; le résultat a déjà été capté par la dernière réévaluation.
   - Le contrat n’étant pas désigné en couverture, aucune part de la variation de valeur n’est comptabilisée en autres éléments du résultat global.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Juste valeur par résultat | OUI | - Le contrat reste hors relation de couverture désignée jusqu’au règlement. |
| 2. Comptabilité de couverture | NON | - (non spécifiées) |

### 1. Juste valeur par résultat
**Applicabilité**: OUI

**Conditions**:
   - Le contrat reste hors relation de couverture désignée jusqu’au règlement.

**Raisonnment**:
Le forward FX est décrit comme non désigné en couverture et correctement classé à la juste valeur par résultat. Dans ce cas, les variations de juste valeur continuent d’être comptabilisées en résultat jusqu’à la date de règlement.
Au 20 décembre 2025, vous passez d’abord la dernière réévaluation de juste valeur, puis vous sortez le dérivé du bilan lors du règlement physique. Si le dérivé est un actif à cette date, son solde crédite l’écriture de règlement.

**Implications pratiques**: Écriture type au 20/12/2025 : réévaluation finale en résultat, puis Dr devise reçue / Cr devise livrée / Cr actif dérivé ; si le dérivé est passif, débiter le passif dérivé à la place.

**Référence**:
 - 5.7.1
    >A gain or loss on a financial asset or financial liability that is measured at fair value shall be recognised in profit or loss
 - 5.7.4
    >For assets measured at fair value, however, the change in fair value shall be recognised in profit or loss

### 2. Comptabilité de couverture
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche ne s’applique pas ici, car les faits indiquent expressément que le forward n’est pas désigné comme instrument de couverture. Les mécanismes d’OCI et de reclassement propres aux couvertures ne sont donc pas pertinents.
La clôture du contrat doit être traitée comme le règlement d’un dérivé FVTPL ordinaire, et non comme la liquidation d’une relation de couverture documentée.

**Implications pratiques**: Aucune écriture en OCI ni reclassement de réserve de couverture ; tout reste en résultat jusqu’au règlement.

**Référence**:
 - 5.7.1
    >unless: (a) it is part of a hedging relationship
 - B6.5.36
    >at the date on which the forward contract is designated as a hedging instrument
