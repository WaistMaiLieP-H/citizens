# Current Rule — 18 U.S.C. §§3121-3127 (Pen Register Act / ECPA Title III)

## THE WOUND

Before 1986, pen registers — devices that record outgoing call numbers dialed from
a telephone — required no court authorization for law enforcement to install. The
Supreme Court in Smith v. Maryland (1979) held that a pen register does not violate
the Fourth Amendment because telephone subscribers have no reasonable expectation of
privacy in the numbers they dial — they voluntarily convey that information to the
telephone company.

The result: law enforcement could monitor who you called without a warrant. The
metadata of your communications — who, when, how often, from where — was unprotected.

Congress addressed this gap in 1986 as part of ECPA, adding Title III (Pen Register
and Trap and Trace Devices statute, 18 U.S.C. §§3121-3127).

## THE PEN REGISTER ACT ARCHITECTURE

### §3121 — General Prohibition

**Core prohibition:** No person may install or use a pen register or a trap and trace
device without first obtaining a court order under §3122(b) or §3123 — OR the
consent of the user.

**Criminal penalties:** Knowingly violating §3121 is punishable by imprisonment for
up to one year and/or a fine.

**No civil damages provision:** Unlike the Wiretap Act (§2520 — $10,000 minimum civil
damages) or the SCA (§2707 — $1,000 minimum civil damages), the Pen Register Act
does NOT have a private civil right of action. Violations are criminal offenses
enforced by the government.

### §3127 — Definitions

**"Pen register" (§3127(3)):** A device or process which records or decodes dialing,
routing, addressing, or signaling information transmitted by an instrument or facility
from which a wire or electronic communication is transmitted, excluding the contents
of a communication.

**"Trap and trace device" (§3127(4)):** A device or process which captures incoming
electronic or other impulses which identify the originating number or other dialing,
routing, addressing, and signaling information reasonably likely to identify the source
of a wire or electronic communication — excluding content.

**Key distinction — metadata vs. content:**
The Pen Register Act covers routing information (who called whom, when, for how long,
from what number) but NOT the content of communications. Content is protected by the
Wiretap Act (§2511) if in transit, or the SCA (§2701) if stored.

### The ECPA Three-Title Structure

| Title | Statute | Covers | Civil Remedy |
|-------|---------|--------|-------------|
| I | §§2510-2522 (Wiretap Act) | Communication content — real-time interception | §2520: $10,000/violation min |
| II | §§2701-2712 (SCA) | Communication content — stored | §2707: $1,000/violation min |
| III | §§3121-3127 (Pen Register Act) | Routing metadata — who called whom | No civil damages |

## WHY THE PEN REGISTER ACT MATTERS FOR SIM SWAP

### No Direct Civil Claim — But Significant Evidence Value

Because the Pen Register Act has no private civil right of action, it does not create
a direct damages claim. However, it matters in three ways for SIM swap litigation:

**1. Evidence preservation:**
Pen register data (call logs, routing records) is exactly the kind of carrier metadata
that documents the SIM swap attack. Call logs showing calls to the victim's number
being answered at the attacker's location = evidence of the SIM swap in operation.
The carrier (AT&T) is legally required to preserve this data under various statutes
and carrier data retention policies.

**2. Criminal prosecution support:**
A SIM swap that installs an unauthorized pen register (redirecting call routing to
attacker's device) may be prosecutable under §3121. While the government, not the
victim, must bring this claim, the criminal violation strengthens the civil damages
picture.

**3. Civil discovery:**
In civil litigation, call records and routing data obtainable through §2703 (SCA
government process) or civil discovery subpoenas are the most direct evidence of:
- Which calls were intercepted (routed to attacker's SIM)
- When the SIM swap was active
- How many violations occurred (for per-violation damages calculation under §2511/CIPA)

### SIM Swap as an Unauthorized Pen Register

A SIM swap attack functionally installs an unauthorized pen register on the victim's
phone number: incoming calls are routed to the attacker's device, and the attacker
can observe all routing information (who is calling, from where) without the caller's
knowledge.

This is §3121 violation territory even if the underlying content interception theory
rests primarily on §2511 and CIPA. The criminal violation of §3121 by the SIM swap
attack strengthens the overall legal theory of the attack's illegality.

### Call Records as Civil Evidence

To calculate per-violation damages under §2511 ($10,000/event) and CIPA §632.7
($5,000/event), the plaintiff must identify the specific communication events that
were intercepted. Call records are the primary evidence for this:

- AT&T call logs showing calls to Michael's number during the SIM swap period
- Duration of SIM swap (how many days/weeks the hijack was active)
- Volume of calls/SMS messages during the attack period

These records are obtainable through civil subpoena to AT&T under SCA §2703(c)
(with proper civil process — not just government subpoena).

## PRACTICAL SIGNIFICANCE — NO CIVIL DAMAGES BUT HIGH EVIDENCE VALUE

The Pen Register Act's primary value in the Hartmann matter is:
1. Establishing the legal framework for why call log evidence is relevant
2. Supporting the criminal violation characterization of the SIM swap attack
3. Framing the civil subpoena for AT&T call records (the metadata documents the attack)

The civil damages claims run through §2511, §2701, CIPA, and CFAA — not §3121.
