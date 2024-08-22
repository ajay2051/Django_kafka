from rest_framework import serializers

from dj_kafka.models import FaceEmbed


class FaceEmbedSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for FaceEmbed
    """
    class Meta:
        model = FaceEmbed
        fields = ['id', 'age', 'emotion', 'gender', 'timestamp']