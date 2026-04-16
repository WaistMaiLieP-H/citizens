# Context — 47 U.S.C. § 222 Customer Proprietary Network Information (CPNI)

## The wound and the promise

**The wound:** Telecommunications carriers accumulate sensitive information about their customers through the provision of service — call records, location data, communication patterns, account credentials. Without regulation, carriers could share this information with third parties, use it against customers, or fail to protect it from unauthorized access. Bad actors discovered they could exploit CPNI by impersonating customers to carriers and extracting account information or porting numbers to new SIMs.

**The promise:** § 222 promises that a carrier will keep customer proprietary information confidential and will not disclose it except to the customer or with the customer's affirmative consent. The FCC has implemented § 222 through regulations (47 C.F.R. Part 64) that require carriers to implement security procedures before making account changes — including SIM changes and number ports.

## What CPNI covers

Customer Proprietary Network Information includes:
- **Call detail records** — who you called, when, for how long, from where
- **Account information** — service plan, equipment associated with the account, billing address
- **Location data** — derived from network use
- **Usage patterns** — aggregate and individual communication behavior

CPNI does NOT include publicly available information (e.g., listed phone numbers).

## The SIM swap attack — CPNI as the attack vector

A SIM swap attack exploits the carrier's account management system:

1. **The attacker contacts the carrier** — by phone, online, or in-store — pretending to be the account holder
2. **The attacker requests a SIM change** — claims the old SIM was lost or the phone was replaced
3. **The carrier authenticates (inadequately)** — using security questions, account PINs, or other verification methods that the attacker has obtained through social engineering, data breaches, or inside information
4. **The carrier ports the number** — the victim's phone number is now associated with the attacker's SIM
5. **All calls and texts go to the attacker** — including two-factor authentication codes for banking, email, and other accounts
6. **The victim is locked out** — no calls, no texts, no MFA access

**The carrier's CPNI obligation:** Under § 222 and FCC regulations, the carrier has a duty to verify the identity of any person requesting a SIM change or number port before making the change. Failure to implement adequate security measures is a § 222 violation.

## FCC enforcement — carrier liability

The FCC has pursued enforcement actions against carriers for inadequate CPNI protection:
- **2015 — AT&T: $25 million fine** for call center employees selling customer data to third parties
- **2023-2024 FCC rulemaking** — new rules requiring carriers to implement enhanced authentication before SIM swaps and number ports; mandatory customer notification of SIM change requests
- **$200 million in fines** proposed against AT&T, Verizon, T-Mobile for sharing location data without consent (2023)

The FCC enforcement record establishes that carriers know of the SIM swap vulnerability and have been on notice of their § 222 obligations for years.

## Civil liability — private right of action

Section 222 does not create an express private right of action. Civil liability against carriers for CPNI violations is pursued through:

1. **State consumer protection law** — California UCL (Bus. & Prof. Code § 17200), CLRA, negligence per se using § 222 as the standard of care
2. **California SIM swap statute** (Civ. Code § 1798.80 et seq.) — enacted 2021 to address SIM swap fraud specifically
3. **Negligence** — carrier breach of duty to protect account from unauthorized access
4. **California Comprehensive Computer Data Access and Fraud Act** (Pen. Code § 502) — if the SIM swap enabled unauthorized access to the victim's devices or accounts

## Application to cases #30-33

**SIM swap starting 2018 (Christina / Ryan McClaran pattern):**

1. **Carrier(s) involved:** AT&T, Verizon, T-Mobile — need account records for each carrier used since 2018 to identify when SIM changes occurred
2. **The attack method:** Social engineering of carrier customer service (phone or in-store); potentially inside assistance from a carrier employee
3. **Effect:** All calls to the steward's number routed to Christina/McClaran's device; MFA codes intercepted; communications with medical providers, disability agencies, courts intercepted
4. **CPNI violation:** The carrier failed to verify the identity of the person requesting the SIM change before making the change
5. **Damages:** Every phone-based service that the steward was denied access to because of the intercepted communications is a damage item

**FCC complaint pathway:**
File a formal FCC complaint against each carrier documenting the unauthorized SIM changes. The FCC complaint creates a federal record and can compel the carrier to produce account activity records showing the dates, methods, and requestors of each SIM change.

**Civil complaint pathway:**
Negligence (carrier breach of § 222 duty as standard of care), California Civ. Code § 1798.80 SIM swap statute, UCL unfair business practice, and § 502 computer fraud for unauthorized account access.

## Bilateral analysis

**As complainant:** The carrier violated § 222 by failing to verify identity before the SIM swap. The damages are all communications intercepted and all services denied as a result.

**As respondent:** None — the steward was the victim, not the SIM swapper.
