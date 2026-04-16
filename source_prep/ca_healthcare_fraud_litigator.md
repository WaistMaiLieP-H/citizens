# SOURCE PREP: CA_Healthcare_Fraud_Litigator
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** ANCHORS_FETCHED (CA statutes); 18 USC §1347 fetch blocked — use uscode.house.gov
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary cases:**
- #11 — Spine Surgery Fraud (2020-2021): Muir Ortho / Blue Shield — prior auth denial, lumbar MRI duplicates with handwritten annotations, spine surgery billed without authorization
- #12-14 — Related medical billing/prior auth fraud pattern
- #20 — SIRVA surgery (Dr. Wiseman, 4/20/2022): COVID vaccine shoulder injury → surgery — PREP Act preemption question (already flagged in CA_Medical_Malpractice_Litigator outstanding investigation)

**Gap analysis finding (folder 3, Spine_Surgery_Fraud):**
MISSING personas: Spine Surgeon, Radiologist, UR Nurse, Insurance Fraud Investigator (SIU), CDI Specialist, Health Plan Compliance Officer

---

## ANCHOR STATUTES — FETCHED AND READY

### CAL. INS. CODE § 10123.135 — Prior authorization requirements
**Text:** FETCHED (full statute — 2026-04-12)
**Key holdings for standards:**
- **Subdivision (a):** Scope — any disability insurer using UR/UM functions
- **Subdivision (b):** Written policies required; criteria must be developed with practicing providers, updated annually, disclosed on request
- **Subdivision (c):** Medical director requirement if CA insureds ≥ 50% of nationwide enrollment
- **Subdivision (e):** NON-PHYSICIAN MAY NOT deny for medical necessity — only licensed physician/health care professional competent in the specific clinical issue
- **Subdivision (h)(1):** 5 business days standard; (h)(2): 72 hours for urgent/serious threat cases; (h)(3): 24 hours to communicate decision to provider
- **Subdivision (j):** AI/algorithm PROHIBITED from denying — must not base determination solely on group dataset; must not supplant health care provider decision-making (added by recent amendment)
- **Subdivision (k):** Does not make disability insurer a "health care provider" — no MICRA cap exposure
**Standard ID:** `ins_10123_135_prior_auth`

### CAL. PEN. CODE § 550 — Insurance fraud
**Text:** FETCHED (full statute — 2026-04-12)
**Key holdings:**
- **§550(a)(6):** Knowingly make false claim for health care benefit = felony if >$950
- **§550(a)(7):** Submit claim for health care benefit not used = felony
- **§550(a)(8):** Multiple claims for same benefit with intent to defraud
- **§550(b)(1):** Written statement containing false/misleading information to support claim
- **§550(b)(3):** Concealing occurrence affecting right to insurance benefit
- **Penalty:** 2, 3, or 5 years; fine up to $50K or double the fraud (whichever greater); mandatory restitution
**Standard ID:** `pen_550_insurance_fraud`

### CAL. INS. CODE § 790 — Unfair trade practices (purpose)
**Text:** FETCHED — citations McCarran-Ferguson Act
**Use:** Gateway section establishing CDI regulatory authority; cite for standing to bring CDI complaint
**Standard ID:** Cross-reference to `ca_insurance_compliance_litigator` — do not build separately

### CAL. INS. CODE § 790.03 — Specific prohibited acts
**Text:** FETCHED (full statute — 2026-04-12)
**Key for healthcare fraud:**
- **§790.03(h)(1):** Misrepresenting pertinent facts or policy provisions
- **§790.03(h)(3):** Failing to implement reasonable standards for prompt investigation
- **§790.03(h)(5):** Not attempting in good faith to effectuate prompt, fair, equitable settlements where liability is reasonably clear
- **§790.03(h)(13):** Failing to provide reasonable explanation for denial
**Standard ID:** `ins_790_03_unfair_claims` — cross-ref from CA_Insurance_Compliance_Litigator

### CAL. HEALTH & SAFETY CODE § 1340 — Knox-Keene Act citation
**Text:** FETCHED — title citation only
**Next fetch needed:** HSC §§ 1367 (timely access), 1367.01 (timely access to care), 1374.30 (independent medical review), 1374.32 (IMR process)
**Standard ID:** `hsc_1340_knox_keene_act`

---

## ANCHOR STATUTES — FETCH REQUIRED

### 18 USC § 1347 — Federal health care fraud
- **What it does:** Knowingly and willfully execute/attempt to execute scheme to defraud any health care benefit program — up to 10 years; if bodily injury, up to 20 years; if death, up to life
- **Fetch:** uscode.house.gov → Title 18 → Part I → Chapter 63 → § 1347
- **Why critical:** Blue Shield is a federal health care benefit program participant (Medicare Advantage contracts). §1347 reaches health insurers, not just providers.
- **Standard ID:** `usc_18_1347_federal_healthcare_fraud`

### CAL. HEALTH & SAFETY CODE § 1367 — Health plan duties; timely access
- **What it does:** Health care service plan must provide covered benefits in a timely manner
- **Fetch:** leginfo → HSC § 1367

### CAL. HEALTH & SAFETY CODE § 1374.30 — Independent Medical Review
- **What it does:** When insurer denies as not medically necessary, patient may request IMR through DMHC; IMR decision is binding on plan
- **Fetch:** leginfo → HSC § 1374.30
- **Standard ID:** `hsc_1374_30_independent_medical_review`

### CAL. BUS. & PROF. CODE § 2234 — Unprofessional conduct (already in CA_Medical_Malpractice_Litigator)
- **Cross-reference only** — physician ordering fraudulent prior auth; do not duplicate build

---

## CASE LAW SEEDS

1. **Sarchett v. Blue Shield of California**, 43 Cal.3d 1 (1987) — Insurer's duty of good faith; arbitrary denial without adequate investigation is bad faith; sets pre-§10123.135 standard
2. **Wilson v. Blue Cross of So. California**, 222 Cal.App.3d 660 (1990) — Third-party liability for bad faith denial; insurance company caused harm by denying medically necessary care; wrongful death
3. **Hailey v. California Physicians' Service**, 158 Cal.App.4th 452 (2007) — Knox-Keene plan cannot deny mental health benefits at lower reimbursement rate than physical — parity
4. **United States v. Krizek**, 111 F.3d 934 (D.C. Cir. 1997) — §1347 "reckless disregard" standard: billing without knowing what was actually done = federal health care fraud; physician is responsible for own billings
5. **United States v. Lucien**, 347 F.3d 45 (2d Cir. 2003) — §1347 requires proof that defendant knew scheme would deceive — intent element; distinguish negligent billing from fraud
6. **Arnett v. California Hospital Medical Center**, (LASC case TBD) — Prior auth denial + surgical harm; establishes causation chain for malpractice + insurance fraud concurrent claims

---

## STANDARDS OF CREATION (document types this Citizen audits)

- **Prior authorization letters** — must comply with §10123.135(h)(4) written criteria disclosure
- **UR/UM denial letters** — must name licensed physician responsible; must include criteria used; must include appeal rights
- **Operative reports / surgical records** — AAPC Official Coding Guidelines (spine CPT codes)
- **NASS Evidence-Based Clinical Guidelines** — spine surgery necessity standard
- **ACR Appropriateness Criteria** — lumbar spine imaging; do 4 duplicate MRI pages represent separate studies billed separately?
- **SIU (Special Investigations Unit) protocols** — CMS Program Integrity Manual Chapter 4; insurer must have SIU and must report suspected fraud to CDI

---

## SOC CONTROLS

- **CMS Program Integrity Manual, Chapter 4** — Benefit Integrity; fraud detection standards
- **NIST SP 800-66** — HIPAA Security Rule (medical records integrity)
- **SOC 2 Type II** — Health insurer systems (Blue Shield audit trail requirements)
- **CDI (CA Department of Insurance)** — enforcement of §790.03; complaint mechanism
- **DMHC (Dept. of Managed Health Care)** — Knox-Keene enforcement; IMR oversight

---

## FIVE-LAYER STANDARDS TO BUILD (initial scaffold)

| Standard ID | Statute/Rule | Priority |
|---|---|---|
| `ins_10123_135_prior_auth` | Ins. Code §10123.135 — UR/prior auth | BUILD FIRST — central spine fraud claim |
| `pen_550_insurance_fraud` | Pen. Code §550 — CA insurance fraud | BUILD SECOND |
| `usc_18_1347_federal_healthcare_fraud` | 18 USC §1347 — federal scheme | BUILD THIRD |
| `hsc_1374_30_independent_medical_review` | HSC §1374.30 — IMR | BUILD FOURTH |
| `hsc_1340_knox_keene_act` | HSC §1340 (+ §1367 framework) | BUILD FIFTH |

---

## HISTORICAL CHAIN SEED

**The wound:** The Knox-Keene Act passed in 1975, the same year HMOs were federally incentivized under the HMO Act of 1973 (Pub. L. 93-222). The promise: managed care would deliver better care at lower cost with proper oversight. The wound arrived within a decade: UR departments staffed by non-physicians using proprietary criteria to deny care. The AMA sued Blue Shield. Families buried people who were denied hospitalizations. §10123.135 was California's 1999 answer — you must use a licensed physician in the specific specialty to deny. It took another 25 years to add the AI provision. The MRI with 4 duplicate pages and handwritten annotations is what happens when an insurer's UR system never had a spine surgeon look at the film.

---

## CROSS-REFERENCES

- `CA_Medical_Malpractice_Litigator` → BPC §2234, CCP §340.5 (already built); SIRVA shared; do not duplicate
- `CA_Insurance_Compliance_Litigator` → Ins. §790.03 unfair claims (cross-ref, not duplicate)
- `US_Federal_Financial_Fraud_Litigator` → 18 USC §1347 may also be built there; coordinate
- `CA_Medical_Privacy_Officer` → HIPAA/CMIA on duplicate MRI records
- `HERALD` → Will witness duplicate MRI pages, handwritten annotations, prior auth denial letters
