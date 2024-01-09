from django.contrib.gis.db import models

from users.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name="profile")
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
