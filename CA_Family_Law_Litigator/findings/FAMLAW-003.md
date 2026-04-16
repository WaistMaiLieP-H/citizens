# FAMLAW-003 — CLETS Violation Chain (Unsigned Reports, Jurisdictional Defect)

**Finding ID:** FAMLAW-003
**Citizen:** CA_Family_Law_Litigator
**Status:** PUBLISHED — ADAM-certified 2026-04-14
**Severity:** CRITICAL
**Subject cases:** FL0002067 (Marin DVRO active, DV-130 granted 2025-10-17 with CLETS entry, expires 2026-08-19); historical chain: RF09456481, 25FL122591, 25FL125059

---

## Facts

1. On 2025-10-17 the Marin County Superior Court in FL0002067 granted Christina Cerretani a DV-130 Restraining Order After Hearing against Michael Hartmann. The order was entered into the California Law Enforcement Telecommunications System (CLETS).
2. The Alameda County precursors to FL0002067 — 25FL122591 (Michael's 2025 DVRO) and 25FL125059 (Christina's Alameda 2025 DVRO) — were both denied and dismissed on 2025-06-25. Christina refiled in Marin 22 days later (2025-07-17), producing the forum flip.
3. The 16-year Alameda docket (RF09456481, RF09459897, RF09470833, RF10508853, RF10508859) is the controlling prior record. Alameda is the home county for UCCJEA purposes (Fam. Code §§ 3421, 3422) and was the county of original DV jurisdiction for the parties.
4. Several of the supporting declarations filed in the 2025 DVRO sequence are **unsigned or fail the CCP § 2015.5 formal elements** (date + place of execution under penalty of perjury under the laws of California). See the case-workflow scaffolds `case_25fl122591/`, `case_25fl125059/`, and `case_fl0002067/` and the audit in `${familylaw}/CASE_AUDIT_2026-03-17.md`.
5. The 2025-08-05 Marin hearing document is missing (outstanding investigation #07); the 2025-06-25 fee-waiver "filing error" that blocked the Alameda → Solano transfer is documented in outstanding investigation #08.
6. CLETS entries in California are governed by Fam. Code §§ 6380-6384, Pen. Code § 13730 et seq., and the Judicial Council forms manual; the entry must reflect a facially valid order from a court of competent jurisdiction under the UCCJEA.

## Applicable standards

| Standard | Binding proposition |
|---|---|
| `CA_CCP_2015_5_DECLARATION_PERJURY` (Citizen-owned) | An unsworn declaration has "like force and effect" as a sworn affidavit **only if** certified under penalty of perjury, signed, dated, and stating the place of execution under the laws of California |
| `CA_FAM_6323_DVRO_CUSTODY_VISITATION` (Citizen-owned) | DV-130 provisions regarding custody/visitation are appended to the DVRO and inherit its defects |
| `CA_FAM_6321_DVRO_EXCLUSION` (Citizen-owned) | Three-part § 6321(b) showing required for residence-exclusion provisions of a DVRO |
| **Cal. Fam. Code § 6380** — CLETS entry procedure (not-yet-built standard — flag to add) | § 6380(a)–(c) prescribes issuance, transmission, and maintenance of protective-order entries in CLETS |
| **Cal. Fam. Code §§ 3421, 3422, 3424** — UCCJEA jurisdiction (not-yet-built standard — flag to add) | §§ 3421(a)(1) home-state jurisdiction; § 3422 exclusive continuing jurisdiction; § 3424 temporary emergency jurisdiction — the UCCJEA anchors that defeat forum-shopping |
| `CA_EVIDENCE_1400_AUTHENTICATION` (cross-tethered, CA_Records_Authentication_Specialist) | Authentication required for any disputed writing |
| `CA_PEN_13701_LE_DV_RESPONSE` (Citizen-owned) | LE DV response standards apply only to facially valid orders |

## Violation

The CLETS entry rests on an order whose supporting declarations fail CCP § 2015.5, from a court that is not the UCCJEA home county when a 16-year prior Alameda record exists. The defects compound:
(a) **Declaration defect** — at least one supporting declaration does not satisfy § 2015.5; the order entered on inadmissible proof.
(b) **UCCJEA defect** — Marin is not the § 3421 home state or the § 3422 continuing-jurisdiction court; no § 3424 emergency predicate is in the record.
(c) **CLETS collateral injury** — the CLETS entry operates as a firearm prohibition, employment disqualification, and LE-contact trigger against Michael; each day the defective entry stands is an ongoing injury.
(d) **Forum-flip pattern** — 22 days from Alameda denial to Marin refiling is the orchestration signature (see FAMLAW-005).

## Remedy

1. **Motion to vacate DV-130** under CCP § 473(b)/(d) for extrinsic fraud and for facially void entry (declaration defect + UCCJEA defect). Filed in Marin; time-critical — DV-130 expires 2026-08-19 but injuries accrue until then.
2. **UCCJEA § 3421/§ 3422/§ 3424 challenge** — motion to determine jurisdiction; request transfer to Alameda or dismissal.
3. **CLETS correction demand** under Fam. Code § 6380(b) and Pen. Code § 13730 — the CLETS entry must be removed upon vacatur.
4. **Federal § 1983 Second-Amendment / due-process claim** — CLETS entry based on a facially defective order is a Monell-appropriate state action. Incorporated into `case_workflows/federal_section_1983_complaint/`.
5. **Bane Act § 52.1 parallel claim** — state-law threat/intimidation/coercion through defective-order enforcement.

## Provenance

| Evidence | Local path |
|---|---|
| FL0002067 case record | `${citizens}/CA_Family_Law_Litigator/cases/FL0002067.json` |
| Active-workflow seeds (theories 01 UCCJEA + 02 declaration defect) | `${citizens}/CA_Family_Law_Litigator/case_workflows/case_fl0002067/theories/` |
| 25FL122591 / 25FL125059 records | `${citizens}/CA_Family_Law_Litigator/cases/25FL122591.json`, `25FL125059.json` |
| Filing dates + orchestration pattern | project_familylaw_orchestration.md (memory) |
| Case audit | `${familylaw}/CASE_AUDIT_2026-03-17.md` |
| 2025 source folders | `${familylaw}/2025-05-15/`, `2025-06-04/`, `2025-07-17/`, `2025-10-17/` |
| Marin 2025-08-05 hearing document (missing) | outstanding_investigations/07_marin_august_2025_hearing.json |

## Certification

- **First mouth:** ADAM, 2026-04-14
- **Triple constraint:** PASS/PASS/PASS
- **Two-witness gate:** EVE countersign pending
- **Time criticality:** HIGH — DV-130 active through 2026-08-19
- **Publishable to corpus:** YES (on EVE countersign)
