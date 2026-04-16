# Current Rule — Cal. Penal Code §502 (Unauthorized Computer Access)

## THE WOUND

California's computer crime statute was first enacted in 1979 — five years before
the federal CFAA (1984). The original statute was narrow. The wound it addressed:
emerging computer fraud in California's nascent tech sector. Early computer crimes
included unauthorized access to corporate mainframes and manipulation of business records.

By 1988, the personal computer revolution had expanded the universe of potential
victims dramatically. The 1988 comprehensive amendment rebuilt §502 from scratch,
making it the first modern state computer crime statute with explicit civil remedies.

The federal CFAA (18 U.S.C. §1030) covers "protected computers" affecting interstate
commerce — it is broad but requires federal nexus. California §502 covers unauthorized
access to any "computer, computer system, or computer network" — no interstate commerce
requirement; the state interest is sufficient.

## THE §502 ARCHITECTURE — CIVIL PLAINTIFF PERSPECTIVE

### §502(c) — The Prohibited Acts

§502(c) lists multiple prohibited acts. The provisions most relevant to SIM swap
and identity theft claims:

**§502(c)(1):** Knowingly accesses and without permission alters, damages, deletes,
destroys, or otherwise uses any data, computer, computer system, or computer network
in order to devise or execute any scheme or artifice to defraud, deceive, or extort,
or to wrongfully control or obtain money, property, or data

**§502(c)(2):** Knowingly accesses and without permission takes, copies, or makes
use of any data from a computer, computer system, or computer network, or takes or
copies any supporting documentation

**§502(c)(7):** Knowingly and without permission accesses or causes to be accessed any
computer, computer system, or computer network

**Key distinction from CFAA:** §502(c)(7) has no "loss" or "damage" threshold. Any
knowing unauthorized access violates §502(c)(7). The CFAA requires $5,000+ aggregate
loss for civil action; California §502 does not.

### §502(e) — Civil Action

Any person who suffers damage or loss by reason of a violation of subdivision (c)
may bring a civil action against the violator for compensatory damages and injunctive
relief. In addition, any person who is denied access to a computer system, computer,
or computer network, or who suffers damage to the person's data, may recover:

- **Compensatory damages** for losses, including lost profits
- **Injunctive relief**
- **Civil penalty of not less than $5,000 per violation** in any case where the person
  has been convicted of a violation of §502(c)

**Note on the $5,000 civil penalty:** The $5,000 civil penalty under §502(e)(2)
applies where the defendant has been convicted. For civil claims without prior
conviction, the remedy is compensatory damages and injunctive relief.

**No minimum damages floor without conviction:** Unlike the Wiretap Act ($10,000 min)
or the SCA ($1,000 min), California §502(e) civil damages without a conviction are
compensatory — there is no per-violation statutory minimum. The statute's strength
is (1) no loss threshold, (2) breadth of covered conduct, and (3) stacking with federal claims.

### "Without Permission" — The Operative Element

§502(b)(12): "Without permission" means any access that has not been explicitly
authorized by the owner, lessee, or authorized user of the computer system, computer
network, or data.

**SIM swap application:** The attacker who uses a hijacked phone number to access
Michael's email accounts, financial accounts, and SSA portal had NO permission to
access those systems. Unlike the CFAA Van Buren analysis (scope-based), California
§502 applies to any access without explicit authorization — a straightforward "without
permission" showing.

### §502(b) — Key Definitions

**§502(b)(1) "Access":** To gain entry to, instruct, communicate with, store data in,
retrieve data from, or otherwise make use of any resources of a computer, computer
system, or computer network.

**§502(b)(3) "Computer":** Any device or collection of devices... that, in conjunction
with associated input, output, interface or communications devices, or auxiliary
storage, holds programs and data, and can execute a systematic sequence of instructions
or processes data...

**§502(b)(5) "Computer network":** Any system that provides communications between
one or more computer systems and input/output devices including... systems involving
telephone lines, cables, fiber optical or other communications media.

**§502(b)(8) "Data":** Any representation of information, knowledge, facts, concepts,
computer software, computer programs, or instructions.

## SIM SWAP APPLICATION — §502 ANALYSIS

### Primary Theory: §502(c)(1) and (c)(7)

**§502(c)(1) — Fraud via unauthorized computer access:**
Ryan McClaran used the SIM swap to gain control of Michael's phone number, then used
that control to access Michael's email, financial accounts, SSA portal, and other
computer systems, in order to:
- Execute a scheme to defraud (diverting financial resources, controlling disability claim communications)
- Wrongfully control money and property (controlling access to Michael's accounts)

This is a §502(c)(1) violation for each fraudulent access event.

**§502(c)(7) — Simple unauthorized access:**
Any access to Michael's computer accounts without permission = §502(c)(7). No fraud
element required; no loss threshold required. Each unauthorized login session = separate violation.

### No $5,000 Aggregate Loss Threshold

CFAA §1030(g) requires $5,000 aggregate loss for civil action. California §502(e)
has no equivalent threshold. This means:

- Small account accesses that individually cause <$5,000 loss still violate §502
- California §502 is the state claim when CFAA $5,000 threshold argumentation is raised
- The two claims reinforce each other: CFAA covers the damages threshold; §502 covers
  any unauthorized access regardless of loss

### Stacking with Federal Claims

For SIM swap civil litigation in California federal court:

| Claim | Minimum Per Event | Threshold |
|-------|------------------|-----------|
| §2511 Wiretap | $10,000 | None (per interception) |
| §2701 SCA | $1,000 | None (per stored comm access) |
| 18 U.S.C. §1030 CFAA | Actual damages | $5,000 aggregate loss required |
| Cal. P.C. §502 | Actual/compensatory | None |
| Cal. P.C. §632.7 CIPA | $5,000 | None (per cellular interception) |

California §502 operates as the no-threshold backstop for computer access violations
where the federal $5,000 CFAA threshold might be arguable or not met on isolated incidents.

### RICO Predicate

Cal. Penal Code §502(c)(1) violations (computer fraud) are criminal offenses that
could support a state RICO theory, but more importantly, the federal Civil RICO claim
(18 U.S.C. §1962) can be supported by federal §1030(a)(4) computer fraud predicates —
§502 is a parallel state claim, not a RICO predicate.
