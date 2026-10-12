#! /bin/bash
minikube delete --all --purge
minikube start

docker build -t md68/planet-node planet-node/ 
docker push md68/planet-node

kubectl apply -f solar-system-cluster

kubectl get pods -n planets

kubectl exec deploy/planet-earth -n planets -- \
  curl -X POST localhost:8000/detect
kubectl exec deploy/planet-mars -n planets -- \
  curl -X POST localhost:8000/detect
kubectl exec deploy/planet-jupiter -n planets -- \
  curl -X POST localhost:8000/detect

kubectl exec deploy/planet-earth -n planets -- curl localhost:8000/asteroids
kubectl exec deploy/planet-mars -n planets -- curl localhost:8000/asteroids
kubectl exec deploy/planet-jupiter -n planets -- curl localhost:8000/asteroids

kubectl exec deploy/planet-earth -n planets -- curl localhost:8000/gossip
kubectl exec deploy/planet-mars -n planets -- curl localhost:8000/gossip
kubectl exec deploy/planet-jupiter -n planets -- curl localhost:8000/gossip

kubectl get jobs -n planets
