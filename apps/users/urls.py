from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import MyTokenObtainPairView, UserCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path("", UserCreateView.as_view(), name="user-create"),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("<pk>/", UserRetrieveUpdateDestroyView.as_view(), name="user-retrieve-update-destroy"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
