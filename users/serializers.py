from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    @classmethod
    def get_tokens(cls, user):
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        tokens = {"refresh": str(refresh), "access": str(access)}
        return tokens

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["email", "password"]
