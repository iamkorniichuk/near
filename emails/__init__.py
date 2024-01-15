from django.core.mail import send_mail as django_send_mail
from django.conf import settings


def send_mail(
    subject,
    message,
    recipient,
    from_email=settings.DEFAULT_FROM_EMAIL,
    fail_silently=True,
):
    return (
        django_send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=[recipient],
            fail_silently=fail_silently,
        )
        != 0
    )
