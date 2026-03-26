{
  "assumptions_fr": [
    "L’analyse porte sur les états financiers consolidés du groupe.",
    "La créance de dividendes est un poste monétaire intragroupe comptabilisé entre entités ayant des monnaies fonctionnelles différentes, et les écarts de change correspondants ne sont pas entièrement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, un élément intragroupe est en principe exclu, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe non entièrement éliminé. Dans cette situation, la créance de dividendes peut être désignée comme élément couvert, sous réserve du choix du modèle de couverture retenu et du respect des critères de désignation, documentation et efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La règle générale exclut les éléments intragroupe en consolidation, mais IFRS 9 ouvre une exception pour le risque de change d’un poste monétaire intragroupe.\nSelon les hypothèses, la créance de dividendes est un receivable intragroupe comptabilisé dont les écarts de change ne sont pas entièrement éliminés.\nComme il s’agit d’un actif comptabilisé exposé à une variation de valeur liée au change affectant le résultat, ce traitement peut s’appliquer ici, sous réserve des critères de qualification de la relation de couverture.",
      "conditions_fr": [
        "Les écarts de change sur la créance ne sont pas entièrement éliminés en consolidation.",
        "Le risque couvert est le risque de change affectant le résultat consolidé.",
        "La relation de couverture est formellement désignée et documentée à l’origine.",
        "La relation satisfait aux critères d’efficacité d’IFRS 9."
      ],
      "practical_implication_fr": "La créance peut être traitée comme élément couvert en juste valeur pour son risque de change dans les comptes consolidés, avec suivi de l’inefficacité selon IFRS 9.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk and could affect profit or loss."
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La même exception d’IFRS 9 rend éligible en consolidation le risque de change d’un poste monétaire intragroupe, dans les faits supposés.\nIci, la créance de dividendes est un actif comptabilisé dont le montant encaissé en monnaie fonctionnelle varie avec le change et peut affecter le résultat consolidé.\nLe traitement en cash flow hedge peut donc être retenu dans cette situation, à condition que la désignation et l’efficacité de la couverture soient dûment établies.",
      "conditions_fr": [
        "Les écarts de change sur la créance affectent le résultat consolidé.",
        "La créance est bien le poste monétaire intragroupe couvert pour son risque de change.",
        "La relation de couverture est formellement désignée et documentée à l’origine.",
        "La relation satisfait aux critères d’efficacité d’IFRS 9."
      ],
      "practical_implication_fr": "Si ce modèle est retenu, la part efficace suit le mécanisme de cash flow hedge avec comptabilisation en OCI puis reclassement selon IFRS 9.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability ... and could affect profit or loss."
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        },
        {
          "section": "6.5.12",
          "excerpt": "if the hedged future cash flows are still expected to occur, that amount shall remain in the cash flow hedge reserve until the future cash flows occur"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter dès l’origine l’instrument de couverture, l’élément couvert, le risque de change visé et la méthode d’évaluation de l’efficacité.",
    "Démontrer en consolidation que les écarts de change liés à la créance de dividendes ne sont pas entièrement éliminés.",
    "Choisir le modèle de couverture cohérent avec le risque effectivement géré sur la créance: variation de valeur ou variabilité des flux.",
    "Vérifier que le hedge ratio retenu reflète la gestion réelle du risque et ne crée pas un déséquilibre artificiel."
  ]
}
