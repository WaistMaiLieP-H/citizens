# SSA Phantom Contact Fraud Workflow — US_Federal_Financial_Fraud_Litigator
# Case: SSA/DDS Disability Denial — Phantom Contacts 2019-2020-2021
# Case folder: ${nonfamilylaw}/2022-2024_(SSA&DoDDsFraud.Docs)

**Citizen:** US_Federal_Financial_Fraud_Litigator
**Case folder:** ${nonfamilylaw}/2022-2024_(SSA&DoDDsFraud.Docs)
**Workflow version:** 1.0 — built 2026-04-11

**Core theory:** The SSA/DDS administrative record contains three "contacts" (9/18/2019,
3/23/2020, 12/17/2020) that do not correspond to genuine communications with the claimant.
The SIM swap / call interception pattern (Ryan McClaran, coordinated with Christina Cerretani)
created a communications layer in which SSA was communicating with an interceptor, not the
claimant. The claimant's disability determination was therefore based on a fraudulent
administrative record — every "contact" was a phantom. The denial is not just wrong; it is
the product of documented fraud.

---

## Phase 0 — Acquire the Administrative Record

**Step 0.1 — Request SSA complete administrative record**
File a written request with the local SSA field office and the Appeals Council for the
complete administrative record in all disability proceedings, specifically:
- All EDCS (Electronic Disability Collect System) entries
- All contact log entries for dates 2019-2021
- All DDS (Disability Determination Services, California EDD) case management notes
- All notices mailed and their addresses (confirm addresses used — were they correct?)
- All ALJ hearing notices and dates
- Appeals Council determination and date

**Step 0.2 — Identify the "phantom contact" dates in the record**
Target dates: 9/18/2019, 3/23/2020, 12/17/2020.
For each date:
- What does the SSA/DDS record say happened? (phone contact, written contact, claimant
  non-response?)
- What actual activity occurred on those dates according to AT&T records?
- AT&T SIM swap records will show whether the claimant's number had an active SIM
  redirect on those dates — if so, any call to that number reached the interceptor.

---

## Phase 1 — Communications Forensics

**Step 1.1 — AT&T Subpoena (or voluntary production request)**
Request or subpoena AT&T records for:
- Account history for Michael Hartmann's phone number 2018-2022
- SIM card change history (SIM swaps and their dates)
- Call log for the three phantom contact dates (who called? What number received the call?)
- Any authorized account changes and the IP addresses / contact methods used

If the SIM was swapped on or before 9/18/2019, every "contact" in the SSA record was
received by the interceptor's device, not the claimant's.

**Step 1.2 — Walgreens / pharmacist SIM swap evidence**
Per project memory, Ryan McClaran is the identified IT operator. The SIM swap evidence
runs through the phone records. Coordinate with Ryan McClaran investigation in
${nonfamilylaw}/Ryan_McClaran folder.

**Step 1.3 — Document the claim: what the SSA record says vs. what AT&T records show**
The claim is not "SSA made a mistake." The claim is:
- SSA/DDS recorded contact with a person who claimed to be the claimant
- That person was not the claimant; it was an interceptor controlling the claimant's number
- The interceptor fed SSA false information or simply failed to respond, causing the
  administrative record to show non-cooperation by the claimant
- The claimant never received proper notice because his communications were intercepted

---

## Phase 2 — Legal Claim Structure

### Claim A: §405(g) Federal Court Review — Equitable Tolling (Bowen)

**Standard:** 42 U.S.C. §405(g) + Bowen v. City of New York, 476 U.S. 467 (1986)

**Argument:**
The 60-day §405(g) filing deadline is equitably tolled because:
1. The SSA administrative record contains fraudulent "phantom contact" entries
2. Those entries were created through an intercepted communications channel
3. The claimant did not receive genuine notice of the adverse determination because
   notices were sent to an address controlled by or accessible to the interceptors,
   or responses to notices were provided by the interceptors, not the claimant
4. The claimant could not have known the basis for the denial until discovery of the
   phantom contact pattern — which did not occur until document review in 2022-2024

**Tolling clock start:** Date the claimant discovered (or with reasonable diligence
could have discovered) the phantom contact fraud — document this precisely.

**Next step:** File in NDCA under §405(g) + §1331 federal question jurisdiction.

### Claim B: Colorable Constitutional Claim — Due Process (Califano + Mathews)

**Standard:** Califano v. Sanders, 430 U.S. 99 (1977) + Mathews v. Eldridge, 424 U.S. 319 (1976)

**Argument:**
Where SSA's process was fraudulent at its core — phantom contacts substituted for
genuine administrative procedures — the claimant was denied due process:
1. **Private interest** (Mathews factor 1): Disability benefits are a critical protected
   property interest, particularly for a person with documented spine/shoulder injuries
   and no other income source
2. **Risk of erroneous deprivation** (Mathews factor 2): A process conducted through
   intercepted communications has a 100% risk of erroneous deprivation — the claimant
   never had a genuine opportunity to present his case
3. **Government interest** (Mathews factor 3): SSA has no legitimate interest in
   maintaining fraudulent contact records or in denying the claimant a new hearing

Under Califano, this due process claim gives the district court jurisdiction under
28 U.S.C. §1331 even without exhausting §405(g) administrative requirements.

### Claim C: Privacy Act §552a — False Records (5 U.S.C. §552a)

**Standard:** USC_5_552A_PRIVACY_ACT

**Argument:**
The SSA phantom contact entries are false records in a federal agency system of records.
The Privacy Act, 5 U.S.C. §552a(e)(5), requires agencies to maintain records "with such
accuracy, relevance, timeliness, and completeness as is reasonably necessary to assure
fairness to the individual in the determination."

§552a(g)(1)(C) civil remedy: agency that makes adverse determination based on records
it knew to be inaccurate is liable for actual damages + costs + attorney fees.

The phantom contact entries are the foundation of the adverse determination.
SSA's reliance on interceptor-sourced "contact" records = adverse determination based
on inaccurate records.

### Claim D: Civil RICO — 18 U.S.C. §1962(c)

**Standard:** USC_18_1961_RICO

**RICO requires:**
1. Person (Ryan McClaran, Christina Cerretani, potentially others)
2. Enterprise (the coordinated network — SIM swap + SSA interception + DDS manipulation)
3. Pattern of racketeering activity (2+ predicate acts; open-ended continuity):
   - Wire fraud (18 U.S.C. §1343): using phone/internet to intercept SSA communications
   - Identity theft (18 U.S.C. §1028): assuming the claimant's identity in SSA contacts
   - Obstruction of federal proceedings (18 U.S.C. §1505): interfering with the SSA
     administrative process
4. Causation: the RICO enterprise caused the claimant's disability benefits to be denied
5. Injury: quantifiable as back SSDI benefits + Medicare premium reimbursement + consequential
   medical expenses denied due to lack of Medicare coverage

**RICO remedy:** Treble damages + mandatory attorneys' fees (18 U.S.C. §1964(c))

### Claim E: Wiretap Act — 18 U.S.C. §2511

**Standard:** USC_18_2511_WIRETAP

The interception of SSA phone communications on the phantom contact dates = civil wiretap
violation. Each intercepted call = separate violation = $10,000 or actual damages,
whichever is greater, per interception.

---

## Phase 3 — Benefits Recovery Calculation

| Category | Calculation basis |
|----------|------------------|
| Back SSDI benefits | Monthly SSDI rate × months from onset date (est. 2019) to current |
| Medicare Part A + B premiums | Monthly premiums × months without coverage |
| Medical expenses — SIRVA | Post-2021 shoulder surgery and treatment, denied coverage |
| Medical expenses — spine | Post-2019 denial, treatment paid out-of-pocket or denied |
| Lost economic damages | Documented inability to work due to disability (SSA's own definition) |
| RICO treble damages | 3× all of the above (if civil RICO proceeds) |

---

## Phase 4 — Coordination Map

| Claim | Citizen |
|-------|---------|
| SIRVA underlying injury | CA_Medical_Malpractice_Litigator (sirva_claim_workflow) |
| §1983 constitutional due process violation (if state actors) | US_Federal_Civil_Rights_Litigator (§1983 corpus) |
| SIM swap telecom violations | CA_Telecom_Privacy_Litigator (Terminal B) |
| Ryan McClaran digital fraud | US_Federal_Financial_Fraud_Litigator (§1030 CFAA, §1028) |
| FCRA if disability denial caused credit entries | US_Federal_Financial_Fraud_Litigator (usc_15_1681_fcra) |
| Family law / conservatorship connection | CA_Family_Law_Litigator (other terminal — coordinate, no write) |

---

## Phase 5 — Sequencing and Timing

**Recommended sequence:**

1. **(Immediate)** File FOIA / Privacy Act request with SSA for complete administrative
   record + contact logs. This preserves the record and starts the clock on agency response.

2. **(Immediate)** File AT&T records preservation request or seek emergency subpoena if
   any litigation is pending.

3. **(Within 60 days of this session)** Consult with SSA disability appeals attorney
   regarding whether a new disability application or motion to reopen prior proceeding
   is available, independent of the fraud claims.

4. **(After records received)** Map phantom contact dates to AT&T records. Build the
   forensic table showing: SSA record says X / AT&T records show Y / conclusion: phantom.

5. **(After forensic table built)** File §405(g) action in NDCA (Oakland), or file as
   part of the existing § 1983 complaint as additional counts. Coordinate with
   US_Federal_Civil_Rights_Litigator steward on complaint structure.

---

## Standards Governing This Workflow

| Standard | Application |
|----------|------------|
| USC_42_405G_SSA_REVIEW | §405(g) review; Bowen equitable tolling; Califano due process exception |
| USC_5_552A_PRIVACY_ACT | False agency records; adverse determination based on inaccurate records |
| USC_18_1961_RICO | RICO enterprise; wire fraud + identity theft predicates; treble damages |
| USC_18_2511_WIRETAP | Each intercepted SSA call = separate $10K civil remedy |
| USC_18_1028 | Identity theft: using claimant's identity in SSA contacts |
| USC_18_1343_WIRE_FRAUD | Wire fraud: using phone to intercept SSA communications |

---

*Workflow status: ACTIVE. FOIA/Privacy Act request to SSA is the highest-priority immediate step. Built 2026-04-11.*
