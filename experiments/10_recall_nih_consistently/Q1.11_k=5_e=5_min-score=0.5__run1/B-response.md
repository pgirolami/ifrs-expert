{
  "assumptions_fr": [
    "La question vise le risque de change en comptes consolidés sous IFRS 9.",
    "Le dividende intragroupe a été déclaré et a fait naître une créance/dette intragroupe monétaire déjà comptabilisée."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en consolidation, la créance/dette de dividende intragroupe déjà comptabilisée peut être désignée en hedge accounting pour son risque de change si les écarts de change ne sont pas entièrement éliminés en consolidation. La couverture d’un investissement net n’est pas adaptée à ce fait générateur."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance/dette de dividende est un actif ou passif intragroupe reconnu.\nLa règle générale exclut les postes intragroupe en consolidation, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe non totalement éliminé ; une couverture de juste valeur peut donc s’appliquer ici.",
      "conditions_fr": [
        "La créance/dette de dividende est un poste monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes",
        "Les écarts de change correspondants ne sont pas entièrement éliminés en consolidation et peuvent affecter le résultat consolidé"
      ],
      "practical_implication_fr": "La documentation peut viser la créance/dette de dividende reconnue comme poste couvert au titre du risque de change.",
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
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le texte de la cash flow hedge vise aussi un \"recognised asset or liability\".\nPour une créance/dette de dividende en devise déjà enregistrée, la variabilité du flux de règlement en monnaie fonctionnelle peut être couverte en consolidation, mais seulement si l’exception applicable aux postes monétaires intragroupe est satisfaite dans ce cas.",
      "conditions_fr": [
        "Le règlement futur du dividende reste exposé à une variabilité de change en monnaie fonctionnelle jusqu’au paiement",
        "La créance/dette est entre entités ayant des monnaies fonctionnelles différentes et les écarts de change ne sont pas entièrement éliminés en consolidation"
      ],
      "practical_implication_fr": "La documentation doit alors cibler le flux de règlement du dividende et son risque de change, et non un investissement net.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Le dividende intragroupe déclaré ne représente pas un montant de net assets d’une foreign operation, mais une créance/dette monétaire intragroupe.\nIFRIC 16 réserve ce modèle aux hedges of net investments et exclut son application par analogie à d’autres expositions ; il ne s’applique donc pas à cette situation.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette exposition ne doit pas être documentée comme une couverture d’investissement net.",
      "references": [
        {
          "section": "8",
          "excerpt": "it should not be applied by analogy to other types of hedge accounting."
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "10",
          "excerpt": "only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord si les entités concernées ont des monnaies fonctionnelles différentes ; sinon l’exception intragroupe de 6.3.6 ne joue pas.",
    "Confirmer que les écarts de change sur la créance/dette de dividende ne sont pas entièrement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "Documenter dès la désignation l’instrument de couverture, la créance/dette de dividende couverte, le risque de change, le hedge ratio et la manière d’apprécier l’efficacité.",
    "Une fois la créance enregistrée, raisonner comme sur un poste monétaire intragroupe reconnu ; ne pas le traiter comme une couverture d’investissement net."
  ]
}
