# 18 USC §1028A — Aggravated Identity Theft: Current Logic

## The logical architecture (post-Dubin, 2023)

§1028A is not a standalone crime. It is a **mandatory consecutive sentence enhancement** that attaches
to any conviction for an "enumerated felony" when the defendant, during and in relation to that felony,
**knowingly transfers, possesses, or uses, without lawful authority, a means of identification of another
person.**

The statute does four things and only four things:
1. Creates a **mandatory minimum** of 2 years (§1028A(a)(1)) or 5 years for terrorism-related predicates
   (§1028A(a)(2)).
2. Makes that sentence **consecutive** to the predicate sentence — it cannot run concurrently.
3. Prohibits **stacking** (§1028A(b)(4)): multiple §1028A counts arising from the same scheme may not
   be stacked consecutively (court has discretion to run them concurrently), but they must be consecutive
   to the predicate.
4. Requires **knowledge** that the identification belongs to a real person (carried over from
   Flores-Figueroa v. United States, which construed §1028(a)(7) and applies equally here).

## The enumerated felony requirement

§1028A(c) lists the qualifying predicate offenses. The most important for the financial fraud portfolio:
- §1028A(c)(4): **18 USC §1343 (wire fraud)** — directly listed
- §1028A(c)(5): **18 USC §1344 (bank fraud)** — directly listed
- §1028A(c)(1): Social Security-related offenses (42 USC §408)
- §1028A(c)(6): Mail fraud (§1341)

If the predicate offense conviction fails, §1028A falls. §1028A does not require a §1028 conviction;
it requires only that the predicate offense was committed using a real person's identification.

## The "at the crux" test — Dubin v. United States (2023)

Before Dubin, courts split on what "uses a means of identification of another person" meant. The
government's broad interpretation would have covered virtually any fraud involving another person's
information. The Supreme Court corrected the overreach.

**The Dubin rule:** A defendant "uses" a means of identification "in relation to" a predicate offense
only when the **use of that identification is at the crux of the underlying offense** — not merely
incidental to it.

Dubin was a Medicaid overbilling case. The provider used a patient's Medicaid ID to submit fraudulent
claims. The Court held: the fraud was the overbilling. The patient's ID was just the mechanism to
access the billing system. The ID was incidental — it was not the crux of the crime.

**Post-Dubin standard:**
- Identity use is "at the crux" when the identity itself is the **object** of the crime or the
  **essential mechanism** by which the fraud is perpetrated (e.g., impersonation, account takeover,
  opening fraudulent accounts in another's name).
- Identity use is NOT "at the crux" when it is merely administrative — used to reference or access
  a victim's record while the actual crime is overbilling, overcharging, or misrepresentation about
  a different subject.

## Application to Michael's cases

### Treasury Securities identity theft (Case #20)
**Strong §1028A predicate.** Someone opened Treasury accounts or made claims using Michael's SSN and
identity credentials. The fraud mechanism **is** the identity — it was necessary to impersonate Michael
as the accountholder. The identity use is at the crux, not incidental. Predicate: §1343 wire fraud
(interstate electronic communications) + §1344 bank fraud (if financial institutions involved).
Result: Mandatory consecutive 2-year enhancement on top of predicate sentence.

### Crypto fraud / SIM swap (Cases #21, #30-33)
**Strong §1028A predicate.** SIM swap to gain control of phone number, then using Michael's phone
identity to access accounts, reset credentials, and drain crypto holdings. The phone identity/SIM is
at the crux — it is the instrument of the account takeover. Predicate: §1343 (interstate wire).
Result: §1028A applies.

### ChexSystems / banking fraud (Case #22)
**Moderate §1028A risk depending on structure.** If someone made entries to ChexSystems using
Michael's identity to prevent him from banking — the identity use was the mechanism by which the
harm was perpetrated (blocking banking access by fraudulently attributing conduct to Michael's
identity). Distinguishable from Dubin's overbilling: the target here IS Michael's banking identity.

### Hillberg UIT / compound identity (Case #25)
**Strong §1028A potential if "HILLBERGMANN" compound identity used in financial account openings.**
Using a synthetic identity containing Michael's components (name, SSN fragments) to open Northern
Trust variable product accounts = identity at the crux of the fraud (the accounts could not have
been opened without the identity). Predicate: §1343 + §1028.

## Damages / sentencing architecture

§1028A is a **criminal statute only**. There is no private civil right of action under §1028A itself.

The civil damages pathway runs through §1028(g) (civil damages provision) and civil RICO (§1964(c))
where the identity theft acts are RICO predicates under §1961(1)(B).

**Criminal referral value of §1028A:**
When presenting cases to FBI, IRS CI, Treasury IG, USSS — the §1028A stacking is the prosecutorial
lever. It converts a white-collar financial fraud case (where defendants often get probation or
light sentences) into a case with mandatory minimum consecutive prison time. Prosecutors use this
to extract cooperation agreements.

## What §1028A does NOT provide
- No civil private right of action (civil damages = §1028(g) + RICO)
- No standalone charge (must have enumerated predicate conviction)
- No enhancement where identity use is merely incidental (Dubin)
- No stacking of multiple §1028A counts consecutively against each other (§1028A(b)(4))
