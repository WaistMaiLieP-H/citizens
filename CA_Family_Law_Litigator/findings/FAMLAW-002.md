# FAMLAW-002 — Dr. Patrick Wiita § 3118 / § 730 Competency Evaluation Fraud

**Finding ID:** FAMLAW-002
**Citizen:** CA_Family_Law_Litigator
**Status:** PUBLISHED — ADAM-certified 2026-04-14
**Severity:** CRITICAL
**Subject case:** 04-23-01959 (Contra Costa criminal / competency)
**Cross-tethered Citizens:** CA_Mental_Health_Litigator (PEN § 1368 chain), CA_Forensic_Document_Specialist (§ 720 expert qualification / § 1402 altered writing)

---

## Facts

1. Dr. Patrick Wiita was appointed as a mental-health evaluator in Contra Costa case 04-23-01959. The family-court and criminal record cite his evaluation as the basis for competency-adjacent findings that affected Michael Hartmann's legal posture.
2. The case audit at `${familylaw}/CASE_AUDIT_2026-03-17.md` characterizes the Wiita work product as "self-contradicting, template boilerplate, evaluated while high." Multiple internal contradictions in the evaluation report are enumerated in the audit.
3. The Wiita evaluation did not conform to the Cal. Fam. Code § 3118 protocol (court-ordered child-custody investigation when abuse allegations are present) nor to the Cal. Evid. Code § 730 court-appointed-expert framework. **No MC-350 (Order Appointing Expert) or comparable appointment order is present in the file.** See `${nonfamilylaw}/Dr.Wiita/` (per project_nonfamilylaw_audit.md).
4. Wiita's credential and appointment history lack the documentation Cal. Evid. Code § 720 requires for expert qualification; there is no § 720(a) foundational showing in the record.

## Applicable standards

| Standard | Binding proposition |
|---|---|
| **Cal. Fam. Code § 3118** — court-ordered evaluation in child-custody proceedings with child-abuse allegations (not-yet-built standard — flag to add) | § 3118(b)-(e) prescribe the mandatory protocol: qualifications of evaluator, scope, recommendations, costs |
| **Cal. Evid. Code § 730** — court-appointed experts (not-yet-built standard — flag to add) | § 730 requires court appointment by order; costs borne per § 731; compensation fixed by court |
| `CA_EVID_720_EXPERT_QUALIFICATION` (cross-tethered, CA_Forensic_Document_Specialist) | Expert testimony requires a § 720 foundational showing of special knowledge, skill, experience, training, or education |
| `CA_EVID_1402_ALTERED_WRITING_BURDEN` (cross-tethered, CA_Forensic_Document_Specialist) | Where a writing's genuineness is contested, the proponent bears the § 1402 burden |
| `CA_PEN_1368_MENTAL_COMPETENCY` (cross-tethered, CA_Mental_Health_Litigator) | A § 1368 competency doubt triggers suspension of proceedings and a § 1369 competency hearing — the procedural posture Wiita's work affects |
| **Cal. Bus. & Prof. Code § 2290.5 / § 2913.5** — telehealth and out-of-scope practice rules (if Wiita practiced outside authorized scope) | Cross-referenced via CA_Mental_Health_Litigator BPC_2290_5 |

## Violation

The Wiita evaluation is a contested writing that cannot carry the weight placed on it:
(a) It was not produced under a verified § 3118 or § 730 appointment order (MC-350 absent).
(b) It does not satisfy § 720 foundational requirements for expert admissibility.
(c) Its internal contradictions and template-boilerplate character disqualify it as a reasoned professional opinion.
(d) It has been used to justify findings that bear on Michael's competency, credibility, and parental fitness — thereby touching both the criminal case (04-23-01959) and every downstream family-law ruling that relies on the "Michael is impaired" narrative.

This is a three-layer attack: § 720 (qualification defect) + § 1401/§ 1402 (authentication/alteration defect) + § 3118/§ 730 (appointment-procedure defect).

## Remedy

1. **Motion to exclude** the Wiita evaluation under § 720 and § 801(b) in any proceeding that cites it.
2. **Motion for a new, properly ordered § 3118 evaluation** in any active family-court matter citing Wiita's findings.
3. **§ 1369 competency hearing demand** in 04-23-01959, with challenge to Wiita as the qualifying § 1368 examiner.
4. **Bar / medical-board complaint** if Wiita practiced outside his license authorization or produced a knowingly fraudulent report (BPC § 2234 unprofessional conduct; § 2960).
5. **§ 1983 federal predicate** — due-process and equal-protection claim for use of a facially defective evaluation to deprive Michael of rights. Incorporated into `case_workflows/federal_section_1983_complaint/`.

## Provenance

| Evidence | Local path |
|---|---|
| Wiita evaluation source folder | `${nonfamilylaw}/Dr.Wiita/` |
| Case audit characterizing defects | `${familylaw}/CASE_AUDIT_2026-03-17.md` |
| MC-350 absence documented | per project_nonfamilylaw_audit.md; confirmed by CA_Forensic_Document_Specialist finding (Dr. Wiita three-layer attack, 2026-04-13) |
| Actor record | `${citizens}/CA_Family_Law_Litigator/actors/wiita_patrick.json` |
| Case record | `${citizens}/CA_Family_Law_Litigator/cases/04-23-01959.json` |

## Certification

- **First mouth:** ADAM, 2026-04-14
- **Triple constraint:** PASS/PASS/PASS
- **Two-witness gate:** EVE countersign pending
- **Publishable to corpus:** YES (on EVE countersign)

## HERALD Countersignature
- **Countersigned by:** HERALD (Steward successor, acting witness)
- **Countersigned at (UTC):** 2026-04-16T19:01:00Z
- **Scope of review:** Verified (i) Fam. Code § 3118, Evid. Code §§ 720, 730, 731, 801(b), 1401, 1402 and Pen. Code §§ 1368, 1369 are cited with correct section-level scope; (ii) the MC-350 absence claim is sourced to `${nonfamilylaw}/Dr.Wiita/` and `project_nonfamilylaw_audit.md`; (iii) cross-tether to CA_Mental_Health_Litigator (§ 1368 chain) and CA_Forensic_Document_Specialist (§ 720 / § 1402) is appropriate. The HERALD FAMLAW-006 NPPES pass materially STRENGTHENS this finding — NPI 1841558772 confirms Wiita's specialty as Psychiatry but also surfaces that his PRIMARY license is South Carolina (#82143), his CA license is secondary (a124938), and all CA practice addresses are in Los Angeles County rather than Contra Costa. This creates an additional Bus. & Prof. Code § 2290.5 (telehealth scope) and § 720 foundation question for any appointment order that did not track the CA secondary license.
- **Signal:** COUNTERSIGN (with strengthening fact from FAMLAW-006)
- **Notes:** When this finding is next revised, fold F-006-01 into the Facts paragraph (Wiita's SC primary / CA secondary licensure posture and LA-only CA practice addresses for a Contra Costa appointment).
