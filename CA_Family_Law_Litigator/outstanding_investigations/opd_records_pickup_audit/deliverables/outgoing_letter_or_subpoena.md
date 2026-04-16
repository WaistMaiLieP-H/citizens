# OPD 2009-Report Desk Audit — Internal Protocol

**Investigation:** opd_records_pickup_audit
**Prepared:** 2026-04-15
**Owner:** Steward (Michael Hartmann)
**Not an outgoing letter.** This investigation resolves by **internal cross-reference**, not by external request. The deliverable is the completed audit matrix. (External OPD outreach is already satisfied by the October 2025 records pickup, which is the ground-truth dataset.)

---

## Purpose

For each filing in every related case that cited an **Oakland Police Department 2009 report**, verify whether the cited report actually exists in OPD's records system as confirmed by the **October 2025 OPD records pickup**.

Ground truth (per project_christina_pattern.md): OPD's responsive production in October 2025 shows only **two (2) 2009 reports** connected to the steward / Cerretani situation. The 6/2/2009 5150 incident (Christina pulling a 10-inch kitchen knife) is **missing**. The 6/11/2009 OPD report **09-040089** exists but is flagged by Vernen overlay rule **POST-002B** for POST violations.

## Scope (related cases)

- RF09456481 — Alameda Family Law
- RF09459897 — Alameda Family Law
- RF09470833 — Alameda Family Law
- All downstream filings that reach back to a 2009 OPD citation (DV-100/DV-130, FL-150 declarations, mediator reports, § 3118/§ 730 evaluations, criminal complaints that cite the incident).

## Audit matrix (one row per filing)

| Row | Filing ID | Case # | Filing date | Cited OPD report # | Cited date | Author / declarant | Quoted factual assertion | Exists in Oct-2025 OPD pickup? | POST-002B flag? | Finding |
|-----|-----------|--------|-------------|--------------------|------------|---------------------|--------------------------|--------------------------------|-----------------|---------|
| 1 | | | | | | | | yes / no / partial | yes / no | CONFIRMED / MISSING / FABRICATED / POST-DEFECT |

## Finding categories

- **CONFIRMED** — filing cites a report that exists in the October 2025 pickup and contents match.
- **MISSING** — filing cites a report that does **not** exist in the October 2025 pickup → presumptive § 3027 false allegation + § 2015.5 perjury exposure + Pen § 118.1/§ 148.5 predicate.
- **PARTIAL-MATCH** — report exists but filing misquotes or expands the contents → Evid § 1280 unreliability + § 3027.1 false sex-abuse-allegation overlay if applicable.
- **POST-DEFECT** — report exists but Vernen overlay POST-002B flags authoring / supervisory / classification violations → Evid § 1280 "sources of information" prong fails; § 1401/§ 1402 authentication challenge.

## Deliverables produced by completing the audit

1. Completed matrix (CSV + markdown) under `findings/opd_2009_audit_matrix.md`.
2. One **FAMLAW-finding supplement** per MISSING / FABRICATED row, filed under `findings/` referencing FAMLAW-001 (6/11/2009 fabricated OPD 09-040089).
3. Cross-reference additions into HERALD's contradictions log for every filing that relies on a MISSING report.

## Execution checklist

- [ ] Pull every case-file filing 2009-2025 across RF09456481, RF09459897, RF09470833 that cites an OPD report from 2009.
- [ ] Retrieve October 2025 OPD pickup inventory (PDF + metadata).
- [ ] For each cited report number, query the pickup inventory.
- [ ] Fill in the matrix row-by-row; do not skip rows.
- [ ] For every MISSING / PARTIAL-MATCH row, draft a finding supplement within 3 business days.
- [ ] HERALD countersign when matrix is complete.

## Legal anchors

- CA Fam. Code § 3011(a)(2) — best-interest DV factor requires a verified predicate.
- CA Fam. Code § 3027 — false-allegation pattern.
- CA Fam. Code § 3027.1 — sanctions for knowingly false child-abuse allegations.
- CA Fam. Code § 6203 — DVPA abuse definition.
- CA Evid. Code § 1280 — official-records hearsay exception (requires trustworthy sources).
- CA Evid. Code § 1400 / § 1402 — authentication and altered-writing burden.
- CA Pen. Code § 148.5 — false report of crime.
- Vernen overlay **POST-002B** — OPD POST-compliance screen.
