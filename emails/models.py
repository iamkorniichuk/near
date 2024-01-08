from django.contrib.gis.db import models
from django.db.models.lookups import GreaterThan
from django.utils.timezone import now
from django.conf import settings
import secrets

from users.models import User


random = secrets.SystemRandom()


class VerifyEmailLetterManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                is_expired=models.ExpressionWrapper(
                    GreaterThan(
                        lhs=now() - models.F("generated"),
                        rhs=settings.VERIFY_EMAIL_CODE_LIFETIME,
                    ),
                    output_field=models.BooleanField(),
                )
            )
        )

    def get(self, *args, **kwargs):
        instance = super().get(*args, **kwargs)
        if instance.is_expired:
            instance.save()
        return instance


class VerifyEmailLetter(models.Model):
    """
    To send email letters use a corresponding manager under `emails.managers` or create your own with `commons.emails.EmailManager`.
    """

    user = models.OneToOneField(
        User,
        models.CASCADE,
        related_name="verify_email_letter",
    )
    generated = models.DateTimeField(auto_now=True)
    code = models.IntegerField(editable=False)

    objects = VerifyEmailLetterManager()

    def save(self, *args, **kwargs):
        self.code = self.generate_code()
        return super().save(*args, **kwargs)

    def generate_code(self):
        return random.randint(1000, 9999)
