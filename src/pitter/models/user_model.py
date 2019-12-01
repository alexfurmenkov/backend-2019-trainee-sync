from django.db import models
from .base import BaseModel


class User(BaseModel):
    login = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    profile_name = models.CharField(max_length=32)
    email_address = models.CharField(max_length=128)
    email_notifications_mode = models.BooleanField()

    def to_dict(self) -> dict:
        """
        Creates a dictionary and returns it
        :return: dictionary
        """
        return dict(
            id=self.id,
            login=self.login,
            password=self.password,
            profile_name=self.profile_name,
            email_address=self.email_address,
            email_notifications_mode=self.email_notifications_mode,
        )

    @staticmethod
    def create_user(login, password, profile_name, email_address, email_notifications_mode):
        """
        Creates a user and saves it to DB
        :return: User object
        """
        return User.objects.create(
            login=login,
            password=password,
            profile_name=profile_name,
            email_address=email_address,
            email_notifications_mode=email_notifications_mode,
        )

