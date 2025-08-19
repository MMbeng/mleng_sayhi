"""
This module contains the FastAPI application with endpoints for 
status, greeting, and summing numbers
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Simple FastAPI Server",
    description="A FastAPI server with status and greeting endpoints.",
    version="1.0.0"
)

@app.get("/status")
def get_status() -> dict:
    """Returns the server status."""
    return {"status": "OK"}

@app.get("/version")
def get_status() -> dict:
    """Returns the server status."""
    return {"status": "1.1"}

@app.get("/sayhi/{name}")
def say_hi(name: str) -> dict:
    """Greets the user with their provided name."""
    return {"message": f"Hi, {name}!"}

class SumRequest(BaseModel):
    """Request model for summing two numbers."""
    a: int
    b: int

@app.post("/sum")
def sum_numbers(data: SumRequest) -> dict:
    """Returns the sum of two numbers using a POST request."""
    return {"sum": data.a + data.b}

# Run as `fastapi run app.py`


"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import joblib
import logging
from sentence_transformers import SentenceTransformer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

app = FastAPI()

try:
    logging.info("Loading model---...")
    CLASSIFIER = joblib.load("svm.joblib")
    EMBEDDER = SentenceTransformer("all-MiniLM-L6-v2")
    logging.info("Models loaded successfully.")
except Exception as e:
    logging.critical("Failed to load models: %s", e)
    raise RuntimeError("Model loading failed.") from e

class HeadlineRequest(BaseModel):
    headlines: List[str]

LABELS = {
    0: "Pessimistic",
    1: "Neutral",
    2: "Optimistic"
}

@app.get("/status")
def get_status():
  
    logging.info("GET /status request received.")
    return {"status": "OK"}

@app.post("/score_headlines")
def score_headlines(request: HeadlineRequest):
   
    headlines = request.headlines
    logging.info("POST /score_headlines request received. Number of headlines: %d", len(headlines))

    if not headlines:
        logging.warning("Received empty headline list.")
        raise HTTPException(status_code=400, detail="No headlines provided.")

    try:
        embeddings = EMBEDDER.encode(headlines)
        predictions = CLASSIFIER.predict(embeddings)
        labels = [LABELS.get(label, "Unknown") for label in predictions]
        return {"labels": labels}
    except Exception as exc:
        logging.error("Error during prediction: %s", exc)
        raise HTTPException(status_code=500, detail="Internal server error.")"""
