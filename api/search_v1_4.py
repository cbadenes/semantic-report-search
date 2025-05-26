from fastapi import APIRouter, Query
import pandas as pd
from pathlib import Path
from .search_base import format_response
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
from collections import defaultdict
import re
import json

router = APIRouter()

# Path to the reports.csv file
reports_path = Path(__file__).resolve().parent.parent / "data" / "api" / "reports.csv"
bigram_index_path = Path(__file__).resolve().parent.parent / "data" / "models" / "bigram_index.json"

# Cargar CSV
df = pd.read_csv(reports_path)
df.fillna("", inplace=True)

# Cargar índice de bigramas ya preprocesado
with open(bigram_index_path, "r", encoding="utf-8") as f:
    bigram_index = json.load(f)


@router.get("/search")
def search(q: str = Query("")):
    # Normalize query
    query = q.strip().lower()

    if not query:
        return format_response(query, df)
    
    last_token = q.strip().lower().split()[-1] if q.strip() else ""
    #suggestions = [w for w, _ in bigram_index.get(last_token, [])]
    top_n = 1
    suggestions = [w for w, _ in bigram_index[last_token][:top_n]]
    if not suggestions:
        suggestions = []
    query = q + " " + " ".join(suggestions)

    # Match exact keyword (compound allowed), normalized
    def matches(row):
        keywords = [kw.strip().lower() for kw in str(row["keywords"]).split(",") if kw.strip()]
        return query in keywords

    filtered = df[df.apply(matches, axis=1)]
    return format_response(query, filtered)