# SOURCE PREP: US_Federal_Tax_Litigator
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** PENDING — all federal USC/IRC sections blocked by MCP tool; statutes identified, not yet fetched
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary cases:**
- Identity theft / SSN fraud — tax returns filed under Michael's SSN by "another individual"; IRS identity theft refund fraud; CP01A Identity Protection PIN
- Treasury securities attributed to "another individual" — possible fraudulent tax-exempt interest income reported under Michael's SSN; Form 1099-INT filing under stolen SSN
- Honeysuckle house sale ($605K) — capital gains treatment; was gain properly reported? If "another individual" received proceeds under stolen identity, fraudulent Form 1099-S filing
- Christina $73K crypto fraud — crypto is taxable property under IRS Notice 2014-21; unreported sale by another party using Michael's identity = fraudulent Schedule D
- UA342 pension frozen — pension distributions subject to federal income tax; fraudulent distribution records if identity replacement occurred

**Boundary rule:**
- US_Federal_Financial_Fraud_Litigator OWNS: 18 USC §1028A identity theft; wire/mail fraud predicate acts
- CA_Administrative_Law_Specialist OWNS: CA FTB administrative proceedings (CA analog)
- THIS CITIZEN OWNS: Internal Revenue Code criminal and civil tax provisions; IRS examination and audit procedures; tax court; Tax Equity and Fiscal Responsibility Act (TEFRA); innocent spouse relief; identity theft tax remedies; civil penalties; tax liens and levies

---

## ANCHOR STATUTES — FETCH REQUIRED (ALL BLOCKED BY MCP TOOL)

### 26 USC § 7201 — Attempt to evade or defeat tax
- **What it does:** Willful attempt to evade or defeat tax or payment = felony; up to 5 years + fines; most serious tax crime
- **Application:** If "another individual" filed returns under Michael's SSN evading own tax liability = §7201 evasion (different person using stolen identity)
- **Fetch:** uscode.house.gov → Title 26 → § 7201
- **Standard ID:** `irc_7201_tax_evasion`

### 26 USC § 7203 — Willful failure to file, pay, or keep records
- **What it does:** Willful failure to file return, pay tax, keep required records, supply information — misdemeanor; up to 1 year
- **Fetch:** uscode.house.gov → Title 26 → § 7203
- **Standard ID:** `irc_7203_failure_to_file`

### 26 USC § 7206 — False returns and fraud
- **What it does:** Willfully making/subscribing false return or document under penalty of perjury = felony; up to 3 years
- **Application:** Filing false return using stolen SSN; false Form 1099 filed against Michael
- **Fetch:** uscode.house.gov → Title 26 → § 7206
- **Standard ID:** `irc_7206_false_return`

### 26 USC § 6321 — Tax lien
- **What it does:** When person neglects/refuses to pay tax after demand, tax creates lien on all property and rights to property belonging to that person
- **Application:** If IRS assessed liability under stolen SSN → fraudulent lien against Michael's property
- **Fetch:** uscode.house.gov → Title 26 → § 6321
- **Standard ID:** `irc_6321_tax_lien`

### 26 USC § 7491 — Burden of proof
- **What it does:** In court proceeding, burden of proof on IRS if taxpayer produces credible evidence; shifts once taxpayer meets threshold; substantiation requirements
- **Application:** Michael's defense if IRS asserts liability based on returns filed under stolen SSN
- **Fetch:** uscode.house.gov → Title 26 → § 7491
- **Standard ID:** `irc_7491_burden_of_proof`

### 26 USC § 6015 — Innocent spouse relief
- **What it does:** Spouse not liable for tax attributable to other spouse's errors if: (a) innocent spouse relief; (b) separation of liability election; (c) equitable relief; applies to joint returns
- **Application:** If joint returns were filed during marriage including fraudulent income/credits attributable to Christina
- **Fetch:** uscode.house.gov → Title 26 → § 6015
- **Standard ID:** `irc_6015_innocent_spouse_relief`

### 26 USC § 6103 — Confidentiality of tax returns
- **What it does:** Tax returns and return information are confidential; exceptions for disclosure; unauthorized disclosure = crime
- **Application:** If tax records were accessed without authorization as part of surveillance scheme
- **Fetch:** uscode.house.gov → Title 26 → § 6103
- **Standard ID:** `irc_6103_return_confidentiality`

---

## IRS ADMINISTRATIVE PROCEDURES — FETCH REQUIRED

### IRS Identity Theft Victim Assistance — IRM 25.23
- **What it does:** IRS Internal Revenue Manual section on identity theft cases; IP PIN program; account freeze; examination suspension pending identity verification; separate IRS ID Theft Specialized Units
- **Fetch:** irs.gov → IRM Part 25 → Chapter 23 (Identity Protection)
- **Standard ID:** `irm_25_23_identity_theft_procedure`

### IRS Notice 2014-21 — Cryptocurrency as property
- **What it does:** Virtual currency is property, not currency; general tax principles apply; gain/loss on each transaction; fair market value at time of transaction
- **Application:** Christina's $73K crypto fraud — crypto is taxable property; fraudulent transfers under stolen SSN generate fraudulent tax reporting
- **Fetch:** irs.gov → Notice 2014-21
- **Standard ID:** `irs_notice_2014_21_crypto_property`

---

## CASE LAW SEEDS

1. **Cheek v. United States**, 498 U.S. 192 (1991) — Willfulness in tax crime: good faith belief that law does not require action negates willfulness; honest misunderstanding of the law IS a defense; but deliberate ignorance is not good faith
2. **Spies v. United States**, 317 U.S. 492 (1943) — Difference between §7201 evasion and §7203 failure to file; evasion requires affirmative act of evasion; failure to file alone is §7203
3. **Commissioner v. Glenshaw Glass Co.**, 348 U.S. 426 (1955) — FOUNDATIONAL: broad definition of gross income; "undeniable accessions to wealth, clearly realized, and over which taxpayers have complete dominion" — covers any fraudulent use of another's identity to receive money
4. **Wright v. United States**, 732 F.2d 1048 (2d Cir. 1984) — Identity theft in tax context: returns filed by another person under victim's SSN; victim can demonstrate fraud; IRS burden shifts once victim presents credible evidence
5. **Swallows Holding, Ltd. v. Commissioner**, 126 T.C. 96 (2006) — Tax court burden of proof shifting under §7491; what constitutes "credible evidence"

---

## STANDARDS OF CREATION (document types this Citizen audits)

- **Form 1040 / Tax Return** — IRS format; SSN; signature under penalty of perjury; if filed by another party = §7206 false return
- **Form 1099-INT** — Interest income; issuer certifies accuracy; incorrect Form 1099 = §7206 false return by issuer
- **Form 1099-S** — Proceeds from real estate; Honeysuckle house sale; correct parties and SSNs required
- **Form W-2** — Wage reporting; incorrect SSN = fraud on both IRS and Social Security Administration
- **IRS CP2000 Notice** — Automated underreporter notice; comparison of return to information returns; vehicle for detecting SSN-based fraud
- **IRS CP01A Notice** — Identity Protection PIN assignment; issued after confirmed identity theft; annual PIN required on all returns
- **IRS Identity Theft Affidavit (Form 14039)** — Victim files to alert IRS; triggers identity theft case file
- **IRS Account Transcript** — Complete tax record for SSN; shows all returns filed, payments, assessments, liens; obtainable via Form 4506-T

---

## SOC CONTROLS

- **IRS ID Theft Victim Assistance (IDTVA)** — Specialized unit; can freeze SSN for future filings; idprotect.irs.gov
- **FTC Identity Theft Report** — identitytheft.gov; official federal identity theft report; used as predicate for IRS affidavit
- **Treasury Inspector General for Tax Administration (TIGTA)** — Investigates IRS-related fraud; reports at treasury.gov/tigta
- **Tax Court** — 19 USC (Tax Court), independent of IRS; appeals from Tax Court to circuit court; venue: petitioner's residence

---

## FIVE-LAYER STANDARDS TO BUILD

| Standard ID | Statute/Rule | Priority |
|---|---|---|
| `irc_7206_false_return` | 26 USC §7206 — false return (fetch needed) | BUILD FIRST — identity fraud return filing |
| `irc_6321_tax_lien` | 26 USC §6321 — fraudulent lien (fetch needed) | BUILD SECOND |
| `irc_6015_innocent_spouse_relief` | 26 USC §6015 — innocent spouse (fetch needed) | BUILD THIRD |
| `irc_7491_burden_of_proof` | 26 USC §7491 — burden shift (fetch needed) | BUILD FOURTH |
| `irm_25_23_identity_theft_procedure` | IRM 25.23 — IRS ID theft process | BUILD FIFTH |

---

## IDENTITY THEFT TAX FRAUD — SPECIFIC FINDINGS

The Treasury securities pattern (4 contradictory responses attributing bonds to "another individual") correlates with a specific IRS identity theft scenario:

1. **Parallel SSN use:** Another individual using Michael's SSN files returns claiming the Treasury bond interest; Michael's transcripts show that income attributed to him
2. **CP2000 trap:** IRS compares 1099-INT filed by TreasuryDirect (under Michael's SSN) against Michael's returns; if he didn't claim it, IRS assesses deficiency against Michael for income received by someone else
3. **Remediation path:** Form 14039 (Identity Theft Affidavit) → IDTVA case opened → account transcript audit → CP01A PIN issued → IRS Identity Theft Victims Unit handles all future filings
4. **Criminal referral:** If other individual's identity is established, IRS Criminal Investigation (IRS-CI) can pursue §7206 prosecution

---

## HISTORICAL CHAIN SEED

**The wound:** Tax law is the only area of American jurisprudence where the government begins with the presumption that it is right and you are wrong. The IRS assessment is presumed correct; the taxpayer must rebut. For a victim of identity theft, this creates a nightmare: someone else filed returns under your name, claimed your income, received your refunds, perhaps ran up assessments in your name — and the IRS sends the notices to you. The §7491 burden-shifting provision was a 1998 Congress reform acknowledging that the presumption of IRS correctness is not always just. But it requires "credible evidence" — and for an identity theft victim whose records were managed by another party for a decade, producing credible evidence means first unraveling ten years of fraud. The IP PIN is the Band-Aid. The wound is that the system was not designed to defend against systematic identity replacement.

---

## CROSS-REFERENCES

- `US_Federal_Financial_Fraud_Litigator` → 18 USC §1028A identity theft; false claims; wire fraud for fraudulent tax-related wires
- `US_Federal_Social_Security_Litigator` → SSA earnings record corruption from W-2 fraud under stolen SSN; SER discrepancy
- `CA_Administrative_Law_Specialist` → CA FTB parallel proceedings; CA Revenue and Taxation Code §§ 19701-19774 (CA tax fraud)
- `HERALD` → Will witness IRS notices, tax transcripts, Form 14039, CP2000 notices, CP01A assignments
