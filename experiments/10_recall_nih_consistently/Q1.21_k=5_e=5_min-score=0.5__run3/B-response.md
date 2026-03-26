{
  "assumptions_fr": [
    "La créance de dividendes est un élément monétaire intragroupe comptabilisé, libellé en devise, et l'analyse est faite dans les comptes consolidés du groupe.",
    "L'exposition de change mentionnée correspond à des écarts de change qui subsistent en consolidation et ne sont pas entièrement éliminés."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. En comptes consolidés, IFRS 9 prévoit une exception permettant de désigner le risque de change d'un élément monétaire intragroupe lorsqu'il génère des écarts de change non entièrement éliminés. Sur les faits décrits, la créance de dividendes entre dans ce cadre; la couverture d'un investissement net n'est pas la qualification pertinente."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "La créance de dividendes est, dans cette situation, un actif comptabilisé exposé au risque de change.\nMême si les éléments intragroupe sont en principe exclus en consolidé, IFRS 9 prévoit une exception pour un élément monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés.\nDans ce cas, une désignation du risque de change en couverture de juste valeur est recevable.",
      "conditions_fr": [],
      "practical_implication_fr": "Le groupe peut documenter la créance de dividendes comme élément couvert pour le seul risque de change en consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui",
      "reasoning_fr": "Le texte permet aussi une couverture de flux de trésorerie pour un actif comptabilisé exposé à un risque particulier.\nIci, les flux de règlement de la créance de dividendes en monnaie de consolidation varient avec le change, et l'exception visant les éléments monétaires intragroupe enlève l'obstacle intragroupe dans ce contexte consolidé.\nCette approche peut donc également être retenue sur ces faits.",
      "conditions_fr": [],
      "practical_implication_fr": "Le groupe peut viser les flux de règlement futurs de la créance si c'est ainsi que le risque de change est géré.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'un investissement net à l'étranger",
      "applicability": "non",
      "reasoning_fr": "Cette voie vise un montant de net assets d'une opération étrangère, y compris un élément monétaire comptabilisé comme faisant partie de l'investissement net.\nLa question porte ici sur une créance de dividendes intragroupe comptabilisée, et non sur un montant de net assets d'une opération étrangère.\nSur ces faits, la désignation comme couverture d'un investissement net ne convient pas.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas fonder la désignation de cette créance sur le modèle de couverture d'investissement net.",
      "references": [
        {
          "section": "6.5.13",
          "excerpt": "including a hedge of a monetary item that is accounted for as part of the net investment"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier et conserver la preuve que les écarts de change sur la créance subsistent en consolidation et ne sont pas entièrement éliminés.",
    "Documenter à l'origine la relation de couverture, l'instrument, la créance couverte, le risque de change visé et le hedge ratio.",
    "Choisir le modèle de couverture cohérent avec la gestion du risque: juste valeur pour la réévaluation de la créance, flux de trésorerie pour son règlement futur.",
    "Ne pas présenter cette créance comme une couverture d'investissement net sans faits distincts montrant qu'elle fait partie de cet investissement net."
  ]
}
