from fastapi import APIRouter, Query
import pandas as pd
from pathlib import Path
from .search_base import format_response

router = APIRouter()

# Path to the reports.csv file
reports_path = Path(__file__).resolve().parent.parent / "data" / "api" / "reports.csv"

@router.get("/search")
def search(q: str = Query("")):
    # Normalize query
    query = q.strip().lower()

    # Reload the CSV on each request to get the latest keywords
    df = pd.read_csv(reports_path)
    df.fillna("", inplace=True)

    if not query:
        return format_response(query, df)

    # Match exact keyword (compound allowed), normalized
    def matches(row):
        keywords = [kw.strip().lower() for kw in str(row["keywords"]).split(",") if kw.strip()]
        return query in keywords

    filtered = df[df.apply(matches, axis=1)]
    return format_response(query, filtered)
