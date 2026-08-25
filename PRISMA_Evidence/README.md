# Systematic Review Evidence

Board Diversity Beyond the Aggregate: A Multi-Level Analysis of FTSE 350 Firms, 2019-2024

Rahat Ahmed Bhuiyan | 001481781 | BUSI 1783 | University of Greenwich

Supporting material for the systematic review reported in Section 2.1, Figure 2.1 and Appendix D of the dissertation. Every count in those places is reproducible from these files.

## Structure

| Folder | Contents |
|---|---|
| `01_workbook/` | `PRISMA_Search_Log.xlsx`, nine sheets: search strategy, stage counts, reconciliation, file manifest |
| `02_raw_exports/` | 16 unedited database exports, 2,313 records in total |
| `03_processing_logs/` | 6 files carrying each record through de-duplication, screening and eligibility |

## Raw exports

| File | Records |
|---|---|
| `scopus_string1_2026-07-18.ris` | 789 |
| `scopus_string2_2026-07-18.ris` | 126 |
| `ebsco_string1_p1-10.bib` | 500 |
| `ebsco_string1_p11.bib` to `ebsco_string1_p15.bib` (5 files, 50 each) | 250 |
| `ebsco_string1_p16.bib` | 19 |
| `ebsco_string2_p1.bib`, `ebsco_string2_p2.bib` | 73 |
| `jstor_string1_abstract_part1.ris` | 110 |
| `jstor_string1_title_part1.ris` | 38 |
| `jstor_string2_abstract.ris` | 8 |
| `pop_string1.ris` | 200 |
| `pop_string2.ris` | 200 |
| **Total** | **2,313** |

Files carry the names under which they were exported. Sheet 1 of the workbook names the export file for every search, so each row pairs with the file that produced it.

## The chain

```
2,313 identified            02_raw_exports  =  03/01_raw_pool
  - 654 duplicates          03/02_duplicates_removed  (+ 03/03_borderline for the 37 adjudicated pairs)
= 1,659 screened            03/04_screening_pool  =  03/05_screening_decisions
  - 704 excluded            03/05, Decision = Reject
= 955 assessed              03/06_eligibility_assessments
  - 949 excluded            03/06, Eligibility = Exclude
= 6 included via databases  03/06, Eligibility = Include
  + 19 via other methods    workbook Sheet 5 (13 citation-tracked, 6 regulatory)
= 25 sources in the review
```

## Notes for a reader

**Zotero item keys are not stable across collections.** Zotero mints a new key when records are copied into a new collection, so keys in `01_raw_pool` do not appear in `04_screening_pool` or `05_screening_decisions`. Files `05` and `06` share one key space; elsewhere, join on title and DOI. The record sets reconcile exactly on title.

**One duplicate title survives de-duplication, by design.** `04_screening_pool` holds 1,659 records across 1,658 distinct titles. The repeat is Magnanelli, Nasta and Karuna (2020) in the *Journal of International Accounting, Auditing and Taxation*: an article and its published discussion, same title and journal, different authors. The decision is recorded in `03_borderline_decisions_37.csv`.

**Publish or Perish exports open with a byte-order mark.** A line-anchored count of `TY  -` returns 199; the true count is 200 in both files.

**Scopus year limits were set in the query, not by coverage.** Both Scopus searches carry `PUBYEAR` limits, string 1 at 1993 to 2024 and string 2 at 1994 to 2024, visible in the query text reproduced in Sheet 1 and in Table D.2 of the dissertation. Every other database was searched over 1980 to 2024.

**Protocol deviation.** Web of Science was the planned fourth database. Institutional access provided no document search, so Business Source Premier (EBSCOhost) was substituted, with both Boolean strings held constant.
