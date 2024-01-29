from rest_framework import serializers

from commons.serializers import RepresentativePkRelatedField
from media.serializers import MediaSerializer
from profiles.serializers import ProfileSerializer
from profiles.models import Profile

from .models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"

    profile = RepresentativePkRelatedField(
        queryset=Profile.objects.all(),
        serializer_class=ProfileSerializer,
    )
    media = MediaSerializer(many=True, read_only=True)
