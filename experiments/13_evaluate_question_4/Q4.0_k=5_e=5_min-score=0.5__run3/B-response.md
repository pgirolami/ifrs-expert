# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>I'm diving into IFRS 9 classification of financial assets, specifically debt instruments held by banks in securitisations that the bank retains or invests in.
Even though most tranches (especially mezzanine and junior/equity) are likely to fail the SPPI test, do we still have to perform the SPPI test every time? Or is there any implicit exemption for contractually linked instruments (CLIs)?

**Documentation consultée**
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - Les instruments visés sont des actifs financiers entrant dans le champ d’IFRS 9.
   - La question porte sur le classement ultérieur de tranches de titrisation détenues ou conservées par une banque.
   - Aucune tranche précise n’est décrite; la réponse vise donc l’existence d’une dispense implicite, et non le classement définitif d’un instrument identifié.

## Recommandation

**OUI**

Oui, l’analyse SPPI reste nécessaire pour les instruments contractuellement liés; IFRS 9 ne prévoit aucune exemption implicite pour les CLIs. Si les conditions CLI ne sont pas démontrées à l’origine, la tranche ne peut pas être classée au coût amorti ni en FVOCI et relève de la FVPL.

## Points Opérationnels

   - Le point clé est l’analyse à la comptabilisation initiale de chaque tranche; l’impossibilité d’évaluer à cette date conduit à la FVPL.
   - Pour un CLI, il faut remonter jusqu’au pool d’instruments qui crée les flux et vérifier les conditions de B4.1.21 à B4.1.24.
   - L’absence de dispense implicite signifie qu’une intuition de non-SPPI ne remplace pas l’analyse et la documentation formelles.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - La tranche satisfait aux conditions CLI de B4.1.21 après analyse du pool sous-jacent.<br>- La banque la détient dans un modèle de collecte des flux contractuels. |
| 2. Juste valeur par OCI | OUI SOUS CONDITIONS | - La tranche satisfait aux conditions CLI de B4.1.21 après look-through sur le pool.<br>- La banque la gère dans un modèle de collecte des flux contractuels et de vente. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La tranche ne satisfait pas aux conditions CLI de B4.1.21, ou la banque ne peut pas les évaluer à la comptabilisation initiale.<br>- Le pool sous-jacent peut changer de sorte qu’il peut ne plus satisfaire B4.1.23 à B4.1.24. |

### 1. Coût amorti
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La tranche satisfait aux conditions CLI de B4.1.21 après analyse du pool sous-jacent.
   - La banque la détient dans un modèle de collecte des flux contractuels.

**Raisonnment**:
Dans cette situation de tranches de titrisation détenues par une banque, le coût amorti n’est possible qu’après l’analyse spécifique des instruments contractuellement liés; il n’existe pas d’exemption implicite. La banque doit établir que la tranche satisfait aux conditions CLI par examen du pool sous-jacent, puis qu’elle est gérée pour collecter les flux contractuels.

**Implications pratiques**: Pas de coût amorti sans analyse documentée de la tranche et du pool sous-jacent dès l’origine.

**Référence**:
 - 4.1.2
    >measured at amortised cost if both of the following conditions are met
 - B4.1.21
    >a tranche has cash flow characteristics that are payments of principal and interest

### 2. Juste valeur par OCI
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La tranche satisfait aux conditions CLI de B4.1.21 après look-through sur le pool.
   - La banque la gère dans un modèle de collecte des flux contractuels et de vente.

**Raisonnment**:
Pour ces tranches de titrisation, la FVOCI n’est possible que si la tranche passe aussi l’analyse CLI/SPPI; le régime CLI ne dispense donc pas du test. En plus, le portefeuille doit être géré dans un modèle qui combine collecte des flux contractuels et ventes.

**Implications pratiques**: La documentation doit couvrir à la fois l’analyse CLI du pool et le modèle économique de collecte et vente.

**Référence**:
 - 4.1.2A
    >measured at fair value through other comprehensive income if both of the following conditions are met
 - B4.1.22
    >must look through until it can identify the underlying pool of instruments

### 3. Juste valeur par résultat
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La tranche ne satisfait pas aux conditions CLI de B4.1.21, ou la banque ne peut pas les évaluer à la comptabilisation initiale.
   - Le pool sous-jacent peut changer de sorte qu’il peut ne plus satisfaire B4.1.23 à B4.1.24.

**Raisonnment**:
Dans une titrisation conservée ou acquise, la FVPL s’applique si la banque ne peut pas démontrer les conditions CLI à la comptabilisation initiale ou si elles ne sont pas remplies. IFRS 9 prévoit explicitement cette issue pour les tranches, ce qui confirme l’absence d’exemption implicite.

**Implications pratiques**: À défaut d’une démonstration positive à l’origine, la tranche doit être classée en FVPL.

**Référence**:
 - 4.1.4
    >A financial asset shall be measured at fair value through profit or loss unless
 - B4.1.26
    >If the holder cannot assess the conditions in paragraph B4.1.21 at initial recognition, the tranche must be measured at fair value through profit or loss.
