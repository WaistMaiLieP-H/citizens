# Van Buren v. United States (2021) 593 U.S. 374

**Citation:** Van Buren v. United States (2021) 593 U.S. 374, 141 S.Ct. 1648
**Court:** United States Supreme Court
**Decided:** June 3, 2021
**Statute construed:** 18 U.S.C. § 1030(a)(2) — "exceeds authorized access"; scope of CFAA

## Facts

A police officer (Van Buren) used his authorized access to a law enforcement database to look up a license plate for a private party in exchange for money. He was charged under the CFAA for "exceeding authorized access" — he had authorization to use the database for law enforcement purposes but not for personal financial gain.

## Holding

Justice Barrett, writing for a 6-3 majority:

1. **"Exceeds authorized access" means accessing areas of a computer that a person is not authorized to access — not merely violating a use restriction.** The phrase is a gate-related concept: you can exceed authorized access by going into parts of the system you weren't allowed to enter, but not by using otherwise-permitted access for impermissible purposes.

2. **Van Buren did not "exceed authorized access"** because he was authorized to access the database; he merely used it in an unauthorized way. The CFAA does not criminalize policy violations by persons who have legitimate access to the system.

3. **The narrowing principle:** The Court rejected the government's broad interpretation that would make every employee who misuses a work computer (sending personal emails on company time) a federal criminal. The narrower interpretation confines CFAA to genuine unauthorized access — going where you're not supposed to go.

## The doctrinal proposition

Van Buren establishes the gate-related vs. use-restriction distinction:

| Type of Access | Van Buren Result | CFAA Violation? |
|---|---|---|
| Pure outsider — no authorization at all | Not addressed — not Van Buren's case | YES |
| Insider accessing unauthorized areas (e.g., hacking restricted database sections) | Exceeds authorized access | YES |
| Insider using authorized access for unauthorized purpose (Van Buren's fact) | Does NOT exceed authorized access | NO |

## Why Van Buren does NOT limit the SIM swap cases

The SIM swap attacker is a **pure outsider** to the victim's accounts:
- The attacker had NO authorization to access the carrier's account management system as the victim
- The attacker had NO authorization to access the victim's email, banking, or any other account
- Van Buren addresses the insider-who-misuses case; the SIM swapper is an outsider-who-impersonates case

**Van Buren left pure unauthorized access untouched.** The outsider who accesses a system by deception or impersonation has no authorization at all — this is squarely within § 1030(a)(2)'s "without authorization" prong, not the "exceeds authorized access" prong. Van Buren does not narrow the "without authorization" prong.

## Application to cases #30-33

The SIM swap attacker accessed:
- The carrier's account management system — without authorization (impersonating the victim)
- The victim's phone communications — without authorization
- Any accounts accessed via intercepted MFA codes — without authorization

Every access point is "without authorization" under § 1030(a)(2). Van Buren's narrowing of "exceeds authorized access" is irrelevant — the claims proceed under the "without authorization" prong, not the "exceeds authorized access" prong.

## Authority status

United States Supreme Court (2021). Controlling authority on the scope of "exceeds authorized access" under § 1030. Does not limit pure unauthorized access claims. Directly applicable to CFAA analysis for all cases.

**Citation confidence: HIGH** — major Supreme Court decision on CFAA scope. 593 U.S. 374, 141 S.Ct. 1648.
