from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserModel
from .serializers import CreateUserSerializer, CustomTokenObtainPairSerializer, UserSerializer


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