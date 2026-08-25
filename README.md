# Board Diversity Beyond the Aggregate

A Multi-Level Analysis of FTSE 350 Firms, 2019-2024

Rahat Ahmed Bhuiyan | 001481781 | BUSI 1783 | MSc Business Analytics, University of Greenwich

## Contents

| File | Description |
|---|---|
| `FTSE350_Dissertation_Analysis.ipynb` | Analysis notebook, saved with all outputs. Produces every statistic and data-derived figure in the dissertation. |
| `FTSE_350_Firms_Anonymised.xlsx` | Firm financials. 631 rows, 49 columns; the 347 rows with a BvD identifier form the analysis frame. Sheet: `Results`. |
| `FTSE_350_Directors_Anonymised.xlsx` | Director records, one row per director-role. 15,400 rows, 9 columns. Sheet: `Results`. |
| `prepare_data.py` | Anonymises the raw ORBIS exports into the two datasets above. |
| `PRISMA_Evidence/` | Search log, database exports and screening records for the systematic review (Section 2.1). Has its own README. |

## Data source

Two exports from ORBIS (Moody's / Bureau van Dijk), taken in May 2026 under the University of Greenwich institutional subscription.

**Firms.** FTSE 350 constituents, six fiscal years of financials (2019 to 2024) stored side by side under ORBIS's relative year labels: total assets, shareholders' funds, profit/loss before tax, operating revenue, non-current liabilities, employees, NACE Rev. 2 codes, country.

**Directors.** Gender, age, nationality, appointment date and ORBIS role codes for board membership (`BoD`), senior management (`SenMan`) and the audit, remuneration and nomination committees (`AudC`, `RemC`, `NomC`).

Director names are replaced with salted SHA-256 pseudonyms by `prepare_data.py`; the salt is held on university storage, not here. The raw exports are licensed data and are not distributed.

## Data notes

Four constituents have financials but no board-coded directors and are excluded, so the notebook reports a working sample of 343 firms, not 347.

The export covers currently serving directors only, so boards reconstructed from appointment dates omit departures. Since departures over this period are disproportionately male, early-year female shares are overstated and the measured improvement is conservative. Discussed in Sections 3.3, 3.7 and 5.5.

Committee role coding is present for about 76% of firms in 2024; committee-level measures run on that subsample.

## Running it

Python 3.13.5; any 3.9 or later should work.

```bash
pip install pandas numpy matplotlib seaborn networkx statsmodels scikit-learn scipy python-calamine
jupyter lab FTSE350_Dissertation_Analysis.ipynb
```

Run top to bottom; later cells reuse earlier objects. About 90 seconds. Seeds are fixed, so results are identical across machines. `calamine` is required, as `openpyxl` cannot read the ORBIS files.

| Part | Contents | Section |
|---|---|---|
| 1 | Loading, cleaning, pseudonym checks | 3.3 |
| 2 | Four-level diversity measures; interlock network | 3.4 |
| 3 | Descriptive and longitudinal analysis | 4.1, 4.2 |
| 4 | Regressions and robustness | 4.3 |
| 5 | Director-level role allocation | 4.4 |
| 6 | Network diffusion and centrality | 4.5 |
| 7 | Random forest, clustering, PCA | 4.6 |
| 8 | Supplementary robustness and report figures | 4.2, 4.3 |
