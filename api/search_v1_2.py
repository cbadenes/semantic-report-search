from fastapi import APIRouter, Query
import pandas as pd
from pathlib import Path
import Levenshtein
from .search_base import format_response

router = APIRouter()

reports_path = Path(__file__).resolve().parent.parent / "data" / "api" / "reports.csv"

@router.get("/search")
def search(q: str = Query("")):
    query = q.strip()

    # Load the CSV fresh on every request
    df = pd.read_csv(reports_path)
    df.fillna("", inplace=True)

    if not query:
        return format_response(query, df)

    # Extract unique keywords for fuzzy correction
    unique_keywords = set()
    for row in df["keywords"]:
        unique_keywords.update([k.strip() for k in str(row).split(",") if k.strip()])

    # Try exact match first
    def matches(row):
        return query in [k.strip() for k in str(row["keywords"]).split(",")]

    filtered = df[df.apply(matches, axis=1)]

    # If no results, apply typo correction
    if filtered.empty:
        distances = [(kw, Levenshtein.distance(query, kw)) for kw in unique_keywords]
        corrected, distance = sorted(distances, key=lambda x: x[1])[0] if distances else (query, 0)

        def fuzzy_matches(row):
            return corrected in [k.strip() for k in str(row["keywords"]).split(",")]
        filtered = df[df.apply(fuzzy_matches, axis=1)]
        return format_response(corrected, filtered)

    return format_response(query, filtered)
