# Layer 2 — Reasoning
## FRE_901 | Why Authentication Matters and How Courts Apply It

**Standard ID:** FRE_901
**Filed:** 2026-04-12

---

## Why Authentication Exists

Authentication is the evidentiary law's answer to forgery, mislabeling, and chain-of-custody breaks. Before evidence is admitted, the court must be satisfied that the item in the courtroom is actually the item from the events — not a substitute, not a fabrication, not a different version. The authentication requirement is the gatekeeper for documentary and physical evidence the same way FRE 602 is the gatekeeper for testimonial evidence.

---

## The "Sufficient to Support a Finding" Standard — Low Threshold, High Stakes

The authentication threshold is low: enough that a reasonable juror could conclude the item is what the proponent claims. The judge acts as a preliminary screener under FRE 104(b) — once the threshold is cleared, authenticity goes to weight (the jury decides how much to trust it). But "low threshold" does not mean "no threshold." A document with no foundation at all — no witness who can identify it, no distinctive characteristics, no public records provenance — fails authentication and is excluded.

**In cases with complex document fraud claims (like Honeysuckle), this matters enormously:** The steward must be able to put every key document in front of a court with a path to authentication. HERALD maps that path for each document.

---

## Authentication via Personal Knowledge — FRE 901(b)(1)

For every document the steward personally received, signed, or submitted, FRE 901(b)(1) authentication is available: the steward testifies "I received this document at the closing on October 6, 2023." That testimony is sufficient to support a finding that the document is what it is claimed to be.

**The scope:** FRE 901(b)(1) authenticates that the document is the one the witness received — not that it is accurate, not that it was not altered after receipt. Subsequent alteration is a separate issue (FRE 901(b)(4) — condition suspicious of authenticity = may be inadmissible as ancient document; or expert testimony about alteration under FRE 901(b)(3)).

---

## Distinctive Characteristics — FRE 901(b)(4) — The Most Flexible Method

Courts have used distinctive characteristics to authenticate:
- Emails: email address, header information, writing style, reply chain, account log
- Text messages: phone number, contact name, thread continuity
- Documents: letterhead, account numbers, routing numbers, format consistent with known authentic documents
- Recordings: voice recognition + content knowledge + circumstances

**Limitation:** Distinctive characteristics alone may not be sufficient for high-stakes documents. Courts sometimes require additional foundation. HERALD flags documents that rely solely on distinctive characteristics without a witness-with-knowledge backup.

---

## Telephone Conversations and Electronic Communications — FRE 901(b)(5)/(6)

FRE 901(b)(5) allows a lay witness to identify a voice in a recording based on personal familiarity acquired at any time (not just for the litigation). FRE 901(b)(6) covers telephone conversations to assigned numbers.

**Application to the SIM swap/MDM track:** The steward's documentation of the SIM swap history involves phone account records and potentially recorded conversations. Authentication requires:
- The phone numbers were assigned to the parties at the relevant times (FRE 901(b)(6)) — established through AT&T/Sprint/T-Mobile account records
- Voice identification if calls were recorded (FRE 901(b)(5)) — established through personal familiarity
- The account records themselves are authenticated through FRE 901(b)(7) or FRE 903(6) business records

---

## Public Records Authentication — FRE 901(b)(7)

A record is authenticated as a public record if it purports to be from the office where records of that kind are kept, or was actually filed in a public office. Court documents, agency letters, and certified copies of government records qualify.

**The self-authentication rule — FRE 902:** Certain documents are self-authenticating and do not require extrinsic authentication evidence:
- Certified copies of public records (FRE 902(4))
- Official publications (FRE 902(5))
- Trade inscriptions (FRE 902(7))
- Acknowledged instruments (FRE 902(8))

HERALD flags: CalVCB letters, court orders, and police reports obtained directly from the issuing agency are publicly-sourced and may be self-authenticating under FRE 902(4) if certified.

---

## The Authentication Failure — Unsigned Documents

The unsigned police reports in the steward's cases fail authentication in the following specific way:

**FRE 901(b)(7) path:** The reports can be authenticated as records from APD/OPD — they came from the agencies, and an agency custodian could certify them. This authenticates them as *documents produced by the agency*, not as *accurate accounts by the named officer*.

**The gap:** Authentication proves the document is what it is said to be (a document produced by APD). It does not prove:
- That the officer named in the report actually wrote it
- That the content was not altered between reporting and filing
- That the unsigned portions represent official findings vs. draft language

The unsigned status does not prevent authentication under FRE 901(b)(7) — it goes to weight, not admissibility. But the trustworthiness challenge under FRE 803(8) (hearsay exception for public records) allows HERALD to challenge these documents' admissibility for their truth: an unsigned report lacks the indicia of trustworthiness that gives public records their reliability premium.

---

## California Parallel — Cal. Evid. Code § 1400

California Evidence Code § 1400 provides:

> "Authentication of a writing means (a) the introduction of evidence sufficient to sustain a finding that it is the writing that the proponent of the evidence claims it is or (b) the establishment of such facts by any other means provided by law."

Same standard as FRE 901(a) — "sufficient to sustain a finding." Cal. Evid. Code §§ 1410–1421 provide specific authentication methods for California proceedings.

**HERALD standard:** Build CAL_EVID_1400 as a separate standard (it is in the priority queue). Cross-reference the FRE 901 analysis above to the California framework when drafting California-specific authentication declarations.
