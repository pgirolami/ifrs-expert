# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>When a financial asset becomes credit-impaired after origination (i.e. moves to Stage 3 under IFRS 9), the manner of recognizing interest income changes. Initially, while the asset is performing (Stage 1 or 2), interest is calculated on the gross carrying amount using the effective interest rate (EIR) determined at origination.

However, once the asset is assessed as credit-impaired, IFRS 9 paragraph 5.4.1 (b) requires that interest income be recognized by applying the EIR (which I believe is not credit adjusted EIR because that bit specially applies to purchased or originated credit impaired financial assets) to the amortized cost of the asset that is, the gross carrying amount less the loss allowance (expected credit loss).

Also, another matter is the unwinding of the discount on the loss allowance as “unwinding of ECL” as interest income for credit impaired loans, which represents the time-value effect on expected recoveries. This unwinding is separate from any changes in the loss allowance due to revised expectations. The complexity for me lies in keeping these two movements distinct. I find it difficult to understand whether the unwinding of ECL is different from the increase or decrease in the total ECL allowance on the reporting date.

Another area of confusion is whether “unwinding of ECL” also applies to performing loans and how this interacts with the presentation of income “at net” when Stage 2 or Stage 3 interest recognition is applied. Because it is not clear to me from IFRS 9 paragraphs whether the interest income calculation methodology for credit impaired loans results in only presentation changes or not.

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`

## Hypothèses
   - L’actif financier entre dans le champ d’IFRS 9 pour les règles d’intérêts et de dépréciation.
   - Il s’agit d’un actif de dette auquel la méthode du taux d’intérêt effectif s’applique.
   - L’actif devient déprécié après l’origination; il n’est donc pas un actif acheté ou originaire déprécié (POCI).

## Recommandation

**OUI**

Oui. Dans votre cas, l’intérêt en Stage 3 se calcule sur le coût amorti avec le taux effectif d’origine, et non avec un taux crédit-ajusté réservé aux actifs POCI. L’« unwinding » vient de l’actualisation de l’ECL et doit être distingué des réestimations de l’ECL dues aux nouvelles attentes de recouvrement.

## Points Opérationnels

   - Pour un actif devenu déprécié après l’origination, ne remplacez pas le EIR d’origine par un taux crédit-ajusté; ce dernier vise les actifs POCI.
   - À la clôture, la variation totale d’ECL n’est pas unique: elle peut inclure l’effet temps d’actualisation et, séparément, la révision des cash flows attendus et des scénarios.
   - Même en Stage 1/2, l’ECL reste une valeur actuelle de cash shortfalls; en revanche, l’intérêt du prêt continue d’être reconnu sur la base brute tant que l’actif n’est pas crédit-déprécié.
   - Pour éviter la confusion, préparez un bridge distinct entre: intérêt selon EIR, effet de base nette en Stage 3, effet passage du temps sur la provision, et remeasurement de la provision.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Méthode du taux d’intérêt effectif | OUI | - (non spécifiées) |
| 2. Modèle des pertes de crédit attendues | OUI | - (non spécifiées) |

### 1. Méthode du taux d’intérêt effectif
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Oui, car vous décrivez un actif non POCI devenu déprécié après l’origination. Les extraits distinguent les actifs POCI, qui utilisent un taux crédit-ajusté, des autres actifs dépréciés, pour lesquels les flux attendus restent actualisés au taux effectif d’origine. Dans cette situation, le passage en Stage 3 change donc la base de calcul de l’intérêt vers le coût amorti; ce n’est pas un simple changement de présentation.

**Implications pratiques**: En Stage 3 post-origination, calculez l’intérêt avec le EIR d’origine sur la valeur brute diminuée de la provision; en Stage 1/2, l’intérêt reste sur la valeur brute.

**Référence**:
 - B5.5.33
    >discounted at the financial asset’s original effective interest rate
 - B5.5.45
    >Expected credit losses shall be discounted using the credit-adjusted effective interest rate

### 2. Modèle des pertes de crédit attendues
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Oui, car l’ECL est une estimation actualisée des cash shortfalls à la date de clôture. Dans votre cas, la variation totale de provision peut donc combiner un effet temps d’actualisation sur les recouvrements attendus et une réestimation séparée liée aux hypothèses de défaut, de recouvrement, de collatéral ou aux perspectives économiques. Le mécanisme d’actualisation existe aussi pour les actifs performants, mais sans faire passer l’intérêt en base nette avant le Stage 3.

**Implications pratiques**: Distinguez dans le roll-forward de provision l’effet passage du temps et les réestimations d’ECL; pour Stage 1/2, ne confondez pas cet effet avec un calcul d’intérêt net.

**Référence**:
 - B5.5.28
    >Expected credit losses are a probability-weighted estimate of credit losses
 - B5.5.44
    >Expected credit losses shall be discounted to the reporting date
 - B5.5.52
    >Estimates of changes in expected credit losses should reflect
