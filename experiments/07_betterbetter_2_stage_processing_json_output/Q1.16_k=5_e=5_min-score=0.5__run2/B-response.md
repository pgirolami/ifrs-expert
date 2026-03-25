{
  "assumptions_fr": [
    "La créance de dividendes est un poste monétaire intragroupe déjà comptabilisé entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Le risque de change subsiste dans les comptes consolidés, car les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Au consolidé, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe non totalement éliminé en consolidation.\nLa créance de dividendes peut donc faire l’objet d’une documentation de couverture, sous réserve de satisfaire aux critères formels et d’efficacité de la relation de couverture."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change de la créance intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans les comptes consolidés, l’élément couvert serait en principe exclu car intragroupe, mais l’exception d’IFRS 9 vise précisément le risque de change d’un poste monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés, ce que retiennent les hypothèses.\nComme la créance est déjà comptabilisée et constitue un actif reconnu exposé à un risque particulier pouvant affecter le résultat, une documentation en fair value hedge est envisageable si la relation est formellement désignée et satisfait aux tests d’efficacité.",
      "conditions_fr": [
        "désignation formelle et documentation de la relation de couverture à son inception",
        "identification d’un instrument de couverture éligible",
        "démonstration d’une relation économique, d’un risque de crédit non dominant et d’un hedge ratio conforme"
      ],
      "practical_implication_fr": "Il faut documenter au niveau consolidé le risque de change de la créance comme élément couvert et organiser les tests d’efficacité de la relation.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk and could affect profit or loss"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation ... and the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie du risque de change de la créance intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Les hypothèses placent la créance de dividendes dans l’exception d’IFRS 9 relative aux postes monétaires intragroupe dont le risque de change subsiste en consolidation, malgré la règle générale d’exclusion des éléments intragroupe.\nDès lors, une documentation en cash flow hedge peut être envisagée pour la variabilité des flux liée au change sur cet actif reconnu, à condition que la relation soit documentée à l’inception et qu’elle respecte les critères d’éligibilité et d’efficacité.",
      "conditions_fr": [
        "désignation formelle et documentation de la relation de couverture à son inception",
        "identification d’un instrument de couverture éligible",
        "démonstration d’une relation économique, d’un risque de crédit non dominant et d’un hedge ratio conforme"
      ],
      "practical_implication_fr": "Il faut documenter la variabilité des flux de règlement liée au change sur la créance et suivre la relation selon le modèle de cash flow hedge.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation ... and the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit traiter expressément l’exception de 6.3.6, car la règle de base de 6.3.5 exclut sinon les éléments intragroupe en consolidation.",
    "La relation de couverture doit être désignée et documentée à son inception ; aucune documentation rétrospective n’est couverte par les extraits fournis.",
    "Le dossier de couverture doit identifier l’instrument de couverture, l’élément couvert, le risque de change couvert, la stratégie de gestion du risque et la méthode d’évaluation de l’efficacité."
  ]
}
