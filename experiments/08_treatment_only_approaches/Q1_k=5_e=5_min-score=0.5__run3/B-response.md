{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a créé une créance et une dette monétaires reconnues entre des entités du groupe.",
    "Cette créance ou dette est exposée à un risque de change qui n’est pas totalement éliminé en consolidation, car les entités concernées ont des monnaies fonctionnelles différentes et l’effet de change peut affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans cette situation, IFRS 9 permet par exception en consolidation de désigner le risque de change d’un poste monétaire intragroupe. La documentation de couverture n’est possible que si les écarts de change subsistent en consolidation et si les exigences formelles de désignation, documentation et efficacité sont respectées."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "En consolidation, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Ici, la créance de dividende est supposée être une créance monétaire reconnue dont le change peut affecter le résultat consolidé ; une fair value hedge peut donc être documentée si la relation est formellement désignée et reste efficace.",
      "conditions_fr": [
        "La créance de dividende doit être un poste monétaire intragroupe reconnu.",
        "Les écarts de change doivent ne pas être totalement éliminés en consolidation et pouvoir affecter le résultat consolidé.",
        "La relation doit être désignée et documentée dès l’origine, avec identification du risque couvert, du hedge ratio et de la méthode d’évaluation de l’efficacité."
      ],
      "practical_implication_fr": "La couverture vise en consolidation la variation de valeur liée au change de la créance intragroupe déjà comptabilisée.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.6",
          "excerpt": "if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
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
      "reasoning_fr": "La même exception de consolidation permet de désigner le risque de change de cette créance intragroupe reconnue si ses effets ne disparaissent pas en consolidation. IFRS 9 admet aussi une cash flow hedge sur un actif ou passif reconnu ; dans cette situation, cela n’est possible que si la documentation vise bien la variabilité des flux en monnaie fonctionnelle liée au change et si les critères d’efficacité sont satisfaits.",
      "conditions_fr": [
        "La créance de dividende doit être un poste monétaire intragroupe reconnu exposé à un risque de change résiduel en consolidation.",
        "Le risque couvert doit être défini comme une variabilité de flux pouvant affecter le résultat consolidé.",
        "La relation doit être désignée et documentée dès l’origine, avec démonstration de la relation économique, de l’absence de domination du risque de crédit et d’un hedge ratio approprié."
      ],
      "practical_implication_fr": "La documentation doit cadrer la variabilité des flux en monnaie fonctionnelle de la créance de dividende due au change.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.6",
          "excerpt": "if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is an economic relationship between the hedged item and the hedging instrument"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedge ratio of the hedging relationship is the same as that resulting from the quantity of the hedged item"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier en premier lieu que l’écart de change sur la créance ou dette de dividende n’est pas intégralement éliminé en consolidation ; sinon l’exception IFRS 9 ne s’applique pas.",
    "Documenter dès l’inception l’instrument de couverture, la créance de dividende couverte, le risque de change visé, le hedge ratio et la méthode d’évaluation de l’efficacité.",
    "Limiter l’élément couvert au risque de change du poste monétaire intragroupe reconnu, et non au dividende intragroupe en tant que distribution en lui-même.",
    "En pratique, pour une créance déjà comptabilisée, la couverture de juste valeur est le cadrage le plus direct ; la couverture de flux reste possible si la variabilité des flux due au change est explicitement documentée."
  ]
}
