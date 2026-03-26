{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà été déclaré et comptabilisé en créance/dette ; l'exposition est donc un poste monétaire intragroupe reconnu, et non une simple transaction future.",
    "La créance/dette est libellée dans une devise qui crée une exposition de change entre entités du groupe ayant des monnaies fonctionnelles différentes."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en consolidation, si le dividende intragroupe déjà comptabilisé constitue un poste monétaire intragroupe exposé à des écarts de change non totalement éliminés. Dans ce cas, le modèle pertinent est la couverture de juste valeur ; la couverture de flux de trésorerie ne correspond pas au fait pattern décrit."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende déjà comptabilisé à recevoir relève, sous les hypothèses posées, d'un poste monétaire intragroupe reconnu. IFRS 9 prévoit en consolidation une exception pour le risque de change d'un tel poste lorsqu'il génère des écarts non totalement éliminés ; le modèle de juste valeur est celui qui correspond à une créance reconnue affectant le résultat.",
      "conditions_fr": [
        "La créance de dividende doit être un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "Documenter dès l'origine la créance couverte, l'instrument de couverture, le risque de change visé et la méthode d'appréciation de l'efficacité.",
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
      "applicability": "non",
      "reasoning_fr": "Ici, le fait générateur est un dividende déjà déclaré et comptabilisé en créance ; l'exposition porte donc sur la réévaluation de change d'un poste monétaire existant. Le contexte fourni pour la cash flow hedge vise la variabilité de flux de trésorerie ; ce n'est pas le traitement le plus adapté à un dividende intragroupe déjà reconnu.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter ce cas comme une couverture de flux de trésorerie du seul fait que l'encaissement interviendra ultérieurement.",
      "references": [
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier en consolidation que les entités concernées ont des monnaies fonctionnelles différentes et que les écarts de change sur la créance/dette ne sont pas totalement éliminés.",
    "Mettre en place la documentation à l'inception de la relation de couverture, avec identification du poste couvert, du risque de change, du ratio de couverture et des sources d'inefficacité.",
    "L'analyse ci-dessus repose sur un dividende intragroupe déjà comptabilisé à recevoir ; si le dividende n'était que prévu, l'analyse IFRS serait différente."
  ]
}
