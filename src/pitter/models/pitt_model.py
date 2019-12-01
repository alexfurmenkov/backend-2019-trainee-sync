from django.db import models
from .base import BaseModel


class Pitt(BaseModel):
    user_id = models.CharField(max_length=256)
    audio_path = models.CharField(max_length=3000)
    audio_decoded = models.CharField(max_length=1000)

    @staticmethod
    def create_pitt(user_id, audio_path, audio_decoded):
        """
        Creates a Pitt object and saves it into the DB
        :return: Pitt object
        """
        return Pitt.objects.create(
            user_id=user_id,
            audio_path=audio_path,
            audio_decoded=audio_decoded,
        )
