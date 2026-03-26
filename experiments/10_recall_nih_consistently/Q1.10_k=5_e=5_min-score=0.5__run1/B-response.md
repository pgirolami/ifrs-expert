{
  "assumptions_fr": [
    "L’analyse est menée au regard d’IFRS 9 dans des états financiers consolidés.",
    "La créance de dividende intragroupe crée bien une exposition de change au sein du groupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, une créance de dividende intragroupe peut être couverte au titre du risque de change si elle constitue un élément monétaire intragroupe dont les écarts de change ne sont pas entièrement éliminés et affectent le résultat consolidé. La couverture d’investissement net n’est pas adaptée à cette créance."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le dividende intragroupe déjà comptabilisé à recevoir est, dans cette situation, un actif reconnu; il entre donc dans le champ d’une couverture de juste valeur.\nEn consolidation, cette voie n’est recevable que si la créance est un élément monétaire intragroupe dont les écarts de change ne sont pas entièrement éliminés et affectent le résultat consolidé.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe.",
        "Les écarts de change sur cette créance ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé."
      ],
      "practical_implication_fr": "La documentation doit viser la créance de dividende reconnue et le risque de change subsistant au niveau consolidé.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
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
      "reasoning_fr": "Le texte fourni admet une couverture de flux de trésorerie pour un actif reconnu, ce qui peut viser une créance de dividende déjà comptabilisée.\nDans cette situation, l’applicabilité reste conditionnée au fait que la créance intragroupe relève de l’exception sur les éléments monétaires intragroupe et que le risque de change affecte le résultat consolidé.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe.",
        "Les écarts de change sur cette créance ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé."
      ],
      "practical_implication_fr": "La documentation doit cibler la variabilité des flux en devise de la créance et son effet au niveau du résultat consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net dans une activité étrangère",
      "applicability": "non",
      "reasoning_fr": "Une créance de dividende intragroupe à recevoir n’est pas un montant de net assets d’une activité étrangère; c’est un poste de règlement intragroupe.\nLe modèle de couverture d’un investissement net vise exclusivement le risque de change sur un investissement net dans une activité étrangère incluse dans les comptes consolidés.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter cette créance de dividende comme une couverture d’investissement net.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Établir la documentation formelle dès l’inception et identifier l’instrument de couverture, la créance de dividende, le risque de change et le hedge ratio.",
    "Démontrer au niveau consolidé que la créance de dividende est un élément monétaire intragroupe et que les écarts de change ne sont pas entièrement éliminés.",
    "Vérifier que le risque de change sur cette créance affecte bien le résultat consolidé; sinon l’exception intragroupe ne tient pas.",
    "Si le dividende n’est pas encore comptabilisé à recevoir, il faut réexaminer l’analyse comme transaction intragroupe hautement probable et non comme créance reconnue."
  ]
}
