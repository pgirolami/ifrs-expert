{
  "assumptions_fr": [
    "La question est analysée dans le cadre des états financiers consolidés.",
    "La créance de dividende intragroupe est un élément monétaire libellé en devise qui crée une exposition de change pour l'entité bénéficiaire."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, un élément intragroupe est en principe exclu, mais IFRS 9 prévoit une exception pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés. Une créance de dividende intragroupe peut donc être documentée comme exposition couverte si cette condition est satisfaite au niveau consolidé."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur de la créance",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende est un actif comptabilisé, ce qui correspond au champ d'une couverture de juste valeur. Toutefois, comme l'exposition est intragroupe, elle n'est éligible en consolidation que par l'exception visant le risque de change d'un élément monétaire intragroupe. Cette voie n'est donc ouverte que si les écarts de change sur cette créance ne sont pas entièrement éliminés en consolidation.",
      "conditions_fr": [
        "Les entités concernées ont des monnaies fonctionnelles différentes et les écarts de change sur la créance/dividende intragroupe ne sont pas entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "La créance de dividende peut être désignée comme élément couvert au titre de son seul risque de change dans les comptes consolidés.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
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
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 admet aussi une couverture de flux de trésorerie pour un actif comptabilisé lorsqu'une variabilité de flux attribuable à un risque particulier peut affecter le résultat. Pour cette créance de dividende intragroupe, cela n'est recevable que si le risque de change subsiste en consolidation et affecte le résultat consolidé. Si l'effet de change est totalement éliminé en consolidation, ce modèle ne s'applique pas dans ce cas.",
      "conditions_fr": [
        "La variabilité des encaissements en monnaie fonctionnelle au titre de la créance de dividende affecte le résultat consolidé, parce que le risque de change n'est pas entièrement éliminé en consolidation."
      ],
      "practical_implication_fr": "Cette désignation n'est défendable que si l'exposition est analysée, au niveau consolidé, comme une variabilité de flux liée au change affectant le résultat.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d'abord que la créance de dividende et la dette correspondante sont entre entités du groupe ayant des monnaies fonctionnelles différentes ; sinon l'exception intragroupe de change ne joue pas.",
    "La documentation doit être mise en place dès l'origine de la relation de couverture au niveau consolidé, en identifiant l'instrument, la créance de dividende, le risque de change désigné et le hedge ratio.",
    "Ne désigner que le risque de change qui subsiste après les éliminations intragroupe ; une exposition totalement neutralisée en consolidation ne peut pas servir d'élément couvert."
  ]
}
