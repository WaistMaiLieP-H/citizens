# Evolution Stage 03 — USA PATRIOT Act 2001 + Van Buren 2021 Narrowing
## Scope Expansion, Then Judicial Contraction

### THE WOUND (POST-9/11)

After September 11, 2001, Congress used the PATRIOT Act as a vehicle for expanding
multiple federal criminal statutes. For the CFAA, the concern was coordinated cyberattacks
on critical infrastructure — the concern was less about individual computer fraud and
more about state-sponsored or large-scale coordinated intrusions.

The PATRIOT Act also addressed the gap in §1030(g)'s civil action: the prior version
required that the conduct cause "damage" (technical term meaning impairment to data/
systems). Many computer crimes caused economic "loss" without technically impairing
a system — e.g., accessing and copying data without destroying it. The amendment
clarified the civil action covers both damage and loss.

### DESIGN RESPONSE — PATRIOT ACT 2001

**USA PATRIOT Act, Pub. L. 107-56 (Oct. 26, 2001):**

1. **Expanded definition of "damage"** and clarified that "loss" includes economic harm
   from unauthorized access beyond technical system impairment

2. **Increased penalties** for cyberterrorism — access affecting critical infrastructure

3. **Extended civil action** to include loss as well as damage — closing the gap for
   claims where data was taken without system impairment

4. **Aggregation period:** $5,000 threshold applies during any 1-year period — enabling
   aggregation of multiple smaller intrusions

### VAN BUREN v. UNITED STATES (2021) — JUDICIAL NARROWING

The Supreme Court's Van Buren decision significantly narrowed the CFAA's scope:

**Van Buren v. United States, 593 U.S. 374 (2021):**
"Exceeds authorized access" in §1030(a)(2) means accessing a computer's files, folders,
or databases that the user was not permitted to access — not using authorized access for
an unauthorized purpose. A gate-up / gate-down analogy: if you are permitted to access
a database, you access it within authorization even if you use the data improperly.

**Effect:** Van Buren overturned the broad "purpose-based" theory of "exceeds authorized
access" that had been used in some circuits. Under purpose-based theory, an employee who
accessed their employer's database for personal gain (not work purposes) "exceeded" their
access. Van Buren rejected this: exceeding authorized access requires accessing
files/systems you were not permitted to access at all.

### LOGICAL DELTA — VAN BUREN NARROWING

| Scenario | Pre-Van Buren | Post-Van Buren |
|----------|---------------|----------------|
| Employee accesses authorized database for personal benefit | Some circuits: "exceeds authorized access" | NOT "exceeds authorized access" |
| Person uses stolen credentials to access another's account | "Without authorization" | Still "without authorization" — CFAA applies |
| SIM swap attacker uses hijacked number to access victim's accounts | "Without authorization" | Still "without authorization" — CFAA applies |
| Insider who has account access uses it for conspiracy | Was: "exceeds authorized access"; Now: only if insider accessed files outside their permission scope | More limited; must show specific file/system access outside scope |

**Van Buren preserves SIM swap/digital intrusion theories:**
Van Buren does not affect cases where the defendant had NO authorization at all.
SIM swap attackers using a hijacked phone number to access a victim's accounts are
completely unauthorized — not misusing permitted access. The Van Buren narrowing
applies only to the "exceeds authorized access" branch; the "without authorization"
branch is unaffected.

### PROVENANCE

USA PATRIOT Act, Pub. L. 107-56, §814, 115 Stat. 384 (Oct. 26, 2001)
Van Buren v. United States, 593 U.S. 374 (2021) — judicial interpretation
