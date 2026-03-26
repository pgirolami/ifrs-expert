{
  "assumptions_fr": [
    "Le dividende intragroupe à recevoir est déjà comptabilisé comme créance intragroupe au moment de la désignation.",
    "L’analyse vise les états financiers consolidés IFRS du groupe, hors cas particulier d’une entité d’investissement."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais seulement via l’exception relative au risque de change d’un poste monétaire intragroupe en consolidation. Ce cas ne relève ni d’une cash flow hedge sur transaction future, ni d’une couverture d’investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "monetary_item_hedge",
      "label_fr": "Couverture du risque de change d’un poste monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le dividende intragroupe à recevoir est, dans ce cas, une créance intragroupe déjà reconnue et s’analyse comme un poste monétaire plutôt que comme une transaction future.\nEn consolidation, cette voie n’est ouverte que si le risque de change sur cette créance génère des écarts non entièrement éliminés, typiquement entre entités à monnaies fonctionnelles différentes.",
      "conditions_fr": [
        "la créance de dividende intragroupe est un poste monétaire entre entités du groupe ayant des monnaies fonctionnelles différentes",
        "les gains ou pertes de change correspondants ne sont pas entièrement éliminés en consolidation"
      ],
      "practical_implication_fr": "La documentation doit désigner la créance de dividende reconnue comme élément couvert et démontrer l’exposition de change résiduelle au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item"
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
      "label_fr": "Couverture de flux de trésorerie d’une transaction intragroupe future",
      "applicability": "non",
      "reasoning_fr": "Cette approche vise une transaction intragroupe future hautement probable.\nOr la question porte sur des dividendes déjà comptabilisés à recevoir ; ce n’est donc plus un flux futur à couvrir au titre d’une cash flow hedge.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter cette relation comme cash flow hedge, car le fait générateur n’est pas une transaction future hautement probable.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "that transaction must be highly probable"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Cette approche concerne le risque de change attaché à un investissement net dans les actifs nets d’une activité étrangère.\nUne créance de dividende intragroupe comptabilisée à recevoir n’est pas un montant de net assets de l’activité étrangère ; elle ne correspond donc pas à ce schéma.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas qualifier la créance de dividende comme couverture d’investissement net ; ce mécanisme vise les actifs nets de l’activité étrangère.",
      "references": [
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "10",
          "excerpt": "only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Faire la désignation formelle et la documentation à l’inception de la relation de couverture.",
    "Justifier explicitement que l’élément couvert est une créance de dividende intragroupe reconnue, et non un dividende futur.",
    "Démontrer dans le dossier de couverture que les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.",
    "Si les faits évoluent vers un dividende seulement envisagé ou déclaré ultérieurement, l’analyse devra être refaite car l’approche applicable pourrait changer."
  ]
}
