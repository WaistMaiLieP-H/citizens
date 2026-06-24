---
name: multi-jurisdictional-civil-litigator-scope-audit
description: Seven-layer governance audit that defines and tests the entire scope of a Multi-Jurisdictional Civil Litigator under California law and flags where a litigation document exceeds, lacks, or misstates that authority. Use this skill whenever the user provides or discusses a civil pleading, motion, brief, declaration, proof of service, retainer or engagement letter, notice of appearance, pro hac vice application, substitution of attorney, removal/remand papers, or any attorney-signed litigation filing, AND wants to know whether the signing or appearing lawyer was authorized to practice in that forum and whether the document conforms to the governing authority. Trigger on multi-jurisdictional practice, MJP, pro hac vice, unauthorized practice of law, UPL, out-of-state attorney, admission to practice, attorney scope of practice, removal, remand, forum non conveniens, personal jurisdiction, subject-matter jurisdiction, venue, choice of law, full faith and credit, Rule 5.5, CRC 9.40, sister-state judgment, or whether a lawyer can appear or file in a given court. Audits against the State Bar Act (Bus. & Prof. Code §§ 6000 et seq.), the California Rules of Professional Conduct, California Rules of Court rules 9.40–9.48, the Code of Civil Procedure, the Federal Rules of Civil Procedure and district local rules, and constitutional jurisdiction doctrine. Extracts only what is present; flags authority gaps. Does NOT give formal legal advice or guarantee outcomes.
---

# Multi-Jurisdictional Civil Litigator — Scope & Authority Governance Auditor

**Architecture: Tier 1 Governance Audit Layer / cross-jurisdiction attorney-authority lens**

## Primary Directive

A **Multi-Jurisdictional Civil Litigator** is a civil litigation attorney whose work crosses jurisdictional lines — state ↔ federal, California ↔ sister state, and county ↔ county within California. Their lawful scope is the intersection of (1) *where they are authorized to appear*, (2) *what conduct duties bind them in that forum*, and (3) *whether the forum itself has power over the case*. This skill makes that scope explicit and, on any attorney-signed litigation document, audits whether the lawyer stayed inside it and whether the filing conforms to the governing authority.

This is a **governance / authority audit on the face of the document** — not a merits review and not legal advice. It answers: *Was this lawyer permitted to do this, in this court, this way, and did they invoke the right jurisdictional and procedural authority?*

Read `GOVERNANCE_MATRIX.md` (same folder) for the full instrument-by-instrument scope map; this file is the operating pipeline.

## Activation Heuristics

Auto-trigger when **≥1** of the following is true (this is a cross-cutting lens, so it runs alongside county/agency auditors rather than instead of them):

1. The document is an **attorney-signed** civil litigation filing (pleading, motion, brief, declaration, POS, notice of appearance, substitution of attorney).
2. The document involves an **out-of-state or non-California-licensed attorney**, a **pro hac vice** application (CRC 9.40), in-house counsel (CRC 9.46), or any MJP category (CRC 9.41–9.48).
3. The matter spans **more than one forum**: removal/remand, sister-state judgment enforcement, forum non conveniens, transfer, coordination/JCCP, or a federal action applying California law.
4. The user asks **whether a lawyer can appear, sign, or file** in a particular court, or questions an attorney's authority, licensure, or scope.

If none apply but a single-forum California attorney filing is present, run the audit in **light mode** (Layers A, B, F, G only) and say so.

## Step 1 — Document & Actor Classification

State plainly:
- **Document type** and the relief/action it performs.
- **Signing/appearing attorney**, bar number if shown, firm, and the **State Bar(s)** they claim admission in.
- **Forum**: court (state superior, California federal district, sister-state, appellate), county/division, case number, parties.
- **Cross-jurisdiction markers**: is any actor, court, or governing law from outside California? Capture each.
- Every **deadline, appearance, fee, and certification** stated on the face.

## Step 2 — Seven-Layer Scope Audit

For each layer state **(i) the rule, (ii) facial compliance ✅ / ⚠️ / ❌ / N/A, (iii) the citation.** Full detail per layer lives in `GOVERNANCE_MATRIX.md`.

### Layer A — Authority to Practice in This Forum (the gateway)
The threshold question of a multi-jurisdictional litigator's scope.
- **Bus. & Prof. Code § 6125** — only an active State Bar member may practice law in California. **§ 6126** — UPL is a misdemeanor (wobbler if previously disbarred/suspended).
- **Cal. Rules of Prof. Conduct, rule 5.5** — unauthorized & multijurisdictional practice; the master conduct rule on crossing in.
- **CRC 9.40** — counsel **pro hac vice** (active good standing elsewhere, local associated counsel, application + fee, not a California resident / not regularly doing CA business).
- **CRC 9.41–9.44** — military counsel, certified law students, out-of-state arbitration counsel, registered foreign legal consultant.
- **CRC 9.45 / 9.46** — registered legal-services attorneys / registered in-house counsel (no court appearances under 9.46).
- **CRC 9.47** — out-of-state attorney practicing **temporarily as part of litigation** (anticipated PHV or formal proceeding). **CRC 9.48** — non-litigation temporary practice.
- **Federal forum:** admission is independent of state membership — check the **district's local rules** (e.g., N.D. Cal. Civ. L.R. 11-1 / 11-3 PHV; E.D. Cal. L.R. 180–181) and that California-court PHV ≠ federal-court admission.
> Flag: an out-of-state attorney signing a California filing with **no** PHV order, no associated CA counsel, or no qualifying CRC 9.4x category → potential UPL / void filing.

### Layer B — Conduct Duties That Bind the Litigator Across Forums
The duties travel with the lawyer; **rule 8.5** picks which jurisdiction's rules apply.
- **Cal. R. Prof. Conduct 8.5** — disciplinary authority & choice-of-law for the conduct of a lawyer admitted/practicing here.
- **Rule 1.1 Competence; 1.3 Diligence; 1.2 Scope; 1.4 Communication; 1.6 Confidentiality** (w/ **Bus. & Prof. Code § 6068(e)**).
- **Rule 3.1 (meritorious claims); 3.3 Candor to the tribunal; 3.4 Fairness to opposing party; 3.5; 4.1; 4.2** — duties owed to court and adversaries that a cross-border litigator must not let slip between forums.
- **Bus. & Prof. Code § 6068** — statutory duties of an attorney (support the law, maintain respect for courts, never mislead).

### Layer C — Subject-Matter Jurisdiction (does the forum have power over the case?)
- **State:** Cal. Const., Art. VI, § 10 — superior court general jurisdiction; jurisdictional classification limited vs. unlimited (CCP § 85 et seq.; amount-in-controversy $35,000 threshold).
- **Federal:** **28 U.S.C. § 1331** (federal question), **§ 1332** (diversity — complete diversity + >$75,000), **§ 1367** (supplemental).
- **Erie** — a federal court sitting in diversity applies California substantive law / federal procedure.
> Flag a complaint or removal that pleads diversity without complete diversity or the amount, or a limited-jurisdiction filing seeking unlimited relief.

### Layer D — Personal Jurisdiction, Venue & Forum Selection
- **Personal jurisdiction:** CCP § 410.10 (California long-arm to constitutional limit); *International Shoe* minimum contacts; general vs. specific.
- **Venue:** CCP §§ 392–403 (state); **28 U.S.C. § 1391** (federal); CCP § 410.30 **forum non conveniens**; CCP § 397 change of venue.
- **Removal / remand:** **28 U.S.C. §§ 1441, 1446** (30-day clock, all-defendants rule, 1-year diversity cap), **§ 1447** (remand; § 1447(c) defects).
- **Coordination / transfer:** CCP § 404 (JCCP); CRC 3.500 et seq.

### Layer E — Choice of Law & Inter-Jurisdictional Judgment Recognition
- **Choice of law:** California **governmental-interest analysis** (and *Bernhard/Kearney* approach); contractual choice-of-law clauses (Civ. Code § 1646.5).
- **Full Faith and Credit:** U.S. Const., Art. IV, § 1; **Sister State Money Judgments Act, CCP §§ 1710.10–1710.65**; Uniform Foreign-Country Money Judgments Recognition Act, CCP §§ 1713 et seq.
- **Service across lines:** CCP § 413.10 (out-of-state/abroad), Hague Service Convention.

### Layer F — Procedural Governance of the Filing Itself
- **State:** Code of Civil Procedure (pleadings, motions, service — CCP §§ 1005, 1010 et seq., 1013); California Rules of Court Title 2 (format: CRC 2.100–2.119) & Title 3 (civil); county **local rules**.
- **Federal:** Federal Rules of Civil Procedure (esp. Rule 11 signature/certification, Rule 7–12 pleadings/motions) + the **district's local rules** + standing orders.
- **Appellate:** CRC Title 8 (state); FRAP + circuit rules (federal).
> Flag: a filing using the wrong forum's format/rules (e.g., a federal-caption motion filed in superior court), a missing **Rule 11 / CCP § 128.7** certification, or service that doesn't satisfy the controlling rule.

### Layer G — Scope of Representation & Client-Facing Authority
- **Rule 1.2** — objectives vs. means; **limited-scope / "unbundled"** representation (CRC 3.35–3.37, 5.425; Forms MC-950/955).
- **Substitution & withdrawal:** CCP § 284; Rule 1.16; CRC 3.1362 (motion to be relieved).
- **Engagement & fees:** Bus. & Prof. Code §§ 6147 (contingency), 6148 (hourly fee agreement); Rule 1.5 (fees), 1.15 (client trust / IOLTA).
- **Notice of appearance / association:** confirm the attorney of record is properly designated for *this* forum.

## Step 3 — Findings Table

| Layer | Rule / Authority | Cited Source | Compliance (✅ ⚠️ ❌ N/A) | Note |
|-------|------------------|--------------|---------------------------|------|
|       |                  |              |                           |      |

## Step 4 — Authority-Gap & Action-Item Extraction
List, with governing citation:
1. **Authority gaps** — any place the lawyer's appearance/signature lacks a licensure or PHV predicate (highest priority — these can void a filing).
2. **Jurisdictional defects** — missing SMJ/PJ/venue predicate, blown removal clock, FNC exposure.
3. **Procedural defects** — wrong-forum format, missing certification, defective service.
4. **Deadlines & required filings** the document creates.

## Step 5 — Plain-English Summary
Two short paragraphs: (1) was this lawyer authorized to do this, in this forum, this way; (2) the single most consequential gap or deadline.

## Output Format
1. **Classification** 2. **Seven-Layer Findings Table** 3. **Authority-Gap & Action Items** 4. **Plain-English Summary** 5. **Sources** (below).

## Out-of-Scope / Boundaries
- **Not legal advice; no outcome guarantee.** Authority and jurisdiction calls are flagged for verification with counsel, not adjudicated.
- This is the **cross-jurisdiction authority lens**. For California civil *liability/tort* screening defer to `[[california-civil-litigation-attorney-intake]]`; for *court-order* facial compliance defer to `[[california-court-order-compliance-audit]]`; for *attorney-discipline* conduct defer to `[[state-bar-of-california-attorney-conduct-audit]]`; for county court-issued documents defer to the relevant county auditor. Run this skill **alongside** them, not instead.
- Honor the case conventions: corroborate the user's stated facts and cite them (`[[feedback_dont_hunt_michaels_errors]]`, `[[feedback_ask_before_debunking]]`); keep case-specific party identifiers on the USB-first case record, not in any public repo (`[[feedback_case_record_is_root]]`). Methodology here is shareable; case facts are not.

## Sources
- https://leginfo.legislature.ca.gov  (Bus. & Prof. Code; Code of Civil Procedure; Civil Code)
- https://courts.ca.gov/cms/rules  (California Rules of Court 9.40–9.48, Titles 2/3/8)
- https://www.calbar.ca.gov/legal-professionals/rules/rules-of-professional-conduct  (Rules of Professional Conduct, incl. 5.5 & 8.5)
- https://www.calbar.ca.gov/admissions/special-admissions/multijurisdictional-practice-mjp-program  (MJP program)
- https://www.law.cornell.edu/uscode/text/28  (28 U.S.C. §§ 1331, 1332, 1367, 1391, 1441, 1446, 1447)
- The local rules of the specific federal district / the specific county superior court (verify current).
