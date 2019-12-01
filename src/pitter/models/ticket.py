from __future__ import annotations

from django.db import models
from django.db.models import QuerySet

from pitter.models.base import BaseModel


class Ticket(BaseModel):
    fake_id = models.CharField(max_length=50, default='')
    message = models.CharField(max_length=256)
    user_comment = models.TextField()

    def to_dict(self) -> dict:
        """
        Creates a dictionary with a ticket properties
        :return: dictionary
        """
        return dict(
            id=self.id,
            fakeId=self.fake_id,
            message=self.message,
            userComment=self.user_comment,
        )

    @staticmethod
    def create_ticket(fake_id: str, message: str, user_comment: str) -> Ticket:
        """
        Creates a Ticket object and saves it into the DB
        :return: Ticket object
        """
        return Ticket.objects.create(
            fake_id=fake_id,
            message=message,
            user_comment=user_comment,
        )

    @staticmethod
    def get_tickets() -> QuerySet:
        """
        Used to find a Ticket object
        :return: Ticket object
        """
        return Ticket.objects.find().order_by('created_at')
