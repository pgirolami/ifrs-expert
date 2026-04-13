# SME Review Notes - 2026-04-12

## 1. Context and Main Takeaway

I reviewed the current state of the assistant with the SME using:
- the current answer on `Q1.0`
- a follow-up on `Q1.0`
- a PwC Viewpoint FAQ question on transaction costs of an FVOCI equity instrument
- follow-up questions on that PwC case

A major takeaway is that my initial scoping was incomplete: Iour initial scope started from the standards, but in practice she starts from **practical FAQ sources** such as **PwC Viewpoint** and **Lefebvre**, and uses those to communicate internally, including with her boss.

---

## 2. Feedback on the Current Q1.0 Answer

### 2.1 What works well

- She likes the **structure** of the answer.
- She is happy with the **clear yes/no answer upfront**.
- She likes having the **references and complete citations**.
- When asked how it would help her, she said it would be useful for:
  - **unusual questions**
  - areas she does not remember immediately from memory

### 2.2 What should be improved

- She asked: **“why is the reformulation in English?”**
  - She wants that part **in French**.

### 2.3 Links and source usability

- When asked whether links back to the standards would help, she said **yes**.
- But this led to a more important point:
  - in practice, she finds **PwC** and **Lefebvre** FAQs **more useful than the standards themselves**
  - she said she **never checks the standards first**
  - she checks the FAQ first because they provide **practical, usable answers**
  - with the current system, even when grounded in the standards, she would still have **some doubt**
  - with the FAQ, she feels she **cannot really be wrong**

### 2.4 Implication for corpus strategy

- When asked whether including **Lefebvre** in the corpus and using it in answers would help, she said **yes, absolutely**
- In particular:
  - this would improve her workflow significantly
  - it would be even better **with links back to the source**
- She explained that these FAQs are also part of **how she communicates with her boss**

### 2.5 Additional observation on FAQ style

- She likes that Lefebvre often:
  - answers the concrete question
  - but also places it in a **broader context**
  - sometimes presents **alternatives** or a more general framing than the narrow question itself

> Note to revisit: I forgot to ask for a concrete example of this.

### 2.6 Lesson learned

- My initial scoping with the SME was incomplete.
- I did not correctly identify her **actual workflow**:
  - real workflow starts from **practical secondary sources**
  - not directly from the standards

This is an important lesson for future discovery work.

---

## 3. Follow-up on Q1.0

### Follow-up question chosen by the SME
- “under what conditions can I do NIH”

### Feedback
- She is **ok with the answer**.

---

## 4. Feedback on PwC Viewpoint Question: FVOCI Equity Instrument Transaction Costs

I then showed her the assistant’s answer to a question found in **PwC Viewpoint** regarding:
- transaction costs on **initial recognition**
- and transaction costs **on sale**
for an equity instrument designated at FVOCI.

The PwC answer is short and practical.

### 4.1 Feedback on the assistant’s main answer

- The assistant spends **too much time explaining approaches that are not applicable**.
- Her view: for this kind of question, the system should not surface “NO” alternatives when the question is not really asking for an approach comparison.
- She finds there is **too much verbiage** compared to the concise PwC answer.
- I asked about the **“Points Opérationnels”** section:
  - she said they are **not really operational points**
  - I suggested removing them
  - she agreed

### 4.2 Feedback on the first follow-up (sale transaction costs)

This follow-up existed because the assistant had not answered the sales transaction cost clearly enough.

Her feedback:
- **way too much verbiage**
- she did **not understand the answer**
- what she expected was simply:

> “yes, it goes into the P&L”

Her interpretation is that:
- this is a **mechanical accounting answer**
- reasoning is **not required**
- the answer should therefore be **short and direct**

### 4.3 Feedback on the second follow-up

The second follow-up was intended to force a direct answer from the previous unclear answer.

The assistant said that sale transaction costs **do not go into P&L**.

Her feedback:
- that answer is **wrong**
- the answer is again **meandering**
- she wanted **only the response**, not a discourse

---

## 5. Emerging Product / Design Implications

## 5.1 There appear to be at least two different answer modes

### A. Structured expert-analysis mode
Useful for:
- unusual questions
- edge cases
- questions where multiple approaches need to be evaluated
- questions where traceability to standards matters

This is where the current system is already helpful.

### B. Short practical-answer mode
Useful for:
- mechanical questions
- questions already well-covered by FAQ-style guidance
- situations where the user wants a direct usable answer, not a full reasoning artifact

This is where the current system appears too verbose.

---

## 5.2 Secondary-source integration is likely high value

The review strongly suggests that adding:
- **PwC Viewpoint**
- **Lefebvre**
- potentially other practical doctrine / FAQ sources

could materially improve usefulness, because:
- these are the SME’s real entry point
- they are phrased in a more practical way
- they are trusted in day-to-day work
- they are used for internal communication

---

## 5.3 The current default output may be too heavy for some classes of question

Current weaknesses highlighted by the SME:
- too much text
- too much explanation of rejected approaches
- too much reasoning for mechanical questions
- “operational points” are not adding value in current form

This suggests the system should eventually distinguish between:
- **approach-comparison questions**
- **mechanical treatment questions**
- **follow-up clarification questions**

---

## 6. Open Questions / Follow-ups

- Ask the SME for an example of a Lefebvre answer she likes because it:
  - answers the narrow question
  - while also framing the broader context
- Clarify whether she would want:
  - two answer modes
  - or one answer mode with optional expansion
- Test whether adding FAQ/doctrine sources changes her level of trust materially
- Reassess whether rejected approaches should be shown at all outside of complex multi-approach questions

---

## 7. Source Used for Part of the Review

### PwC FAQ used for feedback

**FAQ 42.105.1 – How are transaction costs of an FVOCI asset treated on initial recognition and on sale?**

#### Question
An entity acquires an investment in an equity instrument that it designates at fair value through OCI (FVOCI). Its fair value on origination is C100. Purchase commission of C2 is also payable. At the end of the entity’s financial year, the asset's quoted market price is C105. If the asset were to be sold, a commission of C4 would be payable.

How are the transaction costs treated on initial recognition and on sale?

#### Answer
The asset is not classified initially at fair value through profit or loss (FVTPL), so the entity recognises the financial asset at its fair value and adds the purchase commission (that is, a total of C102). At the end of the entity’s financial year, the asset is recorded at C105, without regard to the commission of C4 payable on sale. The change in fair value of C3 recognised in other comprehensive income includes the purchase commission of C2 payable at the acquisition date.

Transaction selling costs are not a subsequent change in fair value that permits to be recognised in OCI, because transaction costs are not deducted in determining fair value (or ‘gains and losses’, as referred to in the standard). IFRS 9 does not otherwise require or permit transaction costs on sale of an equity instrument designated at FVOCI to be recognised in OCI or equity. Therefore, if the asset were sold, the commission payable of C4 would be recognised as an expense in profit or loss. However, in some situations, judgement might be required in determining what is a transaction cost on disposal and what is part of the financial instrument’s fair value.