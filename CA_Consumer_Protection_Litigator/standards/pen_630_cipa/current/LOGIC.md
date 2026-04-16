# Current Rule — Cal. Penal Code §§630-638 (California Invasion of Privacy Act — CIPA)

## THE WOUND

California enacted the Invasion of Privacy Act in 1967 because telephone wiretapping
was widespread — by businesses, by spouses in divorce proceedings, by private
investigators, and by law enforcement operating without the constraints of the
contemporaneous federal Title III. California's Legislature found that "advances in
science and technology have led to the development of new devices and techniques for
the purpose of eavesdropping upon private communications."

The core wound was the asymmetry of information: parties to conversations were unaware
they were being recorded. Unlike the federal Wiretap Act (which adopted a one-party
consent rule), California took a stronger position: all parties to a confidential
communication must consent to its recording. This made California law significantly
broader than federal law.

The second wound the statute addressed was technological: as communication technology
evolved (cellular phones, cordless phones, electronic communications, internet-based
communications), each evolution created a gap that required amendment.

## DESIGN RESPONSE — CIPA ARCHITECTURE

### §630 — Legislative Findings and Purpose

§630 declares: "The Legislature hereby declares that advances in science and technology
have led to the development of new devices and techniques for the purpose of
eavesdropping upon private communications and that the invasion of privacy resulting
from the continual and increasing use of such devices and techniques has created a
serious threat to the free exercise of personal liberties."

The provision states the purpose: protect the right of privacy by prohibiting
eavesdropping and recording of confidential communications without the consent of
all parties.

### §631 — Wiretapping Prohibition

**Core prohibition:** Any person who, by means of any machine, instrument, or contrivance,
or in any other manner:
1. Intentionally taps, or makes any unauthorized connection with any telegraph or
   telephone wire, line, cable, or instrument, including the wire, line, cable, or
   instrument of any internal telephonic communication system; OR
2. Willfully and without the consent of all parties to the communication, or in any
   unauthorized manner, reads, or attempts to read, or to learn the contents or meaning
   of any message, report, or communication while the same is in transit or passing
   over any wire, line, or cable, or is being sent from, or received at any place within
   this state; OR
3. Uses, or attempts to use, in any manner, or for any purpose, or to communicate to
   others, any information so obtained

...is guilty of a public offense and subject to criminal penalties and civil liability.

**Civil remedy — §637.2:**
Any person who has been injured by a violation of CIPA may bring a civil action
for the greater of:
- Actual damages; OR
- **$5,000 per violation**

Plus three times actual damages if the court so awards (discretionary trebling).

**All-party consent:** Unlike the federal Wiretap Act's one-party consent rule,
California requires consent of ALL parties to a confidential communication for lawful
recording. One-party consent (e.g., recording your own phone call without telling the
other party) is permissible under federal law but violates CIPA if the communication
is "confidential."

### §632 — Confidential Communications by Electronic Amplifying or Recording Device

§632 addresses use of electronic devices (as distinct from wire interception):

Any person who, intentionally and without the consent of all parties to a confidential
communication, uses an electronic amplifying or recording device to eavesdrop upon or
record the confidential communication, whether the communication is carried on among
the parties in the presence of one another or by means of a telegraph, telephone, or
other device, except radio communications, shall be punished by imprisonment...

**"Confidential communication" definition (§632(c)):**
Any communication carried on in circumstances as may reasonably indicate that any
party to the communication desires it to be confined to the parties thereto, but
excludes a communication made in a public gathering or in any legislative, judicial,
executive or administrative proceeding open to the public, or in any other circumstance
in which the parties to the communication may reasonably expect that the communication
may be overheard or recorded.

**Key principle:** The test is reasonable expectation of confidentiality — not whether
the communication was in fact private, but whether the circumstances would reasonably
lead the parties to believe it was intended to be private.

### §632.7 — Cellular and Cordless Phone Calls

§632.7 (added 1992) prohibits intentional interception of communications transmitted
between cellular radio telephones, cordless phones, or any combination of the above.
This provision does not require that the communication be "confidential" — any
interception of cellular or cordless calls without consent of all parties is prohibited.

### §637.2 — Civil Remedy

Any person who has been injured by a violation of §631, §632, §632.5, §632.6, §632.7,
§§634-637 may bring a civil action for:
- The greater of actual damages or $5,000 per violation; AND/OR
- A civil penalty of three times the amount of actual damages (discretionary)

**No actual damages required:** The $5,000 floor means CIPA claims have minimum per-
violation value even when actual damages are difficult to quantify. Each separate
interception event is a separate violation.

## SIM SWAP APPLICATION — CIPA ANALYSIS

### The Theory

A SIM swap attack routes all incoming calls and SMS messages to the attacker's device
by hijacking the victim's phone number. Under CIPA:

**§632.7 violation:** The interception of cellular calls and SMS messages routed via
SIM swap = intentional interception of cellular communications without consent of
all parties (victim + all parties communicating with victim). Each call/message
intercepted = separate $5,000 minimum violation.

**§631 violation:** Reading the contents of communications "while the same is in
transit" = the real-time interception of messages and calls during SIM swap active
period. Each intercepted communication = separate violation.

**No confidentiality requirement for §632.7:** Unlike §632 (which requires the
communication to be "confidential"), §632.7 covers any cellular communication —
the SIM swap victim does not need to prove confidentiality of each specific call.

### California All-Party Consent vs. Federal One-Party Consent

Ryan McClaran's SIM swap interception violates both:
- Federal §2511 (one-party consent standard still met because McClaran was not a
  party to the communications he intercepted; he was a third-party interceptor)
- California §632.7/§631 (all-party consent: both the caller and Michael needed to
  consent; neither did)

The California all-party consent rule is more favorable to plaintiffs than federal law
because it eliminates any argument that McClaran's interception was "consensual" on
the theory that he was operating a device (the cloned SIM) as if he were a party.

### Disclosure Chain — §631(b)

§631(b) prohibits use or disclosure of information obtained through unlawful interception.
Each person who received intercepted communications from McClaran and used them =
separate §631(b) violation = separate $5,000 minimum.

Applied to the facts: Christina Cerretani and others who received and acted on
information from intercepted communications = §631(b) disclosure liability stacked
with the interception violations.

### Damages Stacking — CIPA + Federal

| Violation | Per-Event Federal Minimum | Per-Event California Minimum |
|-----------|--------------------------|------------------------------|
| Interception (SIM swap) | $10,000 (§2520) | $5,000 (§637.2) |
| Disclosure (using intercepted content) | $10,000 (§2520) | $5,000 (§637.2) |
| **Both track simultaneously** | **$10,000 federal** | **$5,000 California** |

Note: Federal and California remedies can run simultaneously — total minimum per
interception event is $10,000 federal + $5,000 California = $15,000 minimum per event.
(Actual/punitive damages on top; federal also provides mandatory attorneys' fees.)

### Two-Year Statute of Limitations

Cal. Code Civ. Proc. §335.1 (2-year general tort) applies to CIPA civil claims.
Each interception event is a separate violation with its own 2-year SOL from discovery.
The SIM swap fraud was ongoing from approximately 2018 forward; discovery rule tolling
applies for the period Michael had no reason to know his communications were intercepted.

## THE BROADER CIPA FRAMEWORK (FULL CHAPTER 1.5)

CIPA Chapter 1.5 (§§630-638) covers:
- §630: Legislative findings
- §631: Wiretapping (telephone/telegraph lines)
- §632: Electronic amplifying/recording devices (confidential communications)
- §632.5: Cordless telephone interception (added 1985)
- §632.6: Cellular telephone interception (added 1985)
- §632.7: Combined cellular/cordless (added 1992; current primary mobile provision)
- §633: Law enforcement exemption
- §633.5: Exception for victims recording threats
- §633.8: Exception for domestic violence victims
- §634: Eavesdropping devices prohibition
- §636: Court proceeding recording
- §636.5: Radio communication by emergency services
- §637: Disclosure of telegrams
- §637.2: Civil remedy
- §637.5: Cable/satellite subscriber data (pre-dating federal SCA)

The core provisions for SIM swap civil claims are §§631, 632.7, and 637.2.
