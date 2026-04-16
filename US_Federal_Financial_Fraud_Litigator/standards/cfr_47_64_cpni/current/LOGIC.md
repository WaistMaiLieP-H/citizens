# Current Rule — 47 C.F.R. §64.2010 and FCC CPNI Framework
## Customer Proprietary Network Information — Carrier Duty to Protect

## THE WOUND

When Congress enacted the Telecommunications Act of 1996, it recognized that telephone
carriers collect uniquely sensitive information about their customers: who they call,
when, how long, from where, and for what services they pay. This information —
Customer Proprietary Network Information (CPNI) — tells a detailed story about a
person's life, business relationships, health concerns (who they call), and movements.

Before the CPNI rules, carriers could use, share, and disclose this information broadly
without restriction. Carriers were selling CPNI to direct marketers, third-party service
providers, and others. There was no duty to protect CPNI from unauthorized access or
disclosure.

The second wound: SIM swapping and account takeover attacks directly exploit the
carrier's authentication and identity verification systems. A carrier that does not
adequately verify the identity of a person requesting a SIM port or account change
is the proximate cause of the attack — the carrier is the gatekeeper that failed.

## THE CPNI FRAMEWORK

### 47 U.S.C. §222 — Statutory Basis

Section 222 of the Telecommunications Act of 1996 creates the statutory CPNI duty:
carriers "shall protect the confidentiality of proprietary information of, and relating
to, other telecommunication carriers, equipment manufacturers, and customers, including
telecommunications carriers reselling telecommunications services provided by a
telecommunications carrier."

Specifically, §222(a) prohibits carriers from using, disclosing, or permitting access
to CPNI without customer consent, except in limited circumstances.

### 47 C.F.R. §64.2010 — Authentication Rules

The FCC's implementing rules (47 C.F.R. Part 64, Subpart U) establish specific
authentication requirements before carriers may release CPNI or make account changes.

**§64.2010(a) — Password authentication:**
Carriers must authenticate customers who call in to access CPNI or make account changes.
Authentication must use a password, shared secret, or similar mechanism. The
carrier cannot use "readily available biographical information" (last four of SSN,
date of birth, mother's maiden name) alone as authentication.

**§64.2010(b) — In-store authentication:**
For in-person requests, carriers must verify customer identity.

**SIM swap / number porting authentication:**
FCC CPNI orders (including the 2007 CPNI order and subsequent enforcement actions)
have addressed SIM swap specifically:
- Fraudulent SIM swaps and port-out scams are CPNI violations
- Carriers must implement safeguards against unauthorized number porting
- Failure to verify customer identity before porting = CPNI violation

### 47 C.F.R. §64.2001 — CPNI Defined

"Customer proprietary network information" means:
1. Information that relates to the quantity, technical configuration, type, destination,
   location, and amount of use of a telecommunications service subscribed to by any
   customer of a telecommunications carrier; AND
2. Information contained in the bills pertaining to telephone exchange service or
   telephone toll service received by a customer

**What is CPNI in a SIM swap:**
- The target's phone number (which calls came to it, what services were on it)
- Call records associated with the number
- Account information (service address, account PIN, linked devices)
- Authentication information (the very credentials the attacker is trying to steal)

### 47 C.F.R. §64.2011 — Notice of Breach

When unauthorized access to or disclosure of CPNI occurs, carriers must:
1. Notify the FBI and U.S. Secret Service within 7 business days
2. Notify affected customers after law enforcement notification period

**This creates an independent duty:** If AT&T processed the SIM swap knowing or
suspecting it was fraudulent, AT&T had an independent obligation to notify Michael
and federal law enforcement. Failure to provide that notice = additional CPNI violation.

### FCC Enforcement — Section 503(b)

FCC can impose civil forfeiture penalties up to $100,000 per violation/$1,000,000
per day of a continuing violation (47 U.S.C. §503(b)) for CPNI rule violations.
These are regulatory enforcement penalties, not private civil damages.

## CIVIL LIABILITY THEORY — CPNI AND SIM SWAP

### The Gap: No Private Right of Action Under §222

**Important limitation:** 47 U.S.C. §222 does not expressly create a private right
of action for CPNI violations. The enforcement mechanism is FCC regulatory proceedings.
There is no direct "sue AT&T under §222" civil claim.

However, CPNI violations create civil liability through multiple other paths:

### Path 1 — Negligence / Negligence Per Se

**AT&T's CPNI obligations create a duty of care.** Violation of a federal regulatory
standard is evidence of negligence, and in some jurisdictions creates a negligence per se
presumption.

Elements:
1. AT&T had a duty to protect Michael's CPNI (including his phone number / SIM assignment)
2. AT&T breached that duty by processing the fraudulent SIM swap without adequate
   authentication of the requesting party
3. The breach caused Michael's SIM to be hijacked
4. The hijacked SIM caused Michael's damages (intercepted communications, account access,
   financial fraud, disability claim interference)

**Negligence per se:** If AT&T violated 47 C.F.R. §64.2010's authentication requirements,
that regulatory violation establishes the standard of care for negligence purposes.

### Path 2 — Cal. Civil Code §1714 / California Negligence

California general negligence law (§1714) applies to AT&T's failure to protect
Michael's account. CPNI regulations define the specific duty; California negligence
law provides the civil remedy.

### Path 3 — UCL §17200 Unlawful Prong

AT&T's violation of 47 C.F.R. §64.2010 authentication requirements = "unlawful"
business practice under UCL §17200. UCL adds equitable relief (injunction, restitution)
to the negligence damages framework.

### Path 4 — FCC Complaint

A complaint to the FCC Consumer Complaint Center (consumer.ftc.gov equivalent) can
trigger FCC enforcement proceedings against AT&T for CPNI violations related to the
SIM swap. This is a regulatory path, not a civil damages path, but can be pursued
simultaneously with civil litigation.

## SIM SWAP CPNI ANALYSIS — SPECIFIC APPLICATION

**The AT&T SIM swap facts:**
1. Someone called AT&T (or went in-store) posing as Michael Hartmann
2. They requested a SIM swap — transfer of Michael's phone number to a new SIM/device
3. AT&T processed the request without adequate identity verification
4. AT&T's failure to verify was the direct cause of the SIM hijack

**FCC CPNI violations:**
- §64.2010: AT&T failed to authenticate the requesting party before making the
  account change (SIM swap)
- §64.2011: AT&T failed to notify Michael and federal law enforcement of the
  unauthorized CPNI access (the SIM swap itself = unauthorized account access)
- §64.2001: The phone number and account information used in the SIM swap = CPNI;
  AT&T disclosed it (by executing the port) to an unauthorized party

**Aggregate AT&T exposure:**
AT&T's SIM swap facilitation is the gateway to all subsequent harms:
- Intercepted communications ($10,000/event federal + $5,000/event California)
- Stored communications accessed ($1,000/event)
- Computer accounts accessed (§502, CFAA)
- Financial fraud
- Disability claim interference (months of blocked SSA access)

AT&T's negligence is a but-for cause of all downstream harms — making AT&T potentially
jointly and severally liable for the full damages package alongside McClaran and
co-conspirators.

## RECENT FCC ENFORCEMENT — SIM SWAP SPECIFIC

The FCC's 2023 action (FCC 23-67) specifically addressed SIM swap fraud, noting:
- SIM swap and port-out fraud are serious CPNI violations
- Carriers must implement additional safeguards including customer notification before
  SIM swaps, PIN/passcode requirements for port-outs, and SIM lock features
- The FCC was considering additional CPNI rules specifically targeting SIM swap fraud

**Post-2023 regulatory environment:** The FCC has specifically identified SIM swap as
a CPNI issue, strengthening the regulatory duty argument for incidents that occurred
during the active rule-development period.
