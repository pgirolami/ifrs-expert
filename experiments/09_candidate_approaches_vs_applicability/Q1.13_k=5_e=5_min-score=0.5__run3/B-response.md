{
  "assumptions_fr": [
    "On suppose que la créance de dividende intragroupe est un élément monétaire comptabilisé, libellé dans une monnaie différente de la monnaie fonctionnelle de l'entité concernée.",
    "On suppose que la question porte sur la comptabilité de couverture selon IFRS 9 dans les comptes consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, le risque de change d'un élément monétaire intragroupe peut être désigné comme élément couvert par exception, si les écarts de change ne sont pas entièrement éliminés en consolidation. Pour une créance de dividende déjà comptabilisée, le fair value hedge est le cadre le plus direct ; un cash flow hedge reste possible seulement si la relation vise la variabilité des flux de règlement."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende est supposée être un actif intragroupe monétaire déjà comptabilisé.\nIFRS 9 pose une exception en consolidation pour le risque de change d'un élément monétaire intragroupe, à condition que les écarts de change ne soient pas totalement éliminés ; ce profil correspond ensuite au modèle de fair value hedge d'un actif reconnu exposé à un risque particulier.",
      "conditions_fr": [
        "La créance intragroupe doit générer des écarts de change qui ne sont pas entièrement éliminés en consolidation, typiquement entre entités ayant des monnaies fonctionnelles différentes."
      ],
      "practical_implication_fr": "Documenter la créance comptabilisée comme élément couvert et limiter la désignation à sa composante de risque de change au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le contexte IFRS 9 autorise aussi un cash flow hedge pour un actif ou passif reconnu lorsque le risque particulier crée une variabilité de flux pouvant affecter le résultat.\nIci, cela n'est pertinent que si la relation documentée vise la variabilité des encaissements de règlement de la créance due au change ; l'exception intragroupe de 6.3.6 doit toujours être satisfaite en consolidation.",
      "conditions_fr": [
        "La relation doit viser la variabilité des flux de règlement futurs de la créance attribuable au risque de change.",
        "La créance intragroupe doit générer des écarts de change qui ne sont pas entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation doit cibler les flux d'encaissement futurs de la créance et leur impact en résultat consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point de départ est le timing : une fois le dividende décidé et la créance comptabilisée, l'analyse porte sur un élément monétaire reconnu.",
    "En consolidation, la contrainte décisive est l'existence d'un risque de change qui n'est pas totalement éliminé, ce qui vise les situations entre entités de monnaies fonctionnelles différentes.",
    "La documentation doit identifier la créance de dividende, la seule composante de risque de change couverte et le modèle retenu parmi les deux analysés."
  ]
}
