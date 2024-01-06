from django.contrib.gis.db import models
from django.core.mail import send_mail
from django.conf import settings
import secrets

from users.models import User


random = secrets.SystemRandom()


def generate_code():
    return random.randint(1000, 9999)


class VerifyEmailLetter(models.Model):
    user = models.OneToOneField(
        User,
        models.CASCADE,
        related_name="verify_email_letter",
    )
    sent = models.DateTimeField(auto_now=True)
    code = models.IntegerField(default=generate_code, editable=False)

    def send(self):
        return send_mail(
            "Confirmation",
            str(self.code),
            from_email=f"poriad <{settings.DEFAULT_FROM_EMAIL}>",
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def verify_email(self, code, delete_letter=True):
        is_verified = code == self.code

        if is_verified:
            self.user.is_email_verified = True
            self.user.save()

            if delete_letter:
                self.delete()

        return is_verified
