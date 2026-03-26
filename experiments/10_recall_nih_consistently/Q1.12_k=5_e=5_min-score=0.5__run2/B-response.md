{
  "assumptions_fr": [
    "La créance de dividende intragroupe crée une exposition au risque de change dans les états financiers consolidés.",
    "La question vise la qualification d'une relation de couverture au titre d'IFRS 9 au niveau consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous réserve que la créance de dividende soit un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas, une qualification formelle est envisageable via une fair value hedge ou une cash flow hedge, mais pas via une couverture d'investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance de dividende est déjà un actif reconnu. En consolidation, un élément intragroupe est en principe exclu, mais IFRS 9 prévoit une exception pour le risque de change d'un poste monétaire intragroupe si les écarts de change ne sont pas totalement éliminés. Dans cette situation, le modèle de couverture de juste valeur peut être formellement envisagé pour une créance reconnue exposée au change.",
      "conditions_fr": [
        "la créance de dividende doit constituer un poste monétaire intragroupe",
        "les écarts de change sur cette créance ne doivent pas être totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "La documentation de couverture doit être établie au niveau consolidé dès la désignation de la relation.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items"
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
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 vise aussi la variabilité des flux de trésorerie d'un actif reconnu. Si la créance de dividende intragroupe expose le groupe à une variabilité en monnaie fonctionnelle qui affecte le résultat consolidé, l'exception du paragraphe 6.3.6 permet une désignation formelle au niveau consolidé. Cette approche n'est donc recevable que si le risque de change subsiste après éliminations de consolidation.",
      "conditions_fr": [
        "la créance de dividende doit constituer un poste monétaire intragroupe",
        "le risque de change sur la créance doit affecter le résultat consolidé parce qu'il n'est pas totalement éliminé en consolidation"
      ],
      "practical_implication_fr": "La documentation doit cibler la variabilité de l'encaissement en devise de la créance reconnue.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "La question porte sur une créance de dividende intragroupe déjà comptabilisée, et non sur un montant de net assets d'une activité étrangère. IFRIC 16 réserve ce modèle aux couvertures d'investissements nets dans des opérations étrangères et précise qu'il ne doit pas être appliqué par analogie. Cette qualification ne correspond donc pas aux faits décrits.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter cette relation comme une couverture d'investissement net.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif en consolidation est l'exception du paragraphe 6.3.6 : sans exposition de change résiduelle au niveau consolidé, la couverture ne peut pas être qualifiée.",
    "La présence d'une créance de dividende déjà comptabilisée oriente l'analyse vers une couverture d'un poste reconnu, et non vers une couverture d'investissement net.",
    "La qualification formelle suppose une désignation et une documentation à l'origine de la relation de couverture, avec identification du risque de change couvert et de la méthode d'appréciation de l'efficacité."
  ]
}
