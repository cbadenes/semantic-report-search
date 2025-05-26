from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .search_v0 import router as router_v0
from .search_v1_1 import router as router_v1_1
from .search_v1_2 import router as router_v1_2
from .search_v1_3 import router as router_v1_3
from .search_v2 import router as router_v2
from .search_v2_1 import router as router_v2_1

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
app.include_router(router_v1_1, prefix="/v1.1")
app.include_router(router_v1_2, prefix="/v1.2")
app.include_router(router_v1_3, prefix="/v1.3")
app.include_router(router_v2, prefix="/v2")
app.include_router(router_v2_1, prefix="/v2.1")
