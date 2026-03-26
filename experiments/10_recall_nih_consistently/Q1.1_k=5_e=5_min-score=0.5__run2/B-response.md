{
  "assumptions_fr": [
    "La créance de dividende intragroupe crée une exposition au risque de change car les entités concernées du groupe ont des monnaies fonctionnelles différentes.",
    "La question est limitée aux approches de comptabilité de couverture pouvant être documentées dans les états financiers consolidés pour la composante change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En comptes consolidés, la partie change de cette créance de dividende intragroupe peut être documentée en couverture de juste valeur ou en couverture de flux de trésorerie si l'élément monétaire intragroupe génère des écarts de change non totalement éliminés. En revanche, la couverture d'un investissement net ne correspond pas à cette créance."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe est déjà comptabilisé en créance : il s'agit d'un actif reconnu. En consolidation, IFRS 9 permet exceptionnellement de désigner le risque de change d'un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés ; ce cadre est cohérent avec une couverture de juste valeur du poste reconnu.",
      "conditions_fr": [
        "La créance doit constituer un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation viserait la créance de dividende reconnue comme élément couvert pour son risque de change.",
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
      "reasoning_fr": "La même créance reconnue peut aussi être documentée sous l'angle de la variabilité des flux de trésorerie en monnaie fonctionnelle causée par le change. Dans cette situation, cela n'est recevable en consolidation que si l'exposition de change sur l'élément monétaire intragroupe affecte le résultat consolidé et n'est pas totalement éliminée.",
      "conditions_fr": [
        "La documentation doit viser la variabilité des flux liée au change sur cette créance en consolidation.",
        "La créance doit constituer un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation devrait expliquer que le risque couvert est la variabilité des flux en monnaie fonctionnelle due au change sur la créance.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
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
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'un investissement net",
      "applicability": "non",
      "reasoning_fr": "Le fait décrit porte sur une créance de dividende intragroupe déjà comptabilisée, et non sur un montant d'actifs nets d'une activité à l'étranger. Le modèle de couverture d'un investissement net vise le risque de change de l'investissement net dans l'opération étrangère ; il ne correspond donc pas à cette créance.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette voie doit être écartée pour couvrir la créance de dividende elle-même en consolidation.",
      "references": [
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation."
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        },
        {
          "section": "14",
          "excerpt": "may be designated as a hedging instrument in a hedge of a net investment in a foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation de couverture doit être formalisée dès l'origine et identifier l'instrument de couverture, la créance de dividende, le risque de change couvert et la manière d'apprécier l'efficacité.",
    "En consolidation, le point déterminant est de démontrer que la créance de dividende est un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés.",
    "Si l'objectif économique réel porte sur l'investissement net dans la filiale étrangère, la documentation doit viser les actifs nets de cette opération étrangère et non la créance de dividende."
  ]
}
