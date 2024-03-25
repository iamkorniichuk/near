from rest_framework import serializers

from events.serializers import EventSerializer

from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

    event = EventSerializer()
