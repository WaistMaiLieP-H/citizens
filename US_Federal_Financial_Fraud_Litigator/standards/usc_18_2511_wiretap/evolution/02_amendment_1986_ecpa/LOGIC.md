# Evolution Stage 02 — Electronic Communications Privacy Act of 1986 (ECPA)
## Pub. L. 99-508 — Electronic Communications Added

### THE WOUND

Between 1968 and 1986 electronic communications had exploded: facsimile machines,
computer modems, email over ARPANET/early internet, pager communications, cellular
telephone, and satellite transmission were all in commercial use by 1986. None of
these were covered by Title III's 1968 wire/oral communications framework.

The gap was not theoretical. By 1986:
- Email on ARPANET and early commercial networks carried significant business
  and personal communications — none protected by Title III
- Cellular calls were transmitted over radio frequencies — arguably not "wire"
  communications; some courts held cellular was outside Title III
- Pager messages were entirely unprotected
- Stored computer records had no protection against government or private access

Congress faced two separate problems:
1. Real-time interception of electronic communications (email in transit, cellular calls)
   → needs to be added to Title III's interception prohibition
2. Access to stored electronic communications (email in a mailbox, records on a server)
   → different timing problem; not "interception" but still privacy-sensitive
   → needed a new framework (Stored Communications Act, Title II of ECPA)

### DESIGN RESPONSE — ECPA 1986

**Electronic Communications Privacy Act of 1986 (ECPA), Pub. L. 99-508:**

**Title I — Wiretap Act Amendments:**
- Added "electronic communication" as a covered category alongside "wire communication"
  and "oral communication"
- "Electronic communication" = any transfer of signs, signals, writing, images, sounds,
  data, or intelligence ... transmitted in whole or in part by wire, radio, or
  electromagnetic system
- Cellular telephone calls = electronic communications → covered
- Email in transit = electronic communications → covered
- Pager messages = electronic communications → covered

**Title II — Stored Communications Act (SCA), 18 U.S.C. §§2701-2712:**
- Separate framework for stored communications (email in inbox, voicemail in storage)
- Lower civil remedy: $1,000 minimum + attorneys' fees + punitive
- Different access rules: government access to stored communications has lower
  constitutional threshold than real-time interception

**The interception/storage distinction (established by ECPA):**
- Real-time capture of a communication in transit → Wiretap Act
- Accessing a communication after it has been stored → Stored Communications Act / CFAA
- This distinction is critical for SIM swap: ported calls routed to attacker in transit
  = Wiretap Act; voicemail accessed on server after storage = SCA + CFAA

### LOGICAL DELTA

| Element | Pre-ECPA (1968-1986) | Post-ECPA (1986+) |
|---------|---------------------|-------------------|
| Wire voice calls | Covered | Covered |
| Cellular calls | Arguably excluded | Covered (electronic communication) |
| Email in transit | Not covered | Covered (electronic communication) |
| SMS in transit | N/A (not yet) → later covered | Covered |
| Stored email/voicemail | Not covered | Stored Communications Act (§2701) |
| Civil remedy (interception) | §2520 (actual + $10K min + fees) | Unchanged + extended to electronic |
| Civil remedy (stored access) | None | §2707 ($1,000 min + fees) |

### SIGNIFICANCE

ECPA's 1986 expansion is the foundational provision for the SIM swap Wiretap Act
theory. SMS messages in transit, cellular calls in transit — all are "electronic
communications" covered by §2511. The SIM swap's real-time rerouting of calls and
messages to the attacker's device = interception "during transmission" = Wiretap Act.

### PROVENANCE

Electronic Communications Privacy Act of 1986
Pub. L. 99-508, 100 Stat. 1848 (Oct. 21, 1986)
Title I: Wiretap Act amendments (extending to electronic communications)
Title II: Stored Communications Act (18 U.S.C. §§2701-2712)
Title III: Pen Register provisions (not covered in this standard)
