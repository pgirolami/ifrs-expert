{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a créé une créance/dette intragroupe libellée en devise étrangère déjà comptabilisée, c’est-à-dire un élément monétaire."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions : pour une créance de dividende intragroupe déjà comptabilisée, IFRS 9 prévoit une exception en consolidation pour le risque de change d’un élément monétaire intragroupe si ce risque génère des écarts non totalement éliminés. Il faut ensuite satisfaire la désignation, la documentation et les tests d’efficacité de la relation de couverture."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du poste intragroupe reconnu",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La question vise une créance de dividende intragroupe déjà comptabilisée; selon l’hypothèse, c’est un actif monétaire reconnu. Dans ce cas précis, l’exception d’IFRS 9 pour le risque de change d’un élément monétaire intragroupe peut s’appliquer en consolidation si les écarts de change ne sont pas entièrement éliminés, puis la relation doit encore être formellement désignée, documentée et efficace.",
      "conditions_fr": [
        "la créance/dette de dividende est entre entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change ne sont pas entièrement éliminés en consolidation",
        "la relation de couverture est formellement désignée et documentée à l’inception, avec identification de l’instrument, du poste couvert, du risque couvert et du hedge ratio",
        "les critères d’efficacité sont respectés : relation économique, risque de crédit non dominant et hedge ratio cohérent"
      ],
      "practical_implication_fr": "Le dossier de hedge accounting doit être monté comme une couverture de change sur un élément monétaire intragroupe reconnu, avec preuve de l’exposition résiduelle en consolidation.",
      "references": [
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
      "normalized_label": "hedge_accounting_ineligibility",
      "label_fr": "Inéligibilité en consolidation",
      "applicability": "non",
      "reasoning_fr": "Cette approche reprend la règle générale selon laquelle les postes intragroupe ne sont pas des éléments couverts en consolidation. Mais, dans le cas exact posé — une créance intragroupe déjà reconnue et supposée monétaire — le contexte prévoit une exception explicite pour le risque de change des éléments monétaires intragroupe; elle ne permet donc pas de conclure correctement à une inéligibilité absolue.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas s’arrêter à l’interdiction générale sans tester l’exception spécifique des éléments monétaires intragroupe.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie d’une transaction intragroupe prévue",
      "applicability": "non",
      "reasoning_fr": "Cette approche viserait le stade antérieur où le dividende n’est pas encore comptabilisé et resterait une transaction future hautement probable. Or la question et l’hypothèse portent sur une créance déjà enregistrée; revenir à une transaction forecast contredirait le timing et le statut de comptabilisation décrits.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette voie n’est pertinente que si la désignation intervient avant la reconnaissance de la créance, ce qui n’est pas le cas ici.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction ... that transaction must be highly probable"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... or a highly probable forecast transaction"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Le fait visé par la question est une créance de dividende intragroupe déjà reconnue, pas un montant de net assets d’une activité étrangère. Le modèle IFRIC 16 est réservé aux hedges de net investment et ne doit pas être étendu par analogie à d’autres types de couverture; il ne s’applique donc pas à cette situation précise.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter cette exposition comme un net investment hedge; l’analyse doit rester celle d’un élément monétaire intragroupe.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations; it should not be applied by analogy to other types of hedge accounting"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        },
        {
          "section": "14",
          "excerpt": "may be designated as a hedging instrument in a hedge of a net investment in a foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "En consolidation, le point clé est de démontrer que la créance/dette de dividende est un élément monétaire intragroupe dont les écarts de change ne sont pas entièrement éliminés.",
    "Comme la créance est déjà comptabilisée selon l’hypothèse, la voie pertinente est celle d’un poste reconnu; la couverture d’une transaction intragroupe future est hors timing.",
    "La documentation doit être établie à l’inception de la relation de couverture et couvrir l’instrument, le poste couvert, le risque couvert, le hedge ratio et l’analyse d’efficacité.",
    "Le modèle de hedge de net investment sert ici surtout à borner l’analyse : il ne remplace pas le traitement IFRS 9 des éléments monétaires intragroupe."
  ]
}
