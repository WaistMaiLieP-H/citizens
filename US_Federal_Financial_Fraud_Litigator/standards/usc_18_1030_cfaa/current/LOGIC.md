# 18 U.S.C. §1030 — Computer Fraud and Abuse Act (CFAA)
## Current Operative Architecture

### RULE

The CFAA criminalizes unauthorized access to computers and computer systems and provides
a civil cause of action for certain violations. It is the primary federal statute
governing computer intrusion, unauthorized data access, and computer-based fraud.

**Civil action provision — §1030(g):**
"Any person who suffers damage or loss by reason of a violation of this section may
maintain a civil action against the violator to obtain compensatory damages and injunctive
relief or other equitable relief."

**Private action limitation:** A civil action under §1030(g) requires that the conduct
involved:
- One of the factors described in §1030(c)(4)(A)(i) — i.e., the conduct caused:
  (I) loss to one or more persons during any 1-year period aggregating at least $5,000,
  (II) modification or impairment of medical records,
  (III) physical injury to any person,
  (IV) threat to public health or safety,
  (V) damage affecting a government computer used in the administration of justice,
      national defense, or national security, OR
  (VI) damage affecting 10 or more protected computers.

For most civil cases: the **$5,000 loss aggregation** threshold in factor (I) is the
operative requirement.

**SOL:** §1030(g) — civil action must be brought within 2 years from the date the
complainant first discovered or had reason to discover the violation.

### KEY DEFINITIONS

**"Protected computer" (§1030(e)(2)):**
A computer (A) exclusively for use of a financial institution or the United States
government, OR (B) used in or affecting interstate or foreign commerce or communication.
This definition is effectively universal in the internet era — any computer connected
to the internet affects interstate commerce.

**"Unauthorized access" — post-Van Buren (2021):**
After Van Buren v. United States, 593 U.S. 374 (2021), "exceeds authorized access"
means accessing portions of a computer that the user was not permitted to access —
i.e., going beyond the scope of one's authorization. It does NOT cover using
authorized access for unauthorized purposes. Someone with account credentials who
accesses their own account for the "wrong" purpose does not exceed authorized access.

**"Without authorization" (§1030(e)(6)):**
Accessing a computer without authorization means accessing it when you have no
permission to do so at all — not merely misusing otherwise permitted access.

**"Damage" (§1030(e)(8)):**
Impairment to the integrity or availability of data, a program, a system, or
information. Includes destruction, disruption, or corruption.

**"Loss" (§1030(e)(11)):**
Any reasonable cost to any victim, including the cost of responding to an offense,
conducting a damage assessment, restoring data, programs, systems, or information to
their condition prior to the offense, and any revenue lost, cost incurred, or other
consequential damages incurred because of interruption of service.

### PRIMARY CRIMINAL PROVISIONS RELEVANT TO CFAA CIVIL CLAIMS

**§1030(a)(2) — Unauthorized access to obtain information:**
Intentionally accesses a computer without authorization and obtains information from
a protected computer. Punishable as misdemeanor or felony depending on circumstances.

**§1030(a)(4) — Computer fraud:**
Knowingly and with intent to defraud, accesses a protected computer without authorization
and by means of such conduct furthers the fraud and obtains anything of value.

**§1030(a)(5) — Damage:**
Knowingly causes the transmission of a program, information, code, or command, and
as a result of such conduct, intentionally causes damage without authorization.

### SIM SWAP / COMMUNICATIONS FRAUD APPLICATION

**SIM swap as CFAA violation:**

A SIM swap attack transfers a victim's phone number from their SIM card to an
attacker's SIM card, giving the attacker control over the victim's phone number.
This is accomplished by:
1. Social engineering the carrier (AT&T, Verizon) to port the number
2. Using the ported number to bypass 2FA (two-factor authentication) on accounts
3. Accessing financial accounts, email, and other accounts using the ported number

**CFAA analysis of SIM swap:**

**§1030(a)(2) — Unauthorized information access:**
The attacker uses the ported phone number to access accounts (email, financial,
government portals) that the victim owns. The attacker does not have authorization
to access these accounts. Each account access = a separate §1030(a)(2) violation.

**§1030(a)(4) — Computer fraud:**
If the unauthorized access furthers fraud (e.g., using the account access to change
benefit addresses, intercept financial communications, redirect government mail) =
computer fraud.

**"Loss" for $5,000 threshold:**
For the civil §1030(g) claim, "loss" includes:
- Cost of securing accounts after SIM swap discovery
- Cost of identity theft recovery
- Value of benefits intercepted or denied as a result of the access
- Cost of professional assistance (credit monitoring, security services)
- Revenue lost or benefits denied due to communication interception

The $5,000 threshold is per 1-year period — aggregated across all victims of the
same actor. For a multi-year SIM swap/communications interception pattern (2018 onward),
the aggregated losses across multiple years and accounts substantially exceed $5,000.

**Ryan McClaran CFAA theory:**
If Ryan McClaran orchestrated the SIM swap and digital surveillance infrastructure:
- Each unauthorized access to Michael's accounts = §1030(a)(2) violation
- Each access that furthered financial fraud (disability denial, benefits interception,
  property fraud) = §1030(a)(4) violation
- §1030(g) civil action: compensatory damages + injunctive relief + equitable relief

**Civil damages calculation:**
- SSA/DDS disability benefit denial caused by communications interception: monthly
  benefit × months denied
- Financial account access losses
- Cost of communications security restoration
- Cost of identity theft remediation
- RICO cross-claim: each §1030(a)(4) violation is a wire fraud predicate (§1343) which
  is a RICO predicate (§1961(1)(B)) — see RICO standard

### AT&T CARRIER LIABILITY — SEPARATE THEORY

The SIM swap required AT&T (the carrier) to port the number to the attacker's SIM.
AT&T's internal systems are "protected computers" under §1030(e)(2). The attacker's
social engineering of AT&T staff to execute the unauthorized port = obtaining access
to AT&T's systems "without authorization" to accomplish the fraud.

**AT&T's liability is NOT under CFAA** (AT&T is the victim of the social engineering,
not the perpetrator). AT&T's separate liability for negligent authentication, negligent
SIM porting, and failure to implement reasonable verification = tort and contract claims,
not CFAA.

AT&T may face:
- Negligence (failure to verify identity before porting)
- California CIPA (Cal. Penal Code §632) if AT&T facilitated wiretapping
- FCC regulatory violations (CPNI rules — Customer Proprietary Network Information)

### LIMITS AFTER VAN BUREN

**Van Buren (2021) narrowing:**
Van Buren held that §1030(a)(2)'s "exceeds authorized access" provision does not cover
misuse of authorized access. A police officer who had authorized access to a license
plate database but accessed it for a bribe did not "exceed authorized access."

**Impact on SIM swap claims:**
Van Buren does not affect the SIM swap theory because the attacker had NO authorization
to access Michael's accounts — they were not authorized users who misused their access.
They were completely unauthorized users. Van Buren's limitation applies to authorized
users who misuse their access; it does not protect completely unauthorized intruders.

**Impact on insider-threat theories:**
If any authorized insider at a carrier, government agency, or financial institution
provided account information or access as part of the conspiracy, Van Buren limits the
CFAA theory against that insider — their authorized access + misuse ≠ "exceeds
authorized access" after Van Buren. The CFAA claim against the insider would need to
be framed as the insider acting "without authorization" (not merely "exceeding"
authorized access) — which requires showing the access was completely outside any
permission granted.

### §1030 vs. ECPA / WIRETAP ACT

The Electronic Communications Privacy Act (18 U.S.C. §2511 et seq.) — Wiretap Act —
is the parallel statute for interception of electronic communications. CFAA covers
computer access; Wiretap Act covers interception of communications in transit.

For SIM swap and communications interception:
- Accessing stored accounts (email, voicemail, cloud storage) = CFAA
- Intercepting live communications (calls, messages in transit) = Wiretap Act
- Both may apply to the same underlying conduct

**§2520 civil remedy under Wiretap Act:**
Civil action for each violation: $100/day or $10,000 minimum, whichever is greater +
attorneys' fees. SOL: 2 years.

### SOL

§1030(g): 2 years from when the complainant first discovered or had reason to discover
the violation.

For a multi-year SIM swap campaign (2018 onward), each new unauthorized access is a
fresh violation — the SOL for each access runs separately. The SOL does not run on
the entire course of conduct from the first access; each intrusion event is a separate
cause of action.
