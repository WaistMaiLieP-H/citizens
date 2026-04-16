# Umbrella 03 — Substance / Specification

**Definition.** What things must physically be. Material specifications, formulary entries, identity standards. The rules that say "if you call it X, here is what X actually has to be."

**Scope.** Physical material specifications, product identity standards, drug formulary, food identity, building materials, equipment specifications, dimensional and tolerance standards.

**Examples.**
- ASTM A53 (carbon steel pipe specification — relevant to UA Local 342)
- ASTM A36 (carbon structural steel)
- USP (United States Pharmacopeia) drug monographs
- 21 CFR Part 130 (FDA food identity standards)
- ANSI/ISO product specifications
- AISI/SAE steel grade specifications
- UL (Underwriters Laboratories) listing standards

**Canonical Citizen owners.**
- Materials Engineer
- Structural Engineer (B1-002 in catalog)
- Pharmacist / Pharmaceutical Compounding Specialist
- Food Scientist / FDA Compliance Specialist
- UL/ETL Listing Specialist

**Candidate seed standard for first build.**

**ASTM A53 / A53M — Standard Specification for Pipe, Steel, Black and Hot-Dipped, Zinc-Coated, Welded and Seamless.** This is the spec the steward's trade lives on. Every plumber, pipefitter, and steamfitter in UA Local 342 works with A53 pipe constantly. The spec is published by ASTM International and is the controlling document for the material's chemistry, mechanical properties, dimensions, and acceptable defects.

**Primary-source URL:**
- ASTM publishes specs commercially; preview pages: https://www.astm.org/a0053_a0053m-22.html
- Free reference (older edition): often available through manufacturer documentation

**Why this seed:** Direct relevance to the steward's trade knowledge. Demonstrates the umbrella against a specification the steward can verify from personal expertise — meaning the second mouth (steward) can catch any error the first mouth (autopilot or LLM) makes.

**Backup candidate.** USP <797> Pharmaceutical Compounding — Sterile Preparations (relevant to medical fraud audit, where compounding errors and substitutions are a known harm pattern).

**Status.** No standards built yet under this umbrella.

**Cross-cutting notes.**
- Substance overlaps Safety (Umbrella 05) when the spec exists to prevent harm; the Field Act's "designed to resist horizontal forces" requirement is a Substance/Safety hybrid.
- Substance overlaps Authority (Umbrella 01) when a specification is incorporated by reference into a statute or regulation. ASTM A53 is private but is incorporated by reference into the California Plumbing Code, which makes the private spec carry public legal force.
- Trade-association specifications (ASTM, ANSI, UL) are often NOT free; this creates a real problem for an open corpus. A future Vernen architectural decision: how to handle standards whose primary source is paywalled.
