# SOURCE PREP: CA_Insurance_Compliance_Litigator
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** ANCHORS_FETCHED (Ins. §§790/790.03/10123.135/790.09/10291.5/1861.02; §553 citation error corrected)
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary cases:**
- Blue Shield prior authorization (shared with CA_Healthcare_Fraud_Litigator) — CDI complaint pathway; unfair claims practices
- RedJag yo-yo financing — insurance overlap (forced GAP insurance, yo-yo financing scheme involves insurer); Ins. Code §1861.02+ (auto insurance rate regulation)
- State Farm / Hillberg (UIT) — HILLBERGMANN compound identity on State Farm policy; Northern Trust variable product (annuity product = insurance product under Ins. Code)
- Vehicle insurance fraud pattern (Toyota, RedJag)

**Boundary rule:**
- CA_Healthcare_Fraud_Litigator OWNS: §10123.135 prior auth; PC §550 criminal fraud; Knox-Keene
- THIS CITIZEN OWNS: CDI regulatory enforcement framework, bad faith settlement practices (§790.03), unfair practices across ALL insurance lines, California Insurance Code administrative remedies
- §10123.135 is SHARED — cross-reference; build the administrative/CDI pathway here

---

## ANCHOR STATUTES — FETCHED AND READY

### CAL. INS. CODE § 790 — Purpose of unfair practices article
**Text:** FETCHED — "to regulate trade practices in the business of insurance in accordance with the intent of Congress as expressed in [McCarran-Ferguson Act]"
**Use:** Jurisdiction anchor; CDI's authority to regulate derives from this; establishes state primacy over insurance regulation (per McCarran-Ferguson, federal antitrust does not apply to insurance business regulated by state)
**Standard ID:** `ins_790_unfair_practices_purpose`

### CAL. INS. CODE § 790.03 — Specific prohibited acts
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§790.03(a):** Misrepresenting policy terms, benefits, or financial condition
- **§790.03(b):** False or misleading statements in advertising
- **§790.03(h)(1):** Misrepresenting pertinent facts or policy provisions to claimants
- **§790.03(h)(2):** Failing to acknowledge and act reasonably promptly on communications about claims
- **§790.03(h)(3):** Failing to implement reasonable standards for prompt investigation
- **§790.03(h)(4):** Failing to affirm or deny coverage within reasonable time after proof of loss
- **§790.03(h)(5):** Not attempting in good faith to effectuate prompt, fair settlement where liability is reasonably clear
- **§790.03(h)(6):** Compelling insureds to litigate by offering substantially less than amounts ultimately recovered
- **§790.03(h)(13):** Failing to provide reasonable explanation of basis for denial
- **§790.03(h)(14):** DIRECTLY ADVISING CLAIMANT NOT TO OBTAIN AN ATTORNEY
- **§790.03(h)(15):** MISLEADING CLAIMANT AS TO APPLICABLE STATUTE OF LIMITATIONS
- **NOTE:** §790.03(h)(14) and (15) are particularly relevant to the communications fraud pattern
**Standard ID:** `ins_790_03_unfair_claims_settlement`

### CAL. INS. CODE § 10123.135 — Prior authorization (cross-reference from Healthcare Fraud)
**Text:** Already fully fetched — see ca_healthcare_fraud_litigator.md
**Standard ID:** Cross-reference only — do not build separately

---

## ANCHOR STATUTES — FETCHED AND READY (CONTINUED)

### CAL. INS. CODE § 790.09 — CDI order does not relieve civil/criminal liability
**Text:** FETCHED (full text — 2026-04-12)
**⚠️ CORRECTION:** Prior description ("private right of action for §790.03") was WRONG.
**Actual holding:** "No order to cease and desist... shall in any way relieve or absolve such person from any administrative action against the license or certificate of such person, civil liability or criminal penalty under the laws of this State arising out of the methods, acts or practices found unfair or deceptive."
**What this means:** §790.09 CONFIRMS THE MULTI-TRACK SYSTEM. A CDI cease-and-desist order against an insurer does not wipe out: (1) civil tort liability (bad faith, Gruenberg/Brandt track); (2) criminal prosecution; (3) license revocation proceedings. All three tracks run in parallel and independently.
**What §790.09 is NOT:** It does NOT create a private right of action. Moradi-Shalal confirmed that — §790.03 enforcement = CDI only. §790.09 simply means CDI enforcement does not shelter the insurer from civil/criminal consequences.
**Application:** If CDI issues cease-and-desist for §790.03 violations (e.g., advising claimant not to obtain attorney under §790.03(h)(14)), that order: (a) runs against the insurer's license; AND (b) does not prevent a civil bad faith tort suit; AND (c) does not prevent criminal referral. The CDI track is additive, not exclusive.
**Standard ID:** `ins_790_09_cdi_order_no_shield`

### CAL. INS. CODE § 10291.5 — CDI disability policy approval standards
**Text:** FETCHED (full text — 2026-04-12)
**⚠️ CORRECTION:** Prior description ("bad faith refusal to pay; private right of action; punitive damages") was WRONG.
**Actual holding:** Commissioner SHALL NOT approve a disability policy if it:
- **(b)(1):** Contains provisions that are unintelligible, uncertain, ambiguous, abstruse, or likely to mislead
- **(b)(2):** Contains benefit disparities where certain events pay more than 3x other events for the same loss
- **(b)(7):** Benefits are not sufficient to be of "real economic value" to insured
- **(b)(13):** Fails to conform with CA law
- **§10291.5(c):** Health insurance applications cannot be medically discriminatory; must include HIV test notice
- **§10291.5(i):** Commissioner cannot fix rates for disability insurance; liberal construction
**Application:** Blue Shield prior authorization denial for a service that IS covered under the policy form CDI has approved = policy being applied contrary to its approved form. If Blue Shield's policy was approved by CDI under §10291.5 and contains ambiguous terms, the ambiguity is resolved AGAINST the insurer (§10291.5(b)(1) — not approvable if ambiguous → terms construed against insurer). This is the regulatory foundation for the coverage dispute.
**What bad faith private action actually is:** Common law (Gruenberg v. Aetna, 9 Cal.3d 566 (1973)) + CIV §3294 for punitive damages. Not §10291.5.
**Standard ID:** `ins_10291_5_disability_policy_approval`

### CAL. INS. CODE § 1861.02 — Auto insurance rate regulation (Proposition 103)
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§1861.02(a):** Rates determined by four factors in DECREASING ORDER OF IMPORTANCE:
  - (1) Insured's driving safety record
  - (2) Annual miles driven
  - (3) Years of driving experience
  - (4) Other CDI-approved factors with substantial relationship to risk
- **§1861.02(b)(1):** Every person meeting §1861.025 criteria SHALL be qualified to purchase Good Driver Discount policy from insurer of their choice — insurer SHALL NOT REFUSE
- **§1861.02(b)(2):** Good Driver Discount rate = AT LEAST 20% below otherwise applicable rate; rates must be CDI-approved
- **§1861.02(c):** Absence of prior auto insurance coverage ALONE cannot disqualify from Good Driver Discount or affect rates/insurability
- Any criterion used without approval = UNFAIR DISCRIMINATION
**Application — RedJag forced GAP insurance:** If dealer forced GAP insurance as condition of sale at non-CDI-approved rates, or if insurer used unapproved criteria (prior uninsured status) to increase rates above allowed level = §1861.02 violation. Yo-yo financing scheme that required forced insurance products at inflated rates = unfair discrimination per §1861.02(a).
**Standard ID:** `ins_1861_02_prop103_auto_rates`

### CAL. INS. CODE § 553 — Notice of loss defects — waiver
**Text:** FETCHED (full text — 2026-04-12)
**⚠️ CORRECTION:** Prior description ("variable annuity / variable life insurance") was WRONG.
**Actual holding:** "All defects in a notice of loss, or in preliminary proof thereof, which the insured might remedy, and which the insurer omits to specify to him, without unnecessary delay, as grounds of objection, are WAIVED."
**What this means:** If an insured submits a notice of loss or preliminary proof of loss with technical defects (wrong form, missing information, incomplete), the insurer MUST promptly identify those defects as grounds for objection. If insurer fails to timely specify the defects, they are WAIVED — insurer cannot reject the claim on those grounds later.
**Application:** Communications fraud pattern (SIM swap, intercepted calls) may have prevented proper notice of loss communications. If insurer received defective notice and said nothing, the defects are waived under §553. This is a protection against insurer delay-then-deny tactics.
**Standard ID:** `ins_553_notice_of_loss_defect_waiver`

### CAL. INS. CODE § 785 — Life insurance unfair discrimination
- **What it does:** Cannot discriminate in premiums, benefits, or terms based on protected characteristics
- **Fetch:** leginfo → INS § 785 [STILL PENDING]

---

## CASE LAW SEEDS

1. **Moradi-Shalal v. Fireman's Fund Ins. Co.**, 46 Cal.3d 287 (1988) — Overruled Royal Globe; third parties CANNOT sue insurer directly under §790.03; ONLY CDI can enforce §790.03 against insurer; but Brandt/Tomaselli bad faith tort survives as separate theory
2. **Brandt v. Superior Court**, 37 Cal.3d 813 (1985) — Bad faith: attorney fees incurred to recover policy benefits ARE recoverable as element of compensatory damages (not §790.03)
3. **Tomaselli v. Transamerica Ins. Co.**, 25 Cal.App.4th 1269 (1994) — Bad faith tort standard: unreasonable withholding of benefits; conscious disregard standard for punitive damages
4. **Shade Foods, Inc. v. Innovative Prod. Sales & Mktg., Inc.**, 78 Cal.App.4th 847 (2000) — Insured's Brandt fees are separate element of damages; insurer's bad faith must be independently established
5. **Gruenberg v. Aetna Ins. Co.**, 9 Cal.3d 566 (1973) — FOUNDATIONAL insurance bad faith case; "duty to deal fairly and in good faith" is implied in every insurance contract; breach is tort, not just contract

---

## STANDARDS OF CREATION (document types this Citizen audits)

- **Insurance denial letters** — Must comply with §790.03(h)(13) (reasonable explanation); must include appeal rights; must not mislead re: SOL (§790.03(h)(15))
- **CDI complaint records** — CDI complaint number, investigation status, CDI response
- **Insurance policy** — Declarations page, conditions, exclusions; coverage confirmation
- **Claims correspondence file** — All communications between insurer and claimant; timestamps critical for §790.03(h)(2) (acknowledge within reasonable time) and (h)(3) (prompt investigation)
- **Variable annuity / UIT product disclosure** — Prospectus; surrender charges; death benefit; beneficiary designation
- **Auto insurance policy** — Declarations, coverage confirmation, rate basis (for Prop. 103 compliance)
- **SIU referral records** — Insurer's special investigations unit; if SIU notified CDI (mandatory for suspected fraud)

---

## SOC CONTROLS

- **CDI (California Department of Insurance)** — primary regulator; complaint mechanism; enforcement orders; fine database
- **DMHC (Dept. of Managed Health Care)** — Knox-Keene plans specifically; parallel jurisdiction on health insurers
- **FINRA** — variable annuity products regulated as securities; FINRA complaint mechanism parallel to CDI
- **SEC** — Variable annuities are securities; SEC registration and prospectus requirements

---

## FIVE-LAYER STANDARDS TO BUILD

| Standard ID | Statute/Rule | Priority |
|---|---|---|
| `ins_790_03_unfair_claims_settlement` | Ins. §790.03 — unfair claims practices | BUILD FIRST |
| `ins_790_09_civil_action` | Ins. §790.09 — enforcement/civil action | BUILD SECOND (fetch needed) |
| `ins_bad_faith_brandt` | Brandt v. Superior Court — attorney fees as damages | BUILD THIRD (case law standard) |
| `ins_10291_5_disability_bad_faith` | Ins. §10291.5 — disability insurer bad faith | BUILD FOURTH (fetch needed) |
| `ins_1861_02_prop103_rates` | Ins. §1861.02 — Prop. 103 rate approval | BUILD FIFTH (fetch needed) |

---

## MORADI-SHALAL NAVIGATION NOTE (CRITICAL)

The builder must understand and clearly document the Moradi-Shalal wall:
- **§790.03 enforcement = CDI only** — administrative route; CDI can fine, revoke license, order restitution
- **Private plaintiff = bad faith tort** — "unreasonable withholding of benefits" (Gruenberg/Tomaselli); attorney fees recoverable under Brandt as compensatory damages
- **Punitive damages** = require insurer's malice, oppression, or fraud under §3294 standard
- These are THREE PARALLEL TRACKS: CDI administrative, bad faith tort, punitive damages. The builder must map each case to the appropriate track.

---

## HISTORICAL CHAIN SEED

**The wound:** In 1979, the California Supreme Court in Royal Globe created a direct third-party right of action under §790.03 against insurers. For nine years, insurers faced private litigation for bad-faith claims handling. Then Moradi-Shalal (1988) reversed course — the Supreme Court decided the legislature had not intended to create a private right of action, only CDI enforcement. The insurers celebrated. The Legislature did nothing. The wound: insured persons with legitimate grievances now navigate a two-track system where the criminal enforcement (CDI) depends on CDI staffing and priorities, and the civil remedy (bad faith tort) requires proving an unreasonable denial PLUS financing expensive litigation. The §790.03(h)(14) prohibition on "advising a claimant not to obtain the services of an attorney" exists because this actually happens — and it happened here.

---

## CROSS-REFERENCES

- `CA_Healthcare_Fraud_Litigator` → §10123.135 prior auth; PC §550 criminal fraud (shared but different approach)
- `CA_Consumer_Protection_Litigator` → UCL §17200 (unfair practices) may reach insurer conduct; CLRA if consumer insurance product
- `CA_Vehicle_Code_Specialist` → RedJag forced auto insurance; Prop. 103 rate manipulation
- `US_Federal_Financial_Fraud_Litigator` → Wire fraud (18 USC §1343) for insurance fraud wire communications
- `HERALD` → Will witness all insurance denial letters, CDI complaint correspondence, variable annuity documents
