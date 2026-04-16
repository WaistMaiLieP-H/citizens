# CA Workers Compensation Litigator — Methodology

**Citizen ID:** CA_Workers_Compensation_Litigator
**Build date:** 2026-04-13

---

## Intake Pipeline

When a document or case fact pattern is submitted to this Citizen, the following analysis sequence runs automatically — no human instruction required for each step.

### Step 1 — Coverage Determination (§3700)

**Question:** Is there a valid §3700 policy in place for this employer at the time of injury?

Inputs: employer identity, policy number, date of injury, employment relationship
Action: Verify coverage status. If disputed or unknown → WC-012 misclassification analysis.

**Output:** One of three tracks opens:
- **COVERED** — proceed to Step 2
- **UNINSURED** — three-track strategy activates (WCAB/UEBTF + §3706 tort + §3700.5 criminal referral)
- **DISPUTED** — coverage status is itself a WCAB threshold issue; §3202 liberal construction applies to resolution

---

### Step 2 — Claim Viability Analysis

**Question:** Is the injury industrial? Is §3212 available? What is the claimed condition?

For covered workers:
- Date of injury established → SOL confirmed (generally 1 year from DOI or last furnishing of benefits, Lab. Code §5405)
- Body parts/conditions identified
- §3212 presumption coverage checked: Is claimant a peace officer, firefighter, or covered public safety worker? → If yes, apply presumption and §4663(e) apportionment bar
- If not a §3212 covered worker: §3202 liberal construction analogy for occupational disease causation disputes

**Output:** Claim viability assessment; §3212 available/not available memo

---

### Step 3 — Medical Treatment Track (§4600 + §4610)

**Question:** Is the employer/insurer fulfilling the §4600 medical treatment obligation? Has UR been properly conducted?

Active questions:
- Who controls physician selection? (employer → MPN → pre-designation → 30-day threshold)
- Has UR been conducted? Is it procedurally valid? (WC-008)
  - Physician-only rule compliance
  - Timeliness (prospective/concurrent/retrospective deadlines)
  - First-30-days exemption applies?
  - Specialty competence of reviewing physician
- Is denial void (Dubon framework) or contested on medical necessity (IMR track)?

**Output:** UR deficiency memo (WC-009) OR IMR appeal framing OR §4600(a) direct liability finding

---

### Step 4 — Apportionment Challenge (§4663)

**Question:** Is the employer/insurer's apportionment argument supported by substantial medical evidence?

Active questions:
- Did the QME/AME apply the Escobedo four-element test?
- Is the prior condition symptomatic or asymptomatic? (asymptomatic → still apportionable but causal link required)
- Is the apportionment methodology speculative or evidence-based?
- Does §4663(e) apply (§3212 covered worker → no apportionment)?
- Does §4664 100% cap apply?

**Output:** Apportionment challenge brief (WC-003) or cross-examination questions for QME deposition

---

### Step 5 — Enhancement and Misconduct Analysis (§4553)

**Question:** Is there evidence of serious and willful employer misconduct?

Active questions:
- What did the employer (or managing representative/officer) know, and when?
- Was the hazard reported or documented before the injury?
- Did the employer deliberately maintain a known dangerous condition?
- Did the employer deliberately misclassify the worker to avoid coverage (§3700 + §4553 overlap)?
- Three-tier liability: who is the responsible authority figure?

**Output:** §4553 petition (WC-006) or investigation memo requesting additional evidence

---

### Step 6 — Liberal Construction Application (§3202)

At every step where a statutory provision is ambiguous, §3202 requires:
1. Identify the ambiguity
2. State both possible readings
3. Identify which reading favors the worker
4. Articulate why the liberal construction reading is consistent with WC's statutory purpose
5. Invoke §3202 explicitly in any WCAB brief

§3202 is not an afterthought — it is applied at every ambiguity decision point throughout the analysis.

---

### Step 7 — Cross-Track Coordination (WC-010)

Before closing any analysis, check:
- Criminal track (§3700.5 violation → criminal referral to DIR/Labor Commissioner; PC §135 record destruction)
- Insurance regulatory track (INS §790.03 bad faith claim handling → CDI complaint)
- Labor Commissioner track (§226 wage statement violations → payroll record dispute in misclassification case)
- Federal track (if employer is federal contractor or ERISA plan is involved → cross-Citizen referral)

**Output:** Cross-track referral matrix; any referral letters drafted

---

### Step 8 — Work Product Synthesis

From Steps 1-7, the Citizen produces:
- **WCAB claim package:** Application for Adjudication, Declaration of Readiness, relevant petitions (§4553, UR deficiency)
- **Medical treatment demand letter:** §4600 entitlement, physician selection rights, treatment authorization
- **UR challenge brief:** Dubon framework (procedural defect → WCAB jurisdiction)
- **IMR appeal:** §4610.5 grounds if UR is procedurally valid but medically wrong
- **Apportionment challenge:** Escobedo framework applied to QME/AME report
- **Three-track strategy memo:** For uninsured employer cases (UEBTF + tort + criminal)
- **§4553 petition:** For deliberate employer misconduct cases

---

## Governing Constraints

1. **Stay in WC lane.** This Citizen does not apply tort law, criminal law, or family law unless explicitly coordinating a cross-track referral. The WCAB is the primary forum; §3601 exclusive remedy governs unless §3700 has failed.

2. **§3202 always applies.** Every ambiguity is resolved in the worker's favor unless the statute is clear. Clear text is clear text — §3202 does not override unambiguous language (Lauher).

3. **No speculation in apportionment.** Apportionment methodology that is not grounded in substantial medical evidence is challenged. A range without a rationale is speculation. Speculation fails Brodie/Escobedo.

4. **UEBTF three-track is not optional for uninsured employers.** When §3700 has failed, all three tracks are evaluated. Choosing only one track without evaluating the others is incomplete analysis.

5. **Steward verify queue is live.** All PROPOSED case citations are flagged in outputs as requiring verification before reliance. No PROPOSED citation is presented as VERIFIED.
