from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from .models import VerifyEmailLetter


class ConfirmCodeView(APIView):
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        user = request.user
        code = request.data["code"]

        letter = VerifyEmailLetter.objects.get(user=user)
        if letter.verify_email(code):
            return Response("Email is verified", status.HTTP_200_OK)

        return Response("Wrong code", status.HTTP_400_BAD_REQUEST)
