# 15 USC §1681 — Fair Credit Reporting Act (FCRA)
## Current Framework — Logical Structure

**Standard:** 15 USC §§1681–1681x (Fair Credit Reporting Act)
**Build method:** Logical Delta
**Status:** Current consolidated framework (FCRA as amended through FACTA 2003 + Dodd-Frank 2010)

---

## Why this statute exists (the wound it answers)

Before 1970, consumer credit bureaus were black boxes. They collected information from creditors,
assembled files on consumers, and reported those files without the consumer ever seeing the data,
having any right to correct errors, or knowing who received the report. A false entry — an unpaid
debt that had been paid, a default belonging to someone with a similar name, a fraud entry — could
follow a consumer indefinitely with no remedy. The bureau owed no duty to the consumer; it owed
its duty only to the subscribing creditors who paid for reports. Congress found this created a
system where consumer credit reports had "the potential to be seriously harmful" and where
"inaccurate credit reports directly impair the efficiency of the banking system." 15 USC §1681(a).

FCRA's answer: flip the obligation. Bureaus become Consumer Reporting Agencies (CRAs) with duties
to consumers — not just subscribers. The statute imposes four structural duties, a damages
architecture, and (after FACTA 2003) an identity theft blocking mechanism.

---

## The Four Structural Duties

### Duty 1 — Accuracy: §1681e(b)
**Command:** "Whenever a consumer reporting agency prepares a consumer report it shall follow
reasonable procedures to assure maximum possible accuracy of the information concerning the
individual about whom the report relates."

**Logical object:** The CRA's own procedures for collecting, maintaining, and outputting data.
**Who bears it:** CRAs (Equifax, Experian, TransUnion, ChexSystems, LexisNexis, CLUE, etc.)
**Trigger:** Preparation of any consumer report.
**Standard:** "Reasonable procedures" — not strict liability on individual errors, but liability
for systemic procedural failures.

**ChexSystems application:** ChexSystems is a specialty CRA under §1681a(f). Every entry it
maintains about Michael Hartmann's deposit account history is subject to this accuracy duty.
Reporting closed account, overdraft, or fraud alert without verifying the underlying transaction
is a §1681e(b) failure.

---

### Duty 2 — Reinvestigation: §1681i
**Command:** When a consumer disputes the completeness or accuracy of any item, the CRA must:
(a) conduct a reasonable reinvestigation within 30 days (or 45 days if additional information
is submitted); (b) provide the furnisher with all relevant information the consumer submits;
(c) delete or modify inaccurate or unverifiable information; (d) provide written results and
a free copy of the modified report; (e) certify completeness of deletion if consumer requests.

**Logical object:** The CRA's dispute-resolution process.
**Who bears it:** CRAs.
**Trigger:** Consumer dispute submission.
**Teeth:** Failure to delete unverifiable information after dispute = independent §1681i violation,
separate from the underlying §1681e(b) accuracy failure.

**Application:** If Michael disputed ChexSystems entries and ChexSystems failed to reinvestigate
within 30 days or failed to delete entries it could not verify, each failure is an independent
violation.

---

### Duty 3 — Furnisher Duty: §1681s-2(b)
**Command:** When a furnisher (the entity that reported the information to the CRA) receives
notice from a CRA that a consumer has disputed an item, the furnisher must: (a) investigate the
dispute; (b) review all relevant information provided; (c) report results to the CRA;
(d) correct or delete inaccurate, incomplete, or unverifiable information.

**Logical object:** The furnisher's (creditor's/bank's) response to CRA dispute notice.
**Who bears it:** Furnishers — banks, creditors, collection agencies, government agencies that
reported data to a CRA.
**Trigger:** CRA notifies furnisher of consumer dispute (the CRA-to-furnisher leg).
**Civil enforcement:** §1681s-2(b) duties are privately enforceable via §1681n/§1681o.
(Note: §1681s-2(a) duties to report accurately are NOT privately enforceable — FTC/CFPB only.)

**Application:** Any entity that furnished false data about Michael to a CRA (creditor, bank, or
government agency) who failed to correct after CRA notified them of his dispute = §1681s-2(b)
violation.

---

### Duty 4 — Identity Theft Block: §1681c-2 (added by FACTA 2003)
**Command:** A CRA shall block reporting of information identified by the consumer as resulting
from identity theft, within 4 business days of receiving: (1) appropriate proof of identity;
(2) a copy of an identity theft report; (3) identification of the information to be blocked;
(4) a statement by the consumer that it is identity-theft-related.

**Logical object:** The CRA's mechanism for removing fraudulent tradelines that exist because
someone else used the consumer's identity to open accounts.
**Who bears it:** CRAs.
**Trigger:** Consumer submits identity theft report + blocking request.
**Block effect:** CRA may not report the blocked information and must notify furnisher.
**Rescission:** CRA may rescind block only on certain grounds (misrepresentation, etc.) with notice.

**Application critical for Michael's cases:** Treasury Securities identity theft, SSN theft,
ChexSystems fraud entries — these are FACTA § 1681c-2 blocking candidates if an identity theft
report exists or can be prepared.

---

## Damages Architecture

### Negligent violation — §1681o
Actual damages + attorney fees + costs.
No floor; must prove actual harm (financial loss, credit denial, emotional distress with
concrete connection to violation).

### Willful violation — §1681n
Actual damages OR statutory damages $100–$1,000 per violation (plaintiff's election)
PLUS punitive damages (amount at jury discretion, no statutory cap)
PLUS attorney fees + costs.

**Willful defined (Safeco v. Burr, 2007):** Not limited to conscious disregard — includes
"reckless disregard of a duty." A defendant acts willfully if it acted under an interpretation
of the statute that was objectively unreasonable in light of the statute's text and authoritative
guidance.

**ChexSystems willfulness theory:** If ChexSystems maintained a policy of refusing to delete
unverifiable entries after dispute (institutional pattern, not isolated error), that policy is
objectively unreasonable under §1681i's plain command — willful violation, statutory damages +
punitive available.

---

## Standing Architecture — Post-Spokeo/TransUnion

### Spokeo, Inc. v. Robins, 578 US 330 (2016)
A plaintiff cannot satisfy Article III standing with a bare procedural violation divorced from
any concrete harm. An inaccurate report that was never disclosed to any third party may not
constitute injury-in-fact.

**Implication for Michael:** Must show the inaccurate/fraudulent entry was actually disclosed
to a third party (employer, lender, landlord, bank) OR caused a concrete harm (account denial,
higher interest, employment denial, refusal to open account) — not merely that the inaccuracy
exists in the file.

### TransUnion LLC v. Ramirez, 594 US 413 (2021)
Of the class members whose files contained inaccurate OFAC alerts, only those whose reports were
actually disclosed to third-party businesses had suffered concrete harm sufficient for standing.
Those whose reports were never sent to anyone lacked Article III standing.

**Implication for Michael:** The causal chain matters — inaccurate ChexSystems report → bank
refuses to open account → concrete denial of banking services = standing. Inaccuracy in file
but no actual disclosure = potential standing problem. Document every downstream use of the
report.

---

## Specialty CRA note — ChexSystems under FCRA

ChexSystems maintains "consumer reports" under §1681a(d) — reports used by banks to evaluate
applications to open deposit accounts. It is a CRA under §1681a(f). All four duties apply.
Its reports are "employment reports" analog but for banking access — refusal to open checking
or savings accounts based on ChexSystems data is the concrete harm that satisfies Spokeo/TransUnion
standing.

---

## Operational posture for Michael's portfolio

**Primary targets:**
1. ChexSystems — §1681e(b) accuracy + §1681i reinvestigation + potential §1681c-2 blocking
2. Furnisher(s) who reported the ChexSystems-adverse data — §1681s-2(b) post-dispute failure
3. Downstream: any bank that denied account opening based on ChexSystems = concrete harm → standing
4. Treasury/SSN downstream: if any CRA received and reported data from the identity-theft
   Treasury account, §1681c-2 blocking applies once identity theft report is filed

**SOL:** 2 years from date of discovery of violation, or 5 years from date violation occurred,
whichever is earlier. §1681p. For ongoing ChexSystems reporting, SOL runs from each new report
that includes the inaccuracy.
