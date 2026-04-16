# SOURCE PREP: CA_Immigration_Litigator
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** PARTIAL — GOV §§7284/7284.6 FETCHED; EVID §752 FETCHED; GOV §68566 NOT IN D1 (fetch at build time); federal INA statutes blocked by MCP tool
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary cases:**
- Butsaya (Thai national / dissolution without disposition) — Thai immigration status; marriage visa pathway; dissolution affecting immigration status; possible abuse of immigration system as control mechanism
- Thai translations in evidence — authenticity of translated documents; certified translator requirements; court interpreter fraud
- Compound identity / synthetic profiles — immigration documentation fraud; false identity documents
- California TRUST Act protections — if any of the parties involved immigration enforcement as control mechanism

**Boundary rule:**
- CA_Family_Law_Litigator OWNS: Dissolution proceedings; Butsaya dissolution without disposition; DVRO fraud
- THIS CITIZEN OWNS: Federal immigration law framework (INA); USCIS processes; removal proceedings; CA TRUST Act (GOV §§7282-7284); interpreter standards; immigration documentation authentication; trafficking victim protections (T/U visas)
- Cross-reference heavily — immigration issues are almost always ancillary to a primary case

---

## ANCHOR STATUTES — FETCHED AND READY

### GOV CODE § 7284 — California Values Act (citation)
**Text:** FETCHED (full text — 2026-04-12)
**Key holding:** GOV §7284 is the naming/citation section only: "This chapter shall be known, and may be cited, as the California Values Act."
**NOTE:** The operative provisions are §§7282-7284.10. The substance is in §7284.2-§7284.6.
**Standard ID:** Cross-reference — fetch §7284.2-§7284.6 for operative content

---

## ANCHOR STATUTES — FETCH REQUIRED

### GOV CODE § 7282.5 — Conditions for honoring immigration detainer
- **What it does:** Law enforcement agency may only honor civil immigration detainer if: (1) individual has prior felony conviction; (2) is on sex offender registry; (3) has been convicted of certain crimes; (4) ICE warrant exists; otherwise California agencies SHALL NOT detain
- **Fetch:** leginfo → GOV § 7282.5
- **Standard ID:** `gov_7282_5_immigration_detainer_conditions`

### GOV CODE § 7284.6 — TRUST Act prohibitions on California law enforcement
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§7284.6(a)(1):** CA law enforcement agencies SHALL NOT use agency moneys or personnel to investigate, interrogate, detain, detect, or arrest persons for immigration enforcement — including:
  - **(A)** Inquiring into individual's immigration status
  - **(B)** Detaining on basis of a hold request
  - **(C)** Providing person's release date or responding to notification requests (unless info publicly available OR in response to notification request per §7282.5)
  - **(D)** Providing personal information (home/work address) unless publicly available
  - **(E)** Making or intentionally participating in arrests based on civil immigration warrants
  - **(F)** Assisting immigration authorities in 8 USC §1357(a)(3) activities
  - **(G)** Performing functions of immigration officer under 8 USC §1357(g) or any other law
- **§7284.6(a)(2):** Cannot place peace officers under federal immigration supervision; cannot deputize as special federal immigration deputies
- **§7284.6(a)(3):** Cannot use immigration authorities as interpreters for law enforcement matters
- **§7284.6(a)(4):** Cannot transfer individual to immigration authorities UNLESS judicial warrant, judicial probable cause determination, OR §7282.5 criteria met
- **§7284.6(b)(4) — T/U VISA EXCEPTION:** Agencies may make inquiries necessary to certify potential crime/trafficking victim for T or U visa under 8 USC §§1101(a)(15)(T)/(U) — THIS IS AFFIRMATIVELY PERMITTED
- **§7284.6(c):** Annual reporting to DOJ of joint task force activity; public records subject to CPRA
**Application — fraud control mechanism:** If immigration enforcement threats were used against Butsaya or other parties, those threats violated §7284.6. If APD officers communicated immigration status information to federal authorities without judicial warrant, each communication = separate §7284.6 violation. T/U visa certification inquiry exception (§7284.6(b)(4)) creates a law enforcement cooperation pathway for trafficking/crime victims.
**Standard ID:** `gov_7284_6_trust_act_prohibitions`

### 8 USC § 1101 — INA definitions
- **What it does:** Core definitions for Immigration and Nationality Act; "alien," "immigrant," "nonimmigrant," "refugee," "admission," "lawful permanent resident"
- **Fetch:** uscode.house.gov → Title 8 → § 1101
- **NOTE:** MCP tool blocked — flag for direct fetch at build time

### 8 USC § 1229a — Removal proceedings
- **What it does:** Exclusive procedures for removal; immigration judge jurisdiction; respondent rights; continuances; voluntary departure; appeals to BIA
- **Fetch:** uscode.house.gov → Title 8 → § 1229a
- **NOTE:** MCP tool blocked

### 8 USC § 1227 — Deportable aliens
- **What it does:** Classes of aliens deportable after admission; criminal ground; domestic violence/child abuse conviction; fraud in admission; marriage fraud
- **Application:** If marriage to Butsaya involved fraud by either party; criminal conduct as ground for removal
- **Fetch:** uscode.house.gov → Title 8 → § 1227
- **NOTE:** MCP tool blocked

### 8 USC § 1101(a)(15)(U) — U visa (crime victim nonimmigrant)
- **What it does:** Nonimmigrant status for alien victims of certain crimes who have suffered abuse and are helpful to law enforcement; qualifying crimes include domestic violence, sexual assault, trafficking, stalking
- **Application:** If Butsaya was a victim of domestic violence (not the fabricated DVRO, but actual abuse in the scheme) — U visa pathway provides immigration protection and law enforcement cooperation mechanism
- **Standard ID:** `ina_u_visa_crime_victim`
- **NOTE:** MCP tool blocked — cite as 8 USC §1101(a)(15)(U)

### 8 USC § 1101(a)(15)(T) — T visa (trafficking victim)
- **What it does:** Nonimmigrant status for victims of severe trafficking; must be present in US due to trafficking; must comply with reasonable requests for assistance in investigation/prosecution
- **Application:** If the control system (conservatorship, compound identity scheme) constitutes trafficking under federal law — T visa pathway
- **Standard ID:** `ina_t_visa_trafficking_victim`
- **NOTE:** MCP tool blocked

---

## CA COURT INTERPRETER REQUIREMENTS — FETCH REQUIRED

### CRC Rule 2.890 — Court interpreter standards
- **What it does:** Qualifications for court interpreters; certified interpreter requirement in criminal proceedings; registered interpreter in civil; parties' right to interpreter
- **Fetch:** California Rules of Court → Rule 2.890 (courts.ca.gov/rules)
- **Standard ID:** `crc_2890_court_interpreter`

### GOV CODE § 68566 — Right to interpreter in civil proceedings
**Status:** NOT FOUND IN D1 DATABASE — fetch via courts.ca.gov at build time
- **What it does:** In any civil proceeding, upon request, court shall appoint interpreter at county expense for party who cannot understand/speak English
- **NOTE:** GOV §68566 returned no result from VernenLegal MCP tool. Likely in the Courts Administration section. Courts.ca.gov → Interpreter Program is the authoritative source.
- **Standard ID:** `gov_68566_civil_interpreter_right`

### EVID CODE § 752 — Interpreter for witnesses
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§752(a):** When witness is incapable of understanding or expressing in English → interpreter who can understand witness AND whom witness can understand SHALL be sworn
- **§752(b)(1):** Criminal actions and juvenile court: interpreter compensation = CHARGE AGAINST THE COURT
- **§752(b)(2):** Civil actions: compensation apportioned among parties as court determines; may be taxed as costs
**Application:** Thai-speaking witnesses in Butsaya dissolution proceedings, Thai translation authentication, any proceeding involving Butsaya or other Thai-speaking parties. The interpreter must be sworn — unsworn translations are not §752-compliant. Civil action cost-apportionment rule means pro se party may bear portion of interpreter cost — relevant to access to justice analysis.
**Standard ID:** `evid_752_interpreter_oath`

---

## CASE LAW SEEDS

1. **INS v. Cardoza-Fonseca**, 480 U.S. 421 (1987) — Asylum "well-founded fear" standard; lower than refugee persecution standard; subjective component
2. **Zadvydas v. Davis**, 533 U.S. 678 (2001) — Post-removal-order detention; due process limits on indefinite detention of deportable alien; 6-month presumptive limit
3. **Padilla v. Kentucky**, 559 U.S. 356 (2010) — CRITICAL: Defense counsel MUST advise non-citizen client of deportation consequences of criminal plea; failure = ineffective assistance of counsel; relevant to any criminal case involving non-citizen party
4. **United States v. Brignoni-Ponce**, 422 U.S. 873 (1975) — Border patrol stops; race alone insufficient for reasonable suspicion; appearance of Mexican ancestry alone cannot justify stop
5. **Lopez v. Gonzales**, 549 U.S. 47 (2006) — State drug offense that is a felony under state law but only a misdemeanor under federal law does not constitute an "aggravated felony" for removal purposes — state/federal classification mismatch analysis

---

## STANDARDS OF CREATION (document types this Citizen audits)

- **Certified translation** — Thai-to-English; ATA (American Translators Association) certification; translator's sworn declaration; document-by-document certification required
- **Court interpreter certification** — Certified Court Interpreter Program (Judicial Council); language roster; continuous education requirements
- **USCIS petition/application** — I-130 (family-based); I-485 (adjustment of status); I-751 (removal of conditions on residence); I-918 (U visa petition)
- **Notice to Appear (NTA)** — Form I-862; initiates removal proceedings; must state factual allegations and charges; service requirements
- **Immigration court order** — BIA or IJ order; final order of removal; voluntary departure order
- **Visa petition** — DS-160; K-1 (fiancée visa); supporting documentation requirements

---

## SOC CONTROLS

- **USCIS** — United States Citizenship and Immigration Services; adjudicates petitions and applications
- **EOIR (Executive Office for Immigration Review)** — Immigration courts (IJs) + BIA; removal proceedings
- **ICE (Immigration and Customs Enforcement)** — Detention and removal operations; civil immigration enforcement
- **DOS (State Department)** — Visa issuance; consular processing
- **California Courts Interpreter Program** — Certified interpreter registry; language testing; complaints
- **ATA (American Translators Association)** — Translator certification; translation standards

---

## FIVE-LAYER STANDARDS TO BUILD

| Standard ID | Statute/Rule | Priority |
|---|---|---|
| `gov_7284_6_trust_act_prohibitions` | GOV §7284.6 — TRUST Act (fetch needed) | BUILD FIRST |
| `crc_2890_court_interpreter` | CRC Rule 2.890 — interpreter qualification | BUILD SECOND |
| `evid_752_interpreter_oath` | EVID §752 — interpreter as officer (fetch needed) | BUILD THIRD |
| `ina_u_visa_crime_victim` | 8 USC §1101(a)(15)(U) — U visa (fetch needed) | BUILD FOURTH |
| `gov_68566_civil_interpreter_right` | GOV §68566 — civil interpreter right (fetch needed) | BUILD FIFTH |

---

## BUTSAYA DISSOLUTION — SPECIFIC FINDINGS

Butsaya (Thai national) dissolution without disposition creates several immigration-adjacent issues:

1. **Immigration status after dissolution:** If Butsaya's immigration status was dependent on marriage — dissolution without properly addressing immigration status = potential removal ground; OR exploitation of immigration vulnerability to compel unfavorable dissolution terms
2. **DV status manipulation:** Fabricated DVRO (per family law audit findings) against Michael could have been used to: (a) support Butsaya's U visa petition (fraudulently claiming victim status); OR (b) prevent Michael from contesting dissolution terms under threat of immigration enforcement
3. **Marital fraud angle:** If the marriage itself was fraudulent (entered for immigration benefit) — 8 USC §1325(c) crime; but evidence points to the DVRO as the fraud mechanism, not the marriage
4. **Dissolution without disposition:** Thai property rights (Butsaya's home country); any property in Thailand; Thai family law vs. CA family law; forum selection; enforcement of CA order in Thailand

---

## HISTORICAL CHAIN SEED

**The wound:** The Immigration Marriage Fraud Amendments of 1986 created the conditional residence system — a 2-year conditional green card for marriage-based immigrants, removable jointly with the sponsoring spouse. The Legislature's intent was to prevent fraudulent marriages for immigration benefit. The wound: it gave abusive spouses a weapon. If you control the joint petition to remove conditions, you control your spouse's immigration status. The DVRO route (Violence Against Women Act waiver) was created to address this — a battered immigrant spouse could self-petition without the abuser's cooperation. But the fraud runs both ways: fabricating a DVRO creates the paper record of victimhood, which can be weaponized to claim VAWA protection while the actual immigration manipulation is the control mechanism, not the remedy. The court interpreter requirement exists because a party who cannot understand the proceeding cannot participate in it — and a proceeding conducted in a language someone cannot understand is not due process.

---

## CROSS-REFERENCES

- `CA_Family_Law_Litigator` → Dissolution proceedings; DVRO fraud; Butsaya-Divorce case
- `CA_Criminal_Law_Specialist` → Any criminal proceedings involving non-citizen parties; Padilla obligation
- `CA_Forensic_Document_Specialist` → Certified translation authentication; court interpreter credential verification
- `CA_Communications_Fraud_Litigator` (if built) → SIM swap / impersonation enabling immigration document fraud
- `HERALD` → Will witness NTAs, visa petitions, certified translations, dissolution orders affecting immigration status
