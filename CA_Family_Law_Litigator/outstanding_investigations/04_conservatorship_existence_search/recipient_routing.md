# RECIPIENT ROUTING — Investigation #04 Conservatorship Existence Search

**Prepared:** 2026-04-15
**Total packets:** 9
**Delivery method default:** USPS Certified Mail, Return Receipt Requested + PDF email copy where an address is published

| # | Packet | Recipient | Address | Phone | Email | Cert-Mail | Response SLA |
|---|---|---|---|---|---|---|---|
| 01 | `01_contra_costa_probate_records_request.md` | Clerk, Probate Div., Contra Costa Sup. Ct. | A.F. Bray Courthouse, 725 Court St., Rm 103, Martinez, CA 94553 | (925) 608-1000 | probate@contracosta.courts.ca.gov | YES | 10 business days |
| 02 | `02_alameda_probate_records_request.md` | Clerk, Probate Div., Alameda Sup. Ct. | Rene C. Davidson Cthse, 1225 Fallon St., Rm 109, Oakland, CA 94612 | (510) 891-6000 | probate-dept@alameda.courts.ca.gov | YES | 10 business days |
| 03 | `03_marin_probate_records_request.md` | Clerk, Probate Div., Marin Sup. Ct. | Marin Civic Center, 3501 Civic Center Dr., Rm 113, San Rafael, CA 94903 | (415) 444-7040 | probate@marincourt.org | YES | 10 business days |
| 04 | `04_solano_probate_records_request.md` | Clerk, Probate Div., Solano Sup. Ct. | Hall of Justice, 600 Union Ave., Fairfield, CA 94533 | (707) 207-7000 | probate@solano.courts.ca.gov | YES | 10 business days |
| 05 | `05_san_francisco_probate_records_request.md` | Clerk, Probate Dept. (Rm 202), SF Sup. Ct. | 400 McAllister St., San Francisco, CA 94102 | (415) 551-4000 | probate.department@sftc.org | YES | 10 business days |
| 06 | `06_san_mateo_probate_records_request.md` | Clerk, Probate Div., San Mateo Sup. Ct. | Hall of Justice, 400 County Ctr., Redwood City, CA 94063 | (650) 261-5100 | probate@sanmateocourt.org | YES | 10 business days |
| 07 | `07_florida_statewide_guardianship_search.md` | FL Office of Public & Professional Guardians | 4040 Esplanade Way, Tallahassee, FL 32399-7000 | (850) 414-2000 | information@elderaffairs.org | YES (out-of-state) | 14 business days |
| 07b | `07_florida_statewide_guardianship_search.md` (cc) | FL Courts E-Filing Authority | myflcourtaccess.com (electronic) | — | support@flclerks.com | EMAIL | 14 business days |
| 07c | `07_florida_statewide_guardianship_search.md` (cc) | FL DOH Bureau of Vital Statistics | 1217 N. Pearl St., Jacksonville, FL 32202-4220 | (904) 359-6900 | — | YES | 30 calendar days (FL vital) |
| 08 | `08_judicial_council_form_request.md` | Judicial Council of CA — CFCC | 455 Golden Gate Ave., San Francisco, CA 94102-3688 | (415) 865-4200 | cfcc@jud.ca.gov | YES | 10 business days |
| 09a | `09_ca_doj_lps_database_inquiry.md` | CA DOJ — AG PRA Coordinator | 1300 I Street, Sacramento, CA 95814 | (916) 210-6276 | publicrecords@doj.ca.gov | YES | 10 business days (Gov. Code § 7922.535) |
| 09b | `09_ca_doj_lps_database_inquiry.md` (cc) | CA Dept. of State Hospitals — LPS Records | 1600 9th St., Sacramento, CA 95814 | (916) 654-2300 | — | YES | 10 business days |
| 09c | `09_ca_doj_lps_database_inquiry.md` (cc) | CA Dept. of Developmental Services — OLA | 1600 9th St., Sacramento, CA 95814 | (916) 654-1690 | — | YES | 10 business days |

## Priority sequence

1. **Same-day send (CRITICAL — root-mechanism investigation):** packets 01, 02, 03, 04 (home-venue cluster)
2. **Day +1:** packets 05, 06 (adjacent counties), 08 (Judicial Council), 09 (CA DOJ/DSH/DDS tri-send)
3. **Day +1 (international handoff):** packet 07 + 07b + 07c (Florida tri-send)

## Notes

- All recipients receive identical core body of the packet tailored in its own file; routing differences are captured above.
- For each certified mail envelope, retain USPS tracking number and green card; log in `response_tracker.md`.
- For email sends, request read-receipt and save sent-item PDF.
- If any clerk's office refuses to conduct a name-index search, escalate via Rules of Court 10.500 written request and CCP § 1085 writ of mandate if persisted.
