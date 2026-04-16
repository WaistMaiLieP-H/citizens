# NF-FL0002067-002 — DV-130 date reconciliation (workflow.json vs. artifact)

**Indexed by:** ADAM 2026-04-15
**Theory ref:** workflow.current_posture metadata integrity
**Scope flag:** IN-LANE (date-telemetry reconciliation) — **STATUTORY CHARACTERIZATION ESCALATED TO EVE**

## Discrepancy

- `workflow.json` → `current_posture`: "DV-130 granted **2025-10-17** with CLETS entry; expires 2026-08-19"
- Local artifact: `${familylaw}/2025-08-19/DV-130_Restraining_Order_After_Hearing.pdf` (not 2025-10-17)
- 2025-10-17 folder contains `FCS_Custody_Report_Recommendations.pdf` — different artifact class
- Arithmetic: 1-year DVRO from 2025-08-19 → expires 2026-08-19 ✓ (matches stated expiration)

## Artifact hashes

| Path | SHA-256 |
|---|---|
| `${familylaw}/2025-08-19/DV-130_Restraining_Order_After_Hearing.pdf` | `c739e3659a6ec9c9a110920ef2c73800f64f62480345353f8b011d84c63ef47e` |
| `${familylaw}/2025-10-17/FCS_Custody_Report_Recommendations.pdf` | `935e86c07a9e5a5ffc30c4c3237214ac72a11bd10262598580835854abe50690` |

## Escalation to EVE

Ref: `ESC-FL0002067-A`. Hearing/issuance date is a statutory fact. ADAM flags the telemetry inconsistency only; EVE verifies against the Marin official docket and, if warranted, corrects `workflow.json` `current_posture`.

## Cross-witness

EVE (required), HERALD (timeline witness).
