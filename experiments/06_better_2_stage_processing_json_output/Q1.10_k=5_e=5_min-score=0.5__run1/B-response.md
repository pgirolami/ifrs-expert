{
  "assumptions_fr": [
    "Un dividende intragroupe déclaré et comptabilisé à recevoir est analysé comme un actif monétaire intragroupe reconnu pour l’appréciation de l’élément couvert au titre d’IFRS 9."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, une créance de dividende intragroupe déjà comptabilisée ne peut être documentée en couverture du risque de change que si elle entre dans l’exception des postes monétaires intragroupe de l’IFRS 9 6.3.6 et si les exigences de désignation, documentation et efficacité de l’IFRS 9 6.4.1 sont respectées."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La question vise un dividende intragroupe déjà comptabilisé à recevoir et, selon l’hypothèse retenue, il s’agit d’un poste monétaire intragroupe reconnu. En consolidation, l’exception d’IFRS 9 6.3.6 permet alors une couverture du seul risque de change si ce risque génère des écarts non totalement éliminés à la consolidation, sous réserve de la documentation initiale et des tests d’efficacité de 6.4.1.",
      "conditions_fr": [
        "La créance de dividende et la dette correspondante constituent un poste monétaire intragroupe exposé à un risque de change entre entités ayant des monnaies fonctionnelles différentes.",
        "Le risque de change sur ce poste génère des gains ou pertes de change qui ne sont pas totalement éliminés en consolidation.",
        "La désignation porte sur le seul risque de change et la relation satisfait aux exigences de désignation, documentation, hedge ratio et efficacité de l’IFRS 9 6.4.1."
      ],
      "practical_implication_fr": "La documentation peut être préparée en consolidation, mais elle doit être centrée sur la créance monétaire intragroupe et sur son risque de change uniquement.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "ineligible_hedged_item",
      "label_fr": "Élément couvert inéligible",
      "applicability": "non",
      "reasoning_fr": "Cette approche reprend la règle générale de 6.3.5 selon laquelle, en consolidation, les éléments intragroupe ne sont pas des éléments couverts éligibles. Mais, dans la situation posée et sous l’hypothèse d’une créance monétaire intragroupe reconnue, 6.3.6 prévoit précisément une exception pour le risque de change; conclure à l’inéligibilité pure serait donc trop large.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas arrêter l’analyse à l’exclusion générale des éléments intragroupe sans tester l’exception du poste monétaire intragroupe.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "La question porte sur des dividendes intragroupe déjà comptabilisés à recevoir; avec l’hypothèse retenue, on est donc au stade d’un poste reconnu. L’approche ici visée pour la couverture de flux de trésorerie concerne, dans le contexte fourni, une transaction intragroupe future hautement probable avant comptabilisation; l’utiliser imposerait de revenir à un stade antérieur des faits, ce qui n’est pas permis.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette voie n’est pas la bonne pour justifier la documentation d’une créance de dividende déjà reconnue.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Les textes IFRS 9 et IFRIC 16 fournis visent un modèle distinct pour le risque de change d’un investissement net dans une activité à l’étranger, c’est-à-dire un montant de net assets inclus dans les états financiers. Ici, le dividende intragroupe comptabilisé à recevoir est, par hypothèse, une créance monétaire intragroupe reconnue et non un investissement net; cette approche ne s’applique donc pas.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas utiliser par analogie le modèle de couverture d’investissement net pour une créance de dividende intragroupe.",
      "references": [
        {
          "section": "7",
          "excerpt": "This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations"
        },
        {
          "section": "8",
          "excerpt": "it should not be applied by analogy to other types of hedge accounting."
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "En consolidation, il faut partir de la règle générale d’inéligibilité des éléments intragroupe puis tester explicitement l’exception de l’IFRS 9 6.3.6 pour les postes monétaires intragroupe.",
    "Comme le dividende est déjà comptabilisé à recevoir, l’analyse ne doit pas être reconstruite comme une transaction intragroupe future hautement probable.",
    "La documentation initiale doit identifier l’instrument de couverture, la créance de dividende couverte, le risque de change visé et la méthode d’évaluation de l’efficacité ainsi que du hedge ratio.",
    "Le modèle de couverture d’investissement net constitue une frontière conceptuelle distincte et ne doit pas être invoqué pour une simple créance de dividende intragroupe."
  ]
}
