{
  "assumptions_fr": [
    "Le dividende intragroupe comptabilisé à recevoir/à payer est traité comme un élément monétaire intragroupe pour apprécier l'exception d'IFRS 9 relative aux éléments monétaires.",
    "L'analyse vise des états financiers consolidés ordinaires, hors scénario particulier d'entité d'investissement mentionné au paragraphe 6.3.5 d'IFRS 9."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, la règle générale exclut les éléments intragroupe comme éléments couverts. Sous l'hypothèse retenue d'un dividende intragroupe déjà comptabilisé comme élément monétaire, une documentation de couverture n'est possible qu'au titre de l'exception de 6.3.6 si le risque de change n'est pas entièrement éliminé en consolidation et si les critères de 6.4.1 sont respectés."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_hedge_prohibition",
      "label_fr": "Interdiction générale des couvertures intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La question porte sur des états financiers consolidés et, selon l'hypothèse, hors cas particulier d'entité d'investissement. À ce stade où le dividende intragroupe est déjà comptabilisé à recevoir, la règle de base de 6.3.5 interdit la désignation d'un élément intragroupe comme élément couvert en consolidation.\nCette approche commande la réponse si les faits ne permettent pas d'ouvrir l'exception spécifique de 6.3.6.",
      "conditions_fr": [
        "Les écarts de change liés au dividende intragroupe sont entièrement éliminés en consolidation, de sorte que l'exception de 6.3.6 ne peut pas être utilisée."
      ],
      "practical_implication_fr": "À défaut de démontrer une exposition de change résiduelle au niveau consolidé, la documentation de couverture doit être écartée.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Exception pour élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Compte tenu de l'hypothèse explicite, le dividende intragroupe déjà comptabilisé à recevoir est analysé comme un élément monétaire intragroupe, ce qui correspond au timing visé par 6.3.6. En consolidation, la relation peut être documentée seulement si ce poste crée des gains ou pertes de change qui ne sont pas entièrement éliminés à la consolidation.\nIl faut en outre, sans modifier les faits, satisfaire à l'inception de la relation aux exigences de désignation, documentation et efficacité prévues par 6.4.1.",
      "conditions_fr": [
        "Le dividende intragroupe comptabilisé à recevoir génère des écarts de change qui ne sont pas entièrement éliminés en consolidation.",
        "La relation est formellement désignée et documentée à l'inception, avec identification de l'instrument, de l'élément couvert, du risque de change et du ratio de couverture.",
        "Les exigences d'efficacité de la couverture sont satisfaites."
      ],
      "practical_implication_fr": "La documentation est possible en consolidation, mais uniquement sur le risque de change résiduel du poste monétaire intragroupe et avec un dossier IFRS 9 complet.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "separate_statement_hedge",
      "label_fr": "Couverture en comptes individuels ou séparés",
      "applicability": "non",
      "reasoning_fr": "La question vise expressément la consolidation IFRS. Or 6.3.5 précise que les transactions intragroupe ne peuvent être couvertes que dans les états financiers individuels ou séparés des entités concernées, ce qui suppose un autre périmètre comptable.\nCette approche demanderait donc de changer le référentiel de la situation posée et n'est pas applicable ici.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette voie n'apporte pas de fondement à une documentation de couverture dans les comptes consolidés.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "Le modèle de couverture d'un investissement net concerne les actifs nets d'une opération étrangère, alors que la question porte sur un dividende intragroupe déjà comptabilisé à recevoir. IFRIC 16 précise en outre que cette interprétation ne doit pas être appliquée par analogie à d'autres types de couverture.\nL'utiliser ici reviendrait à reformuler l'élément couvert et à changer les faits de départ.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas requalifier le dividende intragroupe en couverture d'investissement net pour documenter la relation.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations; it should not be applied by analogy to other types of hedge accounting."
        },
        {
          "section": "14",
          "excerpt": "may be designated as a hedging instrument in a hedge of a net investment in a foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le test pertinent se fait au stade actuel d'un dividende déjà comptabilisé à recevoir; il ne faut pas le requalifier en transaction future pour ouvrir une autre voie.",
    "En consolidation, il faut démontrer et documenter pourquoi les écarts de change sur ce poste monétaire intragroupe ne sont pas entièrement éliminés.",
    "La documentation d'inception doit couvrir l'instrument de couverture, l'élément couvert, le risque de change, le ratio de couverture et les sources d'inefficacité.",
    "Si cette démonstration de risque résiduel échoue, la règle générale de 6.3.5 reprend le dessus et la relation ne peut pas être documentée en consolidation."
  ]
}
