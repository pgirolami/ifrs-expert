{
  "assumptions_fr": [
    "La créance de dividende intragroupe déjà comptabilisée est supposée être un poste monétaire libellé de sorte qu'il génère des écarts de change non intégralement éliminés en consolidation.",
    "La question vise le hedge accounting dans les comptes consolidés selon IFRS 9 pour la composante risque de change de cette créance reconnue."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en principe, car IFRS 9 6.3.6 ouvre une exception pour le risque de change d'un poste monétaire intragroupe dans les comptes consolidés. En revanche, la désignation ne fonctionne que si la créance remplit bien cette exception et si la relation de couverture est formellement documentée et efficace selon 6.4.1."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur de la créance intragroupe reconnue",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, la créance de dividende est déjà comptabilisée et, selon les hypothèses, constitue un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. À ce stade de reconnaissance, l'exception de 6.3.6 peut rendre l'item éligible et la voie fair value hedge répond bien à un actif reconnu exposé à un risque particulier affectant le résultat, sous réserve de la désignation et des tests d'efficacité de 6.4.1.",
      "conditions_fr": [
        "La créance de dividende doit bien être un poste monétaire intragroupe dont les écarts de change ne sont pas intégralement éliminés en consolidation.",
        "La relation de couverture doit être formellement désignée et documentée à l'inception de la relation.",
        "La relation doit satisfaire aux critères d'efficacité d'IFRS 9, notamment relation économique, risque de crédit non dominant et hedge ratio cohérent."
      ],
      "practical_implication_fr": "Il faut documenter dès l'inception de la relation la créance comme item couvert pour son risque de change et suivre l'inefficacité de couverture en consolidation.",
      "references": [
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
      "label_fr": "Couverture de flux de trésorerie de la créance intragroupe reconnue",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le fait que la créance soit déjà reconnue n'exclut pas cette voie, car 6.5.2(b) vise aussi un actif ou passif reconnu, et non seulement une transaction prévue. Dans les hypothèses retenues, la créance de dividende relève de l'exception de 6.3.6 ; un cash flow hedge est donc envisageable pour la variabilité des flux en monnaie fonctionnelle due au change, à condition que la désignation et l'efficacité de 6.4.1 soient démontrées.",
      "conditions_fr": [
        "L'exposition désignée doit être la variabilité des flux de trésorerie en monnaie fonctionnelle liée au risque de change sur la créance reconnue.",
        "La créance doit relever de l'exception de 6.3.6, c'est-à-dire générer des écarts de change non intégralement éliminés en consolidation.",
        "La relation doit être formellement désignée et documentée à l'inception et satisfaire aux critères d'efficacité d'IFRS 9."
      ],
      "practical_implication_fr": "Il faut bâtir une documentation de cash flow hedge centrée sur l'encaissement futur en devise de la créance et contrôler l'efficacité de la couverture en consolidation.",
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
    "Le bon cadre d'analyse est celui d'une créance intragroupe déjà comptabilisée ; il ne faut pas revenir au stade antérieur de transaction simplement prévue.",
    "En consolidation, la règle générale d'inéligibilité des transactions intragroupe est tempérée par l'exception spécifique de 6.3.6 pour le risque de change des postes monétaires intragroupe.",
    "La documentation doit être établie à l'inception de la relation de couverture et identifier l'instrument de couverture, l'item couvert, le risque couvert et la méthode d'évaluation de l'efficacité.",
    "Le point probant central sera de démontrer que les écarts de change de la créance de dividende affectent bien le résultat consolidé et ne sont pas totalement éliminés."
  ]
}
