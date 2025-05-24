import uvicorn
from pathlib import Path
import os

if __name__ == "__main__":
    # Ensure we launch from project root
    api_path = Path(__file__).parent / "api" / "main.py"

    # Run the FastAPI server
    uvicorn.run(
        "api.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
