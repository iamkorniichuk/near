from rest_framework.viewsets import ModelViewSet

from commons.mixins import PopulateDataMixin

from .serializers import PlaceSerializer
from .models import Place


class PlaceViewSet(PopulateDataMixin, ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

    def get_populated_data(self):
        return {"profile": self.request.user.profile.pk}
