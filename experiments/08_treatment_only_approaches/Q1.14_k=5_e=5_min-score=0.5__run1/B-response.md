{
  "assumptions_fr": [
    "L’analyse porte sur les états financiers consolidés du groupe.",
    "Le dividende intragroupe déclaré a créé une créance/dette monétaire en devise entre entités du groupe, et les écarts de change correspondants ne sont pas totalement éliminés en consolidation.",
    "La relation de couverture envisagée satisfait par ailleurs aux exigences IFRS 9 de documentation formelle et d’efficacité."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. En consolidation, IFRS 9 prévoit une exception permettant de désigner le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Dans ce cas, la couverture de juste valeur est la lecture la plus directe; un cash flow hedge reste envisageable si la désignation vise bien la variabilité des flux de trésorerie de la créance."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "La règle générale vise des expositions avec des tiers externes, mais IFRS 9 prévoit en consolidation une exception explicite pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Ici, le dividende déclaré a créé un montant à recevoir déjà comptabilisé; la couverture de juste valeur correspond donc directement à un actif reconnu dont la valeur varie avec le change et affecte le résultat consolidé.",
      "conditions_fr": [
        "Le montant à recevoir constitue bien un élément monétaire intragroupe.",
        "Les écarts de change afférents ne sont pas totalement éliminés en consolidation.",
        "La relation est désignée et documentée dès l’origine, avec respect des critères d’efficacité."
      ],
      "practical_implication_fr": "La documentation peut désigner la créance intragroupe issue du dividende comme élément couvert au titre du risque de change en couverture de juste valeur.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
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
      "reasoning_fr": "Le montant à recevoir est aussi un actif reconnu, et IFRS 9 admet un cash flow hedge sur la variabilité de flux de trésorerie liée à un actif ou passif reconnu pouvant affecter le résultat. Dans cette situation, cela n’est recevable que si la documentation rattache clairement le risque couvert à la variabilité en monnaie fonctionnelle des encaissements liés à cette créance intragroupe; à défaut, la couverture de juste valeur est plus naturelle.",
      "conditions_fr": [
        "La désignation vise explicitement la variabilité des flux de trésorerie liée au risque de change du montant à recevoir.",
        "Cette variabilité est susceptible d’affecter le résultat consolidé.",
        "L’exception applicable aux éléments monétaires intragroupe et les critères généraux de documentation et d’efficacité sont respectés."
      ],
      "practical_implication_fr": "Le cash flow hedge peut être documenté, mais la rédaction de la relation doit être plus précise sur les flux couverts et leur impact en résultat consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La désignation et la documentation doivent être établies à l’origine de la relation de couverture.",
    "Il faut démontrer en consolidation que les écarts de change sur la créance/dette de dividende intragroupe ne sont pas totalement éliminés.",
    "Pour cette exposition déjà comptabilisée, la couverture de juste valeur est en pratique la voie la plus directe."
  ]
}
