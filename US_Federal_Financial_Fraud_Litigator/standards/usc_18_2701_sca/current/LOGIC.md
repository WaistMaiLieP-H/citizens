# Current Rule — 18 U.S.C. §§2701-2712 (Stored Communications Act)

## THE WOUND

When Congress enacted the Electronic Communications Privacy Act (ECPA) in 1986, it
distinguished two types of communications violations:

1. **Title I (§§2510-2522 — Wiretap Act):** Real-time interception of communications
   in transit — the wire is tapped as the communication flows through it. High penalty;
   strict prohibition.

2. **Title II (§§2701-2712 — Stored Communications Act):** Access to stored
   communications — voicemail waiting to be retrieved, email sitting on a server,
   account records held by a service provider. Lower penalty; government subpoena
   procedures.

The wound the SCA addressed: the developing ecosystem of electronic communications
storage. By 1986, voicemail systems, early email, and bulletin board services were
storing communications after transmission. These stored communications existed in a
legal gray zone: they were not "in transit" (so Wiretap Act didn't clearly cover them),
but they also contained private communications content (so users expected privacy).

Congress created a framework: stored communications held by service providers require
government process (search warrant, court order, or subpoena depending on type and age)
before law enforcement access, and unauthorized access by private actors is prohibited.

## THE SCA ARCHITECTURE — CIVIL PLAINTIFF PERSPECTIVE

### §2701 — Unlawful Access to Stored Communications

**Core prohibition:** Whoever intentionally accesses without authorization a facility
through which an electronic communication service is provided, OR intentionally
exceeds an authorization to access that facility, and thereby obtains, alters, or
prevents authorized access to an electronic communication while it is in electronic
storage in such system shall be punished...

**Key elements:**
1. Intentional
2. Without authorization (or exceeding authorization)
3. Access to a "facility" providing electronic communication service
4. Obtains, alters, or prevents access to electronic communications
5. While in "electronic storage"

**"Electronic storage" (§2510(17)):**
Any temporary, intermediate storage of a wire or electronic communication incidental
to the electronic transmission thereof; AND any storage of such communication by an
electronic communication service for purposes of backup protection.

### §2707 — Civil Action

Any provider of electronic communication service, subscriber, or other person aggrieved
by any violation of §2701 may, in a civil action, recover:

- **The sum of:** actual damages sustained plus any profits made by the violator as a
  result of the violation; AND
- **Statutory damages:** not less than $1,000 per violation (if actual damages are less)
- **Punitive damages** in appropriate cases
- **Attorney's fees and other litigation costs**

**Important distinction from §2520 (Wiretap Act):**
- §2520 (Wiretap Act): minimum $10,000 per violation (or $100/day)
- §2707 (SCA): minimum $1,000 per violation

The SCA minimum is lower, but the SCA covers a different category of conduct (stored
vs. in-transit), so the claims are additive, not alternatives.

### The Wiretap Act / SCA Boundary

**Critical distinction for SIM swap claims:**

| Category | Governing Statute | Minimum Civil Damages |
|----------|------------------|----------------------|
| Real-time interception (SIM swap routing calls to attacker's phone) | §2511 Wiretap Act | $10,000/violation |
| Accessing stored voicemail, email, text messages | §2701 SCA | $1,000/violation |
| Accessing account records (call logs, subscriber info) | §2703 (government subpoena) / §2707 (civil) | $1,000/violation |

The SIM swap attack combines both categories:
- During the active SIM swap: calls and messages are intercepted in real-time = §2511
- After the SIM swap: attacker accesses stored voicemails, email accounts, stored texts = §2701
- Account takeovers (accessing email accounts, financial account histories stored on servers): §2701

### §2703 — Required Disclosure of Customer Communications or Records

This provision governs government access to stored communications and records. It
establishes the warrant/subpoena framework. For civil plaintiffs, §2703 is relevant
because it defines what records service providers hold and establishes the categories
of information at issue:

- **§2703(a):** Contents of electronic communications in storage >180 days: government
  subpoena with notice; or warrant
- **§2703(b):** Contents of wire or electronic communications in storage >180 days:
  court order or consent; or warrant
- **§2703(c):** Customer records (subscriber info, billing records, IP connection logs,
  session times): subpoena; court order; or warrant

Civil plaintiffs do not use §2703 directly to obtain their own records (that is handled
by §2707 and other discovery mechanisms), but §2703 defines the categories of information
service providers are required to preserve and disclose under government process.

## SIM SWAP APPLICATION — SCA ANALYSIS

### Theory

The SIM swap attack chain involves multiple SCA violations:

**Phase 1 — Account takeover using intercepted authentication:**
Using intercepted 2FA codes (obtained via SIM swap §2511 interception), the attacker
gains access to email accounts, financial accounts, and other services. Once access is
obtained, the attacker reviews stored emails, messages, account history = accessing
stored electronic communications = §2701 violation.

**Phase 2 — Voicemail interception:**
Incoming calls diverted to attacker's phone may reach the attacker's voicemail.
Listening to voicemails left for the victim = accessing stored voice communications =
§2701 violation per voicemail.

**Phase 3 — Account history review:**
The attacker and co-conspirators who gain access to accounts review stored account
records, communications histories, and subscriber information = §2701 violation per
access event.

### Defendants

- **Ryan McClaran (primary):** §2701 violations for each instance of accessing Michael's
  stored email, voicemail, account content, and financial records
- **Co-conspirators:** Each person who accessed stored communications or account content
  using credentials obtained through the SIM swap = §2701 violations
- **At&T (carrier liability):** If AT&T improperly processed the SIM swap request, AT&T
  may have enabled unauthorized access to stored communications services = §2701 theory
  for carrier (more complex; primary AT&T theory is negligence/UCL)

### Damages Calculation

**Per stored communication accessed:** $1,000 minimum
**Per stored voicemail accessed:** $1,000 minimum
**Account history review sessions:** Each session = separate access event

For accounts with months of stored communications reviewed during the attack period:
- Email account (thousands of stored emails reviewed) — substantial per-email access
  count or aggregated to one "access to facility" violation per session
- Financial account statements and records
- SSA/DDS account portals storing communications about disability claims

**Aggregation with §2511 claims:**
Each real-time call intercept: $10,000 (federal) + $5,000 (CIPA state)
Each stored communication access: $1,000 (SCA §2707) + CFAA if $5,000 aggregate loss

### Two-Year Statute of Limitations

Two-year SOL from discovery (§2707(f)). Each access event is a separate violation
with its own SOL from when plaintiff knew or should have known of the access.

## THE ECPA STRUCTURE — THREE TITLES

The full ECPA framework:
- **Title I — §§2510-2522 (Wiretap Act):** Real-time interception in transit
- **Title II — §§2701-2712 (SCA):** Stored communications at rest
- **Title III — §§3121-3127 (Pen Register Act):** Non-content routing information (phone numbers dialed, IP addresses connected to)

For SIM swap claims: Titles I and II both apply. Title III (pen register) covers
metadata and may be relevant for call log records.
