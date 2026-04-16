# EVID § 1271 Business Records Exception — Operative Rule

**Standard ID:** evid_1271_business_records_hearsay_exception
**Citizen:** CA_Forensic_Document_Specialist
**Layer:** 2 — Operative Rule
**Build date:** 2026-04-13

---

## The Rule

A writing made as a record of an act, condition, or event is admissible over a hearsay objection IF all four conditions are met: (1) regular course of business; (2) at or near the time of the event; (3) custodian or qualified witness testifies to identity and preparation; (4) sources and method of preparation indicate trustworthiness.

All four conditions are conjunctive — failure of any one excludes the record.

---

## Condition-by-Condition Analysis

### (a) Regular Course of Business

The record must be the type kept routinely as part of the business's operations. A police department routinely keeps incident reports — those qualify. An auto dealer routinely keeps vehicle history and title records — those qualify. A court's clerk's office routinely keeps orders and filings — those qualify.

**The negative tell:** A document created SPECIFICALLY to serve as evidence in anticipated litigation, or created after the fact to fill a gap in the record, is NOT made in the regular course of business. It was made in the special course of litigation preparation. Courts distinguish:
- Regular course records: created as part of how the entity does its work, not primarily for litigation
- Litigation-prepared records: created after a dispute arises, primarily for use as evidence

**Application to this case record:** Documents created after the events they purport to record — e.g., backdated reports, after-the-fact "memorializations" — fail §1271(a) on their face.

### (b) At or Near the Time

The record must be created contemporaneously with or shortly after the event it records. "At or near the time" is evaluated contextually — a police incident report written at the end of a shift satisfies (b); a report recreated from notes two years later does not.

**The document fraud tell:** The timing of a document's creation is discoverable. File metadata (creation timestamp, modification timestamp), printing logs, email timestamps, witness testimony about when a document was created — all of these establish when the document came into existence. A document bearing a 2009 date but file metadata showing 2015 creation fails §1271(b) — and also triggers §1402.

**Application:** For any document whose timing is suspect, the threshold question is: when was this actually created? If the answer is "after the event it records," the document fails §1271(b) regardless of its face date.

### (c) Custodian or Qualified Witness

Someone must testify to:
- The identity of the record (what it is, where it comes from)
- The mode of its preparation (how records of this type are created and maintained)

This does not require the person who created the record. A records custodian (the person responsible for the records system) can testify to standard procedures without personal knowledge of each individual entry.

**Subpoena mechanism:** EVID §1560 allows businesses to produce records to a court clerk via sealed package with a custodian affidavit (§1561), eliminating the need for live testimony in many cases.

### (d) Trustworthiness

The sources of information, method, and time of preparation must indicate trustworthiness. This is the catchall: even if the first three conditions are met, a court may exclude a business record where the circumstances of preparation suggest unreliability.

**The fraud-detection prong:** §1271(d) is the provision that captures records that technically satisfy (a)-(c) but were prepared under circumstances that undermine reliability. This includes:
- Records where the person entering the data had a motive to falsify (e.g., a dealer employee entering false vehicle history)
- Records where the system generating the record was compromised or manipulated
- Records where the source of information was unreliable (hearsay-on-hearsay from untraceable sources)

---

## The Document Fraud Tell — Synthesis

A document that was created after the fact to paper over misconduct fails §1271 at multiple levels:
- **§1271(a):** Not made in regular course — made for litigation/cover
- **§1271(b):** Not made at or near the time — made after the event
- **§1271(d):** Not trustworthy — method of preparation was deceptive

A proponent who tries to invoke §1271 for an after-the-fact record must survive challenges on all three prongs. The absence of a genuine regular-course record for the relevant event may itself be admissible as an inference: the event either didn't happen as claimed, or the contemporaneous record was destroyed.

---

## Application to Active Cases

### RedJag Wrong CARFAX

CARFAX is a commercial vehicle history reporting service. Vehicle history reports are business records kept in the regular course of CARFAX's operations. A vehicle history report for VIN-X is a genuine business record under §1271 for VIN-X.

**The wrong CARFAX problem:** If the dealer provided the buyer with CARFAX for VIN-Y (a different vehicle), the record offered to the buyer is authentic as to VIN-Y's history but NOT authentic as a record of VIN-X's history. It cannot be admitted under §1271 as evidence of VIN-X's history because it is not a record OF VIN-X. §1271(d) trustworthiness further fails: a record that does not correspond to the vehicle being sold is not trustworthy as a vehicle history.

### OPD Missing Report

**§1271 vs. §1280:** For police records, §1280 (official records exception) is the primary hearsay exception, not §1271. The distinction:
- §1271 requires custodian TESTIMONY — a live witness or §1560 affidavit
- §1280 requires: duty of public employee + at/near the time + trustworthiness — but also has a custodian requirement

**The missing report:** The absence of the 6/2/2009 OPD incident report from the official files is probative:
- If OPD's records are properly maintained and complete (§1271(a)/(d) presumption for kept records), the absence of a report for an incident means either no incident was reported, or a report was removed
- A records custodian who certifies the file's completeness cannot certify that a missing report exists
- This creates a negative implication: the report is missing from a system that should contain it

### Treasury Contradictory Letters

Each Treasury letter is a business record of a federal agency — admissible under §1271 (or the federal equivalent, FRE 803(6)) as a record of the agency's communications and positions. The four contradictory letters are each independently admissible. The contradiction between them is relevant to truth and weight, not admissibility.

**The §1271(d) argument on each:** A letter whose content contradicts official agency records (bond ownership in the official system) was prepared on a false foundation. The trustworthiness of each specific letter is undermined by its contradiction with others. This is a weight argument at trial, not an admissibility argument.

### Family Law Documents — 16-Year Audit

Unsigned court orders, backdated filings, reports with changed dates — for any document where the face date and the actual creation date diverge, §1271(b) fails. For any document created to fill a gap after the proceeding it was supposed to document, §1271(a) fails. The 16-year audit pattern is §1271(a)+(b)+(d) failure across multiple proceedings.
