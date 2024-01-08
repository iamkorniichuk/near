from django.db.models import signals
from django.dispatch import receiver

from emails.managers import VerifyEmailLetterManager

from .models import User


@receiver(signals.post_save, sender=User)
def send_verify_email_letter_on_create(sender, instance, created, **kwargs):
    if created:
        VerifyEmailLetterManager(user=instance).send_letter()
