{
  "assumptions_fr": [
    "La créance et la dette de dividende intragroupe sont libellées dans une devise étrangère pour au moins une des entités concernées.",
    "Les écarts de change correspondants affecteraient le résultat consolidé et ne seraient pas entièrement éliminés en consolidation.",
    "La question porte sur les modèles de comptabilité de couverture à apprécier dans les comptes consolidés pour cette exposition de change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, une documentation de couverture sur la composante change est envisageable en consolidation via l’exception IFRS 9 applicable aux postes monétaires intragroupe. Pour une créance de dividende déjà comptabilisée, la couverture de juste valeur est le cadrage le plus direct; la couverture de flux de trésorerie n’est défendable que si le risque documenté est la variabilité de change des flux de règlement. La couverture d’investissement net ne correspond pas aux faits décrits."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance de dividende est déjà un actif reconnu, ce qui aligne bien ce modèle avec un risque de change porté par un poste comptabilisé. En consolidation, un poste intragroupe est en principe exclu, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts affectent le résultat consolidé et ne sont pas totalement éliminés. Dans cette situation, c’est la voie la plus directe.",
      "conditions_fr": [
        "La créance de dividende constitue un poste monétaire intragroupe en devise.",
        "Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé."
      ],
      "practical_implication_fr": "Documenter l’instrument de couverture, la créance couverte, le risque de change couvert et la méthode d’appréciation de l’efficacité.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ce modèle peut viser la variabilité des flux rattachés à un actif reconnu. Ici, il n’est pertinent que si la documentation cible bien la variabilité de change sur le règlement de la créance de dividende en devise, et non simplement sa réévaluation comptable. En consolidation, il faut en plus rester dans l’exception IFRS 9 sur les postes monétaires intragroupe dont l’effet de change atteint le résultat consolidé.",
      "conditions_fr": [
        "Le risque couvert est documenté comme la variabilité de change des flux de règlement de la créance reconnue.",
        "Les écarts de change sur ce poste monétaire intragroupe ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé."
      ],
      "practical_implication_fr": "La documentation doit démontrer que le risque couvert porte sur les flux de règlement en devise de la créance de dividende.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
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
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Les faits décrits portent sur une créance de dividende intragroupe déjà comptabilisée, et non sur le risque de change attaché à un investissement net dans une activité à l’étranger. IFRIC 16 réserve ce modèle aux net investments et à un montant de net assets de l’activité étrangère en consolidation. Sur cette base factuelle, ce n’est pas la bonne qualification de l’élément couvert.",
      "conditions_fr": [],
      "practical_implication_fr": "Ce modèle ne permet pas de documenter directement le change d’une créance de dividende intragroupe.",
      "references": [
        {
          "section": "7",
          "excerpt": "This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être en place dès l’origine de la relation de couverture et identifier l’instrument, l’élément couvert, le risque de change et la méthode d’appréciation de l’efficacité.",
    "En consolidation, conservez une démonstration explicite que les écarts de change sur la créance/dette de dividende ne sont pas entièrement éliminés et affectent le résultat consolidé.",
    "Pour une créance de dividende déjà reconnue, la couverture de juste valeur est généralement le point d’entrée le plus robuste; la couverture de flux de trésorerie demande une formulation plus serrée du risque couvert.",
    "La couverture d’investissement net suppose un autre objet couvert, à savoir un montant de net assets d’une activité étrangère, et ne doit pas être confondue avec la créance de dividende."
  ]
}
