# United States v. Nosal — Holding

**Citation:** United States v. Nosal, 676 F.3d 854 (9th Cir. 2012) (en banc) (Nosal I);
United States v. Nosal, 844 F.3d 1024 (9th Cir. 2016) (Nosal II)
**Court:** United States Court of Appeals for the Ninth Circuit
**Decided:** Nosal I: 2012; Nosal II: 2016

## Significance for Circuit of Suit

California federal cases (NDCA, CDCA) are in the Ninth Circuit. Nosal's Ninth Circuit
interpretation of the CFAA applies in California federal courts, subject to Van Buren's
(2021) superseding Supreme Court resolution of the "exceeds authorized access" question.

## Nosal I (2012) — En Banc

**Facts:** David Nosal was a former Korn/Ferry International executive who, while still
employed, coordinated with colleagues to download client lists from Korn/Ferry's proprietary
database for use at a competing firm he was setting up.

**Ninth Circuit holding (en banc):**
The court narrowed the "exceeds authorized access" theory — holding that it did not
cover misuse of authorized access for improper purposes. An employee who has authorization
to access a database does not "exceed authorized access" merely by using the data for
the wrong purpose.

**Pre-Van Buren significance:** Nosal I was one of the primary circuit decisions that
led to the eventual Supreme Court resolution in Van Buren. The en banc decision reflected
the Ninth Circuit's rejection of the broad purpose-based theory.

**Post-Van Buren:** Van Buren adopted the Nosal I approach — Nosal I's reasoning is
now the controlling rule (as articulated by the Supreme Court).

## Nosal II (2016) — Former Employee / Credential Sharing

**Facts:** After Nosal left Korn/Ferry, he and his co-conspirators used the login
credentials of a current employee (his former assistant) to access Korn/Ferry's systems.
The assistant shared her credentials with Nosal; she had authorization; Nosal did not.

**Ninth Circuit holding (Nosal II):**
Using another person's credentials to access a system when YOU have no authorization
to access that system = "without authorization" under §1030. The fact that the credential
owner was authorized does not confer authorization on an unauthorized user who borrowed
the credentials.

**Post-Van Buren status:** Nosal II survives Van Buren. Van Buren addressed "exceeds
authorized access"; Nosal II addressed "without authorization." The Supreme Court
explicitly preserved the "without authorization" prong. Credential sharing to grant
access to an unauthorized user = "without authorization" under §1030(a)(2).

## Rules Distilled

**From Nosal I (confirmed by Van Buren):**
1. "Exceeds authorized access" = scope-based, not purpose-based
2. Authorized user who misuses access ≠ CFAA violation under (a)(2)'s "exceeds" prong

**From Nosal II (survives Van Buren):**
3. Using another's credentials to access a system you are not authorized to access =
   "without authorization"
4. The authorized credential-holder's permission does not extend to persons who borrow
   the credentials
5. Post-employment use of former access = "without authorization" once employment ends

## Application to SIM Swap

Nosal II's credential-sharing analysis directly maps to SIM swap:
- The phone number was Michael's — his credential
- The attacker used the hijacked number (Michael's credential) to access Michael's accounts
- Michael had authorization to access those accounts; the attacker did not
- The attacker's use of Michael's credential to access Michael's accounts =
  "without authorization" under Nosal II / §1030(a)(2)

This is a cleaner CFAA theory than any "exceeds authorized access" argument.
