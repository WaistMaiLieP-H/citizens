# SOURCE PREP: CA_Medical_Privacy_Officer
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** ANCHORS_FETCHED | 7 STDS ALREADY SCAFFOLDED
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

This Citizen applies to ALL medical records cases:
- #1: Shoulder Surgery (04-22_Shoulder_Surgery) — Golden State Ortho / John Muir MRI
- #2: Bilateral Ankles (06-14_Bilateral_Ankles) — Muir Orthopaedic 2014
- #3: Spine Surgery Fraud (11-21_Spine_Surgery_Fraud) — Muir Ortho / Blue Shield
- #20: SIRVA (11-21 SIRVA) — Walgreens COVID vaccine / Dr. Wiseman arthroscopy

**Gap analysis finding (folders 1-3):**
MISSING: Health Information Management Director (record completeness/chain of custody), Health IT Security Officer (EHR audit trails, duplicate records), Clinical Documentation Improvement Specialist (e-signature delays)

**Specific forensic findings already documented:**
- E-signature delay: 58 days for post-op note (shoulder surgery)
- Duplicate MRI records in two formats (spine surgery)
- 4 duplicate MRI pages with handwritten annotations (spine surgery)
- PA Kali Koziol signed multiple notes — supervision compliance unverified (shoulder surgery)

---

## ANCHOR STATUTES — FETCHED AND READY

### CAL. CIV. CODE § 56 — CMIA title citation
**Text:** FETCHED — "This part may be cited as the Confidentiality of Medical Information Act."
**Use:** Citation anchor; establishes Part 2.6 of Division 1 of Civil Code as the CMIA framework
**Standard ID:** Foundation section only — cite in all CMIA standards

### CAL. CIV. CODE § 56.10 — Disclosure prohibitions and permitted disclosures
**Text:** FETCHED (full statute — 2026-04-12)
**Key holdings:**
- **Subdivision (a):** DEFAULT RULE — no disclosure without written authorization
- **Subdivision (b):** COMPELLED disclosures (court order, subpoena, valid search warrant, patient's own request under HSC §123100)
- **Subdivision (c)(1):** Permissive disclosure to other providers for treatment
- **Subdivision (c)(2):** Permissive disclosure to payer for billing — but ONLY to extent necessary
- **Subdivision (c)(4):** Permissive to peer review, UR organizations — but only for their stated purpose
- **Subdivision (c)(21):** CRITICAL — expressly authorizes disclosure to Taft-Hartley welfare benefit plans (29 USC §1002(1)) with patient authorization + HIPAA compliance — confirms ERISA/CMIA overlap
- **Subdivision (d):** Prohibits sharing, selling, using for marketing beyond health care services
- **Subdivision (f):** EXPLICIT: no disclosure for immigration enforcement
**Standard ID:** `civ_56_10_cmia_disclosure`

### CAL. CIV. CODE § 56.36 — Civil remedies
**Text:** FETCHED (full statute — 2026-04-12)
**Key holdings:**
- **§56.36(a):** Violation causing economic loss or personal injury = misdemeanor
- **§56.36(b)(1):** Nominal damages: $1,000 per violation (no actual damage required)
- **§56.36(b)(2):** Actual damages
- **§56.36(c)(1):** Negligent disclosure: civil penalty up to $2,500/violation
- **§56.36(c)(2)(A):** Non-professional knowing/willful: up to $25,000/violation
- **§56.36(c)(2)(B):** Licensed professional knowing/willful: $2,500 (1st), $10,000 (2nd), $25,000 (3rd+)
- **§56.36(c)(3)(A):** For financial gain: up to $250,000/violation + disgorgement
- **§56.36(e):** Affirmative defense for HIPAA-compliant covered entities (Business Associate Agreement, proper notification, no medical identity theft, corrective action)
**Standard ID:** `civ_56_36_cmia_remedies`

---

## ANCHOR STATUTES — FETCH REQUIRED

### CAL. CIV. CODE § 56.05 — Definitions
- **What it does:** Defines "medical information," "provider of health care," "patient," "contractor," "health care service plan"
- **Fetch:** leginfo → CIV § 56.05
- **Standard ID:** `civ_56_05_cmia_definitions`

### CAL. HEALTH & SAFETY CODE § 123100 — Patient access to own records
- **What it does:** Patient's right to inspect and copy their own medical records; provider must respond within 5 business days; failure to provide = civil penalty
- **Fetch:** leginfo → HSC § 123100
- **Standard ID:** `hsc_123100_patient_access`

### CAL. HEALTH & SAFETY CODE § 123111 — Records correction
- **What it does:** Patient's right to add statement to record disagreeing with provider's entry
- **Fetch:** leginfo → HSC § 123111

### 45 CFR § 164.312 — HIPAA Technical Safeguards
- **What it does:** Required technical safeguards for electronic PHI: access controls, audit controls, integrity controls, transmission security
- **E-signature delay (58 days) may violate § 164.312(b) (audit controls) if system did not flag unsigned notes**
- **Fetch:** ecfr.gov → Title 45 → Part 164 → § 164.312
- **Standard ID:** `cfr_45_164_312_hipaa_technical_safeguards`

### 45 CFR § 164.501 — HIPAA Minimum Necessary standard
- **What it does:** Covered entity must make reasonable efforts to limit PHI to minimum necessary for each use/disclosure
- **Fetch:** ecfr.gov → Title 45 → Part 164 → § 164.501

---

## CASE LAW SEEDS

1. **Garrett v. Young**, 149 Cal.App.4th 1179 (2007) — CMIA nominal damages available without actual harm; $1,000 per violation; statute construed to protect informational privacy interest
2. **Heller v. Pillsbury Madison & Sutro**, 50 Cal.App.4th 1367 (1996) — Invasion of medical privacy; demonstrates breadth of private right of action
3. **Pettus v. Cole**, 49 Cal.App.4th 402 (1996) — Patient's medical information in workers' comp proceeding improperly disclosed; CMIA provides independent cause of action
4. **Sutter Health v. Superior Court**, 227 Cal.App.4th 1546 (2014) — HIPAA does not preempt CMIA; California may provide greater protections; no private right of action under HIPAA but CMIA fills that gap
5. **In re Google Inc. Cookie Placement Consumer Privacy Litigation**, 806 F.3d 125 (3d Cir. 2015) — For comparative analysis of nominal damages theory in privacy statutes (persuasive, not binding)

---

## STANDARDS OF CREATION (document types this Citizen audits)

- **EHR audit trails** — ASTM E2147 (Audit Trails in Electronic Health Records); HL7 CDA (Clinical Document Architecture)
- **Medical record completion requirements** — California Medical Record Content standards (Title 22 CCR); JCAHO standards
- **E-signature standards** — CCP §1633.7 (UETA); 45 CFR §164.312(d) (authentication)
- **Patient authorization forms** — HIPAA §164.508 (authorization requirements); CMIA §56.11 (form requirements)
- **Release of information logs** — chain of custody from provider to insurer to court

---

## SOC CONTROLS

- **NIST SP 800-66** — HIPAA Security Rule implementation guide
- **SOC 2 Type II** — EHR system (Epic) audit trail requirements
- **HITRUST CSF** — Health Information Trust Alliance certification
- **ONC Health IT Certification** — 21st Century Cures Act certification for EHR systems
- **ASTM E2147** — Audit Trail standard (flags unsigned notes, modification history)

---

## FIVE-LAYER STANDARDS TO BUILD

| Standard ID | Statute/Rule | Priority |
|---|---|---|
| `civ_56_10_cmia_disclosure` | CIV §56.10 — disclosure prohibition | BUILD FIRST — core CMIA rule |
| `civ_56_36_cmia_remedies` | CIV §56.36 — civil remedies schedule | BUILD SECOND — damages framework |
| `civ_56_05_cmia_definitions` | CIV §56.05 — definitions | BUILD THIRD (fetch needed) |
| `hsc_123100_patient_access` | HSC §123100 — patient access | BUILD FOURTH (fetch needed) |
| `cfr_45_164_312_hipaa_technical` | 45 CFR §164.312 — technical safeguards | BUILD FIFTH (fetch needed) |

**NOTE on scaffolded standards:** 7 standards already scaffolded before this session. Builder must audit existing scaffold against five-layer bar before building new. Do not stub — bring existing to bar or mark INCOMPLETE.

---

## HISTORICAL CHAIN SEED

**The wound:** Before CMIA, California patients had no private right of action when a hospital shared their medical records with their employer, their insurance company's marketing department, or their spouse's divorce attorney. The federal Privacy Act (1974) covered federal agencies only. California's CMIA (1981, Stats. 1981, c. 782) was one of the first state medical privacy statutes. The wound it addressed: the medical record was the property of the institution, not the patient. The institution decided who saw it. The 58-day unsigned post-op note is the modern version of that institutional indifference — the record was incomplete for 58 days, the insurer may have received an incomplete record for prior auth purposes, and no system flagged it. The audit trail that §164.312(b) requires would have caught it. It didn't, because the system wasn't audited.

---

## CROSS-REFERENCES

- `CA_Healthcare_Fraud_Litigator` → duplicate MRI pages are both a fraud indicator (§550) and a CMIA/EHR integrity issue (§164.312)
- `CA_Medical_Malpractice_Litigator` → e-signature delay may be both negligence (BPC §2234) and CMIA violation (§56.10)
- `US_Federal_Financial_Fraud_Litigator` → CFAA §1030 (if unauthorized access to EHR) already built; cross-reference
- `HERALD` → Will authenticate medical record chain of custody, flag unsigned notes, document duplicate records
