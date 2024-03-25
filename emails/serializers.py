from rest_framework import serializers


class ConfirmationCodeSerializer(serializers.Serializer):
    code = serializers.IntegerField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
