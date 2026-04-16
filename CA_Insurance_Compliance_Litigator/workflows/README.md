# CA_Insurance_Compliance_Litigator — Workflows

**Build:** Task #3 completion pass, 2026-04-15.
**Owner:** insurance-builder.
**Status:** OPERATIONAL (eight standards five-layer PUBLISHED; ADAM+EVE COUNTERSIGNED).

---

## Case workflows (live work product)

Case-specific workflow drafts are kept under `../case_workflows/` per the
Citizens schema. This `workflows/` folder holds the reusable procedural
pipelines that any case in-scope can invoke.

## Pipelines

### 1. CDI complaint pipeline (`cdi_complaint.md`)
Any §790.03(h) violation triggers a CDI Request for Assistance filing
through `insurance.ca.gov/01-consumers/101-help`. This pipeline papers:
- Violation mapping to specific §790.03(h) subsections
- Evidence schedule (claim correspondence, denial letters, phone logs)
- Parallel tracks preserved: CDI administrative, common-law bad faith,
  criminal PC §550 referral, private UCL §17200 remedy

### 2. Prop. 103 auto rate challenge (`prop_103_rate_challenge.md`)
§1861.02 (four-factor rate hierarchy) + §1861.05 (rate-change approval).
Invoked for RedJag forced-GAP-insurance yo-yo financing and any auto
rate using unapproved criteria.

### 3. Disability policy ambiguity attack (`disability_ambiguity.md`)
§10291.5(b)(1) — CDI cannot approve ambiguous policy language. If CDI
approved it and the insurer now reads an ambiguity to deny coverage,
the ambiguity is construed against the insurer.

### 4. Notice-of-loss defect waiver (`loss_notice_waiver.md`)
§553 — defects the insurer fails to timely specify are WAIVED. Used
against delay-then-deny tactics, particularly where communications
fraud (SIM swap) disrupted proof-of-loss submission.

### 5. First-party bad faith tort (`first_party_bad_faith.md`)
Gruenberg/Brandt/Tomaselli framework — unreasonable withholding +
Brandt fees + CIV §3294 punitive standard. This is the track that
survives Moradi-Shalal.

### 6. §790.03(h)(14)/(15) communications-fraud overlay
Insurer advising claimant not to obtain counsel, or misleading claimant
as to SOL, is a specifically enumerated §790.03 violation. This is
anchored to the Vernen communications-fraud record and is always
triggered where any intermediated communication is in evidence.

---

## Note

Each pipeline file above is a scaffold. Deepening to full procedural
scripts happens per-case under `../case_workflows/<case_id>/`.
