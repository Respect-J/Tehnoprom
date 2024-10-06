from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserModel
from .serializers import CreateUserSerializer, CustomTokenObtainPairSerializer, UserSerializer
from .api import send_verification_sms
from random import randint
class UserCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        if "username" not in request.data:
            return Response({"message": "Username is required"}, status.HTTP_400_BAD_REQUEST)

        username = request.data["username"]

        if UserModel.objects.filter(username=username).first():
            return Response({"message": "User exists"}, status.HTTP_400_BAD_REQUEST)

        create_user_serializer = CreateUserSerializer(data=request.data)

        if not create_user_serializer.is_valid():
            return Response({"message": create_user_serializer.errors}, status.HTTP_400_BAD_REQUEST)

        try:

            create_user_serializer.save()
        except Exception as e:
            return Response({"message": str(e)}, status.HTTP_400_BAD_REQUEST)

        return Response({"username": create_user_serializer.data["username"]}, status.HTTP_201_CREATED)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response


class VerifyPhoneView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        verification_code = request.data.get("verification_code")

        user = UserModel.objects.filter(phone_number=phone_number).first()

        if user and user.verification_code == verification_code:
            user.is_phone_verified = True
            user.save()

            # Генерация JWT токенов
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                "refresh": str(refresh),
                "access": access_token,
                "user_id": user.id,
                "message": "Телефон подтверждён"
            }, status=status.HTTP_200_OK)

        return Response({"message": "Неверный код или телефон"}, status=status.HTTP_400_BAD_REQUEST)


class SendPasswordResetCodeView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")

        user = UserModel.objects.filter(phone_number=phone_number).first()

        if user:
            # Генерация нового кода для сброса пароля
            reset_code = str(randint(100000, 999999))
            user.verification_code = reset_code
            user.save()

            # Отправка кода через SMS
            send_verification_sms(user.phone_number, reset_code)
            return Response({"message": "Код для сброса пароля отправлен"}, status=status.HTTP_200_OK)

        return Response({"message": "Пользователь с таким номером телефона не найден"},
                        status=status.HTTP_404_NOT_FOUND)


class ResetPasswordView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        verification_code = request.data.get("verification_code")
        new_password = request.data.get("new_password")

        user = UserModel.objects.filter(phone_number=phone_number, verification_code=verification_code).first()

        if user:
            # Установка нового пароля
            user.set_password(new_password)
            user.verification_code = None  # Очистить код, чтобы его нельзя было использовать повторно
            user.save()
            return Response({"message": "Пароль успешно изменен"}, status=status.HTTP_200_OK)

        return Response({"message": "Неверный код или номер телефона"}, status=status.HTTP_400_BAD_REQUEST)