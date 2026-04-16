# RECIPIENT ROUTING — Investigation #11 Carrier Communications / Device Proximity

**Prepared:** 2026-04-15
**Total packets:** 8
**Delivery method default:** Email to legal-compliance inbox + USPS Certified Mail + Fax (where a carrier fax line is published). Preservation letters are TIME-CRITICAL — send all three carrier letters same-day.

| # | Packet | Recipient | Address | Phone/Fax | Email | Method | SLA |
|---|---|---|---|---|---|---|---|
| 01 | `01_att_2703f_preservation_letter.md` | AT&T Global Legal Demand Center | 11760 US Hwy 1, Ste 300, N. Palm Beach, FL 33408 | Fax (888) 938-4715 | legaldemands@att.com | Email + Cert-Mail + Fax | Ack w/in 10 biz days |
| 02 | `02_verizon_2703f_preservation_letter.md` | Verizon Wireless — VSAT | 180 Washington Valley Rd, Bedminster, NJ 07921 | Fax (325) 949-6916 | VSAT@verizonwireless.com | Email + Cert-Mail + Fax | Ack w/in 10 biz days |
| 03 | `03_tmobile_2703f_preservation_letter.md` | T-Mobile USA — LER Group | 4 Sylvan Way, Parsippany, NJ 07054 | Fax (813) 801-1793 | subpoenas@t-mobile.com | Email + Cert-Mail + Fax | Ack w/in 10 biz days |
| 04 | `04_att_subpoena_draft.md` | (same as #01) — upon issuance | (same) | (same) | (same) | Issued through case (FL0002067 or N.D. Cal. § 1983) | 30-day compliance |
| 05 | `05_verizon_subpoena_draft.md` | (same as #02) — upon issuance | (same) | (same) | (same) | Issued through case | 30-day compliance |
| 06 | `06_tmobile_subpoena_draft.md` | (same as #03) — upon issuance | (same) | (same) | (same) | Issued through case | 30-day compliance |
| 07 | `07_june16_2023_csli_narrative_request.md` | All three carriers (attached as cover to each subpoena) | — | — | — | Attach to packets 04–06 | With subpoena response |
| 08a | `08_device_proximity_preservation_request.md` (Apple section) | Apple — LE Compliance | One Apple Park Way, MS: 169-5LE, Cupertino, CA 95014 | Fax (408) 606-6555 | lawenforcement@apple.com | Email + Cert-Mail + Fax | Ack w/in 10 biz days |
| 08b | `08_device_proximity_preservation_request.md` (Google section) | Google — LIS | 1600 Amphitheatre Pkwy, Mountain View, CA 94043 | Fax (650) 249-3429 | lis-global@google.com | Email + Cert-Mail + Fax | Ack w/in 10 biz days |
| 08c | `08_device_proximity_preservation_request.md` (Microsoft section) | Microsoft — DCU / Legal Compliance | One Microsoft Way, Redmond, WA 98052 | Fax (425) 936-7329 | legal.compliance@microsoft.com | Email + Cert-Mail + Fax | Ack w/in 10 biz days |
| 08d | `08_device_proximity_preservation_request.md` (Samsung section) | Samsung Electronics America — Legal Compliance | 85 Challenger Rd, Ridgefield Park, NJ 07660 | — | legalcompliance@sea.samsung.com | Email + Cert-Mail | Ack w/in 10 biz days |

## Priority sequence

1. **Same-day (2026-04-15):** packets 01, 02, 03 — SCA preservation clocks start the moment the carrier receives the letter; do not wait.
2. **Same-day:** packets 08a, 08b, 08c, 08d — device-platform preservation.
3. **Day +1:** case-status check to confirm which vehicle (FL0002067 state subpoena vs N.D. Cal. § 1983 § 2703(d) order) is preferred; issue subpoena packets 04/05/06 with the consolidated June-16-2023 narrative (packet 07) attached.

## Notes

- Steward MUST fill `[TO BE FILLED]` MSISDN / IMEI / ICCID placeholders from historical billing records before sending.
- Retain every certified-mail tracking number, fax confirmation page, and email read-receipt in `response_tracker.md`.
- For the § 2703(d) route, N.D. Cal. requires magistrate-judge sign-off; pair with the draft § 1983 complaint at project_federal_complaint_draft.md.
- For the state-court route, pair with a § 1985.3 notice-to-consumer in FL0002067 (subscriber = steward = waiver).
