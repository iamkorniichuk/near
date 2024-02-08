from rest_framework.viewsets import ModelViewSet

from commons.mixins import PopulateDataMixin
from profiles.permissions import IsOwnerOrReadOnly

from .serializers import EventSerializer
from .models import Event


class EventViewSet(PopulateDataMixin, ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_populated_data(self):
        return {"profile": self.request.user.profile.pk}

    def get_permissions(self):
        return super().get_permissions() + [IsOwnerOrReadOnly("profile")]
