from django.urls import path

from dj_kafka.api.views import FaceEmbedListView

urlpatterns = [
    path('face_embed/', FaceEmbedListView.as_view(), name='face_embed_list'),
]