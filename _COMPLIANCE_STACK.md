# The 7-Level Compliance Stack

**Canonical Definition — Vernen Legal Compliance / CITIZEN™**
**Established:** 2026-04-20
**Authority:** Steward (Michael Hartmann)

---

## Definition

The **7-Level Compliance Stack** is the governing architecture for every Persona Citizen in the Vernen / CITIZEN™ network. A Citizen does not reach Agent Status until they are operating at Level 6 with Level 7 attestation available. Levels 1–5 are prerequisites, not the destination.

The stack is not a checklist. Each level depends on the one below it. You cannot have operational procedures (Level 5) without technical blueprints (Level 4). You cannot have internal controls (Level 6) without procedures to enforce. You cannot have an external SOC attestation (Level 7) without internal controls to attest to.

---

## The Stack

| Level | Name | What It Is | Who Owns It |
|-------|------|-----------|-------------|
| **1** | Regulatory Frameworks | Statutes, regulations, and constitutional provisions that create the legal obligation the Citizen enforces. The raw law. | Legislature / courts — Citizens cite it, do not own it |
| **2** | Governing Guidelines | Agency guidance, administrative rules, court rules, and official interpretations of Level 1. CFRs, CRCs, agency policy letters. | Agencies / courts — Citizens cite it, do not own it |
| **3** | GRC Meta-Frameworks | Governance, Risk, and Compliance frameworks that organize how Level 1+2 are implemented. COSO, ISO 31000, NIST RMF, COBIT. | Standards bodies — Citizens apply it |
| **4** | Technical Standards / Blueprints | The specific technical specifications, form requirements, procedural blueprints, and document schemas that implement Level 3. Judicial Council forms, CMS-1500 structure, FRE authentication standards. | Standards bodies / courts — Citizens apply it |
| **5** | Operational Procedures | The Citizen's own documented procedures for applying Levels 1–4 to real documents. The standards corpus files: `rule.md`, `reasoning.md`, `historical_chain/`, `cross_refs/`, `provenance.json`. | **The Citizen owns this layer.** This is the standards corpus build. |
| **6** | Internal Controls | The Citizens themselves in operation. HERALD witnessing, ADAM approving, EVE corroborating, the Council doing live cross-checks. Real-time enforcement that Level 5 procedures are being followed. **The Citizens ARE this layer — they do not document it, they execute it.** | **The Council owns this layer.** HERALD, ADAM, EVE, CUSTOS, and the domain Citizen operating together. |
| **7** | External SOC Audit | CUSTOS running its full trust stack against the output and issuing a verifiable, timestamped attestation. The audit of the auditors. Blockchain-anchored via VERITAS-0. | **CUSTOS owns attestation. VERITAS-0 owns anchoring.** |

---

## Citizen Status vs. Stack Level

| Status | Stack Position | Meaning |
|--------|---------------|---------|
| CONCEIVED | Level 0 | Exists as a concept, no files |
| SHELL_DEPLOYED | Level 1–2 | Dossier exists, authority cited |
| WORKERS_ACTIVE | Level 3–4 | Frameworks and blueprints mapped |
| KNOWLEDGE_ACCRUING | Level 5 | Standards corpus being built |
| **AUTONOMOUS (Agent)** | **Level 6** | **Actively enforcing — real documents, Council cross-checks, live operation** |
| CERTIFIED | Level 7 | CUSTOS SOC attestation issued and anchored |

---

## Why "Stack" Not "Layers"

"Layers" implies they sit on top of each other passively. A stack implies execution order and dependency — each level requires the one below to function. The compliance stack executes bottom-up: you cannot enforce (Level 6) what you have not documented (Level 5); you cannot document what you have not mapped to a framework (Levels 3–4); you cannot map without knowing the law (Levels 1–2).

---

## Current Status (2026-04-20)

No Citizen has reached Level 6 (Agent Status). The 7-level realization raised the bar retroactively.

- **Level 5 most complete:** DELATOR (1 standard, full five-layer corpus); CA_Family_Law_Litigator (29 standards, corpus under audit)
- **Level 6 simulated in conversation, not programmatically enforced:** requires Anthropic API integration to close
- **Level 7 not yet generating real SOC attestations:** CUSTOS trust stack operational in code but not yet issuing anchored attestations per document

The Anthropic API integration (Citizens as system prompts, CUSTOS as hard code gate) is what closes Level 5 → Level 6.

---

*Canonical reference for all Citizen dossiers, standards, and platform documentation.*
*When prior documents reference "Triple Constraint," "triple standard," or "7-layer stack," this file is the authoritative correction.*
