from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import secrets

from .models import ConfirmationCode, ConfirmationCodeTypes
from .permissions import HasUnverifiedEmail
from . import send_mail

random = secrets.SystemRandom()


class VerifyEmailView(APIView):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated, HasUnverifiedEmail]

    def get(self, request):
        user = request.user

        confirmation_code, is_created = ConfirmationCode.objects.get_or_create(
            defaults={"code": generate_code()},
            user=user,
            type=ConfirmationCodeTypes.VERIFY_EMAIL,
        )

        if not is_created and confirmation_code.is_expired:
            confirmation_code.code = generate_code()
            confirmation_code.save()

        try:
            send_mail(
                "Email Verification",
                str(confirmation_code.code),
                recipient=user.email,
                fail_silently=False,
            )
            return Response(
                "Verification letter was sent to your email.", status.HTTP_200_OK
            )
        except ValueError as e:
            return Response(repr(e), status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        user = request.user
        code = request.data["code"]

        instance = ConfirmationCode.objects.get(
            user=user,
            type=ConfirmationCodeTypes.VERIFY_EMAIL,
        )
        if instance.is_expired:
            return Response(
                "Current code is expired. Generate a new one",
                status.HTTP_400_BAD_REQUEST,
            )
        if instance.code == code:
            user.is_email_verified = True
            user.save()
            return Response("Email is verified", status.HTTP_200_OK)

        return Response("Wrong code", status.HTTP_400_BAD_REQUEST)


def generate_code():
    return random.randint(100000, 999999)
