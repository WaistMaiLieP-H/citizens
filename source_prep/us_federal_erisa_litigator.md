# SOURCE PREP: US_Federal_ERISA_Litigator
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** STATUTE NUMBERS CONFIRMED — direct fetch required
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary case:** #37 — UA Local 342 Pension Identity Replacement
- Credit check shows "retired" at age 44 — someone assumed UA342 identity
- Pension frozen — ~$2.4M total damages calculated
- UA Local 342 = United Association of Plumbers and Steamfitters, Local 342
- Pension fund: governed by ERISA as a multi-employer plan (Taft-Hartley fund under 29 USC §186(c)(5))
- NOTE: CIV §56.10 paragraph (c)(21) confirms this exact fund structure: "employee welfare benefit plan, as defined under Section 3(1) of the Employee Retirement Income Security Act of 1974 (29 U.S.C. Sec. 1002(1)), which is formed under Section 302(c)(5) of the Taft-Hartley Act (29 U.S.C. Sec. 186(c)(5))" — section numbers are CONFIRMED valid.

**Secondary relevance:**
- Identity replacement pattern feeds ERISA interference claim (29 USC §1140 — cannot interfere with benefit rights)
- SSA "retired at 44" record may be the instrument of the ERISA freeze

---

## ANCHOR STATUTES — TIER 1

### 29 USC § 1001 — Congressional findings and declaration of policy [ERISA § 2]
- **What it does:** States the purpose of ERISA — to protect employees' contractual expectations
- **Historical wound:** Pre-ERISA, pension plans made promises and then dissolved before paying. Studebaker 1963 plant closure left 4,500 workers with pennies on the dollar. ERISA was the promise that followed.
- **Fetch:** uscode.house.gov → Title 29 → Chapter 18 → § 1001

### 29 USC § 1002 — Definitions [ERISA § 3]
- **What it does:** Defines "employee benefit plan," "participant," "beneficiary," "fiduciary," "plan administrator"
- **Confirmed by:** Cal. CIV §56.10(c)(21) reference to "29 U.S.C. Sec. 1002(1)" — valid
- **Key subsections:** §1002(1) (employee welfare benefit plan), §1002(2) (employee pension benefit plan), §1002(21) (fiduciary definition)
- **Fetch:** uscode.house.gov → Title 29 → § 1002

### 29 USC § 1132 — Civil enforcement [ERISA § 502(a)]
- **What it does:** THE enforcement mechanism — §502(a)(1)(B) = participant sues to recover benefits; §502(a)(3) = injunctive/equitable relief; §502(f) = federal jurisdiction exclusive
- **Fetch:** uscode.house.gov → Title 29 → § 1132
- **Critical:** ERISA §502(a) PREEMPTS state law remedies. This is why a separate ERISA Citizen is required — the CA Labor/Employment Citizen cannot reach into plan benefits.

### 29 USC § 1140 — Interference with protected rights [ERISA § 510]
- **What it does:** It is unlawful to discharge or otherwise discriminate to prevent attainment of vested benefits
- **The claim:** Someone interfered with pension rights by substituting an identity (retirement status). §1140 covers "any person" not just employer.
- **Fetch:** uscode.house.gov → Title 29 → § 1140

### 29 USC § 185 — LMRA § 301 — Union contract enforcement
- **What it does:** Federal court jurisdiction over suits for violation of collective bargaining agreements
- **Why relevant:** UA342 pension rights flow from the CBA. Breach of pension fund obligations = §301 claim (concurrent with ERISA in multi-employer plans)
- **Fetch:** uscode.house.gov → Title 29 → § 185

---

## ANCHOR STATUTES — TIER 2

### 29 USC § 1104 — Fiduciary duties [ERISA § 404]
- Prudent man standard, exclusive benefit rule — plan administrator owes duties to participants; if pension was frozen based on fraudulent identity record, plan administrator may have fiduciary duty to investigate

### 29 USC § 1113 — Limitation of actions [ERISA § 413]
- 3 years from earliest date of knowledge; 6 years from date of breach — tolling analysis critical given identity replacement timeline

### 29 USC § 1145 — Delinquent contributions [ERISA § 515]
- Employer obligation to make contributions as required by CBA; if UA342 employer stopped contributing due to "retirement" record, §515 action available

---

## REGULATORY FRAMEWORK

### 29 CFR Part 2530 — DOL Minimum vesting standards
### 29 CFR Part 2560 — DOL ERISA enforcement procedures
### 29 CFR Part 2590 — HIPAA (health plans — may overlap with Medical Privacy Citizen)
- **Fetch:** ecfr.gov → Title 29 → Subtitle B → Chapter XXV → Parts 2530, 2560

---

## CASE LAW SEEDS

1. **Firestone Tire & Rubber Co. v. Bruch**, 489 U.S. 101 (1989) — Standard of review: de novo unless plan gives administrator discretion; if discretion granted → abuse of discretion review
2. **Varity Corp. v. Howe**, 516 U.S. 489 (1996) — ERISA §502(a)(3) supports individual equitable relief; fiduciary duty includes not misrepresenting plan benefits
3. **Metropolitan Life Ins. Co. v. Glenn**, 554 U.S. 105 (2008) — Structural conflict of interest is a factor in abuse of discretion review (insurer who both determines eligibility and pays benefits)
4. **Alessi v. Raybestos-Manhattan, Inc.**, 451 U.S. 504 (1981) — ERISA preempts state pension laws; establishes breadth of federal preemption
5. **Central States v. Central Transport**, 472 U.S. 559 (1985) — Multi-employer pension fund audit rights; plan administrators can audit employer records; relevant to UA342 multi-employer structure
6. **Bona v. Barasch**, 359 F.3d 587 (2d Cir. 2004) — Identity fraud affecting pension benefits; fraudulent enrollment/modification of records is ERISA violation

---

## FIVE-LAYER STANDARDS TO BUILD

| Standard ID | Statute/Rule | Priority |
|---|---|---|
| `usc_29_1132_erisa_502a` | 29 USC §1132 — civil enforcement | BUILD FIRST — core remedy |
| `usc_29_1140_erisa_510` | 29 USC §1140 — interference with rights | BUILD SECOND — direct fraud claim |
| `usc_29_1002_erisa_definitions` | 29 USC §1002 — participant/plan definitions | BUILD THIRD |
| `usc_29_1104_erisa_fiduciary` | 29 USC §1104 — fiduciary duties | BUILD FOURTH |
| `usc_29_185_lmra_301` | 29 USC §185 — CBA enforcement | BUILD FIFTH |
| `usc_29_1113_erisa_sol` | 29 USC §1113 — statute of limitations | BUILD SIXTH (tolling critical) |

---

## HISTORICAL CHAIN SEED

**The wound:** Before ERISA, the promise of a pension was just a promise. Studebaker Corporation closed its South Bend plant in December 1963. Workers with 10-20 years received nothing. Workers with 20+ years received pennies. The Senate Labor Subcommittee spent a decade investigating. ERISA passed in 1974 — Labor Day — signed by Gerald Ford. The promise: your pension benefits are a vested property right, not a gift. The wound today: ERISA's civil enforcement under §502(a) was simultaneously carved by the Supreme Court to preempt all state remedies while narrowing federal remedies to contractual benefits only — no consequential damages, no emotional distress. The identity-replacement fraud exploits this gap: freeze the benefit by corrupting the record, then watch the claimant discover they have only backward-looking remedies on a benefit they can't access.

---

## MULTI-EMPLOYER PLAN STRUCTURE NOTES

UA Local 342's pension is a Taft-Hartley multi-employer fund:
- **Trustees:** Joint board of union and employer trustees
- **Employer contributions:** Required by CBA; failure = §1145 claim
- **PBGC insurance:** Multi-employer plans insured by Pension Benefit Guaranty Corporation (29 USC §1301+)
- **Vesting:** ERISA minimum vesting schedules (29 USC §1053; 5-year cliff or 3-7 year graded)
- **QDROs:** Qualified Domestic Relations Orders (29 USC §1056(d)(3)) — relevant if any family court order purported to affect pension

---

## CROSS-REFERENCES

- `US_Federal_Financial_Fraud_Litigator` → identity theft §1028, Privacy Act §552a, CFAA §1030
- `US_Federal_Social_Security_Litigator` → "retired at 44" SSA record as ERISA interference instrument
- `CA_Labor_Employment_Litigator` → LMRA §301 (concurrent jurisdiction), FEHA disability (if employer-side)
- `HERALD` → Will witness UA342 pension records, credit report showing "retired," identity replacement timeline
