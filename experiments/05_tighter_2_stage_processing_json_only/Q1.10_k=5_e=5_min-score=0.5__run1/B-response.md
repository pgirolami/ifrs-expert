{
  "assumptions": [
    "Un dividende intragroupe déclaré et comptabilisé en créance/dette est traité comme un poste monétaire intragroupe reconnu.",
    "La question vise la comptabilité de couverture dans les états financiers consolidés, et non dans les états financiers individuels ou séparés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en consolidation, si le dividende intragroupe comptabilisé à recevoir relève de l'exception IFRS 9 applicable aux postes monétaires intragroupe en devise et si les écarts de change ne sont pas totalement éliminés. Il faut aussi satisfaire aux exigences de désignation, documentation et efficacité de la relation de couverture."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "monetary_item_hedge",
      "label_fr": "Couverture de change d'un poste monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 pose d'abord une règle générale d'externalité des éléments couverts en consolidation, puis prévoit une exception explicite pour le risque de change d'un poste monétaire intragroupe. Si la créance de dividende entre entités de devises fonctionnelles différentes génère des écarts de change non totalement éliminés en consolidation, elle peut être désignée. La relation doit en plus satisfaire aux critères de documentation et d'efficacité d'IFRS 9.",
      "conditions_fr": [
        "Le dividende à recevoir/à payer est un poste monétaire intragroupe reconnu.",
        "Les entités concernées ont des monnaies fonctionnelles différentes.",
        "Les écarts de change afférents ne sont pas totalement éliminés en consolidation.",
        "La relation est formellement désignée et documentée à l'origine.",
        "Les critères d'efficacité, y compris le hedge ratio, sont respectés."
      ],
      "practical_implication_fr": "La documentation est possible en consolidation, mais seulement comme couverture du risque de change sur le poste monétaire intragroupe et avec démonstration de l'exception IFRS 9.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "ineligible_hedged_item",
      "label_fr": "Élément couvert inéligible",
      "applicability": "non",
      "reasoning_fr": "La règle générale d'IFRS 9 en consolidation exige que l'actif, le passif, l'engagement ferme ou la transaction prévue soit avec une partie externe au groupe. Donc, sans l'exception spécifique des postes monétaires intragroupe, un dividende intragroupe n'est pas un élément couvert admissible. Si les effets de change sont totalement éliminés à la consolidation, l'exception ne joue pas.",
      "conditions_fr": [
        "Les effets de change du dividende sont totalement éliminés en consolidation.",
        "Le dividende ne remplit pas l'exception de l'article 6.3.6 sur les postes monétaires intragroupe."
      ],
      "practical_implication_fr": "À défaut d'exception applicable, aucune relation de couverture ne peut être documentée sur ce dividende intragroupe en consolidation.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "However, as an exception to paragraph 6.3.5"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "forecast_transaction_hedge",
      "label_fr": "Couverture d'une transaction intragroupe future",
      "applicability": "non",
      "reasoning_fr": "IFRS 9 admet certaines transactions intragroupe futures hautement probables pour le seul risque de change en consolidation. Mais ce modèle vise une transaction encore future et non un dividende déjà comptabilisé à recevoir. Une fois la créance reconnue, l'analyse pertinente est celle du poste monétaire intragroupe, pas celle de la transaction prévue.",
      "conditions_fr": [
        "L'approche ne vaut qu'avant comptabilisation, tant que la transaction reste hautement probable.",
        "La transaction doit être libellée dans une monnaie autre que la monnaie fonctionnelle de l'entité qui y entre.",
        "Le risque de change doit affecter le résultat net consolidé."
      ],
      "practical_implication_fr": "Pour un dividende déjà enregistré en créance, cette voie ne doit pas être utilisée pour la documentation de couverture.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction ... that transaction must be highly probable"
        },
        {
          "section": "B6.3.5",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in a cash flow hedge"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "IFRIC 16 traite uniquement des couvertures du risque de change lié à un investissement net dans une activité à l'étranger. L'élément couvert y est un montant d'actifs nets d'une activité étrangère, non une créance de dividende intragroupe. Cette documentation ne doit donc pas être requalifiée en couverture d'investissement net.",
      "conditions_fr": [
        "L'élément couvert devrait être un montant d'actifs nets d'une activité à l'étranger.",
        "La relation devrait être documentée comme couverture d'investissement net selon IFRS 9 et IFRIC 16."
      ],
      "practical_implication_fr": "La piste 'net investment hedge' n'est pas adaptée à un dividende intragroupe comptabilisé à recevoir.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d'abord si la créance de dividende est bien un poste monétaire intragroupe en devise au sens de l'hypothèse retenue.",
    "Tester si les écarts de change correspondants ne sont pas totalement éliminés en consolidation, ce qui suppose en pratique des monnaies fonctionnelles différentes.",
    "La documentation de couverture doit être établie à l'origine de la relation avec identification de l'instrument, de l'élément couvert, du risque couvert et de la méthode d'évaluation de l'efficacité.",
    "Ne pas utiliser le modèle de transaction future intragroupe si le dividende est déjà comptabilisé en créance.",
    "Si les conditions de l'exception IFRS 9 6.3.6 ne sont pas remplies, la réponse redevient négative en consolidation."
  ]
}
