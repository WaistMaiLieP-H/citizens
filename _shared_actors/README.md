# Shared Actor Registry

**Purpose:** Canonical registry for actors who appear across multiple Citizens. Each Citizens' `actors/` folder contains records relevant to that Citizen's domain. This shared registry links them — same person, multiple legal domains.

**Rule:** When an actor appears in more than one Citizen's domain, the canonical identity lives here. Each Citizen's local actor record references the shared registry entry. Updates to identity, aliases, and cross-domain risk flow through this registry.

**Filed:** 2026-04-08 (updated 2026-04-08)

## Cross-domain actors

| Actor | Family Law | Federal CR | CA CR | CA Civil | Shared ID |
|---|---|---|---|---|---|
| Ann Hillberg / Packard | ORCHESTRATOR | §1983 defendant | Bane Act defendant | Tort Claims | hillberg_ann |
| Christina Cerretani | OPPOSING PARTY | §1983 co-conspirator | Bane Act | — | cerretani_christina |
| Sala Ajaniku | CRITICAL (mediator) | §1983 (state actor) | — | §1094.5 (admin review) | ajaniku_sala |
| Paul Delucchi (Judge) | HIGH (adopted Ajaniku rec) | §1983 (judicial immunity) | — | §1085 (mandamus) | delucchi_paul |
| David Ditsworth, MD | HIGH (SSA report) | — | — | §340.5 (MICRA) | ditsworth_david |
| Patrick Wiita, Dr. | HIGH (competency eval) | — | — | §340.5 (MICRA) | wiita_patrick |
| Antioch PD officers | Investigation subjects | §1983 defendants | Bane Act defendants | §815.2 (entity) | apd_officers |
| Ryan McClaran | IT operator | — | — | — | mcclaran_ryan |

## Schema

Each shared actor entry is a JSON file with:
- `shared_id` — canonical identifier
- `canonical_name`, `aliases`
- `citizen_appearances` — which Citizens reference this actor and in what role
- `cross_domain_risk` — aggregate risk across all domains
- `identity_notes` — anything relevant to identity verification across domains
