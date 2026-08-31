# Planet Node Service

This repository is part of Asteroid Intelligence Network project:  **https://github.com/mariellederocher/asteroid-intelligence-network**. 

The Planet Node is a Python-based FastAPI service that represents a single computing node located on a planet in the solar system. Each node detects nearby asteroids, stores sightings in a shared PostgreSQL database, and communicates with other planet nodes to maintain a consistent, distributed asteroid dataset.

This service is designed to run inside Kubernetes as part of the Solar System Cluster, but it can also be run locally for development. The Solar System Cluster code is located at **https://github.com/mariellederocher/asteroid-intelligence-network/solar-system-cluster**.

---

## Current Features

- **Fake Asteroid Detection:** When `/detect` is called, the node generates a small set of fake asteroids within a configurable detection range. 
- **Data Storage:** Asteroids are saved in a local store on each node. This is currently an in-memory dictionary, with plans to use a PostgreSQL-backed database for the full version. 
- **Gossip Between Planets:** Each node periodically contacts its peers and pulls their asteroid lists. This allows nodes to gradually converge toward a shared view of asteroid detections.
- **Docker Container:** Containerized via Docker for deployment to Kubernetes

**FastAPI Endpoints:** 
- `GET /health` — basic health check
- `POST /detect` — generate and store asteroid detections
- `GET /gossip` — pull asteroid data from peers
- `GET /asteroids` — list local asteroid records


## Running Locally

```
pip install -r requirements.txt

uvicorn app.main:app --reload --port 8000

curl -X POST localhost:8000/detect
curl localhost:8000/gossip
curl localhost:8000/asteroids
```
