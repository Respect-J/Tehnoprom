from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import UserModel
from .serializers import CreateUserSerializer, CustomTokenObtainPairSerializer, UserSerializer


class UserCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        create_user_serializer = CreateUserSerializer(data=request.data)
        if UserModel.objects.filter(username=request.data["username"]).first():
            return Response({"message": "user exists"}, status.HTTP_400_BAD_REQUEST)

        if not create_user_serializer.is_valid():
            return Response({"message": create_user_serializer.error_messages}, status.HTTP_400_BAD_REQUEST)
        try:
            create_user_serializer.save()
        except Exception as e:
            return Response({"message": str(e)}, status.HTTP_400_BAD_REQUEST)
        return Response({"username": create_user_serializer.data["username"]}, status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = response.data.get("refresh")
        access = response.data.get("access")
        user_id = response.data.get("user_id")

        response.data = {
            "user_id": user_id,
            "access": access,
            "refresh": refresh,
        }

        return response
