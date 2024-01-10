from rest_framework import generics

from .serializers import ProfileSerializer
from .models import Profile


class ProfileListView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def create(self, request, *args, **kwargs):
        request.data["user"] = self.request.user.pk
        return super().create(request, *args, **kwargs)

    def get_object(self):
        user = self.request.user
        self.check_object_permissions(self.request, user)
        return user


class ProfileDetailsView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class MyProfileDetailsView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        user = self.request.user
        self.check_object_permissions(self.request, user)
        return user
