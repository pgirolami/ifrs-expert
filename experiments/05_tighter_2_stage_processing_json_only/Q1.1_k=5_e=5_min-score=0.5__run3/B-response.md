{
  "assumptions": [
    "La créance de dividende intragroupe est libellée dans une devise créant une exposition de change pour au moins une entité du groupe.",
    "L'analyse est limitée aux possibilités de comptabilité de couverture dans les comptes consolidés au regard des extraits IFRS 9 et IFRIC 16 fournis."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais seulement via les exceptions IFRS 9 applicables au risque de change intragroupe. Pour une créance déjà comptabilisée, la piste principale est la couverture d'un élément monétaire intragroupe; la couverture de flux n'est possible que si la documentation est mise en place avant la comptabilisation, au stade de transaction hautement probable."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "En consolidation, IFRS 9 pose d'abord une règle d'exclusion des éléments intragroupe, puis prévoit une exception pour le risque de change d'un élément monétaire intragroupe. Une créance de dividende déjà comptabilisée peut entrer dans cette exception si l'écart de change n'est pas totalement éliminé en consolidation et si la relation de couverture est formellement documentée et efficace.",
      "conditions_fr": [
        "La créance est un élément monétaire.",
        "Les entités concernées ont des monnaies fonctionnelles différentes.",
        "Les écarts de change ne sont pas totalement éliminés en consolidation.",
        "La relation de couverture respecte la désignation formelle, la documentation et les tests d'efficacité IFRS 9."
      ],
      "practical_implication_fr": "Pour une créance de dividende déjà reconnue, c'est la voie la plus directement envisageable en consolidation si l'exposition de change subsiste au niveau groupe.",
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
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
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
      "label_fr": "Couverture de flux de trésorerie d’un dividende/paiement intragroupe prévu",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Cette voie ne vise pas la créance déjà comptabilisée en tant que telle, mais le dividende ou paiement intragroupe tant qu'il reste une transaction prévue hautement probable. IFRS 9 admet cette exception en consolidation pour le risque de change si la transaction est dans une devise autre que la monnaie fonctionnelle de l'entité qui l'enregistre et si ce risque affectera le résultat consolidé.",
      "conditions_fr": [
        "La documentation de couverture est mise en place avant que le dividende/paiement ne devienne seulement une créance existante.",
        "La transaction intragroupe prévue est hautement probable.",
        "La transaction est libellée dans une devise différente de la monnaie fonctionnelle de l'entité concernée.",
        "Le risque de change affectera le résultat consolidé.",
        "La relation de couverture respecte la désignation formelle, la documentation et les tests d'efficacité IFRS 9."
      ],
      "practical_implication_fr": "Cette approche est pertinente surtout en amont; si la créance est déjà née, il faut vérifier si la documentation a été posée suffisamment tôt.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction ... that transaction must be highly probable"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following criteria"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité à l’étranger",
      "applicability": "non",
      "reasoning_fr": "IFRIC 16 encadre un modèle distinct, réservé au risque de change sur un investissement net dans une activité à l'étranger inclus dans les comptes consolidés. Une créance ordinaire de dividende intragroupe n'est pas, en elle-même, un investissement net; ce modèle ne doit pas être transposé par analogie.",
      "conditions_fr": [
        "Applicable seulement si l'élément couvert est un investissement net dans une activité à l'étranger inclus dans les comptes consolidés."
      ],
      "practical_implication_fr": "Cette documentation n'est pas adaptée à une créance de dividende intragroupe prise isolément.",
      "references": [
        {
          "section": "IFRIC 16.8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations; it should not be applied by analogy to other types of hedge accounting."
        },
        {
          "section": "IFRIC 16.10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        },
        {
          "section": "IFRIC 16.11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Point de départ IFRS 9: en consolidation, un élément intragroupe n'est couvert que via une exception explicite sur le risque de change.",
    "Si la créance de dividende est déjà comptabilisée, la documentation la plus défendable est celle d'un élément monétaire intragroupe, pas celle d'un flux futur sauf documentation antérieure.",
    "La documentation doit identifier l'instrument couvert, l'élément couvert, le risque de change visé, la méthode d'efficacité et le hedge ratio dès l'origine de la relation.",
    "Le test clé en consolidation est de démontrer que le risque de change affecte ou affectera bien le résultat consolidé et n'est pas totalement éliminé.",
    "La couverture d'investissement net reste hors sujet sauf si l'analyse porte en réalité sur des net assets d'une activité étrangère et non sur la créance de dividende elle-même."
  ]
}
