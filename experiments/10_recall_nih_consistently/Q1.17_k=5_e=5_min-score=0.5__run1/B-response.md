{
  "assumptions_fr": [
    "La question est analysée au niveau des états financiers consolidés.",
    "La créance de dividende intragroupe est libellée dans une devise étrangère."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, la seule composante de change d’une créance de dividende intragroupe peut être désignée comme élément couvert si cette créance est un élément monétaire dont le risque de change n’est pas totalement éliminé et affecte le résultat consolidé. La qualification comme couverture d’investissement net ne convient pas à ce fait."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe a déjà été comptabilisé à recevoir : il s’agit donc d’un actif reconnu. En consolidation, la règle générale exclut les postes intragroupe, mais l’exception vise le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. Dans ce cas, une couverture de juste valeur de la seule composante change est cohérente avec le fait couvert.",
      "conditions_fr": [
        "la créance de dividende intragroupe est un élément monétaire",
        "les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé"
      ],
      "practical_implication_fr": "Documenter la créance de dividende comme élément couvert et mesurer en résultat consolidé l’inefficacité de la couverture.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
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
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende reste exposée jusqu’au règlement à une variabilité de sa contre-valeur en monnaie fonctionnelle liée au change. Le texte permet une couverture de flux de trésorerie pour un actif reconnu associé à un risque particulier, sous réserve de l’exception intragroupe en consolidation. Cette voie n’est donc possible que si l’objectif documenté est bien de couvrir la variabilité des flux en résultat consolidé jusqu’au paiement.",
      "conditions_fr": [
        "les écarts de change sur la créance intragroupe affectent le résultat consolidé",
        "l’objectif de gestion documenté porte sur la variabilité des flux en monnaie fonctionnelle jusqu’au règlement du dividende"
      ],
      "practical_implication_fr": "La documentation doit viser la variabilité des flux en monnaie fonctionnelle jusqu’au paiement du dividende.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Le fait visé est une créance de dividende intragroupe comptabilisée à recevoir, pas un investissement net dans une activité étrangère. L’IFRIC 16 limite ce modèle aux couvertures du risque de change sur un investissement net dans une activité étrangère. Ce traitement ne correspond donc pas à la situation décrite.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter cette relation comme une couverture d’investissement net.",
      "references": [
        {
          "section": "6.5.2(c)",
          "excerpt": "hedge of a net investment in a foreign operation"
        },
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "10",
          "excerpt": "only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "risk_component_designation",
      "label_fr": "Désignation d’une composante de risque",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La question porte précisément sur la seule composante de change. Le texte autorise la désignation d’un risque spécifique comme élément couvert, à condition qu’il soit séparément identifiable et mesurable de façon fiable. Pour une créance de dividende intragroupe en devise, la composante change peut donc être isolée, mais seulement si l’exception intragroupe en consolidation est satisfaite.",
      "conditions_fr": [
        "la composante de change de la créance est séparément identifiable",
        "la composante de change est mesurable de façon fiable",
        "la créance remplit en consolidation les conditions de l’exception prévue pour les éléments monétaires intragroupe"
      ],
      "practical_implication_fr": "La désignation doit isoler explicitement la seule composante change de la créance de dividende.",
      "references": [
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "B6.3.8",
          "excerpt": "a risk component must be a separately identifiable component ... and ... reliably measurable"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier que la créance et la dette de dividende sont des éléments monétaires entre entités ayant des monnaies fonctionnelles différentes.",
    "Démontrer que l’écart de change n’est pas totalement éliminé en consolidation et qu’il affecte bien le résultat consolidé.",
    "Choisir un seul modèle de couverture cohérent avec l’objectif de gestion documenté : juste valeur ou, si pertinent, flux de trésorerie.",
    "Documenter dès l’origine la seule composante de change couverte, le ratio de couverture et les sources attendues d’inefficacité."
  ]
}
