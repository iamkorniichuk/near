from rest_framework import generics
from rest_framework import permissions

from .serializers import UserCredentialsSerializer, UserSerializer
from .models import User


class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserCredentialsSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return super().get_permissions()


class UserDetailsView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
