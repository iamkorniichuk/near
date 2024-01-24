from rest_framework import serializers

from media.serializers import MediaSerializer

from .models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"

    media = MediaSerializer(many=True, read_only=True)
