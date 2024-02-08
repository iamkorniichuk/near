from rest_framework.generics import RetrieveAPIView, ListCreateAPIView

from commons.mixins import PopulateCreateDataMixin, PopulateUpdateDataMixin

from .serializers import TicketSerializer
from .models import Ticket


class TicketListView(PopulateCreateDataMixin, ListCreateAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def get_populated_data(self):
        return {"profile": self.request.user.profile.pk}


class TicketDetailsView(PopulateUpdateDataMixin, RetrieveAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def get_populated_data(self):
        return {"profile": self.request.user.profile.pk}
