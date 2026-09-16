from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Monsoon Guardian", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "project": "Monsoon Guardian",
        "problem_statement": "SIH26086",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
