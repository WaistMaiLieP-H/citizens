# Van Buren v. United States — Holding

**Citation:** 593 U.S. 374 (2021)
**Court:** Supreme Court of the United States
**Decided:** June 3, 2021
**Author:** Barrett, J.

## Facts

Nathan Van Buren was a Georgia police officer who had authorized access to a law
enforcement database of license plate information. A person posing as a mediator in
a dispute offered Van Buren money to look up a license plate number in the database
to determine if a specific person was an undercover police officer. Van Buren ran the
query and accepted payment.

The government prosecuted Van Buren under 18 U.S.C. §1030(a)(2) for "exceeds authorized
access" — specifically, that he accessed the database for a purpose (personal enrichment)
outside the scope of his authorized use (law enforcement purposes only).

## Holding

**"Exceeds authorized access" means accessing files, folders, or databases that the
defendant was not permitted to access — not accessing a permitted system for an
improper purpose.**

The Court adopted the "gates-up-or-down" framework: if you are permitted to access
a system or file, you access it within authorization, even if you use the data in a
way that violates the terms under which access was granted. "Exceeds authorized access"
means going into areas of the computer you were not permitted to enter — like a guest
who was given a key to the front door but opens doors they were told are off-limits.

Van Buren had authorization to access the license plate database. He used that
authorized access for an unauthorized purpose. Under §1030(a)(2), this does not
constitute "exceeding authorized access" — it is an authorized user acting improperly,
which may be punishable under other statutes but not §1030(a)(2)'s "exceeds" prong.

## Rules Distilled

1. **"Exceeds authorized access"** = accessing parts of a computer system you were not
   permitted to access (scope-based, not purpose-based)
2. **Authorized use for unauthorized purpose** = not a §1030(a)(2) violation
3. **"Without authorization"** (separate prong) = still applies to persons with no access
   rights at all — Van Buren does not touch this prong
4. **Gate-up/gate-down analogy:** If the gate is up for you, using what you access
   improperly is not "exceeding authorized access"
5. **Civil §1030(g) implications:** The same analysis applies — civil plaintiffs cannot
   use "exceeds authorized access" theory against authorized users who misuse their access

## What Van Buren Does NOT Change

1. **"Without authorization" cases:** Someone with no permission who accesses a computer
   system (SIM swap attacker, credential thief, unauthorized remote access) still violates
   §1030(a)(2)'s "without authorization" prong — Van Buren's narrowing does not apply
2. **Physical trespass analogy:** Van Buren was not told certain files were off-limits;
   if he had been told specific databases were outside his access and he accessed them
   anyway, that would still be "exceeds authorized access"
3. **Credential sharing:** Someone who obtains credentials through fraud or theft and uses
   them is not "authorized" — they are accessing "without authorization"

## Significance for SIM Swap Claims

Van Buren strengthens the SIM swap CFAA theory: the attacker who uses a hijacked phone
number to access a victim's email, SSA portal, or financial accounts has NO authorization
to access those accounts. This is the "without authorization" prong — completely
unaffected by Van Buren.

Van Buren also limits potential theories against carrier employees (AT&T) who may have
been complicit in the SIM swap: if a carrier employee had authorized access to the porting
system and used it to execute an improper port, that is now potentially Van Buren-protected
unless it can be shown the employee accessed a specific system outside their authorization
scope.
