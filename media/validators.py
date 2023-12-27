from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.utils.deconstruct import deconstructible

from typing import Iterable
import magic


@deconstructible
class MimeTypeValidator:
    """
    Check MIME type of file by reading its header.
    """

    def __init__(self, allowed: Iterable[str] = None, prohibited: Iterable[str] = None):
        if bool(allowed) ^ bool(prohibited):
            self.allowed = allowed
            self.prohibited = prohibited
        else:
            raise ImproperlyConfigured(
                "You need to pass either `allowed` or `prohibited` attribute."
            )

    def __call__(self, file):
        mime_type = magic.from_buffer(file.read(2048), mime=True)

        if bool(self.allowed):
            if mime_type not in self.allowed:
                raise ValidationError(
                    f"{file.name} MIME type is {mime_type}. Allowed types: {', '.join(self.allowed)}"
                )

        if bool(self.prohibited):
            if mime_type in self.prohibited:
                raise ValidationError(
                    f"{file.name} MIME type is {mime_type}. Prohibited types: {', '.join(self.prohibited)}"
                )

    def __eq__(self, other):
        return self.allowed == other.allowed and self.prohibited == other.prohibited
