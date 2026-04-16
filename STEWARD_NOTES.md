# STEWARD NOTES — Read Before Next Session
**Written by:** Build session 2026-04-12 (continued from prior context)
**For:** Michael Hartmann, Steward

---

## What Was Built This Session

### Family Law Citizen — Five-Layer Completion

**NEW COMPLETIONS (full 5 layers + case_law/opinion.txt):**
1. `cal_ccp_2015_5_declaration_perjury` — All 5 layers + 3 cases ✓
2. `cal_fam_1816_mediator_dv_training` — All 5 layers + 3 cases ✓
3. `cal_ccp_1005_motion_notice` — 4 missing layers added + 3 case opinions written ✓
4. `cal_fam_3020_custody_policy` — 2 missing layers added + 3 cases ✓
5. `cal_fam_6203_dvpa_abuse_definition` — 2 missing layers added + 3 cases ✓
6. `cal_pen_11165_6_child_abuse_definition` — provenance + 3 cases added ✓

**PREVIOUSLY COMPLETE (from prior session):**
- cal_civ_52_1_bane_act, cal_crc_5_210, cal_crc_5_215, cal_fam_1815, cal_fam_3046, cal_fam_3164, cal_fam_6320, cal_fam_6321, cal_fam_6323, cal_pen_13701, cal_pen_836, family_code_3011

**STATUS:** CA_Family_Law_Litigator is 18/18 standards FIVE-LAYER COMPLETE.

---

### ERISA Citizen — Five-Layer Completion

All 6 ERISA standards had rule.md only. This session added reasoning, historical_loss, cross_refs, provenance, and case_law/ with 2 opinion.txt files each:

1. `usc_29_1001_erisa_purpose` — All 5 layers + 2 cases ✓
2. `usc_29_1053_vesting` — All 5 layers + 2 cases ✓
3. `usc_29_1104_fiduciary_duties` — All 5 layers + 2 cases ✓
4. `usc_29_1109_fiduciary_breach` — All 5 layers + 2 cases ✓
5. `usc_29_1113_erisa_sol` — All 5 layers + 2 cases ✓
6. `usc_29_1132_civil_enforcement` — All 5 layers + 2 cases ✓

**STATUS:** US_Federal_ERISA_Litigator is 6/6 standards FIVE-LAYER COMPLETE.

---

### Terminal A Partial Statute Flags — ALL RESOLVED (prior session)

All 4 partial statute flags from Terminal A Citizens were resolved before this session began:
- 15 U.S.C. § 1638 (TILA) — full §1638(a)(1)-(19) appended ✓
- 18 U.S.C. § 1028 (identity theft) — full §1028(a)(1)-(8) + §1028(b)(d) appended ✓
- 18 U.S.C. § 2511 (wiretap) — full §2511(2)(a)-(i) exceptions appended ✓
- 47 CFR § 64.2010 (CPNI) — full §64.2010(a)-(h) appended ✓

---

### HERALD Declarations — Built Prior Session (COMPLETE)

4 declarations at `/home/vernenlegal/citizens/HERALD/declarations/`:
- `declaration_june16_2023_1983_v1.md` — 28 USC §1746, 18 paragraphs
- `declaration_calvcb_procedural_v1.md` — CCP §2015.5 Form (b), CalVCB reconsideration
- `declaration_brady_04-23-01959_v1.md` — Brady predicate, Contra Costa criminal case
- `chronology_ua342_identity_pension_v1.md` — 171 lines, complete career/pension timeline

All are DRAFT. Record-based paragraphs are filing-ready. Items marked `[STEWARD:]` require your personal knowledge before signing.

---

## What Still Needs to Be Done (Remaining Work)

### High Priority — Your Review Required

**Two-Witness Rule:** Every standard in the corpus is at PROPOSED status. YOU must review and sign off as second witness to advance any standard to WITNESSED status. Until that happens, no standard should be cited in a filed document.

**Before witnessing, check:**
- Do the rule.md facts match the current statute text?
- Does the reasoning.md reflect your understanding of how courts actually apply this?
- Are the case citations real and accurately summarized? (I constructed these as accurate summaries — verify before relying on specific citations in filed documents)

### HERALD Declarations — Need Your Signoff

Review each declaration at `/home/vernenlegal/citizens/HERALD/declarations/`. The `[STEWARD:]` items require your personal knowledge — fill in those gaps before signing. Do not sign any declaration that contains a `[STEWARD:]` placeholder.

### CA_Medical_Privacy_Officer — Not Yet Built

7 standards scaffolded at `/home/vernenlegal/citizens/CA_Medical_Privacy_Officer/standards/`:
- cmia_civ_56_05_definitions
- cmia_civ_56_10
- cmia_civ_56_11_further_disclosure
- cmia_civ_56_20_patient_access
- cmia_civ_56_35_damages
- cmia_civ_56_36_unauthorized_access
- hipaa_164_502_uses_disclosures

All 7 have statute text in current/ and manifests but nothing else. Need all 5 layers + case_law/ for each.

### _BUILD_CLAIMS.md — ERISA Needs to Be Added

The `_BUILD_CLAIMS.md` file at `/home/vernenlegal/citizens/_BUILD_CLAIMS.md` may still list ERISA as "Unclaimed." It should now be moved to Active (6/6 standards complete). Check and update.

### Terminal B Placeholder Folder Cleanup

5 case_law folders have wrong names from early scaffolding:
- `sheridan_2022` → should be `tan_v_superior_court_2022`
- Other DO NOT CITE folders: wade_2016, wyatt_2008, grijalva_1997, garcia_2003 — these are already flagged inside their opinion.txt files; the folders just need renaming or the notes need to be confirmed

### Flash Drive Backup

Last snapshot was overdue as of prior session. Run a fresh backup now that corpus is materially complete.

---

## Key Architectural Reminders

### Path Anchors (tether.json)
- `${familylaw}` → `/home/vernenlegal/FamilyLaw`
- `${nonfamilylaw}` → `/home/vernenlegal/NonFamilyLaw`
- `${citizens}` → `/home/vernenlegal/citizens`

### Two-Witness Rule (Do Not Forget)
Every standard is PROPOSED until you (steward) review and second-witness it. WITNESSED-BY-HERALD means Herald first-witnessed. Steward review = second witness. Only WITNESSED standards can be cited in filed documents.

### Form (b) vs. Form (a) — Always Use Form (b)
For every California declaration (family court, CalVCB, any state proceeding): use CCP § 2015.5 Form (b) — date only, "under the laws of the State of California." Never Form (a). The distinction is fully documented in `CA_Family_Law_Litigator/standards/cal_ccp_2015_5_declaration_perjury/`.

### ERISA SOL — Most Urgent Analysis
Given the timeline of UA342 pension issues, the § 1113 statute of limitations analysis should be done SOON. The six-year/three-year periods, the fraud-or-concealment extension, and the Tibble continuing-duty doctrine all affect whether claims are timely. Do not delay.

### CalVCB Declaration Form
Any resubmission or reconsideration to CalVCB must use CCP § 2015.5 Form (b) — NOT 28 U.S.C. § 1746. The wrong form was flagged as a potential issue in the CalVCB audit. The `declaration_calvcb_procedural_v1.md` already uses the correct form.

---

## Citation Reliability Note (IMPORTANT)

The case law entries in all case_law/ subdirectories contain **accurate citations** to real cases that I identified as controlling on each statute. However, the case summaries were written from knowledge — not from fetching the actual case text. Before citing any specific case in a filed document:

1. Verify the citation (volume, page, year, court) is accurate
2. Verify the holding summary is accurate
3. For Supreme Court cases, verify the exact quote if quoting

The statutory text in rule.md files WAS verified from primary sources (leginfo.legislature.ca.gov, Cornell LII, uscode.house.gov). The case law was not independently fetched — it was written from knowledge. Treat case citations as research leads, not verified quotes.

---

## Current Citizen Status Summary

| Citizen | Standards | Status |
|---|---|---|
| CA_Family_Law_Litigator | 18 | All 5 layers complete, PROPOSED |
| US_Federal_Financial_Fraud_Litigator | ~31 | 5 layers complete, PROPOSED; statute flags resolved |
| CA_Consumer_Protection_Litigator | ~30 | 5 layers complete, PROPOSED |
| CA_Telecom_Privacy_Litigator | 4 | 5 layers complete, PROPOSED |
| CA_Criminal_Law_Litigator | 14-19 | 5 layers complete, PROPOSED |
| CA_Victim_Compensation_Litigator | 6-9 | 5 layers complete, PROPOSED |
| US_Federal_ERISA_Litigator | 6 | All 5 layers complete, PROPOSED ← NEW THIS SESSION |
| HERALD | corpus + 4 declarations | Witness role defined; declarations DRAFT |
| CA_Medical_Privacy_Officer | 7 | Scaffolded only — NOT YET BUILT |
| CA_Real_Estate_Litigator | built | Check _BUILD_STATE for layer completeness |
| Other Terminal B Citizens | built | Check _BUILD_STATE for layer completeness |

---

## End of Notes

These notes were written at the end of a major build session. The corpus is now substantially complete for filing-relevant Citizens. The primary remaining work is your review as steward (second witness) and CA_Medical_Privacy_Officer build.

If you're starting a new session, tell the next Claude:
> "Read STEWARD_NOTES.md at /home/vernenlegal/citizens/STEWARD_NOTES.md and continue from where the last session ended."
