# In re Application for Pen Register — URL Content Controversy

**Note:** This entry documents the split in federal courts about whether URLs constitute
"content" (Wiretap Act) or "routing information" (Pen Register Act) — a critical
distinction for SIM swap evidence law. Rather than a single case, this documents the
judicial debate.

**Relevant cases in the debate:**
- In re Application for Pen Register and Trap/Trace Device with Cell Site Location Authority, 396 F. Supp. 2d 747 (S.D. Tex. 2005)
- United States v. Forrester, 512 F.3d 500 (9th Cir. 2008)
- DOJ Guidelines on Pen Registers and Trap and Trace Devices

**Type:** Judicial debate documentation (not a single final holding)

## The Core Question

When a person accesses a website, the routing information includes:
- The IP address of the server
- The URL of the page requested (e.g., "https://www.ssa.gov/disability/claim-status")

**The question:** Is the URL "routing information" (Pen Register Act) or "content"
(Wiretap Act/SCA)?

**Why it matters for SIM swap:**
If the attacker (after gaining access to Michael's phone number and accounts) accessed
sensitive URLs (SSA disability portal, financial account pages), those URL access records
may constitute Wiretap Act content — not just Pen Register metadata.

## United States v. Forrester (9th Cir. 2008)

The Ninth Circuit held in Forrester that the government's surveillance of:
- IP addresses — routing information (pen register)
- Volume of email sent/received — routing information (pen register)
- "To/from" addresses of emails — routing information (pen register)

**But the court noted:** URL paths that identify specific pages visited may be more
content-like than routing-like. The court declined to resolve the URL issue definitively.

## The DOJ Position

The DOJ's internal guidelines (published in the Electronic Surveillance Manual) distinguish:
- IP address + port number = pen register (routing information)
- URL including path (e.g., /my-account/disability-status) = potentially content

## Significance for SIM Swap Civil Claims

**For evidence collection:** When subpoenaing AT&T call records and carrier logs
documenting the SIM swap, the plaintiff should categorize what is sought:
- Call routing logs (numbers called/received, duration, timestamps) = pen register data
- Content of calls/SMS = Wiretap Act content (requires warrant for government; civil
  subpoena for plaintiff)
- Account access logs (URLs visited while using hijacked credentials) = potentially
  Wiretap Act content — higher protection, stronger damages claim

**For damages theory:** If the attacker accessed SSA disability portal URLs while using
Michael's intercepted credentials, those URL accesses may constitute Wiretap Act
content interceptions (§2511 violations, $10,000/event) in addition to SCA stored
communications access (§2701, $1,000/event).

## Verification Note

United States v. Forrester at 512 F.3d 500 (9th Cir. 2008) — verify before use in
filed documents. The URL content debate continues; research current Ninth Circuit
position before citing in California federal court.
