from rest_framework.viewsets import ModelViewSet

from .serializers import PlaceSerializer
from .models import Place


class PlaceViewSet(ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

    def create(self, request, *args, **kwargs):
        request.data["profile"] = self.request.user.profile.pk
        return super().create(request, *args, **kwargs)
