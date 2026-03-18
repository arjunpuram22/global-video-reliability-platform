import requests
import time
import random

URL = "http://localhost:8000/upload"

for i in range(20):
    payload = {
        "video_id": f"vid-load-{i}",
        "duration": random.randint(60, 300),
        "quality": random.choice(["720p", "1080p", "4k"])
    }

    response = requests.post(URL, json=payload)
    print(f"Sent job {i}: {response.status_code} - {response.text}")

    time.sleep(1)
