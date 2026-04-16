# Evidence Intake Trigger

**Citizen:** CA_Family_Law_Litigator
**Created:** 2026-04-15
**Purpose:** When new evidence arrives, this workflow maps it to the investigation it closes, the standards that need re-audit, and the scope of the re-audit.

---

## Trigger Rule

Any new artifact entering this Citizen's case file triggers this workflow. The artifact is classified by evidence type, matched to an investigation ID, and the affected standards are queued for re-audit. No human instruction is required — the document is the instruction.

---

## Evidence Type → Investigation → Standards Re-Audit Map

### 1. Agency PRA Responses

| Evidence Received | Investigation Closed/Advanced | Standards Requiring Re-Audit | Re-Audit Scope |
|---|---|---|---|
| Alameda SCSC — Ajaniku employment/credential records | INV-02 (ajaniku_pra_request) | cal_fam_3164, cal_fam_1815, cal_fam_1816 | Credential void becomes affirmative finding; re-audit every mediation recommendation Ajaniku authored |
| Alameda SCSC — Paredes/Ajaniku reassignment record | INV-06 (mediator_switch_reason) | cal_fam_3164, cal_crc_5_210 | Continuity violation assessment; re-audit the September 2010 mediation recommendation |
| DCA/Board of Psychology — Paredes license verification | INV-03 (paredes_license_verification) | cal_fam_3164, cal_fam_1815 | If no license found: Bus. & Prof. § 2903 violation; re-audit July 2009 evaluation |
| Alameda SCSC — fee waiver rejection/correction notice | INV-08 (alameda_solano_fee_waiver_filing_error) | (procedural — no standard re-audit) | Document the jurisdictional break in the chain; feed to case_25fl122591 and case_rf10508853 workflows |
| Benicia PD — dispatch logs / 911 recordings | INV-09 (benicia_pd_call_recordings) | cal_pen_13701_le_dv_response, cal_pen_836_arrest_authority | Re-audit law enforcement response protocol; feed to federal_section_1983_complaint |

### 2. Probate Court Docket Search Results

| Evidence Received | Investigation Closed/Advanced | Standards Requiring Re-Audit | Re-Audit Scope |
|---|---|---|---|
| Any county — conservatorship docket hit | INV-04 (conservatorship_existence_search) | ALL 24 standards (root mechanism) | If conservatorship confirmed: every case workflow must be re-audited for conservatorship overlay. Immediate cross-citizen handoff to CA_Probate_Conservatorship_Litigator. |
| All counties — negative search (no docket found) | INV-04 (partial advance) | None immediately | Shifts investigation weight to INV-05 (CMIA logs) as the remaining parallel path |
| Florida statewide — guardianship search result | INV-04 (conservatorship_existence_search) | Same as above if positive | Check for "Michael Vernen Thomas" alternate identity match |

### 3. Subpoena Returns — Medical Provider CMIA Logs

| Evidence Received | Investigation Closed/Advanced | Standards Requiring Re-Audit | Re-Audit Scope |
|---|---|---|---|
| Any provider — § 56.10(c)(12) disclosure log entry found | INV-05 (cmia_disclosure_log_subpoenas) | (Cross-citizen: CA_Medical_Privacy_Officer standards) | Identifies the requesting investigator, the proceeding, and the date. If probate court investigator: confirms conservatorship investigation regardless of docket search. Immediate handoff to CA_Probate_Conservatorship_Litigator. |
| All providers — no (c)(12) entries | INV-05 (closed negative) | None | Weakens conservatorship theory; document the negative finding |

### 4. Court Transcripts and Minute Orders

| Evidence Received | Investigation Closed/Advanced | Standards Requiring Re-Audit | Re-Audit Scope |
|---|---|---|---|
| Marin County — FL0002067 8/5/2025 hearing transcript | INV-07 (marin_august_2025_hearing) | cal_fam_217_live_testimony_right, cal_fam_3048_custody_jurisdiction_abduction, cal_fam_3020_custody_policy | Assess whether § 217 testimony right was violated; assess UCCJEA jurisdictional basis; feed to case_fl0002067 workflow |
| Any case — minute order showing Michael as both petitioner and respondent | INV-10 (michael_dual_filing_status) | cal_ccp_1005_motion_notice | Procedural irregularity documentation; feed to fee waiver investigation (INV-08) |

### 5. Carrier / Device Records

| Evidence Received | Investigation Closed/Advanced | Standards Requiring Re-Audit | Re-Audit Scope |
|---|---|---|---|
| AT&T/Verizon/T-Mobile — SIM swap records, CSLI data, account access logs | INV-11 (carrier_communications_device_proximity) | (Cross-citizen: CA_Telecom_Privacy_Litigator standards) | Feed to CA_Telecom_Privacy_Litigator for SCA/CPNI/CFAA analysis. If CSLI shows device co-location on 6/16/2023: feed to case_fl0002067 and federal_section_1983_complaint. |
| Apple/Google/Microsoft/Samsung — account recovery logs showing physical-proximity gates | INV-11 (carrier_communications_device_proximity) | (Cross-citizen: CA_Telecom_Privacy_Litigator standards) | Same routing as above |

### 6. OPD Records Cross-Reference (Desk Audit)

| Evidence Received | Investigation Closed/Advanced | Standards Requiring Re-Audit | Re-Audit Scope |
|---|---|---|---|
| Steward completes OPD records cross-reference against case filings | INV-01 (opd_records_pickup_audit) | family_code_3011_best_interest, cal_fam_6203_dvpa_abuse_definition, cal_ccp_2015_5_declaration_perjury | For each filing that cited a nonexistent OPD report: re-audit under § 2015.5 (perjury) and § 3027 (false abuse claims). Re-audit § 6203 abuse definition against actual OPD records. |

---

## Processing Steps

1. **Classify** — Match the incoming artifact to an evidence type above.
2. **Log** — Update the investigation JSON: change `status` from `READY_TO_SEND` or `OPEN` to `RESPONSE_RECEIVED`; add `response_received_at_utc` and `response_summary`.
3. **Queue Re-Audit** — For each standard listed in the re-audit scope, flag the standard's `opinion.txt` as `PENDING_RE_AUDIT` with a reference to the new evidence.
4. **Cross-Citizen Handoff** — If the map above indicates a cross-citizen handoff, execute `cross_citizen_handoff.md`.
5. **Case Workflow Update** — Update the relevant `case_workflows/*/workflow.json` with the new evidence reference.
6. **Steward Notification** — If the evidence resolves a CRITICAL investigation, flag for steward review before the re-audit opinion is finalized.
