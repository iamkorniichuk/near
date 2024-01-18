from rest_framework import serializers

from .models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"
        extra_kwargs = {
            "content_type": {"write_only": True},
            "object_id": {"write_only": True},
        }
