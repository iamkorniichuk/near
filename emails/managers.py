from django.conf import settings

from commons.emails import EmailSender

from .models import ConfirmationCode


class ConfirmationCodeSender(EmailSender):
    queryset = ConfirmationCode.objects.all()

    def get_subject(self):
        return "poriad: Email Verification"

    def get_message(self):
        instance = self.get_instance()
        return str(instance.code)

    def get_from_email(self):
        return f"poriad <{settings.DEFAULT_FROM_EMAIL}>"

    def get_recipient(self):
        instance = self.get_instance()
        return instance.user.email

    def get_html_message(self):
        return None
