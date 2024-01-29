from django.contrib.gis.db import models
from django.contrib.contenttypes.fields import GenericRelation

from profiles.models import Profile
from places.models import Place
from media.models import Media


class Event(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    datetime = models.DateTimeField()
    price = models.DecimalField(max_digits=19, decimal_places=4)
    place = models.ForeignKey(Place, models.CASCADE)
    profile = models.ForeignKey(Profile, models.CASCADE)
    media = GenericRelation(Media)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name
