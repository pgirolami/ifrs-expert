{
  "assumptions_fr": [
    "La créance de dividendes est un poste monétaire intragroupe comptabilisé, libellé dans une devise différente de la monnaie fonctionnelle pertinente pour la désignation de couverture au niveau consolidé.",
    "Les gains ou pertes de change correspondants ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "L’entité dispose d’un instrument de couverture éligible et peut satisfaire aux exigences de désignation, de documentation et d’efficacité du paragraphe 6.4.1 d’IFRS 9."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Au consolidé, les éléments intragroupe sont en principe exclus, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Dans cette situation, une documentation de couverture IFRS est donc possible, sous réserve du respect des critères de l’article 6.4.1."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividendes est supposée être un poste monétaire intragroupe reconnu, exposé à un risque de change qui affecte le résultat consolidé. Même si les éléments intragroupe sont en principe exclus en consolidation, l’exception d’IFRS 9 pour le risque de change d’un poste monétaire intragroupe permet ici une désignation en couverture, et le modèle de juste valeur est directement compatible avec un actif reconnu exposé à une variation de valeur liée au change.",
      "conditions_fr": [
        "Démontrer que les écarts de change sur la créance ne sont pas totalement éliminés en consolidation.",
        "Désigner formellement dès l’origine la créance, l’instrument de couverture, le risque de change couvert et le ratio de couverture.",
        "Vérifier l’existence d’une relation économique et l’absence de domination du risque de crédit dans l’inefficacité."
      ],
      "practical_implication_fr": "La documentation peut être établie au niveau consolidé sur la créance comptabilisée, avec un suivi d’efficacité conforme à IFRS 9.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk and could affect profit or loss"
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
      "reasoning_fr": "Dans cette situation, la même exception d’IFRS 9 pour les postes monétaires intragroupe permet d’envisager la désignation du risque de change au niveau consolidé. Une couverture de flux de trésorerie est possible si l’entité documente que le risque couvert est la variabilité des encaissements en monnaie fonctionnelle lors du règlement de la créance de dividendes et si cette variabilité peut affecter le résultat consolidé.",
      "conditions_fr": [
        "Relier explicitement dans la documentation le risque de change à la variabilité des flux encaissés en monnaie fonctionnelle.",
        "Démontrer que cette variabilité peut affecter le résultat consolidé.",
        "Respecter les exigences de désignation, de documentation et d’efficacité du paragraphe 6.4.1."
      ],
      "practical_implication_fr": "La relation de couverture doit être documentée autour du règlement futur de la créance et de la variabilité de ses flux en monnaie fonctionnelle.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability ... and could affect profit or loss"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following criteria"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif au consolidé est de prouver que les écarts de change sur la créance intragroupe ne sont pas totalement éliminés et affectent bien le résultat consolidé.",
    "La documentation doit être mise en place dès l’origine de la relation de couverture, avec identification précise du risque de change, de l’instrument et du ratio de couverture.",
    "La couverture de juste valeur est la voie la plus directement appuyée ici par le fait générateur décrit, à savoir une créance monétaire déjà comptabilisée.",
    "Si l’entité retient une couverture de flux de trésorerie, l’effort de documentation est plus exigeant sur la démonstration de la variabilité des flux encaissés en monnaie fonctionnelle."
  ]
}
