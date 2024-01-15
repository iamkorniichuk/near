from django.contrib.gis.db import models
from django.conf import settings
from os import path

from users.models import User

DEFAULT_PICTURE = path.join(settings.DEFAULTS_MEDIA_URL, "profiles_picture")


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name="profile")
    name = models.CharField(max_length=32)
    picture = models.ImageField(
        upload_to="profiles/",
        default=DEFAULT_PICTURE,
    )

    def __str__(self):
        return self.name
