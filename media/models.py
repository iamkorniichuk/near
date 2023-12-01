from django.contrib.gis.db import models

from .validators import MimeTypeValidator


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

    def __str__(self):
        return self.file.name
