import json
import random
from datetime import datetime
from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

emotions = ["happy", "sad", "angry", "neutral"]
genders = ["male", "female", "other"]

def generate_random_data():
    return {
        "id": random.randint(1, 1000000),
        "age": random.randint(1, 100),
        "emotion": random.choice(emotions),
        "gender": random.choice(genders),
        "timestamp": datetime.now().isoformat()
    }

while True:
    data = generate_random_data()
    producer.send('face.embed.data', data)
    print(f"Sent: {data}")
    time.sleep(1)