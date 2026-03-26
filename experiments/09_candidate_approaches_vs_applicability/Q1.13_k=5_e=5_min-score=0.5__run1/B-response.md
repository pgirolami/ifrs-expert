{
  "assumptions_fr": [
    "La créance correspond à un poste monétaire intragroupe libellé dans une devise autre que la monnaie fonctionnelle d’au moins l’une des entités du groupe concernées.",
    "La réponse est limitée aux modèles de comptabilité de couverture traités dans les extraits IFRS 9 et IFRIC 16 fournis."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, si la créance de dividende est un poste monétaire intragroupe dont le risque de change génère des écarts non totalement éliminés en consolidation. Dans ce cas, la couverture de juste valeur est le modèle le plus direct; la couverture de flux de trésorerie n’est envisageable que si la documentation vise la variabilité du règlement en monnaie fonctionnelle."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, la créance de dividende intragroupe est déjà un actif comptabilisé. IFRS 9 admet par exception, en comptes consolidés, le risque de change d’un poste monétaire intragroupe comme élément couvert si les écarts de change ne sont pas totalement éliminés. Si cette condition est remplie, la désignation de la composante de change dans une relation documentée est compatible avec une couverture de juste valeur.",
      "conditions_fr": [
        "Le poste doit être un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation.",
        "La relation doit être structurée comme couverture de la variation de valeur de la créance déjà comptabilisée."
      ],
      "practical_implication_fr": "C’est l’option la plus naturelle pour une créance de dividende déjà reconnue au bilan.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
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
      "reasoning_fr": "Ce modèle n’est pertinent dans cette situation que si la relation documentée vise la variabilité du montant encaissé en monnaie fonctionnelle jusqu’au règlement de la créance. IFRS 9 permet une couverture de flux de trésorerie sur un actif comptabilisé, mais pour une créance de dividende déjà reconnue ce modèle est moins direct que la couverture de juste valeur. Il reste donc possible seulement si l’objectif de gestion couvert est bien le flux de règlement.",
      "conditions_fr": [
        "Le risque couvert doit être défini comme la variabilité du montant encaissé en monnaie fonctionnelle jusqu’au règlement.",
        "Le poste doit être un poste monétaire intragroupe dont les écarts de change affectent le résultat consolidé."
      ],
      "practical_implication_fr": "Possible, mais la documentation doit viser le flux de règlement et non seulement la réévaluation comptable de la créance.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation of the hedging relationship"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord que la créance de dividende est bien un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation.",
    "Documenter dès l’origine l’élément couvert, l’instrument de couverture, le risque de change visé et le ratio de couverture.",
    "Si le modèle retenu est la couverture de flux de trésorerie, expliciter dans la documentation que le risque couvert porte sur la variabilité du montant encaissé en monnaie fonctionnelle jusqu’au règlement."
  ]
}
