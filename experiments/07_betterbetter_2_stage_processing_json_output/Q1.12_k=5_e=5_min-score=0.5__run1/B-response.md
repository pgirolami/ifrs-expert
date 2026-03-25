{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a déjà donné lieu à une créance et à une dette monétaires comptabilisées.",
    "Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change sur ce poste monétaire intragroupe ne sont pas entièrement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "La relation de couverture serait désignée et documentée dès l’origine et satisferait aux exigences d’efficacité d’IFRS 9."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Au niveau consolidé, IFRS 9 admet par exception qu’un poste monétaire intragroupe exposé à un risque de change résiduel soit un élément couvert. Dans les hypothèses retenues, une formalisation est donc possible, en couverture de juste valeur ou en couverture de flux de trésorerie selon l’objectif de gestion documenté."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Le dividende intragroupe est ici déjà au stade d’une créance monétaire comptabilisée ; l’analyse porte donc sur un actif reconnu, et non sur une transaction future. Compte tenu des hypothèses de monnaies fonctionnelles différentes et d’un impact résiduel en résultat consolidé, l’exception d’IFRS 9 pour les postes monétaires intragroupe rend l’élément éligible ; la désignation et l’efficacité étant supposées satisfaites, une couverture de juste valeur peut être formellement mise en place.",
      "conditions_fr": [],
      "practical_implication_fr": "Il faut documenter la créance de dividende comme élément couvert contre la variation de valeur liée au change et suivre l’efficacité de la relation jusqu’au règlement.",
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
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui",
      "reasoning_fr": "Le même poste reconnu peut aussi être appréhendé sous l’angle de la variabilité des flux en monnaie fonctionnelle au règlement du dividende déjà comptabilisé. Dans les hypothèses données, le risque de change sur ce poste monétaire intragroupe peut affecter le résultat consolidé et, la documentation ainsi que l’efficacité étant supposées remplies au bon moment, la couverture de flux de trésorerie constitue aussi une voie formelle applicable dans cette situation.",
      "conditions_fr": [],
      "practical_implication_fr": "Il faut documenter que le risque couvert est la variabilité des flux du dividende en devise et assurer un suivi d’efficacité cohérent jusqu’au dénouement.",
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
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le sujet porte sur un dividende déjà comptabilisé en créance ; il ne faut donc pas fonder l’analyse sur la règle des transactions intragroupe futures hautement probables.",
    "L’éligibilité en consolidation repose sur le fait que le risque de change du poste monétaire intragroupe n’est pas entièrement éliminé et affecte le résultat consolidé.",
    "Quelle que soit l’option retenue, la désignation initiale, la documentation du risque couvert et l’évaluation de l’efficacité restent indispensables.",
    "En pratique, il faut retenir un seul modèle de couverture cohérent avec l’objectif de gestion documenté pour ce risque donné."
  ]
}
