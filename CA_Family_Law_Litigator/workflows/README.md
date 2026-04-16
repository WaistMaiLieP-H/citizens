# CA_Family_Law_Litigator — Workflows

**Created:** 2026-04-15
**Citizen:** CA_Family_Law_Litigator

Operational workflows governing how this Citizen processes incoming evidence, handles agency responses, escalates obstruction, and routes cross-domain evidence to sibling Citizens.

---

| File | Purpose |
|---|---|
| `evidence_intake_trigger.md` | Maps new evidence (agency response, subpoena return, court transcript) to which investigations close and which standards need re-audit. Evidence type → investigation ID → affected standard IDs → re-audit scope. |
| `response_processing.md` | Handles four response types: positive (records received), negative (denial/no records), partial (redacted/incomplete), sealed (court-sealed). Each has defined next action, escalation path, and documentation requirements. |
| `escalation_pipeline.md` | Legal escalation when requests are ignored or denied: CPRA ignored → writ of mandate (CCP § 1085); subpoena quashed → motion to compel (CCP § 1987.1); clerk refuses correction → ex parte application (CCP § 473(d)). Includes form numbers and filing requirements. |
| `cross_citizen_handoff.md` | Routing matrix: which evidence gets forwarded to which sibling Citizens (Criminal, Probate, Mental Health, Insurance, Telecom) by investigation ID and evidence type. Includes handoff protocol. |
