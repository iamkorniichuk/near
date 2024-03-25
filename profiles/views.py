from rest_framework import generics
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser

from commons.mixins import PopulateCreateDataMixin, PopulateUpdateDataMixin

from .serializers import ProfileSerializer
from .models import Profile
from .permissions import HasProfile


class ProfileListView(PopulateCreateDataMixin, generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return super().get_permissions()

    def get_populated_data(self):
        return {"user": self.request.user.pk}


class ProfileDetailsView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class MyProfileDetailsView(PopulateUpdateDataMixin, generics.RetrieveUpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [HasProfile]

    def get_object(self):
        return self.request.user.profile

    def get_populated_data(self):
        return {"user": self.request.user.pk}
