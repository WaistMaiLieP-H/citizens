# SOURCE PREP: CA_Labor_Employment_Litigator
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** ANCHORS_FETCHED (Lab §132a, §1102.5; Gov §12940, §12965)
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary cases:**
- #37: UA Local 342 Identity Replacement — pension frozen, "retired" at 44, ~$2.4M total damages; occupational identity stolen
- #2: Bilateral Ankles (06-14) — bilateral ankle injuries; trade worker occupational injury nexus (Cal. Lab. Code §3209.3)
- SIRVA (#20) — COVID vaccine shoulder injury during employment period; occupational injury nexus if within scope of employment
- SSA "retired at 44" — may have also been used to deny workers comp or OEHS/occupational claims

**Why separate from CA_Civil_Rights_Litigator and Federal ERISA:**
- FEHA (Gov. Code §12940) is the state employment discrimination statute — different elements, different exhaustion, different forum (DFEH/CRD → civil action)
- Lab. Code §132a (workers comp retaliation) lives in WCAB jurisdiction — not superior court
- Both are state employment law, not federal civil rights or ERISA plan benefits

---

## ANCHOR STATUTES — FETCHED AND READY

### CAL. LAB. CODE § 132a — Workers comp retaliation
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **Policy declaration:** "There should not be discrimination against workers who are injured in the course and scope of employment" — this is the promise
- **§132a(1):** MISDEMEANOR to discharge or discriminate against employee who filed or intends to file workers comp claim; compensation INCREASED BY 50% (up to $10K); reinstatement + lost wages
- **§132a(2):** Insurer who advises employer to discharge for filing = misdemeanor
- **§132a(3):** Retaliation for testifying in another worker's case = misdemeanor
- **Jurisdiction:** WCAB — petition to appeals board; NOT superior court employment claims; 1-year SOL from discriminatory act
**Standard ID:** `lab_132a_workers_comp_retaliation`

### CAL. LAB. CODE § 1102.5 — Whistleblower protection
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§1102.5(a):** Cannot adopt rule preventing employee from disclosing information to government/law enforcement if employee has reasonable cause to believe it discloses violation of statute/rule/regulation
- **§1102.5(b):** Cannot retaliate against employee for disclosure to government, person with authority over employee, or person who can investigate/correct
- **§1102.5(c):** Cannot retaliate for refusing to participate in activity that would violate statute/rule/regulation
- **§1102.5(d):** Cannot retaliate for prior-employment disclosures
- **§1102.5(f)(1):** $10,000 CIVIL PENALTY per employee per violation
- **§1102.5(j):** Court may award attorney fees to successful plaintiff
**Standard ID:** `lab_1102_5_whistleblower`

### CAL. GOV. CODE § 12940 — FEHA prohibited employment practices
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings (relevant subsections):**
- **§12940(a):** Cannot refuse to hire, discharge, discriminate in compensation or terms because of physical disability, mental disability, medical condition, age, sex, race, or other protected categories
- **§12940(a)(1)-(2):** Exception if employee cannot perform essential duties with reasonable accommodation
- **§12940(m):** Failure to make REASONABLE ACCOMMODATION for known physical/mental disability = unlawful
- **§12940(n):** Failure to engage in timely, good-faith INTERACTIVE PROCESS = unlawful
- **§12940(h):** Retaliation for opposing FEHA violations = unlawful
- **§12940(j):** Harassment: one or more supervisors, or severe/pervasive hostile environment
- **Application:** If UA342 identity replacement caused employer to record "retired" and deny accommodation/continuation of employment — FEHA §12940(a) may apply
**Standard ID:** `gov_12940_feha_employment`

### CAL. GOV. CODE § 12965 — FEHA civil action procedure
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§12965(a):** DFEH (now CRD) may bring civil action; requires mandatory dispute resolution first
- **§12965(c):** If no civil action within 150 days, CRD issues right-to-sue notice; employee has 1 year from notice to file
- **§12965(c)(1)(D):** Tolled during mandatory dispute resolution
- **§12965(c)(6):** Attorney fees to prevailing plaintiff; frivolous-action standard for defendant fees
- **Application:** Must exhaust administrative remedy (CRD complaint) before filing; 1-year SOL from right-to-sue
**Standard ID:** `gov_12965_feha_civil_action`

---

## ANCHOR STATUTES — FETCH REQUIRED

### CAL. LAB. CODE § 3209.3 — Workers comp injury definition
- **What it does:** Defines "injury" to include occupational disease; plumber's bilateral ankle injuries are likely occupational injuries
- **Fetch:** leginfo → LAB § 3209.3
- **Standard ID:** `lab_3209_3_occupational_injury`

### CAL. LAB. CODE § 3600 — Workers comp liability conditions
- **What it does:** Employer liability for industrial injuries; exclusive remedy with exceptions
- **Fetch:** leginfo → LAB § 3600

### CAL. LAB. CODE § 1194 — Minimum wage / overtime civil action
- **What it does:** Employee may sue for unpaid minimum wage or overtime; mandatory attorney fees
- **Fetch:** leginfo → LAB § 1194

### 29 USC § 185 — LMRA § 301 — CBA enforcement (union contracts)
- Already identified in ERISA prep; cross-reference here
- **Why relevant:** UA342 CBA protects workers from discriminatory discharge; §301 in federal court concurrent with FEHA in state court

### CAL. LAB. CODE § 6310 — OSHA retaliation
- **What it does:** Cannot discharge/discriminate against employee who files complaint about workplace safety or testifies in OSHA proceedings
- **Fetch:** leginfo → LAB § 6310

---

## CASE LAW SEEDS

1. **Harris v. City of Santa Monica**, 56 Cal.4th 203 (2013) — FEHA mixed-motive cases; employer cannot escape liability by showing same decision would have been made without discriminatory motive if discrimination was "a substantial factor"
2. **Yanowitz v. L'Oreal USA, Inc.**, 36 Cal.4th 1028 (2005) — Retaliatory acts under FEHA; defining "adverse employment action" broadly; employer cannot retaliate for refusing illegal orders
3. **City of Moorpark v. Superior Court**, 18 Cal.4th 1143 (1998) — FEHA remedies: full back pay, front pay, emotional distress, punitive damages available; not limited to contract damages
4. **Cabesuela v. Browning-Ferris Industries of California, Inc.**, 68 Cal.App.4th 101 (1998) — §132a WCAB jurisdiction is exclusive for workers comp retaliation; cannot sue in superior court; but wrongful discharge in violation of public policy may overlap
5. **Tameny v. Atlantic Richfield Co.**, 27 Cal.3d 167 (1980) — Wrongful discharge in violation of public policy (not a statute-based claim); tortious wrongful termination; available in superior court as parallel to §132a WCAB proceedings

---

## STANDARDS OF CREATION (document types this Citizen audits)

- **FEHA complaint to CRD** — Mandatory administrative form; specific elements required; verified complaint
- **DFEH/CRD right-to-sue notice** — Triggers 1-year civil action SOL; must be attached to complaint
- **WCAB petition** — Workers comp appeals board form; §132a petition specific requirements
- **Workers comp claim form (DWC-1)** — Employer must provide within 1 business day of injury report
- **Interactive process documentation** — Reasonable accommodation requests, employer responses, meeting records
- **Reasonable accommodation records** — Written confirmation of what was offered and accepted/rejected
- **UA342 pension records** — CBA, contribution history, pension statement showing "retired at 44"

---

## SOC CONTROLS

- **CRD investigation records** — DFEH/CRD complaint number, investigation status
- **WCAB case file** — All WCAB proceedings have public docket; case number tracks
- **Cal/OSHA inspection records** — If workplace injury reported; 6330 form
- **EDD (Employment Development Dept.)** — Unemployment records; if employer reported termination vs. retirement vs. leave

---

## FIVE-LAYER STANDARDS TO BUILD

| Standard ID | Statute/Rule | Priority |
|---|---|---|
| `gov_12940_feha_employment` | Gov. §12940 — FEHA discrimination/accommodation | BUILD FIRST |
| `lab_132a_workers_comp_retaliation` | Lab. §132a — WC retaliation (WCAB) | BUILD SECOND |
| `lab_1102_5_whistleblower` | Lab. §1102.5 — whistleblower | BUILD THIRD |
| `gov_12965_feha_civil_action` | Gov. §12965 — FEHA procedure/right-to-sue | BUILD FOURTH |
| `lab_3209_3_occupational_injury` | Lab. §3209.3 — occupational injury def | BUILD FIFTH (fetch needed) |

---

## HISTORICAL CHAIN SEED

**The wound:** California's workers compensation system was born in 1913 (Stats. 1913, c. 176) as a no-fault compromise: workers gave up tort rights; employers got liability certainty. The "exclusive remedy" doctrine protected employers from civil suits. §132a (added 1959) was the Legislature's recognition that the system was being weaponized — employers were firing injured workers to avoid comp claims. The promise: disability cannot cost you your job. The wound: the WCAB remedy under §132a ($10K cap, reinstated in a hostile workplace) is weak. The real protection came from layering FEHA (1980) and §1102.5 (1984) on top. Three statutes, three forums, three standards of proof — the worker must navigate all three simultaneously. Identity replacement collapses all three: "retired" at 44 eliminates the worker from the employment system entirely, mooting FEHA claims before they can be filed.

---

## CROSS-REFERENCES

- `US_Federal_ERISA_Litigator` → LMRA §301 (CBA enforcement); pension benefits derive from same employment relationship
- `US_Federal_Civil_Rights_Litigator` → §1983 if state actor involved in employment discrimination
- `CA_Medical_Malpractice_Litigator` → SIRVA occupational injury nexus; bilateral ankles occupational
- `CA_Disability_Rights_Litigator` → ADA Title I (disability in employment) parallels FEHA §12940(m); coordinate
- `HERALD` → Will witness UA342 employment records, CRD/DFEH filings, workers comp history
