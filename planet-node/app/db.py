asteroid_store = {}

def save_asteroids(asteroids):
    for a in asteroids:
        asteroid_store[a["id"]] = a["distance"]

def get_all_asteroids():
    return [{"id": k, "distance": v} for k, v in asteroid_store.items()]