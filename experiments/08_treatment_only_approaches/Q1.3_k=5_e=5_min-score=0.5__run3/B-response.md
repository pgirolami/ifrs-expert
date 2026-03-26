{
  "assumptions_fr": [
    "Le dividende intragroupe a été déclaré et a créé une créance et une dette monétaires en devise entre des entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, la règle générale d’exclusion des éléments intragroupe est écartée ici par l’exception relative au risque de change d’un élément monétaire intragroupe dont les écarts ne sont pas totalement éliminés.\nLa relation doit aussi être formellement désignée, documentée à l’origine et satisfaire aux critères d’efficacité d’IFRS 9.\nSelon le risque formellement désigné, un fair value hedge ou un cash flow hedge peut être envisagé."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende intragroupe déjà comptabilisée est un actif monétaire reconnu.\nMême si la règle générale exclut les éléments intragroupe en consolidation, l’exception d’IFRS 9 vise précisément le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés, ce qui est l’hypothèse retenue.\nLa désignation n’est possible que si la relation est documentée dès l’origine et respecte les critères d’efficacité.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe reconnu dans des monnaies fonctionnelles différentes.",
        "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.",
        "La relation de couverture est formellement désignée et documentée à l’origine.",
        "Une relation économique, un hedge ratio approprié et l’absence de domination du risque de crédit sont démontrés."
      ],
      "practical_implication_fr": "En consolidation, le risque de change sur la créance de dividende peut être documenté comme élément couvert dans un modèle de fair value hedge.",
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
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende intragroupe est un actif reconnu dont le montant encaissé en monnaie fonctionnelle/consolidée varie avec le cours de change jusqu’au règlement.\nL’exception d’IFRS 9 relative aux éléments monétaires intragroupe permet ici l’éligibilité en consolidation, puisque l’hypothèse retient des écarts de change non totalement éliminés.\nCette voie suppose toutefois que l’objectif documenté porte bien sur la variabilité des flux et que les tests d’efficacité soient satisfaits.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe reconnu et exposé au change jusqu’au règlement.",
        "Les écarts de change affectent encore le résultat consolidé car ils ne sont pas totalement éliminés.",
        "La documentation initiale identifie la variabilité des flux liée au risque de change comme risque couvert.",
        "Les exigences de désignation, de hedge ratio et d’efficacité de l’article 6.4.1 sont respectées."
      ],
      "practical_implication_fr": "La documentation doit viser la variabilité du flux de règlement en devise de la créance de dividende jusqu’à son encaissement.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "the documentation shall include identification of the hedging instrument, the hedged item, the nature of the risk being hedged"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La désignation doit être faite à l’origine de la relation et identifier la créance de dividende, le risque de change couvert, l’instrument de couverture et le hedge ratio.",
    "Il faut documenter que la créance/dette de dividende constitue bien un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes et que les écarts de change ne sont pas totalement éliminés en consolidation.",
    "Le modèle retenu doit être cohérent avec l’objectif de gestion documenté : exposition de valeur pour le fair value hedge ou variabilité du règlement pour le cash flow hedge."
  ]
}
