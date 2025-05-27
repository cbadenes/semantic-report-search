from fastapi import APIRouter, Query
import pandas as pd
from pathlib import Path
from .search_base import format_response
from pathlib import Path
import pandas as pd
import numpy as np
from flair.embeddings import WordEmbeddings
from flair.data import Sentence
from sklearn.metrics.pairwise import cosine_similarity
from rank_bm25 import BM25Okapi


router = APIRouter()


# Load Flair embedding model
embedding = WordEmbeddings('en')  # or 'glove', 'news-forward'

@router.get("/search")
def search(q: str = Query("")):

    query_sentence = Sentence(q, use_tokenizer=True)
    embedding.embed(query_sentence)

    if not query_sentence or query_sentence[0].embedding is None:
        return {"query": q, "results": [], "total": 0}

    # Path to the reports.csv file
    reports_path = Path(__file__).resolve().parent.parent / "data" / "api" / "reports.csv"

    df = pd.read_csv(reports_path).fillna("")

    # Create tokenized keywords for BM25
    df['keyword_list'] = df['keywords'].apply(lambda x: [kw.strip().lower() for kw in x.split(',') if kw.strip()])
    tokenized_corpus = df['keyword_list'].tolist()
    bm25 = BM25Okapi(tokenized_corpus)

    # Precompute keyword embeddings
    keyword_set = set()
    for kw_list in df["keywords"]:
        keyword_set.update([k.strip().lower() for k in kw_list.split(",") if k.strip()])
    keywords = sorted(keyword_set)

    keyword_vectors = {}
    for kw in keywords:
        sentence = Sentence(kw, use_tokenizer=True)
        embedding.embed(sentence)
        if sentence and sentence[0].embedding is not None:
            vector = np.mean([token.embedding.cpu().numpy() for token in sentence], axis=0)
            keyword_vectors[kw] = vector



    query_vector = np.mean([token.embedding.cpu().numpy() for token in query_sentence], axis=0).reshape(1, -1)
    
    # Compute similarity between query and all keywords
    similarities = {}
    for kw, vec in keyword_vectors.items():
        sim = cosine_similarity(query_vector, vec.reshape(1, -1))[0][0]
        similarities[kw] = sim


    best_keyword = max(similarities, key=similarities.get)
    best_score = similarities[best_keyword]

    # Match exact keyword (compound allowed), normalized
    def matches(row):
        keywords = [kw.strip().lower() for kw in str(row["keywords"]).split(",") if kw.strip()]
        return best_keyword in keywords

    filtered = df[df.apply(matches, axis=1)].copy()

    # BM25 scores
    query_tokens = q.lower().split()
    bm25_scores = bm25.get_scores(query_tokens)

    # Combine cosine similarity and BM25 for each row
    def combined_score(row, bm25_score):
        cosine_scores = [similarities.get(kw, 0.0) for kw in row['keyword_list']]
        cosine = max(cosine_scores) if cosine_scores else 0.0
        bm25_norm = bm25_score / max(bm25_scores) if max(bm25_scores) > 0 else 0.0
        return 0.5 * cosine + 0.5 * bm25_norm

    filtered['combined_score'] = [combined_score(row, bm25_scores[i]) for i, row in filtered.iterrows()]
    results = filtered[filtered['combined_score'] > 0].sort_values(by='combined_score', ascending=False).copy()
    results.rename(columns={"combined_score": "score"}, inplace=True)

    return format_response(best_keyword, results)



