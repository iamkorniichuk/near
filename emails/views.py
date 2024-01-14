from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import ConfirmationCode, ConfirmationCodeTypes


class ConfirmConfirmationCodeView(APIView):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
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
