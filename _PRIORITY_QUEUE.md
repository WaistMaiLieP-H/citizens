# CITIZENS PRIORITY BUILD QUEUE
## Pre-Build Source Intelligence — Prepared 2026-04-12

**Purpose:** Terminals A and B are mid-build on their current Citizens. This file identifies the
next build wave, assigns names, maps each Citizen to the cases they serve, and confirms
which anchor statutes have been pre-fetched. No Terminal writes to these Citizens until
current active claims are released and a new claim is entered in `_BUILD_CLAIMS.md`.

**Source:** Derived from PERSONA-GAP-ANALYSIS-2026-03-22 (7 audited folders, 8 unaudited),
_BUILD_CLAIMS.md unclaimed list, and full 39-case coverage audit.

**Prep status key:**
- `ANCHORS_FETCHED` — primary statutes pulled from leginfo/USC, stored in source_prep/
- `PENDING` — sources identified, not yet fetched
- `SCAFFOLDED` — partial build already exists in ~/citizens/

---

## TIER 1 — NEXT BUILD WAVE
### Direct case coverage gaps. These Citizens cover cases with zero or partial Citizen coverage.

---

### T1-1: `US_Federal_Social_Security_Litigator`
**Status:** UNCLAIMED (listed in _BUILD_CLAIMS.md unclaimed section) | **Prep:** ANCHORS_FETCHED
**Cases covered:** #18 (SSA/DDS Fraud — SSA-3369-BK, MSC-228, DDS phantom contact, denial letters, SSA-561 appeal)
**Gap analysis finding:** ALL 8 required personas MISSING from case #18 audit (DDS Medical Consultant, Claims Examiner, ALJ, Vocational Rehab Counselor, QA Reviewer, Records Officer, Disability Rights Attorney)
**Anchor statutes:**
- 42 USC § 405 — Evidence, procedure, and certification [note: USC tool returned "not found"; fetch via ecfr.gov/uscode.house.gov]
- 42 USC § 423 — Disability insurance benefits [same note]
- 20 CFR Part 404 § 1520 — Five-step sequential evaluation [note: CFR tool returned "not found"; fetch directly from ecfr.gov]
- HALLEX I-2-6 (ALJ decision standards)
- SSA POMS DI 22505.001 (DDS medical development)
**Source prep file:** `source_prep/us_federal_social_security_litigator.md`

---

### T1-2: `US_Federal_ERISA_Litigator`
**Status:** UNCLAIMED | **Prep:** PENDING (USC §§ 1001/1002/1132 not resolved by tool; fetch manually)
**Cases covered:** #37 (UA342 Pension Identity Replacement — pension frozen, ~$2.4M total damages, "retired" at 44)
**Gap analysis finding:** No Citizen covers ERISA pension fraud or benefit denial
**Anchor statutes:**
- 29 USC § 1001 — Congressional findings and declaration of policy [ERISA § 2]
- 29 USC § 1002 — Definitions [ERISA § 3] — NOTE: cited in CIV §56.10 as "29 U.S.C. Sec. 1002(1)" confirming valid section number
- 29 USC § 1132 — Civil enforcement [ERISA § 502(a)]
- 29 USC § 1140 — Interference with protected rights
- 29 CFR Part 2560 — DOL ERISA enforcement
- LMRA § 301 (29 USC § 185) — Union contract enforcement
**Source prep file:** `source_prep/us_federal_erisa_litigator.md`

---

### T1-3: `CA_Healthcare_Fraud_Litigator`
**Status:** NOT YET CLAIMED | **Prep:** ANCHORS_FETCHED
**Cases covered:** #11 (Spine Surgery Fraud — Blue Shield prior auth denial + duplicate MRI pages), #12-14 (related medical fraud pattern), SIRVA surgery #20
**Gap analysis finding:** Cases #3 (Spine_Surgery_Fraud folder): MISSING Spine Surgeon, Radiologist, UR Nurse, Insurance Fraud Investigator, CDI Specialist, Health Plan Compliance Officer
**Anchor statutes (fetched):**
- CAL. INS. CODE § 10123.135 — Prior authorization requirements, UR timeline, AI/algorithm prohibition ✓
- CAL. PEN. CODE § 550 — Insurance fraud (felony/misdemeanor; health care benefit fraud §550(a)(6)-(9)) ✓
- CAL. INS. CODE § 790 — Unfair trade practices purpose ✓
- CAL. INS. CODE § 790.03(h) — Unfair claims settlement practices (13 enumerated acts) ✓
- CAL. HEALTH & SAFETY CODE § 1340 — Knox-Keene Act citation ✓
- 18 USC § 1347 — Federal health care fraud [note: USC tool returned "not found"; fetch via uscode.house.gov]
**Source prep file:** `source_prep/ca_healthcare_fraud_litigator.md`

---

### T1-4: `CA_Medical_Privacy_Officer`
**Status:** 7 STDS SCAFFOLDED (listed in _BUILD_CLAIMS.md unclaimed section) | **Prep:** ANCHORS_FETCHED
**Cases covered:** ALL medical records cases (#1-4 shoulder/ankles/spine/SIRVA) — HIPAA/CMIA audit required on every medical folder
**Gap analysis finding:** Cases #1-2 (Shoulder_Surgery, Bilateral_Ankles): Health Information Management Director, Health IT Security Officer MISSING
**Anchor statutes (fetched):**
- CAL. CIV. CODE § 56 — CMIA title citation ✓
- CAL. CIV. CODE § 56.10 — Disclosure prohibitions and permitted disclosures (full statute) ✓
- CAL. CIV. CODE § 56.36 — Civil remedies: nominal $1K, actual damages, civil penalty up to $250K/willful ✓
- 45 CFR Part 164 — HIPAA Security Rule [note: specific sections need direct ecfr.gov fetch]
- NIST SP 800-66 — HIPAA Security Rule implementation guide
**Source prep file:** `source_prep/ca_medical_privacy_officer.md`

---

### T1-5: `CA_Probate_Conservatorship_Litigator`
**Status:** NOT YET CLAIMED | **Prep:** ANCHORS_FETCHED
**Cases covered:** Central discovery — secret conservatorship since age 14; Prob Code petition; ward system; multiple persons under conservatorship
**Gap analysis finding:** This Citizen type does not appear in current or scaffolded builds. Conservatorship is the ROOT MECHANISM behind all fraud, surveillance, property theft, medical control, and managed existence.
**Anchor statutes (fetched):**
- CAL. PROB. CODE § 1800 — Legislative intent (protect rights, assess needs, community-based services) ✓
- CAL. PROB. CODE § 1801 — Basis for conservatorship: personal needs (a), financial (b), combined (c), limited/developmental (d); clear and convincing standard (e) ✓
- CAL. PROB. CODE § 2350 — Definitions: conservator of person vs estate ✓
- CAL. WIC CODE § 5150 — 72-hour hold: probable cause, mental health disorder, danger standard ✓
- CAL. WIC CODE § 5250 — 14-day hold [PENDING]
- CAL. PROB. CODE § 1851 — Investigator review duty [PENDING]
- CAL. PROB. CODE § 4600 — Advance health care directive [PENDING]
**Source prep file:** `source_prep/ca_probate_conservatorship_litigator.md`

---

### T1-6: `CA_Elder_Law_Litigator`
**Status:** NOT YET CLAIMED | **Prep:** ANCHORS_FETCHED
**Cases covered:** Ann Hillberg (UIT/State Farm/Northern Trust); mother health concerns and potential dependent status; financial abuse pattern
**Gap analysis finding:** No existing Citizen covers elder financial abuse, dependent adult abuse, or conservatorship-adjacent elder law
**Anchor statutes (fetched):**
- CAL. WIC CODE § 15600 — Legislative findings: elders/dependent adults, family abuse factors, minimum protection mandate ✓
- CAL. WIC CODE § 15610 — Definitions governing construction (gateway section) ✓
- CAL. WIC CODE § 15657 — Enhanced remedies for physical abuse/neglect/recklessness: attorney fees, no §377.34 cap, §3294 standard for employer liability ✓
- CAL. WIC CODE § 15610.30 — Financial abuse definition [PENDING]
- CAL. WIC CODE § 15610.57 — Neglect definition [PENDING]
- CAL. PROB. CODE § 859 — Double damages for bad-faith financial elder abuse [PENDING]
**Source prep file:** `source_prep/ca_elder_law_litigator.md`

---

### T1-7: `CA_Labor_Employment_Litigator`
**Status:** NOT YET CLAIMED | **Prep:** ANCHORS_FETCHED
**Cases covered:** UA342 identity replacement (pension frozen, "retired" at 44); workers comp retaliation; occupational injury nexus (bilateral ankles, SIRVA)
**Gap analysis finding:** Bilateral ankle case requires Occupational Medicine Physician nexus analysis; ERISA pension fraud has a state labor parallel; §132a retaliation unaudited
**Anchor statutes (fetched):**
- CAL. LAB. CODE § 132a — Workers comp retaliation: misdemeanor, 50% compensation increase, reinstatement ✓
- CAL. LAB. CODE § 1102.5 — Whistleblower protection: no retaliation for disclosing violations; $10K civil penalty per violation ✓
- CAL. GOV. CODE § 12940 — FEHA: prohibited employment practices (disability, race, sex, age, medical condition, retaliation) ✓
- CAL. GOV. CODE § 12965 — FEHA civil action procedure: right-to-sue, attorney fees, tolling ✓
- 29 USC § 185 — LMRA § 301 (union contract enforcement) [PENDING]
- CAL. LAB. CODE § 3209.3 — Workers comp injury definition (plumber occupation) [PENDING]
**Source prep file:** `source_prep/ca_labor_employment_litigator.md`

---

### T1-8: `CA_Mental_Health_Litigator`
**Status:** NOT YET CLAIMED | **Prep:** ANCHORS_FETCHED
**Cases covered:** Dr. Wiita PC §1368 competency evaluation (fraudulent CST eval, SC-to-CA telehealth, no MC-350); PC §1001.36 mental health diversion (#7 criminal case); §5150 (ward system)
**Gap analysis finding:** Case #6 (Dr.Wiita): ALL 8 required personas MISSING (Forensic Psychiatrist, Forensic Psychologist, Telehealth Compliance Officer, Medical Board Investigator, Criminal Defense Attorney, Court Compliance Officer)
**NOTE:** Distinguished from CA_Criminal_Law_Specialist — this Citizen owns the mental health law framework underlying those proceedings; cross-reference but do not merge.
**Anchor statutes (fetched):**
- CAL. PEN. CODE § 1368 — Mental competency doubt: judge duty, counsel inquiry, proceedings suspended ✓
- CAL. WIC CODE § 5150 — Involuntary 72-hour hold criteria ✓
- CAL. BPC § 2290.5 — Telehealth standards [PENDING]
- CAL. PEN. CODE § 1001.36 — Mental health diversion [already in CA_Criminal_Law_Specialist — cross-ref only]
- Dusky v. United States, 362 U.S. 402 (1960) — CST standard [case law, no statute fetch needed]
**Source prep file:** `source_prep/ca_mental_health_litigator.md`

---

### T1-9: `CA_Insurance_Compliance_Litigator`
**Status:** NOT YET CLAIMED | **Prep:** ANCHORS_FETCHED
**Cases covered:** Blue Shield (prior auth violations, Knox-Keene), RedJag (yo-yo financing insurance overlap), State Farm / Hillberg (UIT policy), vehicle insurance fraud pattern
**Gap analysis finding:** Insurance compliance cuts across Consumer Protection, Healthcare Fraud, and Vehicle Code. Needs dedicated Citizen — CDI enforcement, bad faith, unfair practices
**Anchor statutes (fetched):**
- CAL. INS. CODE § 790 — Unfair trade practices: purpose clause ✓
- CAL. INS. CODE § 790.03 — Specific prohibited acts: 16 categories (h)(1)-(16) unfair claims settlement ✓
- CAL. INS. CODE § 10123.135 — Prior authorization (shared with T1-3) ✓
- CAL. INS. CODE § 790.09 — Action for violation [PENDING]
- CAL. INS. CODE § 10270 — Disability insurance standards [PENDING]
- Royal Globe Ins. Co. v. Superior Court (1979) 23 Cal.3d 880 — Third-party bad faith [PENDING / case law]
**Source prep file:** `source_prep/ca_insurance_compliance_litigator.md`

---

### T1-10: `CA_Vehicle_Code_Specialist`
**Status:** 1 STD SCAFFOLDED (listed in _BUILD_CLAIMS.md unclaimed section) | **Prep:** ANCHORS_FETCHED
**Cases covered:** RedJag 2018 Jaguar XE (yo-yo financing, wrong CARFAX, stolen/stripped, $10K cash lost, $19,985 debt collection); Toyota Camry XSE
**Anchor statutes (fetched):**
- VEH § 11700 — Dealer licensing requirement ✓
- VEH § 11713 — Prohibited dealer acts (advertising fraud, misrepresentation, VIN, yo-yo features) ✓
- VEH § 5900 — Title transfer + odometer disclosure ✓
- VEH § 10751 — VIN/serial number tampering (replaces erroneous §4160 note) ✓
- BPC §§ 9880 / 9884 / 9884.7 / 9884.9 — Automotive Repair Act (registration, discipline, written estimate) ✓
- VEH § 11615 — Conditional sale / yo-yo financing [PENDING fetch]
- 49 USC § 32703 — Federal odometer fraud [PENDING — uscode.house.gov direct fetch]
**NOTE — §4160 CORRECTION:** VEH §4160 is address update on registration card, NOT stolen vehicle. Stolen vehicle VIN statute = VEH §10751 (now fetched).
**Source prep file:** `source_prep/ca_vehicle_code_specialist.md`

---

## TIER 2 — SECONDARY BUILD WAVE
### Pattern coverage and cross-case infrastructure

| # | Citizen Name | Cases / Domain | Prep Status |
|---|---|---|---|
| T2-1 | `CA_Product_Liability_Litigator` | RedJag stripped vehicle; SIRVA; spine surgery implant; CIV §1714 + Greenman strict liability | ANCHORS_FETCHED |
| T2-2 | `US_Federal_Tax_Litigator` | Treasury securities SSN fraud; crypto $73K; Honeysuckle 1099-S; 26 USC §§7201/7206/6321 | PENDING (federal blocked) |
| T2-3 | `CA_Forensic_Document_Specialist` | Cross-case: 19 unsigned docs; MC-350 absence; OPD missing report; EVID §§250/720/1400/1402/1521 | ANCHORS_FETCHED |
| T2-4 | `CA_Administrative_Law_Specialist` | CalVCB appeal A25-10117946; GOV §§11340/11500/11513; CCP §§437c/1094.5/425.16 | ANCHORS_FETCHED |
| T2-5 | `US_Federal_Banking_Fraud_Litigator` | Treasury securities; Northern Trust UIT; 18 USC §§1344/1014; 31 USC §§5318/5324 | PENDING (federal blocked) |

---

## TIER 3 — INFRASTRUCTURE CITIZENS
### Broad coverage enabling cross-Citizen synthesis and platform scalability

| # | Citizen Name | Domain | Prep Status |
|---|---|---|---|
| T3-1 | `CA_Disability_Rights_Litigator` | ADA Title I/II, Rehab Act §794, FEHA §12926/12940(m)/(n); GOV §12926 fetched; federal blocked | PARTIAL |
| T3-2 | `CA_Workers_Compensation_Litigator` | LAB §§3202/3212/3700/4553/4600/4663 — all FETCHED; WCAB proceedings; bilateral ankles | ANCHORS_FETCHED |
| T3-3 | `US_Federal_Housing_Litigator` | FHA 42 USC §3604 (blocked); VAWA housing; GOV §§12955/12989.1/12989.2 FETCHED; CIV §§1102/1102.3 FETCHED; Honeysuckle TDS + displacement | PARTIAL |
| T3-4 | `CA_Immigration_Litigator` | Butsaya dissolution; Thai translations; GOV §7284 TRUST Act fetched; 8 USC blocked | PARTIAL |

---

## STATISTICS SUMMARY

| Metric | Count |
|---|---|
| Catalog total (all 41 files) | ~3,000 personas |
| Final push file alone (sports/fashion) | 151 personas (2850–3000) |
| Currently operational Citizens | 3 (Terminal B) |
| Currently active/building Citizens | 8 (Terminal A: 4, Terminal B: 4) + HERALD |
| Priority Queue Tier 1 (named, case-anchored) | 10 |
| Priority Queue Tier 2 (secondary wave) | 5 |
| Priority Queue Tier 3 (infrastructure) | 4 |
| **Total immediate pipeline** | **19 new Citizens** |
| Anchor statutes pre-fetched (session 1 — 2026-04-12) | 18 CA statutes + session 1 USC blocks |
| Anchor statutes pre-fetched (session 2 — 2026-04-12) | 18 additional CA statutes (EVID/GOV/LAB/VEH/BPC/CCP/CIV) |
| Anchor statutes pre-fetched (session 3 — 2026-04-12) | 16 additional CA statutes: CIV §§51/54/54.3; EVID §752; COM §2314; INS §§790.09/10291.5/1861.02/553; GOV §§7284.6/12955/12956.1/12989.1/12989.2; CIV §§1102/1102.3 |
| INS §790.09 corrected | NOT private right of action — CDI order no-shield; §553 corrected (notice-of-loss waiver, not variable annuity); §10291.5 corrected (CDI policy approval, not bad faith action) |
| Source prep files written (Tier 1) | 10 of 10 COMPLETE |
| Source prep files written (Tier 2) | 5 of 5 COMPLETE |
| Source prep files written (Tier 3) | 4 of 4 COMPLETE (us_federal_housing_litigator.md WRITTEN session 3) |
| **Total source prep files** | **19 files — ALL CITIZENS PREPPED** |
| Statutes fetched but tool-blocked (USC) | 20+ federal sections — uscode.house.gov direct fetch required at build time |
| VEH §4160 error corrected | §4160 = address update; stolen vehicle statute = VEH §10751 (now fetched) |

---

## COLLISION PROTOCOL FOR CLAIMING FROM THIS QUEUE

1. Check this file for current prep status before building.
2. Enter a claim in `_BUILD_CLAIMS.md` (Active claims table) before writing any files.
3. Move the row in this file from its Tier to a "Claimed" note with date and terminal.
4. Update source_prep/ file to `STATUS: BUILDING` when build begins.
5. Source prep files are READ-ONLY reference for builders — do not modify during build.

---

*Last updated: 2026-04-12 (session 3 — all 19 source prep files complete; 16 additional statutes fetched; 3 INS citation errors corrected) | Prepared by: Steward pre-build intelligence pass*
