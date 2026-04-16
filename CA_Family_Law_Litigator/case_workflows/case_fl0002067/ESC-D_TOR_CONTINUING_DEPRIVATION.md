# ESC-FL0002067-D — Post-DVRO Tor-Access Denial as § 1983 Continuing Deprivation

**Escalation ref:** ESC-FL0002067-D (ADAM NF-006 → EVE-DEPUTY)
**Scope:** Statutory characterization of 2026-03-19 Tor-bridge failure telemetry during active-DVRO window (2025-08-19 → 2026-08-19) as an ongoing § 1983 injury.
**Resolution:** CHARACTERIZATION-ISSUED

---

## 1. Underlying telemetry (from ADAM NF-006)

During the active-DVRO window, endpoint exhibited selective Tor failure on 2026-03-19: three bridge types failed while baseline system connectivity tests passed. Pattern is consistent with DNS/TLS-layer targeting of anonymous-channel access from the restrained party's endpoint. Artifact: `${nonfamilylaw}/Digital_Forensics/Tor_Connection_Failures_2026-03-19/ANALYSIS.md` (sha256 `4cce4c7c5f8d1d53ce6f4fbb116e0abac4a15b40d2ea294895e627c257b46c54`).

## 2. § 1983 accrual and continuing-violation analysis

### 2.a Default rule — discrete-act accrual

A § 1983 claim accrues "when the plaintiff has 'a complete and present cause of action,'" *Wallace v. Kato*, 549 U.S. 384, 388 (2007) (quoting *Bay Area Laundry & Dry Cleaning Pension Trust Fund v. Ferbar Corp. of Cal.*, 522 U.S. 192, 201 (1997)). California's two-year personal-injury statute governs (Cal. Civ. Proc. Code § 335.1), so an isolated access denial on 2026-03-19 would, absent more, run to 2028-03-19. *Jones v. Blanas*, 393 F.3d 918, 927 (9th Cir. 2004).

### 2.b Continuing-violation doctrine — availability

The Supreme Court narrowed continuing-violation doctrine in *Nat'l R.R. Passenger Corp. v. Morgan*, 536 U.S. 101, 113–15 (2002): each discrete discriminatory act "starts a new clock"; only hostile-environment-type claims, where "a single act of harassment may not be actionable on its own" but becomes actionable only through accumulation, qualify for a true continuing-violation tolling. *Id.* at 115–17. Ninth Circuit applies *Morgan* outside Title VII to § 1983. *RK Ventures, Inc. v. City of Seattle*, 307 F.3d 1045, 1061 (9th Cir. 2002); *Pouncil v. Tilton*, 704 F.3d 568, 578–79 (9th Cir. 2012) (distinguishing continuing violations from continuing effects of discrete acts); *Bird v. Dep't of Human Servs.*, 935 F.3d 738, 746–48 (9th Cir. 2019).

### 2.c Application

The 2026-03-19 Tor failure presents as a **pattern anchor**, not a standalone discrete act, when read against:
- the CLETS footprint (ESC-B) — ongoing database-driven reputational and access consequences;
- the DVRO's in-force conditions through 2026-08-19 — a state-law restraint continuously operating on the respondent;
- the documented 16-year SIM/communications interference history (`project_communications_fraud.md`; `project_ryan_mcclaran_it.md`) — recurrent, not one-off.

Where anonymous-channel denial recurs across the DVRO window, the correct pleading posture is **per-incident accrual with a pattern overlay**: plead each confirmed failure as its own discrete § 1983 event (each starting its own two-year clock per *Morgan* / *Pouncil*), while pleading the cumulative course of conduct as evidentiary support for state-action nexus, motive, and injury magnitude. This preserves every later-confirmed incident without depending on continuing-violation tolling that *Morgan* largely forecloses.

Where the *continuing* feature is the **in-force state order itself** (the DVRO + its CLETS entry), courts recognize that an ongoing state-imposed status can supply present injury for § 1983 purposes. *Elliot-Park v. Manglona*, 592 F.3d 1003, 1007 (9th Cir. 2010) (present-effects analysis); cf. *Knick v. Township of Scott*, 588 U.S. 180, 190–91 (2019) (present constitutional injury from ongoing state action). The DVRO-window denial therefore has two accrual paths: (i) discrete-act per failure event; (ii) ongoing-status via the DVRO's continued operation, which tolls accrual of the *DVRO-as-injury* claim until the order is lifted or expires.

## 3. First Amendment anonymous-speech doctrine

- **Core right.** The First Amendment protects anonymous speech as a matter of constitutional right, not merely tradition. *McIntyre v. Ohio Elections Comm'n*, 514 U.S. 334, 341–43, 357 (1995) ("an author's decision to remain anonymous ... is an aspect of the freedom of speech protected by the First Amendment").
- **Internet as the relevant forum.** The Internet receives full First Amendment protection, with no diminished scrutiny for medium. *Reno v. ACLU*, 521 U.S. 844, 868–70 (1997). State laws that "foreclose access to social media altogether" for a class of persons "prevent the user from engaging in the legitimate exercise of First Amendment rights." *Packingham v. North Carolina*, 582 U.S. 98, 107–08 (2017).
- **Selective denial of the anonymity layer.** Where state action (directly or through complicit private carriers — see § 4) selectively disables Tor access from a specific endpoint while baseline internet connectivity remains, the state has targeted the *anonymity feature* of protected speech. That is precisely the *McIntyre* interest: the choice of anonymous mode is itself protected. Selective targeting cannot survive content-neutral scrutiny under *Ward v. Rock Against Racism*, 491 U.S. 781, 791 (1989), because it is not narrowly tailored and forecloses a whole medium of protected speech. *Packingham*, 582 U.S. at 107–08.
- **Chilling as injury.** A chill on anonymous speech is cognizable § 1983 injury where the plaintiff can show the challenged action would deter a person of ordinary firmness. *Mendocino Envtl. Ctr. v. Mendocino County*, 192 F.3d 1283, 1300 (9th Cir. 1999); *Index Newspapers LLC v. U.S. Marshals Serv.*, 977 F.3d 817, 827 (9th Cir. 2020).

## 4. State-action nexus for private-carrier / infrastructure interference

Private-carrier conduct becomes state action under § 1983 only via a recognized nexus test:

- **Public-function test.** *Jackson v. Metropolitan Edison Co.*, 419 U.S. 345, 352 (1974) — limited; unlikely to reach ordinary ISP traffic management.
- **Joint-action / conspiracy.** *Dennis v. Sparks*, 449 U.S. 24, 27–28 (1980); 9th Cir.: *Franklin v. Fox*, 312 F.3d 423, 445 (9th Cir. 2002). Plaintiff must plead specific facts of agreement or concerted conduct between carrier and state actor.
- **State-compulsion / significant-encouragement.** *Blum v. Yaretsky*, 457 U.S. 991, 1004–05 (1982); 9th Cir.: *Sutton v. Providence St. Joseph Med. Ctr.*, 192 F.3d 826, 836 (9th Cir. 1999).
- **Entwinement / pervasive entanglement.** *Brentwood Academy v. Tennessee Secondary School Athletic Ass'n*, 531 U.S. 288, 298 (2001).

**Application.** Pure private-carrier traffic shaping (e.g., generic ISP anti-Tor heuristics applied across the user base) does *not* satisfy any of these tests. What elevates the Tor denial to state action is the **selective** character — if the denial is targeted at the DVRO respondent specifically, by reference to state-database identity (CLETS/NCIC footprint per ESC-B), that is at minimum a *Dennis v. Sparks* joint-action allegation backed by the state-authored identifier. The pleading must concretely allege (i) the state-action actor or state-furnished identifier, (ii) the carrier's awareness or receipt of that identifier, and (iii) differential treatment of the plaintiff relative to similarly-situated subscribers. Absent such allegations, the claim sounds only in private tortious interference, not § 1983. EVE should note this as a *pleading-gap* item that depends on subpoena or carrier-discovery corroboration not present in the current telemetry.

## 5. Distinguishing continuing-violation from discrete-act cases

| Doctrine | When it applies | Authority | Application here |
|---|---|---|---|
| Discrete-act / per-incident accrual | Each identifiable adverse event is independently actionable. | *Morgan*, 536 U.S. at 113–14; *RK Ventures*, 307 F.3d at 1061; *Pouncil*, 704 F.3d at 578. | Each confirmed Tor denial during DVRO window = its own claim, own two-year clock. **Default posture.** |
| Hostile-environment / cumulative | Individual acts not actionable alone; actionable only in the aggregate. | *Morgan*, 536 U.S. at 115–17. | Generally unavailable outside Title VII hostile-environment theory in § 1983, per 9th Cir. *Bird*, 935 F.3d at 746–48. Do not rely. |
| Continuing effects of past discrete act | Non-tolling — lingering consequences of a single prior act do not extend accrual. | *Del. State College v. Ricks*, 449 U.S. 250, 257 (1980); *Knox v. Davis*, 260 F.3d 1009, 1013 (9th Cir. 2001). | Not the plaintiff's friend. The DVRO *issuance* is a discrete act; its later downstream effects do not toll from issuance date. |
| Ongoing-status / present-injury | Continuing in-force state order supplies present constitutional injury each day of its operation. | *Knick*, 588 U.S. at 190–91 (takings analog); *Elliot-Park*, 592 F.3d at 1007. | Available as to the DVRO + CLETS entry itself so long as the order remains in force (through 2026-08-19). Prospective / injunctive claims remain ripe throughout. |

**Recommended plead posture for the Tor telemetry:**
1. Plead each confirmed anonymous-channel denial as a discrete First-Amendment / procedural-DP violation with its own accrual date.
2. Plead the DVRO + CLETS entry as an ongoing-status deprivation (ESC-B) that is contemporaneously in force, providing both injury-in-fact for standing and an anchor for injunctive relief.
3. Plead the 16-year communications-interference history (project_communications_fraud.md) as pattern evidence (Fed. R. Evid. 404(b)(2) — motive, identity, absence of accident) supporting the Tor incident, not as a continuing-violation tolling argument.
4. Do **not** rely on hostile-environment continuing-violation tolling for § 1983 claims outside Title VII contexts; *Morgan* and 9th Cir. *Bird* foreclose it.

## 6. Residual verification flag (for EVE)

- The 2026-03-19 Tor failure is a *single confirmed event* in the current record. Additional confirmed events would strengthen the per-incident posture and provide pattern corroboration. EVE (with ADAM forensics support out of scope here) should treat further network-layer telemetry as new ESC filings, not as amendments to ESC-D.
- State-action nexus for carrier interference is **not yet pleaded-sufficient** on this record. The characterization above identifies the doctrinal path but flags the evidentiary gap. Subpoena / Rule 45 discovery against the carrier and/or a *Dennis v. Sparks* joint-action factual predicate must be developed before a § 1983 Tor-denial claim is filed as a standalone count.
- *Packingham*'s reach beyond sex-offender registries to DVRO respondents is persuasive, not directly held. EVE should pin whether any post-*Packingham* 9th Cir. or district authority has extended it to DVRO/restraining-order contexts.

## 7. Witness chain

```yaml
witness_chain:
  author: EVE-DEPUTY
  authored_at_utc: 2026-04-15T00:00:00Z
  signal: CHARACTERIZATION-ISSUED
  eve_countersign: PENDING
  custos_gate: PENDING
```
