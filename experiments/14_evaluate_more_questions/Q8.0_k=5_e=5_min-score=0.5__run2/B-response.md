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
   - La question vise des actifs financiers de type dette relevant d’IFRS 9, pour lesquels un taux d’intérêt effectif est déterminé et les règles de dépréciation s’appliquent.
   - Les références aux Stages 1, 2 et 3 sont utilisées comme raccourci pour le modèle de pertes de crédit attendues d’IFRS 9.
   - L’actif concerné n’était pas crédit-déprécié à la comptabilisation initiale et ne relève donc pas, dans les faits décrits, de la catégorie des actifs achetés ou originés avec dépréciation de crédit.

## Recommandation

**OUI**

Dans cette situation, il faut combiner la méthode du TIE et le modèle ECL: l’intérêt d’un actif devenu crédit-déprécié après l’origine se comprend avec le TIE d’origine, tandis que la provision ECL reste une mesure actualisée distincte. L’« unwinding » de l’ECL est conceptuellement distinct d’une réestimation des recouvrements, et le traitement POCI au taux ajusté du crédit ne s’applique pas.

## Points Opérationnels

   - Pour Stages 1–2, l’intérêt reste calculé sur la base brute; l’existence d’une ECL actualisée n’implique pas à elle seule une présentation « nette » de l’intérêt.
   - Pour un actif non-POCI devenu crédit-déprécié, le changement de base de calcul de l’intérêt n’est pas qu’un reclassement de présentation: il modifie le montant d’intérêt reconnu par rapport à une base brute.
   - L’« unwinding » de l’ECL correspond au seul effet temps sur des cash shortfalls déjà estimés; il doit être distingué analytiquement d’une variation de provision causée par des hypothèses de recouvrement révisées.
   - La variation totale de la provision à la date de clôture peut donc combiner simultanément effet temps, changements de probabilités de défaut, changements de montants recouvrables et changements de calendrier des encaissements attendus.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Méthode du taux d’intérêt effectif | OUI | - (non spécifiées) |
| 2. Pertes de crédit attendues | OUI | - (non spécifiées) |
| 3. Taux effectif ajusté du crédit | NON | - (non spécifiées) |

### 1. Méthode du taux d’intérêt effectif
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Oui. La question porte directement sur la base de calcul de l’intérêt après dégradation du risque de crédit d’un actif déjà comptabilisé. Dans cette situation, la méthode du TIE est la base pertinente pour conserver le TIE d’origine et pour distinguer le calcul de l’intérêt de la réévaluation séparée de la perte de crédit attendue.

**Implications pratiques**: Pour un actif devenu crédit-déprécié après l’origine, ne remplacez pas le TIE d’origine par un taux ajusté du crédit; suivez séparément le calcul d’intérêt et la provision.

**Référence**:
 - B5.4.4
    >amortises any fees, points paid or received, transaction costs and other premiums or discounts
 - B5.4.6
    >discounted at the financial instrument’s original effective interest rate

### 2. Pertes de crédit attendues
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Oui. Votre difficulté sur l’« unwinding of ECL » relève du modèle ECL, car l’allocation est une valeur actuelle de cash shortfalls actualisée à la date de clôture. Dans cette situation, une part de la variation de la provision peut venir du seul passage du temps, distinctement d’une hausse ou baisse liée à des changements d’anticipations de défaut, de recouvrement ou de calendrier; ce mécanisme existe aussi pour les actifs performants, même si la base de calcul de l’intérêt ne devient pas nette en Stages 1–2.

**Implications pratiques**: Analysez la variation de la provision de clôture en deux blocs: effet temps sur une ECL actualisée et réestimation des flux/cash shortfalls attendus.

**Référence**:
 - B5.5.28
    >the present value of all cash shortfalls
 - B5.5.33
    >difference between the asset’s gross carrying amount and the present value of estimated future cash flows
 - B5.5.44
    >Expected credit losses shall be discounted to the reporting date

### 3. Taux effectif ajusté du crédit
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Non. Les faits décrits portent sur un actif qui devient crédit-déprécié après l’origination, alors que le taux effectif ajusté du crédit vise les actifs achetés ou originés déjà crédit-dépréciés à la comptabilisation initiale. Dans ce cas précis, il ne faut donc pas transposer le régime POCI au simple passage en Stage 3.

**Implications pratiques**: N’appliquez le taux ajusté du crédit que si l’actif était POCI dès l’origine; sinon, restez sur le TIE d’origine.

**Référence**:
 - B5.4.7
    >for financial assets that are considered to be purchased or originated credit-impaired at initial recognition
 - B5.4.7
    >does not mean that a credit-adjusted effective interest rate should be applied solely because the financial asset has high credit risk at initial recognition
 - B5.5.45
    >discounted using the credit-adjusted effective interest rate determined at initial recognition
