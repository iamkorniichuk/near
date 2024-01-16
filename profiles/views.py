from rest_framework import generics
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import ProfileSerializer
from .models import Profile
from .permissions import HasProfile


class ProfileListView(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def create(self, request, *args, **kwargs):
        request.data["user"] = self.request.user.pk
        return super().create(request, *args, **kwargs)

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return super().get_permissions()


class ProfileDetailsView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class MyProfileDetailsView(generics.RetrieveUpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [HasProfile]

    def get_object(self):
        return self.request.user.profile
