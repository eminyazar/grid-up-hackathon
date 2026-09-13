from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Grid Up Hackathon - Erken Uyarı Sistemi")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tüm domainlerden gelen isteklere izin ver
    allow_credentials=True,
    allow_methods=["*"],  # Tüm HTTP metodlarına izin ver
    allow_headers=["*"],  # Tüm header'lara izin ver
)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Grid Up Hackathon - Erken Uyarı Sistemi API'si çalışıyor. Verileri almak için /api/sensor-data endpoint'ini kullanabilirsiniz."}