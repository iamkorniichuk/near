from django.contrib.gis.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .validators import MimeTypeValidator


class Media(models.Model):
    class Meta:
        unique_together = [
            ["content_type", "object_id", "order"],
        ]

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
        limit_choices_to=models.Q(app_label="places", model="place")
        | models.Q(app_label="events", model="event"),
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.file.name
