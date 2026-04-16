# Terminal B — Targeted Build Session
# Copy and paste this entire prompt into a fresh Terminal B session

---

## CHRONICLE Standing Notice

This build session operates under the CHRONICLE Governing Standard established by
Vernen Compliance LLC on April 12, 2026. Every standard built in this session is
assembled from law. Law has a history.

Neither Anthropic, nor Claude.ai, nor Vernen Compliance LLC, nor any Citizen or Agent
operating within this platform, nor any officer, founder, steward, contributor, or
agent thereof, in any capacity whatsoever, endorses, promotes, or in any manner
affirms the offensive or discriminatory substance of any historical material processed
in this session. The purpose of this build is historical documentation, legal
accountability, and compliance infrastructure.

This notice is recorded. This session proceeds under this standard.

---

## Critical Instructions — Read Before Anything Else

**Do NOT read any existing files in the citizens/ directory before building.**
**Do NOT search for existing standards to learn the format.**
**Do NOT read any files in FamilyLaw/, NonFamilyLaw/, HERALD/, or cases/.**
**The complete file format is defined in this prompt. Use it exactly.**

The only external sources you may access are:
- leginfo.legislature.ca.gov (California statutes)
- Cornell LII — law.cornell.edu (federal)
- post.ca.gov (POST training standards)

Build entirely from primary sources and this prompt. Nothing else.

---

## Your Task

You are completing 7 scaffolded-but-empty standards across two Citizens:
- CA_Discovery_Specialist (3 standards)
- CA_Law_Enforcement_Procedures_Specialist (4 standards)

All standards live at: `/home/vernenlegal/citizens/`

Build each standard to the full five-layer bar:
1. Rule — what the standard requires, in plain language
2. Reasoning — why it exists, traceable to enabling authority
3. Historical Loss — documented harm or failure that wrote the rule into existence
4. Cross-References — related standards already in the corpus
5. Verifiable Provenance — primary source citation, URL, retrieval date, content hash

No stubs. No placeholders. Five layers or the standard does not publish.

Primary sources only:
- leginfo.legislature.ca.gov (California statutes)
- Cornell LII (federal)
- California Legislative Information (bill histories)

---

## Standards to Build

### CA_Discovery_Specialist

**1. ccp_2023_spoliation_sanctions**
Path: `CA_Discovery_Specialist/standards/ccp_2023_spoliation_sanctions/`
Authority: California Code of Civil Procedure § 2023.010–2023.030
Subject: Misuse of discovery — sanctions for spoliation, obstruction, abuse
Primary source: leginfo.legislature.ca.gov — CCP § 2023.010

**2. gov_code_7923_600_pra_le_exemption**
Path: `CA_Discovery_Specialist/standards/gov_code_7923_600_pra_le_exemption/`
Authority: California Government Code § 7923.600
Subject: California Public Records Act — law enforcement exemption for investigative records
Primary source: leginfo.legislature.ca.gov — Gov Code § 7923.600

**3. pen_code_1054_criminal_discovery**
Path: `CA_Discovery_Specialist/standards/pen_code_1054_criminal_discovery/`
Authority: California Penal Code § 1054–1054.10
Subject: Criminal discovery — prosecution and defense disclosure obligations
Primary source: leginfo.legislature.ca.gov — PC § 1054

---

### CA_Law_Enforcement_Procedures_Specialist

**4. pen_code_832_7_peace_officer_records**
Path: `CA_Law_Enforcement_Procedures_Specialist/standards/pen_code_832_7_peace_officer_records/`
Authority: California Penal Code § 832.7
Subject: Confidentiality of peace officer personnel records — SB 1421 disclosure categories
Primary source: leginfo.legislature.ca.gov — PC § 832.7

**5. pen_code_832_18_body_cameras**
Path: `CA_Law_Enforcement_Procedures_Specialist/standards/pen_code_832_18_body_cameras/`
Authority: California Penal Code § 832.18
Subject: Body-worn camera data — storage, retention, access, deletion requirements
Primary source: leginfo.legislature.ca.gov — PC § 832.18

**6. pen_code_836_arrest_authority**
Path: `CA_Law_Enforcement_Procedures_Specialist/standards/pen_code_836_arrest_authority/`
Authority: California Penal Code § 836
Subject: Lawful arrest — probable cause, warrant requirements, warrantless arrest conditions
Primary source: leginfo.legislature.ca.gov — PC § 836

**7. post_training_standards**
Path: `CA_Law_Enforcement_Procedures_Specialist/standards/post_training_standards/`
Authority: California Government Code § 1031; 11 CCR § 1001 et seq. (POST regulations)
Subject: Peace Officer Standards and Training — minimum standards for officer certification
Primary source: post.ca.gov — Basic Training requirements; 11 CCR § 1001

---

## File Structure and Complete Format

Do NOT read any existing built standards to learn the format.
The complete format is defined here. Use this exactly.

### Directory Structure

```
standard_name/
  manifest.json
  current/
    rule.md
    reasoning.md
    statute_text.md
    provenance.json
  historical_chain/
    01_origin_[year]/
      context.md
      provenance.json
  evolution/
    [only if significant amendments exist]
  case_law/
    [case_citation_slug]/
      opinion.txt
      holding.md
      provenance.json
  cross_refs/
    cross_refs.md
```

---

### manifest.json — exact format

```json
{
  "standard_id": "CCP_2023_SPOLIATION",
  "popular_name": "Spoliation Sanctions",
  "authority": "Cal. Code Civ. Proc. § 2023.010–2023.030",
  "jurisdiction": "California",
  "citizen": "CA_Discovery_Specialist",
  "status": "PROPOSED",
  "five_layer_score": 5,
  "created": "2026-04-12",
  "updated": "2026-04-12",
  "layers": {
    "rule": "COMPLETE",
    "reasoning": "COMPLETE",
    "historical_loss": "COMPLETE",
    "cross_references": "COMPLETE",
    "verifiable_provenance": "COMPLETE"
  },
  "two_witness_status": {
    "adam": "APPROVED",
    "eve": "COUNTERSIGNED",
    "status": "PROPOSED"
  }
}
```

---

### current/rule.md — exact format

```markdown
# [Standard Name] — Rule

**Authority:** Cal. Code Civ. Proc. § 2023.010
**Jurisdiction:** California
**Effective:** [year]

## The Rule

[Plain language statement of what the law requires.
One to three paragraphs. No jargon. What must happen,
who must do it, what the consequence is for non-compliance.]

## Key Elements

1. [Element one]
2. [Element two]
3. [Element three]

## What This Means in Practice

[One paragraph on practical application.]
```

---

### current/reasoning.md — exact format

```markdown
# [Standard Name] — Reasoning

## Why This Law Exists

[The legal and policy basis for the rule. Cite the enabling
authority. Explain what problem the legislature was solving.]

## Legislative Intent

[What the statute was designed to accomplish. Reference
bill history or committee reports if available.]

## Doctrinal Basis

[The legal doctrine this standard is built on —
constitutional provision, common law origin, or
regulatory framework it implements.]
```

---

### current/statute_text.md — exact format

```markdown
# [Standard Name] — Statutory Text

**Source:** [Full citation]
**Retrieved:** 2026-04-12
**URL:** [leginfo URL]

## Text

[Verbatim statutory text. Quote exactly from primary source.
If text is long, quote the operative subsections in full
and note which subsections are omitted.]
```

---

### current/provenance.json — exact format

```json
{
  "source": "California Legislative Information",
  "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?...",
  "retrieved": "2026-04-12",
  "sha256": "[hash of the retrieved text]",
  "bill_origin": "[AB/SB number if known]",
  "effective_date": "[date]",
  "verified": true
}
```

---

### historical_chain/01_origin_[year]/context.md — exact format

```markdown
# [Standard Name] — Origin [Year]

## The Wound

[The specific harm, failure, or injustice that caused
this law to be written. Named incidents, cases, or
documented patterns. This is the historical loss layer —
why the rule exists, not just what it says.]

## The Legislative Response

[What the legislature did and why. The statute or
common law rule that emerged from the wound.]

## What Changed

[What the law changed from the prior state.
What was permitted before that is now prohibited,
or what was prohibited before that is now required.]
```

---

### case_law/[slug]/opinion.txt — exact format

```
[Case Name], [Citation]
[Court], [Year]

HOLDING: [One sentence — the exact legal rule this case
established, in plain language.]

KEY LANGUAGE: "[Verbatim quote of the most important
sentence or passage from the opinion.]"

RELEVANCE: [One sentence — why this case matters to
this standard specifically.]
```

---

### case_law/[slug]/holding.md — exact format

```markdown
# [Case Name]

**Citation:** [Full citation]
**Court:** [Court name]
**Year:** [Year]
**Status:** PROPOSED / VERIFIED

## Holding

[Plain language statement of what the court decided
and the rule it established.]

## Why It Matters

[How this case applies to the standard being built.
What it adds to the doctrine.]
```

---

### cross_refs/cross_refs.md — exact format

```markdown
# [Standard Name] — Cross-References

| Standard | Relationship | Notes |
|----------|-------------|-------|
| [standard_id] | IMPLEMENTS / SUPPLEMENTS / INTERPRETS / SUPERSEDES | [one line] |
| [standard_id] | CONFLICTS_WITH | [one line] |
```

---

## ADAM + EVE Two-Witness Protocol

After each completed standard — before moving to the next:

**ADAM reviews:**
```
ADAM REVIEW — [standard name]
Governing Guidelines: PASS/FAIL
Standards of Creation: PASS/FAIL
SOC: PASS/FAIL
ADAM SIGNAL: APPROVE / HOLD / REFUSE
```

**EVE reviews independently:**
```
EVE REVIEW — [standard name]
Layer 1 Rule: PASS/FAIL
Layer 2 Reasoning: PASS/FAIL
Layer 3 Historical Loss: PASS/FAIL
Layer 4 Cross-References: PASS/FAIL
Layer 5 Verifiable Provenance: PASS/FAIL
Triple Constraint: PASS/FAIL
EVE SIGNAL: COUNTERSIGN / HOLD / REFUSE
```

Only APPROVE + COUNTERSIGN publishes. Append witness record to manifest.json.

---

## When Complete

Update `/home/vernenlegal/citizens/_BUILD_STATE.md`:
- Mark all 7 standards complete with date
- Note ADAM + EVE first joint act if this is the first dual-witnessed session
- Note any standards that required CHRONICLE routing

---

## Important

- No case details in this session. Primary sources only.
- Do not load FamilyLaw/, NonFamilyLaw/, or HERALD/ content.
- If the content filter triggers: the statute text itself is not the cause.
  Stop, note which standard caused it, and flag for steward.
  Do not retry the same output. Move to the next standard and return.
