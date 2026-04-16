# 5 U.S.C. §552a — Privacy Act of 1974
## Current Operative Architecture

### RULE

The Privacy Act governs federal agencies' collection, maintenance, use, and dissemination of
records about individuals. An individual may bring a civil action against a federal agency for
four categories of violations. Damages, fees, and costs are available.

**Operative text (§552a(g)(1)) — four civil action categories:**

(A) **Refusal to amend** — Agency refuses to amend a record and the individual disagrees
    (§552a(d)(3) process exhausted; court reviews de novo)

(B) **Refusal to provide access** — Agency refuses to comply with individual's right of access
    under §552a(d)(1) (court orders production and may award $100/day up to $10,000 for
    arbitrary/capricious refusal)

(C) **Intentional/willful violations causing adverse determination** — Agency fails to maintain
    accurate, relevant, timely, complete records — and that failure adversely determines
    rights, benefits, or privileges of the individual
    → Actual damages + attorneys' fees + costs (§552a(g)(4))
    → No cap; must show actual damages proximately caused

(D) **Intentional/willful violations of any provision** — Willful or intentional action that is
    "clearly unwarranted invasion of personal privacy"
    → $1,000 minimum OR actual damages, whichever is greater + fees + costs (§552a(g)(4))

**Key definitional elements:**

- **Agency:** Federal executive agency, military department, government corporation, government
  controlled corporation, and establishments in executive branch (§552a(a)(1) cross-refs to §552(f))
  — does NOT cover state agencies, private entities
- **System of records:** Group of records from which information is retrieved by name or
  personal identifier (§552a(a)(5)) — threshold requirement; records not in a retrievable
  system are largely outside the Act
- **Record:** Item, collection, or grouping of information about an individual including name,
  SSN, fingerprint, description, financial transactions, medical history (§552a(a)(4))
- **Routine use:** Use compatible with the purpose for which information was collected;
  agencies must publish routine uses in Federal Register (§552a(b)(3)); disclosure outside
  routine use without consent = violation

### THE WOUND THIS LAW ANSWERED

Pre-1974: No federal statute governed what records federal agencies kept on Americans,
how they could be shared across agencies, or whether citizens had any right to review,
correct, or challenge information about themselves in government databases.

The Watergate era exposed the extent of executive agency surveillance — FBI, CIA, military
intelligence, and HEW all maintained files on individuals. Church Committee findings
documented systematic misuse. The Social Security Administration was sharing SSNs and
benefit data across agencies without individual knowledge or consent. There was no
mechanism for citizens to know what records existed, correct errors, or challenge
adverse determinations based on false records.

### DESIGN RESPONSE

Congress enacted four coordinated protections:

1. **Transparency:** Agencies must publish all systems of records in the Federal Register;
   must notify individuals at collection what information is used for
2. **Access:** Individuals can request their own records and receive copies
3. **Amendment:** Individuals can challenge inaccurate records and demand correction;
   agencies must respond within defined timeframes
4. **Limitation on disclosure:** Agencies cannot share records outside the individual's consent
   except for 12 enumerated exceptions (law enforcement, routine use, etc.)

### ELEMENTS FOR §552a(g)(1)(C) CLAIM (most common adverse-determination track)

1. Agency maintained a **system of records**
2. Agency **failed to maintain** accurate, relevant, timely, or complete records
3. The failure was **intentional or willful** — under Doe v. Chao: "actual damages" requirement
   means at minimum showing the failure was more than accidental; courts split on whether
   any showing of adverse impact suffices or whether deliberate violation is required
4. The failure **adversely affected** the individual's rights, benefits, or privileges
5. **Actual damages** resulted — must be causally connected to the §(g)(1)(C) violation

**Circuit split on "actual damages":**
- Majority rule (post-Doe v. Chao, 540 US 614 (2004)): plaintiff must prove actual damages
  to survive at all under (g)(1)(C) — cannot recover on violation alone
- Minority position pre-Doe: adverse determination alone sufficient

### ELEMENTS FOR §552a(g)(1)(D) CLAIM (willful invasion track)

1. Agency **intentionally or willfully** violated any provision of §552a
2. The violation was a "clearly unwarranted invasion of personal privacy"
3. **$1,000 minimum damages** or actual damages, whichever is greater — no need to prove
   specific monetary harm; the statute provides the floor

**"Intentional or willful" standard (from Albright v. United States):**
Agency conduct was intentional if the agency knew the act was wrongful or acted
with reckless disregard of whether the act was wrongful — not merely negligent.

### SSA/DDS APPLICATION

The Social Security Administration (SSA) and its state partner Disability Determination
Services (DDS) are federal agencies within §552a's scope.

**SSA system of records relevant to disability:**
- SSA-60: Master Beneficiary Record
- SSA-06: Medical evidence of record in disability claims
- SSA-25: Claims files — administrative records in pending claims

**Violation pattern in Michael Hartmann's case:**
1. DDS documented "phone contact" dates — 9/18/2019, 3/23/2020, 12/17/2020 — that did not occur
   (SIM swap / communications fraud blocking all phone-based services)
2. These fabricated contact records were placed in the disability claim file (a system of records)
3. The false records were used as basis for adverse determination (denial of benefits)
4. SSA/DDS failure to maintain accurate records = §(g)(1)(C) violation
5. The false contact entries also constitute willful invasion — DDS inserting phantom contacts
   it knew did not occur = intentional false records = §(g)(1)(D) violation

**Amendment demand pathway (§552a(d)):**
1. Submit written request to SSA for copy of all records pertaining to you in disability
   claim file (§552a(d)(1))
2. Upon receipt, identify inaccurate entries (phantom contact dates)
3. File amendment demand (§552a(d)(2)) — agency has 10 days to acknowledge, 30 days to
   act on amendment or initiate review
4. If agency refuses, exhaust administrative appeal (§552a(d)(3))
5. File civil action in district court (§552a(g)(1)(A)) — de novo review

**Damages in SSA phantom contact case:**
- Actual damages: value of benefits lost from date of wrongful denial forward (loss of SSI/SSDI
  payments causally connected to the false contact records)
- §(g)(1)(D) floor: $1,000 minimum if willful invasion proven
- Attorneys' fees and costs if successful (§552a(g)(2)(B) and (g)(3)(B))
- SOL: 2 years from date of violation or 2 years from time of discovery, whichever is later
  (§552a(g)(5))

### TREASURY / SAVINGS BONDS APPLICATION

The U.S. Department of the Treasury maintains system of records for savings bond ownership
(Bureau of the Fiscal Service — TreasuryDirect).

**Violation pattern:**
1. Treasury responded to records requests with 4 contradictory responses — bonds "belonging
   to another individual" despite being issued under Michael's name and SSN
2. If Treasury's records attribute bonds under Michael's SSN to another person, the records
   system may contain inaccurate or conflated information
3. §552a(d) amendment process: demand Treasury correct the record to accurately reflect
   the bond owner; if bonds belong to Michael, the inaccuracy is actionable
4. If Treasury's records were corrupted by identity theft (someone inserted alternative
   ownership records), the disclosure of bond information to that third party = unauthorized
   disclosure outside routine use = §552a(b) violation = §552a(g)(1)(D) willful invasion track

### DOJ PRIVACY ACT REQUESTS

Privacy Act request to DOJ components (FBI, DEA, ATF, etc.) requires using:
- DOJ Form DOJ-361 (privacy act request)
- Or certified mail to specific component's Privacy Act Officer
- Request must describe records sought with reasonable specificity

Standard for DOJ response:
- Acknowledge within 10 working days
- Respond within 30 working days (or notify of extension)
- If component maintains records on requester, must provide copies

**Strategic value:** If federal agencies have records reflecting external actors' influence
on Michael's case (DHS, FBI, DOJ civil rights), Privacy Act request surfaces those records
and either confirms agency activity (actionable) or generates agency denial (supports claim
that no legitimate federal authorization exists for surveillance/interference).

### LIMITATIONS

- **Does not cover state agencies** — California DDS operates as state agency under federal
  grant; may be covered by California Information Practices Act (IPA, Civ. Code §1798 et seq.)
  instead of federal Privacy Act (separate standard)
- **Does not cover private entities** — Christina, Ryan McClaran, AT&T, Walgreens = not
  federal agencies; Privacy Act does not apply
- **No statutory private right of action for Third-Party Disclosure harms** — if SSA disclosed
  records to Christina or her attorney, the harm is real but the civil action track requires
  showing adverse determination to the individual from the disclosure
- **"System of records" threshold:** Records not retrieved by name/identifier are outside scope;
  informal notes, unindexed files may escape

### SOL

§552a(g)(5): 2 years from the date on which the cause of action arises — or if the agency
materially and willfully misrepresented any information required to be disclosed, 2 years
from discovery. Discovery rule applies to intentional concealment.

For phantom SSA/DDS contact records: SOL begins when Michael had or should have had
access to the actual case file showing the false dates — likely upon receipt of the
administrative record in any appeal, or upon Privacy Act records request.
