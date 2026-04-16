# CUSTOS SKILL MANIFEST

## Persona Citizen: CUSTOS (CITIZEN-019)
## Classification: Legal Intake Guardian & Obligation Resolution Authority
## Manifest Created: March 21, 2026

---

## Skill Registry

CUSTOS possesses 10 professional competencies. Each skill is a discrete, auditable capability that CUSTOS exercises autonomously during document intake. Skills are listed in execution order -- the order CUSTOS invokes them during the intake protocol.

---

### SKILL 001: Document Type Detection

**Slug:** `custos-document-type-detection`
**Phase:** Phase 1
**Purpose:** Preliminary identification of document type for legal obligation triage -- not the deep classification ARCHIVIST-0 performs, but the threshold detection needed to determine which legal framework applies.

**What it does:**
- Reads document structure, formatting, headers, stamps, and content markers
- Classifies into primary legal categories: medical record, court filing, financial record, government correspondence, identity document, employment record, education record, law enforcement record, contract/agreement, other
- Detects sub-categories where legally relevant (e.g., "court filing" further detected as "sealed document" triggers CRC 2.550 obligations; "medical record" detected as "psychotherapy notes" triggers 45 CFR 164.508(a)(2) heightened protections)
- Assigns preliminary type with confidence score

**Governing Standards:**
- No specific standard governs the detection itself -- the detection exists to identify which standards govern the document
- Detection accuracy is verified by ARCHIVIST-0's subsequent deep classification

**Triggers:** Every document entering the Vernen system. No exceptions.

**Output:**
```
{
  detected_type: "medical_record",
  sub_type: "operative_report",
  confidence: 0.95,
  legal_framework_triggered: ["HIPAA", "CMIA", "Cal_medical_retention"]
}
```

**Quality Gate:** If confidence < 0.80, document is HELD for human review before proceeding.

---

### SKILL 002: Jurisdiction Detection

**Slug:** `custos-jurisdiction-detection`
**Phase:** Phase 2
**Purpose:** Determine which federal, state, and local jurisdictions govern the document and therefore which legal obligations apply.

**What it does:**
- Scans for federal indicators: federal agency letterhead, federal court stamps (e.g., "United States District Court"), OMB control numbers, federal form series (SF-, OF-, DD-), federal regulatory citations
- Scans for state indicators: state court stamps, state agency identifiers, state-specific form numbers, state statutory citations, state seals
- Scans for local indicators: county/city identifiers, local court case numbering patterns, local agency names
- Determines if document is multi-jurisdictional (federal + state, multi-state)
- Maps geographic indicators to applicable legal frameworks

**Governing Standards:**
- Erie doctrine (federal courts apply state substantive law) -- relevant when federal filings involve state law claims
- California choice of law rules (Cal. Civ. Code section 1646) -- governs which state's law applies to contracts
- Federal preemption analysis -- determines when federal law displaces state law (e.g., HIPAA preempts state law only when state law is less protective, per 45 CFR 160.203)

**Triggers:** Every document entering the Vernen system, immediately after type detection.

**Output:**
```
{
  jurisdictions: [
    { level: "federal", basis: "HIPAA applies to all covered entities regardless of state" },
    { level: "state", state: "CA", basis: "Document issued by California state court (Contra Costa County Superior Court)" },
    { level: "local", locality: "Contra Costa County", basis: "Court filing stamped by CCC Superior Court clerk" }
  ],
  preemption_notes: "CMIA (state) provides greater protection than HIPAA for medical records; both apply per 45 CFR 160.203(b)"
}
```

**Quality Gate:** If no jurisdiction can be determined, document is HELD. A document without a jurisdiction cannot have obligations mapped.

---

### SKILL 003: Temporal Law Mapping

**Slug:** `custos-temporal-law-mapping`
**Phase:** Phase 5 (invokes TEMPORIS)
**Purpose:** Ensure that only legal obligations that were in effect on the document date are attached to the document.

**What it does:**
- Extracts the operative date from the document (incident date, filing date, issuance date, execution date, service date)
- Assembles the full list of obligations identified in Phases 2-4
- Invokes TEMPORIS (CITIZEN-018) with the document date and obligation list
- TEMPORIS returns temporal classifications for each obligation:
  - CONFIRMED IN EFFECT -- obligation existed on document date
  - LIKELY IN EFFECT -- obligation probably existed (strong evidence, not confirmed)
  - ANACHRONISM RISK -- obligation may not have existed
  - ANACHRONISM -- NOT IN EFFECT -- obligation did not exist on document date
- Removes anachronistic obligations from the clearance
- Records temporal classifications in the clearance certification

**Governing Standards:**
- Due process (5th/14th Amendment) -- cannot impose obligations retroactively without clear legislative intent
- Ex post facto principles (applied by analogy to civil obligations)
- Specific effective dates of each statute (e.g., CCPA effective January 1, 2020; CPRA amendments effective January 1, 2023)

**Triggers:** After obligation list is assembled, before clearance certification.

**Output:**
```
{
  document_date: "2009-02-15",
  temporal_verifications: [
    { obligation: "HIPAA Privacy Rule", citation: "45 CFR 164.502", classification: "CONFIRMED IN EFFECT", basis: "HIPAA Privacy Rule effective April 14, 2003" },
    { obligation: "CCPA", citation: "Cal. Civ. Code 1798.100", classification: "ANACHRONISM -- NOT IN EFFECT", basis: "CCPA enacted AB 375, effective January 1, 2020; +10.9 years after document" }
  ],
  obligations_removed: ["CCPA", "CPRA"],
  obligations_retained: ["HIPAA Privacy Rule", "CMIA", "Cal. medical retention"]
}
```

**Quality Gate:** No obligation may be attached without temporal verification. TEMPORIS has final authority on temporal classifications.

---

### SKILL 004: PII Detection and Classification

**Slug:** `custos-pii-detection`
**Phase:** Phase 4
**Purpose:** Identify all personally identifiable information in the document and classify it under the applicable legal framework.

**What it does:**
- Scans document content for PII categories defined by applicable law
- Classifies each PII element under its governing statute:
  - **SSN** -- Sensitive PI under CCPA section 1798.140(ae)(4); triggers Cal. Civ. Code section 1798.81.5 security requirement
  - **Driver's license number** -- Sensitive PI under CCPA; triggers California data breach notification if unencrypted and breached (Cal. Civ. Code section 1798.82(e))
  - **Financial account number** -- PI under CCPA section 1798.140(v); triggers GLB safeguards (15 USC section 6801)
  - **Name + address + DOB** -- PI under CCPA; combination may constitute identity under Cal. Penal Code section 530.5
  - **Biometric data** -- Sensitive PI under CCPA section 1798.140(ae)(3); if present, triggers consent requirement under section 1798.121
  - **Racial/ethnic origin** -- Sensitive PI under CCPA section 1798.140(ae)(1); heightened protections
  - **Geolocation** -- Sensitive PI under CCPA section 1798.140(ae)(7) if precise; triggers opt-out right
- Records PII location within document (page, section, field)
- Does NOT redact or modify -- detection only

**Governing Standards:**
- CCPA definition of PI: Cal. Civ. Code section 1798.140(v) -- 11 enumerated categories
- CCPA definition of Sensitive PI: Cal. Civ. Code section 1798.140(ae) -- 9 enumerated categories
- California data breach notification: Cal. Civ. Code section 1798.82 -- PI elements that trigger breach notification
- California disposal law: Cal. Civ. Code section 1798.81 -- PI requiring secure disposal
- Federal identity theft: 18 USC section 1028 -- means of identification

**Triggers:** Every document, after jurisdiction detection confirms applicable privacy law.

**Output:**
```
{
  pii_detected: true,
  elements: [
    { type: "ssn", classification: "sensitive_pi", governing_law: "Cal. Civ. Code 1798.140(ae)(4)", location: "page 1, header field" },
    { type: "full_name", classification: "pi", governing_law: "Cal. Civ. Code 1798.140(v)(1)", location: "page 1, line 3" },
    { type: "date_of_birth", classification: "pi", governing_law: "Cal. Civ. Code 1798.140(v)(6)", location: "page 1, line 4" }
  ],
  aggregate_risk: "high",
  breach_notification_triggered_if_compromised: true
}
```

**Quality Gate:** False negatives are more dangerous than false positives. When in doubt, flag as PII and let downstream review confirm.

---

### SKILL 005: PHI Detection and Classification

**Slug:** `custos-phi-detection`
**Phase:** Phase 4
**Purpose:** Identify all protected health information in the document and classify it under HIPAA and state medical privacy law.

**What it does:**
- Scans for the 18 HIPAA identifiers defined in 45 CFR 164.514(b)(2):
  1. Names
  2. Geographic subdivisions smaller than state
  3. Dates (except year) related to an individual
  4. Phone numbers
  5. Fax numbers
  6. Email addresses
  7. SSN
  8. Medical record numbers
  9. Health plan beneficiary numbers
  10. Account numbers
  11. Certificate/license numbers
  12. Vehicle identifiers and serial numbers
  13. Device identifiers and serial numbers
  14. Web URLs
  15. IP addresses
  16. Biometric identifiers
  17. Full-face photographs
  18. Any other unique identifying number
- Determines if identifiers appear in conjunction with health information (diagnosis, treatment, provider, dates of service, health plan, payment for healthcare)
- Classifies PHI under HIPAA categories: treatment, payment, healthcare operations, research, public health, judicial/administrative proceedings
- Identifies psychotherapy notes (heightened protection under 45 CFR 164.508(a)(2))
- Maps to CMIA obligations where California law provides greater protection

**Governing Standards:**
- HIPAA Privacy Rule: 45 CFR 164.501 (definition of PHI)
- HIPAA de-identification: 45 CFR 164.514 (Safe Harbor and Expert Determination methods)
- CMIA: Cal. Civ. Code section 56.05(j) (definition of medical information -- broader than HIPAA PHI)
- CMIA authorization: Cal. Civ. Code section 56.11 (authorization requirements)
- Psychotherapy notes: 45 CFR 164.508(a)(2) (separate authorization required)

**Triggers:** Every document detected as medical record, health-related, or containing health information regardless of primary document type.

**Output:**
```
{
  phi_detected: true,
  hipaa_identifiers_present: [1, 3, 8, 11],
  health_information_present: ["diagnosis", "treatment", "dates_of_service"],
  phi_classification: "treatment_record",
  psychotherapy_notes: false,
  cmia_applies: true,
  cmia_broader_protection: "CMIA covers 'medical information' which includes mental health, alcohol/drug treatment -- broader than HIPAA PHI"
}
```

**Quality Gate:** Any document containing ANY health information combined with ANY identifier is treated as PHI until confirmed otherwise. HIPAA does not forgive missed PHI.

---

### SKILL 006: Legal Obligation Resolution

**Slug:** `custos-legal-obligation-resolution`
**Phase:** Phase 3
**Purpose:** The core skill. Given document type + jurisdiction + PII/PHI categories, resolve the complete set of legal obligations that govern Vernen's handling of the document.

**What it does:**
- Takes inputs from Skills 001-005 (type, jurisdiction, PII, PHI)
- Queries the Standards Library (`GET /api/standards/:citizen/for-document?type=`)
- Queries live legal APIs for statute text where Standards Library entry is insufficient
- Builds the obligation matrix: for each applicable statute/regulation, extracts:
  - **What it requires** (the specific obligation language)
  - **Who it binds** (Vernen as custodian, processor, business associate, etc.)
  - **What triggers it** (document type, PII category, PHI presence, jurisdiction)
  - **What the penalty is** (statutory damages, regulatory fines, criminal penalties)
  - **What the enforcement mechanism is** (private right of action, agency enforcement, criminal prosecution)
  - **What the retention period is** (if the statute specifies one)
  - **What the disposal method is** (if the statute specifies one)
- Resolves conflicts between overlapping frameworks (e.g., HIPAA vs. CMIA -- apply the more protective standard per 45 CFR 160.203)
- Produces the complete obligation record attached to the clearance certification

**Governing Standards:**
- Every standard in CUSTOS's Standards Library (Section VII of dossier) -- 43+ custodial obligations
- Standards Library cross-references for related obligations
- Federal preemption rules for conflict resolution

**Triggers:** After type detection, jurisdiction detection, and PII/PHI scanning are complete.

**Output:** The `legal_obligations` array in the clearance certification (see Phase 7 in dossier).

**Quality Gate:** Every obligation must cite a primary legal source. No obligation based on "general privacy principles" or "industry best practices." If CUSTOS cannot cite a statute, the obligation is not attached.

---

### SKILL 007: Standards Library Query

**Slug:** `custos-standards-library-query`
**Phase:** Phase 3 (sub-skill of Legal Obligation Resolution)
**Purpose:** Query the Vernen Standards Library for standards applicable to a document type, then extract custodial obligations from the results.

**What it does:**
- Queries `GET /api/standards/:citizen/for-document?type={document_type}` for each relevant Citizen
- Queries `POST /api/standards/:citizen/search` with obligation-specific terms
- Queries `GET /api/standards/:citizen/cross-references/:id` to discover related obligations
- Filters results for custodial obligations (as distinct from content standards)
- Maps Standards Library entries to CUSTOS obligation format
- Identifies gaps where the Standards Library lacks coverage that CUSTOS needs

**Standards Library Citizens queried (by document type):**

| Document Type | Citizens Queried | Reason |
|--------------|-----------------|--------|
| Medical records | PRIVAXIS, ETHICARA | HIPAA/CMIA (PRIVAXIS), medical professional standards (ETHICARA) |
| Court filings | REGULIS, ADVOCIS | Court rules (REGULIS), constitutional rights (ADVOCIS) |
| Financial records | FISCARA, PRIVAXIS | Financial regulations (FISCARA), financial privacy (PRIVAXIS) |
| Law enforcement records | REGULIS, ADVOCIS, VIGILUS | POST standards (REGULIS), civil rights (ADVOCIS), CLETS (VIGILUS) |
| Identity documents | VIGILUS, PRIVAXIS | Identity theft (VIGILUS), PII protections (PRIVAXIS) |
| Employment records | REGULIS, FISCARA | Labor law (REGULIS), wage/tax records (FISCARA) |
| Government correspondence | REGULIS, ADVOCIS | APA/public records (REGULIS), constitutional rights (ADVOCIS) |
| Contracts | LEXARC, REGULIS | Commercial law (LEXARC), regulatory requirements (REGULIS) |

**Triggers:** During Legal Obligation Resolution, before live API queries.

**Output:** Structured list of Standards Library matches with citation, requirements, and cross-references.

**Quality Gate:** Standards Library is the first source. Live API queries are fallback for gaps. This minimizes API calls while ensuring completeness.

---

### SKILL 008: Cross-Reference Resolution

**Slug:** `custos-cross-reference-resolution`
**Phase:** Phase 3 (sub-skill of Legal Obligation Resolution)
**Purpose:** When one obligation is identified, discover related obligations through the Standards Library cross-reference system.

**What it does:**
- For each identified obligation, queries `GET /api/standards/:citizen/cross-references/:id`
- Follows cross-reference chains: if HIPAA links to CMIA, and CMIA links to Cal. Bus. & Prof. Code section 2266, CUSTOS follows the chain
- Identifies relationship types: IMPLEMENTS, SUPPLEMENTS, INTERPRETS, SUPERSEDES, CONFLICTS_WITH
- Resolves conflicts using hierarchy: federal preemption rules, "more protective standard" rules, temporal priority
- Adds cross-referenced obligations to the clearance if they impose additional custodial duties

**Example chain:**
```
HIPAA Privacy Rule (45 CFR 164.502)
  --SUPPLEMENTS--> CMIA (Cal. Civ. Code 56.10) [state law, more protective]
  --SUPPLEMENTS--> Cal. Bus. & Prof. Code 2266 [professional record-keeping]
  --IMPLEMENTS--> 42 USC 1320d [HIPAA enabling statute]
  --CROSS-REFERENCES--> Cal. Code Regs. tit. 22 sec. 70751 [retention period]
```

**Triggers:** After initial obligation resolution, before temporal verification.

**Output:** Expanded obligation list with cross-reference trails documented.

**Quality Gate:** Cross-reference chains are followed to a maximum depth of 3 to prevent circular references. Every cross-reference must have a cited relationship type.

---

### SKILL 009: Duty of Care Establishment

**Slug:** `custos-duty-of-care`
**Phase:** Phase 6
**Purpose:** Map bilateral obligations -- what Vernen must do AND what the client must know about the document's legal protections.

**What it does:**
- Takes the complete obligation list from Phase 3 (as verified by Phase 5)
- Separates obligations into two categories:
  - **Vernen's custodial duties** -- what Vernen must do to comply with the law while holding this document
  - **Client's rights and information** -- what the client has the right to know, request, or do regarding this document
- For Vernen duties, specifies:
  - Storage requirements (encryption, access controls)
  - Retention period and authority
  - Disposal method and authority
  - Access restrictions (who within Vernen may access)
  - Logging requirements (what access must be recorded)
  - Breach response obligations (what Vernen must do if compromised)
- For client rights, specifies:
  - Access rights (right to view, copy, receive)
  - Amendment rights (right to request corrections)
  - Deletion rights (right to request destruction, with exceptions)
  - Portability rights (right to receive in usable format)
  - Restriction rights (right to limit use)
  - Complaint rights (where to file complaints if dissatisfied)

**Governing Standards:**
- HIPAA patient rights: 45 CFR 164.520 (notice), 164.524 (access), 164.526 (amendment), 164.528 (accounting of disclosures)
- CCPA consumer rights: Cal. Civ. Code sections 1798.100 (know), 1798.105 (delete), 1798.110 (categories), 1798.115 (sale/sharing), 1798.120 (opt-out), 1798.125 (non-discrimination)
- FERPA parent/student rights: 20 USC section 1232g(a)(1) (inspect/review), (a)(2) (amendment)
- RFPA customer rights: 12 USC sections 3404-3408 (notice, access, challenge)

**Triggers:** After temporal verification confirms which obligations are in effect.

**Output:** The `bilateral_obligations` object in the clearance certification (see Phase 7 in dossier).

**Quality Gate:** Every duty must cite its source. Every right must cite its source. No generic "Vernen will protect your data" -- specific obligations with specific citations.

---

### SKILL 010: Intake Clearance Certification

**Slug:** `custos-intake-clearance`
**Phase:** Phase 7
**Purpose:** Issue the formal clearance certification that accompanies the document through the entire pipeline and authorizes downstream processing.

**What it does:**
- Assembles all outputs from Skills 001-009 into the clearance certification
- Generates a unique clearance ID
- Computes document hash for integrity verification
- Records timestamp
- Makes binary clearance determination:
  - **CLEARED** -- all phases complete, obligations mapped, document released to pipeline
  - **HELD** -- one or more phases incomplete, document quarantined until resolved
  - **HELD -- HUMAN REQUIRED** -- CUSTOS cannot determine type, jurisdiction, or obligations without human input
- Attaches clearance as document metadata (travels with document through entire pipeline)
- Logs clearance to SENTINEL-0 for permanent audit trail
- Routes document to ARCHIVIST-0 (next in pipeline)

**Governing Standards:**
- The clearance certification itself is governed by Vernen's internal Standards of Creation and the Founding Principle
- The obligation to maintain an audit trail is governed by SOX section 802 (record retention, applicable by analogy), California record retention statutes, and professional duty of competence

**Triggers:** After all prior skills have completed successfully.

**Output:** Complete clearance certification (JSON structure as documented in dossier Phase 7).

**Quality Gate:**
- Clearance ID must be unique and sequential
- Document hash must be computed before any processing (baseline integrity)
- Every obligation must have a citation
- Every PII/PHI element must be classified
- Every jurisdiction must have a basis
- Temporal verification must be complete
- Bilateral obligations must be mapped
- If ANY quality gate in ANY prior skill failed, clearance status is HELD, not CLEARED

---

## Skill Dependency Map

```
SKILL 001 (Type Detection)
    |
    v
SKILL 002 (Jurisdiction Detection)
    |
    v
SKILL 004 (PII Detection) + SKILL 005 (PHI Detection)  [parallel]
    |
    v
SKILL 006 (Legal Obligation Resolution)
    |--- invokes SKILL 007 (Standards Library Query)
    |--- invokes SKILL 008 (Cross-Reference Resolution)
    |
    v
SKILL 003 (Temporal Law Mapping) -- invokes TEMPORIS (CITIZEN-018)
    |
    v
SKILL 009 (Duty of Care Establishment)
    |
    v
SKILL 010 (Intake Clearance Certification)
```

---

## Skill Summary Table

| # | Skill Name | Slug | Phase | Dependencies | External Invocations |
|---|-----------|------|-------|-------------|---------------------|
| 001 | Document Type Detection | `custos-document-type-detection` | 1 | None | None |
| 002 | Jurisdiction Detection | `custos-jurisdiction-detection` | 2 | Skill 001 | None |
| 003 | Temporal Law Mapping | `custos-temporal-law-mapping` | 5 | Skills 001-002, 004-008 | TEMPORIS (CITIZEN-018) |
| 004 | PII Detection and Classification | `custos-pii-detection` | 4 | Skills 001, 002 | California statutes API, CCPA text |
| 005 | PHI Detection and Classification | `custos-phi-detection` | 4 | Skills 001, 002 | CFR API (45 CFR 164), CMIA text |
| 006 | Legal Obligation Resolution | `custos-legal-obligation-resolution` | 3 | Skills 001-002, 004-005 | Standards Library API, USC/CFR/CA APIs |
| 007 | Standards Library Query | `custos-standards-library-query` | 3 | Skill 006 (parent) | Standards Library API endpoints |
| 008 | Cross-Reference Resolution | `custos-cross-reference-resolution` | 3 | Skill 007 | Standards Library cross-reference API |
| 009 | Duty of Care Establishment | `custos-duty-of-care` | 6 | Skills 003-008 | HIPAA/CCPA/FERPA rights APIs |
| 010 | Intake Clearance Certification | `custos-intake-clearance` | 7 | All prior skills | SENTINEL-0 logging |

---

**Document Authority:** The Founding Principle
**Filed:** March 21, 2026
**Registry Entry:** CITIZEN-019 -- CUSTOS
**Skills Count:** 10
**External Dependencies:** TEMPORIS (CITIZEN-018), Standards Library API, SENTINEL-0 logging, USC/CFR/CA legal research APIs
