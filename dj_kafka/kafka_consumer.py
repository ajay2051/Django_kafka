import json
import time

from django.utils import timezone
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

from .models import FaceEmbed

while True:
    try:
        consumer = KafkaConsumer(
            'face.embed.data',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='face_embed_group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        print("Successfully connected to Kafka")
        break
    except NoBrokersAvailable:
        print("No brokers available. Retrying in 5 seconds...")
        time.sleep(5)


def start_consuming():
    """
    This function creates FaceEmbed object
    :return: None
    """
    for message in consumer:
        data = message.value
        FaceEmbed.objects.create(
            id=data['id'],
            age=data['age'],
            emotion=data['emotion'],
            gender=data['gender'],
            timestamp=timezone.now()
        )
        print(f"Saved: {data}")
