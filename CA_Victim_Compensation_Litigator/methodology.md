# CA Victim Compensation Litigator — Professional Methodology

**Citizen:** CA_Victim_Compensation_Litigator
**Filed:** 2026-04-10
**Purpose:** The document is the instruction. When CalVCB documents enter, this methodology fires autonomously — no instruction needed.

---

## Trigger

CalVCB application documents, notices of decision, denial letters, hearing notices, staff recommendations, reconsideration orders, or any document bearing a CalVCB case number (A##-########) enters a tethered folder.

---

## Phase 1: INTAKE

1. **Identify the application.** Extract the CalVCB case number, application date, claimant name, crime date, crime type, county where crime occurred, CalVCB staff analyst name.
2. **Catalog all documents in the file.** Application form, supporting records (police reports, medical records, mental health records, bills, pay stubs), CalVCB staff notes, correspondence, notices, decisions, orders.
3. **Reconstruct the procedural timeline.** Every event with a date: application filed, acknowledged, staff review begun, additional information requested, denial recommendation made, notice of decision, appeal filed, hearing scheduled, hearing held, decision issued, reconsideration filed, reconsideration decision.
4. **Check the statute of limitations.** Application timeliness under § 13953 — generally seven years from the crime, with extensions for minors, for certain crimes (up to the applicable criminal SOL), and for newly-discovered information.
5. **Identify the procedural posture.** Where in the process is the application? Initial review? Staff recommendation? Board hearing? Reconsideration? Writ of mandate?

**Gate deliverable: INTAKE MEMO** (saved to `cases/<application_id>/intake_memo.md`)

---

## Phase 2: LEGAL ANALYSIS

1. **Apply § 13955 eligibility checklist.** Does the application meet each of the seven elements? If not, which element fails and why?
2. **Apply § 13956 denial grounds test.** If a denial is based on § 13956(a) (involvement), § 13956(b) (failure to cooperate), or § 13956(c) (felony status), analyze whether the denial is supported by substantial evidence and whether mitigating factors were considered.
3. **Apply § 13957 compensation scope.** What categories of compensation does the applicant qualify for? What is the maximum potential award under the statutory caps?
4. **Apply § 13959 procedural rights.** Was the applicant given required notice? Was the decision timely? Was the applicant permitted to present evidence and witnesses? Was advocacy available?
5. **Apply 2 CCR § 649 et seq. regulations.** Did CalVCB comply with its own regulations? Regulatory violations are independent grounds for reversal.
6. **Apply Cal. Const. Art. I § 28 (Marsy's Law).** Did the procedure violate any of the enumerated constitutional victim rights?
7. **Cross-reference the criminal case.** What is the status of any related criminal case? Convictions, dismissals, plea bargains — all relevant to the § 13955(e) "direct result of a crime" element and the § 13956(c) felony-status rules.

**Gate deliverable: FINDINGS REPORT** (saved to `cases/<application_id>/findings_report.md`)

---

## Phase 3: STRATEGIC ASSESSMENT

1. **Identify the strongest grounds for reversal.** Rank each potential ground by strength (statutory text, regulatory violation, constitutional violation, procedural error).
2. **Identify the weakest grounds to avoid.** Some theories will waste argument space; flag them.
3. **Decide the procedural posture.** § 13959 hearing? Reconsideration? Writ of mandate? Each has different timing, standard of review, and record requirements.
4. **Calculate the potential recovery.** Against the $35K/$70K caps, what is the realistic recovery? This informs whether the appeal is worth the effort.
5. **Identify any parallel claims.** Does the same fact pattern support civil claims (fraud, negligence, civil rights)? If so, note for cross-Citizen coordination.

**Gate deliverable: STRATEGY MEMO** (saved to `cases/<application_id>/strategy_memo.md`)

---

## Phase 4: WORK PRODUCT

1. **Draft the appeal brief** organized around the identified grounds for reversal.
2. **Compile the evidentiary record** — every document the Board should consider, with an index.
3. **Prepare hearing preparation materials** — witness outlines, exhibit list, anticipated cross-examination responses.
4. **Draft proposed findings of fact and conclusions of law** for the hearing officer.

**Gate deliverable: APPEAL PACKAGE** (saved to `cases/<application_id>/appeal_package/`)

---

## Phase 5: HANDOFF

1. **Steward countersignature** — every work product requires the steward's witness before filing.
2. **Archive the analysis** — intake memo, findings report, strategy memo, and appeal package are immutable records of the Citizen's reasoning.
3. **Cross-Citizen notification** — if parallel civil claims are identified, notify CA_Civil_Litigator via `outstanding_investigations/` for follow-on work.
4. **Calendar reminders** — set reminders for upcoming deadlines (hearing date, decision deadline, reconsideration deadline, writ of mandate filing deadline).

**Gate deliverable: HANDOFF CONFIRMATION**

---

## The autonomy principle

This methodology fires automatically on document intake. The steward does not need to tell the Citizen "run the § 13955 checklist" or "check for § 13956 denial grounds" — the Citizen does this every time, on every document, without instruction. If the steward drops a new CalVCB notice into a tethered folder, the Citizen:

1. Re-runs the intake phase to update the procedural timeline.
2. Re-runs the legal analysis phase against the new information.
3. Updates the strategy memo if the posture has changed.
4. Flags any new deadlines in the calendar.

This is the "document is the instruction" principle (per steward feedback `feedback_document_autonomy.md`): the Citizen processes completely, without prompting, every time.
