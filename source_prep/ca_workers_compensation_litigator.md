# SOURCE PREP: CA_Workers_Compensation_Litigator
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** ANCHORS_FETCHED (LAB §§3202/3212/3700/4553/4600/4663)
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary cases:**
- Michael bilateral ankle injuries — industrial injury; employer/insurer interference with treatment; §4600 medical treatment rights; apportionment under §4663
- UA Local 342 identity replacement — "retired at 44" on credit check; pension frozen; possible fraudulent employer reporting to WCAB / falsified injury records
- SIRVA (COVID vaccine Walgreens Brentwood ~11/2021) — occupational nexus question; SIRVA is typically a vaccine injury under VICP, but if vaccine was mandated/encouraged by employer, workers comp nexus may exist; LAB §3212 presumption analysis

**Boundary rule:**
- CA_Labor_Employment_Litigator OWNS: LAB §132a (workers comp retaliation), LAB §1102.5 (whistleblower), GOV §12940 (FEHA disability accommodation)
- THIS CITIZEN OWNS: The WCAB system itself — LAB §§3200-5956; indemnity benefits; medical treatment disputes; apportionment; serious and willful misconduct; DWC procedures
- Do not merge. Cross-reference LAB §132a retaliation TO Labor/Employment Citizen.

---

## ANCHOR STATUTES — FETCHED AND READY

### LAB CODE § 3202 — Liberal construction
**Text:** FETCHED (full text — 2026-04-12)
**Key holding:** "This division and Division 5 (commencing with Section 6300) shall be liberally construed by the courts with the purpose of extending their benefits for the protection of persons injured in the course of their employment."
**Application:** Ambiguities in workers comp coverage, causation, or benefits resolved IN FAVOR OF injured worker; anti-retrenchment canon
**Standard ID:** `lab_3202_liberal_construction`

### LAB CODE § 3212 — Presumption of industrial injury (law enforcement / firefighters)
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- For peace officers, firefighters, CHP, sheriff's staff: hernia, heart trouble, pneumonia PRESUMED industrial if develops during service
- Presumption extends POST-TERMINATION: 3 calendar months per year of service, max 60 months
- Presumption disputable — may be controverted by other evidence
- §3212(e) exception list: §§3212.1-3213.2 (cancer, HIV, PTSD — separate presumptions for specific categories)
**NOTE:** This section's presumption list is not applicable to Michael directly (plumber, not LEO) — but §3212's framework shows California's general philosophy that exposure + disease = presumed industrial. Apply §3202 liberal construction to non-presumption cases.
**Standard ID:** `lab_3212_industrial_presumptions`

### LAB CODE § 3700 — Employer duty to secure compensation
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- Every employer (except State) MUST secure payment of compensation: (a) by licensed insurer; (b) by DI certificate to self-insure; (c) political subdivisions may self-insure with director approval
- Failure to secure = misdemeanor + civil liability
**Standard ID:** `lab_3700_employer_comp_obligation`

### LAB CODE § 4553 — Serious and willful misconduct — 50% enhancement
**Text:** FETCHED (full text — 2026-04-12)
**Key holding:** "The amount of compensation otherwise recoverable shall be increased one-half, together with costs and expenses not to exceed $250, where the employee is injured by reason of the serious and willful misconduct" of employer, managing representative, partner, or corporate executive/managing officer/general superintendent
**Application:** If employer or insurer engaged in fraudulent injury reports, falsified records, or deliberate denial of compensable claim — this is the enhancement mechanism
**Standard ID:** `lab_4553_serious_willful_misconduct_enhancement`

### LAB CODE § 4600 — Medical treatment entitlement
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- Employer must provide ALL reasonably required medical, surgical, chiropractic, acupuncture, hospital treatment to cure or relieve effects of industrial injury
- "Reasonably required" = treatment based on DWC Medical Treatment Utilization Schedule (MTUS) guidelines (§5307.27)
- After 30 days from injury report: employee may choose own physician (unless MPN established)
- Pre-designated personal physician right: if notified employer IN WRITING before injury, employee can see personal physician from day one
- Insurer may require prior auth for non-emergency treatment (utilization review under §4610)
- Employer/insurer NEGLECT OR REFUSAL = liable for employee's reasonable treatment expenses
**NOTE:** §4600(c)/(d) interplay with §4616 (MPN) is critical — MPN can limit physician choice; pre-designation is the workaround
**Standard ID:** `lab_4600_medical_treatment_entitlement`

### LAB CODE § 4663 — Apportionment of permanent disability
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- Apportionment shall be based on CAUSATION
- Physician MUST address apportionment in any PD report — report is INCOMPLETE without it
- Physician must find: % of PD from industrial cause vs. % from other factors (pre-existing conditions, subsequent injuries)
- Employee must disclose previous PD or physical impairments upon request
- **§4663(e) EXCEPTION:** §3212 series exemptions (law enforcement/firefighter presumptions) — apportionment rules do NOT apply to those
**Application:** Bilateral ankle injuries — any prior injuries or conditions will be subject to apportionment; insurer will argue pre-existing condition; §3202 liberal construction pushes back
**Standard ID:** `lab_4663_apportionment_permanent_disability`

---

## ANCHOR STATUTES — FETCH REQUIRED (HIGH PRIORITY)

### LAB CODE § 4610 — Utilization review (UR) process — FETCHED
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- First 30 days after injury: if MPN/HCO/predesignated physician — treatment authorized WITHOUT prospective UR (except: non-formulary pharmaceuticals, non-emergency surgery, psychological treatment, home health care, imaging [excluding x-rays], durable medical equipment >$250, electrodiagnostics)
- Employer must have UR process with written policies and procedures; process must be URAC-accredited
- Medical director must hold unrestricted CA license — they oversee UR decisions
- **PHYSICIAN-ONLY RULE:** Only licensed physician competent to evaluate the clinical issues may modify or deny treatment requests for medical necessity — non-physicians CANNOT deny treatment
- **No financial incentive:** Employer/insurer shall NOT offer or provide financial incentive to physician based on number of modifications or denials
- **Time limits (§4610(i)):** Prospective: 5 business days (max 14 days); concurrent: 72 hours for imminent threat; retrospective: 30 days
- Denial/modification must be communicated to physician within 24 hours by phone/fax, then in writing within 24 hours (concurrent) or 2 days (prospective)
- Disputes → §4610.5 IMR (Independent Medical Review) or §4062 QME process
**Standard ID:** `lab_4610_utilization_review`

### LAB CODE § 4616 — Medical Provider Networks (MPN)
- **What it does:** Employer/insurer may establish MPN limiting physician choice; MPN approval; employee rights within MPN; second opinion process
- **Fetch:** leginfo → LAB § 4616 [STILL PENDING]
- **Standard ID:** `lab_4616_medical_provider_network`

### LAB CODE § 4062 — Qualified Medical Evaluator (QME) process — FETCHED
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- If either party objects to treating physician medical determination (on issues not covered by §4060/4061 and not subject to §4610): must notify other party in writing within 20 days (represented) or 30 days (unrepresented)
- **Represented employee:** QME evaluation via §4062.2 (agreed QME or panel) — no other medical evaluation
- **Unrepresented employee:** Employer provides PQME request form; panel of 3 QMEs assigned by DWC Medical Unit
- **§4062(b):** UR denial disputes (§4610 modifications/denials) → resolved ONLY through IMR (§4610.5); NOT through QME
- **§4062(c):** MPN physician disputes → IMR under §§4616.3/4616.4
**Standard ID:** `lab_4062_qme_process`

### LAB CODE § 5400 — Written notice requirement — FETCHED
**Text:** FETCHED (full text — 2026-04-12)
**Key holding:** No claim for compensation shall be maintained unless within THIRTY DAYS after injury, written notice signed by injured person (or someone on their behalf) is served upon employer — EXCEPT as provided by §§5402 (employer knowledge) and 5403 (waiver)
**NOTE:** §5400 is the NOTICE requirement, not the claim form provision. The DWC-1 claim form process is separately governed. The critical protection is §5402 — if employer KNEW of injury, failure to file §5400 notice is excused.
**Standard ID:** `lab_5400_notice_requirement`

### LAB CODE § 132a — Anti-retaliation (cross-reference to Labor/Employment)
- **Cross-reference only** — built in CA_Labor_Employment_Litigator; cite from there

### 8 CCR § 9792.6 — MTUS (Medical Treatment Utilization Schedule) applicability
- **What it does:** DWC regulations implementing the MTUS; treatment guidelines; evidence-based standards
- **Fetch:** ecfr.gov → Title 8 CCR § 9792.6 (California-specific, not federal CFR)
- **NOTE:** This is CA CCR (Cal. Code of Regulations), not federal CFR

---

## CASE LAW SEEDS

1. **Subsequent Injuries Fund v. Workmens Comp. Appeals Bd.**, 2 Cal.3d 56 (1970) — Foundational: liberal construction of §3202 mandates resolving ambiguity in favor of injured worker; entire workers comp system is remedial legislation
2. **State Comp. Ins. Fund v. Workers' Comp. Appeals Bd. (Viterbi)**, 40 Cal.4th 1 (2006) — Apportionment reform under SB 899 (2004); §4663 causation-based apportionment replaces prior "compensation-based" system; insurer bears burden of apportionment evidence
3. **Ogilvie v. City and County of San Francisco**, 197 Cal.App.4th 1262 (2011) — WCAB must follow PDRS; rebuttal of AMA Guides; treating physician report weight
4. **Benson v. Workers' Comp. Appeals Bd.**, 170 Cal.App.4th 1535 (2009) — Multiple injuries; apportionment must account for subsequent injuries; §4663 causation analysis
5. **Brodie v. Workers' Comp. Appeals Bd.**, 40 Cal.4th 1313 (2007) — Companion to Viterbi; "other factors" in §4663 apportionment must be based on substantial medical evidence; bare percentages without explanation insufficient

---

## STANDARDS OF CREATION (document types this Citizen audits)

- **DWC-1 Claim Form** — Employer-provided; must be provided within 1 day; employee's completion triggers employer liability
- **Primary Treating Physician (PTP) Report** — Must include: diagnosis, mechanism of injury, treatment plan, apportionment determination (or stated reason why not possible)
- **Qualified Medical Evaluator (QME) Report** — Panel-selected; must meet WCAB format requirements; address all disputed medical issues
- **Utilization Review Determination Letter** — Must state basis; must be issued within time limits (prospective: 5 business days; concurrent: 1 day; retrospective: 30 days)
- **Independent Medical Review (IMR) Determination** — DWC-administered; final and binding on treatment disputes; no WCAB appeal of medical necessity after IMR
- **Compromise and Release (C&R)** — Full settlement of all claims; court approval not required but must be voluntary; WCAB approval required
- **Findings and Award** — WCAB adjudication outcome; findings of fact; award of benefits; permanent disability rating

---

## SOC CONTROLS

- **WCAB (Workers' Compensation Appeals Board)** — statewide adjudication; district offices; 20 judges; wcab.ca.gov
- **DWC (Division of Workers' Compensation)** — administrative agency; UR oversight; QME certification; MTUS
- **CWCI (California Workers' Compensation Institute)** — industry research; fraud pattern data
- **DI (Director of Industrial Relations)** — self-insurance certification; oversight of DWC
- **CIGA (California Insolvency Insurance Association)** — pays claims when insurer goes insolvent; relevant if employer's insurer is defunct

---

## FIVE-LAYER STANDARDS TO BUILD

| Standard ID | Statute/Rule | Priority |
|---|---|---|
| `lab_4600_medical_treatment_entitlement` | LAB §4600 — medical treatment | BUILD FIRST — treatment denial entry point |
| `lab_4663_apportionment_permanent_disability` | LAB §4663 — apportionment | BUILD SECOND — PD determination |
| `lab_4553_serious_willful_misconduct_enhancement` | LAB §4553 — 50% enhancement | BUILD THIRD — misconduct track |
| `lab_3202_liberal_construction` | LAB §3202 — liberal construction | BUILD FOURTH — interpretive anchor |
| `lab_4610_utilization_review` | LAB §4610 — UR process (fetch needed) | BUILD FIFTH |

---

## HISTORICAL CHAIN SEED

**The wound:** California workers compensation was established in 1913 as a grand bargain — workers give up tort rights for guaranteed no-fault compensation; employers get certainty in exchange for paying premiums. The wound arrived in 2004 with SB 899. Insurers had lobbied for years that malingering and "system gaming" were costing billions. SB 899 rewrote §4663 — apportionment shifted from "compensation-based" to "causation-based." The effect: a worker with a prior knee surgery from decades before, injured at work today, could have 40% of their permanent disability attributed to the old surgery — cutting their benefit by 40%. The insurers celebrated. The Legislature made this change without fully understanding that causation-based apportionment would be applied to conditions the worker had never sought compensation for — conditions that never constituted disability at all. The wound is paid for in percentages: every percentage point of apportionment is money the insurer keeps. And the person counting those percentages is a physician hired by the insurer.

---

## CROSS-REFERENCES

- `CA_Labor_Employment_Litigator` → LAB §132a retaliation; LAB §1102.5 whistleblower; FEHA disability accommodation after comp injury
- `CA_Medical_Malpractice_Litigator` → treating physician in comp case may have independent malpractice liability
- `CA_Disability_Rights_Litigator` → ADA/FEHA accommodation obligations after work injury — separate track from WCAB
- `US_Federal_Social_Security_Litigator` → workers comp offset against SSDI benefits (42 USC §424a — reverse offset)
- `HERALD` → Will witness DWC-1 claim forms, UR denial letters, QME reports, treating physician reports
