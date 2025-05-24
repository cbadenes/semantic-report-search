# api/search_base.py

import pandas as pd

def format_response(query: str, results_df: pd.DataFrame):
    return {
        "query": query,
        "total": len(results_df),
        "results": results_df.to_dict(orient="records")
    }
