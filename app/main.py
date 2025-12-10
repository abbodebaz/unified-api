from fastapi import FastAPI
from app.routers import onestation

app = FastAPI()

@app.get("/")
def health():
    return {"status": "OK", "message": "FastAPI is running on Railway"}

# إضافة ربط الراوتر
app.include_router(onestation.router)
