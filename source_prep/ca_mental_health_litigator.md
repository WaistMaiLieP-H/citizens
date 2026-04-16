# SOURCE PREP: CA_Mental_Health_Litigator
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** ANCHORS_FETCHED (PC §§1368/1369/1370; WIC §§5150/5250; BPC §2290.5 — ALL CORE SECTIONS FETCHED)
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary cases:**
- Dr. Wiita competency evaluation — PC §1368/1369 proceeding; fraudulent CST eval; SC-to-CA telehealth; no MC-350 form used; wrong examiner credentials
- PC §1001.36 mental health diversion (#7 criminal case) — already in CA_Criminal_Law_Specialist; this Citizen owns the UNDERLYING MENTAL HEALTH LAW FRAMEWORK, not the diversion mechanics
- WIC §5150 holds as instrument of control in conservatorship/ward system
- Mental health records in discovery — authentication, privilege, disclosure

**Boundary rule:**
- CA_Criminal_Law_Specialist OWNS: criminal defense strategy, diversion outcome, PC §1001.36 five-step analysis
- THIS CITIZEN OWNS: the mental health law framework that underlies those proceedings — Dusky standard, evaluator qualifications, telehealth compliance, patient rights during evaluation, LPS conservatorship pathway
- Do not merge. Cross-reference.

---

## ANCHOR STATUTES — FETCHED AND READY

### CAL. PEN. CODE § 1368 — Mental competency — judicial doubt
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§1368(a):** When doubt arises in judge's mind, judge must state doubt in record and inquire of defense counsel
- **§1368(a):** If defendant not represented, court must appoint counsel
- **§1368(b):** If counsel informs court of belief of incompetence: court SHALL order competency determination under §§1368.1 and 1369
- **§1368(b):** If counsel says competent: court MAY nevertheless order determination
- **§1368(c):** Once inquiry commenced, ALL CRIMINAL PROCEEDINGS SUSPENDED until question determined
- **Application to Dr. Wiita case:** Was there actually a legitimate doubt? Was the §1368 referral proper or pretextual? Did defense counsel actually believe incompetence?
**Standard ID:** `pen_1368_mental_competency`

### CAL. WIC CODE § 5150 — 72-hour involuntary hold
**Text:** FETCHED (full text — 2026-04-12)
**Key for mental health law context:**
- **§5150(e):** Application must state PROBABLE CAUSE in writing; person making statement is civilly liable for intentionally false statement
- **§5150(g):** Person must be advised orally of reason for hold, in accessible language/modality
- **§5150(k):** Facility must notify county patients' rights advocate if person not released within 72 hours
- **Application:** Fraudulent 5150 applications in the ward system; false probable cause statements = civil liability
**Standard ID:** `wic_5150_involuntary_hold` — cross-ref from CA_Probate_Conservatorship; build independently in mental health context

---

## ANCHOR STATUTES — FETCH REQUIRED (HIGH PRIORITY)

### CAL. PEN. CODE § 1369 — Competency determination process — FETCHED
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- Court suspends criminal proceedings and appoints at least ONE licensed psychologist or psychiatrist
- If defense counsel says defendant NOT seeking incompetence finding → court appoints TWO evaluators (one per side) upon request
- If developmental disability suspected → also appoint Regional Center director/designee
- Evaluator's written report MUST include: (a) diagnosis; (b) whether defendant can understand proceedings OR assist counsel in rational manner (BOTH Dusky prongs); (c) whether competency likely attainable in foreseeable future; (d) if requested by defense, §1001.36 diversion eligibility
- **§1369(c):** Defendant presumed competent — burden on party claiming incompetence to prove by PREPONDERANCE
- Jury trial available unless counsel waives; verdict must be UNANIMOUS
- **§1369(d):** State DSH must adopt education/training guidelines for appointed evaluators; court shall appoint experts meeting those guidelines or with equivalent experience
**Standard ID:** `pen_1369_competency_hearing`

### CAL. PEN. CODE § 1370 — Incompetency commitment and restoration — FETCHED
**Text:** FETCHED (full text — 2026-04-12; output saved to tool-results file — see persisted output)
**Key holdings (from preview):**
- **§1370(a)(1)(A):** If found competent → criminal process resumes
- **§1370(a)(1)(B):** If found incompetent AND not charged with §1001.36-listed offense → trial suspended; court must determine: (i) whether restoring competency is in interests of justice (weighing harm to victim, mental health condition, criminal history, likelihood of incarceration, public safety); (ii) if yes → commitment to DSH or outpatient restoration; (iii) if no → §1001.36 diversion hearing
**Standard IDs:** `pen_1369_competency_hearing`, `pen_1370_incompetency_commitment`

### CAL. PEN. CODE § 1370.01 — Outpatient competency restoration
- **What it does:** Court may order outpatient treatment instead of institutional commitment if certain conditions met
- **Fetch:** leginfo → PEN § 1370.01 [STILL PENDING]

### CAL. BUS. & PROF. CODE § 2290.5 — Telehealth standards — FETCHED
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§2290.5(b):** Before delivering health care via telehealth, provider MUST inform patient about telehealth AND obtain verbal or written consent; consent must be documented
- **§2290.5(d):** Failure to comply = UNPROFESSIONAL CONDUCT
- **§2290.5(e):** Does NOT alter scope of practice or authorize services not otherwise authorized by law — interstate licensure requirement survives
- **§2290.5(f):** ALL confidentiality laws apply to telehealth interactions
- **§2290.5(g):** ALL professional responsibility, unprofessional conduct, and standards of practice laws apply to provider while providing telehealth
- **§2290.5(i):** Hospital may grant telehealth privileges based on distant-site hospital's credentials — but only for hospital-based telehealth; does NOT relieve individual practitioner of state licensure obligation
**Dr. Wiita application:** §2290.5(g) is the critical provision — the same CA forensic psychiatry evaluation standards that apply in-person apply via telehealth; SC license does not satisfy CA Medical Practice Act; §2290.5(e) expressly preserves that requirement
**Standard ID:** `bpc_2290_5_telehealth_standards`

### CAL. RULES OF COURT § 5.230 — Expert evaluator qualifications (CST)
- **What it does:** Evaluators appointed for competency must meet specific qualification requirements — licensed, trained in forensic evaluation
- **Fetch:** California Rules of Court, Rule 5.230 (not a leginfo statute — access courts.ca.gov/rules)

### CAL. EVID. CODE § 1010-1027 — Psychotherapist-patient privilege
- **What it does:** Communications to licensed psychotherapist are privileged; exceptions for court-ordered evaluations (§1016)
- **Fetch:** leginfo → EVID § 1010; § 1016
- **Standard ID:** `evid_1016_psychotherapist_privilege_exception`

### CAL. WIC CODE § 5250 — 14-day hold (certification for intensive treatment) — FETCHED
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- After §5150 72-hour hold (or court-ordered evaluation under §§5200/5225), if person has received evaluation AND professional staff finds person is STILL a danger to others, danger to self, OR gravely disabled → may certify for up to 14 days intensive treatment
- **§5250(a):** Professional staff must analyze and find continued danger/grave disability
- **§5250(b):** Facility must be county-designated for intensive treatment and agree to admit
- **§5250(c):** Person must have been advised of need for treatment but unwilling/unable to accept voluntary treatment
- **§5250(d)(1):** NOT "gravely disabled" if person can survive safely with help of willing/able family, friends, or others — BUT family/friends must specifically indicate willingness in writing
- Person retains right to certification review hearing (§5256 et seq.)

### CAL. WIC CODE § 5350 — LPS conservatorship (already in Probate prep)
- **Cross-reference only** from Conservatorship Citizen; build the mental health entry point here

---

## CASE LAW SEEDS

1. **Dusky v. United States**, 362 U.S. 402 (1960) — THE STANDARD: defendant must have "sufficient present ability to consult with lawyer with reasonable degree of rational understanding" AND "rational as well as factual understanding of proceedings against him" — both prongs required; the fundamental test Dr. Wiita was supposed to apply
2. **Drope v. Missouri**, 420 U.S. 162 (1975) — Due process requires state to conduct competency hearing whenever there is sufficient doubt; court cannot ignore behavioral evidence of incompetency; what constitutes "doubt"
3. **People v. Superior Court (Ghilotti)**, 27 Cal.4th 888 (2002) — Mentally disordered offenders; SVP proceedings; demonstrates scope of mental health law in criminal system
4. **In re Anthony H.**, 129 Cal.App.4th 495 (2005) — PC §1368 standards; court must conduct adequate competency hearing; inadequate evaluation is structural error
5. **Sell v. United States**, 539 U.S. 166 (2003) — Forced medication to restore competency; four-part test; constitutional limits on government's ability to medicate defendant to make them "competent" for trial

---

## STANDARDS OF CREATION (document types this Citizen audits)

- **Judicial Council Form MC-350** — Court-ordered psychological/psychiatric evaluation — **REQUIRED BY COURT RULES; Dr. Wiita DID NOT USE IT** (flagged in gap analysis as violation)
- **APA Specialty Guidelines for Forensic Psychology** (2013) — Professional standards for CST evaluations
- **AAPL Practice Guidelines for CST** (American Academy of Psychiatry and the Law) — Clinical methodology standards for forensic evaluators
- **Cal. Rules of Court Rule 5.230** — Evaluator qualification requirements
- **ABPN Board Certification** — Required for forensic psychiatry credential verification
- **Telehealth consent documentation** — BPC §2290.5 requires prior informed consent

---

## SOC CONTROLS

- **Medical Board of California license verification** — Dr. Wiita's SC license for CA telehealth; active license search
- **ABPN (American Board of Psychiatry and Neurology)** — Board certification verification
- **AAPL membership/training verification** — Optional but relevant to standard of care
- **Court record audit trail** — MC-350 non-use must be documented in court file; absence of form IS the finding

---

## FIVE-LAYER STANDARDS TO BUILD

| Standard ID | Statute/Rule | Priority |
|---|---|---|
| `pen_1368_mental_competency` | PC §1368 — judicial doubt trigger | BUILD FIRST — Dr. Wiita entry point |
| `pen_1369_competency_hearing` | PC §1369 — hearing process (fetch needed) | BUILD SECOND |
| `bpc_2290_5_telehealth_standards` | BPC §2290.5 — telehealth consent/compliance | BUILD THIRD (fetch needed) |
| `wic_5150_involuntary_hold` | WIC §5150 — 72-hour hold | BUILD FOURTH (cross-ref from Conservatorship) |
| `evid_1016_psychotherapist_privilege` | Evid. §1016 — privilege exception | BUILD FIFTH (fetch needed) |

---

## HISTORICAL CHAIN SEED

**The wound:** Before Dusky (1960), defendants were tried while incompetent — some were executed — because courts had no uniform standard. Dusky imposed the minimum: rational understanding of the proceeding and ability to assist counsel. California's PC §1368 implemented this and added the defense attorney trigger — counsel must tell the court when they observe incompetency. The wound arrived when §1368 was weaponized in the opposite direction: prosecutors or cooperative judges triggering §1368 proceedings to suspend criminal cases, remove defendants from proceedings, and route them through the mental health system on pretextual grounds. The MC-350 is the paper proof that the evaluation met the standard. Its absence means the evaluation existed only as a performance — not a clinical finding.

---

## DR. WIITA SPECIFIC FINDINGS (from gap analysis)

The following violations were identified and need formal standard-based analysis:
1. **SC license / CA telehealth**: Does South Carolina license authorize CA telehealth under BPC §2290.5? Medical board must authorize; state-specific licensure required
2. **MC-350 not used**: Judicial Council Form MC-350 is mandatory for court-ordered evaluations; its absence means the evaluation was not conducted within the court's prescribed framework
3. **APA Standard 9 (Assessment)**: Specialty guidelines require review of all available records; did Dr. Wiita review the criminal case file, prior medical records, prior competency evaluations?
4. **AAPL qualification**: Was Dr. Wiita qualified in forensic psychiatry, or was this a general psychiatrist performing a specialized function without specialty training?
5. **Cal. Rules of Court 5.230 qualification**: Court-appointed expert must meet rule requirements; was this appointment procedurally valid?

---

## CROSS-REFERENCES

- `CA_Criminal_Law_Specialist` → PC §1001.36 diversion (already built); PC §§1368/1369 proceedings cross-referenced from there
- `CA_Probate_Conservatorship_Litigator` → WIC §5150 shared; LPS conservatorship pathway (WIC §5350)
- `CA_Medical_Privacy_Officer` → Mental health records subject to CMIA; psychotherapist-patient privilege
- `US_Federal_Civil_Rights_Litigator` → §1983 if state-ordered evaluation violated constitutional rights (Drope v. Missouri due process)
- `HERALD` → Will witness Dr. Wiita evaluation documents, MC-350 absence, telehealth consent records
