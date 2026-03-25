{
  "assumptions_fr": [
    "Le dividende intragroupe a été déclaré et une créance/dette correspondante a été comptabilisée ; il s'agit donc d'un élément monétaire intragroupe reconnu.",
    "La créance/dette est libellée dans une devise qui crée un risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change correspondants ne sont pas intégralement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions.\nDans cette situation, l'exception IFRS 9 pour le risque de change d'un élément monétaire intragroupe peut s'appliquer en consolidation si les écarts de change affectent le résultat consolidé. La relation doit ensuite être formellement désignée, documentée et satisfaire aux critères d'efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende intragroupe déclaré a créé une créance/dette monétaire comptabilisée.\nEn consolidation, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d'un élément monétaire intragroupe s'il génère des écarts non totalement éliminés.\nCe traitement peut donc s'appliquer ici comme fair value hedge, sous réserve de la désignation, de la documentation et des tests d'efficacité.",
      "conditions_fr": [
        "La créance/dette de dividende intragroupe est un élément monétaire comptabilisé.",
        "Le risque de change génère des écarts non intégralement éliminés en consolidation.",
        "La relation de couverture est désignée et documentée dès l'origine.",
        "Les critères d'efficacité de la couverture sont respectés, y compris le hedge ratio."
      ],
      "practical_implication_fr": "Le dossier de couverture vise le poste monétaire intragroupe reconnu et son risque de change en résultat consolidé.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
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
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, l'exposition porte aussi sur le flux de règlement futur du dividende intragroupe déjà reconnu.\nIFRS 9 permet un cash flow hedge pour la variabilité des flux d'un actif ou passif comptabilisé, et l'exception relative à l'élément monétaire intragroupe reste nécessaire en consolidation.\nCe traitement peut donc aussi s'appliquer ici, si la variabilité de change du règlement affecte le résultat consolidé et si la relation est correctement documentée.",
      "conditions_fr": [
        "L'exposition désignée est la variabilité des flux de règlement liée au change sur le poste reconnu.",
        "Le poste reste un élément monétaire intragroupe dont les écarts de change affectent le résultat consolidé.",
        "La relation de couverture est désignée et documentée dès l'origine.",
        "Les critères d'efficacité de la couverture sont respectés, y compris le hedge ratio."
      ],
      "practical_implication_fr": "Le dossier de couverture vise le règlement futur du dividende intragroupe reconnu et sa variabilité de change.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        },
        {
          "section": "6.4.1(c)",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La désignation doit intervenir à partir du moment où la créance/dette de dividende est reconnue, avec documentation formelle dès l'inception de la relation de couverture.",
    "Le point décisif en consolidation est de démontrer que les écarts de change du poste intragroupe ne sont pas totalement éliminés et affectent le résultat consolidé.",
    "Le choix entre fair value hedge et cash flow hedge doit être cohérent avec l'exposition effectivement désignée dans la documentation.",
    "La documentation doit identifier l'instrument de couverture, l'élément couvert, le risque de change couvert, le hedge ratio et les sources d'inefficacité."
  ]
}
