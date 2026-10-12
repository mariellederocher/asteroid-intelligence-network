import requests
import os

PLANET_NAME = os.getenv("PLANET_NAME", "unknown")

# hardcoded for now
PEERS = {
    "http://planet-earth-svc.planets.svc.cluster.local:80",
    "http://planet-mars-svc.planets.svc.cluster.local:80",
    "http://planet-jupiter-svc.planets.svc.cluster.local:80",
}

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