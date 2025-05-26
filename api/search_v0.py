from fastapi import APIRouter, Query
import pandas as pd
from pathlib import Path
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

    def matches(row):
        keywords = [k.strip() for k in str(row["keywords"]).split(",")]
        return query in keywords

    filtered = df[df.apply(matches, axis=1)]
    return format_response(query, filtered)
