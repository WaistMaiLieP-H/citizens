# Context — 18 U.S.C. § 1030 Computer Fraud and Abuse Act (CFAA)

## The wound and the promise

**The wound:** The CFAA was enacted in 1986 to address the gap between existing federal fraud statutes and the new reality of computer crime. The existing wire fraud statute (18 U.S.C. § 1343) covered some computer fraud but required a scheme to defraud — unauthorized access alone was not enough. The CFAA was designed to make unauthorized access to computers a federal crime regardless of whether money was taken.

**The promise:** § 1030 promises that unauthorized access to a "protected computer" — which includes virtually any computer connected to the internet — is a federal crime. The civil provision (§ 1030(g)) promises that victims of CFAA violations can recover compensatory damages and injunctive relief in federal court.

## The "protected computer" scope

The CFAA's reach is nearly universal because § 1030(e)(2)(B) defines "protected computer" as any computer "used in or affecting interstate or foreign commerce or communication." This includes:
- Any computer connected to the internet
- Mobile phones and smartphones
- Carrier systems and network equipment
- Cloud computing systems
- Any device that communicates across state lines

**All smartphone SIM swaps involve protected computers** — the carrier systems, the victim's phone, and any accounts accessed through them are all "protected computers" under § 1030(e)(2)(B).

## The Van Buren scope limitation (2021)

*Van Buren v. United States* (2021) 593 U.S. 374 narrowed the CFAA by holding that "exceeds authorized access" means obtaining information from areas of the computer that the person was not authorized to access — not merely violating a use restriction. Van Buren limited CFAA to cases of actual unauthorized access, not mere policy violations.

**Application:** Van Buren does not limit the SIM swap cases, because:
- The attacker had NO authorization to access the carrier's system under the victim's account
- The attacker had NO authorization to access the victim's email, banking, or other accounts
- Van Buren addresses insiders who exceed their scope; the SIM swapper is a pure outsider to the victim's accounts

## The civil cause of action — § 1030(g)

Section 1030(g) provides a civil cause of action if:
1. The defendant violated § 1030(a)
2. The violation caused "damage or loss"
3. The conduct involves one of the § 1030(c)(4)(A)(i) factors

**The most applicable factor for the steward's cases:** § 1030(c)(4)(A)(i)(I) — "loss to 1 or more persons during any 1-year period... aggregating at least $5,000 in value." This $5,000 threshold is met by the accumulated losses from intercepted communications blocking access to medical care, disability benefits, and financial accounts.

**The "loss" definition** is broad under § 1030(e)(11): it includes the cost of responding to the offense, damage assessment costs, restoration costs, revenue lost, costs incurred, and consequential damages from service interruption. All of these apply to a multi-year SIM swap attack.

## SOL for civil claims

Two years from the date of the act or the date of discovery. For an ongoing concealed SIM swap starting in 2018, the discovery rule runs the SOL from when the victim knew or should have known about the unauthorized access.

## Application to cases #30-33

**Case #30 — SIM swap / clone (AT&T, Verizon, T-Mobile):**
- § 1030(a)(2)(C): unauthorized access to a protected computer and obtaining information → each interception of a call, text, or MFA code is a violation
- § 1030(a)(4): unauthorized access with intent to defraud and obtaining something of value → the value of the intercepted communications and the accounts accessed
- § 1030(a)(5): intentional transmission causing damage → if the SIM swap disrupted the steward's service

**Case #31 — Ryan McClaran:**
- § 1030(a)(2): unauthorized access to obtain information
- § 1030(a)(5): if any device or account was damaged by the unauthorized access
- RICO predicate: § 1030 violations are not listed as RICO predicates in § 1961(1), but wire fraud (§ 1343) predicates cover the scheme — the CFAA violations establish the conduct, wire fraud establishes the predicate

**Case #33 — Device admin control:**
- § 1030(a)(5)(A): transmission of a program or command that intentionally causes damage to a protected computer — if spyware or remote access tools were installed on the steward's devices

## Bilateral analysis

**As complainant:** Every unauthorized access to the steward's phone number, device, accounts, or communications is a § 1030 violation. The civil action can be filed in federal court.

**As respondent:** None in the telecom fraud context — the steward was the victim.
