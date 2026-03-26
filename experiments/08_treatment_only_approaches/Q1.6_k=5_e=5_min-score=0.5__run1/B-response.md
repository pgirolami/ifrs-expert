{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà été déclaré et a donné lieu à la comptabilisation d'une créance/dette ; l'analyse porte donc sur un élément monétaire intragroupe comptabilisé, et non sur une transaction intragroupe future.",
    "La créance/dette existe entre des entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change correspondants ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans les comptes consolidés, un poste intragroupe n'est en principe pas éligible, mais l'exception IFRS 9 vise le risque de change d'un élément monétaire intragroupe lorsqu'il affecte le résultat consolidé. Dans cette situation, la variation de change sur la créance de dividende peut donc être désignée en couverture, sous réserve des critères formels et d'efficacité d'IFRS 9."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende a déjà créé une créance/dette intragroupe comptabilisée ; il s'agit donc d'un actif/passif reconnu. En consolidation, la règle générale exclut les postes intragroupe, mais l'exception de l'élément monétaire intragroupe s'applique si les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. Dans ce cas précis, une désignation en couverture de juste valeur du risque de change est possible, sous réserve de la documentation et de l'efficacité requises.",
      "conditions_fr": [
        "La créance/dette de dividende est bien un élément monétaire intragroupe comptabilisé.",
        "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
        "La relation de couverture respecte la désignation, la documentation et les tests d'efficacité d'IFRS 9."
      ],
      "practical_implication_fr": "La documentation de couverture doit viser spécifiquement le risque de change de la créance/dette de dividende dans les comptes consolidés.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk and could affect profit or loss."
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance/dette de dividende intragroupe en devise expose aussi le groupe à une variabilité des flux de règlement en monnaie fonctionnelle. Comme l'item est supposé être un élément monétaire intragroupe dont les effets de change atteignent le résultat consolidé, l'exception de 6.3.6 ouvre l'éligibilité en consolidation. Une désignation en couverture de flux de trésorerie est donc également envisageable, si elle correspond à la gestion du risque documentée et satisfait IFRS 9.",
      "conditions_fr": [
        "Le risque couvert est bien la variabilité des flux de règlement liée au change sur la créance/dette reconnue.",
        "Les effets de change de l'élément monétaire intragroupe affectent le résultat consolidé.",
        "La relation de couverture satisfait aux exigences de désignation, de documentation, de ratio de couverture et d'efficacité."
      ],
      "practical_implication_fr": "Le choix de ce modèle suppose d'aligner la documentation sur la variabilité des flux de règlement en devise dans les comptes consolidés.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability ... and could affect profit or loss."
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif est le moment de comptabilisation : l'analyse ci-dessus vaut parce qu'une créance/dette de dividende a déjà été constatée.",
    "En consolidation, il faut démontrer que les écarts de change du poste monétaire intragroupe ne sont pas totalement éliminés et affectent bien le résultat consolidé.",
    "La désignation doit être faite dès l'origine avec documentation formelle du poste couvert, de l'instrument de couverture, du risque couvert et du test d'efficacité.",
    "Le modèle retenu doit être cohérent avec la gestion du risque du groupe : couverture de juste valeur ou de flux de trésorerie, mais toujours sur le risque de change du poste monétaire intragroupe."
  ]
}
