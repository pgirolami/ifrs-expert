{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà fait naître une créance et une dette intragroupe monétaires reconnues.",
    "La créance et la dette sont libellées de telle sorte que les écarts de change ne sont pas totalement éliminés en consolidation, car les entités concernées ont des monnaies fonctionnelles différentes."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Dans les hypothèses données, le risque de change attaché à la créance/dette de dividende intragroupe peut relever de l’exception d’IFRS 9 pour les éléments monétaires intragroupe en consolidation. La relation doit toutefois être désignée et documentée à son inception et satisfaire aux critères de 6.4.1."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Le dividende intragroupe a déjà généré une créance/dette monétaire reconnue, donc on est bien au stade d’un actif ou passif reconnu visé par IFRS 9 6.5.2(a). Sous l’hypothèse que les écarts de change ne sont pas entièrement éliminés en consolidation, l’exception de 6.3.6 permet de désigner ce risque de change comme élément couvert, à condition de documenter la relation à son inception selon 6.4.1.",
      "conditions_fr": [
        "désigner formellement la relation à l’inception de la couverture",
        "identifier l’instrument de couverture, l’élément couvert et le risque de change couvert",
        "démontrer la relation économique, l’absence de domination du risque de crédit et un hedge ratio conforme"
      ],
      "practical_implication_fr": "Le groupe peut documenter une couverture de juste valeur sur la créance/dette intragroupe reconnue, pour les effets de change couverts à compter de l’inception de la relation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui",
      "reasoning_fr": "Le fait que la créance/dette soit déjà reconnue n’empêche pas une couverture de flux de trésorerie, car IFRS 9 6.5.2(b) vise aussi un actif ou passif reconnu. Dans les hypothèses retenues, le risque de change sur les flux de règlement de cet élément monétaire intragroupe affecte le résultat consolidé et peut donc être documenté en relation de couverture, sous réserve des critères de 6.4.1 et sans requalifier le cas en transaction future.",
      "conditions_fr": [
        "désigner formellement la relation à l’inception de la couverture",
        "documenter l’exposition couverte comme la variabilité des flux de règlement de la créance/dette déjà reconnue",
        "démontrer la relation économique, l’absence de domination du risque de crédit et un hedge ratio conforme"
      ],
      "practical_implication_fr": "Le groupe peut documenter une couverture des flux de règlement en devise de la créance/dette intragroupe déjà comptabilisée, à partir de l’inception de cette relation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "associated with all, or a component of, a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La règle générale de 6.3.5 vise des contreparties externes, mais le cas posé entre dans l’exception spécifique de 6.3.6 pour les éléments monétaires intragroupe.",
    "La documentation doit être établie à l’inception de la relation de couverture ; elle ne couvre pas rétroactivement des effets de change antérieurs.",
    "Le point clé de consolidation est que les écarts de change sur la créance/dette intragroupe ne soient pas totalement éliminés, ce qui découle ici de l’hypothèse de monnaies fonctionnelles différentes."
  ]
}
