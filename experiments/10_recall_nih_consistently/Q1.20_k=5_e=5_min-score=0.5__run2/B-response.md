{
  "assumptions_fr": [
    "La créance est un poste monétaire libellé en devise qui crée un risque de change dans les états financiers consolidés.",
    "L’analyse est menée au titre du hedge accounting du risque de change selon IFRS 9."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Sous les hypothèses posées, le risque de change sur cette créance intragroupe peut être couvert en hedge accounting dans les comptes consolidés via un fair value hedge ou un cash flow hedge. En revanche, cette exposition ne relève pas d’une couverture d’investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui",
      "reasoning_fr": "En consolidation, un élément intragroupe n’est en principe pas éligible comme hedged item.\nMais le paragraphe 6.3.6 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsqu’il génère des écarts non totalement éliminés.\nIci, la créance de dividendes est un actif comptabilisé exposé au change ; le modèle de fair value hedge de 6.5.2(a) est donc applicable.",
      "conditions_fr": [],
      "practical_implication_fr": "La documentation peut désigner la créance comme élément couvert pour son risque de change en fair value hedge.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui",
      "reasoning_fr": "La créance est aussi un actif comptabilisé dont le montant encaissé en monnaie de consolidation varie avec le change.\nLe paragraphe 6.5.2(b) vise la variabilité des flux de trésorerie d’un actif comptabilisé, et 6.3.6 admet cette désignation pour un poste monétaire intragroupe en consolidation.\nDans cette situation, une documentation en cash flow hedge du risque de change est donc également possible.",
      "conditions_fr": [],
      "practical_implication_fr": "La documentation peut viser la variabilité des flux de règlement de la créance due aux fluctuations de change.",
      "references": [
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of ... a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.5",
          "excerpt": "Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements ... and not in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité étrangère",
      "applicability": "non",
      "reasoning_fr": "La question porte sur une créance de dividendes intragroupe, pas sur des net assets d’une activité étrangère.\nIFRIC 16 limite explicitement ce modèle aux hedges of net investments in foreign operations et exclut son application par analogie à d’autres couvertures.\nCette voie ne s’applique donc pas à l’exposition décrite.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter cette créance de dividendes comme un net investment hedge.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "7",
          "excerpt": "This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif en consolidation est de démontrer que la créance est bien un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés.",
    "Le choix entre fair value hedge et cash flow hedge doit être arrêté dès l’inception et formalisé avec la désignation et la documentation requises par le paragraphe 6.4.1.",
    "La documentation doit identifier précisément le risque couvert comme le seul risque de change attaché à la créance de dividendes intragroupe.",
    "La piste net investment hedge doit être écartée, car elle vise les net assets d’une activité étrangère et non une créance de dividendes."
  ]
}
