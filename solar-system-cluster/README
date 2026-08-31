# Solar System Cluster

This repository is part of Asteroid Intelligence Network project:  **https://github.com/mariellederocher/asteroid-intelligence-network**. 

The Solar System Cluster defines the Kubernetes environment that hosts the distributed planet nodes. Each planet is deployed as a separate pod with its own detection range and environment configuration. The cluster simulates a miniature solar system where each planet node can detect asteroids and share information with other planets.

The application code for the planet nodes lives in: **https://github.com/mariellederocher/asteroid-intelligence-network/planet-node**

---

## How It Works

Each planet node:
- Runs the `planet-node` Python service
- Detects asteroids within its configured range
- Stores sightings in a local in-memory dictionary
- Periodically gossips with other planets to sync asteroid data

The cluster simulates a distributed system where nodes maintain a collective,
consistent dataset without duplicates.

## Current Features

- Planet Deployments: Each planet (Earth, Mars, Jupiter) is deployed as a standalone pod. Each pod runs the same planet-node image but with different environment variables.
- Planet Services: Every planet has a ClusterIP service that allows nodes to gossip using stable DNS names like `planet-earth.planets.svc.cluster.local`
- Shared Configuration: A ConfigMap provides detection ranges, and in future versions it will define PostgreSQL database credentials.
- Gossip CronJob: A CronJob triggers periodic gossip, ensuring the cluster gradually synchronizes asteroid data.

## How to Deploy
**Requirements:**
- Kubernetes cluster (minikube)
- kubectl
- Planet Node container images published to GitHub Container Registry: **https://github.com/mariellederocher/asteroid-intelligence-network/planet-node**
```
kubectl apply -f namespace.yaml
kubectl apply -f config/planet-config.yaml
kubectl apply -f planets/earth/
kubectl apply -f planets/mars/
kubectl apply -f planets/jupiter/
kubectl apply -f gossip/cronjob.yaml
```


