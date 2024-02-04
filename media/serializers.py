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


class MultipleMediaSerializer(serializers.Serializer):
    files = serializers.ListField(child=serializers.FileField())
    content_type = serializers.IntegerField(write_only=True)
    object_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        result = {"files": []}
        files = validated_data.pop("files")
        for i, file in enumerate(files):
            serializer = MediaSerializer(
                data={
                    "file": file,
                    "order": i,
                    **validated_data,
                }
            )
            serializer.is_valid(raise_exception=True)
            result["files"].append(serializer.create(serializer.validated_data))
        return result

    def to_representation(self, data):
        result = {"files": []}
        for obj in data["files"]:
            result["files"].append(MediaSerializer().to_representation(obj))
        return result


class SwaggerMultipleMediaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    files = serializers.ListField(child=serializers.FileField())
    model = serializers.CharField(write_only=True)
