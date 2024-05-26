from fastapi import FastAPI
import random
import time

app = FastAPI()

@app.get("/random-data")
async def get_random_data():
    data = {
        "room_id": random.randint(1, 5),
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 60.0), 2),
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }
    return data
