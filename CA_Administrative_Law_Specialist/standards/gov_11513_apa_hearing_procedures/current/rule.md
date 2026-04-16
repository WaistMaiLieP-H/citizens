# GOV § 11513 APA Hearing Procedures — Operative Rule

**Standard ID:** gov_11513_apa_hearing_procedures
**Citizen:** CA_Administrative_Law_Specialist
**Layer:** 2 — Operative Rule
**Build date:** 2026-04-13

---

## The Rule

California APA hearings follow GOV §11513's evidentiary framework: relaxed admissibility (responsible persons standard), full cross-examination beyond the scope of direct, hearsay admitted but not sufficient alone for a finding unless civilly admissible, oath required for oral evidence, statutory privileges preserved.

---

## The Six Rules Analyzed

### (a) Oath Requirement
All oral testimony is sworn. Unsworn statements are not testimony and cannot be the basis for a finding. This is the foundation of the APA hearing's evidentiary integrity. An ALJ who accepts unsworn statements as findings-worthy evidence violates §11513(a).

### (b) Cross-Examination Rights — The Key APA Procedural Protection
§11513(b) grants cross-examination on **any matter relevant to the issues**, even if not covered on direct. This is explicitly broader than the civil trial default (where cross-examination is typically limited to the scope of direct). The party's right to cross-examine is:
- Mandatory: the presiding officer cannot deny it for convenience
- Scope: any relevant matter, regardless of whether raised on direct
- Includes: right to impeach any witness regardless of who called them

**Attack ground:** An agency decision based on evidence the respondent was not permitted to cross-examine is a fair trial violation under CCP §1094.5(b)(2). This is not a technical objection — it is the deprivation of the core due process protection the APA provides.

### (c) Relaxed Admissibility — The "Responsible Persons" Standard
The APA does not apply civil evidence rules as a default. Evidence is admitted if it is "the sort of evidence on which responsible persons are accustomed to rely in the conduct of serious affairs." This is permissive — the APA opens the door wider than civil courts. However:
- The relaxed standard runs **only in the direction of admission** — it makes more evidence admissible
- It does not override the oath requirement (§11513(a)), the hearsay limitation (§11513(d)), or statutory privileges (§11513(e))
- The ALJ still has §11513(f) discretion to exclude for undue time consumption

### (d) The Hearsay Limitation — Critical for CalVCB
§11513(d) is the most operationally important provision for cases where police reports or official records are the primary evidence:

**Hearsay IS admissible** in APA hearings — but only to "supplement or explain" other evidence.

**Hearsay CANNOT be the sole basis for a finding** unless it would be admissible over objection in a civil action (i.e., a recognized hearsay exception applies).

**Timely objection:** Must be made before submission or on reconsideration.

**Application to CalVCB:**
CalVCB's single-source denial based on the police report alone violates §11513(d) if:
- The police report was the *sole* evidence supporting the denial finding
- The police report constitutes hearsay (it does — out-of-court statements offered for truth)
- No recognized civil hearsay exception independently qualifies the police report (business records under EVID §1271 requires foundation; official records under §1280 requires showing; neither automatically applies without foundation)

A finding based solely on a police report, over timely objection, is not supported by sufficient evidence under §11513(d). This directly supports the §1094.5(b) findings-not-supported-by-evidence ground.

### (e) Privilege
Statutory privileges apply. This means attorney-client communications, physician-patient privilege (EVID §994), and psychotherapist-patient privilege (EVID §1014) are effective in APA hearings if recognized by statute. A party can refuse to disclose privileged communications at an OAH hearing.

### (f) Efficiency Exclusion
The ALJ has discretion to exclude evidence if probative value is substantially outweighed by undue time consumption. Note: this is a narrower test than the civil unfair prejudice balancing. The APA excludes only for *time* — not for unfair prejudice, confusion, or cumulative nature in the civil sense.

---

## Application to Active Cases

### CalVCB Appeal — A25-10117946

**§11513(d) single-source attack:**
- If CalVCB's denial findings are based solely on the police report (single-source denial per audit findings)
- And the police report is hearsay
- And no recognized civil hearsay exception independently qualifies it
- Then: the denial finding is not supported by evidence sufficient under §11513(d)
- This maps to: §1094.5(b) findings not supported by evidence → abuse of discretion → writ issues

**§11513(b) cross-examination attack:**
- If the applicant was not given the opportunity to cross-examine the evidence sources CalVCB relied upon (e.g., the officer who wrote the police report, the CDI investigator if any)
- Fair trial violation under §1094.5(b)(2)

**§11513(a) oath attack:**
- If CalVCB accepted unsworn statements from third parties as evidence supporting denial
- §11513(a) violation → evidence inadmissible → finding unsupported

### OAH Proceedings — PC §1368 Evaluation

If Dr. Wiita testified in any OAH proceeding related to the §1368 evaluation:
- Was she sworn (§11513(a))? 
- Was the respondent given full cross-examination (§11513(b)) on all relevant matters — including her failure to use MC-350?
- Were any hearsay reports (prior evaluations, secondary descriptions) used as sole basis for findings without civil admissibility (§11513(d))?

---

## Hearsay Attack Flowchart — APA Proceedings

```
Evidence offered at APA hearing
↓
Is it hearsay? (out-of-court statement offered for truth)
  → NO: admissible under §11513(c) responsible persons standard
  → YES:
      Was timely objection made?
        → NO: objection waived; hearsay considered
        → YES:
            Is it supplementing/explaining other evidence?
              → YES: admitted (§11513(d) — supplementary role)
              → NO (sole basis for finding):
                  Is it civilly admissible over objection?
                    → YES: admissible (recognized exception — business records, official records, etc.)
                    → NO: NOT sufficient to support finding → §1094.5(b) attack available
```
