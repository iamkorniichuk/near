from django.contrib.gis.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from operator import or_
from functools import reduce

from .validators import MimeTypeValidator

related_content_types = [
    {
        "app_label": "places",
        "model": "place",
    },
]


class Media(models.Model):
    file = models.FileField(
        upload_to="media/",
        validators=[
            MimeTypeValidator(
                allowed=[
                    "image/jpeg",
                    "image/png",
                    "video/mp4",
                    "video/mpeg",
                ]
            )
        ],
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=reduce(
            or_,
            [
                models.Q(
                    app_label=content_type["app_label"],
                    model=content_type["model"],
                )
                for content_type in related_content_types
            ],
        ),
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.file.name
