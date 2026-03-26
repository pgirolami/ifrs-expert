{
  "assumptions_fr": [
    "La créance de dividende intragroupe est libellée dans une devise différente de la monnaie fonctionnelle d’au moins une des entités concernées.",
    "Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en comptes consolidés, mais seulement si la créance de dividende constitue un poste monétaire intragroupe dont le risque de change subsiste en résultat consolidé. Dans cette situation, le modèle pertinent est le fair value hedge; le cash flow hedge n’est pas adapté à une créance déjà comptabilisée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "En consolidation, les éléments intragroupe sont en principe exclus comme éléments couverts, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés.\nIci, la question vise une créance de dividende déjà comptabilisée; si cette créance est bien le poste monétaire visé et que ses écarts de change affectent le résultat consolidé, la logique de fair value hedge correspond à un actif reconnu exposé au change.",
      "conditions_fr": [
        "La créance de dividende est un poste monétaire intragroupe.",
        "Les entités concernées ont des monnaies fonctionnelles différentes.",
        "Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé."
      ],
      "practical_implication_fr": "La documentation de couverture doit être portée au niveau consolidé et limitée au seul risque de change de la créance comptabilisée.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "La situation décrite ne porte pas sur une transaction intragroupe future hautement probable, mais sur une créance de dividende déjà comptabilisée.\nDans ce cas, l’exposition identifiée est la réévaluation au change d’un poste reconnu, pas une variabilité de flux futurs telle que visée par le cash flow hedge dans les extraits fournis; l’exception intragroupe citée pour les flux vise surtout les transactions prévisionnelles affectant le résultat consolidé.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter cette créance de dividende déjà enregistrée comme cash flow hedge dans les comptes consolidés.",
      "references": [
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "B6.3.5",
          "excerpt": "If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify as a hedged item."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier et documenter que la créance de dividende est bien un poste monétaire intragroupe en devise.",
    "Démontrer au niveau consolidé que les écarts de change correspondants ne sont pas totalement éliminés et passent en résultat consolidé.",
    "Si ces conditions sont remplies, documenter la relation comme fair value hedge dès la désignation, en identifiant précisément le poste couvert, le risque de change et l’instrument de couverture.",
    "Ne pas utiliser un cash flow hedge pour cette créance déjà comptabilisée; ce modèle viserait plutôt une transaction future hautement probable."
  ]
}
