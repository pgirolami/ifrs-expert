{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré et comptabilisé à recevoir constitue un poste monétaire intragroupe comptabilisé, libellé en devise.",
    "Les écarts de change sur ce poste monétaire intragroupe ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
    "La relation proposée satisferait par ailleurs aux exigences générales d'IFRS 9 en matière de désignation, de documentation et d'efficacité."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "En consolidation, IFRS 9 permet de désigner le risque de change d'un poste monétaire intragroupe comme élément couvert lorsque les écarts de change ne sont pas totalement éliminés. Sous les hypothèses données, la documentation est donc possible, en couverture de juste valeur ou en couverture de flux de trésorerie."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui",
      "reasoning_fr": "La question vise une créance de dividende intragroupe déjà comptabilisée à recevoir, et l'hypothèse la qualifie de poste monétaire intragroupe en devise. IFRS 9 prévoit qu'en consolidation le risque de change d'un tel poste peut être un élément couvert, dès lors que les écarts de change ne sont pas totalement éliminés, ce qui est précisément supposé ici. Comme les exigences générales de désignation, documentation et efficacité sont aussi supposées remplies, cette voie s'applique au stade actuel de reconnaissance.",
      "conditions_fr": [],
      "practical_implication_fr": "La documentation de couverture peut viser la créance de dividende déjà comptabilisée comme élément couvert du risque de change en consolidation selon un modèle de couverture de juste valeur.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui",
      "reasoning_fr": "IFRS 9 autorise aussi une couverture de flux de trésorerie pour un actif ou passif comptabilisé exposé à une variabilité de flux liée à un risque particulier. Dans le fact pattern retenu, la créance de dividende intragroupe en devise est déjà comptabilisée, les écarts de change aff ectent le résultat consolidé selon les hypothèses, et les critères généraux de documentation et d'efficacité sont supposés satisfaits. Cette désignation reste donc compatible avec la situation telle qu'elle est décrite, sans devoir revenir à un stade antérieur.",
      "conditions_fr": [],
      "practical_implication_fr": "La documentation peut cibler la variabilité des flux en monnaie fonctionnelle liée au risque de change de la créance de dividende intragroupe.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être établie à l'inception de la relation de couverture et identifier l'instrument de couverture, la créance de dividende, le risque de change couvert et le test d'efficacité.",
    "Le point clé en consolidation est l'application de l'exception relative au poste monétaire intragroupe: les écarts de change doivent ne pas être totalement éliminés et affecter le résultat consolidé.",
    "Le choix entre couverture de juste valeur et couverture de flux de trésorerie doit rester cohérent avec l'objectif de gestion du risque retenu pour cette créance intragroupe déjà comptabilisée."
  ]
}
