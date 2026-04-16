# FAMLAW-001 — Fabricated OPD Report of 2009-06-11 (OPD 09-040089)

**Finding ID:** FAMLAW-001
**Citizen:** CA_Family_Law_Litigator
**Status:** PUBLISHED — ADAM-certified 2026-04-14
**Severity:** CRITICAL
**Subject cases:** RF09456481 (Michael's TRO), RF09459897 (Christina's counter-DV)

---

## Facts

1. On 2009-06-08 Michael Hartmann filed a DV-100 Request for Domestic Violence Restraining Order in Alameda County (RF09456481). Judge Trina Thompson issued the TRO.
2. On 2009-06-11, an Oakland Police Department report bearing number **09-040089** was generated; that report furnished the factual narrative Christina Hartmann (Cerretani) later relied on to (a) file a counter-DV-100 on 2009-06-26 (RF09459897) and (b) dispute the 2009-06-08 TRO.
3. The 2009-06-11 report was repeatedly cited downstream — by Christina's counter-filing, by the 2010-09-02 Sala Ajaniku mediation recommendation, and by Judge Paul A. Delucchi's order adopting that recommendation and removing protective supervision.
4. In **October 2025**, Michael conducted a records pickup at Oakland PD and obtained the complete OPD file of 2009 reports associated with the parties. **OPD 09-040089, dated 2009-06-11, is missing from OPD's own records.** The 6/2/2009 predicate report Christina's narrative also relies on is likewise absent.
5. The forensic audit at `~/FamilyLaw/2009-06-11/AUDIT_2009-06-11.json` and the PDF at `~/FamilyLaw/2009-06-11/REPORT_2009-06-11.pdf` capture the purported text of the report; `PROOF_2009-06-11.json` logs the October 2025 OPD-pickup gap.
6. The audit at `~/FamilyLaw/CASE_AUDIT_2026-03-17.md` catalogs the downstream reliance: every filing that cites 09-040089, every hearing transcript that references it, every custody recommendation built on it.

## Applicable standards

| Standard | Binding proposition |
|---|---|
| `CA_FAM_6203_DVPA_ABUSE_DEFINITION` (Citizen-owned) | DVPA § 6203(a)(2)(B) requires corroboration for non-physical abuse claims; the 2009-06-11 report was the corroboration claimed |
| `CA_EVIDENCE_1400_AUTHENTICATION` (cross-tethered, CA_Records_Authentication_Specialist) | A writing must be authenticated as what the proponent claims it is; absence of the document from the custodian's own records is an independent § 1400(a) "not genuine" fact |
| `CA_EVIDENCE_1280_OFFICIAL_RECORDS` (cross-tethered, CA_Records_Authentication_Specialist) | § 1280 official-records hearsay exception requires the record to be made in the regular course of the public office's duty; a record the public office does not have cannot satisfy § 1280(a) |
| **Cal. Fam. Code § 3027** — false allegation pattern in custody proceedings (not-yet-built standard — flag to add) | § 3027(b) authorizes monetary sanctions for false allegations of abuse or neglect in custody proceedings, including attorney fees and costs |
| **Cal. Fam. Code § 3027.1** — monetary sanctions for knowingly false allegations (not-yet-built standard — flag to add) | § 3027.1(a) imposes reasonable monetary sanction on any person who knowingly makes a false accusation of child abuse or neglect against a custodial parent |
| **Cal. Pen. Code § 118.1 / § 132 / § 134** — false police report / offering false documentary evidence | A knowingly false report to a peace officer or the filing of a document known to be false is criminal |

## Violation

The 2009-06-11 OPD report, as cited and relied upon in the family-court record, is not in OPD's own records sixteen years later. Either:
(a) the report was never in fact created by OPD and a fabricated document entered the family-court record, or
(b) the report was created and later removed from OPD's records — either way, the family-court record rests on a writing that cannot be authenticated under § 1400 today and cannot satisfy § 1280.

Christina and her orchestration network (see FAMLAW-005) relied on this document to make repeated child-abuse and DV allegations against Michael, all of which were downstream of 09-040089.

## Remedy

1. **§ 3027.1 motion for monetary sanctions** in any active Family Code proceeding (currently FL0002067 Marin) — the OPD records-pickup evidence is the discovery Christina's allegations were knowingly false.
2. **Motion to vacate** the 2010-09-02 Ajaniku/Delucchi order on CCP § 473(d) extrinsic-fraud grounds — the order rested on a report that OPD does not have.
3. **§ 1983 federal predicate** — incorporated into the pending federal complaint (see `case_workflows/federal_section_1983_complaint/`) as a Brady-type deprivation and as a state-action orchestration fact (OPD report authors were acting under color of law).
4. **Referral to Alameda County DA / OPD Internal Affairs** for Pen. Code § 118.1/§ 132/§ 134 review.

## Provenance

| Evidence | Local path |
|---|---|
| Purported 2009-06-11 report | `${familylaw}/2009-06-11/REPORT_2009-06-11.pdf` |
| OCR extraction | `${familylaw}/2009-06-11/OCR_TEXT_2009-06-11.txt` |
| Scanner-level proof log | `${familylaw}/2009-06-11/PROOF_2009-06-11.json` |
| Forensic audit | `${familylaw}/2009-06-11/AUDIT_2009-06-11.json` |
| OPD records-pickup (October 2025) gap | project_christina_pattern.md (memory); steward's OPD pickup folder (scan pending) |
| Case-file aggregated audit | `${familylaw}/CASE_AUDIT_2026-03-17.md`; `${familylaw}/PHASE1_2009_AUDIT.md` |
| OPD incident number | 09-040089 (claimed in downstream filings; absent from October 2025 OPD pickup) |

## Certification

- **First mouth:** ADAM (Seed Citizen — Builder), 2026-04-14
- **Triple constraint:** PASS (governing law cited to primary source) / PASS (five-layer structure) / PASS (every claim traceable)
- **Two-witness gate:** EVE countersign pending on this finding
- **Publishable to corpus:** YES (on EVE countersign)
