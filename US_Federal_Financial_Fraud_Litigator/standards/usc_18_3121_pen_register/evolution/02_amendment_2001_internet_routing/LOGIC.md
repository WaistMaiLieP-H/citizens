# Evolution Stage 02 — 2001 PATRIOT Act: Internet Routing Information

### THE WOUND

The original 1986 Pen Register Act was written for telephone pen registers — physical
devices attached to telephone lines. By 2001, internet routing information (IP addresses,
email header data, URLs) was equally revealing metadata that was not clearly covered
by the original telephone-centric language.

The FBI's "Carnivore" system (later renamed DCS1000) had been deployed to capture
internet routing information from ISPs, creating controversy about whether this
required a pen register order.

### DESIGN RESPONSE — 2001

**USA PATRIOT Act, Pub. L. 107-56 (Oct. 26, 2001):**

**Expanded §3127 definitions:**
- "Pen register" was amended to cover "dialing, routing, addressing, or signaling
  information" — explicitly extending to internet routing (IP addresses, email headers)
- "Electronic communication" was added alongside "wire or electronic communication"
  to ensure coverage of internet-based communications

**Multi-district jurisdiction:**
The PATRIOT Act also expanded the jurisdiction of pen register orders — a single court
could authorize surveillance across multiple judicial districts.

**Effect on civil litigation:**
The PATRIOT Act expansion increased the scope of metadata covered but did not add a
civil damages remedy. The criminal-only enforcement structure was retained.

**Current coverage:** Under the post-PATRIOT Act framework, pen register orders cover:
- Telephone call routing (numbers dialed, numbers calling)
- Email header information (to/from/subject — not body content)
- IP address connection logs (who connected to what server, when)
- Website URL addresses (in some interpretations)

### SIGNIFICANCE FOR SIM SWAP CIVIL LITIGATION

**The post-PATRIOT Act definition matters for civil discovery:**
IP connection logs, email headers, and telephone call routing records are all pen register
data under the post-2001 definition. In civil discovery:
- Subpoenas to AT&T for call routing logs documenting the SIM swap period
- Subpoenas to email providers for IP connection logs showing account access by the attacker
- These records identify when the SIM swap was active and what communications/accounts were compromised

Even without a civil damages claim under §3121, the records preserved under the
pen register framework are available through civil discovery processes.

### PROVENANCE

USA PATRIOT Act, Pub. L. 107-56, §216 (Oct. 26, 2001)
Amended: 18 U.S.C. §§3121, 3123, 3127 (internet routing expansion)
