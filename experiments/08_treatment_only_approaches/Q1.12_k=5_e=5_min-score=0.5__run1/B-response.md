{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a déjà créé une créance et une dette comptabilisées, et il est analysé comme un élément monétaire intragroupe reconnu.",
    "Les entités concernées ont des monnaies fonctionnelles différentes et ce dividende génère des écarts de change non totalement éliminés en consolidation, susceptibles d'affecter le résultat consolidé.",
    "L'analyse est limitée aux modèles de comptabilité de couverture couverts par les extraits fournis d'IFRS 9 et d'IFRIC 16."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Au niveau consolidé, IFRS 9 pose une interdiction de principe pour les postes intragroupe, mais prévoit une exception pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. La qualification formelle est donc possible ici, sous réserve de désignation, documentation et efficacité conformes à IFRS 9."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende intragroupe est un actif reconnu.\nAu consolidé, IFRS 9 l'exclut en principe car il s'agit d'un poste intragroupe, mais l'exception vise précisément le risque de change d'un élément monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés et affectent le résultat consolidé.\nDès lors, une désignation en couverture de juste valeur est formellement envisageable ici, sous réserve de documentation initiale et du respect des critères d'efficacité.",
      "conditions_fr": [
        "La créance de dividende doit bien être traitée comme un élément monétaire intragroupe reconnu.",
        "Le risque de change doit générer des écarts non totalement éliminés en consolidation et affecter le résultat consolidé.",
        "La relation de couverture doit être désignée et documentée dès l'origine, avec un ratio de couverture conforme."
      ],
      "practical_implication_fr": "Une qualification formelle au consolidé est défendable, mais elle exige un dossier de désignation IFRS 9 complet dès l'inception.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items."
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
      "reasoning_fr": "Dans cette situation, la même créance reconnue peut aussi être analysée au titre de la variabilité des flux en monnaie fonctionnelle jusqu'au règlement du dividende.\nL'exception d'IFRS 9 pour le risque de change d'un élément monétaire intragroupe au consolidé rend ce poste éligible si les écarts de change affectent le résultat consolidé, comme supposé ici.\nUne couverture de flux de trésorerie est donc également possible, à condition d'être formellement documentée et de satisfaire aux critères de qualification d'IFRS 9.",
      "conditions_fr": [
        "Le dividende comptabilisé doit exposer le groupe à une variabilité de flux liée au change jusqu'au règlement.",
        "Le risque de change doit affecter le résultat consolidé et ne pas être totalement éliminé à la consolidation.",
        "La documentation de couverture doit identifier l'instrument, l'élément couvert, le risque couvert et la méthode d'appréciation de l'efficacité."
      ],
      "practical_implication_fr": "Ce modèle permet de formaliser l'exposition de change jusqu'à l'encaissement du dividende, sous réserve d'une documentation stricte.",
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
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La règle générale au consolidé vise des postes avec des tiers externes; il faut donc documenter explicitement l'application de l'exception IFRS 9 pour l'élément monétaire intragroupe.",
    "La désignation doit être faite dès l'origine de la relation de couverture et inclure l'instrument couvert, le poste couvert, le risque de change et le test d'efficacité.",
    "IFRIC 16 ne doit pas être transposé par analogie à ce cas, car il s'applique uniquement aux couvertures d'investissements nets dans des opérations étrangères."
  ]
}
