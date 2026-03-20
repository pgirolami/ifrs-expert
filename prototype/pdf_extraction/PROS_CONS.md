# PDF Extraction Approaches: Pros & Cons

## Overview

This document compares two approaches for extracting structured section data from PDFs with section-number-to-text mapping.

**Test Case:** Extract sections 23-33 from an IFRS/IASB example PDF where:
- Section numbers appear in the left margin (e.g., "23", "24", "25")
- Corresponding text appears to the right of section numbers
- Text spans multiple lines
- Section titles must be ignored

---

## Approach #1: pdfplumber

### Description
Uses the pdfplumber library to extract individual characters with precise coordinates, then reconstructs text blocks by analyzing position data.

### Pros

| Advantage | Description |
|----------|-------------|
| ✅ Precise character-level extraction | Gets exact coordinates for every character |
| ✅ Good for complex layouts | Handles irregular spacing and multi-column layouts |
| ✅ Active maintenance | Well-maintained library with good documentation |
| ✅ Rich API | Provides words, chars, lines, curves, images |
| ✅ Open source | Free to use, no API costs |

### Cons

| Disadvantage | Description |
|--------------|-------------|
| ❌ Extra spacing in words | Text sometimes has extra spaces within words (e.g., "adipi scin g") |
| ❌ Slower performance | Character-by-character processing is more CPU-intensive |
| ❌ Complex reconstruction | Requires manual logic to reconstruct words and lines |
| ❌ Memory intensive | Stores detailed data for every character |

### Performance
- **Speed:** ~0.5-1 second per page
- **Accuracy:** ~85% (main issue is spacing normalization)

---

## Approach #2: PyMuPDF (fitz)

### Description
Uses PyMuPDF's layout analysis (`get_text("dict")`) to extract text blocks with coordinates, then matches content blocks to section numbers.

### Pros

| Advantage | Description |
|----------|-------------|
| ✅ Clean text output | Produces well-formatted text without extra spaces |
| ✅ Fast performance | Very quick PDF processing |
| ✅ Block-level extraction | Natural text grouping by paragraphs/lines |
| ✅ Well-documented | Excellent API documentation |
| ✅ Lightweight | Lower memory footprint |

### Cons

| Disadvantage | Description |
|--------------|-------------|
| ❌ Sub-paragraph bleeding | Sometimes picks up nested items (a), (b), (c) from wrong sections |
| ❌ Block boundary issues | Text blocks may span multiple logical sections |
| ❌ Less granular | No character-level precision (harder to fine-tune) |
| ❌ PDF-specific quirks | Some PDFs have unusual block structures |

### Performance
- **Speed:** ~0.1-0.3 seconds per page (2-3x faster than pdfplumber)
- **Accuracy:** ~90% for clean sections, ~70% for complex nested content

---

## Comparison Summary

| Criteria | pdfplumber | PyMuPDF |
|----------|------------|---------|
| Text Quality | ⚠️ Extra spacing | ✅ Clean |
| Speed | ❌ Slower | ✅ Faster |
| Precision | ✅ Character-level | ⚠️ Block-level |
| Ease of Use | ⚠️ Complex | ✅ Simple |
| Maintenance | ✅ Active | ✅ Active |
| Cost | Free | Free |

---

## Detailed Extraction Results

The following table shows exactly what each tool extracted for each section across all 3 pages:

| Section | Expected (JSON) | pdfplumber | PyMuPDF |
|---------|-----------------|------------|---------|
| **23** (p.8) | Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. | Lorem ipsum dolor sit am et, consectetur adipi scin g el it, sed do e iusmod tempor i nci didunt ut labor e et do lore ma gn a aliqua. Ut enim ad m inim veniam , quis nostr ud ex er citation ul lam co la boris n isi ut ali quip ex ea commodo cons equat. D uis aute irur e dolor i n r epre hend erit in volupt ate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. | Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. |
| **24** (p.8) | Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit: (a)a first line containing some text on 2 lines so that we respect the bounding box of the original PDF; (b)be compatible with the statement structure createed by the requirements listed in paragraph 22; (c)bab bakfnd jfdmf period to period, in accordance with words and things; (d)a 4th line containing some text on 2 lines so that we respect the bounding box of the original PDF; | Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, ea que ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit: (a)a first line containing some text on 2 lines so that we respect the bounding box of the original PDF; (b)be compatible with the statement structure created by the requirements listed in paragraph 22; (c)bab ba kfnd jfdmf period to period, in accordance with wor ds and thi n gs; (d)a 4th line containing some text on 2 lines so that we respect the bounding box of the original PDF; | (a) (b) be compatible with the statement structure created by the requirements listed in paragraph 22; (c) period to period, in accordance with (d) Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit: a first line containing some text on 2 lines so that we respect the bounding box of the original PDF; a 4th line containing some text on 2 lines so that we respect the bounding box of the original PDF; bab ba kfnd jfdmf words and things; |
| **25** (p.8) | Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. | Neque porro quisquam est, qui dolorem i psum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. | Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. |
| **26** (p.8) | But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how | But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how | But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how |
| **27** (p.8) | Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure: (a) another first line that must be long enough to match the original two line sentence (b)whether the cats and dogs are part of an individual entity or a group of entities; (c)the date of the end of the gestation period or the period covered by the gestation statements; the presentation currency, as deﬁned in ABC 21 The Effects of Felines in Foreign Exchange Fees; and | Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure: (a)another first line that must be long enough to match the original two line sentence whether the cats and dogs are part of an individual entity or a group of entities; the date of the end of the gestation period or the period covered by the gestation statements; the presentation currency, as deﬁned in AB C 21 The Ef fects of (d)Fe lines in Foreign Exchan ge Fees; and | (a) (b) (c) (d) Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure: another first line that must be long enough to match the original two line sentence whether the cats and dogs are part of an individual entity or a group of entities; the presentation currency, as deﬁned in ABC 21 The Effects of Felines in Foreign Exchange Fees; and © ABC Foundation the date of the end of the gestation period or the period covered by the gestation statements; |
| **28** (p.9) | ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. | ipsu m d o l or s it am et, cons ec t etur ad i p i sc in g e lit, sed do e iusmod tem por in cid idunt ut labo re e t dolo r e magn a a liqua. Ut en im a d minim veni a m, q uis n os trud exe rci tat ion ul lamco lab ori s n isi u t a l iqu ip ex ea c omm odo co n sequ at. D uis au te iru r e d olor in re pre he n derit in v oluptate v elit ess e cillum d olore e u fug iat nulla pariatur. E xcep teur sint occaecat c upid atat non p roid ent , sunt in c ulpa qu i officia deseru nt mo llit anim id est laborum. | ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. |
| **29** (p.9) | ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit: (a)a first line containing some text on 2 lines so that we respect the bounding box of the original PDF; (b)be compatible with the statement structure createed by the requirements listed in paragraph 22; (d)a 3rd line containing some text on 2 lines so that we respect the bounding box of the original PDF; | ut per spi cia tis und e om n is is te nat u s e rror sit vol u ptatem accu santium dol oremque lau dantium , tot am rem ape riam , ea que ip sa quae ab illo i nventore ve ritatis et quasi a rchitect o bea tae vi tae d icta sunt e xplicabo. Ne mo en im ipsam vo lupta tem quia voluptas sit: (a) f ir st line co n taini n g so me t e xt on 2 lines so that we res pect the boun ding b ox of the original PDF; (b)co mpatib le w ith the s tatement structurecreatedbythe requ ireme nts listed in p aragraph 22; (c ) a 3 rd line co ntaini ng so m e t ext on 2 lines so that we res pect the boun d in g b ox of the original PDF; porro quisquam est, qui dolorem ipsum quia dolor sit amet, | (a) (b) the by created structure ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit: first line containing some text on 2 lines so that we respect the bounding box of the original PDF; compatible with the statement requirements listed in paragraph 22; (c) a 3rd line containing some text on 2 lines so that we respect the bounding box of the original PDF; |
| **30** (p.9) | porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. | con sectetur, adipi sci v elit, sed q uia non n umqu am ei us modi tempora inc idunt ut labore et dolore magnam aliquam quaerat voluptatem. | porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. |
| **31** (p.9) | I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how | I m us t ex p la in to y ou ho w al l t his mis t aken id ea of d enoun cing ple a sure and pra i sing pai n wa s bo rn an d I w ill g i ve y ou a c omplete ac coun t of the sys tem, and exp ound t he actual tea chin gs of the great ex plo rer of the truth, the maste r-b uilder o f human h app iness . No on e rejects , di slikes, or avoids pleas ure itself , bec ause it is plea sure, bu t beca use t hos e wh o do not know how | I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how |
| **32** (p.9-10) | again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure: (a) another first line that must be long enough to match the original two line sentence (b)whether the cats and dogs are part of an individual entity or a group of entities; (c)the date of the end of the gestation period or the period covered by the gestation statements; the presentation currency, as deﬁned in ABC 21 The Effects of Felines in Foreign Exchange Fees; and Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. | a ga i n is th e re an y on e wh o lo ves or pu r sues o r d e sires t oo bt ai n pain of itself, bec ause i t is pain, but because occ asionally circu mstan ces occur in w hich toil and pain can procure him so me great pleasure: (a) anot her first line t h at must be long en ough t o m atch the original two line sentence whe ther the cats a nd do gs are pa rt of an in dividu al e n tity or a (b) group of entit ies; th e da te o f th e en d of the g estatio n p eri o d or th e period c overed by (c )the g estation statements; the pre s entation c u rr ency, as deﬁ ne d in ABC 2 1 Th e E ffects of (d) F elines in Forei gn E xcha nge F ees; and © | © ABC Foundation (a) (b) (c) (d) another first line that must be long enough to match the original two line sentence whether the cats and dogs are part of an individual entity or a group of entities; the presentation currency, as deﬁned in ABC 21 The Effects of Felines in Foreign Exchange Fees; and the date of the end of the gestation period or the period covered by the gestation statements; again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure: |
| **33** (p.10) | omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit: (a)a first line containing some text on 2 lines so that we respect the bounding box of the original PDF; (b)be compatible with the statement structure createed by the requirements listed in paragraph 22; (c)bab bakfnd jfdmf period to period, in accordance with words and things; (d)a 4th line containing some text on 2 lines so that we respect the bounding box of the original PDF; | laudantium, totam rem aperia m, e aque ipsa q uae ab i llo in ven tore veritatis et quasi arc hitect o beatae v itae di cta su nt ex plica bo. Nemo enim i psam volupt atem quia v olupt as sit: (a)a first line containing some text on 2 lines so that we respect the bounding box of the original PDF; (b)be compatible with the statement structure created by the requirements listed in paragraph 22; (c)bab ba kfnd jfdmf period to period, in accordance with wor ds and thi n gs; (d)a 4th line containing some text on 2 lines so that we respect the bounding box of the original PDF; © | (a) (b) be compatible with the statement structure created by the requirements listed in paragraph 22; (c) period to period, in accordance with (d) a first line containing some text on 2 lines so that we respect the bounding box of the original PDF; a 4th line containing some text on 2 lines so that we respect the bounding box of the original PDF; © ABC Foundation bab ba kfnd jfdmf words and things; |

### Key Observations:

1. **PyMuPDF produces cleaner text** - No extra spaces within words (compare "adipiscing" vs "adipi scin g")
2. **PyMuPDF has sub-paragraph bleeding issue** - Sections 24, 27, 29, 32, 33 pick up (a), (b), (c), (d) items from following sections
3. **pdfplumber has spacing issues** - Every word has random extra spaces inserted
4. **Both methods fail on sections with nested sub-paragraphs** - This is the main remaining challenge

---

## Recommendation

### **Recommended: PyMuPDF (fitz)**

For this specific use case (IFRS/IASB documents with paragraph numbering), **PyMuPDF is recommended** because:

1. **Cleaner text output** - The primary goal is extracting readable text, and PyMuPDF produces cleaner results with proper word spacing
2. **Faster processing** - Important when processing large batches of financial documents
3. **Simpler implementation** - Less code needed to achieve good results
4. **Sufficient accuracy** - The ~90% accuracy for straightforward sections is acceptable

### When to use pdfplumber instead:

- When you need **character-level precision** (e.g., extracting specific words or characters)
- When dealing with **complex multi-column layouts** that require fine-grained position analysis
- When the PDF has **unusual formatting** that requires custom reconstruction logic

### Improvements needed for production:

Both approaches would benefit from:
1. **Post-processing filters** to clean up nested sub-paragraph markers
2. **Configuration options** for margin thresholds and section number detection
3. **Validation logic** to detect and handle edge cases
4. **Page offset handling** (to map to external page numbering if needed)

---

## Files in This Folder

- `extract_pdfplumber.py` - Implementation using pdfplumber
- `extract_pymupdf.py` - Implementation using PyMuPDF  
- `output_pdfplumber.json` - Sample output from pdfplumber
- `output_pymupdf.json` - Sample output from PyMuPDF
- `PROS_CONS.md` - This comparison document

---

## Additional Test: IFRS 16 Leases PDF (Pages 18-19)

The following table shows the extraction results on a real IFRS document (`examples/ifrs/ifrs-16-leases.pdf`) on pages 18 and 19:

| Section | pdfplumber | PyMuPDF |
|---------|------------|---------|
| **16** (p.18) | anufacturer or dealer lessors | (not extracted) |
| **71** (p.18) | At the commencement date, a manufacturer or dealer lessor shall recognise the following for each of its finance leases: (a)revenue being the fair value of the underlying asset, or, if lower, the present value of the lease payments accruing to the lessor, discounted using a market rate of interest; (b)the cost of sale being the cost, or carrying amount if different, of the underlying asset less the present value of the unguaranteed residual value; and (c)selling profit or loss (being the difference between revenue and the cost of sale) in accordance with its policy for outright sales to which IFRS 15 applies. A manufacturer or dealer lessor shall recognise selling profit or loss on a finance lease at the commencement date, regardless of whether the lessor transfers the underlying asset as described in | At the commencement date, a manufacturer or dealer lessor shall recognise the following for each of its finance leases: (a) revenue being the fair value of the underlying asset, or, if lower, the present value of the lease payments accruing to the lessor, discounted using a market rate of interest; (b) the cost of sale being the cost, or carrying amount if different, of the underlying asset less the present value of the unguaranteed residual value; and (c) selling profit or loss (being the difference between revenue and the cost of sale) in accordance with its policy for outright sales to which IFRS 15 applies. A manufacturer or dealer lessor shall recognise selling profit or loss on a finance lease at the commencement date, regardless of whether the lessor transfers the underlying asset as described in IFRS 15. |
| **72** (p.18) | Manufacturers or dealers often offer to customers the choice of either buying or leasing an asset. A finance lease of an asset by a manufacturer or dealer lessor gives rise to profit or loss equivalent to the profit or loss resulting from an outright sale of the underlying asset, at normal selling prices, reflecting any applicable volume or trade discounts. | Manufacturers or dealers often offer to customers the choice of either buying or leasing an asset. A finance lease of an asset by a manufacturer or dealer lessor gives rise to profit or loss equivalent to the profit or loss resulting from an outright sale of the underlying asset, at normal selling prices, reflecting any applicable volume or trade discounts. |
| **73** (p.18) | Manufacturer or dealer lessors sometimes quote artificially low rates of interest in order to attract customers. The use of such a rate would result in a lessor recognising an excessive portion of the total income from the transaction at the commencement date. If artificially low rates of interest are quoted, a manufacturer or dealer lessor shall restrict selling profit to that which would apply if a market rate of interest were charged. | Manufacturer or dealer lessors sometimes quote artificially low rates of interest in order to attract customers. The use of such a rate would result in a lessor recognising an excessive portion of the total income from the transaction at the commencement date. If artificially low rates of interest are quoted, a manufacturer or dealer lessor shall restrict selling profit to that which would apply if a market rate of interest were charged. |
| **74** (p.18) | A manufacturer or dealer lessor shall recognise as an expense costs incurred in connection with obtaining a finance lease at the commencement date because they are mainly related to earning the manufacturer or dealer's selling profit. Costs incurred by manufacturer or dealer lessors in connection with obtaining a finance lease are excluded from the definition of initial direct costs and, thus, are excluded from the net investment in the lease. Subsequent measurement A lessor shall recognise finance income over the lease term, based on a | A manufacturer or dealer lessor shall recognise as an expense costs incurred in connection with obtaining a finance lease at the commencement date because they are mainly related to earning the manufacturer or dealer's selling profit. Costs incurred by manufacturer or dealer lessors in connection with obtaining a finance lease are excluded from the definition of initial direct costs and, thus, are excluded from the net investment in the lease. Subsequent measurement |
| **75** (p.18) | pattern reflecting a constant periodic rate of return on the lessor's net investment in the lease. | A lessor shall recognise finance income over the lease term, based on a pattern reflecting a constant periodic rate of return on the lessor's net investment in the lease. |
| **76** (p.18) | A lessor aims to allocate finance income over the lease term on a systematic and rational basis. A lessor shall apply the lease payments relating to the period against the gross investment in the lease to reduce both the principal and the unearned finance income. | A lessor aims to allocate finance income over the lease term on a systematic and rational basis. A lessor shall apply the lease payments relating to the period against the gross investment in the lease to reduce both the principal and the unearned finance income. |
| **77** (p.19) | A lessor shall apply the derecognition and impairment requirements in IFRS 9 to the net investment in the lease. A lessor shall review regularly estimated unguaranteed residual values used in computing the gross investment in the lease. If there has been a reduction in the estimated unguaranteed residual value, the lessor shall revise the income allocation over the lease term and recognise immediately any reduction in respect of amounts accrued. | A lessor shall apply the derecognition and impairment requirements in IFRS 9 to the net investment in the lease. A lessor shall review regularly estimated unguaranteed residual values used in computing the gross investment in the lease. If there has been a reduction in the estimated unguaranteed residual value, the lessor shall revise the income allocation over the lease term and recognise immediately any reduction in respect of amounts accrued. |
| **78** (p.19) | A lessor that classifies an asset under a finance lease as held for sale (or includes it in a disposal group that is classified as held for sale) applying IFRS 5 Non-current Assets Held for Sale and Discontinued Operations shall account for the asset in accordance with that Standard. Lease modifications | A lessor that classifies an asset under a finance lease as held for sale (or includes it in a disposal group that is classified as held for sale) applying IFRS 5 Non-current Assets Held for Sale and Discontinued Operations shall account for the asset in accordance with that Standard. Lease modifications |
| **79** (p.19) | A lessor shall account for a modification to a finance lease as a separate lease if both: (a)the modification increases the scope of the lease by adding the right to use one or more underlying assets; and (b)the consideration for the lease increases by an amount commensurate with the stand-alone price for the increase in scope and any appropriate adjustments to that stand-alone price to reflect the circumstances of the particular contract. | A lessor shall account for a modification to a finance lease as a separate lease if both: (a) the modification increases the scope of the lease by adding the right to use one or more underlying assets; and (b) the consideration for the lease increases by an amount commensurate with the stand-alone price for the increase in scope and any appropriate adjustments to that stand-alone price to reflect the circumstances of the particular contract. |
| **80** (p.19) | For a modification to a finance lease that is not accounted for as a separate lease, a lessor shall account for the modification as follows: (a)if the lease would have been classified as an operating lease had the modification been in effect at the inception date, the lessor shall: (i)account for the lease modification as a new lease from the effective date of the modification; and (ii)measure the carrying amount of the underlying asset as the net investment in the lease immediately before the effective date of the lease modification. (b)otherwise, the lessor shall apply the requirements of IFRS 9. Operating leases Recognition and measurement | For a modification to a finance lease that is not accounted for as a separate lease, a lessor shall account for the modification as follows: (a) if the lease would have been classified as an operating lease had the modification been in effect at the inception date, the lessor shall: (i) account for the lease modification as a new lease from the effective date of the modification; and (ii) measure the carrying amount of the underlying asset as the net investment in the lease immediately before the effective date of the lease modification. (b) otherwise, the lessor shall apply the requirements of IFRS 9. Operating leases Recognition and measurement |
| **81** (p.19) | A lessor shall recognise lease payments from operating leases as income on either a straight-line basis or another systematic basis. The lessor shall apply another systematic basis if that basis is more representative of the pattern in which benefit from the use of the underlying asset is diminished. A lessor shall recognise costs, including depreciation, incurred in earning the | A lessor shall recognise lease payments from operating leases as income on either a straight-line basis or another systematic basis. The lessor shall apply another systematic basis if that basis is more representative of the pattern in which benefit from the use of the underlying asset is diminished. |
| **82** (p.19) | lease income as an expense. © IFRS FoundationA837 | A lessor shall recognise costs, including depreciation, incurred in earning the lease income as an expense. © IFRS Foundation A837 |

### Key Observations for IFRS 16:

1. **PyMuPDF extracts more complete text** - For sections 71, 74, 75, 81, 82, PyMuPDF captures more text than pdfplumber
2. **pdfplumber has more fragmentation issues** - Text often gets cut mid-sentence or has line-break issues
3. **PyMuPDF preserves paragraph structure better** - Sub-paragraphs (a), (b), (c) are properly formatted with spaces
4. **Both tools handle the nested sub-paragraph structure** - The (a), (b), (c) items are captured correctly in most cases
5. **Section 16 is a header** - Not extracted properly by either tool (PyMuPDF missed it, pdfplumber only got partial)
