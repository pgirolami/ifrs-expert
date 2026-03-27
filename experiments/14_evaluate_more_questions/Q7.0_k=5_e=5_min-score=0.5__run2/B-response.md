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
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - Le contrat de change à terme est un dérivé au sens d’IFRS 9, non désigné dans une relation de couverture, et reste classé à la juste valeur par résultat jusqu’au 20/12/2025.
   - Le contrat est réglé physiquement à l’échéance; les devises remises et reçues sont comptabilisées à la date de règlement.
   - Les écritures de règlement ci-dessous supposent qu’à l’échéance la juste valeur est positive (actif dérivé); si elle devient négative, il faut inverser le sens du compte de dérivé.

## Recommandation

**OUI**

Oui. Dans cette situation, le traitement applicable est la juste valeur par résultat: il faut comptabiliser la dernière variation de juste valeur jusqu’au 20/12/2025 en résultat, puis enregistrer le règlement physique en soldant le dérivé. La comptabilité de couverture et la comptabilisation à la date de règlement ne changent pas cette conclusion sur ces faits.

## Points Opérationnels

   - Avant le règlement du 20/12/2025, comptabiliser la dernière revalorisation: Dr Actif dérivé / Cr Gain de juste valeur en résultat, ou l’inverse si la juste valeur finale a diminué depuis le dernier arrêté.
   - Au règlement physique si le dérivé est un actif à l’échéance: Dr Banque / devise reçue ; Cr Banque / devise livrée ; Cr Actif dérivé.
   - Si la juste valeur finale est négative au 20/12/2025, remplacer l’actif dérivé par un passif dérivé et inverser le sens de l’écriture de dérivé au règlement.
   - Si la juste valeur a été mise à jour juste avant le dénouement, le règlement ne crée pas un gain ou une perte distinct(e); il matérialise et solde la valeur déjà portée par le dérivé.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Juste valeur par résultat (FVTPL) | OUI | - (non spécifiées) |
| 2. Comptabilité de couverture | NON | - (non spécifiées) |
| 3. Comptabilisation à la date de règlement | NON | - (non spécifiées) |

### 1. Juste valeur par résultat (FVTPL)
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Oui. Le contrat est expressément hors comptabilité de couverture et classé FVTPL.
Dans cette situation, la dernière variation de juste valeur entre le dernier arrêté et le 20/12/2025 va en résultat, puis le règlement physique éteint le dérivé; aucun solde ne doit rester après règlement.

**Implications pratiques**: Passer la revalorisation finale en résultat, puis solder l’actif dérivé contre les devises échangées au dénouement.

**Référence**:
 - 5.7.1
    >A gain or loss on a financial asset or financial liability that is measured at fair value shall be recognised in profit or loss

### 2. Comptabilité de couverture
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Non. Les extraits IFRS 9 présentent la couverture comme une exception au schéma normal de juste valeur par résultat.
Or vous indiquez que le forward n’est pas désigné comme instrument de couverture; il n’y a donc ni OCI ni réserve de couverture à traiter à l’échéance.

**Implications pratiques**: Aucune écriture d’OCI ou de réserve de couverture n’est requise au 20/12/2025.

**Référence**:
 - 5.7.1
    >unless: (a) it is part of a hedging relationship
 - 5.7.3
    >hedged items in a hedging relationship shall be recognised in accordance with paragraphs 6.5.8–6.5.14

### 3. Comptabilisation à la date de règlement
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Non. Le paragraphe 5.7.4 vise le choix de reconnaissance entre date de transaction et date de règlement pour des actifs à recevoir.
Ici, la question porte sur le dénouement d’un dérivé déjà reconnu à la juste valeur par résultat; le traitement déterminant reste donc FVTPL, avec revalorisation finale puis règlement.

**Implications pratiques**: Cette approche ne pilote pas le schéma comptable final du forward sur les faits décrits.

**Référence**:
 - 5.7.4
    >If an entity recognises financial assets using settlement date accounting
