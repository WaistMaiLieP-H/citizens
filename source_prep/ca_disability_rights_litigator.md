# SOURCE PREP: CA_Disability_Rights_Litigator
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** PARTIAL — CA statutes FETCHED (GOV §§12926/12940 via Labor/Employment Citizen; CIV §§51/54/54.3 FETCHED this session; EVID §752 FETCHED); federal ADA blocked by MCP tool
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary cases:**
- Michael bilateral ankle injuries — ADA Title I employment discrimination after industrial injury; failure to provide reasonable accommodation; interactive process failure; FEHA parallel track
- Identity replacement ("retired at 44" credit report) — possible ADA record-of-disability discrimination; employer falsely reporting disability status
- SIRVA occupational nexus — disability from COVID vaccine; ADA coverage of SIRVA-related impairment
- Dr. Wiita PC §1368 — competency evaluation as proxy for disability-based court system discrimination; Drope v. Missouri due process
- Secret conservatorship — Lanterman-Petris-Short and PROB §1800.3 minor conservatee; ADA Title II state court obligation to accommodate disabled court participants

**Boundary rule:**
- CA_Labor_Employment_Litigator OWNS: LAB §132a retaliation; LAB §1102.5 whistleblower; GOV §12940 FEHA employment; interactive process; reasonable accommodation analysis
- CA_Workers_Compensation_Litigator OWNS: WCAB proceedings; indemnity; medical treatment; apportionment
- THIS CITIZEN OWNS: ADA Title I (employment), Title II (public services/courts), Title III (public accommodations); §504 Rehabilitation Act; CA Unruh Civil Rights Act (CIV §51); CA Disabled Persons Act (CIV §54)
- Overlap zone: GOV §12940 FEHA disability is BOTH citizens' territory — Labor/Employment owns the employment case; this Citizen owns the disability rights doctrine layer

---

## ANCHOR STATUTES — FETCHED AND READY (via Labor/Employment Citizen)

### GOV CODE § 12926 — FEHA definitions (disability)
**Text:** FETCHED in ca_labor_employment_litigator.md (full text — 2026-04-12)
**Key holdings relevant here:**
- **§12926(j):** "Mental disability" — any mental/psychological disorder that limits a major life activity; includes having a RECORD of such disorder; includes being REGARDED as having such disorder
- **§12926(m):** "Physical disability" — any physiological disease/disorder/condition affecting body systems that limits a major life activity; without regard to mitigating measures (medications, prosthetics, assistive devices)
- **§12926(n):** If ADA definition would provide BROADER protection than FEHA definition, ADA coverage incorporated by reference into FEHA
- **§12926(p):** "Reasonable accommodation" — making facilities accessible; restructuring jobs; modified schedules; reassignment; equipment modification; adjusted exams/training; interpreters
**Standard ID:** Cross-reference from `gov_12940_feha_employment` — build disability-specific standards separately here

### GOV CODE § 12940 — FEHA prohibited employment practices (disability provisions)
**Text:** FETCHED in ca_labor_employment_litigator.md
**Key holdings relevant here:**
- **§12940(a):** Discrimination on basis of physical disability, mental disability, or medical condition
- **§12940(m):** Employer must provide REASONABLE ACCOMMODATION for known physical or mental disability unless undue hardship
- **§12940(n):** Employer must engage in INTERACTIVE PROCESS in good faith — mandatory, not optional
- **§12940(k):** Failure to prevent discrimination/harassment is itself a violation
**Standard ID:** Cross-reference — build `feha_disability_accommodation` standard here

---

## ANCHOR STATUTES — FETCH REQUIRED (ALL FEDERAL — MCP TOOL BLOCKED)

### 42 USC § 12101 — ADA findings and purpose
- **What it does:** Congressional findings: 43 million Americans with disabilities; discrimination is pervasive; three purposes: equality of opportunity, full participation, independent living, economic self-sufficiency
- **Fetch:** uscode.house.gov → Title 42 → § 12101
- **Standard ID:** `ada_12101_findings_purpose`

### 42 USC § 12112 — ADA Title I — employment discrimination
- **What it does:** No covered entity shall discriminate against qualified individual on basis of disability in: hiring, firing, advancement, compensation, training, conditions of employment
- Includes: limiting/classifying/segregating employees; using selection criteria that screen out disabled; failing to make reasonable accommodation; using qualification standards with discriminatory effect
- **Fetch:** uscode.house.gov → Title 42 → § 12112
- **Standard ID:** `ada_12112_title_i_employment`

### 42 USC § 12131-12132 — ADA Title II — public services
- **What it does:** No qualified individual with disability shall, by reason of disability, be excluded from participation in, denied benefits of, or subjected to discrimination by public entity
- **Application:** State courts (including LASC and Contra Costa Superior Court) must accommodate disabled court participants; UC conservatorship proceedings; criminal proceedings
- **Fetch:** uscode.house.gov → Title 42 → § 12131; § 12132
- **Standard ID:** `ada_12131_title_ii_public_services`

### 29 USC § 794 — Section 504 Rehabilitation Act
- **What it does:** No individual with disability shall, solely by reason of disability, be excluded from participation in or denied benefits of any program receiving federal financial assistance
- **Application:** Any state court, agency, hospital, school receiving federal funds = covered; broader than ADA in some applications
- **Fetch:** uscode.house.gov → Title 29 → § 794
- **Standard ID:** `rehab_act_504_no_exclusion`

### 29 USC § 705 — Rehabilitation Act definitions
- **What it does:** "Individual with a disability" definition for §504 purposes; "substantially limits" standard
- **Fetch:** uscode.house.gov → Title 29 → § 705
- **Standard ID:** Cross-reference to § 794

---

## CA STATUTES — FETCHED AND READY

### CIV CODE § 51 — Unruh Civil Rights Act
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§51(b):** All persons within CA are free and equal; regardless of disability (or any other listed characteristic) are entitled to FULL AND EQUAL accommodations, advantages, facilities, privileges, or services in ALL business establishments of every kind
- **§51(e)(1):** "Disability" = any mental or physical disability as defined in GOV §§12926/12926.1 — incorporates FEHA definition
- **§51(f):** A violation of the right of any individual under the federal ADA of 1990 SHALL ALSO constitute a violation of this section — ADA violation = per se Unruh violation; no separate showing required
- **§51(e)(7):** Includes perception that person has characteristic, and association with person who has characteristic — broad coverage
- **Damages:** CIV §52 (not §51 itself) provides $4,000 per offense minimum statutory damages plus actual damages plus attorney fees
**Application:** Every ADA-covered denial — employment accommodation failure, court access failure, business establishment denial — triggers parallel Unruh cause of action with $4,000 minimum damages per incident. Court proceedings are "business establishments" under CA case law.
**Standard ID:** `civ_51_unruh_civil_rights_act`

### CIV CODE § 54 — California Disabled Persons Act
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§54(a):** Individuals with disabilities have SAME RIGHT as general public to full and free use of: streets, highways, sidewalks, walkways, public buildings, medical facilities (hospitals, clinics, physician offices), public facilities, and other public places
- **§54(b)(1):** "Disability" = mental or physical disability as defined in GOV §12926
- **§54(c):** ADA violation = per se §54 violation (parallel to §51(f))
**Application:** Medical facilities — blocked access to hospitals, clinics, physician offices — triggers §54. Medical care denial after SIRVA, spine surgery complications, blocked disability claims all fall within §54's medical facility coverage.
**Standard ID:** `civ_54_disabled_persons_act`

### CIV CODE § 54.3 — Disabled Persons Act — damages
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§54.3(a):** Any person who denies or interferes with admittance to or enjoyment of public facilities (§§54/54.1) OR interferes with rights of individual with disability under §§54/54.1/54.2 is liable for:
  - Actual damages PLUS
  - Up to THREE TIMES actual damages (no cap specified beyond 3x)
  - Minimum $1,000 per offense (regardless of actual damages)
  - Attorney's fees
- **§54.3(a):** "Interfere" includes preventing a service dog from carrying out functions
- **§54.3(b):** May ALSO file verified complaint with CRD (§12948 GOV); remedies are NON-EXCLUSIVE
- **§54.3(c):** Cannot recover under both §54.3 AND §52 for the SAME act (one recovery max)
**Application:** Each denial of medical facility access is a separate offense ($1,000 minimum); cumulative across 16-year pattern = significant statutory damages independent of actual damages proof.
**Standard ID:** `civ_54_3_disabled_persons_damages`

### EVID CODE § 752 — Interpreter for witnesses
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§752(a):** When witness is incapable of understanding OR expressing in English → interpreter who can understand the witness AND whom witness can understand SHALL be sworn to interpret
- **§752(b):** Record must identify the interpreter; may be appointed and compensated under §730 framework
- **§752(b)(1):** Criminal actions and juvenile court: interpreter compensation is CHARGE AGAINST THE COURT
- **§752(b)(2):** Civil actions: compensation apportioned among parties in proportion court determines; may be taxed as costs
**Application:** Any proceeding where Butsaya or Thai-speaking party participated without qualified interpreter = §752 violation. Interpreter must be DISINTERESTED. Compensation mechanism identifies which party carries the cost — critical for pro se litigants who cannot afford court-charged civil interpreter fees.
**Standard ID:** `evid_752_interpreter_oath`

---

## CASE LAW SEEDS

1. **Jensen v. Wells Fargo Bank**, 85 Cal.App.4th 245 (2000) — FEHA interactive process; employer must engage in a genuine, interactive process; refusing to engage = independent violation; does not matter if accommodation ultimately impossible
2. **Scotch v. Art Institute of California**, 173 Cal.App.4th 986 (2009) — Interactive process must be timely; delay = failure; employer cannot stall then claim no reasonable accommodation exists
3. **Olmstead v. L.C.**, 527 U.S. 581 (1999) — ADA Title II requires states to provide community-based services to disabled individuals rather than unnecessary institutionalization; "unjustified segregation of disabled persons constitutes discrimination"
4. **Tennessee v. Lane**, 541 U.S. 509 (2004) — ADA Title II applies to court proceedings; state must make judicial services accessible to disabled persons; Congress properly abrogated state sovereign immunity for Title II court access
5. **Brewer v. Copeland**, 86 Wn.2d 58 (1975) — Foundational: disability discrimination is not a matter of charity but of right; "the Constitution and civil rights laws... do not permit exclusion based solely on disability"
6. **California Foundation for Independent Living Centers v. County of Sacramento**, 142 F.Supp.3d 1035 (E.D.Cal. 2015) — ADA Title II applies to emergency services; county programs serving disabled persons must be accessible

---

## STANDARDS OF CREATION (document types this Citizen audits)

- **ADA/FEHA accommodation request** — Must be in writing ideally; but oral request triggers obligation; employer must confirm receipt and begin interactive process
- **Interactive process documentation** — Employer's written record of accommodation dialogue; failure to document = evidence of failure to engage
- **Medical certification of disability** — Must address: nature of impairment, major life activities affected, essential job functions that are affected; must not demand more than necessary
- **Right-to-sue letter (DFEH/CRD)** — Required before filing FEHA civil suit; 1-year SOL from issuance; exhaustion prerequisite
- **ADA self-evaluation plan** — Public entities under Title II must conduct self-evaluation; failure to maintain = evidence of non-compliance
- **ADA transition plan** — Public entity with structural barriers must have plan; failure to have = evidence of bad faith

---

## SOC CONTROLS

- **CRD (Civil Rights Department, formerly DFEH)** — CA enforcement agency for FEHA; complaint intake; right-to-sue; crd.ca.gov
- **EEOC** — Federal ADA/Rehab Act enforcement for employment (Title I); cross-files with CRD by agreement
- **DOJ Civil Rights Division** — ADA Title II enforcement for state/local government; Pattern-or-practice suits
- **Access Board** — Federal accessibility standards; ADA Accessibility Guidelines (ADAAG)

---

## FIVE-LAYER STANDARDS TO BUILD

| Standard ID | Statute/Rule | Priority |
|---|---|---|
| `feha_disability_accommodation` | GOV §12940(m)/(n) — interactive process | BUILD FIRST — already have text |
| `civ_51_unruh_civil_rights_act` | CIV §51 — Unruh / ADA per se (fetch needed) | BUILD SECOND |
| `ada_12112_title_i_employment` | 42 USC §12112 — ADA employment (fetch needed) | BUILD THIRD |
| `ada_12131_title_ii_public_services` | 42 USC §12131 — ADA courts (fetch needed) | BUILD FOURTH |
| `rehab_act_504_no_exclusion` | 29 USC §794 — Section 504 (fetch needed) | BUILD FIFTH |

---

## HISTORICAL CHAIN SEED

**The wound:** In 1973, Section 504 of the Rehabilitation Act was enacted — a single sentence: no program receiving federal money could exclude people solely because of disability. For seven years, HEW (Health, Education, and Welfare) issued no regulations implementing it. Disability rights advocates organized a sit-in occupation of the San Francisco HEW offices in 1977 — 25 days, the longest occupation of a federal building in U.S. history. They stayed until the regulations were signed. That sit-in produced the first federal disability rights regulations. The ADA came seventeen years later (1990), and the wound moved inward: the ADA's "reasonable accommodation" and "interactive process" requirements exist on paper, but enforcement depends on the disabled person filing their own complaint, exhausting administrative remedies, and funding litigation. The person with the disability bears the burden of proving what the employer should have provided. The interactive process is mandatory for the employer — but the consequences for refusing to engage are the same as any other FEHA violation: a right to file, pay filing fees, find an attorney, and wait years for a decision.

---

## CROSS-REFERENCES

- `CA_Labor_Employment_Litigator` → GOV §12940 interactive process; FEHA employment discrimination
- `CA_Workers_Compensation_Litigator` → Work injury → disability; §4600 medical treatment; apportionment
- `CA_Probate_Conservatorship_Litigator` → ADA Title II court access in conservatorship proceedings; Olmstead obligation
- `CA_Mental_Health_Litigator` → ADA coverage of mental disability; competency proceedings as disability discrimination
- `HERALD` → Will witness accommodation requests, right-to-sue letters, denial of accommodation documentation
