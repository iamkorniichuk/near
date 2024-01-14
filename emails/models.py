from django.contrib.gis.db import models
from django.db.models.lookups import GreaterThan
from django.utils.timezone import now
from django.conf import settings

from users.models import User


class ConfirmationCodeManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                is_expired=models.ExpressionWrapper(
                    GreaterThan(
                        lhs=now() - models.F("generated"),
                        rhs=settings.CONFIRMATION_CODE_LIFETIME,
                    ),
                    output_field=models.BooleanField(),
                )
            )
        )


class ConfirmationCodeTypes(models.TextChoices):
    VERIFY_EMAIL = "VE", "verify email"


class ConfirmationCode(models.Model):
    class Meta:
        unique_together = ["user", "type"]

    user = models.ForeignKey(
        User,
        models.CASCADE,
        related_name="confirmation_codes",
    )
    generated = models.DateTimeField(auto_now=True)
    code = models.IntegerField(editable=False)
    type = models.CharField(
        max_length=16,
        choices=ConfirmationCodeTypes.choices,
    )

    objects = ConfirmationCodeManager()
