from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from .serializers import UserCredentialsSerializer
from .models import User


class CreateUserView(CreateAPIView):
    serializer_class = UserCredentialsSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
