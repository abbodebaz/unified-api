from fastapi import FastAPI
from app.routers import onestation, ahd, tickets, unified

app = FastAPI()

@app.get("/")
def health():
    return {"status": "OK", "message": "FastAPI is running on Railway"}

app.include_router(onestation.router)
app.include_router(ahd.router)
app.include_router(tickets.router)
app.include_router(unified.router)

