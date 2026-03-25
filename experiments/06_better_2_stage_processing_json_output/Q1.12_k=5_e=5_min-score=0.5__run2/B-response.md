{
  "assumptions_fr": [
    "On suppose que le dividende déclaré a créé une créance/dette intragroupe comptabilisée et libellée en devise étrangère pour au moins une entité du groupe.",
    "On suppose que l’analyse est limitée à la comptabilité de couverture dans les états financiers consolidés selon IFRS 9, IFRIC 16 n’étant considérée que pour les couvertures d’investissement net.",
    "On suppose que la question clé d’éligibilité est de savoir si les écarts de change sur l’élément intragroupe ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais seulement sous conditions. Dans le cas d’un dividende intragroupe déjà comptabilisé en créance, la seule voie pertinente au consolidé est l’analyse comme élément monétaire intragroupe; elle ne qualifie que si le risque de change subsiste en résultat consolidé et si les exigences formelles d’IFRS 9 sont remplies."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Selon les hypothèses, le dividende a déjà donné lieu à une créance/dette intragroupe reconnue; l’analyse porte donc, à ce stade, sur un élément monétaire intragroupe et non sur une transaction future.\nEn consolidation, IFRS 9 interdit en principe les éléments intragroupe, mais prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés et affectent le résultat consolidé; il faut aussi satisfaire aux critères de mesure, de documentation et d’efficacité.",
      "conditions_fr": [
        "les écarts de change sur la créance/dette de dividende ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé",
        "l’élément couvert est de manière fiable mesurable",
        "la relation de couverture est formellement désignée et documentée à l’origine, avec une évaluation d’efficacité conforme"
      ],
      "practical_implication_fr": "La qualification est envisageable au niveau consolidé, mais uniquement comme couverture du risque de change sur la créance/dette intragroupe reconnue.",
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
          "section": "6.3.2",
          "excerpt": "The hedged item must be reliably measurable."
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "forecast_transaction_hedge",
      "label_fr": "Couverture d’une transaction intragroupe future",
      "applicability": "non",
      "reasoning_fr": "Cette approche vise une transaction intragroupe hautement probable avant sa comptabilisation. Or la question et les hypothèses imposent un dividende déjà comptabilisé en créance à recevoir; revenir à un stade antérieur contredirait le timing et le statut comptable du cas.\nElle ne s’applique donc pas à cette situation précise, même si elle pourrait être pertinente avant la reconnaissance.",
      "conditions_fr": [],
      "practical_implication_fr": "La piste de la transaction future doit être écartée pour ce dividende déjà reconnu.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net",
      "applicability": "non",
      "reasoning_fr": "IFRIC 16 traite d’un modèle distinct portant sur le risque de change d’un investissement net dans une activité à l’étranger, c’est-à-dire un montant de net assets, et non une créance de dividende intragroupe déjà comptabilisée.\nLe contexte vise explicitement un dividende intragroupe reconnu; appliquer le modèle d’investissement net supposerait un autre objet couvert, ce que les hypothèses et le timing n’autorisent pas.",
      "conditions_fr": [],
      "practical_implication_fr": "Il faut distinguer strictement la créance de dividende d’une couverture d’investissement net; ce ne sont pas le même objet couvert.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations; it should not be applied by analogy to other types of hedge accounting."
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "14",
          "excerpt": "A derivative or a non-derivative instrument ... may be designated as a hedging instrument in a hedge of a net investment in a foreign operation."
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "non_qualifying_hedge",
      "label_fr": "Absence de couverture qualifiante",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Cette issue s’applique dans la situation posée si, malgré la créance intragroupe reconnue, le risque de change correspondant est entièrement éliminé en consolidation ou n’affecte pas le résultat consolidé.\nDans ce cas, la règle générale d’IFRS 9 sur les éléments intragroupe prévaut, et aucune relation de couverture qualifiante ne peut être formalisée au niveau consolidé; le même résultat suit si la documentation ou l’efficacité font défaut.",
      "conditions_fr": [
        "les écarts de change sur la créance/dette sont entièrement éliminés en consolidation, ou n’affectent pas le résultat consolidé",
        "ou les exigences de désignation, de documentation ou d’efficacité d’IFRS 9 ne sont pas remplies"
      ],
      "practical_implication_fr": "À défaut d’exception qualifiante, les effets de change et l’instrument de couverture restent hors comptabilité de couverture au consolidé.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "may qualify as a hedged item ... if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le fait que le dividende soit déjà comptabilisé en créance à recevoir fixe le bon angle d’analyse: élément monétaire intragroupe reconnu, et non transaction future.",
    "Au niveau consolidé, le point décisif est de démontrer que les écarts de change sur cette créance/dette ne sont pas totalement éliminés et qu’ils affectent le résultat consolidé.",
    "La documentation doit exister à l’origine de la relation de couverture et identifier l’instrument de couverture, l’élément couvert, le risque de change visé et la méthode d’évaluation de l’efficacité.",
    "La couverture d’un investissement net est un modèle séparé, réservé aux net assets d’une activité étrangère, et ne doit pas être utilisée par analogie pour une créance de dividende intragroupe."
  ]
}
