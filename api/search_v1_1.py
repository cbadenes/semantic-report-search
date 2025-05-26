from fastapi import APIRouter, Query
import pandas as pd
import spacy
from pathlib import Path
from .search_base import format_response

router = APIRouter()

reports_path = Path(__file__).resolve().parent.parent / "data" / "api" / "reports.csv"

nlp = spacy.load("en_core_web_sm")

@router.get("/search")
def search(q: str = Query("")):
    query = q.strip()

    # Load the CSV fresh on every request
    df = pd.read_csv(reports_path)
    df.fillna("", inplace=True)

    if not query:
        return format_response(query, df)

    doc = nlp(query.lower())
    lemma = doc[0].lemma_ if doc else ""

    def matches(row):
        return lemma in [k.strip() for k in str(row["keywords"]).split(",")]

    filtered = df[df.apply(matches, axis=1)]
    return format_response(lemma, filtered)
