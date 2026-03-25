{
  "assumptions_fr": [
    "La créance et la dette de dividende intragroupe sont libellées dans une devise générant un risque de change entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Le dividende comptabilisé crée un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "La question vise la qualification en comptabilité de couverture dans les états financiers consolidés au titre d’IFRS 9."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions, car IFRS 9 admet en consolidation la couverture du risque de change d’un poste monétaire intragroupe lorsque les écarts de change affectent le résultat consolidé. Pour une créance de dividende déjà comptabilisée, la couverture de juste valeur est la voie la plus directe; la couverture de flux de trésorerie reste envisageable si la relation est documentée sur la variabilité des flux de règlement."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende déjà comptabilisée est, selon les hypothèses, un poste monétaire intragroupe. IFRS 9 pose une exception au principe d’exclusion des éléments intragroupe en consolidation lorsque le risque de change n’est pas totalement éliminé et affecte le résultat; comme il s’agit d’un actif reconnu, une couverture de juste valeur peut alors être formellement désignée si la documentation et les tests d’efficacité sont établis dès l’origine.",
      "conditions_fr": [
        "La créance de dividende doit constituer un poste monétaire intragroupe.",
        "Les écarts de change doivent ne pas être totalement éliminés en consolidation et affecter le résultat consolidé.",
        "La relation de couverture doit être formellement désignée et documentée à l’inception.",
        "Les critères d’éligibilité et d’efficacité d’IFRS 9 doivent être respectés."
      ],
      "practical_implication_fr": "La documentation de couverture doit viser le risque de change sur la créance reconnue et être suivie au niveau consolidé.",
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
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... that could affect profit or loss."
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
      "reasoning_fr": "Dans cette situation, le même poste monétaire intragroupe peut aussi être envisagé sous l’angle de la variabilité des flux de règlement en devise de la créance de dividende. Cette qualification n’est possible que si, en consolidation, le risque documenté est bien la variabilité des flux de trésorerie liés à cette créance reconnue et si les écarts de change affectent le résultat consolidé; à défaut, cette voie est moins naturelle qu’une couverture de juste valeur.",
      "conditions_fr": [
        "La créance de dividende doit être un poste monétaire intragroupe exposé à une variabilité de flux en monnaie fonctionnelle.",
        "Les écarts de change liés au poste doivent affecter le résultat consolidé.",
        "La documentation doit identifier la variabilité des flux de règlement comme risque couvert.",
        "Les exigences de désignation, de documentation et d’efficacité d’IFRS 9 doivent être satisfaites."
      ],
      "practical_implication_fr": "Il faut documenter précisément que le risque couvert porte sur les flux de règlement de la créance de dividende au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability ... and could affect profit or loss."
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La démonstration clé, en consolidation, est que les écarts de change sur la créance/dette intragroupe ne sont pas totalement éliminés et affectent le résultat consolidé.",
    "La désignation et la documentation formelles doivent être en place à l’inception de la relation de couverture.",
    "Pour une créance de dividende déjà comptabilisée, la couverture de juste valeur est généralement la qualification la plus directe; la couverture de flux de trésorerie exige une documentation ciblée sur les flux de règlement."
  ]
}
