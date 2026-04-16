# 18 U.S.C. §2511 — Electronic Communications Privacy Act / Wiretap Act
## Current Operative Architecture

### RULE

Title I of the Electronic Communications Privacy Act (ECPA), 18 U.S.C. §§2510-2522
(the Wiretap Act), prohibits the intentional interception of wire, oral, or electronic
communications. It provides a civil cause of action for any person whose communications
are intercepted, disclosed, or used in violation of the Act.

**Prohibition — §2511(1)(a):**
"[A]ny person who ... intentionally intercepts, endeavors to intercept, or procures any
other person to intercept or endeavor to intercept, any wire, oral, or electronic
communication ... shall be punished as provided in subsection (4) or shall be subject
to suit as provided in subsection (5)."

**Civil cause of action — §2520(a):**
"[A]ny person whose wire, oral, or electronic communication is intercepted, disclosed,
or intentionally used in violation of this chapter may in a civil action recover from
the person or entity, other than the United States, which engaged in that violation such
relief as may be appropriate."

**Damages — §2520(b) and (c):**
The court may award:
(1) Equitable or declaratory relief
(2) Damages — the greater of:
    (a) Actual damages + profits made by violator, OR
    (b) Statutory damages of whichever is the greater of $100/day or $10,000
(3) Punitive damages (in appropriate cases)
(4) Reasonable attorneys' fees + costs

**Minimum:** $10,000 per violation (or $100/day, whichever is greater) regardless of
actual damages. For a multi-year interception campaign, statutory damages can be
substantial: $10,000 per intercepted call/message × number of intercepts.

**SOL — §2520(e):** 2 years from the date the claimant first has a reasonable
opportunity to discover the violation.

### KEY DEFINITIONS

**"Wire communication" (§2510(1)):** Any aural transfer (voice) carried by wire or
similar connection with the aid of electronic storage; includes telephone calls.

**"Electronic communication" (§2510(12)):** Any transfer of signs, signals, writing,
images, sounds, data, or intelligence of any nature transmitted by wire, radio, or
electromagnetic system — includes email, text messages, internet communications.

**"Intercept" (§2510(4)):** The aural or other acquisition of the contents of any wire,
electronic, or oral communication through the use of any electronic, mechanical, or
other device. Critically: interception occurs at the moment of acquisition during
transmission — i.e., real-time capture of a communication while it is in transit.

**The transmission/storage distinction (critical):**
The Wiretap Act covers interception *during transmission*. Stored communications (email
in an inbox, voicemail stored on a server) are governed by the Stored Communications
Act (SCA, 18 U.S.C. §2701), not the Wiretap Act. This distinction matters for SIM swap:
- Live call intercepted by porting the number: Wiretap Act
- Voicemail accessed after storage on the carrier's server: Stored Communications Act
- Text messages in transit: Wiretap Act
- Text messages stored in an inbox: Stored Communications Act / CFAA

### SIM SWAP — WIRETAP ACT ANALYSIS

**How SIM swap enables interception:**

A SIM swap ports the victim's phone number to the attacker's SIM card. Once ported:
- Incoming calls to the victim's number ring on the attacker's phone
- SMS messages sent to the victim's number are received by the attacker
- Two-factor authentication codes sent to the victim's number go to the attacker
- Any person who dials the victim's number reaches the attacker

**Wiretap Act analysis:**

**§2511(1)(a) — Intentional interception:**
1. The attacker intentionally intercepted the victim's wire and electronic communications
   (incoming calls = wire communications; incoming SMS = electronic communications)
2. Interception occurred in transit: the call/SMS was routed to the attacker's SIM
   rather than the victim's — the interception happens during transmission
3. No consent: the victim did not consent to the interception; no service provider
   exception applies because the carrier was tricked into enabling the interception

**$10,000 minimum per violation:**
Each intercepted call, each intercepted text message = a separate violation.
For a communications campaign targeting disability benefits, financial accounts, and
legal proceedings over multiple years, the number of violations is large.

**§2520(c) statutory damages:**
If actual damages are difficult to prove, the $10,000 minimum per violation provides
a substantial floor. A court could award $10,000 per intercepted communication event.
For a multi-year SIM swap campaign: number of intercepted communications × $10,000
+ punitive damages + attorneys' fees.

**Provider exception (§2511(2)(a)(i)):**
A provider of wire or electronic communication service may intercept communications
to protect the rights or property of the provider. This exception does NOT apply to
AT&T's facilitation of a fraudulent SIM swap: AT&T did not intercept the communications
to protect its rights — it was deceived into porting the number, enabling a third party
to intercept.

### STORED COMMUNICATIONS ACT (SCA) — §2701 PARALLEL

For stored communications (voicemail on carrier server, email in inbox), the SCA
(18 U.S.C. §2701) governs:
- Civil action: §2707 — actual damages or $1,000 minimum + attorneys' fees + punitive
- SOL: 2 years

For SIM swap, the attacker who accesses stored voicemail through the hijacked number
violates both:
- SCA §2701 (accessing stored voicemail without authorization)
- CFAA §1030(a)(2) (accessing a protected computer without authorization)

Both civil remedies run simultaneously on the stored communications component.

### CALIFORNIA CIPA — STATE PARALLEL

California Penal Code §632 et seq. (CIPA — California Invasion of Privacy Act) provides
a parallel state law cause of action for interception and recording of communications
without all-party consent.

**§637.2 civil action:** Any person injured by a violation of CIPA may bring a civil
action for the greater of: $5,000 per violation OR three times the actual damages.

**CIPA + Wiretap Act stacking:**
Federal Wiretap Act: $10,000 minimum per violation + punitive + fees
California CIPA: $5,000 per violation or 3× actual damages

Both run on the same intercepted communication facts. Total exposure per intercepted
communication: $10,000 (federal) + $5,000 (state) + fees + punitive.

### CONSENT EXCEPTION ANALYSIS

The Wiretap Act has a one-party consent exception: if one party to the communication
consents to the interception, it is lawful (§2511(2)(d)). California is a two-party
(all-party) consent state for state CIPA purposes, but the federal one-party consent
standard governs Wiretap Act claims.

**SIM swap consent analysis:**
Neither Michael nor any legitimate caller consented to the SIM swap interception.
The attacker who ported the number is not a party to Michael's incoming calls —
they are a third-party interceptor. The one-party consent exception (which requires
a legitimate party to consent) does not apply to a non-party attacker.

### CARRIER LIABILITY ANALYSIS

**AT&T's exposure:**
AT&T's negligent porting process enabled the interception. But AT&T is not the
"intercetor" — the attacker is. AT&T's liability runs on:
- Negligence / negligence per se (FCC CPNI rules, 47 C.F.R. §64.2010 — customer
  authentication requirements before porting)
- State tort claims for enabling the fraud
- NOT Wiretap Act (AT&T did not "intercept" communications)

**FCC CPNI rules** require carriers to authenticate identity before porting a number
or disclosing account information. A carrier that ports a number without proper
authentication violates CPNI rules — creating a negligence per se theory in state court.
