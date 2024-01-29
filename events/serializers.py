from rest_framework import serializers

from commons.serializers import RepresentativePkRelatedField
from media.serializers import MediaSerializer
from profiles.serializers import ProfileSerializer
from profiles.models import Profile
from places.serializers import PlaceSerializer
from places.models import Place

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    place = RepresentativePkRelatedField(
        queryset=Place.objects.all(),
        serializer_class=PlaceSerializer,
    )
    profile = RepresentativePkRelatedField(
        queryset=Profile.objects.all(),
        serializer_class=ProfileSerializer,
    )
    media = MediaSerializer(many=True, read_only=True)
