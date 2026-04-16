# Historical Chain — 47 C.F.R. §64.2010 CPNI Framework

## The Two-Stage Evolution

### Stage 01 — 1996 Origin: Telecommunications Act §222

Congress enacted 47 U.S.C. §222 in the Telecommunications Act of 1996 — creating the
first federal statutory duty for carriers to protect Customer Proprietary Network
Information. The initial FCC implementing rules (1999) established the framework but
did not yet specify authentication requirements.

The gap: carriers could still use biographical information (SSN, DOB) for customer
authentication when handling CPNI or account changes. This gap enabled pretexting
attacks and was exploited systematically.

---

### Stage 02 — 2007 FCC Order + 2023 SIM Swap Action

**FCC 07-22 (2007):** The comprehensive CPNI order following the HP pretexting scandal
closed the authentication gap by requiring:
- Customer-selected passwords/PINs for CPNI access
- Prohibition on biographical information alone as authentication
- Breach notification requirements (FBI/Secret Service + customer notification)

This is the current operative framework.

**AT&T 2015 enforcement:** $25 million CPNI settlement for authentication failures
that enabled unauthorized CPNI access through call center vendors. AT&T on actual
notice of authentication vulnerability.

**FCC 23-67 (2023):** SIM swap specifically identified as CPNI violation. Carriers
required to notify customers before executing SIM swaps, implement enhanced verification,
and allow SIM lock options.

---

## No Private Right of Action Under §222

**Important limitation:** 47 U.S.C. §222 does not create a private right of action.
The civil liability path for CPNI violations runs through:
1. Negligence (CPNI rules define the standard of care; violation = negligence per se)
2. California UCL §17200 (unlawful prong — CPNI violation = unlawful business practice)
3. FCC enforcement complaint (regulatory, not civil damages)

The CPNI standard is an input to the negligence / UCL claims against AT&T, not a
standalone damages claim.

## Significance in the Litigation Stack

CPNI rules complete the AT&T liability theory:
- AT&T is a necessary actor in the SIM swap (only AT&T can execute the SIM port)
- AT&T violated specific federal CPNI authentication obligations when it processed
  the fraudulent port
- AT&T was on actual notice of this vulnerability (2015 enforcement action)
- AT&T's breach is the but-for cause of all downstream harms (communications interception,
  account access, financial fraud, disability claim interference)

This makes AT&T potentially jointly and severally liable with McClaran for all damages.
