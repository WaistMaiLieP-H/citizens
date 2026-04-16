# LPS Pipeline Audit — Case Workflow

**Citizen:** CA_Mental_Health_Litigator
**Workflow:** Comprehensive audit of any LPS confinement episode using the five-standard LPS expansion pack.
**Built:** 2026-04-15

---

## Purpose

Given any documented LPS confinement event (hold, certification, extension, conservatorship petition), produce a four-gate compliance audit identifying every statutory defect preservable or collaterally attackable.

## Inputs

- The person's medical/LPS record for the confinement window.
- Facility admission documentation (§ 5150 application, § 5250 certification, § 5270.15 certification).
- Facility designation status (county IT-designation letters).
- Any § 5256 certification-review hearing transcripts or § 5275 judicial-review records.
- Every release-of-information form, subpoena, and third-party disclosure in the record.
- Any SUD diagnosis anywhere in the chart (triggers § 290dd-2 audit).

## Pipeline Steps

**Step 1 — § 5150 audit** (existing standard `wic_5150_involuntary_hold`)
- Written probable-cause statement? Specific facts or conclusory?
- Third-party statement basis? If yes — civil-liability candidate under § 5150(e).
- § 5150(g) advisement documented?
- Patient advocate § 5150(k) notification if held beyond 72 hours?

**Step 2 — § 5250 audit** (`wic_5250_14_day_certification`)
- Independent clinical analysis by facility staff? Or reaffirmation of § 5150?
- Facility actually county-designated for IT? (Check designation letters.)
- Voluntary refusal documented or assumed?
- Gravely-disabled finding? If yes — § 5250(d) written-family-offer documentation?

**Step 3 — § 5270.15 audit** (`wic_5270_15_additional_30_day`)
- County opted into Article 4.5? Confirm.
- Independent continued-grave-disability finding? (Not re-statement of § 5250.)
- 10-day interval reviews present? (Days ~10, ~20, ~30.)
- Daily treatment-plan monitoring notes present?
- 36-hour family notice attempted? Or suppressed per documented patient request?

**Step 4 — § 5325 audit** (`wic_5325_patients_rights`)
- Posting documentation for patients' rights in appropriate languages?
- Advisement log showing how rights were explained?
- Handbook receipt signed at admission?
- Advocate visit log with advocate's organizational affiliation (independence)?
- Any ECT, convulsive, or psychosurgery event? Each is its own absolute-right audit.
- Any third-party waiver attempt (conservator/parent/guardian)? Void by statute.

**Step 5 — § 5328 audit** (`wic_5328_lps_confidentiality`)
- Every disclosure event: identify the numbered § 5328(a) or (b) exception.
- Every disclosure to a non-facility professional: documented patient/conservator consent?
- Every court-proceeding use: "as necessary to the administration of justice" showing?
- Every HIPAA-paralleled disclosure: 45 C.F.R. § 164.512(e) conditions met?
- Every redisclosure: traceable back to an authorized primary disclosure?

**Step 6 — § 290dd-2 / Part 2 audit** (`usc_42_290dd_2_substance_abuse_confidentiality`) — triggered whenever the record contains SUD/alcoholism diagnosis.
- Is the originating facility a "part 2 program" (federally-assisted SUD treatment)?
- Every disclosure: consent meeting Part 2 requirements, or § 290dd-2(b)(2)(C) court order, or emergency/research/audit exception?
- Every downstream recipient: received the prescribed redisclosure notice?
- Any use in criminal/civil/administrative/legislative proceeding: supported by heightened § 290dd-2(c) authorization?

## Outputs

- Per-gate compliance table (PASS / FAIL / UNKNOWN per each numbered requirement).
- List of preservable defects (to be raised at next available § 5256 or § 5275 hearing).
- List of collaterally-attackable defects (for civil suit, § 1983 action, or post-judgment relief in downstream proceedings).
- List of unauthorized-disclosure events (for separate civil action under § 5330 and § 290dd-2(f)).
- Steward verify queue (any federal statute/regulation whose text could not be live-fetched).

## Integrations

- **HERALD** — authenticates all records feeding the audit; signs declarations under penalty of perjury (CCP § 2015.5) for use in downstream filings.
- **CA_Probate_Conservatorship_Litigator** — downstream if the audit reveals a § 5350 conservatorship built on void § 5250/§ 5270.15 predicates.
- **US_Federal_Civil_Rights_Litigator** — § 1983 claims where state actors are in the disclosure chain.
- **CA_Family_Law_Litigator** — § 5328 and § 290dd-2 admissibility attacks on LPS records that appeared in family-court proceedings.

## Cases Covered

- **Dr. Wiita fraudulent competency evaluation** — § 5328 + § 720 + § 1401 + § 1402 four-layer attack; § 290dd-2 if SUD content was present.
- **Ward-system IT episodes** — every "IT" reference in the conservatorship breakthrough dossier audited against Steps 2-5 above.
- **LPS confidentiality violations in family-law audit** — every LPS record that surfaced in dissolution/custody/DVRO proceedings traced to a § 5328 exception.
- **Mother / dependent adult** — if LPS holds have occurred, same audit pipeline applies.
