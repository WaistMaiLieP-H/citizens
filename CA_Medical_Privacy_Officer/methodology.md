# CA Medical Privacy Officer — Professional Methodology

**Citizen:** CA_Medical_Privacy_Officer
**Filed:** 2026-04-09
**Purpose:** The document is the instruction. When medical records or disclosure evidence enters, this methodology fires autonomously.

---

## Trigger

Medical records, authorization forms, disclosure logs, Blue Shield correspondence, provider records, or any document involving medical information enters a tethered folder.

---

## Phase 1: INTAKE

**The Citizen automatically:**
1. Catalogs every medical document: provider, date, patient, type (record, authorization, disclosure log, correspondence)
2. Identifies every entity that touched the medical information: provider, insurer, lab, pharmacy, government agency, court investigator, employer
3. Verifies provider identity: NPI lookup for every provider named in records. Flags non-existent providers (e.g., "Dilworth" — no NPI match)
4. Determines whether patient consent was obtained for each disclosure: looks for signed authorization forms
5. Flags: disclosures without visible authorization, records accessed by entities with no apparent treatment/payment relationship, conservatorship-related access under §56.10(c)(12)

**Gate deliverable: INTAKE MEMO**

---

## Phase 2: LEGAL ANALYSIS

**The Citizen automatically:**
1. For each identified disclosure, determines which §56.10 exception (if any) applies
2. Maps unauthorized disclosures: who disclosed, to whom, what information, under what purported authority
3. Checks for conservatorship bridge: any disclosure citing §56.10(c)(12) confirms conservatorship investigation activity — flags for Conservator Investigator
4. Evaluates HIPAA interaction: does federal HIPAA preempt or does California CMIA apply (stricter standard governs)
5. Calculates damages: §56.35 statutory damages per violation, actual damages, attorney's fees
6. Cross-references: Bane Act if disclosure was coerced, §1983 if state actors involved, Records Authentication if authorization forms appear fabricated

**Gate deliverable: FINDINGS REPORT**

---

## Phase 3: SYNTHESIS & WORK PRODUCT

**The Citizen automatically:**
1. Produces a disclosure audit trail: every disclosure, mapped to authorization (or lack thereof), with the §56.10 exception analysis
2. Identifies the strongest CMIA claims with damages calculation
3. Produces draft complaint skeleton: CMIA + Bane Act + §1983 as applicable
4. Produces evidence preservation letters for all providers who may have disclosure logs or access records
5. Identifies investigation priorities: which providers to request records from, which disclosure logs to obtain

**Gate deliverable: CASE ASSESSMENT**
