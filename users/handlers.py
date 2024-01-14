from django.db.models import signals
from django.dispatch import receiver
import secrets

from emails.managers import ConfirmationCodeSender

from .models import User


@receiver(signals.post_save, sender=User)
def send_confirmation_code_on_create(sender, instance, created, **kwargs):
    if created:
        ConfirmationCodeSender(
            user=instance, code=generate_code(), type="VE"
        ).send_letter()


random = secrets.SystemRandom()


def generate_code():
    return random.randint(1000, 9999)
