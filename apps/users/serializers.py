from rest_framework import serializers

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "username", "mainimg", "created_at", "updated_at"]


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, style={"input_type": "password"})

    class Meta:
        model = UserModel
        fields = ["username", "password"]

    def create(self, validated_data):
        user = UserModel(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user
