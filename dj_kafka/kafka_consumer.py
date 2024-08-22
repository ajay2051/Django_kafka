import json

from django.utils import timezone
from kafka import KafkaConsumer

from .models import FaceEmbed

consumer = KafkaConsumer(
    'face.embed.data',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='face_embed_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def start_consuming():
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