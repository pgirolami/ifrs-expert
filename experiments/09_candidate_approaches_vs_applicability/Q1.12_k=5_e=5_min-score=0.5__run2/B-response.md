{
  "assumptions_fr": [
    "La question porte sur la comptabilité de couverture au niveau des états financiers consolidés selon IFRS 9.",
    "La créance de dividende intragroupe est libellée dans une devise générant une exposition de change au sein du groupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, au niveau consolidé, si la créance de dividende constitue un poste monétaire intragroupe en devise dont les écarts de change ne sont pas totalement éliminés en consolidation. Les deux modèles identifiés peuvent être envisagés, sous réserve d'une désignation formelle cohérente avec le risque effectivement documenté."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende déjà comptabilisée est un actif reconnu, ce qui cadre avec une couverture de juste valeur. En consolidation, la règle générale d'exclusion de l'intragroupe est levée par l'exception visant le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Cette voie est donc formellement envisageable si la créance produit bien cette exposition résiduelle.",
      "conditions_fr": [
        "la créance doit constituer un poste monétaire intragroupe en devise",
        "les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "La documentation doit viser dès l'origine le risque de change porté par la créance intragroupe déjà reconnue.",
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
      "reasoning_fr": "IFRS 9 admet aussi une couverture de flux de trésorerie pour un actif reconnu. Ici, si la créance de dividende intragroupe est un poste monétaire en devise, le montant des flux de règlement en monnaie fonctionnelle varie avec le change et l'exception de 6.3.6 permet la qualification au niveau consolidé. La désignation reste toutefois défendable seulement si le risque couvert est bien formulé comme une variabilité des flux de règlement de cette créance.",
      "conditions_fr": [
        "la créance doit constituer un poste monétaire intragroupe en devise",
        "les écarts de change correspondants doivent pouvoir affecter le résultat consolidé parce qu'ils ne sont pas totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "La relation de couverture doit être documentée comme portant sur la variabilité des flux de règlement de la créance en devise.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le verrou principal en consolidation est de démontrer que la créance de dividende crée des écarts de change non totalement éliminés lors de la consolidation.",
    "La désignation et la documentation doivent être établies à l'inception de la relation de couverture.",
    "Le modèle retenu doit rester strictement cohérent avec le risque documenté: réévaluation de la créance existante ou variabilité des flux de règlement en devise."
  ]
}
