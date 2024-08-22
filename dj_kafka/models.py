import uuid

from django.db import models


class FaceEmbed(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    emotion = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'face_embed'
        verbose_name = 'Face Embed'
        ordering = ['-timestamp']