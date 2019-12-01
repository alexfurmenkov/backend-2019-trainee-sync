from django.db import models
from .base import BaseModel


class Follower(BaseModel):
    user_id = models.CharField(max_length=30)
    follower_id = models.CharField(max_length=30)
    subscription_flag = models.BooleanField()

    @staticmethod
    def create_follower(user_id, follower_id, subscription_flag):
<<<<<<< HEAD
        """
        Creates a Follower object and saves it to DB
        :return: Follower object
        """
=======
>>>>>>> master
        return Follower.objects.create(
            user_id=user_id,
            follower_id=follower_id,
            subscription_flag=subscription_flag,
        )
