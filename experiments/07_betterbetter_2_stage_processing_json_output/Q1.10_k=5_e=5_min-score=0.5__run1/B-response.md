{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a créé une créance/dette monétaire déjà comptabilisée, libellée dans une devise qui génère une exposition de change entre entités du groupe ayant des monnaies fonctionnelles différentes."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, la règle générale exige une contrepartie externe, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe. Une relation de couverture sur des dividendes intragroupe comptabilisés à recevoir peut donc être documentée, sous réserve que le risque de change survive à la consolidation et que les critères de désignation, documentation et efficacité soient remplis."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur de la créance intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans la situation décrite, le dividende est déjà comptabilisé à recevoir et, selon l’hypothèse, constitue un poste monétaire intragroupe exposé au change. En consolidation, IFRS 9 exclut en principe les éléments intragroupe, mais l’exception de 6.3.6 permet de désigner le risque de change d’un poste monétaire intragroupe si les écarts de change ne sont pas totalement éliminés. Cette voie reste donc ouverte seulement si la relation est formellement documentée à l’inception et satisfait aux critères d’efficacité de 6.4.1.",
      "conditions_fr": [
        "les écarts de change sur la créance/dette de dividende intragroupe ne sont pas totalement éliminés en consolidation",
        "la relation est désignée et documentée à l’inception avec identification de l’instrument, de l’élément couvert, du risque couvert et du ratio de couverture",
        "la relation satisfait aux critères d’efficacité de l’IFRS 9, notamment relation économique, effet du risque de crédit non dominant et ratio cohérent"
      ],
      "practical_implication_fr": "Le groupe peut documenter une couverture de juste valeur en consolidation sur la créance de dividende, avec suivi de l’inefficacité et dossier de couverture complet dès l’origine.",
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
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie de la créance intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le fait pattern porte sur une créance de dividende déjà reconnue ; IFRS 9 admet aussi un cash flow hedge d’un risque associé à un actif reconnu. Comme il s’agit ici, selon l’hypothèse, d’un poste monétaire intragroupe en devise, l’éligibilité en consolidation dépend d’abord de l’exception de 6.3.6, puis de la documentation et des tests de 6.4.1. Cette approche n’est donc recevable que si la variabilité de flux en monnaie fonctionnelle liée au change est bien celle couverte dans la relation documentée.",
      "conditions_fr": [
        "les écarts de change sur la créance/dette de dividende intragroupe ne sont pas totalement éliminés en consolidation",
        "la documentation de couverture vise explicitement la variabilité des flux liée au risque de change sur la créance reconnue",
        "la relation est désignée et documentée à l’inception et satisfait aux critères d’efficacité de l’IFRS 9"
      ],
      "practical_implication_fr": "Le groupe peut structurer la documentation comme une couverture de flux de trésorerie, mais devra démontrer précisément la variabilité couverte et en assurer le suivi d’efficacité.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1(c)",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif en consolidation est que la créance de dividende soit un poste monétaire intragroupe dont le risque de change affecte encore le résultat consolidé.",
    "La documentation doit être établie à l’inception de la relation de couverture et décrire l’instrument, l’élément couvert, le risque de change visé et le ratio de couverture.",
    "Le groupe doit choisir un seul modèle de couverture cohérent avec sa gestion du risque et mesurer l’inefficacité pendant toute la durée de la relation."
  ]
}
