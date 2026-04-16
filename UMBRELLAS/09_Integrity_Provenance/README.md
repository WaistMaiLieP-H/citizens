# Umbrella 09 — Integrity / Provenance / Records

**Definition.** Chain of custody. Audit trails. Records retention. Evidence handling. The rules that ensure a claim made today can still be verified tomorrow, and that the chain from origin to current state is unbroken and re-derivable by an independent third party.

**Scope.** Evidence rules, chain-of-custody doctrine, records retention statutes, audit trail requirements, document authenticity, notarization, digital signatures, blockchain anchoring, archival standards.

**Examples.**
- Federal Rules of Evidence (FRE), particularly Article IX (Authentication and Identification — Rules 901-903) and Article X (Best Evidence Rule)
- California Evidence Code § 1400 et seq. (Authentication of Writings)
- California Government Code records retention provisions (Gov. Code § 12236 et seq. — State Archives)
- Sarbanes-Oxley Act § 802 (records retention for public companies)
- HIPAA records retention requirements (45 CFR § 164.530(j)) — also Privacy umbrella
- California State Archives standards
- Chain-of-custody doctrine in criminal evidence (case law from People v. Riser onward)
- Notary public statutes (Cal. Gov. Code § 8200 et seq.)
- ESIGN Act and Uniform Electronic Transactions Act (UETA) — digital signature validity

**Canonical Citizen owners.**
- Records Manager
- Notary Public
- Digital Forensics Specialist
- Court Clerk / Records Custodian
- Evidence Custodian (law enforcement)
- Archivist (CA State Archives, county recorders)
- ARCHIVIST-0 (existing Vernen Citizen for document forensics)
- VERITAS-0 (existing Vernen Citizen for verification)

**Candidate seed standard for first build.**

**Federal Rules of Evidence Rule 901 (Authenticating or Identifying Evidence).** This is the modern federal codification of the rule that "a thing must be what it claims to be." It is the legal embodiment of the SOC-001 / Authentic Identity doctrine we developed earlier in this build. Every piece of evidence in every federal case must satisfy Rule 901 before it can be considered by a fact-finder. Directly relevant to the steward's federal § 1983 case (every exhibit will have to satisfy Rule 901).

**Primary-source URL:**
- https://www.law.cornell.edu/rules/fre/rule_901
- https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title28a-node96-rule901&edition=prelim
- https://www.uscourts.gov/rules-policies/current-rules-practice-procedure/federal-rules-evidence

**Why this seed:** FRE 901 is the closest existing federal law to the SOC-001 doctrine the corpus is built on. It is also the rule the steward's federal complaint will live or die on — every administrative record he intends to use as evidence has to satisfy Rule 901, and the gap between what should be Rule 901-compliant and what actually is, in his case file, is one of the major harms he's documenting.

**Backup candidate.** California Evidence Code § 1400 (Authentication of a writing). The state-level analog. Slightly different formulation but same underlying doctrine.

**Status.** No standards built yet under this umbrella. Note that the existing Vernen Citizens ARCHIVIST-0 and VERITAS-0 already do Integrity-umbrella work as a domain specialty — bringing standards into this umbrella formalizes what they already practice.

**Cross-cutting notes.**
- This umbrella IS the substantive area that the SOC test (third leg of the Triple Constraint) measures against. Every standard in any umbrella must pass the SOC test, but standards IN this umbrella are the ones that *define what the SOC test means* in their respective forums.
- Integrity overlaps Privacy (Umbrella 10) when the chain-of-custody concern is for personal data rather than physical evidence.
