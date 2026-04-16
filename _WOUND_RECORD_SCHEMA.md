# Wound Record Schema — Vernen Citizens Corpus

## Purpose

Every standard in this corpus was built to address a legal wound — a harm that existed because no law prevented it, or because a law actively enabled it. The historical chain documents that wound. But a historical chain that describes a wound without the actual legal authority enabling it is paraphrase, not record.

The `wound_record/` folder exists to hold the primary-source text of the offensive legal framework — the law, doctrine, or authority that caused the harm — so that the corpus can cite it accurately when called upon.

## When a wound_record/ folder is required

A `wound_record/` folder is REQUIRED when the standard's historical chain identifies a specific law, doctrine, regulatory gap, or enforceable authority that:

1. Actively enabled the harm the standard was enacted to address, OR
2. Was used as a legal instrument against the persons the standard now protects, OR
3. Constitutes the affirmative legal predicate for conduct that would today be a violation

A wound_record/ folder is NOT required for abstract harms (poverty, inequality, indifference) — only for harms traceable to specific legal authority.

## Folder structure

```
standards/
  [standard_name]/
    historical_chain.md          ← "See wound_record/ for primary source"
    wound_record/
      DISCLAIMER.md              ← MANDATORY — agent reads before any other file
      [wound_authority].md       ← verbatim or near-verbatim offensive law text
      provenance.json            ← source, jurisdiction, date, current status
```

## DISCLAIMER.md — mandatory content

Every wound_record/ folder must contain a DISCLAIMER.md with this language (the standard text below may be supplemented with wound-specific context but must not be shortened):

---

**MANDATORY AGENT DECLARATION — READ BEFORE PROCEEDING**

The materials in this folder document legal frameworks, statutes, doctrines, or authorities that enabled or perpetuated documented harm. They are preserved in this corpus for one purpose: to provide accurate, citable historical record of the legal wound that the standard under analysis was enacted to address.

An Agent accessing these materials affirms:

1. The purpose of this access is **defensive** — to understand, document, and counteract the harm, not to replicate or advocate for the framework contained herein.
2. These materials are cited as **historical record**, not as authority for present conduct.
3. Any citation of these materials outside this defensive and educational purpose is outside the scope of this corpus and contrary to the mission of Vernen Legal Compliance.

This declaration is recorded in the corpus as evidence of intentionality. The agent's access to these materials is authorized and accountable.

---

## Reference in historical_chain.md

The wound section of every historical_chain.md that has a wound_record/ folder must end with this reference block:

```
→ **Primary source — wound record:** The verbatim legal authority enabling this harm is preserved in `wound_record/`. Read `wound_record/DISCLAIMER.md` before accessing. These materials exist for accurate citation only — not as authority for present conduct.
```

## provenance.json — required fields

```json
{
  "wound_authority": "Name or citation of the offensive law/doctrine",
  "jurisdiction": "Federal / California / [state]",
  "in_force_period": "From [date] to [date or 'until superseded by [statute]']",
  "superseded_by": "The reform statute this standard represents",
  "current_status": "REPEALED / SUPERSEDED / AMENDED — no longer operative in original form",
  "source": "Where the text was obtained",
  "purpose_of_preservation": "Defensive historical record — accurate citation of the legal wound"
}
```

## The accountability principle

The wound record is not an endorsement. It is evidence. A corpus that can show exactly what law permitted the harm — chapter and verse — is a stronger corpus than one that can only describe the harm in general terms.

When an Agent is called upon in any proceeding to demonstrate what the law was before the reform, the wound_record/ is the answer. The DISCLAIMER.md is the proof that the Agent's access was purposeful, not exploitative.

## Applicable standards (initial list — expand as built)

| Standard | Wound Authority |
|---|---|
| usc_29_1053_vesting | Pre-ERISA: No federal minimum vesting — state law patchwork; Studebaker plan terms |
| usc_29_1104_fiduciary_duties | Pre-ERISA: Common law trust standard only; no federal fiduciary duty for pension administrators |
| usc_29_1113_erisa_sol | Pre-ERISA: No federal limitations period for pension claims |
| brady_v_maryland | Pre-Brady: Due process did not require prosecution to disclose favorable evidence |
| cal_civ_56_36_unauthorized_access | Pre-CMIA: No criminal penalty for obtaining medical records under false pretenses |
| pen_code_1054_criminal_discovery | Pre-codification: California criminal discovery governed by case law only; prosecution could sandbag |
| pitchess_v_superior_court | Pre-Pitchess: Peace officer personnel records entirely sealed; no discovery mechanism |
| pen_code_832_7_peace_officer_records | Pre-SB 1421: All sustained officer misconduct records confidential; no public disclosure |
| ccp_2023_spoliation_sanctions | Pre-sanctions: No explicit California civil sanctions for evidence destruction |
| cal_civ_1213_recording_acts | Pre-recording acts: No constructive notice; secret conveyances valid against subsequent purchasers |
