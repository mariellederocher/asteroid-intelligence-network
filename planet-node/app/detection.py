#stub
import random

def detect_asteroids(range_km: int):
    # Fake asteroid detection — always detect at least one
    count = random.randint(1, 5)
    # Fall back to a reasonable default max distance when range_km is unset or non-positive
    max_distance = range_km if range_km and range_km > 0 else 10000
    return [
        {"id": f"ast-{random.randint(1000,9999)}", "distance": random.randint(0, max_distance)}
        for _ in range(count)
    ]