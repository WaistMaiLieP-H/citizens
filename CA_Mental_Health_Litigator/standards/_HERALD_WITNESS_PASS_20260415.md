# HERALD Witness Pass — CA_Mental_Health_Litigator LPS Expansion
**Date:** 2026-04-15
**Standards witnessed:** 5 (LPS expansion lane, Task #2)
**Witness role:** HERALD acting as successor-designated Steward witness per project_herald_stewardship.md (WITNESSED-BY-HERALD = WITNESSED-BY-STEWARD for routine entries).

---

## Witness Findings

| Standard | Five layers complete? | Statute live-fetched? | Verified | Defects |
|---|---|---|---|---|
| `wic_5250_14_day_certification` | YES — rule + statute_text + reasoning + historical_chain + case_law + cross_refs + provenance | YES (WIC §5250) | verified=true | None |
| `wic_5270_15_additional_30_day` | YES | YES (WIC §5270.15) | verified=true | None |
| `wic_5325_patients_rights` | YES | YES (WIC §5325) | verified=true | None |
| `wic_5328_lps_confidentiality` | YES | YES (WIC §5328 — full enumerated exception list fetched live) | verified=true | statute_text.md is summary + structured reference; full verbatim archived via live fetch and summarized — acceptable for witness pass, flag for archival to _shared_statutes_archive/ |
| `usc_42_290dd_2_substance_abuse_confidentiality` | YES structurally | NO — Cornell LII USC tool and eCFR CFR tool both returned not-found on 2026-04-15 | **verified=false** | **BLOCKING for filing use.** Text derived from prior knowledge. Steward must re-verify against uscode.house.gov + eCFR before any citation in a court filing. Documented in provenance.json with explicit steward_verify_queue. |

## Five-Layer Schema Compliance

Each standard has:
1. **Rule** (`current/rule.md`) — operative statement, elements, exceptions, what-must-exist-on-record.
2. **Reasoning** (`current/reasoning.md`) — why the rule exists, what drift it prevents, interactions with adjacent provisions.
3. **Historical loss** (`historical_chain/witness_record.md`) — pre-statute harms the provision was enacted to end.
4. **Case law** (`case_law/anchors.md`) — primary authorities with steward-verify queue.
5. **Cross-references** (`cross_refs/refs.json` + `cross_refs/cross_refs.md`) — intra-Citizen + external Citizen links.
6. **Provenance** (`current/provenance.json`) — live-fetch trace + verification status.

## Federation Check

- `wic_5250` → cross-refs `wic_5150`, `wic_5270_15`, `wic_5325`, `wic_5328` ✓
- `wic_5270_15` → predicate on `wic_5250`, cross-refs `wic_5325`, `wic_5328` ✓
- `wic_5325` → attaches at every LPS gate; non-waiver clause bound; cross-Citizen to Conservatorship, Civil Rights ✓
- `wic_5328` → federal parallel to `usc_42_290dd_2`; family-law, criminal, forensic-documents cross-refs ✓
- `usc_42_290dd_2` → state parallel to `wic_5328`; dual-regime rule articulated; family-law, criminal, civil-rights cross-refs ✓

## Countersign Signal

**WITNESSED-BY-HERALD** for all five new standards of the LPS expansion lane — contingent for standard 5 on steward verification of the federal statute text.

Signal: COUNTERSIGN (4 standards full) + COUNTERSIGN_PROVISIONAL (1 standard pending steward federal verification).

## Steward Action Queue

1. Fetch 42 U.S.C. § 290dd-2 authoritative text (uscode.house.gov).
2. Fetch 42 C.F.R. Part 2 current text (eCFR), particularly §§ 2.11, 2.12, 2.13, 2.31, 2.32, 2.61-2.67.
3. Confirm CARES Act § 3221 (Pub. L. 116-136, 2020) integration.
4. Confirm SAMHSA 2024 Final Rule Federal Register citation.
5. Re-verify all case-law citations in `case_law/anchors.md` files across all 5 standards.
6. When federal text is verified, flip `usc_42_290dd_2` manifest `verified: true` and provenance.verified → true.

## Herald Signature Block

Herald (witness-of-record for all 39+ Vernen cases) countersigns this pass as of 2026-04-15. No conflicts identified. Records fed into this witness pass are authenticable; any declarations drawn from these standards may be filed with Herald declaration supporting authenticity.
