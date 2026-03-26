{
  "assumptions_fr": [
    "La créance sur dividendes intragroupe est un élément monétaire comptabilisé entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "L’exposition de change identifiée génère des écarts de change qui ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Au niveau consolidé, un élément intragroupe n’est en principe pas éligible, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe. Dans cette situation, l’exposition peut donc être couverte si cette exception est satisfaite et si les critères de désignation, documentation et efficacité sont respectés."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance sur dividendes intragroupe est un actif monétaire déjà comptabilisé. Bien que la règle générale exclue les éléments intragroupe en consolidation, IFRS 9 admet le risque de change d’un élément monétaire intragroupe s’il crée des écarts de change non totalement éliminés et affecte le résultat consolidé. Une couverture de juste valeur est donc recevable si la relation est formellement désignée et efficace.",
      "conditions_fr": [
        "la créance est un élément monétaire intragroupe reconnu",
        "les écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé",
        "la relation satisfait aux exigences de désignation, de documentation et d’efficacité d’IFRS 9.6.4.1"
      ],
      "practical_implication_fr": "Le risque de change de la créance peut être désigné comme élément couvert dans une relation de couverture de juste valeur au niveau consolidé.",
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
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, l’exposition de change sur la créance reconnue peut aussi être traitée comme une variabilité de flux de trésorerie en devise susceptible d’affecter le résultat consolidé. L’exception d’IFRS 9 pour un élément monétaire intragroupe ouvre alors l’éligibilité en consolidation. Ce traitement n’est applicable que si l’objectif de gestion du risque, la documentation initiale et l’efficacité de la couverture sont établis.",
      "conditions_fr": [
        "la variabilité de change associée à la créance peut affecter le résultat consolidé",
        "l’exception applicable aux éléments monétaires intragroupe en devise est satisfaite",
        "la relation satisfait aux exigences de désignation, de documentation et d’efficacité d’IFRS 9.6.4.1"
      ],
      "practical_implication_fr": "Le groupe peut désigner la variabilité des flux en devise liés à cette créance dans une relation de couverture de flux de trésorerie au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter dès l’origine pourquoi l’exception relative à l’élément monétaire intragroupe en devise s’applique en consolidation, malgré la règle générale visant des contreparties externes.",
    "Conserver la preuve que les écarts de change sur la créance sur dividendes ne sont pas totalement éliminés et affectent bien le résultat consolidé.",
    "Choisir entre couverture de juste valeur et couverture de flux de trésorerie en cohérence avec l’objectif de gestion du risque, puis documenter le ratio de couverture et le test d’efficacité."
  ]
}
