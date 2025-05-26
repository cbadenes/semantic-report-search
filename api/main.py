from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .search_v0 import router as router_v0

app = FastAPI()

# Allow CORS for frontend access during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include versioned routers
app.include_router(router_v0, prefix="/v0")
