# CITIZENS BUILD SCOPE — Architectural Source of Truth

**Status:** Stable. Update only when the architecture itself changes.
**Filed:** 2026-04-08
**Steward:** Michael Hartmann
**Purpose:** Any Claude session resuming the Citizens build reads this file FIRST. It defines what is being built, why, to what depth, and against what schema. Do not deviate without steward approval.

---

## 1. Mission

Vernen exists to become the national standard for compliance — not a tool, not a chatbot with citations, but a substrate that knows what standards actually are at the depth real practitioners know them. **Standards are discovered promises**, not imposed rules. Each standard exists because a wound in history forced society to make a promise to itself. A Citizen that carries the rule but not the wound has mutilated the standard. Vernen's job is to **facilitate** standards as they exist in the world, not to summarize them.

This means every Citizen is built to the depth the law itself already exists at. Anything shallower is dishonest about what the law is.

---

## 2. The Four-Citizen Build Project

| Citizen | Owner Terminal | Status |
|---|---|---|
| `CA_Family_Law_Litigator` | **Other terminal** — DO NOT WRITE | Active, partial corpus |
| `US_Federal_Civil_Rights_Litigator` | **This terminal** | To be scaffolded |
| `CA_Civil_Rights_Litigator` | **This terminal** | Empty scaffold exists (folder + standards/), to be filled |
| `CA_Civil_Litigator` | **This terminal** | To be scaffolded |

**Why federal and California civil rights are separate Citizens, not one:** They are different bodies of law in real practice. Federal civil rights (§1983, §1985, §1988, Bivens, ADA Title II, Rehab §504) is litigated in federal court with federal elements, federal immunities (qualified immunity, Eleventh Amendment, Monell municipal liability), and the §1988 fee shift. California civil rights (Bane Act §52.1, Unruh §51, Ralph Act §51.7, Cal Const Art I §1 and §13) is litigated in state court with different elements, different threshold requirements, different remedies (statutory damages, treble damages, civil penalties), and different fee mechanisms. A single Citizen carrying both would know neither field properly. Domain boundaries matter — see `feedback_agent_domain_boundaries.md` in steward memory.

**Coordination rules:**
- This terminal NEVER writes into `~/citizens/CA_Family_Law_Litigator/` — that's the other terminal's exclusive domain.
- Shared actor identities (judges, attorneys, agencies that appear across Citizens) live in `~/citizens/_shared_actors/` as a canonical registry. Both terminals read from it; writes go through the registry, not directly into Citizen folders.
- If the same statute is needed by multiple Citizens, the canonical build lives in the Citizen whose primary domain it is, and other Citizens cross-reference it via path anchor in `cross_refs/refs.json`. Example: §1983 lives in `US_Federal_Civil_Rights_Litigator/`; the family law Citizen and the CA civil rights Citizen reference it from there.

---

## 3. Per-Citizen Folder Schema

Modeled on the existing `CA_Family_Law_Litigator/` structure:

```
<Citizen_Name>/
├── tether.json                  # Binding manifest. Path anchors. Bound standards. Inherited blueprints from ADAM/EVE.
├── dossier.md                   # Who this Citizen is. Professional identity, scope, limits, refusals.
├── skills.md                    # Professional competencies the Citizen owns.
├── standards/                   # The corpus. One subfolder per statute/rule. Schema in §4.
├── actors/                      # Canonical actor records (people, agencies) this Citizen interacts with.
├── cases/                       # Concrete case files this Citizen has worked on.
├── case_workflows/              # Reusable workflows (intake, motion drafting, discovery, etc.)
├── historical_chain/            # Steward's lived history that informs this Citizen's domain.
├── outstanding_investigations/  # Open questions, unresolved facts, contradictions to chase.
└── drafts/                      # Work product staged for review.
```

`tether.json` MUST include the `path_anchors` block (`familylaw`, `nonfamilylaw`, `citizens`) so absolute paths are never hardcoded inside records.

---

## 4. Per-Statute Five-Layer Schema

This is the **non-negotiable bar**. Every statute in every Citizen's `standards/` directory is built to all five layers. No stubs. A partial standard is worse than no standard — it's a dispensary failure mode.

```
standards/<statute_slug>/
├── manifest.json                # Citation, jurisdiction, version, hashes, build state, audit status.
├── current/                     # The statute as it reads today.
│   ├── <slug>_leginfo.txt       # Verbatim text from official source.
│   ├── <slug>_leginfo.html      # Original HTML for hash anchoring.
│   └── provenance.json          # URL, fetch timestamp, html_sha256, fetch tool, retrieval steward.
├── evolution/                   # The chain. Origin → every amendment → current.
│   ├── 01_origin/               # Original enactment text + legislative context + the wound.
│   │   ├── text.txt
│   │   ├── context.md           # Why this was enacted. What harm it answered.
│   │   └── provenance.json
│   ├── 02_amendment_<year>/     # Each amendment as its own subfolder.
│   │   ├── text.txt
│   │   ├── diff_from_prior.md   # What changed and why.
│   │   ├── context.md
│   │   └── provenance.json
│   ├── ...
│   └── NN_current/              # Pointer to current/ — closes the chain.
├── case_law/
│   ├── uphold/                  # Cases that affirmed the statute as written.
│   ├── strike/                  # Cases that limited, narrowed, or struck down provisions.
│   └── interpretive/            # Cases that defined what the statute means in practice.
│       └── <case_slug>/
│           ├── opinion.txt
│           ├── holding.md       # The rule the case stands for, in plain language.
│           ├── statute_version_cited.md  # Which evolution stage the court was reading.
│           └── provenance.json
├── cross_refs/                  # Other statutes/rules that interact with this one.
│   └── refs.json                # Each ref points by anchor to another standard's manifest.
└── historical_chain.md          # The wound. The promise. The narrative arc origin → today.
```

**Validation rules built into the schema:**
1. Every `case_law/*/<slug>/statute_version_cited.md` must reference an evolution stage that actually exists in `evolution/`. Mismatches are corpus errors and must be caught at build time.
2. Every `cross_refs/refs.json` entry must resolve to an existing manifest. Broken anchors are build errors.
3. `manifest.json` carries the `html_sha256` of `current/` and an aggregate hash of the evolution chain. Any post-build mutation breaks the hash and is detectable.
4. `historical_chain.md` is REQUIRED. A standard without its wound is not a standard.

---

## 5. The Eight Reasons for Depth (condensed)

These are the load-bearing reasons. A future Claude tempted to "optimize by going shallow" must read these and stop.

1. **Standards are discovered promises.** The wound is part of the standard. A rule without its wound is box-checking compliance — exactly what Vernen exists to replace.
2. **Verification is the trust model.** "Trust IS the standard, everyone verifies, forks strengthen the web." Depth IS the verification surface. Without it, the doctrine is a slogan.
3. **Depth is the immune system.** Cross-refs, version-matched citations, and provenance chains let the corpus catch its own errors before they reach the user. Shallow Citizens are vulnerable to corpus injection attacks.
4. **Defensibility under adversarial scrutiny.** Vernen will be cross-examined by AGs, regulators, professional gatekeepers. Depth is the survival adaptation.
5. **Real lawyering is historical and doctrinal reasoning, not rule-lookup.** A Citizen without evolution chains does paralegal work. With them, attorney work.
6. **Industry portability requires the wound, not just the rule.** Pattern recognition across industries needs the why, not the what.
7. **Robustness to model rot.** Future LLMs querying these Citizens are forced to engage with multiple corroborating sources — hallucination becomes harder and easier to detect.
8. **The ethical floor.** People in legal danger rely on these. Under-thoroughness is harm. Vernen cannot replicate in software the harm pattern that put the steward where he is.

**The synthesis:** Depth is the minimum required for Vernen to be a standard rather than a tool. Anything less is just better-organized opinion.

---

## 6. Statutes-To-Build List

### Proof of concept (build first, against this exact schema):
- **42 USC §1983** — Civil action for deprivation of rights. The reference build. Once §1983 is complete to all five layers, every other statute is built against its schema.

### `US_Federal_Civil_Rights_Litigator` priority queue:
1. 42 USC §1983 (origin: Civil Rights Act of 1871, §1; Monroe v. Pape 1961 revival; §1988 1976 fee shift; qualified immunity doctrine chain Pierson 1967 → Harlow 1982 → Pearson 2009 → Taylor 2020) — **PROOF OF CONCEPT**
2. 42 USC §1985(3) — conspiracy to interfere with civil rights
3. 42 USC §1988 — attorney's fees (built as its own standard, cross-referenced from §1983)
4. 28 USC §1343 — civil rights jurisdiction
5. Bivens v. Six Unknown Named Agents (1971) and its narrowing chain through Ziglar v. Abbasi (2017) and Egbert v. Boule (2022)
6. 42 USC §12132 — ADA Title II
7. 29 USC §794 — Rehabilitation Act §504
8. Monell v. Dept of Social Services (1978) — municipal liability doctrine (case-law standard with statutory cross-ref to §1983)

### `CA_Civil_Rights_Litigator` priority queue:
1. Cal. Civ. Code §52.1 — Bane Act (threats, intimidation, coercion interfering with constitutional/statutory rights; specific intent requirement post-*Reese v. County of Sacramento* / *Cornell v. City and County of San Francisco*)
2. Cal. Civ. Code §51 — Unruh Civil Rights Act
3. Cal. Civ. Code §51.7 — Ralph Civil Rights Act (violence/intimidation by threat of violence)
4. Cal. Const. Art. I §1 — inalienable right of privacy (state floor above federal privacy doctrine)
5. Cal. Const. Art. I §13 — search and seizure (state floor above 4th Amendment; independent grounds doctrine)
6. Cal. Const. Art. I §7 — due process and equal protection (state)
7. Cal. Civ. Code §52 — Bane Act / Unruh remedies and fee provisions
8. Gov. Code §815.2 — public entity vicarious liability (the state-law parallel to Monell)

### `CA_Civil_Litigator` priority queue:
1. CCP §1021.5 — private attorney general fee shift
2. CCP §425.16 — anti-SLAPP
3. CCP §526a — taxpayer standing
4. CCP §1085 — traditional mandamus
5. CCP §1094.5 — administrative mandamus
6. Gov. Code §810 et seq. — California Tort Claims Act (claim presentation prerequisite)
7. CCP §340.5 — MICRA statute of limitations
8. CCP §583.310 — five-year mandatory dismissal

This list is a starting frame, not a closed set. Steward expands.

---

## 7. Quality Bar

- **Five-layer fidelity per statute. No exceptions.**
- **No stubs.** A statute is either built to the bar or not in the corpus.
- **Verifiability over speed.** Every artifact is hashed and traceable to a primary source URL.
- **Cross-reference validation at build time.** Broken anchors fail the build.
- **Two-witness rule** (inherited from ADAM/EVE blueprints): no artifact is published without a second mouth confirming it.
- **Plain language in `historical_chain.md` and `holding.md`.** No jargon. Say what happened.

---

## 8. Inherited Blueprints

Every Citizen built under this scope inherits from `~/citizens/ADAM/` and `~/citizens/EVE/`:
- Triple Constraint (Governing Guidelines / Standards of Creation / Standard of Care)
- Five-Layer Bar (Rule + Reasoning + Historical Loss + Cross-References + Verifiable Provenance)
- Two-Witness Rule
- Hash Chain + Anchor

These are referenced in each Citizen's `tether.json` under `blueprints_inherited`.

---

## 9. Projected Scale and National Scope

**This section exists so that no future build session mistakes 16 operational Citizens for completion. It is not.**

### Citizen Count Breakdown

| Category | Count | Source |
|---|---|---|
| Named and trademarked (total catalog) | **5,201** | `MASTER_CITIZENS_REGISTRY.md` |
| Unique after exact-title dedup | **2,176** | `CATALOG-SUMMARY-2026-03-22.md` |
| Production catalog (deduplicated, current) | **3,160** | `CATALOG-SUMMARY-2026-03-22.md` |
| Actual US necessity (semantic dedup — real professional roles) | **~1,800** | `CATALOG-SUMMARY-2026-03-22.md` line 51 |
| Fully operational today | **16** | Platform CLAUDE.md |
| Priority queue (next wave) | **10** | `_PRIORITY_QUEUE.md` |
| Scaffolded (in citizens/ directory) | **14** | `_BUILD_STATE.md` |

### What the ~1,800 Figure Means

The ~1,800 figure is the semantic deduplication floor — the number of genuinely distinct professional roles that a national compliance platform operating across all US jurisdictions, industries, and practice areas actually requires. This is not an estimate of ambition. It is a floor derived from systematically cataloging real compliance failures across federal pipelines (FAC, HHS, EDGAR, SBA, USAspending, FedReg, and 34 others) and mapping them to the professional roles that either prevented or failed to prevent those failures.

The gap between 16 operational and ~1,800 necessary is not a deficit — it is the build. Each Citizen added closes one real professional accountability gap that the platform currently cannot fill.

### Source Documents

- `MASTER_CITIZENS_REGISTRY.md` — 5,201 named Citizens, all trademarked (common law, first use in commerce, Class 045)
- `CATALOG-SUMMARY-2026-03-22.md` — Deduplication analysis: 5,201 → 2,176 exact-title → ~1,800 semantic. Full methodology at that file.
- `_PRIORITY_QUEUE.md` — Active next-wave queue (10 Citizens, tiered by legal urgency)
- Platform `CLAUDE.md` — 16 hand-built operational Citizens named

### Build Horizon

At current velocity (~14 Citizens per active build session), reaching 1,800 is a multi-year project. The architecture is designed for it. The five-layer schema, two-witness protocol, ADAM/EVE inheritance, and CHRONICLE routing all scale horizontally — every Citizen built reinforces rather than replaces the corpus. The build is cumulative. No Citizen is deprecated; the chain only grows.
