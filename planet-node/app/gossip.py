import requests
import os

PLANET_NAME = os.getenv("PLANET_NAME")

# hardcoded for now
PEERS = [
    "http://planet-earth.planets.svc.cluster.local:8000",
    "http://planet-mars.planets.svc.cluster.local:8000",
    "http://planet-jupiter.planets.svc.cluster.local:8000",
]

def gossip_with_peers():
    updated = 0
    for peer in PEERS:
        if PLANET_NAME in peer:
            continue
        try: 
            res = requests.get(f"{peer}/asteroids")
            peer_data = res.json()
            updated += len(peer_data)
        except Exception:
            pass
    return updated