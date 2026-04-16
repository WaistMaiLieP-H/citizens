# ESC-FL0002067-A — DV-130 Issuance Date Reconciliation

**Escalation ref:** ESC-FL0002067-A (ADAM NF-002 → EVE-DEPUTY)
**Scope:** Statutory date verification + workflow.json telemetry correction
**Resolution:** RECONCILED

---

## 1. Artifact verified

| Item | Value |
|---|---|
| Artifact path | `${familylaw}/2025-08-19/DV-130_Restraining_Order_After_Hearing.pdf` |
| SHA-256 | `c739e3659a6ec9c9a110920ef2c73800f64f62480345353f8b011d84c63ef47e` |
| OCR support | `${familylaw}/2025-08-19/OCR_TEXT_2025-08-19.txt` (sha256 `752cde22e11d3810fb121c52b0b429637a4c021edff648b57849163267c6f977`) |
| Court | Marin County Superior Court (3501 Civic Center Dr., San Rafael, 94903) |
| Clerk stamp | `FILED AUG 19 [2025]` — James M. Kim, Court Executive Officer, by A. Urton, Deputy (page 1, form face) |
| DV-130 Item 7.a (Hearing date) | Handwritten, rendered by OCR as `tea U9 | OS` — consistent with `08/19/[20]25` given the FILED AUG 19 stamp and lack of any other date on the face of the order |
| Item 4 (Expiration) | `2026-08-19` (reported by workflow and corroborated by 1-year default arithmetic from 2025-08-19 hearing) |

## 2. Discrepancy resolved

| Field | Original (pre-patch) | Corrected |
|---|---|---|
| `workflow.json` → `current_posture` | "ACTIVE — DV-130 granted **2025-10-17** with CLETS entry; expires 2026-08-19." | "ACTIVE — DV-130 granted **2025-08-19** with CLETS entry; expires 2026-08-19." |
| `workflow.json` → `current_posture_patch_log` | (did not exist) | New array entry appended by EVE-DEPUTY with patch metadata, reason, artifact hash, and witness flags. |

## 3. Reason for correction

- DV-130 PDF bears the Marin Superior Court `FILED AUG 19` clerk stamp and no other court filing stamp.
- The `2025-10-17` folder in `${familylaw}/` contains `FCS_Custody_Report_Recommendations.pdf` (sha256 `935e86c07a9e5a5ffc30c4c3237214ac72a11bd10262598580835854abe50690`), a separate artifact class (Family Court Services custody report), not a DV-130 order.
- One-year default DVRO term running from the 2025-08-19 hearing produces a 2026-08-19 expiration — which matches the value the workflow already carried. The `2025-10-17` "granted" assertion was therefore internally inconsistent with its own stated expiration; the `2025-08-19` correction resolves the inconsistency.
- No primary-source evidence in the workspace supports a 2025-10-17 issuance of DV-130.

## 4. Residual verification flag (for EVE / steward)

Item 7.a hearing-date handwriting was read from OCR, not from a clean certified docket. EVE should, on her next pass, obtain the Marin County Superior Court official register-of-actions entry for case FL0002067 and confirm the hearing date reads `08/19/2025`. If the certified docket shows any other hearing date, this reconciliation must be revisited. The *filing stamp* `AUG 19` is unambiguous; the *hearing date* line is OCR-inferred.

## 5. Witness chain

```yaml
witness_chain:
  author: EVE-DEPUTY
  authored_at_utc: 2026-04-15T00:00:00Z
  signal: RECONCILED
  artifact_sha256: c739e3659a6ec9c9a110920ef2c73800f64f62480345353f8b011d84c63ef47e
  workflow_patch_applied: true
  eve_countersign: PENDING
  custos_gate: PENDING
```
