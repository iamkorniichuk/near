from rest_framework import generics
from rest_framework import permissions

from .serializers import UserSerializer
from .models import User


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]


class UserDetailsView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        user = self.request.user
        self.check_object_permissions(self.request, user)
        return user
