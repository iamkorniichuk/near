from django.contrib.gis.db import models

from users.models import User


class Place(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    location = models.PointField(srid=4326)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return self.name
