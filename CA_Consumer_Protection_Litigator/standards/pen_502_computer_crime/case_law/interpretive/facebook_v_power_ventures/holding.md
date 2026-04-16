# Facebook v. Power Ventures — Holding

**Citation:** Facebook, Inc. v. Power Ventures, Inc., 844 F.3d 1058 (9th Cir. 2016)
**Court:** United States Court of Appeals for the Ninth Circuit
**Decided:** December 9, 2016

## Facts

Power Ventures operated a social media aggregation service that allowed users to
access their Facebook accounts through Power Ventures' platform. Facebook objected
to Power Ventures accessing its servers. Facebook sent a cease-and-desist letter
revoking any permission or authorization. After receiving the letter, Power Ventures
continued accessing Facebook's servers.

Facebook sued under both the CFAA (18 U.S.C. §1030) and California Penal Code §502.
The district court found Power Ventures liable and imposed injunctive relief and
statutory damages.

## Holding

**After receiving express notice revoking permission, continuing to access a computer
system is "without permission" under Cal. Penal Code §502(c)(7) and "without
authorization" under the CFAA.**

The Ninth Circuit held:
1. A defendant who initially had permission can lose that permission through an explicit
   revocation — continuing to access after revocation = "without permission" / "without
   authorization"
2. California §502 and federal CFAA can be analyzed in parallel; the "without permission"
   standard under §502 is not necessarily more restrictive than the CFAA standard
3. The cease-and-desist letter constituted legally effective revocation of any implied
   permission arising from the users' authorization to access their own accounts

**On CFAA:** The court applied a similar analysis — permission can be revoked by the
system owner independent of the user's wishes.

## Rules Distilled

1. **Revocation ends permission:** Explicit notice from a computer system owner that
   further access is unauthorized = "without permission" under §502 for any subsequent
   access
2. **Owner permission controls:** Even where a user grants access, the system owner can
   independently revoke permission — and the user's continued permission does not
   override the owner's revocation
3. **§502 and CFAA are parallel:** Both statutes can be analyzed simultaneously; the
   same facts can support both claims
4. **"Without permission" = "without authorization":** California §502's "without
   permission" standard operates similarly to CFAA's "without authorization" — both
   are about whether the system owner authorized the specific access
5. **No technical circumvention required:** §502 violations do not require hacking or
   defeating security measures — accessing after revocation is sufficient

## Significance for SIM Swap Claims

Power Ventures establishes that §502's "without permission" standard applies cleanly
to unauthorized account access. For SIM swap claims:

**The attacker (Ryan McClaran) never had permission to access Michael's accounts.**
This is simpler than the revocation scenario in Power Ventures — there was no
initial permission, consent, or implied authorization. McClaran's access was entirely
"without permission" from the moment of the SIM swap.

**System owner vs. user:**  The Power Ventures principle (system owner controls
permission) also applies against AT&T's potential defense that the SIM port was
authorized by "someone." Google (email), SSA (portal), and financial institutions
are system owners who never authorized McClaran's access — regardless of what the
SIM swap attack made it appear.

## Verification Note

Facebook v. Power Ventures at 844 F.3d 1058 — verify citation before use in filed documents.
