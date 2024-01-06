from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import UserCredentialsSerializer, UserSerializer
from .models import User

from emails.models import VerifyEmailLetter


class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)
        data = {"user": serializer.data, "tokens": serializer.get_tokens(user)}
        VerifyEmailLetter.objects.create(user=user).send()
        return Response(data=data)

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


class MyUserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user
