from django.db import models
from .base import BaseModel


class Token(BaseModel):
    access_token = models.CharField(max_length=1024)

    @staticmethod
    def create_token(access_token):
        """
        Creates a Token object and saves it into the DB
        :return: Token object
        """
        return Token.objects.create(
            access_token=access_token,
        )
