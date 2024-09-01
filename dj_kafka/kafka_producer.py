import json
import random
import time
from datetime import datetime

from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Successfully connected to Kafka")
        break
    except NoBrokersAvailable:
        print("No brokers available. Retrying in 5 seconds...")
        time.sleep(5)

emotions = ["happy", "sad", "angry", "neutral"]
genders = ["male", "female", "other"]


def generate_random_data():
    """
    This function generates random data
    :return: Random model data
    """
    return {
        "id": random.randint(1, 1000000),
        "age": random.randint(1, 100),
        "emotion": random.choice(emotions),
        "gender": random.choice(genders),
        "timestamp": datetime.now().isoformat()
    }


while True:
    data = generate_random_data()
    future = producer.send('face.embed.data', data)
    try:
        record_metadata = future.get(timeout=10)
        print(f"Sent: {data}")
        print(f"Topic: {record_metadata.topic}")
        print(f"Partition: {record_metadata.partition}")
        print(f"Offset: {record_metadata.offset}")
    except Exception as e:
        print(f"Error sending message: {e}")
    time.sleep(1)
