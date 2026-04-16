# WhatsApp Inc. v. NSO Group Technologies Ltd. — Holding

**Citation:** WhatsApp Inc. v. NSO Group Technologies Ltd., 17 F.4th 930 (9th Cir. 2021) (jurisdictional ruling); underlying civil complaint filed N.D. Cal. 2019
**Court:** United States Court of Appeals for the Ninth Circuit (jurisdictional ruling); Northern District of California (substantive claims)
**Status:** 9th Circuit affirmed subject matter jurisdiction 2021; remanded for further proceedings; §502 claims asserted in underlying complaint

## Facts

NSO Group Technologies, an Israeli cybersurveillance company, deployed its Pegasus
spyware through WhatsApp's servers. NSO's clients — government agencies and other
actors — used Pegasus to covertly surveil approximately 1,400 WhatsApp users by
exploiting a vulnerability in WhatsApp's video calling feature. The attack used
WhatsApp's own servers as a delivery mechanism: NSO's clients sent malicious code
through WhatsApp's infrastructure to install Pegasus on target devices.

WhatsApp sued NSO Group asserting violations of:
- 18 U.S.C. §1030 (CFAA) — unauthorized access to WhatsApp's computers
- Cal. Penal Code §502(c) — unauthorized access to California-based computer systems

The initial dispute was whether NSO Group could claim foreign sovereign immunity.

## 9th Circuit — Jurisdictional Ruling

The 9th Circuit (17 F.4th 930 (2021)) held that NSO Group was not entitled to
foreign sovereign immunity merely because it acted as a contractor for foreign
government clients. The case was remanded for resolution of the substantive claims.

## §502 and CFAA Claims

The complaint's §502 and CFAA theories are directly parallel:

**§502(c)(1):** NSO Group accessed WhatsApp's computer systems to execute a scheme
to defraud and wrongfully control data (user communications) — accessing WhatsApp's
California-based servers without permission to deliver malware

**§502(c)(7):** NSO Group accessed WhatsApp's computer systems "without permission"
by exploiting a software vulnerability — the access was never authorized by WhatsApp

**CFAA §1030(a)(2):** Same facts support unauthorized access to protected computers
affecting interstate commerce

## Rules Established for §502 Application

1. **State law parallel to CFAA:** Cal. P.C. §502 and 18 U.S.C. §1030 operate as
   parallel claims on the same facts; both are viable in federal court under supplemental
   jurisdiction
2. **Exploitation of vulnerability = without permission:** Using a software vulnerability
   to access a computer system that has not authorized that access method is "without
   permission" under §502 — even if the access path technically goes through the system's
   own infrastructure
3. **Malware delivery through victim's servers:** Using a victim's own servers as a
   delivery mechanism for an attack against third parties violates §502 — the server
   owner's permission covers normal operation, not exploitation
4. **No geographic limitation:** §502 applies when the attacked computer systems are
   in California, regardless of where the attacker is located (mirroring Kearney's
   CIPA extraterritoriality holding)

## Significance for SIM Swap Claims

The WhatsApp/NSO theory maps directly onto SIM swap digital fraud:

- NSO used WhatsApp's infrastructure to deliver malware to target phones
- Ryan McClaran used AT&T's infrastructure (SIM porting system) to redirect Michael's
  phone number — accessing Michael's digital accounts through the redirected credentials
- In both cases: the attack uses legitimate infrastructure as an attack vector; the
  access is "without permission" of the ultimate victim and the platform owner

**Cal. P.C. §502 applies to the SIM swap:**
- AT&T's California-based network systems were accessed to execute the SIM port
- Michael's California-based email, financial, and SSA accounts were accessed
- The access was "without permission" of both Michael and each account provider

## Verification Note

17 F.4th 930 (9th Cir. 2021) is the jurisdictional ruling — verify before use.
The substantive §502/CFAA claims have not yet been finally adjudicated as of
knowledge cutoff — cite as confirming parallel pleading of §502 + CFAA in
California federal courts, not as a decided merits ruling.
