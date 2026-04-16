# Evolution Stage 02 — Technology Amendments and CCPA Era (1998-2018)
## Digital Record Systems + CCPA Private Sector Carve-Out

### THE WOUND

By the late 1990s, California state agencies had fully migrated to digital record systems.
The IPA's 1977 architecture — built around paper files and manual disclosure — had not been
updated to address:

- Automated database transfers between state agencies that occurred without any human
  review of whether the disclosure complied with IPA requirements
- Electronic systems that could generate records about individuals as a byproduct of
  other transactions (clickstream data, log files, administrative metadata)
- The California DMV's widespread sale of personal information from motor vehicle records
  to commercial data brokers — a practice that the federal Driver's Privacy Protection Act
  (1994) eventually restricted but that the IPA had not addressed clearly
- Health information in state systems that fell outside HIPAA (which only covered certain
  covered entities) but was also not clearly within IPA's protection framework

### DESIGN RESPONSE — INCREMENTAL AMENDMENTS

The Legislature addressed these gaps through a series of amendments between 1994 and 2002
rather than wholesale revision:

**Driver's Privacy Protection alignment (1995-2000):**
California amended its Vehicle Code to restrict DMV record disclosure consistent with the
federal DPPA. The IPA's framework was not the vehicle for this specific fix.

**Computer data access provisions:**
Amendments clarified that "disclosure" under §1798.24 includes electronic transfers and
that "maintenance" includes digital storage — closing the argument that automated
database-to-database transfers bypassed the IPA's disclosure restrictions.

**Sensitive information categories:**
The Legislature added or strengthened protections for specific sensitive categories —
medical information, financial information, and social security numbers — in the context
of state agency records.

### CCPA CARVE-OUT (2018-2020)

The California Consumer Privacy Act (Civil Code §§1798.100-1798.199, effective January 1, 2020)
created a comprehensive private-sector data privacy framework. The CCPA explicitly does NOT
supersede the IPA for state agency records:

- CCPA §1798.145(a)(1): The CCPA "shall not restrict a business's ability to ... comply
  with ... any California ... law" — and the CCPA's obligations apply to "businesses"
  (for-profit entities), not state agencies
- The IPA continues to be the exclusive framework for California state agency personal records
- CCPA's consumer rights (access, deletion, portability, opt-out of sale) DO NOT apply
  to state agency records; IPA access and amendment rights apply instead

### LOGICAL DELTA

| Element | Pre-1998 | Post-2000 |
|---------|----------|-----------|
| "Disclosure" | Manual records, paper | Clarified to include electronic transfers |
| DMV records | IPA ambiguous | DPPA alignment + IPA supplemented |
| CCPA era | N/A | CCPA covers private sector; IPA remains exclusive for state agencies |
| Individual liability | §1798.53 unchanged | Unchanged; $2,500 punitive per willful violation |

### WHAT CHANGED FOR DDS/CDSS

The clarification that electronic database transfers constitute "disclosures" matters
for DDS: if DDS transferred the disability claim file (including false contact records)
to SSA systems or to other California agencies without IPA-compliant authorization,
each such transfer is a separate IPA disclosure violation — potentially triggering §1798.45
per-occurrence liability.

An accounting of disclosures under §1798.40 (disclosures to other agencies over the
prior three years) can reveal the transfer chain: where the disability file went, who
had access, and whether any disclosures to non-authorized parties occurred.
