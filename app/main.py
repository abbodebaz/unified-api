from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers explicitly
from app.routers.onestation import router as onestation_router
from app.routers.ahd import router as ahd_router
from app.routers.tickets import router as tickets_router
from app.routers.unified import router as unified_router

app = FastAPI(
    title="Unified API",
    version="1.0.0"
)

# --------------------------------
# Enable CORS (IMPORTANT for Next.js)
# --------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # يمكن لاحقًا حصره على رابط الداشبورد فقط
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------
# Routers
# --------------------------------
app.include_router(onestation_router, prefix="/onestation")
app.include_router(ahd_router, prefix="/ahd")
app.include_router(tickets_router, prefix="/tickets")
app.include_router(unified_router)  # unified already contains prefix="/unified"

# --------------------------------
# Root Health Check
# --------------------------------
@app.get("/")
def health():
    return {"status": "OK", "message": "FastAPI is running on Railway!"}
