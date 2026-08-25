"""
Anonymises the raw ORBIS exports for FTSE350_Dissertation_Analysis.ipynb.

Each director name is replaced with a salted SHA-256 pseudonym and the name
column dropped, so no raw name reaches the analysis environment. The salt is
held outside the repository and read from the environment:

    set DISS_SALT=<salt>        (macOS/Linux: export DISS_SALT="<salt>")
    python prepare_data.py

Reads FTSE_350_Export_01.xlsx and FTSE_350_Export_02.xlsx from this folder and
writes the two *_Anonymised.xlsx files. The raw exports are licensed ORBIS data
and are not distributed here.
"""

import hashlib
import os
import re
import sys

import pandas as pd

FIRMS_IN = "FTSE_350_Export_01.xlsx"
DIRECTORS_IN = "FTSE_350_Export_02.xlsx"
FIRMS_OUT = "FTSE_350_Firms_Anonymised.xlsx"
DIRECTORS_OUT = "FTSE_350_Directors_Anonymised.xlsx"

NAME_COL = "DMFull name"
ID_COL = "director_id"

# Leading honorifics stripped before hashing, so name variants resolve to one identifier.
HONORIFIC = (
    r"^(?:the\s+)?(?:rt\.?\s*hon\.?|right\s+honourable|sir|dame|lord|lady|"
    r"baron(?:ess)?|dr|prof(?:essor)?|mr|mrs|ms|miss|mx)\.?\s+"
)


def normalise(name):
    """Strip parentheticals and a leading honorific, drop periods, lower-case."""
    text = re.sub(r"\([^)]*\)", "", str(name))
    text = re.sub(HONORIFIC, "", text.strip(), flags=re.IGNORECASE)
    text = text.replace(".", "")
    return re.sub(r"\s+", " ", text.lower()).strip()


def pseudonym(name, salt):
    """Salted SHA-256 digest, truncated to 16 hex characters."""
    return hashlib.sha256((salt + "|" + normalise(name)).encode("utf-8")).hexdigest()[:16]


def main():
    salt = os.environ.get("DISS_SALT")
    if not salt:
        sys.exit("DISS_SALT is not set. See the header of this file.")

    # ---- firm file: no personal data, copied through unchanged ----
    firms = pd.read_excel(FIRMS_IN, sheet_name="Results", engine="calamine")
    firms.to_excel(FIRMS_OUT, sheet_name="Results", index=False)
    print(f"{FIRMS_OUT}: {firms.shape[0]} rows, {firms.shape[1]} columns")

    # ---- director file --------------------------------------------
    directors = pd.read_excel(DIRECTORS_IN, sheet_name="Results", engine="calamine")
    directors = directors.drop(
        columns=[c for c in directors.columns if str(c).startswith("Unnamed")]
    )
    ID_POSITION = 2                              # immediately after BvD ID number

    # ORBIS writes a repeated company identifier only on its first row.
    for col in ("Company name Latin alphabet", "BvD ID number"):
        directors[col] = directors[col].ffill()

    # Pseudonym in, name out.
    directors.insert(
        ID_POSITION, ID_COL, directors[NAME_COL].map(lambda n: pseudonym(n, salt))
    )
    directors = directors.drop(columns=[NAME_COL])

    assert NAME_COL not in directors.columns, "name column still present"
    directors.to_excel(DIRECTORS_OUT, sheet_name="Results", index=False)

    print(f"{DIRECTORS_OUT}: {directors.shape[0]} rows, {directors.shape[1]} columns")
    print(f"distinct pseudonyms: {directors[ID_COL].nunique()}")


if __name__ == "__main__":
    main()
