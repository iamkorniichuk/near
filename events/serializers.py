from rest_framework import serializers

from media.serializers import MediaSerializer

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    media = MediaSerializer(many=True, read_only=True)
