import requests
import random
import time

url = "http://localhost:8080/data"

while True:
    data = {
        "room_id": random.randint(1, 5),
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 60.0), 2),
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }
    response = requests.post(url, json=data)
    print(response.json())
    time.sleep(5)
