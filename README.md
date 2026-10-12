# Asteroid Intelligence Network

This project simulates a distributed system of compute nodes located on planets in the solar system. Each node detects nearby asteroids, stores them, and shares information with other planets to maintain a collective, eventually consistent asteroid database. The system is split into multiple repositories to reflect real-world distributed architecture patterns.

---

## Running Locally

Start Minikube cluster, build and push planet-node service, and apply manifests. 
```
minikube start

docker build -t <docker acc>/planet-node planet-node/ 
docker push <docker acc>/planet-node

kubectl apply -f solar-system-cluster
```

View state of current planet pods.
```
kubectl get pods -n planets
```

Use a `POST` call to `/detect` to have the planet to detect new asteroids. This currently generates 0-5 random asteroids and adds them to the planet's lo 
```
kubectl exec deploy/planet-earth -n planets -- \
  curl -X POST localhost:8000/detect
kubectl exec deploy/planet-mars -n planets -- \
  curl -X POST localhost:8000/detect
kubectl exec deploy/planet-jupiter -n planets -- \
  curl -X POST localhost:8000/detect
```

Call `/asteroids` to get the current local list of asteroids from a planet. 
```
kubectl exec deploy/planet-earth -n planets -- curl localhost:8000/asteroids
kubectl exec deploy/planet-mars -n planets -- curl localhost:8000/asteroids
kubectl exec deploy/planet-jupiter -n planets -- curl localhost:8000/asteroids
```

Call `/gossip` to have a planet contact the other planets and add their asteroids lists to the current planets local database. 
```
kubectl exec deploy/planet-earth -n planets -- curl localhost:8000/gossip
kubectl exec deploy/planet-mars -n planets -- curl localhost:8000/gossip
kubectl exec deploy/planet-jupiter -n planets -- curl localhost:8000/gossip
```

## Repositories

### planet-node
A FastAPI service that runs on each planet. This repo contains the application code and Dockerfile.

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

Each planet runs the same planet-node container, but with different environment variables (planet name, detection range). Planets detect asteroids using a stub currently, but eventually the project will use real NASA data. Planets currently store asteroid detections locally, with plans to implement Postgres in the future. Planets gossip by calling each other’s /asteroids endpoint, and the cluster converges toward a shared asteroid database.

## Future Plans: 

- **Real NASA Asteroid Data Integration:** A separate database will feed each planet only the asteroids it should detect based on orbital position.
- **AWS Hybrid Integration:** Asteroid data will be stored using S3, which the local Kubernetes planet nodes will connect to and draw data from. 
- **CRDT-Based Consistency:** Use conflict-free replicated data types to merge asteroid records without duplicates.
- **Event-Driven Architecture:** Use AWS Lambda and Eventbridge to simpulate the real time propagation of asteroid updates