{
  "assumptions_fr": [
    "La créance de dividendes est un élément monétaire intragroupe reconnu et libellé en devise.",
    "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "L’entité dispose d’un instrument de couverture éligible et peut satisfaire aux exigences IFRS 9 de désignation, de documentation et d’efficacité."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, dans cette situation, le hedge accounting est envisageable en consolidation grâce à l’exception IFRS 9 visant le risque de change des éléments monétaires intragroupe. Il faut toutefois démontrer que l’exposition affecte bien le résultat consolidé et respecter la désignation, la documentation et l’efficacité de la relation de couverture."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "En consolidation, les éléments intragroupe sont en principe exclus, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe. Ici, la créance de dividendes est supposée être un actif reconnu en devise dont les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. Un fair value hedge peut donc s’appliquer dans cette situation, sous réserve de la documentation initiale et des tests d’efficacité.",
      "conditions_fr": [
        "La créance constitue bien un élément monétaire intragroupe en devise déjà comptabilisé",
        "Les écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé",
        "La relation de couverture est formellement désignée et documentée dès l’origine",
        "L’instrument de couverture est éligible et la relation satisfait aux critères d’efficacité"
      ],
      "practical_implication_fr": "La documentation doit viser explicitement le risque de change de la créance reconnue au niveau consolidé.",
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
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "En consolidation, la même exception permet aussi de viser le risque de change d’un élément monétaire intragroupe. Ici, la créance de dividendes en devise crée une variabilité du montant encaissé en monnaie fonctionnelle, et l’hypothèse retient que cet effet touche le résultat consolidé. Un cash flow hedge peut donc être documenté dans cette situation, sous réserve des critères de désignation, de hedge ratio et d’efficacité.",
      "conditions_fr": [
        "La variabilité liée au change sur l’encaissement de la créance peut affecter le résultat consolidé",
        "L’exception applicable aux éléments monétaires intragroupe en consolidation est satisfaite",
        "La relation est désignée et documentée à l’inception",
        "Le hedge ratio et l’efficacité économique sont démontrés"
      ],
      "practical_implication_fr": "Il faut documenter la variabilité des flux liée au change et suivre l’efficacité de la couverture au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point clé est l’exception IFRS 9 sur les éléments monétaires intragroupe en devise : sans impact potentiel sur le résultat consolidé, l’exposition ne serait pas éligible.",
    "La désignation et la documentation doivent être en place à l’inception, avec identification de l’instrument, du risque de change couvert et de la méthode d’évaluation de l’efficacité.",
    "Le choix entre fair value hedge et cash flow hedge doit rester cohérent avec la manière dont l’exposition de change de cette créance est gérée et mesurée en consolidation."
  ]
}
