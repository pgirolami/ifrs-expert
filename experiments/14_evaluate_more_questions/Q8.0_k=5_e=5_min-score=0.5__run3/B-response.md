# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>When a financial asset becomes credit-impaired after origination (i.e. moves to Stage 3 under IFRS 9), the manner of recognizing interest income changes. Initially, while the asset is performing (Stage 1 or 2), interest is calculated on the gross carrying amount using the effective interest rate (EIR) determined at origination.

However, once the asset is assessed as credit-impaired, IFRS 9 paragraph 5.4.1 (b) requires that interest income be recognized by applying the EIR (which I believe is not credit adjusted EIR because that bit specially applies to purchased or originated credit impaired financial assets) to the amortized cost of the asset that is, the gross carrying amount less the loss allowance (expected credit loss).

Also, another matter is the unwinding of the discount on the loss allowance as “unwinding of ECL” as interest income for credit impaired loans, which represents the time-value effect on expected recoveries. This unwinding is separate from any changes in the loss allowance due to revised expectations. The complexity for me lies in keeping these two movements distinct. I find it difficult to understand whether the unwinding of ECL is different from the increase or decrease in the total ECL allowance on the reporting date.

Another area of confusion is whether “unwinding of ECL” also applies to performing loans and how this interacts with the presentation of income “at net” when Stage 2 or Stage 3 interest recognition is applied. Because it is not clear to me from IFRS 9 paragraphs whether the interest income calculation methodology for credit impaired loans results in only presentation changes or not.

**Documentation consultée**
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - La question vise un actif financier relevant à la fois des règles IFRS 9 sur le taux d’intérêt effectif et du modèle IFRS 9 de pertes de crédit attendues.
   - L’actif n’était pas déprécié lors de la comptabilisation initiale puis est devenu déprécié ultérieurement (passage en Stage 3).

## Recommandation

**OUI SOUS CONDITIONS**

Oui, pour un actif devenu déprécié après l’origination et non POCI, les deux traitements s’appliquent ensemble : intérêts selon le taux effectif sur la base nette en Stage 3 et perte attendue mesurée comme valeur actualisée des insuffisances de trésorerie. L’« unwinding » est une composante de la variation de l’ECL liée au temps, distincte analytiquement d’une réestimation des recouvrements.

## Points Opérationnels

   - En Stage 1/2, selon les faits posés, l’intérêt reste calculé sur le montant brut; seul le Stage 3 fait basculer la base d’intérêt vers le montant net.
   - À chaque clôture, séparer analytiquement deux moteurs de variation de la provision: effet temps lié à l’actualisation et réestimation des cash flows/probabilités de recouvrement.
   - Les extraits fournis montrent une mécanique de provision actualisée; ils ne montrent pas une obligation distincte de présenter l’« unwinding » comme un modèle autonome séparé de la variation totale de l’ECL.
   - Ne pas utiliser le taux effectif ajusté du crédit pour un actif simplement devenu déprécié après l’origination; les extraits le rattachent aux actifs achetés ou émis comme dépréciés à l’origine.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Méthode du taux d’intérêt effectif | OUI SOUS CONDITIONS | - L’actif n’était pas acheté ou émis comme déprécié à l’origine (non-POCI). |
| 2. Modèle des pertes de crédit attendues | OUI | - (non spécifiées) |

### 1. Méthode du taux d’intérêt effectif
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif n’était pas acheté ou émis comme déprécié à l’origine (non-POCI).

**Raisonnment**:
Dans votre situation, la question porte directement sur la base de calcul des intérêts avant et après le passage en Stage 3. Le contexte confirme l’usage du taux d’intérêt effectif d’origine et montre que le taux effectif ajusté du crédit vise les actifs achetés ou émis comme dépréciés à l’origine; ainsi, pour un actif devenu déprécié après l’origination, votre lecture est cohérente sous cette limite.

**Implications pratiques**: Le passage en Stage 3 change la base de calcul des intérêts de la base brute à la base nette; ce n’est donc pas une simple question de présentation.

**Référence**:
 - B5.4.6
    >discounted at the financial instrument’s original effective interest rate
 - B5.4.7
    >this does not mean that a credit-adjusted effective interest rate should be applied solely because the financial asset has high credit risk at initial recognition.

### 2. Modèle des pertes de crédit attendues
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans votre situation, la provision ECL doit être comprise comme une valeur actualisée des cash shortfalls à chaque date de clôture. Dès lors, une part de la variation de la provision peut provenir du seul passage du temps jusqu’à la date de reporting (« unwinding »), tandis qu’une autre part provient d’un changement d’hypothèses de recouvrement, de calendrier ou de probabilités; ces deux effets ne sont donc pas la même chose, même s’ils aboutissent tous deux à une variation de la provision totale.

**Implications pratiques**: L’« unwinding » n’est pas réservé au Stage 3: l’ECL étant actualisée à la date de clôture, un effet temps peut exister aussi sur des actifs performants, sans changer pour autant la base d’intérêt en Stage 1/2.

**Référence**:
 - B5.5.28
    >the present value of all cash shortfalls
 - B5.5.44
    >Expected credit losses shall be discounted to the reporting date
 - B5.5.33
    >measure the expected credit losses as the difference between the asset’s gross carrying amount and the present value of estimated future cash flows discounted at the financial asset’s original effective interest rate.
