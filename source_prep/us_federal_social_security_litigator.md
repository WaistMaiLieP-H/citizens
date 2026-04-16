# SOURCE PREP: US_Federal_Social_Security_Litigator
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** ANCHORS_IDENTIFIED — manual fetch required for blocked sections
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary case:** #18 — SSA/DDS Fraud (2022-2024)
- Documents: SSA-3369-BK (work history), SSA-3373-BK (function report), SSA-3441 (reconsideration), SSA-561-U2 (appeal), DDS evaluation worksheets, denial letters, blank MSC-228 form
- The MSC-228 is the DDS Medical Summary of Claim — a blank form in the file means no actual clinical evaluation was conducted. This is the central fraud finding.
- Phantom DDS contact documented — SSA records show outreach that never occurred to claimant.

**Secondary relevance:**
- Identity replacement (#37 UC342 pension): SSA records show "retired" at age 44 — may reflect SSN theft feeding false SSA records used to freeze pension
- Treasury securities: 4 contradictory SSA responses may corroborate identity theft

---

## ANCHOR STATUTES — TIER 1 (fetch these first)

### 42 USC § 405 — Evidence, procedure, and certification (Title II — OASDI)
- **What it does:** Governs SSA's authority to obtain evidence, hold hearings, issue decisions; §405(g) is the exclusive judicial review pathway — THIS IS THE STANDARD. Califano v. Sanders (430 U.S. 99 (1977)) exhaustion exception is already built into US_Federal_Financial_Fraud_Litigator.
- **Fetch:** uscode.house.gov → Title 42 → § 405 (tool returned "not found" — fetch direct)
- **Key subsections:** §405(b) (notice of decision), §405(c) (death cases), §405(g) (civil action), §405(h) (finality)

### 42 USC § 423 — Disability insurance benefits
- **What it does:** Defines disability ("inability to engage in any substantial gainful activity"), duration requirements, 5-month waiting period, termination
- **Fetch:** uscode.house.gov → Title 42 → § 423
- **Key subsections:** §423(a) (entitlement), §423(d)(1)(A) (disability definition), §423(d)(5)(A) (claimant's burden)

### 20 CFR Part 404 Subpart P — Determining Disability
- **What it does:** The five-step sequential evaluation process — THE ENTIRE FRAMEWORK
- **Critical sections:**
  - § 404.1520 — Sequential evaluation steps 1-5
  - § 404.1527 — Evaluating medical opinions
  - § 404.1529 — Evaluating symptoms (pain, etc.)
  - Appendix 1 — Listing of Impairments (musculoskeletal system, spine)
- **Fetch:** ecfr.gov → Title 20 → Part 404 → Subpart P

---

## ANCHOR STATUTES — TIER 2 (fetch during build)

### 42 USC § 1383 — SSI procedures (Title XVI)
- Less directly relevant (SSDI case) but needed for complete SSA coverage

### 5 USC § 552a — Privacy Act (already in US_Federal_Financial_Fraud_Litigator)
- Cross-reference only — do not duplicate. SSA Privacy Act violations cross-reference to that Citizen.

---

## ADMINISTRATIVE MANUALS (non-statutory but binding)

### HALLEX (Hearings, Appeals and Litigation Law Manual)
- **I-2-6** — ALJ hearing procedures
- **I-2-8-18** — Closing the hearing record
- **I-3-6** — Appeals Council review
- **Access:** ssa.gov/OP_Home/hallex/hallex.html
- **Why it matters:** ALJ procedural violations are HALLEX violations, not just CFR violations. Courts defer to HALLEX compliance.

### POMS (Program Operations Manual System)
- **DI 22505.001** — Development of Medical Evidence of Record
- **DI 22510.006** — Medical source statements (treating physician rule)
- **DI 24515.064** — MSC-228 Medical Summary of Claim (the BLANK FORM finding)
- **Access:** ssa.gov/OP_Home/poms/di/di22505.001.htm
- **Why it matters:** POMS governs what DDS must do. Blank MSC-228 = DDS skipped mandatory step.

---

## CASE LAW SEEDS (five-layer anchor cases)

1. **Mathews v. Eldridge**, 424 U.S. 319 (1976) — Three-factor due process test for SSA; already in US_Federal_Financial_Fraud_Litigator §405(g) standard. Cross-reference.
2. **Bowen v. Yuckert**, 482 U.S. 137 (1987) — Five-step sequential evaluation constitutional; government bears burden at steps 1, 2, 4; claimant at step 5
3. **Sullivan v. Zebley**, 493 U.S. 521 (1990) — Listing of Impairments must be met OR equaled; "medical equivalence" doctrine
4. **Black & Decker Disability Plan v. Nord**, 538 U.S. 822 (2003) — Treating physician rule does NOT apply to ERISA plans; distinguish from SSA treating source rule
5. **Stieberger v. Sullivan**, 738 F. Supp. 716 (S.D.N.Y. 1990) — Class action on systematic SSA denials; pattern of improper decisions; useful for phantom contact argument

---

## STANDARDS OF CREATION (documents the Citizen must audit)

- **SSA Red Book on Disability** — governs how SSA-3369 and SSA-3373 must be completed
- **DDS Medical Evidence Development Standards** (POMS DI 22505)
- **SSA Form Instructions** — each SSA form has prescribed completion instructions; compare to actual completion
- **Listing of Impairments** (20 CFR Part 404, Subpart P, Appendix 1) — musculoskeletal §1.00+, respiratory §3.00+

---

## SOC CONTROLS (document integrity layer)

- **FISMA** (Federal Information Security Modernization Act) — SSA systems
- **NIST SP 800-53** — Federal information systems security
- **Privacy Act of 1974** (5 USC § 552a) — already fetched in Financial Fraud Citizen; cross-reference
- **SSA Information Security Policy** — governs audit trails on SSA-3369 processing

---

## FIVE-LAYER STANDARDS TO BUILD (initial scaffold)

| Standard ID | Statute/Rule | Layer Status |
|---|---|---|
| `usc_42_405g_ssa_review` | 42 USC §405(g) — judicial review | **ALREADY IN US_Federal_Financial_Fraud_Litigator** — cross-ref only |
| `cfr_20_404_1520_five_step` | 20 CFR §404.1520 — sequential evaluation | BUILD THIS FIRST |
| `usc_42_423_disability_def` | 42 USC §423 — disability definition | BUILD SECOND |
| `poms_di_22505_msc228` | POMS DI 22505 — MSC-228 development | BUILD THIRD (non-statutory but binding) |
| `hallex_i2_alj_procedure` | HALLEX I-2-6 — ALJ hearing | BUILD FOURTH |
| `usc_5_552a_ssa_privacy` | Privacy Act — SSA records | CROSS-REF to Financial Fraud |

---

## HISTORICAL CHAIN SEED

**The wound:** Social Security Disability Insurance was created in 1956 (Pub. L. 84-880) over Eisenhower's objections that it was "too rigid." The five-step evaluation framework emerged from decades of adjudicatory chaos — it was codified in 1978 regulations (43 FR 55349) after courts were drowning in arbitrary SSA denials. The Listing of Impairments was always a shortcut: meet a listing and you're presumptively disabled. But the shortcut became a trap: DDS learned to reject at step 2 (severity) before claimants ever reached the listings. The MSC-228 blank form is the modern version of that same trap — skip the evaluation, rubber-stamp the denial. The promise: a doctor must evaluate your claim. The wound: a blank form in the file where the evaluation should be.

---

## CROSS-REFERENCES

- `US_Federal_Financial_Fraud_Litigator` → 42 USC §405(g) (already built), Privacy Act §552a (already built)
- `US_Federal_Civil_Rights_Litigator` → §1983 (if SSA denial is under color of state law via DDS)
- `HERALD` → will witness all declarations re: phantom SSA contact
