# Steward Verification Pass — 2026-04-15

**Citizen:** CA_Family_Law_Litigator
**Standards reviewed:** 24
**Verified:** 22 | **Unverified:** 2
**Verifier:** Claude (Opus 4.6) under steward direction — Michael Hartmann
**Method:** Each statute fetched live via VernenLegal MCP tools (california_get_section, crc_get_rule) and compared against stored verbatim text. Six standards missing stored text were populated from live fetch.

| # | Standard | Statute | Verified | Notes |
|---|----------|---------|----------|-------|
| 1 | cal_ccp_1005_motion_notice | CCP § 1005 | YES | Stored text matches live source |
| 2 | cal_ccp_2015_5_declaration_perjury | CCP § 2015.5 | YES | Stored text matches live source |
| 3 | cal_civ_52_1_bane_act | Civ. Code § 52.1 | YES | Stored text matches live source |
| 4 | cal_crc_5_210_custody_mediation | CRC Rule 5.210 | NO | CRC tool returned "not found"; stored text present but not independently verified |
| 5 | cal_crc_5_215_dv_protocol | CRC Rule 5.215 | NO | CRC tool returned "not found"; stored text present but not independently verified |
| 6 | cal_fam_1815_counselor_qualifications | Fam. Code § 1815 | YES | Stored text matches live source |
| 7 | cal_fam_1816_mediator_dv_training | Fam. Code § 1816 | YES | Stored text matches live source |
| 8 | cal_fam_2030_needbased_attorney_fees | Fam. Code § 2030 | YES | Text fetched and saved; no prior stored text |
| 9 | cal_fam_217_live_testimony_right | Fam. Code § 217 | YES | Text fetched and saved; no prior stored text |
| 10 | cal_fam_3020_custody_policy | Fam. Code § 3020 | YES | Stored text matches live source |
| 11 | cal_fam_3027_false_child_abuse_sanctions | Fam. Code § 3027 | YES | Text fetched and saved; no prior stored text |
| 12 | cal_fam_3046_absence_dv | Fam. Code § 3046 | YES | Stored text matches live source |
| 13 | cal_fam_3048_custody_jurisdiction_abduction | Fam. Code § 3048 | YES | Text fetched and saved; no prior stored text |
| 14 | cal_fam_3100_visitation_orders_dv | Fam. Code § 3100 | YES | Text fetched and saved; no prior stored text |
| 15 | cal_fam_3164_mediator_qualifications | Fam. Code § 3164 | YES | Stored text matches live source |
| 16 | cal_fam_3170_mandatory_custody_mediation | Fam. Code § 3170 | YES | Text fetched and saved; no prior stored text |
| 17 | cal_fam_6203_dvpa_abuse_definition | Fam. Code § 6203 | YES | Stored text matches live source |
| 18 | cal_fam_6320_dvpa_enjoinable_behaviors | Fam. Code § 6320 | YES | Stored text matches live source |
| 19 | cal_fam_6321_dvro_exclusion | Fam. Code § 6321 | YES | Stored text matches live source |
| 20 | cal_fam_6323_dvro_custody_visitation | Fam. Code § 6323 | YES | Stored text matches live source |
| 21 | cal_pen_11165_6_child_abuse_definition | Pen. Code § 11165.6 | YES | Stored text matches live source |
| 22 | cal_pen_13701_le_dv_response | Pen. Code § 13701 | YES | Stored text matches live source |
| 23 | cal_pen_836_arrest_authority | Pen. Code § 836 | YES | Stored text matches live source |
| 24 | family_code_3011_best_interest | Fam. Code § 3011 | YES | Stored text matches live source |

## Actions Taken
- 22/24 manifests updated: `verified: true`, `verification_date: "2026-04-15"`
- 2/24 manifests updated: `verified: false` with discrepancy note (CRC rules — MCP tool limitation)
- 6 standards had missing verbatim text files — fetched from leginfo and saved to `current/`
- 0 substantive discrepancies found between stored and live statute text

## Open Items
- CRC Rules 5.210 and 5.215: require manual verification against courts.ca.gov (MCP crc_get_rule does not resolve these rules)