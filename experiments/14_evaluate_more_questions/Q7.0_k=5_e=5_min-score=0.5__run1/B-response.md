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
   - Le contrat reste non désigné comme instrument de couverture jusqu'au 20 décembre 2025.
   - Le règlement du 20 décembre 2025 est un règlement physique des deux devises; si la juste valeur finale est négative, les sens des écritures sur le dérivé sont inversés.

## Recommandation

**OUI**

Dans cette situation, le traitement applicable est celui du dérivé à la juste valeur par résultat. Il faut d'abord comptabiliser la dernière variation de juste valeur au 20 décembre 2025, puis solder l'actif ou le passif dérivé lors du règlement physique, sans OCI ni comptabilité de couverture.

## Points Opérationnels

   - Écriture de remeasurement finale au 20 décembre 2025 si la juste valeur a encore augmenté: Dr Actif dérivé / Cr Gain de juste valeur sur dérivé (résultat). Si elle a diminué, écriture inverse; si la juste valeur devient négative, constater un passif dérivé.
   - Après cette dernière remeasurement, le règlement physique ne crée pas un nouveau résultat distinct du dérivé, sauf la variation de juste valeur entre le dernier arrêté et le 20 décembre 2025.
   - Écriture de règlement physique, cas d'un dérivé en actif à l'échéance: Dr Banque - devise reçue ; Cr Banque - devise livrée ; Cr Actif dérivé. Le crédit du dérivé sert à le décomptabiliser intégralement.
   - Si le dérivé est en passif à l'échéance, logique inverse sur le dérivé: Dr Passif dérivé au règlement, avec constatation des flux de devise reçue et livrée.
   - Le point clé est qu'après le règlement du 20 décembre 2025, le solde du dérivé doit être nul.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Juste valeur par résultat | OUI | - (non spécifiées) |
| 2. Comptabilité de couverture | NON | - (non spécifiées) |

### 1. Juste valeur par résultat
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Vous indiquez que le forward FX n'est pas désigné comme couverture et qu'il est correctement classé à la juste valeur par résultat. Dans ce cas, les variations de juste valeur jusqu'à la date de règlement restent comptabilisées en résultat. Le règlement final sert ensuite à éteindre le dérivé et à enregistrer l'échange effectif des devises.

**Implications pratiques**: Au 20 décembre 2025: remeasurement final en résultat, puis extinction du dérivé et comptabilisation de la devise reçue/de la devise livrée.

**Référence**:
 - 5.7.1
    >A gain or loss on a financial asset or financial liability that is measured at fair value shall be recognised in profit or loss
 - 5.7.4
    >For assets measured at fair value, however, the change in fair value shall be recognised in profit or loss or in other comprehensive income

### 2. Comptabilité de couverture
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche ne s'applique pas ici, car le contrat n'est pas désigné comme instrument de couverture. Les mécanismes d'OCI et de test d'efficacité cités dans le contexte visent une relation de couverture documentée. Les écritures finales restent donc en juste valeur par résultat.

**Implications pratiques**: Aucun passage en OCI ni reclassement de réserve de couverture n'est à enregistrer au règlement.

**Référence**:
 - 5.7.1
    >unless: (a) it is part of a hedging relationship
 - 3
    >the gain or loss on the hedging instrument that is determined to be an effective hedge ... is recognised in other comprehensive income
