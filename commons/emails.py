from django.core.mail import send_mail
from django.db.models import Manager
from django.db.models.query import QuerySet


class EmailLetterManager:
    """
    Compose and send an email letter from a model instance.
    """

    def __init__(self, instance):
        self.instance = instance

    def get_instance(self):
        return self.instance

    def get_subject(self):
        return self.subject

    def get_message(self):
        return self.message

    def get_from_email(self):
        return self.from_email

    def get_recipient(self):
        return self.recipient

    def get_html_message(self):
        return self.html_message

    def send_letter(self):
        subject = self.get_subject()
        message = self.get_message()
        from_email = self.get_from_email()
        recipient = self.get_recipient()
        html_message = self.get_html_message()
        return send_mail(
            subject,
            message,
            from_email=from_email,
            recipient_list=[recipient],
            html_message=html_message,
            fail_silently=False,
        )


class CreateEmailModelMixin:
    queryset = None

    def __init__(self, **data):
        super().__init__(self.create_instance(**data))

    def create_instance(self, **data):
        instance = self.get_queryset().create(**data)
        return instance

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, (QuerySet, Manager)):
            queryset = queryset.all()
        return queryset
