# Smith v. Maryland — Holding

**Citation:** Smith v. Maryland, 442 U.S. 735 (1979)
**Court:** Supreme Court of the United States
**Decided:** June 20, 1979
**Author:** Blackmun, J.

## Facts

The Baltimore Police Department asked telephone company Maryland to install a pen
register at its central offices to record the numbers dialed from Michael Lee Smith's
home telephone. Smith had been making threatening calls to Patricia McDonough, who
had reported the calls and provided Smith's license plate number. The pen register
was installed without a warrant. The results showed Smith had called McDonough.
Smith was convicted of robbery and moved to suppress, arguing the warrantless
pen register violated his Fourth Amendment rights.

## Holding

**The installation of a pen register to record the telephone numbers dialed from a
subscriber's phone does not constitute a "search" under the Fourth Amendment — no
warrant is required.**

The Court applied the two-part Katz reasonable expectation of privacy test:
1. Did the defendant have a subjective expectation of privacy?
2. Is that expectation one that society is prepared to recognize as "reasonable"?

The Court held that a telephone subscriber has no reasonable expectation of privacy
in the numbers they dial. When a person dials a number, they "voluntarily convey"
that number to the telephone company by the act of dialing. The telephone company
routinely records this information for billing and other purposes. The subscriber
assumes the risk that the telephone company will reveal the numbers to law enforcement.

## Rules Distilled

1. **No Fourth Amendment protection for dialed numbers:** The numbers a person dials
   are not constitutionally protected — no warrant required for government to obtain
   them via pen register
2. **Voluntary conveyance to third party = no expectation:** When you dial a number,
   you convey it to the carrier; no reasonable expectation of privacy in what you
   expose to third parties
3. **Content vs. metadata distinction:** The Fourth Amendment protects the content of
   a phone call (Katz) but not the routing information (Smith) — a fundamental distinction
   in surveillance law
4. **Broader third-party doctrine:** Smith is a key pillar of the third-party doctrine:
   information voluntarily shared with a third party (even a carrier) loses constitutional protection

## Limitations and Subsequent Development

**Carpenter v. United States, 585 U.S. 296 (2018):**
The Supreme Court held that the government must obtain a warrant to access historical
cell-site location information (CSLI) from carriers — because location data provides
a "detailed chronicle" of a person's movements over time. The Court narrowed the
third-party doctrine for comprehensive surveillance, though Smith itself was not overruled.

**Significance:** For SIM swap victims, Carpenter's logic potentially extends to other
comprehensive metadata surveillance. A SIM swap attack that routes all of a victim's
calls creates the functional equivalent of long-term location/contact monitoring.

## Why Smith Matters for SIM Swap Civil Claims

Smith is the constitutional backdrop that explains why the Pen Register Act (§§3121-3127)
has no civil damages provision:

Congress chose to protect pen register metadata only at a statutory level (no civil
remedy) — reflecting the Supreme Court's ruling that the Constitution doesn't protect
this information. The gap in civil remedies for metadata is the direct result of Smith.

**For civil litigation:** The absence of a §3121 civil claim does not mean metadata
is unimportant. Call records are critical evidence for:
- Proving the SIM swap was active (routing anomalies show calls diverted to attacker)
- Quantifying the number of violations (per-event damages under §2511/CIPA)
- Establishing the timeline of the attack

## Verification Note

Smith v. Maryland at 442 U.S. 735 — verify before use in filed documents.
