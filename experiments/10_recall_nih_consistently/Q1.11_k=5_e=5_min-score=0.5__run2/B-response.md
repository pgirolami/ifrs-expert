{
  "assumptions_fr": [
    "La créance de dividende est un poste monétaire intragroupe libellé dans une devise différente de la monnaie fonctionnelle pertinente.",
    "La question vise les états financiers consolidés."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Dans les comptes consolidés, le risque de change d’un poste monétaire intragroupe peut être désigné comme élément couvert lorsqu’il crée des écarts de change non totalement éliminés en consolidation. Pour une créance de dividende déjà comptabilisée, la couverture de juste valeur est l’approche la plus directement alignée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Ici, la créance de dividende intragroupe est déjà comptabilisée : il s’agit donc d’un actif reconnu. Le contexte prévoit explicitement qu’en consolidation le risque de change d’un poste monétaire intragroupe peut être un élément couvert s’il génère des écarts de change non totalement éliminés, ce qui correspond directement à une couverture de juste valeur d’un actif reconnu exposé au change.",
      "conditions_fr": [
        "Le poste doit être un poste monétaire intragroupe dont le risque de change génère des écarts non totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation peut viser la créance de dividende enregistrée comme élément couvert, avec désignation formelle du risque de change et du ratio de couverture dès l’inception.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le texte permet une cash flow hedge d’un actif ou passif reconnu lorsqu’il existe une variabilité de flux attribuable à un risque particulier. Dans cette situation, cette approche n’est recevable que si la relation est documentée comme une couverture de la variabilité des encaissements futurs en monnaie fonctionnelle sur la créance de dividende, et si ce risque affecte le résultat consolidé.",
      "conditions_fr": [
        "La documentation doit viser la variabilité des flux d’encaissement futurs de la créance de dividende enregistrée, et non simplement sa valeur comptable.",
        "Le risque de change couvert doit affecter le résultat consolidé."
      ],
      "practical_implication_fr": "Possible, mais la documentation doit être construite sur les flux futurs de règlement de la créance et non sur la seule réévaluation du poste reconnu.",
      "references": [
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net",
      "applicability": "non",
      "reasoning_fr": "Un dividende intragroupe comptabilisé crée une créance monétaire entre entités du groupe ; ce n’est pas un montant de net assets d’une activité à l’étranger. Le modèle de couverture d’un investissement net vise le risque de change sur l’investissement net dans l’activité étrangère, pas sur une créance intercompany de dividende déjà reconnue.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter cette exposition comme une couverture d’investissement net ; elle relève d’un poste monétaire intragroupe distinct.",
      "references": [
        {
          "section": "2",
          "excerpt": "the hedged item ... may be an amount of net assets"
        },
        {
          "section": "10",
          "excerpt": "only ... the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        },
        {
          "section": "14",
          "excerpt": "may be designated as a hedging instrument in a hedge of a net investment in a foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier et documenter que la créance/dividende intragroupe est un poste monétaire dont les écarts de change ne sont pas totalement éliminés en consolidation.",
    "Formaliser la désignation et la documentation à l’inception de la relation de couverture, avec identification de l’instrument, de la créance couverte, du risque de change et du hedge ratio.",
    "En pratique, pour une créance de dividende déjà enregistrée, la qualification la plus robuste dans cette situation est la couverture de juste valeur ; la couverture de flux n’est défendable que si l’objet couvert est bien la variabilité des encaissements futurs."
  ]
}
