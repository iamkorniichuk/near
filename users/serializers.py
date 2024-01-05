from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .models import User


class UserCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "tokens"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)
        data = {"refresh": str(refresh), "access": str(access)}
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["email", "password"]
