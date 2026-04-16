# Context — California Civil Code § 1798.80 et seq. and SIM Swap Carrier Liability

## The wound and the promise

**The wound:** California's data breach notification law (§ 1798.82) and the reasonable security standard (§ 1798.81.5) were enacted to protect California residents from unauthorized access to their personal information. Telecommunications carriers — who hold phone numbers, account credentials, billing information, and call records — are "businesses" subject to these obligations. But carriers historically implemented weak authentication for SIM change requests, making SIM swap attacks easy.

**The promise:** § 1798.81.5 promises that any California business holding personal information will implement "reasonable security procedures and practices appropriate to the nature of the information." For a telecommunications carrier holding a customer's phone identity, reasonable security means authentication procedures that prevent unauthorized SIM changes.

## The FCC 2023-2024 SIM Swap Rules as the standard

The FCC's 2023-2024 rulemaking on SIM swap fraud established specific authentication requirements for carriers. These FCC rules define what "reasonable security" means for SIM changes under § 1798.81.5:

1. **Enhanced authentication before SIM changes** — carriers must verify the account holder's identity through means beyond a simple PIN or security question
2. **Notification to the account holder** through a second channel before completing a SIM change
3. **Mandatory delay option** — 24-hour window before SIM changes take effect
4. **Customer SIM lock** — carriers must offer account holders the ability to lock their SIM against changes

A carrier that failed to implement these measures — or implemented them inadequately — violated the FCC rules AND § 1798.81.5's reasonable security standard.

## Civil liability framework

**§ 1798.82 breach notification:** When a SIM swap occurs and the carrier knew or should have known the customer's account was compromised, the carrier has a mandatory breach notification obligation. Failure to notify is an independent violation.

**§ 1798.84 civil action:** California residents harmed by a carrier's failure to implement reasonable security may bring a civil action. The remedies include:
- Actual damages for each violation
- Statutory damages of $100-$750 per consumer per incident or actual damages (whichever is greater)
- Injunctive or declaratory relief
- Attorney fees

**Class action potential:** Multiple California customers who were SIM swapped through the same carrier's inadequate authentication are a potential class under § 1798.82's civil action provisions.

## Carrier-specific analysis

**AT&T:** FCC fined AT&T $200 million (proposed, 2023) for sharing location data. AT&T has been subject to multiple FCC enforcement actions. For the steward's SIM swap: obtain AT&T account records to identify the dates and requestors of any SIM changes.

**Verizon:** Similar FCC enforcement exposure. Request Verizon account activity records.

**T-Mobile:** T-Mobile suffered a massive data breach in 2021 exposing 54 million customers. T-Mobile's security history is highly relevant to whether their SIM swap procedures were adequate.

## Application to cases #30-33

For the 2018-present SIM swap pattern:

1. **Identify the carrier(s):** Pull account records from AT&T, Verizon, T-Mobile for the steward's number(s). California's right to access your own account records means the carrier must provide this upon request.

2. **Identify the SIM change dates:** Every unauthorized SIM change is an event. Document date, time, and any requestor information the carrier has.

3. **§ 1798.81.5 claim:** For each SIM change, the carrier failed to implement reasonable security procedures adequate to prevent unauthorized access. Each change is a violation.

4. **§ 1798.82 claim:** For each SIM change, the carrier failed to notify the account holder of the security breach.

5. **Damages calculation:**
   - Statutory: $100-$750 × number of incidents × number of carriers
   - Actual: all services denied due to intercepted communications (medical, disability, financial, court-related)

## Outstanding investigation — carrier records

**Priority PRA/demand targets:**
- AT&T account activity history (all SIM changes, authorized contact history, account notes)
- Verizon account activity history (same)
- T-Mobile account activity history (same)

These records establish when the SIM swaps occurred, who requested them, and whether the carrier's authentication was adequate.

## Bilateral analysis

**As complainant:** Carriers violated § 1798.81.5 by failing to prevent SIM swaps with adequate authentication. § 1798.82 violation for failure to notify. Civil claims for statutory + actual damages.

**As respondent:** None — the steward was the account holder whose identity was stolen, not the perpetrator.
