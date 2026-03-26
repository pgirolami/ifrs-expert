{
  "assumptions_fr": [
    "La créance/dette de dividende intragroupe est un élément monétaire libellé dans une devise générant une exposition de change entre entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "Les exigences générales d’IFRS 9 en matière de désignation, de documentation et d’efficacité de la couverture peuvent être respectées."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, IFRS 9 admet par exception le risque de change d’un élément monétaire intragroupe comme élément couvert lorsque les écarts de change ne sont pas totalement éliminés. Une créance de dividende reconnue peut donc servir de base à une documentation de couverture, sous réserve du modèle retenu et d’une documentation formelle à l’inception."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende déjà comptabilisée est un élément monétaire intragroupe ; l’exception IFRS 9 permet en consolidation de couvrir son risque de change si les écarts de change ne sont pas totalement éliminés.\nLa relation peut donc être documentée comme une couverture de juste valeur de la composante change, à condition que la désignation initiale, la documentation et l’efficacité requises par IFRS 9 soient satisfaites.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe en devise.",
        "Les écarts de change correspondants affectent le résultat consolidé et ne sont pas totalement éliminés.",
        "La composante change est désignée formellement dès l’inception avec documentation et test d’efficacité."
      ],
      "practical_implication_fr": "Le dossier de couverture doit viser la variation de valeur de la créance attribuable au change au niveau consolidé.",
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
          "section": "6.3.7",
          "excerpt": "an entity may designate ... only changes ... attributable to a specific risk"
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
      "reasoning_fr": "Dans cette situation, la créance reconnue est aussi un actif reconnu dont les flux d’encaissement en monnaie fonctionnelle varient avec le change ; IFRS 9 permet le modèle de cash flow hedge pour un actif reconnu, et l’exception intragroupe couvre le risque de change d’un élément monétaire intragroupe.\nCe traitement n’est donc possible que si le risque couvert est bien la variabilité des flux liée au change et si cette exposition affecte le résultat consolidé.",
      "conditions_fr": [
        "La couverture vise la variabilité des flux d’encaissement liée au change sur la créance reconnue.",
        "Le risque de change de l’élément monétaire intragroupe affecte le résultat consolidé.",
        "La relation est désignée et documentée à l’inception avec démonstration de l’efficacité."
      ],
      "practical_implication_fr": "La documentation doit décrire la composante change des flux de règlement de la créance comme risque couvert au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
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
    "La documentation doit être mise en place à l’inception de la relation de couverture ; une désignation rétroactive n’est pas conforme au critère de documentation initiale.",
    "Le point clé en consolidation est de démontrer que les écarts de change sur la créance/dette intragroupe ne sont pas totalement éliminés et affectent bien le résultat consolidé.",
    "La composante change peut être isolée comme risque couvert, mais le modèle retenu doit être cohérent avec le risque effectivement géré : variation de valeur ou variabilité de flux.",
    "Le dossier doit identifier l’instrument de couverture, l’élément couvert, le risque de change visé, le hedge ratio et la méthode d’appréciation de l’efficacité."
  ]
}
