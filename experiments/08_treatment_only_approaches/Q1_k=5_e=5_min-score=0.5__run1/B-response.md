{
  "assumptions_fr": [
    "La créance de dividende intragroupe et la dette correspondante sont libellées dans une devise créant une exposition de change entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "La créance/dette de dividende est un poste monétaire intragroupe reconnu et les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans cette situation, un poste intragroupe serait en principe exclu en consolidation, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe non totalement éliminé. Une documentation de couverture est donc possible si la relation est formellement désignée et remplit les critères d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, la créance de dividende déjà comptabilisée est un actif reconnu, ce qui correspond au champ de la couverture de juste valeur.\nEn consolidation, cela n’est possible que parce que, selon les hypothèses, il s’agit d’un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé ; il faut en plus la documentation formelle et les critères d’efficacité IFRS 9.",
      "conditions_fr": [
        "La créance de dividende est un poste monétaire intragroupe reconnu.",
        "Les écarts de change afférents affectent le résultat consolidé car ils ne sont pas totalement éliminés.",
        "La relation de couverture est désignée et documentée à l’origine.",
        "Il existe une relation économique et un ratio de couverture conforme à IFRS 9."
      ],
      "practical_implication_fr": "Vous pouvez documenter en consolidation la couverture du risque de change de la créance intragroupe, sous réserve de satisfaire l’exception intragroupe et les critères de qualification.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende reconnue génère un encaissement futur en devise, dont la contre-valeur varie avec le change ; IFRS 9 admet une couverture de flux sur un actif reconnu.\nEn consolidation, cette désignation reste conditionnée au fait que le poste soit un poste monétaire intragroupe avec un risque de change non totalement éliminé, ainsi qu’au respect des exigences de documentation et d’efficacité.",
      "conditions_fr": [
        "La variabilité de l’encaissement en monnaie fonctionnelle provient du risque de change sur la créance reconnue.",
        "Le poste intragroupe est monétaire et son risque de change affecte le résultat consolidé.",
        "La désignation et la documentation sont établies dès l’origine de la relation.",
        "Les critères d’efficacité de la couverture sont satisfaits."
      ],
      "practical_implication_fr": "Vous pouvez aussi documenter une couverture des flux de change liés au règlement futur de la créance, si les conditions intragroupe et de qualification sont remplies.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point clé en consolidation n’est pas le caractère intragroupe du dividende en soi, mais le fait que la créance/dette soit un poste monétaire dont le change n’est pas totalement éliminé.",
    "La documentation doit être mise en place à l’origine de la relation de couverture, avec identification de l’instrument, du poste couvert, du risque de change et du test d’efficacité.",
    "Dans votre cas, l’analyse doit porter sur la créance de dividende déjà comptabilisée ; la logique des transactions intragroupe futures hautement probables n’est pas la base principale ici.",
    "Le choix entre couverture de juste valeur et couverture de flux doit rester cohérent avec le risque effectivement désigné sur la créance de dividende en consolidation."
  ]
}
