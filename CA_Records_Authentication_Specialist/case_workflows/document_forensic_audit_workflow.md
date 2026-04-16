# Document Forensic Audit Workflow

## Authenticate → Evaluate → Flag → Report

---

### Phase 1: INTAKE — Receive Document for Audit

**For each document submitted to the engine:**
1. Record: source, date received, format (scan, PDF, original, copy), number of pages
2. Classify: court filing, medical record, financial document, police report, evaluation/report, correspondence, contract
3. Identify: the proceeding or transaction the document relates to

---

### Phase 2: AUTHENTICATE — Is This Document What It Claims to Be? (§1400/§1401)

**Signature check:**
- Is the document signed? By whom?
- If unsigned: can it be authenticated through other means (§1410-1421)?
- If signed: does the signature match known specimens?

**Completeness check:**
- Are all pages present? (check page numbering, headers/footers)
- Are there gaps in content that suggest missing pages?
- Does the document reference attachments or exhibits that are not included?

**Consistency check:**
- Do dates, names, case numbers, and references match across the document?
- Do they match other documents in the same matter?
- Are there internal contradictions?

**Metadata check (for electronic documents):**
- Creation date vs. stated date — do they match?
- Author field — does it match the stated author?
- Modification history — has the document been altered after creation?

**Output:** AUTHENTICATION FINDING — Authenticated / Authentication Deficient / Cannot Authenticate

---

### Phase 3: EVALUATE — Does It Meet the Standard It Claims to Meet?

**For official records (§1280):**
- Was it made by or under the direction of a public employee?
- Was it made within the scope of duty?
- Are the sources of information and method of preparation trustworthy?
- ALL THREE must be satisfied. If any fails, the official records exception does not apply.

**For evaluations/reports:**
- How many sources were reviewed? (Wiita CST: only 2 — red flag)
- Were the sources identified and verified?
- Does the conclusion follow from the evidence presented?
- Are qualifications of the evaluator documented and verifiable?

**For financial documents:**
- Do the numbers add up? (escrow statements, accountings, bank records)
- Are all transactions accounted for?
- Are there transactions that appear without authorization?

**Output:** EVALUATION FINDING — Meets Standard / Deficient (with specific deficiencies) / Fails Standard

---

### Phase 4: FLAG — Identify Specific Problems

**Flag categories:**

| Flag | Meaning | Example |
|---|---|---|
| UNSIGNED | Document lacks required signature | 19 unsigned docs in house sale |
| INCOMPLETE | Missing pages or referenced attachments | Evaluation without cited sources |
| INCONSISTENT | Internal contradictions or cross-document conflicts | Blue Shield auth naming non-existent provider |
| FABRICATED | Evidence suggests document was created to appear to be something it is not | CARFAX for wrong vehicle |
| ALTERED | Document shows signs of post-creation modification | Metadata date mismatch |
| UNVERIFIED | Claims in document cannot be verified from independent sources | SSA/DDS "phantom contact" |
| SOURCE DEFICIENT | Insufficient sources for the conclusion reached | CST report with 2 sources |

---

### Phase 5: REPORT — Generate Forensic Audit Report

**For each document audited:**
1. Document identifier (title, date, source, pages)
2. Authentication finding (with basis)
3. Evaluation finding (with specific deficiencies)
4. Flags raised (with evidence for each flag)
5. Recommended action (admissible as-is / admissible with foundation / inadmissible / requires further investigation)

**Cross-Citizen handoffs:**
- Flagged official records → CA Civil Litigator (mandamus to compel correction, §1094.5 review)
- Flagged medical records → CA Medical Privacy Officer (CMIA disclosure audit)
- Flagged financial documents → CA Conservator Investigator (§2620 accounting audit) or CA Real Estate Attorney (closing statement audit)
- Flagged custody evaluations → CA Family Law Litigator (qualification audit, §3011 factor analysis)
- Documents supporting civil rights violations → US Federal Civil Rights / CA Civil Rights (complaint drafting)
