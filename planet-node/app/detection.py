#stub
import random

def detect_asteroids(range_km: int):
    # Fake asteroid detection
    count = random.randint(0, 5)
    return [
        {"id": f"ast-{random.randint(1000,9999)}", "distance": random.randint(0, range_km)}
        for _ in range(count)
    ]