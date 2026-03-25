{
  "assumptions": [
    "Une créance de dividende intragroupe déclarée et comptabilisée est traitée comme un élément monétaire intragroupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, la règle générale exclut les éléments intragroupe comme éléments couverts, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Sous l’hypothèse retenue, une créance de dividende intragroupe comptabilisée peut donc être documentée en couverture uniquement sous ces conditions et si les critères de désignation, documentation et efficacité sont respectés."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 pose une exception explicite pour le risque de change d’un élément monétaire intragroupe dans les comptes consolidés. Si la créance de dividende comptabilisée est bien un tel élément et si les écarts de change ne sont pas totalement éliminés à la consolidation, elle peut être désignée comme élément couvert pour le seul risque de change. La relation doit en plus satisfaire aux exigences formelles de documentation et d’efficacité.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe.",
        "Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change ne sont pas totalement éliminés en consolidation.",
        "Seul le risque de change est désigné comme risque couvert.",
        "La relation est formellement désignée et documentée dès l’origine et respecte les tests d’efficacité d’IFRS 9."
      ],
      "practical_implication_fr": "La documentation est possible en consolidation, mais seulement comme couverture du risque de change sur la créance intragroupe et avec un dossier IFRS 9 complet.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship"
        },
        {
          "section": "6.4.1(c)",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "external_party_rule",
      "label_fr": "Interdiction générale pour les éléments internes",
      "applicability": "non",
      "reasoning_fr": "La règle générale d’IFRS 9 en consolidation est que seuls des actifs, passifs, engagements fermes ou transactions prévues avec une partie externe peuvent être désignés comme éléments couverts. Un dividende intragroupe à recevoir est, par nature, un poste interne au groupe. Il n’est donc pas éligible sauf s’il entre dans l’exception spécifique applicable aux éléments monétaires intragroupe.",
      "conditions_fr": [
        "Cette conclusion vaut si la créance de dividende intragroupe ne relève pas de l’exception spécifique d’IFRS 9."
      ],
      "practical_implication_fr": "À défaut de satisfaire à l’exception d’IFRS 9 sur les éléments monétaires intragroupe, la documentation de couverture en consolidation n’est pas recevable.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.5",
          "excerpt": "Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements ... and not in the consolidated financial statements of the group"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net",
      "applicability": "non",
      "reasoning_fr": "IFRIC 16 traite uniquement des couvertures du risque de change sur un investissement net dans une activité à l’étranger. Une créance de dividende intragroupe comptabilisée à recevoir ne constitue pas, dans ce cadre, un investissement net. Cette interprétation ne doit pas être étendue par analogie à ce cas.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas fonder la documentation sur IFRIC 16 ; l’analyse doit rester dans le cadre d’IFRS 9 sur les éléments monétaires intragroupe.",
      "references": [
        {
          "section": "7",
          "excerpt": "This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations"
        },
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations; it should not be applied by analogy to other types of hedge accounting"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord que la créance de dividende est bien un élément monétaire intragroupe au moment de la désignation.",
    "Confirmer que les sociétés concernées ont des monnaies fonctionnelles différentes et que les écarts de change ne sont pas totalement éliminés en consolidation.",
    "Documenter la relation dès l’origine avec l’instrument de couverture, l’élément couvert, le risque de change visé et la méthode de test d’efficacité.",
    "Limiter la désignation au seul risque de change ; en dehors de cette exception, la règle générale des parties externes interdit la couverture en consolidation.",
    "Ne pas traiter cette situation comme une couverture d’investissement net au sens d’IFRIC 16."
  ]
}
