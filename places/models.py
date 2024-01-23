from django.contrib.gis.db import models
from django.contrib.contenttypes.fields import GenericRelation

from profiles.models import Profile
from media.models import Media


class Place(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    location = models.PointField(srid=4326)
    profile = models.ForeignKey(Profile, models.CASCADE)
    media = GenericRelation(Media)

    def __str__(self):
        return self.name
