# Response Processing

**Citizen:** CA_Family_Law_Litigator
**Created:** 2026-04-15
**Purpose:** Handling the four response types from agencies, courts, carriers, and providers. Each type has a defined next action, escalation path, and documentation requirement.

---

## Response Type 1: POSITIVE (Records Received)

The agency or provider produced the requested records in full.

**Next Action:**
1. Log receipt in the investigation JSON (`status` → `RESPONSE_RECEIVED`, add `response_received_at_utc`, `response_summary`).
2. File the records in the appropriate `outstanding_investigations/<id>/responses/` directory.
3. Execute `evidence_intake_trigger.md` to identify affected standards and queue re-audits.
4. Update the `case_workflows/*/evidence_index/` for every case the investigation touches.
5. If the response closes the investigation, set `status` → `RESOLVED` and write `resolution_summary`.

**Escalation Path:** None required for a full positive response.

**Documentation Requirements:**
- Date received
- Method of receipt (mail, email, portal, in-person pickup)
- Custodian who produced (name and title if available)
- Page count / file count
- Any cover letter or transmittal note (scan and file with response)
- Chain of custody note: "Received by [steward name] on [date] via [method]; filed at [path]"

---

## Response Type 2: NEGATIVE (Denial / No Records Found)

The agency states no responsive records exist, or denies the request on stated grounds.

**Next Action:**
1. Log the denial in the investigation JSON (`status` → `DENIED` or `NO_RECORDS_FOUND`).
2. File the denial letter/communication in `outstanding_investigations/<id>/responses/`.
3. Evaluate the denial basis:
   - **"No responsive records"** — Document as an affirmative finding. In many investigations (INV-02 Ajaniku, INV-03 Paredes), a negative response IS the evidence. Proceed to re-audit with the negative finding as the anchor.
   - **"Exempt under [statute]"** — Identify the exemption cited. Evaluate whether the exemption applies. If it does not, escalate per `escalation_pipeline.md`.
   - **"Request too broad / not reasonably described"** — Narrow and re-submit within 10 calendar days.
   - **"Records destroyed per retention schedule"** — Document the destruction. Request the retention schedule itself. If destruction was improper (e.g., litigation hold should have applied), escalate.
4. For CPRA denials: the 10-day clock for writ of mandate (CCP § 1085) starts from the denial date.

**Escalation Path:**
- CPRA denial → `escalation_pipeline.md` § 1 (writ of mandate)
- Subpoena objection → `escalation_pipeline.md` § 2 (motion to compel)
- Court clerk refusal → `escalation_pipeline.md` § 3 (ex parte application)

**Documentation Requirements:**
- Exact text of the denial (verbatim quote or scanned letter)
- Stated legal basis for denial (statute, rule, policy cited)
- Date of denial
- Name and title of person who denied (if provided)
- Whether the denial was timely under CPRA (10 calendar days from request)
- Analysis note: "The denial [is/is not] legally sufficient because [reason]"

---

## Response Type 3: PARTIAL (Redacted or Incomplete Production)

The agency produced some records but withheld others, or produced records with redactions.

**Next Action:**
1. Log in investigation JSON (`status` → `PARTIAL_RESPONSE`).
2. File what was received in `outstanding_investigations/<id>/responses/`.
3. Process the received portion through `evidence_intake_trigger.md` immediately — do not wait for the withheld portion.
4. For each redaction or withholding:
   - Identify the claimed basis (privilege, exemption, privacy).
   - Create a redaction log: page number, redaction location, claimed basis, assessment of validity.
5. Prepare a meet-and-confer letter (CPRA) or deficiency letter (subpoena) within 10 calendar days identifying:
   - What was requested but not produced
   - What was produced but improperly redacted
   - The legal basis for compelling the withheld material
6. If the partial response resolves any investigation question standing alone, update that investigation accordingly.

**Escalation Path:**
- If meet-and-confer fails within 15 calendar days → `escalation_pipeline.md` (appropriate section based on original request type)

**Documentation Requirements:**
- Everything from POSITIVE, plus:
- Redaction log (page, location, claimed basis, validity assessment)
- List of categories requested but not produced
- Meet-and-confer letter (date sent, method, response deadline given)
- Comparison: what was requested vs. what was produced (gap analysis)

---

## Response Type 4: SEALED (Court-Sealed Records)

The records exist but are sealed by court order.

**Next Action:**
1. Log in investigation JSON (`status` → `SEALED`).
2. Obtain and file a copy of the sealing order if possible.
3. Identify:
   - Which court sealed the records
   - The case number associated with the sealing order
   - The date of the sealing order
   - The legal basis cited (CRC 2.550, CRC 2.551, specific statute)
   - Whether Michael is a party to the sealed proceeding
4. Evaluate unsealing options:
   - **CRC 2.551(h)** — Motion to unseal: any person may file. Must show: (1) the records are not exempt from disclosure; (2) sealing is not necessary to protect an overriding interest; or (3) a less restrictive means exists.
   - **If the sealed record IS the conservatorship** (INV-04): this is the root finding. The existence of the sealed record is itself evidence. File motion to unseal under CRC 2.551(h) and simultaneously notify CA_Probate_Conservatorship_Litigator.
5. For sealed records in a case where Michael is a party: he has standing to move for access to his own case file under the due process clause.

**Escalation Path:**
- Motion to unseal under CRC 2.551(h) — filed in the court that issued the sealing order.
- If the sealing court is unknown or refuses to identify itself: file a petition for writ of mandate in the appellate division (CCP § 1085).

**Documentation Requirements:**
- Copy of sealing order (or confirmation that it exists but cannot be obtained)
- Court, case number, date of order
- Legal basis cited in order
- Standing analysis for unsealing motion
- Draft motion to unseal (filed in `drafts/` when prepared)

---

## Non-Response (No Reply Within Statutory Period)

Not a response type — it is the absence of one. Treated as a trigger for escalation.

**CPRA requests:** If no response within 10 calendar days (Gov. Code § 7922.535), the request is deemed denied. Escalate immediately per `escalation_pipeline.md` § 1.

**Subpoenas:** If no objection or production by the return date, the subpoena is deemed unanswered. Escalate per `escalation_pipeline.md` § 2 (motion to compel + sanctions under CCP § 1987.2).

**Court clerk requests:** If no response within 5 business days, escalate per `escalation_pipeline.md` § 3.

**Documentation Requirements:**
- Date request was sent (with proof of service/mailing)
- Statutory deadline
- Date deadline passed with no response
- Screenshot or log showing no communication received
