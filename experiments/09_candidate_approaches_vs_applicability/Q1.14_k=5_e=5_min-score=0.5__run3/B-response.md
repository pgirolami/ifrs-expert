{
  "assumptions_fr": [
    "La question est analysée au niveau des états financiers consolidés selon IFRS 9.",
    "La créance de dividende intragroupe est libellée dans une devise générant une exposition de change pour au moins une entité du groupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, à condition que la créance intragroupe constitue un item monétaire dont les écarts de change ne soient pas entièrement éliminés en consolidation. Dans ce cas, le modèle pertinent est la couverture de juste valeur; la couverture de flux de trésorerie n’est pas adaptée aux faits décrits."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe a déjà donné naissance à une créance comptabilisée au sein du groupe, donc à un item monétaire intragroupe.\nLa règle générale exclut les éléments intragroupe en consolidation, mais IFRS 9 prévoit une exception expresse pour le risque de change d’un item monétaire intragroupe si les écarts de change ne sont pas totalement éliminés en consolidation.\nCette exposition correspond, dans ces faits, à une couverture de juste valeur d’une créance reconnue.",
      "conditions_fr": [
        "La créance/dette de dividende intragroupe génère des écarts de change non intégralement éliminés en consolidation, typiquement entre entités à monnaies fonctionnelles différentes."
      ],
      "practical_implication_fr": "Si cette condition est remplie, la documentation doit viser une couverture de juste valeur du risque de change de la créance intragroupe.",
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
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Dans les faits décrits, l’exposition ne porte pas sur une transaction intragroupe encore future mais sur une créance de dividende déjà comptabilisée.\nLe contexte fourni rattache l’exception intragroupe pour les cash flow hedges aux transactions intragroupe prévisionnelles hautement probables qui affecteront le résultat consolidé.\nIci, le sujet est la réévaluation de l’item monétaire existant, pas une variabilité de flux futurs à documenter comme telle.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette exposition ne devrait pas être documentée, dans ces circonstances, comme une couverture de flux de trésorerie.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "B6.3.5",
          "excerpt": "If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify as a hedged item."
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord que la créance et la dette de dividende intragroupe sont des items monétaires entre entités à monnaies fonctionnelles différentes et que l’écart de change subsiste en consolidation.",
    "La désignation doit être faite à l’origine de la relation de couverture avec une documentation formelle identifiant l’instrument, l’élément couvert, le risque de change et le hedge ratio.",
    "Si l’exposition de change est entièrement éliminée en consolidation, aucune couverture documentée en consolidation n’est possible pour cette créance intragroupe."
  ]
}
