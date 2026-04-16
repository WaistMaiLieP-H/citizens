# Family Law Junction Registry

**Purpose.** Family Law standards routinely incorporate rules owned by other Citizens (Criminal Law, Mental Health, Probate Conservatorship, Victim Compensation). Instead of copying those rules, junction files here point to the canonical location and record the legal relationship (incorporation, cross-application, preemption, or procedural bridge).

**Authority rule.** The canonical standard lives in the owning Citizen. A junction here does not restate the rule — it declares dependency and records how Family Law invokes it.

**Format.** One junction = one `.md` file. Each file has:
- `family_law_anchor:` — the Family Code / CCP / CRC standard inside this Citizen that triggers the cross-reference
- `target_citizen:` — the Citizen that owns the referenced standard
- `target_standard:` — path to canonical standard file
- `relationship:` — incorporates | parallel_authority | procedural_bridge | preempts | conditional
- `triggering_cases:` — Vernen case numbers where this junction fires
- `doctrinal_note:` — one paragraph on how the cross-referenced rule operates inside Family Law

**Read-only rule.** T4 does not edit standards owned by other Citizens. If a target standard needs correction, file an issue in the owning Citizen's folder via that Citizen's steward.

## Index

| Junction | Family Law Anchor | Target Citizen | Target Standard |
|---|---|---|---|
| [fl_to_criminal_pen_1368_competency](./fl_to_criminal_pen_1368_competency.md) | § 3118 DV custody eval / MC-350 | CA_Mental_Health_Litigator | `pen_1368_competency_doubt` |
| [fl_to_mh_wic_5150_hold](./fl_to_mh_wic_5150_hold.md) | § 3020 best interest (parent hospitalized) | CA_Mental_Health_Litigator | `wic_5150_involuntary_hold` |
| [fl_to_probate_wic_5350_lps](./fl_to_probate_wic_5350_lps.md) | § 3020 / § 3011 (conservatee parent) | CA_Probate_Conservatorship_Litigator | `wic_5350_lps_conservatorship` |
| [fl_to_probate_prob_1800_minor](./fl_to_probate_prob_1800_minor.md) | § 3011 / § 3041 (nonparent custody) | CA_Probate_Conservatorship_Litigator | `prob_1800_3_minor_conservatee` |
| [fl_to_criminal_pen_273a_child_endanger](./fl_to_criminal_pen_273a_child_endanger.md) | § 3011 / § 3044 DV presumption | CA_Criminal_Law_Specialist | `cal_pen_273a` (scaffold) |
| [fl_to_criminal_pen_278_5_deprivation](./fl_to_criminal_pen_278_5_deprivation.md) | § 3048 custody order enforcement | CA_Criminal_Law_Specialist | `cal_pen_278_5` (scaffold) |
| [fl_to_criminal_pen_166_contempt](./fl_to_criminal_pen_166_contempt.md) | § 6320 DVRO violation | CA_Criminal_Law_Specialist | `cal_pen_166` (scaffold) |
| [fl_to_vc_marsys_law](./fl_to_vc_marsys_law.md) | § 6320 DVPA / victim notice | CA_Victim_Compensation_Litigator | `cal_const_art1_28_marsys_law` |
| [fl_to_vc_gov_13955_eligibility](./fl_to_vc_gov_13955_eligibility.md) | § 6203 DV victim status | CA_Victim_Compensation_Litigator | `cal_gov_13955_eligibility` |
| [fl_to_mh_evid_1016_privilege](./fl_to_mh_evid_1016_privilege.md) | § 3118 DV eval record disclosure | CA_Mental_Health_Litigator | `evid_1016_psychotherapist_privilege` |

### Pass 2 — EVE / T2 (2026-04-14)

| Junction | Family Law Anchor | Target Citizen | Target Standard | Relationship |
|---|---|---|---|---|
| [fl_to_criminal_pen_148_5_false_report](./fl_to_criminal_pen_148_5_false_report.md) | § 3027 / § 3027.1 false-allegation sanctions | CA_Criminal_Law_Specialist | `cal_pen_148_5` | predicate |
| [fl_to_criminal_pen_273_6_dvro_violation](./fl_to_criminal_pen_273_6_dvro_violation.md) | § 6320 / § 6321 / § 6323 / § 6345 DVRO | CA_Criminal_Law_Specialist | `cal_pen_273_6` | criminal_enforcement_of_civil_order |
| [fl_to_criminal_pen_273_5_corporal_injury](./fl_to_criminal_pen_273_5_corporal_injury.md) | § 3044 DV presumption | CA_Criminal_Law_Specialist | `cal_pen_273_5` | predicate_for_dv_presumption |
| [fl_to_criminal_pen_422_criminal_threats](./fl_to_criminal_pen_422_criminal_threats.md) | § 3044 / § 6203(a)(3) / § 6320(a) threats | CA_Criminal_Law_Specialist | `cal_pen_422` | parallel_authority |
| [fl_to_mh_evid_730_court_appointed_expert](./fl_to_mh_evid_730_court_appointed_expert.md) | § 3118 / Evid. § 730 eval vs LPS safeguards | CA_Mental_Health_Litigator | `pen_1368` + `wic_5150` + `wic_5350` | procedural_bridge |
| [fl_to_vc_fam_3027_1_child_sex_abuse_allegation](./fl_to_vc_fam_3027_1_child_sex_abuse_allegation.md) | § 3027.1 false-allegation finding | CA_Victim_Compensation_Litigator | `cal_gov_13955_eligibility` | eligibility_conditional |
| [fl_to_vc_gov_13956_denial_criteria](./fl_to_vc_gov_13956_denial_criteria.md) | § 6320 / § 6203 DVRO record → CalVCB denial analysis | CA_Victim_Compensation_Litigator | `cal_gov_13956_denial_criteria` | evidentiary_bridge |
| [fl_to_elder_wic_15610_07_abuse_definition](./fl_to_elder_wic_15610_07_abuse_definition.md) | § 3044 / § 6203 / § 6211 ↔ Elder abuse | CA_Elder_Law_Litigator | `wic_15610_30_financial_abuse` + `wic_15657_penalties` | parallel_authority |
