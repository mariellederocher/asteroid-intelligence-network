# Asteroid Intelligence Network

This project is a multi-repository distributed system that simulates computing nodes located on planets in the solar system. Each node detects nearby asteroids, stores them, and shares information with other planets to maintain a collective, eventually consistent asteroid database. The system is split into multiple repositories to reflect real-world distributed architecture patterns.

---

## Repositories

### planet-node
A FastAPI microservice that runs on each planet. This repo contains the application code and Dockerfile.

- Detects asteroids within its configured range
- Stores asteroid data 
- Gossips with other planets to synchronize records
- Exposes `/detect`, `/asteroids`, `/gossip`, `/health`

### solar-system-cluster
Kubernetes manifests that deploy the planets. This repo contains the infrastructure that runs the planet-node service.

- Namespace definition
- ConfigMap with detection ranges 
- Deployments for Earth, Mars, Jupiter
- ClusterIP services for interplanet communication
- Gossip CronJob to trigger periodic synchronization

## How It Works

Each planet runs the same planet-node container, but with different environment variables (planet name, detection range).
Planets detect asteroids using a stub currently, but eventually the project will use real NASA data.
Planets store asteroid detections locally currently , with plans to implement Postgres in the future. 
Planets gossip by calling each other’s /asteroids endpoint.
The cluster converges toward a shared asteroid database.

## Future Plans: 

- **Real NASA Asteroid Data Integration:** A separate database will feed each planet only the asteroids it should detect based on orbital position.
- **AWS Hybrid Integration:** Asteroid data will be stored using S3, which the local Kubernetes planet nodes will connect to and draw data from. 
- **CRDT-Based Consistency:** Use conflict-free replicated data types to merge asteroid records without duplicates.
- **Event-Driven Architecture:** Use AWS Lambda and Eventbridge to simpulate the real time propagation of asteroid updates