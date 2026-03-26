{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a déjà généré une créance/dette intragroupe comptabilisée et libellée dans une devise différente d’au moins une monnaie fonctionnelle pertinente.",
    "La question vise uniquement la comptabilité de couverture, en états financiers consolidés, pour le seul risque de change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, un dividende intragroupe à recevoir est en principe exclu comme élément couvert. Il peut toutefois être documenté pour le risque de change si la créance/dette de dividende constitue un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation; sur le contexte fourni, les deux formes de couverture restent alors ouvertes."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe est déjà comptabilisé à recevoir: il s’agit donc d’un actif reconnu au sein du groupe. En consolidation, la règle générale interdit les éléments intragroupe, mais l’exception de 6.3.6 ouvre la couverture du seul risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas entièrement éliminés; c’est compatible avec une couverture de juste valeur d’une créance reconnue.",
      "conditions_fr": [
        "La créance/dette de dividende intragroupe est un élément monétaire entre entités ayant des monnaies fonctionnelles différentes.",
        "Les écarts de change afférents génèrent des gains ou pertes qui ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation peut viser la créance de dividende existante comme élément couvert du seul risque de change en consolidation.",
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
      "reasoning_fr": "Le contexte fourni définit aussi la couverture de flux de trésorerie comme pouvant porter sur un actif ou passif reconnu. Dans cette situation, elle n’est envisageable en consolidation qu’après franchissement du même verrou de 6.3.5/6.3.6: le dividende doit être un élément monétaire intragroupe dont le risque de change crée des écarts non totalement éliminés, la documentation visant alors la variabilité en monnaie fonctionnelle des flux de règlement.",
      "conditions_fr": [
        "La créance/dette de dividende intragroupe est un élément monétaire entre entités ayant des monnaies fonctionnelles différentes.",
        "Les écarts de change afférents génèrent des gains ou pertes qui ne sont pas totalement éliminés en consolidation.",
        "La relation est documentée sur la variabilité en monnaie fonctionnelle des flux d’encaissement ou de décaissement liés au règlement du dividende."
      ],
      "practical_implication_fr": "Si cette voie est retenue, la documentation doit cibler les flux de règlement du dividende exposés au change, et non un risque intragroupe autre que le change.",
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
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être établie à l’inception et identifier l’instrument de couverture, la créance de dividende, le risque de change couvert et le ratio de couverture.",
    "Le point décisif en consolidation est de démontrer que les écarts de change sur la créance/dette de dividende ne sont pas totalement éliminés; sinon la relation ne peut pas être qualifiée.",
    "Quelle que soit l’approche retenue, il faut aussi satisfaire aux critères de 6.4.1 sur la relation économique, l’absence de domination du risque de crédit et la cohérence du hedge ratio."
  ]
}
