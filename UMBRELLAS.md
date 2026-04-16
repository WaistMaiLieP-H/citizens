# Substantive Umbrellas — Vernen Compliance Corpus

**Filed:** 2026-04-08
**Status:** Living catalog. Will be revised as the corpus matures.
**Note:** This document corrects the earlier "at least 10" framing. The honest count is closer to 18 and the most consequential omission was **Family / Personal Status**, which is the umbrella the steward's own case lives in. Leaving it off the first list was a real gap, not a rounding error.

---

## What this catalog is

The **Triple Constraint** (Governing Guidelines / Standards of Creation / Standard of Care) is the *test* every standard must pass to enter the corpus. The **substantive umbrellas** below are the *categories* the standards belong to. Three orthogonal dimensions:

1. **Umbrella** — the substantive category the standard is about (which Citizen owns it, what domain expertise interprets it)
2. **Triple Constraint** — the three tests each standard must pass to be valid
3. **Five-Layer Bar** — the operational form of the tests, applied to a single artifact

A standard belongs to one or more umbrellas; every standard, in any umbrella, must pass all three tests; every standard's manifest must satisfy the five-layer bar.

---

## The umbrellas (current count: 18)

### 1. Authority / Governing Law
Statutes, regulations, court rules, constitutional provisions, treaties, executive orders. The binding-source layer.
*Examples:* the U.S. Code, the California Code of Regulations, FRCP, FRE, the U.S. Constitution.

### 2. Procedure
How processes must be conducted in administrative, civil, and criminal contexts.
*Examples:* FRCP, FRCrP, California Code of Civil Procedure, administrative procedure acts, due process doctrine.

### 3. Substance / Specification
What things must physically be — material specs, formulary entries, identity standards.
*Examples:* ASTM material specs, building codes, drug formulary, food identity standards, ANSI/ISO product specs.

### 4. Measurement / Metrology
How things are measured, what units are used, what counts as a calibrated instrument.
*Examples:* NIST kilogram, ASTM testing methods, ISO/IEC 17025 calibration standards, FDA validated assay methods.

### 5. Safety
How things must protect human life, health, and physical wellbeing.
*Examples:* OSHA, Cal/OSHA, fire codes, NEC, FAA airworthiness, FDA drug safety, transportation safety standards. **The Field Act and Riley Act both live here.**

### 6. Ethics / Conduct
How professionals must behave; fiduciary duty; conflict-of-interest; professional codes of conduct.
*Examples:* ABA Model Rules, AMA Code of Medical Ethics, engineering codes of ethics, accounting professional standards.

### 7. Access / Inclusion
Who must be served; barriers that must be removed; accommodations that must be provided.
*Examples:* ADA, Section 504, civil rights statutes, language access, WCAG.

### 8. Environmental / External Impact
What must not be damaged; emissions and discharge limits; stewardship of shared resources.
*Examples:* Clean Air Act, Clean Water Act, RCRA, CERCLA, hazardous materials regulation, NEPA.

### 9. Integrity / Provenance / Records
Chain of custody, evidence handling, audit trails, records retention.
*Examples:* federal and state evidence rules, records retention statutes, audit trail requirements, FRE 901-902.

### 10. Privacy / Information Stewardship
Personal data, confidentiality, privileged communication.
*Examples:* HIPAA, GDPR, CCPA/CPRA, attorney-client privilege, work-product doctrine, FERPA, GLBA.

---

### 11. Family / Personal Status — *the umbrella Michael's case lives in*
Marriage, divorce, child custody, adoption, conservatorship, guardianship, paternity, name change, civil unions, domestic partnerships. Anything that defines the legal status of a person in relation to other persons.

This umbrella was **omitted from the first draft of the catalog** and that omission is corrected here. It is the most consequential omission because it is the substantive area in which the steward has spent sixteen years documenting administrative and procedural failures. It is also one of the umbrellas where SOC failures (chain-of-custody breaks, missing records, fabricated witnesses, jurisdictional traps) cause the deepest and least-recoverable harm to individuals. The forensic-audit work the steward has already done on his own case is, structurally, a Vernen-corpus contribution to this umbrella before the umbrella had a name.

*Examples:* California Family Code, Probate Code (conservatorships and guardianships), DVPA (Domestic Violence Prevention Act), CLETS (Cal Law Enforcement Telecommunications System), juvenile dependency law, ICWA (Indian Child Welfare Act).

### 12. Property / Title / Ownership
Real estate, intellectual property, water rights, mineral rights, recording acts, eminent domain, adverse possession.
*Examples:* California Civil Code real property provisions, U.S. patent and copyright statutes, Uniform Commercial Code articles 2/9, recording acts.

### 13. Finance / Money / Currency / Banking
Banking regulation, securities, currency, monetary policy, lending standards, consumer credit, AML.
*Examples:* Glass-Steagall, Dodd-Frank, Securities Act of 1933, Bank Secrecy Act, Truth in Lending, FDIC regulation, state contractor bond requirements.

### 14. Tax
Tax statutes, tax procedure, tax accounting standards, tax exemption rules.
*Examples:* Internal Revenue Code, California Revenue and Taxation Code, IRS regulations, GAAP/IFRS where they intersect with tax accounting. *(Could be considered a sub-umbrella of Finance, but is large enough and distinct enough in practice to warrant its own.)*

### 15. Communication / Speech / Press
First Amendment doctrine, telecommunications regulation, broadcast standards, libel and defamation, journalism ethics.
*Examples:* FCC regulations, Section 230, state defamation law, journalism shield laws.

### 16. Travel / Movement / Immigration
Vehicle codes, air travel, maritime, rail, immigration, border control, passports, asylum.
*Examples:* California Vehicle Code, FAA regulations, Immigration and Nationality Act, USCIS procedures, FMCSA.

### 17. Energy
Energy policy, utility regulation, oil and gas, electricity, renewables, nuclear, grid reliability.
*Examples:* California Public Utilities Code, FERC orders, NRC regulations, NERC reliability standards, state RPS rules.

### 18. Agriculture / Food
Farming standards, food safety, organic certification, pesticide regulation, animal welfare in food production.
*Examples:* USDA regulations, FDA food safety, FSMA, NOP organic standards, state pesticide use enforcement.

---

## Umbrellas the catalog is still missing or under-developed

This list is itself outstanding work. Honest candidates I have not yet committed:

- **Religion / Conscience** — religious accommodation, tax-exempt status of religious organizations, conscientious objection. May be its own umbrella or a cross-cutting concern within Access/Inclusion and Authority.
- **Education** — accreditation, school standards, teacher credentialing, student rights. Currently distributed across Authority, Access, and Privacy but probably deserves its own umbrella.
- **Cyber / Information Security** — distinct from Privacy; covers threat models, vulnerability disclosure, incident response, secure development standards. Currently overlaps Integrity and Privacy.
- **Defense / National Security** — military regulation, classified information handling, export control. Cross-cutting but possibly its own.
- **Sports / Athletic Conduct** — rules of competition, anti-doping, athlete safety. Distinct domain with its own bodies (USADA, IOC, NCAA).
- **Cultural Heritage / Antiquities** — NAGPRA, historic preservation, museum ethics, archaeological standards.

The right number of umbrellas depends on the use case. For an intake gate (CUSTOS), broader umbrellas are easier to triage with. For an audit pipeline, finer umbrellas are easier to specialize Citizens against. The catalog should evolve toward the granularity that lets each Citizen own a domain coherent enough to develop expertise in, without forcing standards into umbrellas they don't fit.

---

## How to use this catalog

When building a new standard:
1. Identify which umbrella(s) it primarily belongs to.
2. Use that umbrella to identify the right Citizen owner from the persona catalog.
3. Record the umbrella in the manifest's `umbrellas` field.
4. If the standard doesn't fit any umbrella in this catalog, **flag the gap** in the manifest's outstanding work and propose either a new umbrella or a re-categorization.

When in doubt, prefer fewer umbrellas with broader coverage over more umbrellas with narrow scope. Over-specialization fragments the corpus; under-specialization conflates distinct domains. The middle path is better than either extreme.

---

**Filed:** 2026-04-08
**Authority:** Vernen corpus architecture; under steward review
**Outstanding:** Promote Religion, Education, Cyber, and Defense to first-class umbrellas after primary-source review of representative standards from each
