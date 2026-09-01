from fastapi import FastAPI
from .detection import detect_asteroids
from .db import save_asteroids, get_all_asteroids
from .gossip import gossip_with_peers
import os

app = FastAPI()

PLANET_NAME = os.getenv("PLANET_NAME", "unknown")
DETECTION_RANGE = int(os.getenv("DETECTION_RANGE", "0"))

# k8s health check
@app.get("/health")
def health():
    return {"status": "ok", "planet": PLANET_NAME}

# run asteroid detection
@app.post("/detect")
def detect():
    asteroids = detect_asteroids(DETECTION_RANGE)
    save_asteroids(asteroids)
    return {"planet": PLANET_NAME, "detected": asteroids}

# sync with other planets
@app.get("/gossip")
def gossip():
    updated = gossip_with_peers()
    return {"planet": PLANET_NAME, "updated_records": updated}

# list local db contents
@app.get("/asteroids")
def list_asteroids():
    return get_all_asteroids()