{
  "assumptions_fr": [
    "Le dividende intragroupe a été déclaré et un receivable/payable en devise a été comptabilisé ; l’élément potentiellement couvert est donc un poste monétaire intragroupe déjà reconnu.",
    "Les entités du groupe concernées ont des monnaies fonctionnelles différentes ; les écarts de change correspondants ne sont donc pas entièrement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans cette situation, l’exception IFRS 9 pour le risque de change d’un poste monétaire intragroupe en consolidation peut s’appliquer. La variation de change sur le receivable de dividende est donc désignable en comptabilité de couverture, sous réserve de la documentation et des critères d’efficacité d’IFRS 9.6.4.1."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende a déjà donné lieu à un receivable intragroupe reconnu ; il s’agit donc d’un actif reconnu et d’un poste monétaire intragroupe. En consolidation, l’exception de 6.3.6 permet la désignation du risque de change si les écarts de change ne sont pas totalement éliminés et affectent le résultat, ce qui cadre avec 6.5.2(a).",
      "conditions_fr": [
        "Le receivable de dividende est un poste monétaire intragroupe reconnu.",
        "Le risque désigné est le seul risque de change.",
        "Les écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
        "La désignation et la documentation formelles prévues par IFRS 9.6.4.1 sont en place."
      ],
      "practical_implication_fr": "La couverture viserait la réévaluation de change du receivable intragroupe à compter de sa comptabilisation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... that could affect profit or loss"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le receivable de dividende est un actif reconnu en devise ; jusqu’au règlement, ses encaissements en monnaie fonctionnelle varient avec le change. Comme 6.3.6 admet le risque de change d’un poste monétaire intragroupe en consolidation sous les hypothèses retenues, une désignation sous le modèle de 6.5.2(b) est également envisageable.",
      "conditions_fr": [
        "Le receivable reste exposé à une variabilité de change jusqu’au règlement.",
        "Cette variabilité peut affecter le résultat consolidé.",
        "Le poste monétaire intragroupe et le risque couvert sont clairement désignés.",
        "Les exigences de documentation et d’efficacité d’IFRS 9.6.4.1 sont respectées."
      ],
      "practical_implication_fr": "La couverture viserait la variabilité des flux de règlement du receivable exprimés dans la monnaie fonctionnelle pertinente.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of ... a recognised asset or liability ... and could affect profit or loss"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point de départ pertinent est la date de constatation du receivable de dividende ; avant cette date, il ne s’agit pas du même objet comptable.",
    "Il faut documenter dès l’origine la relation de couverture, l’instrument de couverture, l’élément couvert, le risque de change visé et le hedge ratio selon IFRS 9.6.4.1.",
    "La condition clé à démontrer en consolidation est que les écarts de change sur le poste monétaire intragroupe ne soient pas totalement éliminés et affectent bien le résultat consolidé."
  ]
}
