{
  "assumptions_fr": [
    "L'analyse est menée dans les états financiers consolidés, puisque la créance naît à l'intérieur du périmètre de consolidation.",
    "Le dividende déclaré a créé une créance intragroupe monétaire libellée en devise; les indications d'IFRS 9 sur les éléments couverts intragroupe en monnaie étrangère sont donc pertinentes."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous réserve que la créance de dividende soit un élément monétaire intragroupe en devise dont les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. Sur ces faits, les deux modèles peuvent être envisagés, avec un ancrage plus direct pour la couverture de juste valeur."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende déclaré a déjà créé une créance intragroupe reconnue; on est donc face à un actif monétaire existant, non à une transaction future. En consolidation, l'exception de 6.3.6 permet de désigner le risque de change d'un tel élément si les écarts ne sont pas totalement éliminés et affectent le résultat consolidé; dans ce cas, une couverture de juste valeur de cette créance peut être documentée.",
      "conditions_fr": [
        "la créance de dividende et la dette correspondante constituent un élément monétaire intragroupe",
        "la créance est libellée dans une devise créant des écarts de change non totalement éliminés en consolidation",
        "ces écarts de change affectent le résultat consolidé"
      ],
      "practical_implication_fr": "La documentation peut viser la créance de dividende reconnue comme item couvert pour son risque de change jusqu'au règlement.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
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
      "reasoning_fr": "Le fait que le dividende soit déjà déclaré n'empêche pas, d'après 6.5.2(b), qu'un actif reconnu serve de support à un cash flow hedge. Dans cette situation, ce modèle n'est recevable que si l'exposition documentée est la variabilité, en monnaie fonctionnelle, de l'encaissement futur sur la créance intragroupe et si les écarts de change affectent le résultat consolidé.",
      "conditions_fr": [
        "la créance de dividende donne lieu à un encaissement futur en monnaie fonctionnelle exposé au change jusqu'au règlement",
        "la créance est un élément monétaire intragroupe en devise dont les écarts de change ne sont pas totalement éliminés en consolidation",
        "ces écarts de change affectent le résultat consolidé"
      ],
      "practical_implication_fr": "La documentation doit alors cibler la variabilité des encaissements futurs sur la créance de dividende jusqu'à son règlement.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d'abord que la créance de dividende est bien un élément monétaire intragroupe libellé dans une devise différente de la monnaie fonctionnelle pertinente; sinon l'exception de 6.3.6 ne s'ouvre pas.",
    "La documentation doit être établie dès l'origine de la relation de couverture, avec identification de l'instrument, de la créance couverte, du risque de change et du hedge ratio.",
    "En pratique, il faut choisir un seul récit de risque cohérent avec la gestion: variation de valeur de la créance reconnue (juste valeur) ou variabilité de l'encaissement en monnaie fonctionnelle (flux de trésorerie)."
  ]
}
