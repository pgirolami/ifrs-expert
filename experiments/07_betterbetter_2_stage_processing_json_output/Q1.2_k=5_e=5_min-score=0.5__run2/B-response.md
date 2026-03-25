{
  "assumptions_fr": [
    "On suppose que la créance de dividende intragroupe, déjà comptabilisée, est libellée en devise étrangère et génère un risque de change dans les comptes consolidés."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Dans les faits décrits, la voie pertinente est la documentation d'une couverture de change sur le poste monétaire déjà reconnu. La couverture d'investissement net vise un autre objet couvert — les actifs nets d'une opération étrangère — et ne répond pas à la créance de dividende comptabilisée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "monetary_item_hedge",
      "label_fr": "Couverture d'un poste monétaire",
      "applicability": "oui",
      "reasoning_fr": "Le fait générateur décrit est une créance de dividende déjà reconnue; sous l'hypothèse fournie, elle porte un risque de change dans les comptes consolidés. Le contexte IFRS 9 vise précisément une relation de couverture entre un actif monétaire non dérivé et un passif monétaire non dérivé pour la composante devise, ce qui correspond au bon stade de reconnaissance et au bon objet couvert.",
      "conditions_fr": [],
      "practical_implication_fr": "En pratique, la documentation de couverture en consolidation peut viser la créance de dividende comme poste couvert de change et l'instrument désigné, avec traitement de la composante devise en résultat.",
      "references": [
        {
          "section": "B5.7.4",
          "excerpt": "If there is a hedging relationship between a non-derivative monetary asset and a non-derivative monetary liability, changes in the foreign currency component of those financial instruments are presented in profit or loss."
        },
        {
          "section": "B5.7.2",
          "excerpt": "IAS 21 requires any foreign exchange gains and losses on monetary assets and monetary liabilities to be recognised in profit or loss."
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "Cette piste ne répond pas au fait précis posé: la question vise la partie change d'une créance de dividende déjà comptabilisée, alors que l'IFRIC 16 traite uniquement des couvertures d'investissement net dans une opération étrangère. L'objet couvert y est un montant d'actifs nets d'une opération étrangère, pas une créance de dividende reconnue au stade actuel.",
      "conditions_fr": [],
      "practical_implication_fr": "Poursuivre cette piste ferait documenter un autre risque en consolidation, celui de l'investissement net, sans couvrir la créance de dividende comptabilisée elle-même.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations; it should not be applied by analogy to other types of hedge accounting."
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point clé de timing est que le dividende est déjà comptabilisé en créance: la documentation doit donc viser un poste monétaire reconnu.",
    "En consolidation, il faut cibler la seule composante change de cette créance et l'instrument de couverture désigné contre cette exposition.",
    "Une documentation de type investissement net déplacerait l'analyse vers les actifs nets d'une opération étrangère, donc hors du périmètre exact de la question."
  ]
}
