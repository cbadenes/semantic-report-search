from pathlib import Path
import pandas as pd
from rank_bm25 import BM25Okapi
from fastapi import APIRouter, Query
from .search_base import format_response

# Load dataset
data_path = Path(__file__).parent.parent / "data" / "api" / "reports.csv"
df = pd.read_csv(data_path).fillna("")

# Preprocess keywords as token lists
df['keyword_list'] = df['keywords'].apply(lambda x: [kw.strip().lower() for kw in x.split(',') if kw.strip()])
tokenized_corpus = df['keyword_list'].tolist()

# Build BM25 index
bm25 = BM25Okapi(tokenized_corpus)

# FastAPI router
router = APIRouter()

@router.get("/search")
def search_bm25(q: str = Query("")):
    if not q.strip():
        return format_response(q, df)

    query_terms = q.lower().split()
    scores = bm25.get_scores(query_terms)
    df['score'] = scores

    results = df[df['score'] > 0].sort_values(by='score', ascending=False)
    return format_response(q, results)
