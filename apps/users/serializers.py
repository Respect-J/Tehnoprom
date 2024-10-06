from random import randint

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .api import send_verification_sms
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "username", "mainimg", "created_at", "updated_at"]


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username", "password", "phone_number"]

    def validate_phone_number(self, value):
        if UserModel.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Пользователь с таким номером телефона уже существует.")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = UserModel(**validated_data)
        user.set_password(password)

        verification_code = str(randint(100000, 999999))
        user.verification_code = verification_code


        if send_verification_sms(user.phone_number, verification_code):
            user.save()
        else:
            raise serializers.ValidationError("Не удалось отправить SMS")

        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({"user_id": self.user.id})
        return data
