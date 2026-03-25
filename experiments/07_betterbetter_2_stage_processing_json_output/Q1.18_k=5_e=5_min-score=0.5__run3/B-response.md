{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà été déclaré ; la créance/dette de dividende est donc un poste monétaire comptabilisé, et non une transaction intragroupe future.",
    "Les entités concernées ont des monnaies fonctionnelles différentes et les écarts de change correspondants ne sont pas totalement éliminés en consolidation ; le risque de change affecte donc le résultat consolidé.",
    "La désignation de couverture envisagée satisfait par ailleurs aux exigences de documentation et d’efficacité d’IFRS 9."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Dans les faits supposés, l’exposition provient d’un poste monétaire intragroupe déjà comptabilisé et IFRS 9 prévoit précisément, en consolidation, une exception pour ce risque de change lorsqu’il affecte le résultat consolidé. En revanche, la couverture d’un investissement net vise les actifs nets d’une activité étrangère, pas cette créance distincte."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "monetary_item_hedge",
      "label_fr": "Couverture du risque de change sur un poste monétaire intragroupe",
      "applicability": "oui",
      "reasoning_fr": "La question porte sur une créance de dividende intragroupe déjà comptabilisée ; selon les hypothèses, il s’agit donc d’un poste monétaire reconnu au stade actuel.\nIFRS 9 pose une règle générale d’externalité, mais prévoit explicitement en consolidation une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés.\nComme cette condition est supposée remplie et que les autres critères de désignation/efficacité sont aussi supposés satisfaits, cette voie s’applique dans cette situation.",
      "conditions_fr": [],
      "practical_implication_fr": "En pratique, la relation de couverture doit être documentée au niveau consolidé en visant la créance/dette de dividende intragroupe comme élément couvert pour son seul risque de change.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Cette approche ne répond pas à l’exposition précise décrite : la question vise une créance sur dividendes intragroupe déjà reconnue, donc un poste monétaire distinct au stade actuel.\nOr la couverture d’investissement net vise le risque de change sur les actifs nets d’une activité étrangère, pour un montant de net assets, et non le risque attaché à une créance de dividende comptabilisée.\nL’utiliser ici reviendrait à changer l’élément couvert et à reformuler le cas de fait ; elle n’est donc pas applicable à cette situation.",
      "conditions_fr": [],
      "practical_implication_fr": "En pratique, poursuivre cette voie conduirait à documenter une couverture des actifs nets de l’activité étrangère, pas de la créance de dividende identifiée.",
      "references": [
        {
          "section": "2",
          "excerpt": "the item being hedged ... may be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point de départ retenu est un dividende déjà déclaré : l’analyse doit donc rester au niveau d’un poste monétaire intragroupe comptabilisé, et non d’une transaction future.",
    "Au niveau consolidé, il faut pouvoir démontrer que les écarts de change sur cette créance/dette ne sont pas totalement éliminés et qu’ils affectent le résultat consolidé.",
    "La voie pertinente est la couverture du risque de change du poste monétaire intragroupe ; la couverture d’un investissement net est une mécanique distincte qui ne traite pas cette créance spécifique."
  ]
}
