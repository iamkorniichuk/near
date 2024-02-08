from django.contrib.gis.db import models

from events.models import Event
from profiles.models import Profile


class Ticket(models.Model):
    event = models.ForeignKey(Event, models.CASCADE)
    profile = models.ForeignKey(Profile, models.CASCADE)
    bought = models.DateTimeField(auto_now_add=True, editable=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{str(self.event)} - {str(self.profile)}"
