{
  "assumptions_fr": [
    "La créance de dividende intragroupe est un élément monétaire intragroupe reconnu dans les états financiers consolidés.",
    "La créance est libellée dans une devise générant des écarts de change qui ne sont pas totalement éliminés en consolidation parce que les entités concernées ont des monnaies fonctionnelles différentes."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans cette situation, IFRS 9 permet, par exception, de désigner le risque de change d’un élément monétaire intragroupe comme élément couvert en consolidation si les écarts de change ne sont pas totalement éliminés. La désignation reste soumise aux critères formels de documentation, de relation économique et de hedge ratio."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende intragroupe est un actif reconnu en consolidation. La règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Ce risque peut donc être désigné dans une couverture de juste valeur s’il affecte le résultat et si les critères de désignation et d’efficacité sont respectés.",
      "conditions_fr": [
        "La créance doit être un élément monétaire intragroupe reconnu dans les comptes consolidés.",
        "Les écarts de change doivent ne pas être totalement éliminés en consolidation.",
        "La relation doit être formellement désignée et documentée à l’origine, avec relation économique et hedge ratio conforme."
      ],
      "practical_implication_fr": "Le groupe peut couvrir en consolidation la variation de valeur liée au change sur cette créance, sous réserve d’une documentation IFRS 9 complète.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk and could affect profit or loss."
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
      "reasoning_fr": "Dans cette situation, la même exception d’IFRS 9 permet de viser en consolidation le risque de change porté par la créance intragroupe reconnue, dès lors qu’il affecte le résultat consolidé. Une couverture de flux de trésorerie est envisageable si l’exposition couverte est documentée comme une variabilité des flux en monnaie fonctionnelle liée au change sur cet actif reconnu. Elle reste soumise aux critères généraux de désignation, de documentation et d’efficacité.",
      "conditions_fr": [
        "La créance doit être un élément monétaire intragroupe reconnu dans les comptes consolidés.",
        "Le risque de change doit affecter le résultat consolidé parce que les écarts ne sont pas totalement éliminés.",
        "La documentation de couverture doit identifier le risque couvert, l’instrument de couverture et la manière d’évaluer l’efficacité."
      ],
      "practical_implication_fr": "Le groupe peut structurer la relation comme une couverture de la variabilité des flux en monnaie fonctionnelle liée au change sur la créance.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with ... a recognised asset or liability ... and could affect profit or loss."
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La possibilité existe ici uniquement en consolidation, via l’exception visant le risque de change d’un élément monétaire intragroupe.",
    "Le point décisif est que les écarts de change sur la créance ne soient pas totalement éliminés en consolidation.",
    "Le choix entre couverture de juste valeur et couverture de flux de trésorerie doit être cohérent avec le risque précisément documenté au démarrage de la relation."
  ]
}
