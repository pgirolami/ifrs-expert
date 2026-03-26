{
  "assumptions_fr": [
    "La créance et la dette de dividendes intragroupe constituent un élément monétaire intragroupe libellé en devise.",
    "L’exposition de change mentionnée signifie que les écarts de change correspondants ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En principe, un élément intragroupe n’est pas un élément couvert en consolidation, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe. Dans les faits décrits et sous les hypothèses posées, cette exposition peut donc être désignée, sous réserve de la documentation initiale et des critères d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance de dividende intragroupe est, selon les hypothèses, un actif monétaire reconnu en devise.\nIFRS 9 exclut en principe les éléments intragroupe, mais admet en consolidation le risque de change d’un élément monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés.\nDans cette situation, une couverture de juste valeur du risque de change peut donc s’appliquer si la relation est correctement désignée et efficace.",
      "conditions_fr": [
        "La créance est un élément monétaire intragroupe reconnu et libellé en devise.",
        "Les écarts de change sur cet élément ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
        "La relation de couverture est formellement désignée, documentée et satisfait aux critères d’efficacité d’IFRS 9."
      ],
      "practical_implication_fr": "Le groupe peut désigner le risque de change de la créance comme élément couvert dans une relation de fair value hedge, sous réserve du respect des critères IFRS 9.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
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
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La même créance reconnue est aussi un actif reconnu au sens d’IFRS 9 6.5.2(b).\nSi le groupe couvre la variabilité des flux en monnaie fonctionnelle issue du règlement en devise de cette créance, et si cette variabilité affecte le résultat consolidé, le modèle de cash flow hedge est disponible dans ce cas.\nL’application reste toutefois conditionnée par la désignation formelle et la démonstration de l’efficacité de la couverture.",
      "conditions_fr": [
        "La créance est un élément monétaire intragroupe reconnu et libellé en devise.",
        "Le risque couvert est défini comme la variabilité des flux en monnaie fonctionnelle liée au règlement de cette créance.",
        "Cette variabilité de change affecte le résultat consolidé et la relation respecte les critères de désignation, de documentation et d’efficacité d’IFRS 9."
      ],
      "practical_implication_fr": "Le groupe peut aussi structurer la relation comme cash flow hedge des flux de règlement en devise, si c’est bien le risque géré et documenté.",
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
          "excerpt": "there is an economic relationship between the hedged item and the hedging instrument"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter dès l’origine l’élément couvert, l’instrument de couverture, le risque de change couvert et la méthode de test d’efficacité.",
    "Conserver une démonstration que les écarts de change sur la créance de dividende intragroupe ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
    "Choisir un seul modèle cohérent avec l’objectif de gestion du risque : juste valeur si l’on vise la variation de valeur de la créance, cash flow hedge si l’on vise la variabilité des flux de règlement."
  ]
}
