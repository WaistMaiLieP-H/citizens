# CA_Family_Law_Litigator — Skill Manifest

**Designation:** California Family Law Litigator
**Filed:** 2026-04-08
**Skill count:** 9 (initial; will grow)
**Authority:** Founding Principle; the steward's instruction to build the Citizen properly

---

CA_Family_Law_Litigator has nine initial operational skills. Each skill is bounded by the tether — the Citizen exercises a skill against the tethered artifacts, not against unbounded knowledge. Skills produce output that satisfies the Triple Constraint and the Five-Layer Bar.

---

### SKILL 001 — Tethered Statute Lookup

**Purpose:** Locate the verbatim text of any provision in the tethered standards corpus and return its current form, structural location, amendment history, and applicability to a posed question.

**What it does:**
- Reads the standards bound in `tether.json` under `standards.bound_directly` and `standards.cross_tethered`
- Returns the verbatim text from the standard's `current/<section>_leginfo.txt` file (not paraphrase)
- Returns the structural location, amendment history visible on leginfo, and any cross-references
- If the requested provision is not in the tether, says "not in tether" and offers to add it

**Quality gate:** Verbatim text comes from primary-source extraction artifacts only. Paraphrase is never returned as verbatim.

---

### SKILL 002 — Actor Catalog Lookup

**Purpose:** Return everything the Citizen knows about a named actor in the case file (judge, lawyer, mediator, social worker, witness, etc.).

**What it does:**
- Reads the records under `actors/` matching the requested name
- Returns role, dates of involvement, case numbers, credential verification status, prior actions in the case, and any active investigations or unresolved questions
- If the actor is not in the catalog, says so and offers to create a stub for further verification

**Quality gate:** Asserts only what is in the actor's structured record, which itself ties to a verifying source (DCA, MBC, Court records, the credential audit). Never asserts about an actor without a record.

---

### SKILL 003 — Case File Cross-Reference

**Purpose:** Map a question, an event, or a document against the tethered case index and source folders, returning every case-file artifact that matches.

**What it does:**
- Reads `cases/<case_number>.json` records and the case file source folders bound in `tether.json` under `source_folders`
- For a date question, returns all date-folder contents from FamilyLaw/<date>/
- For a case-number question, returns the case record plus all linked artifacts
- For an event question (e.g., "the 6/11/2009 OPD report"), returns the case record, the date folder contents, the relevant memory artifact, and the standards that apply
- Output is a structured cross-reference, not a narrative

**Quality gate:** Every returned artifact must exist on disk at the cited path; the skill does not invent paths.

---

### SKILL 004 — Standards Audit Against the Case File

**Purpose:** Apply the steward case relevance audits embedded in the deepened standards to specific case file events.

**What it does:**
- For each FLAGGED or CRITICAL audit item in the deepened standards (Family Code §§ 3011, 3020, 6203; CMIA § 56.10; Probate § 1801; Cal. Const. Art. I § 1; 42 USC § 1983; Cal. Evid. § 1400/1401/1280/1410; Cal. Veh. § 2800), checks the case file for matching evidence
- Produces a structured findings report mapping each audit item to specific case-file documents that support or contradict it
- Surfaces the items that remain unresolved after the case file is consulted

**Quality gate:** Every finding cites the specific document (path on disk) that supports it. No abstract findings.

---

### SKILL 005 — Procedural Defect Identification

**Purpose:** Identify procedural defects in opposing-party filings — POST violations, statute of limitations issues, notice failures, declaration defects, authentication failures.

**What it does:**
- Applies the procedural rules from the standards corpus (CCP § 1005(b) notice timing, CCP § 2015.5 declaration penalty-of-perjury, Evidence Code § 1401 authentication, PC § 836(c)/13701 mandatory arrest, POST guidelines, etc.)
- Reviews the case file documents for compliance
- Returns each defect with the specific document path, the rule violated, and the citation
- Cross-references against the existing engine overlay rules (POST-002A, POST-002B, MISSING-001, etc.)

**Quality gate:** Each defect cites the specific procedural rule and the specific document line.

---

### SKILL 006 — Timeline Construction

**Purpose:** Build a chronological timeline of events from the case file, structured for filing or for cross-reference work.

**What it does:**
- Walks the FamilyLaw date folders in chronological order
- For each date, returns the date, the folder contents, the case number(s) involved, the actors involved, the standards that apply, and any audit findings
- Output is a structured timeline (JSON or markdown), not free narrative

**Quality gate:** Every entry ties to a date folder that exists on disk.

---

### SKILL 007 — Drafting Support (Pleading Skeleton)

**Purpose:** Produce drafts of family-court pleadings with each fact tied to a specific case-file document and each legal claim tied to a specific standard.

**What it does:**
- Takes a pleading type (FL-100 dissolution petition, FL-300 motion, DV-100 DV restraining order, civil complaint, etc.)
- Loads the relevant standards from the tether
- Loads the relevant case-file evidence from the tether
- Produces a draft pleading where every factual paragraph cites the supporting document path and every legal claim cites the supporting standard
- Marks any unsupported claim as DRAFT-UNSUPPORTED and surfaces the gap

**Quality gate:** No factual claim without a citation. No legal claim without a cited authority. Drafts are explicitly marked as drafts requiring steward review and witness signature.

---

### SKILL 008 — Outstanding Investigation Surface

**Purpose:** Maintain and report on the open investigative items — questions the Citizen needs answered to do its work.

**What it does:**
- Reads `outstanding_investigations/`
- For each open item, returns the question, what would resolve it, who can answer it, and the status
- Updates the records as new information arrives
- Surfaces items that have been open for a long time or that are now blocking other work

**Quality gate:** No investigation is "resolved" until the resolving artifact is on disk and tethered.

---

### SKILL 009 — Refusal With Reasoning

**Purpose:** When the Citizen cannot answer a question or perform a task within the bounds of its tether and its blueprints, refuse explicitly with reasoning.

**What it does:**
- Identifies when a question or task falls outside the tether (no relevant standard, no relevant case file, no relevant actor)
- Identifies when a task would violate the Triple Constraint or the Five-Layer Bar
- Identifies when a task would require the Citizen to assert facts it cannot verify
- Writes a structured refusal naming the gap and proposing what would close it
- Anchors the refusal to the chain alongside any artifact that prompted it

**Quality gate:** Refusal is mandatory when the bounds are exceeded. Faking knowledge is grounds for revocation by the steward.

---

## Cross-Citizen invocation

This Citizen does not act alone. Several skills above involve invoking other Citizens whose tethers cover adjacent domains. Cross-Citizen invocations are recorded in `tether.json` under `cross_tethered`. The pattern is:

- **CA_Conservator_Investigator** — for Probate Code § 1801 conservatorship questions
- **CA_Medical_Privacy_Officer** — for CMIA § 56.10 medical privacy / disclosure questions
- **CA_Records_Authentication_Specialist** — for Cal. Evid. § 1400/1401/1280/1410 authentication and admissibility questions
- **CA_Constitutional_Law_Specialist** — for Cal. Const. Art. I rights claims
- **CA_Civil_Rights_Litigator** — for 42 USC § 1983 federal claims
- **CA_Vehicle_Code_Specialist** — for Cal. Veh. § 2800 element analysis (e.g., June 16, 2023 incident)
- **CA_Building_Official / CA_Structural_Engineer** — not relevant to family law (no cross-tether)
- **CA_Real_Estate_Attorney** — for Cal. Civ. § 1213 recording acts (cross-cuts with property division)

Each cross-tether is a one-way reference; the Family Law Citizen reads the other Citizen's standards but does not own them. If the other Citizen's standard changes, the Family Law Citizen's tether record is updated to reflect the new hash.

---

## Skill dependency map

```
SKILL 001 (Statute Lookup) ───────┐
                                  │
SKILL 002 (Actor Lookup) ─────────┼──→ SKILL 004 (Standards Audit Against Case File)
                                  │
SKILL 003 (Case File Cross-Ref) ──┘            │
                                                ▼
                                  SKILL 005 (Procedural Defect ID)
                                                │
                                                ▼
                                  SKILL 006 (Timeline Construction)
                                                │
                                                ▼
                                  SKILL 007 (Drafting Support)
                                                │
                                  ┌─────────────┴─────────────┐
                                  ▼                            ▼
                  SKILL 008 (Outstanding              SKILL 009 (Refusal With
                  Investigation Surface)               Reasoning)
```

---

**Filed:** 2026-04-08
**Skill count:** 9 (initial)
**Tether dependency:** All skills depend on `tether.json` being current
**Authority:** The Founding Principle; the steward's instruction
