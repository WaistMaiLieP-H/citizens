# 18 USC §1343 — Wire Fraud
## Current Framework — Logical Structure

**Standard:** 18 USC §1343 (Wire Fraud)
**Build method:** Logical Delta
**Status:** Current framework (as amended through 1988 §1346 addition)

---

## Why this statute exists (the wound it answers)

Wire fraud is the electronic extension of mail fraud (18 USC §1341, enacted 1872). Congress first
enacted wire fraud in 1952 when radio and television created communication channels that could
carry fraud schemes without using the mails. The logical structure is identical to mail fraud;
only the transmission medium differs. Both statutes answer the same wound: fraudsters who use
the postal system or electronic communications to execute schemes that would otherwise be purely
local crimes — giving federal jurisdiction over fraud that crosses state or national lines.

The wire fraud statute's power is its breadth: it criminalizes any scheme to defraud that uses
a wire communication, without requiring that the fraud succeed, that the victim be identified,
or that a specific dollar amount be involved. The wire communication need not itself carry the
fraudulent misrepresentation — it need only be used "in furtherance" of the scheme.

---

## The Three Elements

### Element 1 — Scheme to defraud (or to obtain money/property by false/fraudulent pretenses)
**Logical structure:** Two alternative phrasings in a single statute:
- "a scheme or artifice to defraud" (covers deception that deprives victim of money, property, or honest services)
- "for obtaining money or property by means of false or fraudulent pretenses, representations, or promises"

**Property defined broadly:** "Property" includes tangible assets, money, intangible business
information (Carpenter v. United States, 1987), and contractual rights. After Kelly v. United
States (2020), a scheme that targets regulatory power or government policy — rather than money
or property — does not satisfy §1343's property requirement. The scheme must deprive the victim
of something that can be characterized as property.

**Honest services:** Pre-McNally, courts extended "scheme to defraud" to include depriving victims
of their right to honest services of employees or public officials. McNally v. United States (1987)
limited "property" to traditional property interests. Congress responded in 1988 with 18 USC §1346,
which defines "scheme or artifice to defraud" to include depriving another of "the intangible right
of honest services." Skilling v. United States (2010) then limited §1346 to bribery and kickback
schemes — honest services fraud without a quid pro quo is not covered.

**Application to Michael's cases:** The wire fraud theory in Michael's cases does not depend on
honest services. The scheme to defraud is a classic property-fraud theory:
- Treasury Securities: someone used Michael's SSN/identity to claim bonds belonging to "another
  individual" — scheme to defraud the government and Michael of property (bonds, financial value).
- Crypto fraud (#21): unauthorized transfer of cryptocurrency = property fraud via electronic means.
- ChexSystems pattern: if account fraud was executed via online banking applications or electronic
  transfers, each wire communication in furtherance of the scheme = §1343 count.
- Hillberg UIT (#25): if the compound-identity fraud used wire communications (account applications,
  fund transfers, electronic correspondence) in furtherance of the scheme, §1343 applies.

---

### Element 2 — Materiality
**Rule:** A misrepresentation or omission is material if it has a natural tendency to influence,
or is capable of influencing, the decision of a reasonable person. (Neder v. United States, 1999)

**Implication:** Neder imported the common-law materiality element into wire fraud by holding
that the term "defraud" carries the common-law requirement. Trivial or immaterial
misrepresentations — lies that would not have influenced any reasonable person's decision —
do not satisfy Element 1.

**Application:** In identity theft / financial fraud schemes, materiality is essentially always
satisfied. Misrepresenting identity (using Michael's SSN, name, or identity to open accounts,
claim bonds, or access financial instruments) is inherently material — no institution would open
accounts or release funds if it knew the applicant was an identity thief.

---

### Element 3 — Use of wire, radio, or television communication in interstate or foreign commerce
**Rule:** The wire communication must (a) be a wire, radio, or TV communication, and (b) cross
state lines or national borders (interstate or foreign). A single phone call, email, fax,
or electronic funds transfer that crosses state lines is sufficient.

**Furtherance requirement:** The wire communication need not itself contain the fraudulent
representation — it need only be used in furtherance of the scheme. Routine communications
that advance the scheme (e.g., an email confirming a fraudulent account opening, an ACH transfer
moving stolen funds, a phone call to verify a fraudulently opened account) satisfy the element.

**Electronic communications are inherently interstate:** In the modern financial system, virtually
every electronic banking transaction, online account application, email, or phone call routes
through servers in multiple states. The interstate element of wire fraud is almost never the
battleground in financial fraud cases.

---

## Specific Intent

**Rule:** Wire fraud requires specific intent to defraud — the defendant must have acted with
the purpose of obtaining money, property, or services by deception. Recklessness or negligence
is insufficient.

**Good faith defense:** A sincere good-faith belief in the truth of the representations negates
specific intent. This is the primary defense theory in wire fraud prosecutions and must be
specifically negated in charging documents.

---

## Sentencing

**Base:** Up to 20 years imprisonment per count. 18 USC §1343.
**Enhanced:** Up to 30 years if the offense affects a financial institution or is connected to
a presidentially declared major disaster or emergency. 18 USC §1343 (last sentence).
**Fines:** Up to $250,000 per count (or twice the gain/loss, whichever is greater).
**Forfeiture:** Criminal forfeiture of proceeds under 18 USC §981(a)(1)(C) + 28 USC §2461.

---

## Civil RICO predicate

Wire fraud under §1343 is a listed RICO predicate act under 18 USC §1961(1)(B). Two or more
wire fraud acts, related to each other and part of a pattern of racketeering activity, form the
predicate pattern for a civil RICO claim under §1964(c). This is the pathway from the financial
fraud portfolio (individual wire fraud acts) to treble damages under civil RICO.

**Pattern requirement:** At least two predicate acts within 10 years; relationship between acts;
threat of continued criminal activity (continuity). H.J. Inc. v. Northwestern Bell (1989).
Multiple wire fraud counts across multiple schemes (Treasury, crypto, ChexSystems, Hillberg UIT)
constitute related predicates supporting RICO continuity.

---

## Civil remedies outside RICO

Wire fraud does not create a private right of action directly — only the government can prosecute
§1343 criminally. Civil plaintiffs access wire fraud through:
1. **Civil RICO (§1964(c)):** wire fraud as predicate → treble damages + attorney fees
2. **State tort claims:** the same facts supporting §1343 typically satisfy common-law fraud,
   conversion, and unfair business practices claims
3. **Federal agency referral:** FTC, CFPB, FBI can prosecute on the civil/criminal tracks
4. **Restitution in criminal proceeding (MVRA 18 USC §3663A):** if a criminal prosecution
   results from Michael's referral, restitution to victims is mandatory
