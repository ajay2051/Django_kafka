from rest_framework import generics

from dj_kafka.api.serializers import FaceEmbedSerializer
from dj_kafka.models import FaceEmbed


class FaceEmbedListView(generics.ListAPIView):
    queryset = FaceEmbed.objects.all()
    serializer_class = FaceEmbedSerializer